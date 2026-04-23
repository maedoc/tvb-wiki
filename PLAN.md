# TVB-Wiki Autonomous Improvement Plan

> "The wiki at month 6 is substantially richer than at day 1 — not just more pages, but better connections, fewer stale claims, and a usage-informed authority graph that knows which pages matter." — llm-wiki README

## What We Want

An autonomous "Ralph" loop — a long-running script you start in a terminal (or tmux/screen) and monitor. Not cron, not systemd — just `python3 scripts/ralph_daemon.py` and it loops internally with sleep timers between cycles. You watch the output, you Ctrl+C when you want, you restart when you want.

It continuously:

1. **Ingests** new reputable academic sources related to TVB and whole-brain modeling
2. **Improves** existing pages: better explanations, richer cross-links, stronger references
3. **Maps** the software ecosystem: which tools exist, how they relate, which papers describe them
4. **Builds** Scholarpedia-quality pages that compound over time

## Landscape: What Others Have Built

We're not inventing this from scratch. Several systems tackle the same problem:

### Karpathy's LLM Wiki Pattern (Apr 2026)
The original. Three core operations on a flat markdown wiki:
- **Ingest**: Drop a source → LLM reads it, extracts key ideas, updates relevant pages across the wiki, logs the addition
- **Query**: Ask questions → LLM synthesizes from pre-built wiki pages (not raw sources). Good answers get filed back as `type: synthesis` pages
- **Lint**: Periodic health check → surface contradictions, stale claims, orphaned pages, gaps

Key insight: **The schema (AGENTS.md) is the most important file** — it's the system prompt that turns a generic LLM into a disciplined wiki maintainer.

### llm-wiki (Labhund/llm-wiki)
Production implementation of Karpathy's pattern. Ships a daemon with four background agents:

| Agent | Role | Scope |
|-------|------|-------|
| **Auditor** | Structural integrity: orphaned pages, broken wikilinks, missing citations, drift | Background, read-only |
| **Compliance** | Debounced on edits: checks new content for citation and structural issues | Background, read-only |
| **Librarian** | Usage-driven: refines tags/summaries, scores page authority from link graph + usage patterns | Background, read-only |
| **Adversary** | Claim verification: samples claims, fetches cited source, verifies via LLM | Background, read-only |

Critical design rule: **Background workers never edit page body content.** They only write frontmatter metadata and issue queues. Only supervised/interactive agents write prose. Provenance via git commit trailers: `Agent: researcher-3`.

### llm-wiki-compiler (atomicmemory)
CLI tool: `llmwiki ingest <url>`, `llmwiki compile`, `llmwiki query "..."`, `llmwiki lint`. Ships an MCP server. Has semantic search via embeddings. Incremental compilation — only recompiles changed sources.

### AgentWiki (agentwiki.org)
Fully autonomous: every morning pulls ~40 AI newsletters → DSPy/Haiku pipeline extracts concepts/entities/comparisons → writes pages or merges into existing ones → cross-links via embeddings → enriches thin pages to 1500-3000 word articles → publishes daily digest. GEPA-optimized prompts (87.4% writer quality).

### WINELL (arXiv:2508.03728)
Multi-agent framework for updating Wikipedia articles. Three agents: **Navigator** searches for online sources, **Extractor** pulls updates, **Aggregator** consolidates and deduplicates. Trains a fine-grained editing model on Wikipedia's edit history.

### BrainDB (beckfexx/BrainDB)
Local-first SQLite memory system. 3-layer memory (raw → indexed → entity graph), contradiction detection, nightly self-learning (validates memories against web via SearXNG), knowledge graph with entity/relation extraction.

### NELL (CMU, 2010-2018)
The OG never-ending learner. Ran 24/7 for 8 years. Key loop: read web → extract beliefs → populate KB → retrain itself → read better tomorrow. 120M beliefs accumulated. The lesson: **compounding requires self-improvement of the reader, not just accumulation of the read.**

---

## The Plan: TVB-Wiki Ralph Loop

### Design Principles (borrowed from the landscape)

1. **Raw is immutable.** Papers in `raw/papers/` are never edited once written. Wiki pages in `entities/`, `concepts/`, `comparisons/` are the mutable synthesis layer that cites raw.
2. **Background agents are read-only on prose.** They flag issues, update frontmatter, write to talk/issue queues. Only supervised passes edit page bodies.
3. **Every claim cites its source.** No orphan assertions. Wikilinks to `raw/papers/` or explicit references.
4. **Knowledge compounds.** Each ingestion builds on what's already there — new pages cross-reference existing ones, existing pages get updated with new findings.
5. **Provenance via git.** Every commit attributed to the agent that made it. `git log` is the audit trail.
6. **Two models, writer-reviewer dynamic.** Different models catch different errors. Disagreement is signal, not noise.

### Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                       Ralph Daemon                           │
│                                                              │
│  ┌──────────┐  ┌────────────────────────────┐  ┌──────────┐ │
│  │ Ingestor │  │  Writer-Reviewer Pipeline   │  │ Auditor  │ │
│  │ (hourly) │  │                            │  │ (daily)  │ │
│  │  Python  │  │  ┌──────────┐ ┌──────────┐ │  │  Python  │ │
│  │  only    │  │  │ Writer   │ │ Reviewer │ │  │  only    │ │
│  │          │  │  │ kimi-k2.6│ │ glm-5.1  │ │  │          │ │
│  └────┬─────┘  │  │(ollama)  │ │ (zai)    │ │  └────┬─────┘ │
│       │        │  └────┬─────┘ └────┬─────┘ │       │       │
│       │        │       │            │        │       │       │
│       │        │       └─────┬──────┘        │       │       │
│       │        │             │ merge/review  │       │       │
│       │        └─────────────┼───────────────┘       │       │
│       │                      │                       │       │
│  ┌────▼──────────────────────▼───────────────────────▼───┐   │
│  │              Shared Wiki State                        │   │
│  │                                                       │   │
│  │  raw/papers/     entities/      concepts/            │   │
│  │  (immutable)     (software,     (methods,            │   │
│  │                   people,         models,            │   │
│  │                   datasets)       modalities)        │   │
│  │                                                       │   │
│  │  comparisons/    meta/           log.md              │   │
│  │  (side-by-side)  (lint,counts)  (audit trail)        │   │
│  └───────────────────────────────────────────────────────┘   │
│       │                                                      │
│  ┌────▼─────┐                                                │
│  │  Git +   │  →  GitHub Pages (mkdocs build)                │
│  │  Deploy  │                                                │
│  └──────────┘                                                │
└──────────────────────────────────────────────────────────────┘

Agents by execution model:

  Python-only (no LLM):        LLM via pi subshell:
  ─────────────────────         ────────────────────
  Ingestor (hourly)             Improver/Writer (hourly, kimi-k2.6)
  Auditor (daily)               Improver/Reviewer (hourly, glm-5.1)
  Librarian (daily)             Software Mapper (weekly, alternating)
```
│  ┌────▼──────────────▼─────────────▼──────────────▼───┐ │
│  │              Shared Wiki State                      │ │
│  │                                                     │ │
│  │  raw/papers/     entities/      concepts/          │ │
│  │  (immutable)     (software,     (methods,          │ │
│  │                   people,         models,          │ │
│  │                   datasets)       modalities)      │ │
│  │                                                     │ │
│  │  comparisons/    meta/           log.md             │ │
│  │  (side-by-side)  (lint,counts)  (audit trail)      │ │
│  └─────────────────────────────────────────────────────┘ │
│       │                                                  │
│  ┌────▼─────┐                                            │
│  │  Git +   │  →  GitHub Pages (mkdocs build)            │
│  │  Deploy  │                                            │
│  └──────────┘                                            │
└─────────────────────────────────────────────────────────┘
```

### Parallelism Map

Where subagents can fan out:

| Agent | Parallelizable work | How many parallel? | Constraint |
|-------|--------------------|--------------------|------------|
| **Ingestor** | Fetching from different sources | 5 sources at once | API rate limits per source |
| **Ingestor** | Saving + extracting entities per paper | All papers at once | Disk I/O (trivial) |
| **Improver** | Writing improvements to N pages | 5-10 pages at once | ollama concurrency (kimi-k2.6 is local) |
| **Improver** | Reviewing N edits | 5-10 at once | zai rate limits (glm-5.1 is cloud) |
| **Auditor** | Per-page checks | All pages at once | Pure Python, already fast, no need |
| **Librarian** | Per-page tag/summary updates | 5-10 at once | Needs full index first (sequential) |
| **Software Mapper** | Creating pages for N missing tools | All at once | LLM throughput |
| **Software Mapper** | Reviewing N new pages | All at once | zai rate limits |

The big win is the **Improver doing 5-10 pages per cycle instead of 1**.

