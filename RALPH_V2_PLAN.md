# Ralph V2: Improved Improver — Architecture Plan

**Date**: 2026-04-23
**Status**: Draft for review
**Based on**: Code audit of `ralph_daemon.py`, `improver.py`, `ingestor.py`, `deep_research.py` + research into WINELL, KARMA, APOLLO, Karpathy's LLM Wiki, OpenScholar

---

## The Core Problem

Ralph spends most of its wall-clock time fetching papers (hourly ingest + 6h deep research) and getting rate-limited. Meanwhile the Improver — the only agent that actually improves pages — is starved:

- **83% of raw papers (572/691) are never referenced** by any wiki page
- **116 pages have `sources: []`** — the writer LLM gets told "No source papers available — use general knowledge"
- Nothing connects raw papers to the wiki pages that need them
- The writer → reviewer pipeline fails 2/3 pages on validation (frontmatter issues, now fixed)

The Improver doesn't need more papers. It needs to **discover and use the 691 papers already on disk**.

---

## Research-Informed Design Principles

From the literature on autonomous knowledge base curation:

| Paper / System | Key Insight for Ralph |
|---|---|
| **WINELL** (WWW 2026) | Section-aware editing: analyze article structure, define per-section criteria, then target edits. Their pipeline: *structure analysis → information seeking → fact aggregation → human-like edit generation*. |
| **KARMA** (NeurIPS 2025) | Nine specialized agents for entity discovery, relation extraction, schema alignment, conflict resolution. Multi-layer verification yields 83% correctness. Key: **separate discovery from integration**. |
| **APOLLO** (OpenReview) | Self-guided iterative editorial loop: retrieve → fact-check → structure → verify. Emphasis on **iterative refinement** not single-shot generation. |
| **Karpathy's LLM Wiki** | Three-layer architecture: raw/ (immutable sources) → wiki/ (curated) → schema. Three operations: **ingest, query, lint**. The "lint" step catches decay. |
| **OpenScholar** (Nature 2025) | 45M papers with retrieval → rerank → self-feedback loop. Citation-aware generation reduces hallucination. |

### Principles distilled

1. **Separate sourcing from writing** — A matcher finds relevant papers; the writer consumes them.
2. **Section-aware, not page-level** — Edit specific sections, not entire pages at once.
3. **Iterative refinement** — Multiple small passes beat one big rewrite.
4. **Verify against sources** — Every claim must trace to a cited paper.
5. **Lint continuously** — Catch contradictions, stale content, broken links between cycles.

---

## Proposed Architecture: Ralph V2 Agent Team

```
                    ┌──────────────┐
                    │   Scheduler  │  (ralph_daemon.py — simplified)
                    └──────┬───────┘
                           │
              ┌────────────┼────────────────┐
              ▼            ▼                ▼
      ┌──────────┐  ┌───────────┐  ┌──────────────┐
      │ Ingestor │  │  Matcher  │  │   Improver   │
      │ (daily)  │  │ (hourly)  │  │  (hourly)    │
      └──────────┘  └─────┬─────┘  │              │
                         │         │  ┌─────────┐ │
              ┌──────────┘         │  │ Writer  │ │
              ▼                    │  ├─────────┤ │
     ┌─────────────────┐          │  │Reviewer │ │
     │ raw/papers/      │◄────────┘  ├─────────┤ │
     │ (692 .md files)  │            │ Editor  │ │
     └─────────────────┘            └─────────┘ │
                                    └──────────────┘
                           ▼
              ┌────────────────────┐
              │  Linter (daily)    │
              └────────────────────┘
```

### New Agent: **Matcher** (the critical missing piece)

**Purpose**: Given a wiki page, find the most relevant raw papers on disk and attach them.

**How it works** (embedding-first pipeline):

1. **Embed** (one-time, then incremental)
   - Split all wiki pages and raw papers into sentences
   - Run through `embeddinggemma:latest` (768-dim, Ollama local)
   - Store in `meta/embeddings/` as `.npy` files with metadata index
   - 14K sentences × 768-dim = 28 MB, brute-force cosine search in 1.8s
   - Incremental: ~8s to embed new daily papers

