# Ralph Quality Improvement Plan

**Date:** 2026-04-24  
**Status:** Planning — no code changes yet  

## Problem Statement

After one night of running (ralph-0.txt), the wiki has 220 pages and 691 raw papers. The pipeline works mechanically, but three systematic quality defects persist across the wiki:

1. **Dual/opaque references sections** — Some pages have two `## References` sections (one with proper citations, one dumping raw source slugs like `arxiv-2509.02799`). Even single-section pages often list opaque slugs instead of human-readable citations with DOIs/URLs.

2. **Thin narrative** — Pages like `concepts/zerlaut.md` (195 words) have equations but no motivating context. The Improver treats them as "done" because they lack placeholders and have wikilinks, so they score ≥80 and fall off the priority queue.

3. **Missing crosslinks** — Pages mention terms like "mean-field equations" and "integrate-and-fire" as plain text instead of `[[wikilinks]]`. The Crosslink agent only runs weekly and only *suggests* — nothing actually *applies* the suggestions.

---

## Root Cause Analysis

### Issue 1: Dual/Opaque References

**Where it comes from:** The `sources:` frontmatter field and the `## References` body section serve different purposes but nothing reconciles them.

- The **Matcher** attaches raw paper paths to `sources:` (e.g., `raw/papers/arxiv-2509.02799.md`).
- The **Improver** writer prompt says "Add factual claims ONLY if you can cite a source" but gives no instruction on *how* to format citations in the body. The LLM sometimes invents a nice `## References` section with proper citations (with DOIs), and sometimes doesn't.
- The **Auditor** has `find_pages_no_sources()` which checks frontmatter `sources:` — but it never checks if the body has a readable references section. It also doesn't detect duplicate `## References` headings.
- The **Linter** doesn't inspect reference section quality at all.

**Result:** The frontmatter has machine-readable paths. The body may or may not have a human-readable references section. The LLM, when doing a full rewrite, may create a fresh `## References` without knowing there's already one, or it may copy the raw slug list.

### Issue 2: Thin Narrative

**Where it comes from:** The Improver's `score_page()` function:

```python
if info['words'] < 200:
    score -= 30
elif info['words'] < 500:
    score -= 10
```

Pages with ~200 words of equations and a table get scored ~70-80 — just above the threshold. The Improver's `pick_weakest_section()` targets sections scoring <80, but a page with short-but-present sections may not trigger.

More importantly, **the writer prompt has no instruction to add narrative context** — it says "Replace ALL placeholder text" and "Add wikilinks", but doesn't say "Begin with a clear introduction explaining what this model is and why it exists". The schema says concept pages should include "Definition / explanation" and "Current state of knowledge", but the prompt doesn't enforce this structure.

**Result:** Pages with equations and tables but no "why should I care?" text get scored as acceptable and never re-enter the improvement queue.

### Issue 3: Missing Crosslinks

**Where it comes from:** Three disconnects:

1. **Crosslink agent only suggests** — `crosslink.py` writes suggestions to `crosslink_suggestions.json` but never applies them. Nothing in the pipeline consumes that file.
2. **Writer prompt is vague** — It says "Add wikilinks [[like-this]] to related pages (minimum 3)" but doesn't provide the list of *existing* pages. The LLM guesses, creating links to slugs that may not exist (which then become "broken wikilinks" for the Repairer to clean up).
3. **No inline crosslinking pass** — There's no agent that reads a page's text, identifies terms that match existing page titles/slugs, and inserts `[[wikilinks]]`.

**Result:** The embedding-based crosslink suggestions sit in a JSON file unused. Meanwhile, the Improver's writer adds 3-5 wikilinks but misses many opportunities because it doesn't know what pages exist.

---

## Proposed Changes

### Change 1: New Agent — `ref_formatter.py` (daily)

**Purpose:** Ensure every page has exactly one well-formatted `## References` section with human-readable citations.

**Logic:**
1. Load each page's `sources:` from frontmatter.
2. For each source, read the raw paper file and extract: title, authors, year, DOI, URL.
3. Check the body for existing `## References` sections.
4. **If no `## References` section exists:** Generate one at the bottom of the page with formatted entries like:
   ```
   1. Author A, Author B (Year). *Title*. Journal/venue. [DOI](https://doi.org/10.xxx) [arXiv](https://arxiv.org/abs/xxxx)
   ```
5. **If duplicate `## References` sections exist:** Merge into one, deduplicating.
6. **If existing section lists raw slugs** (matches pattern `arxiv-\d{4}\.\d{4,5}` or `semanticscholar-...`): Replace each with a formatted citation using metadata from the corresponding raw paper file.
7. **If a proper citation already exists:** Leave it alone.
8. No LLM needed — this is entirely mechanical from raw paper metadata.

**Scheduling:** Daily, after the Matcher (so sources are fresh).

### Change 2: Improve `improver.py` — Enrich Writer Prompt

**Changes to `build_writer_prompt()`:**

1. **Add a "Page Inventory" block** — inject the list of all existing page slugs into the prompt so the writer can link accurately:
   ```
   ## EXISTING WIKI PAGES (use these for wikilinks)
   neural-mass-models, mean-field-theory, integrate-and-fire, wilson-cowan, ...
   ```