```
                    ┌─ pi (kimi-k2.6) ─── improve page A ─┐
                    ├─ pi (kimi-k2.6) ─── improve page B ─┤
  priority queue    ├─ pi (kimi-k2.6) ─── improve page C ─┼─→ git commits
  of 50 pages ──→   ├─ pi (kimi-k2.6) ─── improve page D ─┤
  pick worst 10     ├─ pi (kimi-k2.6) ─── improve page E ─┤
                    ├─ pi (kimi-k2.6) ─── improve page F ─┤
                    ├─ pi (kimi-k2.6) ─── improve page G ─┤
                    ├─ pi (kimi-k2.6) ─── improve page H ─┤
                    ├─ pi (kimi-k2.6) ─── improve page I ─┤
                    └─ pi (kimi-k2.6) ─── improve page J ─┘
                                       ~2-5 min each
                                       all running concurrently

                    ┌─ pi (glm-5.1) ─── review edit A ─┐
                    ├─ pi (glm-5.1) ─── review edit B ─┤
  then review ──→   ├─ pi (glm-5.1) ─── review edit C ─┼─→ accept/revise/reject
  all 10 edits      ├─ ...                              │
                    └─ pi (glm-5.1) ─── review edit J ─┘
```

Key constraint: **ollama runs locally**, so parallel pi subshells all hit the same local GPU.
- If kimi-k2.6 fits in VRAM: ollama queues requests sequentially anyway (no real parallelism for the LLM call itself, but you get parallel I/O — one subshell reads files while another is generating)
- If you have enough VRAM or multiple GPUs: true parallel inference
- The real parallelism win is with **zai/glm-5.1** (cloud) — those are truly independent HTTP calls

Practical defaults:
```python
PARALLEL_WRITERS = 3    # ollama concurrency (conservative for single GPU)
PARALLEL_REVIEWERS = 5  # zai concurrency (cloud, more headroom)
PARALLEL_INGESTORS = 5  # API fetches (arXiv, Semantic Scholar, etc.)
```

**What it does:** Finds and ingests new academic sources.

**Sources to monitor:**

| Source | Method | API | Quality |
|--------|--------|-----|---------|
| arXiv | `export.arxiv.org/api/query` | Free, no key | Preprints — verify before citing as established |
| PubMed | `eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi` | Free | Peer-reviewed biomedical |
| Semantic Scholar | `api.semanticscholar.org/graph/v1` | Free tier (100 req/s) | Good metadata, citations |
| OpenAlex | `api.openalex.org` | Free, open | Comprehensive coverage, institutional metadata |
| bioRxiv | `api.biorxiv.org` | Free | Preprints in neuroscience |
| Google Scholar | Scraping via SerpAPI or manual | Paid | Highest coverage but rate-limited |
| DBLP | `dblp.org/search/publ/api` | Free | Computer science, some comp-neuro |

**Search queries (TVB-scoped):**

```python
QUERIES = [
    # Direct TVB
    '"The Virtual Brain"',
    'TVB AND (connectome OR whole-brain)',
    
    # Neural mass models (TVB's core)
    '"neural mass model" AND (connectome OR whole-brain)',
    '"Wilson-Cowan" AND (brain OR cortical)',
    '"Jansen-Rit"',
    '"Epileptor" AND (seizure OR epilepsy)',
    '"Wong-Wang" AND (decision OR whole-brain)',
    '"Larter-Breakspear"',
    '"Stefanescu-Jirsa"',
    '"mean-field" AND (cortical OR brain)',
    
    # Connectomics
    '"structural connectivity" AND (DTI OR tractography OR connectome)',
    '"functional connectivity" AND (resting-state OR fMRI)',
    '"effective connectivity" AND (DCM OR dynamic causal)',
    
    # Whole-brain modeling
    '"whole-brain model" OR "whole brain simulation"',
    '"brain network" AND (simulation OR modeling)',
    '"personalized brain"',
    
    # Software ecosystem
    'NEST AND (spiking AND brain)',
    'NEURON AND (simulation AND neuron)',
    '"dynamic causal modeling" AND SPM',
    
    # Applications
    'epilepsy AND (modeling OR simulation) AND (brain OR cortical)',
    '"resting-state" AND (bifurcation OR dynamics)',
    '"connectome" AND (aging OR development)',
]
```

**Ingestor pipeline (per paper):**

```
1. Fetch metadata (title, authors, year, venue, DOI, abstract)
2. Check if already in raw/papers/ (by DOI or title hash) → skip if exists
3. Write to raw/papers/<slug>.md (immutable from here on)
4. Extract entities mentioned (software tools, people, methods, datasets)
5. Extract concepts mentioned (models, modalities, theories)
6. Determine which existing wiki pages should be updated
7. For each relevant existing page: add the paper to its `sources:` frontmatter
8. For each new entity/concept that appears ≥2 times across papers: create stub page
9. Update meta/entity_counts.json
10. Update index.md
11. Log to log.md
12. Git commit with message: "Ingest: <paper-slug> (Ingestor)"
```