2. **Match** (every cycle, fast — no LLM)
   - For each wiki page sentence, compute cosine similarity against all paper sentence embeddings
   - Aggregate sentence-level hits → paper-level relevance scores
   - Top-10 candidate papers per wiki page

3. **Evaluate** (LLM, cheap — one prompt per page)
   - Batch prompt: "Are these 10 papers relevant to page about X? Answer yes/no per paper."
   - LLM returns confirmed matches with relevance reason
   - Filters false positives from cosine similarity (~40% noise)

4. **Attach** (file I/O only)
   - Write confirmed papers to page's `sources:` frontmatter (top 5 max)
   - Log pages where no matches found → "needs external research" for DeepResearch

**Why embedding-first beats keyword matching**:
- "Whole-brain simulation" matches "large-scale brain network modeling" even with zero word overlap
- Sentence-level granularity: identifies WHICH section of a page is relevant to WHICH paper
- 1.8s for full search — no FAISS needed at this scale

**Schedule**: Full rebuild daily, incremental hourly, LLM evaluation hourly (before Improver).

**Why this matters**: The Improver's writer prompt currently says "No source papers available" for 116 pages. After the Matcher runs, those pages will have 3-5 relevant raw papers injected. The writer can then cite real sources instead of guessing.

### Improved Agent: **Improver** (split into sub-agents)

Instead of one monolithic `improve_page()`, split into a pipeline:

#### Sub-agent 1: **Writer**
- Receives: page content + matched sources (from Matcher)
- Produces: improved page draft with citations
- Key change: **section-aware editing** — instead of rewriting the whole page, identify the weakest section (shortest, placeholder text, no citations) and improve just that section
- This reduces token cost, reduces LLM hallucination, and makes review easier

#### Sub-agent 2: **Reviewer**
- Receives: original section + proposed edit
- Checks: factual claims vs sources, writing quality, placeholder removal
- Key change: **source-grounded verification** — "Does claim X appear in source Y?" rather than generic quality checks
- Outputs: PASS or structured feedback

#### Sub-agent 3: **Editor** (new)
- Receives: draft + reviewer feedback
- Makes targeted fixes based on reviewer feedback
- Applies mechanical fixes (frontmatter, date, wikilinks) programmatically — no LLM needed
- Validates and writes the final page

**Why separate Editor from Writer**: Currently the Writer is called again for revisions, which is expensive and often drops frontmatter. The Editor handles the deterministic fixes (frontmatter, dates) and only calls the LLM for substantive revision.

### Changed Agent: **Ingestor**

- **Daily + startup** instead of hourly (TVB is niche — ~5-10 new papers/week)
- On startup: full fetch. After that: once per 24h.
- `since_date` covers the full gap since last run, so nothing is missed.

### Changed Agent: **DeepResearch**

- **2× per week** instead of every 6 hours
- Focused on gap-filling: only runs when Matcher reports pages that still have `sources: []` after matching
- Uses citation chaining from already-linked papers (follow references of papers already cited in wiki pages)

### New Agent: **Linter** (replaces parts of Auditor)

Daily health checks inspired by Karpathy's LLM Wiki "lint" concept:
- Contradiction detection between pages
- Staleness scoring (pages not updated in N days)
- Broken wikilinks
- Orphan pages (no incoming links)
- Source drift (cited papers that have newer versions/corrections)

---

## Implementation: Phase Plan

### Phase 1: Embedding Matcher (highest impact, ~350 lines)

New file: `scripts/matcher.py`

```python
def build_embedding_index():
    """One-time: embed all wiki sentences + raw paper sentences. Store to disk."""
    # 1. Extract sentences from all wiki pages and raw papers
    # 2. Batch-embed through Ollama (500 at a time, ~15 min total)
    # 3. Save embeddings.npy + metadata.json to meta/embeddings/
    # Total: 14K sentences × 768-dim = 28 MB
    pass

def update_embedding_index(new_files: list[str]):
    """Incremental: embed only new/changed files. ~8s for 5 new papers."""
    pass

def match_papers_to_page(slug: str, filepath: str) -> list[str]:
    """Find relevant raw papers for a wiki page using embedding similarity."""
    # 1. Load page sentence embeddings from index
    # 2. Cosine similarity against all paper sentence embeddings (1.8s full scan)
    # 3. Aggregate sentence hits → paper-level scores
    # 4. Return top-10 candidate paper paths
    pass

def evaluate_matches(slug: str, candidates: list[dict]) -> list[str]:
    """LLM evaluates: are these papers actually relevant? Returns confirmed paths."""
    # One prompt: "Page is about X. Are papers 1-10 relevant? yes/no + reason"
    # Returns only confirmed matches (typically 3-5)
    pass

def run_matcher_cycle():
    """Run matcher for all pages with sources: []. Returns pages matched."""
    pass
```