2. **Add narrative instructions** for concept pages:
   ```
   For concept/model pages, the page MUST include:
   - A "Motivation" or "Context" paragraph explaining WHY this model exists
   - A plain-English description of what the model does before any equations
   - Use analogies or comparisons to related models where helpful
   Target 500-800 words for concept pages, 400-600 for entity pages.
   ```

3. **Add reference formatting instruction:**
   ```
   Do NOT add a ## References section — a separate agent handles reference formatting.
   ```

4. **Raise the word-count thresholds** in `score_page()`:
   - `< 300 words` → -40 (was -30 at <200)
   - `< 500 words` for concept pages → -20 (was -10 at <500)
   - This pushes thin narrative pages back into the improvement queue.

### Change 3: New Agent — `crosslink_applier.py` (daily)

**Purpose:** Actually apply the crosslink suggestions that `crosslink.py` generates, plus scan for inline link opportunities.

**Logic — Layer 0 (mechanical, no LLM):**
1. Load `crosslink_suggestions.json`.
2. For each suggestion with `score > 1.0`, check if `[[target]]` already exists in the source page.
3. If not, find a natural insertion point using a simple heuristic: search for the target's title (or keyword from it) in the body text and wrap it in `[[wikilinks]]`.
4. If no natural text match exists, skip (don't force it).

**Logic — Layer 1 (LLM-assisted):**
5. For high-value suggestions (score > 1.5) with no mechanical insertion point, use the LLM to insert a crosslink naturally.
6. Use the REPAIRER_MODEL (cheap) for this.

**Logic — Layer 2 (inline scan):**
7. Build a dictionary of `{display_term: page_slug}` from all existing page titles and slugs (e.g., `{"mean-field theory": "mean-field-theory", "Epileptor": "epileptor"}`).
8. For each page, scan body text for these terms appearing as plain text (not already inside `[[]]`).
9. Wrap matches in `[[slug|display term]]` — but only if the term appears in a natural sentence (not in code blocks, tables, or headings).

**Scheduling:** Daily, replacing the current weekly `crosslink.py` cycle. The existing `crosslink.py` becomes a sub-step (generate suggestions) of this agent.

### Change 4: Enhance `auditor.py` — New Quality Checks

Add these checks to `run_auditor_cycle()`:

1. **`find_duplicate_references_sections()`** — Detect pages with more than one `## References` or `## Sources` heading.
2. **`find_opaque_references()`** — Detect reference entries that are raw slugs (match `arxiv-\d{4}\.\d+` or `semanticscholar-[a-f0-9]+` in the body text).
3. **`find_thin_narrative_pages()`** — Pages where the first non-heading, non-table paragraph under the first `##` section is < 50 words (suggesting missing motivation/context).
4. **`find_missing_crosslinks()`** — Pages that contain terms matching existing page titles but without `[[wikilinks]]`.

These feed into the audit report so the Repairer and new agents can act on them.

### Change 5: Enhance `repairer.py` — Consume Audit Quality Flags

Add a new repair layer that acts on the new audit checks:

- **Fix duplicate references** — purely mechanical: merge, dedup, keep the better-formatted one.
- **Fix opaque references** — delegate to `ref_formatter.py`.
- **Fix missing crosslinks** — delegate to `crosslink_applier.py`.

This keeps the Repairer as the orchestrator that reads the audit report and dispatches to specialist fixers.

---

## Agent Schedule Updates

Current → Proposed:

| Agent | Current | Proposed |
|---|---|---|
| Matcher | hourly | hourly (unchanged) |
| Ingestor | daily | daily (unchanged) |
| Improver | hourly | hourly (with enriched prompt) |
| RefFormatter | — | **daily, after Matcher** |
| CrosslinkApplier | — | **daily, after RefFormatter** |
| Auditor | daily | daily (with 4 new checks) |
| Repairer | daily | daily (with new quality fix dispatch) |
| Librarian | daily | daily (unchanged) |
| Linter | daily | daily (unchanged) |
| DeepResearch | 2x/week | 2x/week (unchanged) |
| SoftwareMapper | weekly | weekly (unchanged) |

---

## Implementation Order

1. **`ref_formatter.py`** — Highest impact, fully mechanical, no LLM cost. Fixes the most visible defect.
2. **Auditor enhancements** — Adds the detection layer so we know the scope of all issues.
3. **`crosslink_applier.py`** — Turns existing suggestions into action + adds inline scanning.
4. **Improver prompt enrichment** — Prevents thin pages from being generated in the first place.
5. **Repairer integration** — Wires the new checks to the new fixers.

---

## Risk Mitigation

- **ref_formatter.py is mechanical** — no LLM, deterministic, easy to test on one page before rolling out.
- **crosslink_applier.py Layer 0** uses exact text matching only — no risk of garbled insertions.
- **Improver prompt changes** are additive — the existing writer pipeline continues to work, just with better instructions.
- **All new agents follow the existing pattern** — `run_X_cycle()` returning stats, gated by intervals, disabled after 3 consecutive failures.