**Parallelism:** Fetch all 5 sources concurrently (subprocesses). Save + extract per paper concurrently. The entire ingest cycle that currently runs sequentially through arXiv queries with `time.sleep(1)` between them becomes 5 parallel fetchers.

**Implementation:** Rewrite `scripts/hourly_update.py` — currently uses 10 arXiv-only queries. Extend to multi-source. Keep the existing keyword extraction but expand `KEYWORD_MAP` to cover the full TVB ecosystem.

### Agent 2: Improver — Writer-Reviewer Pipeline (runs hourly, after Ingestor)

**What it does:** Picks N pages that need work and improves them in parallel through a two-model pipeline.

Two models work together: **kimi-k2.6** (ollama, local, fast) writes, **glm-5.1** (zai, cloud, different training) reviews. The disagreement between them is the quality signal.

**Improver cycle (parallel version):**

```
1. [Python] Build a priority queue of pages needing improvement
   - Pages with *Placeholder* text → CRITICAL
   - Pages under 200 words → HIGH
   - Pages with no wikilinks → HIGH
   - Pages with < 2 references → MEDIUM
   - Pages not updated in 30+ days → LOW
   - New stub pages from Ingestor → HIGH
   
2. [Python] Pick top N pages (default: 3 writers, configurable)

3. [PARALLEL] Spawn N pi subshells with kimi-k2.6, each improving one page:
   pi --model ollama/kimi-k2.6 --no-session -p "Read SCHEMA.md. Improve <page>. ..."
   Each subshell independently reads, edits, and writes its page.
   Wait for all N to complete (timeout per subshell: 300s).
   → Produces edits A1, A2, ..., AN

4. [PARALLEL] Spawn N pi subshells with glm-5.1, each reviewing one edit:
   pi --model zai/glm-5.1 --no-session --tools read -p "Review this edit. ..."
   Reviewer gets original + edited version, checks for errors.
   → Produces reviews B1, B2, ..., BN

5. [Python] For each page where review flagged issues:
   Re-spawn with kimi-k2.6 to revise (sequential or small parallel batch)
   → Produces revised edits

6. [Python] Validate all final edits:
   - All new claims cite a source in raw/papers/
   - New wikilinks point to existing pages
   - Frontmatter updated
   - No placeholder text introduced
   
7. Git commit each page: "Improve <page>: <what changed> (Writer:kimi-k2.6 Reviewer:glm-5.1)"
```

**Why this is safe in parallel:**
- Each pi subshell edits exactly ONE file
- No two subshells touch the same page
- Git commits are serialized by the daemon (sequential `git add && git commit`)
- Validation happens after all edits are in, before any commit

**Parallelism tuning:**
```python
PARALLEL_WRITERS = 3    # ollama/kimi-k2.6 — conservative for single GPU
PARALLEL_REVIEWERS = 5  # zai/glm-5.1 — cloud, more headroom
# With a beefier GPU or multi-GPU:
# PARALLEL_WRITERS = 10
```

**Content quality standards (Scholarpedia-level):**

Each page should eventually reach this structure:

```markdown
---
title: <Name>
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity|concept
tags: [...]
sources: [raw/papers/xxx.md, ...]
trust: verified|accepted|draft
---

# <Title>

## Overview
2-3 paragraph summary. Accessible to a neuroscience grad student.

## Mathematical Formulation (for models)
Equations with variable definitions. Links to related models.

## Key Properties
Bulleted list of important properties/results.

## Applications in TVB
How this is used within The Virtual Brain ecosystem specifically.

## Relationship to Other <Concepts|Software>
- [[related-thing-1]] — brief note on relationship
- [[related-thing-2]] — brief note on relationship

## Software Implementations (for concepts)
Which tools implement this: [[TVB]], [[NEST]], etc.

## References
(Auto-generated from sources: frontmatter by obsidian_support.py hook)
```

**Implementation:** This replaces the missing `pick_random_page.py` + prose-based improvement steps from the old cronjobs.md. Should be a Python script that:
- Scores all pages by quality metrics
- Picks the worst page
- Writes a detailed prompt for the LLM including: the page content, relevant raw papers, the wiki schema, and improvement instructions
- The LLM returns the updated page
- Script validates and commits

### Agent 3: Auditor (runs daily, 03:00 UTC)

**What it does:** Structural integrity check.