### Phase 2: Section-Aware Writer + Dedicated Editor (~150 lines changed)

Modify `improver.py`:
- `build_writer_prompt()` targets the weakest section, not the whole page
- Sources now come from Matcher output (embedding-confirmed papers)
- New `_apply_mechanical_fixes()` handles frontmatter, dates, wikilinks without LLM
- Reviewer prompt includes specific source-checking instructions
- Editor sub-agent handles revision + validation

### Phase 3: Cross-Page Link Discovery (bonus from embeddings)

The sentence-level embeddings enable a free bonus:
- For each wiki page sentence, find nearest sentences from OTHER wiki pages
- These are high-quality wikilink suggestions: "This sentence about neural mass models
  is semantically similar to this sentence on the Jansen-Rit page → suggest [[jansen-rit]]"
- Feed to Linter as automated cross-linking suggestions
- ~50 lines on top of the embedding index

### Phase 4: Linter Agent (replaces Auditor subset)

Extract linting from `auditor.py` into a focused daily agent:
- Contradiction detection
- Cross-page consistency checks
- Staleness tracking
- Feed results to Improver as a priority queue

---

## Revised Schedule

| Agent | Current | Proposed | Rationale |
|-------|---------|----------|-----------|
| Ingestor | hourly | **daily + startup** | Niche field, 5-10 papers/week |
| Matcher | *doesn't exist* | **daily** (full) + **hourly** (eval only) | Embedding search is 1.8s, LLM eval is one prompt/page |
| Improver | hourly | **hourly** (after Matcher) | Now has real sources to work with |
| DeepResearch | 6h | **2×/week** + on-demand | Only when Matcher reports empty pages |
| Auditor | daily | daily | Unchanged |
| Linter | *doesn't exist* | **daily** | New — catches decay |
| Librarian | daily | daily | Unchanged |
| SoftwareMapper | weekly | weekly | Unchanged |

---

## Expected Impact

| Metric | Current | After Phase 1-2 |
|--------|---------|-----------------|
| Pages with `sources: []` | 116 (53%) | < 20 (9%) |
| Raw papers referenced | 119 (17%) | 400+ (58%) |
| Improver success rate | ~33% (1/3 in log) | > 70% |
| Time spent on API fetching | ~30 min/cycle | ~5 min/day |
| Time spent on page improvement | ~10 min/cycle | ~50 min/cycle |

The key insight: **Ralph's bottleneck isn't fetching — it's connecting what it already has to what needs it.**

---

## Open Questions

1. **Embedding model choice: `embeddinggemma` (local, 768d) vs something smaller/faster?**
   - Current: `embeddinggemma:latest` at ~15 sentences/sec batched. 15 min initial build is fine.
   - Alternative: `bge-small-en` via sentence-transformers (384d, faster). But requires another dependency.
   - Recommendation: stick with Ollama/embeddinggemma since it's already running.

2. **Sentence-level vs paragraph-level embedding?**
   - Sentences give better granularity for cross-linking (Phase 3) but more vectors (14K).
   - Paragraphs would be ~3K vectors but lose precision.
   - Recommendation: sentences for first pass. Can always merge later.

3. **Should section-aware editing replace whole-page editing entirely?**
   - Recommendation: section-aware for pages with score > 40, full rewrite for score < 40 (stub/placeholder pages need a full rewrite).

4. **Should the Editor sub-agent be a separate `pi` call or inline Python?**
   - Recommendation: inline Python for mechanical fixes (frontmatter, dates, wikilinks). Only call `pi` for substantive revisions requested by the reviewer. Saves ~50% of LLM calls.

5. **Should we add a human-in-the-loop gate?**
   - Recommendation: optional `--dry-run` mode that writes to `meta/staged/` for human review before committing. Default: autonomous.