Already partially exists in `scripts/daily_lint.py`. Extend it:

```
1. Broken wikilinks (exists — keep)
2. Orphan pages with no inbound links (exists — keep)
3. Pages missing from index.md (exists — keep)
4. NEW: Pages with placeholder text still present
5. NEW: Pages with no sources/references
6. NEW: Pages not updated in 60+ days (stale)
7. NEW: Duplicate/overlapping pages (e.g., dti.md vs diffusion-mri.md)
8. NEW: Broken references (sources: pointing to non-existent raw papers)
9. NEW: Inconsistent frontmatter (missing fields, wrong type)
10. NEW: Cross-reference consistency (if A links to B, does B mention A?)
```

Output goes to `meta/audit-report.json` (machine-readable) and `meta/lint.log` (human-readable). The Improver reads the audit report to prioritize its work.

### Agent 4: Librarian (runs daily, 06:00 UTC)

**What it does:** Metadata and cross-reference maintenance.

```
1. Regenerate index.md with current summaries
2. Rebuild link graph: for each page, ensure "Related" sections link back
3. Score page authority: pages cited by many other pages get higher authority
4. Ensure See Also / Related sections are symmetric (if A→B then B→A)
5. Update concept page tag consistency
6. For software entities: ensure they list which papers describe them
7. For people entities: ensure they list which software/tools they created
8. Write meta/page_authority.json
```

### Agent 5: Software Mapper (runs weekly)

**What it does:** Builds and maintains the software ecosystem map.

This is the agent you specifically asked for — mapping software, how it works, which papers it's related to.

**Two-model approach:** Each model independently identifies gaps, then results are merged. Different models will know about different tools and make different connections.

```
1. [pi --model ollama/kimi-k2.6] "Scan all entity pages in this wiki. 
   List every software tool related to TVB/whole-brain modeling that's MISSING." 
   → Gap list A

2. [pi --model zai/glm-5.1] Same prompt.
   → Gap list B

3. [Python] Union of A and B → comprehensive gap list

4. For each missing tool, [pi --model ollama/kimi-k2.6] creates the page
   (writer, since this is bulk creation)

5. [pi --model zai/glm-5.1] reviews the new pages for accuracy
```

**Software to cover:**

| Category | Tools |
|----------|-------|
| Whole-brain simulation | **TVB**, The Virtual Epileptic Brain |
| Spiking simulation | **NEST**, **NEURON**, Brian, BRIAN2, Arbor, CoreNEURON |
| Neural mass models | TVB (built-in), DynaSim, SPM (neural mass module) |
| Neuroimaging processing | **ANTs**, **FreeSurfer**, FSL, SPM, MRtrix3, DSI Studio |
| Connectivity analysis | **GraphVar**, Brain Connectivity Toolbox, Nilearn, CONN |
| EEG/MEG analysis | FieldTrip, MNE-Python, EEGLAB, Brainstorm |
| Dynamic Causal Modeling | **SPM/DCM**, TVB-DCM integration |
| Atlases & parcellations | AAL, Desikan-Killiany, Destrieux, HCP-MMP1.0, Schaefer, Brainnetome |
| Databases | **ModelDB**, NeuroMorpho.Org, Allen Brain Atlas, OpenNeuro, Human Connectome Project |
| Visualization | ITK-SNAP, ParaView, TVB Web Interface |

**For each software tool, the mapper ensures:**

1. Entity page exists with proper frontmatter
2. Key papers linked (the original paper, major version papers)
3. Relationship to TVB explicitly stated (used together? alternative? complementary?)
4. Comparison pages exist for closely related tools (TVB vs NEST, ANTs vs FSL, etc.)
5. Cross-links to all concept pages relevant to that tool

**Output:** Updated entity pages + a new `comparisons/software-ecosystem.md` page that's a comprehensive map.

### No Reporter Agent — Git Log Is the Report

Every agent writes structured git commits and appends to `log.md`. When you want a summary:

```bash
# What happened today
git log --since="24 hours ago" --oneline

# What the Improver has been doing
git log --grep="Improver" --oneline

# Full narrative
less log.md
```

Commit message convention: `"<verb>: <what> (<Agent>)"`
- `Ingest: jirsa-2026-propagation (Ingestor)`
- `Improve epileptor: added formulation section (Improver)`
- `Audit: 12 broken links, 4 orphans (Auditor)`
- `Librarian: rebuilt index, 3 symmetric links added (Librarian)`
- `Map: created fieldtrip.md, mne-python.md (SoftwareMapper)`

This keeps the audit trail in git where it belongs, no extra agent needed.

---

## Implementation Roadmap

### Phase 1: Fix What's Broken (1-2 days)

Get the existing automation working end-to-end:

1. **Create `scripts/pick_random_page.py`** — score pages, pick worst one, output path + issues
3. **Fix hardcoded paths** in `daily_lint.py` and `hourly_update.py` (use `__file__`-relative)
4. **Test the full pipeline manually**: `hourly_update.py` → `sync_to_docs.py` → `mkdocs build` → git commit
5. **Write the wiki SCHEMA.md** — the single most important file (per Karpathy). This is the system prompt that tells the LLM what the wiki is, what conventions to follow, what quality looks like.

### Phase 2: Multi-Source Ingestor (3-5 days)

Extend `hourly_update.py` beyond arXiv:

1. Add Semantic Scholar API client (free, good citation data)
2. Add PubMed client (peer-reviewed filter)
3. Add OpenAlex client (institutional metadata)
4. Expand `KEYWORD_MAP` to cover the full TVB ecosystem
5. Add DOI-based deduplication across sources
6. Add trust/quality scoring per source (peer-reviewed > preprint > blog)
7. Write `raw/papers/` with richer metadata (citations, cited-by count, h-index of first author)

### Phase 3: The Improver Agent (3-5 days)

Build the content-writing loop:

1. Write `scripts/improver.py` — the priority queue + edit + validate pipeline
2. Write `scripts/SCHEMA.md` — the wiki constitution (page structure, conventions, quality bar)
3. Build the prompt template for page improvement (include: page content + relevant raw papers + schema + edit constraints)
4. Add validation: no uncited claims, no new placeholders, wikilinks must resolve
5. Add the "Ralph loop": Ingestor → Improver → git push, running every hour

### Phase 4: Background Quality Agents (3-5 days)

1. Extend `daily_lint.py` into full Auditor (add placeholder detection, stale pages, broken refs)
2. Build Librarian: index regeneration, authority scoring, cross-link symmetry
3. Build `meta/audit-report.json` machine-readable output
4. Have Improver read audit report to prioritize its queue

### Phase 5: Software Ecosystem Mapper (2-3 days)

1. Build `scripts/software_mapper.py` — ensures every tool in the ecosystem has a page
2. Create stub pages for missing tools (FieldTrip, MNE, MRtrix, etc.)
3. Create/expand comparison pages
4. Build the master software map: `comparisons/software-ecosystem.md`
5. Ensure every tool page links to its key papers in `raw/papers/`

### Phase 6: Deployment & Operations (1-2 days)

1. Write `scripts/ralph_daemon.py` — the main loop you start manually
2. It runs an event loop with configurable intervals (hourly/daily/weekly per agent)
3. Outputs progress to stdout (what it's doing, what it changed, sleep timers)
4. Trappable signals: Ctrl+C for graceful shutdown between cycles
5. Resume-safe: reads git log + log.md on startup to know what's already been done today

---

## Logging

Dual output: **stdout + file**, always.

```
scripts/ralph.log          ← structured, append-only, survives restarts
stdout                     ← same content, live in your terminal
```

### Log format

Every line is timestamped with the agent name:

```
2026-04-23 14:02:31 [Ingestor] Starting hourly cycle
2026-04-23 14:02:33 [Ingestor] arXiv: found 3 new papers
2026-04-23 14:02:34 [Ingestor] Semantic Scholar: found 1 new paper
2026-04-23 14:02:35 [Ingestor] Saved raw/papers/arxiv-2507.15519.md
2026-04-23 14:02:35 [Ingestor] Saved raw/papers/arxiv-2506.03806.md
2026-04-23 14:02:35 [Ingestor] Saved raw/papers/semanticscholar-abc123.md
2026-04-23 14:02:36 [Ingestor] Updated 4 entity pages with new sources
2026-04-23 14:02:37 [Ingestor] Committed: "Ingest: 3 papers (Ingestor)"
2026-04-23 14:02:37 [Ingestor] Cycle complete. 3 papers added, 4 pages updated.
2026-04-23 14:02:37 [daemon]   Sleeping 3600s until next cycle

2026-04-23 14:03:01 [Improver] Starting hourly cycle
2026-04-23 14:03:01 [Improver] Scoring 176 pages by quality...
2026-04-23 14:03:02 [Improver] Worst page: entities/yan-wang.md (placeholder, 120 words, 0 refs)
2026-04-23 14:03:02 [Improver] Reading page + 2 relevant raw papers...
2026-04-23 14:03:15 [LLM]      Request sent to provider (sonnet, ~6K tokens in)
2026-04-23 14:03:22 [LLM]      Response received (7.1s, ~1.8K tokens out)
2026-04-23 14:03:22 [Improver] Validating: 0 uncited claims, 2 new wikilinks, no placeholders ✓
2026-04-23 14:03:23 [Improver] Committed: "Improve yan-wang: replaced placeholder, added refs (Improver)"
2026-04-23 14:03:23 [Improver] Cycle complete. 1 page improved.
2026-04-23 14:03:23 [daemon]   Sleeping 3600s until next cycle

2026-04-23 15:00:01 [Ingestor] Starting hourly cycle
2026-04-23 15:00:05 [Ingestor] No new papers found.
2026-04-23 15:00:05 [Ingestor] Cycle complete. Nothing to do.
```

Key properties:
- Every agent cycle has a clear START and COMPLETE line so you can scan for hangs
- LLM calls log send/receive with latency and token counts
- Errors are logged at `[ERROR]` level with full detail, never silently swallowed
- Silent cycles (nothing to do) log that explicitly so you know it's alive, not stuck
- Sleep messages tell you how long until the next cycle

### Startup log

On launch, the daemon logs its state:

```
2026-04-23 14:00:00 [daemon]   Ralph daemon starting
2026-04-23 14:00:00 [daemon]   Wiki root: /home/duke/src/tvb-wiki
2026-04-23 14:00:00 [daemon]   Pages: 176 (54 entities, 59 concepts, 6 comparisons, 57 other)
2026-04-23 14:00:00 [daemon]   Raw papers: 250
2026-04-23 14:00:00 [daemon]   Last ingest: 2026-04-23T13:02:37 (from meta/last_update.txt)
2026-04-23 14:00:00 [daemon]   Agents: Ingestor(hourly) Improver(hourly) Auditor(daily) Librarian(daily) SoftwareMapper(weekly)
2026-04-23 14:00:00 [daemon]   Models: writer=ollama/kimi-k2.6, reviewer=zai/glm-5.1
2026-04-23 14:00:00 [daemon]   LLM interface: pi subshell (pi --model <model> -p "...")
2026-04-23 14:00:00 [daemon]   Log file: scripts/ralph.log
2026-04-23 14:00:00 [daemon]   Ready. Ctrl+C to stop.
```

---

## LLM Error Handling

The daemon doesn't call LLM APIs directly. It spawns **pi subshells**:

```bash
pi --model ollama/kimi-k2.6 -p "Read SCHEMA.md. Improve entities/yan-wang.md. ..."
pi --model zai/glm-5.1 -p "Review this proposed edit to entities/yan-wang.md. ..."
```

This means the error handling is about **managing pi subprocess lifecycle**, not raw HTTP.

### Timeout

```python
# pi subprocess timeout (configurable, default 300s = 5 min)
# If pi doesn't exit in time:
#   - Kill the subprocess
#   - Log: "[pi] Timeout after 300s (kimi-k2.6, Improver, retry 1/3)"
#   - Retry up to 3 times
#   - If all retries fail: skip this agent cycle
```

### pi exits with error

```python
# pi returned non-zero exit code:
#   - Capture stderr
#   - If "connection refused" / "ollama not running":
#       - Log: "[ERROR] ollama not running. Sleeping 60s then retry."
#       - This is the most common failure — local ollama needs a nudge sometimes
#   - If "model not found":
#       - Log: "[ERROR] Model ollama/kimi-k2.6 not found. Check ollama list."
#       - Halt daemon — can't proceed without the model
#   - If "rate limit" / HTTP 429 (from zai/glm-5.1):
#       - Sleep 60s, retry up to 3 times, then skip cycle
#   - If "auth" / HTTP 401 (from zai):
#       - Log: "[ERROR] zai auth failed. Check credentials."
#       - Continue with only ollama/kimi-k2.6 for the rest of the session
#   - Other errors: log + skip cycle
```

### pi produces garbled / empty output

```python
# pi exited 0 but the output is unusable:
#   - Log: "[pi] Response failed validation: <reason>"
#   - Do NOT write anything to the wiki
#   - Retry once with a stricter prompt
#   - If still bad: skip cycle
```

### Ollama goes down (local model)

```python
# ollama/kimi-k2.6 is the primary writer. If ollama is unreachable:
#   - Log: "[WARN] ollama unreachable, falling back to zai/glm-5.1 for Writer"
#   - glm-5.1 takes over Writer AND Reviewer roles
#   - Check ollama health every 5 minutes
#   - When ollama comes back: resume dual-model pipeline
#   - Log: "[INFO] ollama back online, resuming dual-model pipeline"
```

### Circuit breaker (per agent)

```python
# If an agent fails 3 cycles in a row:
#   - Disable that agent for the rest of the session
#   - Log: "[daemon] Auditor disabled: 3 consecutive failures"
#   - Other agents keep running
#   - Re-enabled on next daemon restart
```

### Summary of the contract

| Situation | Action |
|-----------|--------|
| pi timeout | Kill subprocess, retry 3×, skip cycle |
| ollama not running | Sleep 60s, retry, skip cycle if persistent |
| ollama model not found | Halt daemon |
| zai rate limit | Sleep + retry, skip cycle if persistent |
| zai auth failure | Continue with ollama only for rest of session |
| ollama goes down | Fall back to zai for Writer, check ollama health periodically |
| Bad pi output | Don't write, retry once, skip cycle |
| Agent fails 3× in a row | Disable agent, others continue |
| All agents disabled | Log + halt daemon |

The invariant: **the daemon never writes garbage to the wiki.** If there's any doubt about the pi output, it skips the cycle and logs why.

---

## The SCHEMA.md (Wiki Constitution)

This is the single most important file. Draft structure:

```markdown
# TVB Wiki Schema

## What This Is
A Scholarpedia-quality knowledge base on The Virtual Brain, whole-brain 
modeling, neural mass models, connectomics, and related computational 
neuroscience. Every page should be accessible to a neuroscience grad student 
and rigorous enough for a researcher.

## Page Types
- entity: Software tools, people, datasets, research labs
- concept: Methods, models, modalities, theories
- comparison: Side-by-side analyses of related things  
- paper: Raw paper metadata (in raw/papers/, immutable)

## Naming Conventions
- Filenames: kebab-case.md (e.g., neural-mass-model.md)
- Wikilinks: [[neural-mass-model]] or [[Neural Mass Model|display text]]

## Content Rules
1. Every factual claim must cite a source (wikilink to raw/papers/ or explicit ref)
2. No placeholder text in production pages (*Placeholder* = page not ready)
3. Mathematical formulations use LaTeX notation where appropriate
4. Related pages linked via wikilinks — aim for ≥3 outgoing links per page
5. Software pages MUST list: overview, key features, relationship to TVB, key papers
6. Concept pages MUST list: definition, mathematical formulation, applications, related concepts

## Quality Levels
- draft: New stub, needs major work
- accepted: Reasonable content, may have gaps
- verified: Reviewed, well-sourced, comprehensive

## What NOT To Do
- Don't copy abstracts verbatim — synthesize in your own words
- Don't add papers outside scope (TVB, whole-brain modeling, connectomics, neural mass models)
- Don't create pages for tangentially related topics without a clear TVB connection
- Don't remove content without noting why in log.md
```

---

## Key Files to Create/Modify

| File | Status | Purpose |
|------|--------|---------|
| `SCHEMA.md` | **NEW** | Wiki constitution — the most important file |
| `scripts/ralph_daemon.py` | **NEW** | Main loop. Spawns pi subshells, manages schedule, handles errors. No direct LLM API calls. |
| `scripts/improver.py` | **NEW** | Page improvement via writer (kimi-k2.6) + reviewer (glm-5.1) pipeline |
| `scripts/software_mapper.py` | **NEW** | Ensures software ecosystem is fully mapped |
| `scripts/daily_summary.py` | **DROP** | Replaced by structured git commits + log.md |
| `scripts/pick_random_page.py` | **NEW** | Priority-based page selection |
| `scripts/hourly_update.py` | **MODIFY** | Expand beyond arXiv, fix hardcoded paths |
| `scripts/daily_lint.py` | **MODIFY** | Extend auditor checks, fix hardcoded paths |
| `scripts/update_index.py` | **MODIFY** | Fix hardcoded paths |
| `cronjobs.md` | **UPDATE** | Reflect new 6-agent architecture |

---

## Success Metrics

Track these weekly:

| Metric | Target (month 1) | Target (month 6) |
|--------|------------------|-------------------|
| Papers ingested | 300+ | 2,000+ |
| Entity pages | 60+ | 150+ |
| Concept pages | 65+ | 200+ |
| Comparison pages | 10+ | 30+ |
| Placeholder pages | 0 | 0 |
| Avg words per page | 500+ | 1,000+ |
| Broken wikilinks | < 20 | < 5 |
| Orphan pages | < 10 | < 3 |
| Pages with ≥3 references | > 50% | > 80% |
| Pages rated "verified" | > 20% | > 60% |
