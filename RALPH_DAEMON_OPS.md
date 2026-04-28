# Ralph Daemon Operations Log

Live documentation of hard-won lessons from running `scripts/ralph_daemon.py` in production.

---

## 2026-04-27 — Session Summary

### What Was Fixed Today

1. **Agent ordering** — Improver now runs FIRST, then RefFormatter/CrosslinkApplier, then Matcher. Previously Matcher (2–3h cycle) blocked everything.
2. **MATCHER_INTERVAL** — Changed from 3600s (1h) to 21600s (6h). Matcher needs 1–2h to complete; hourly scheduling caused starvation.
3. **TOP_CANDIDATES** — Reduced from 10 to 3 in `matcher.py`. Smaller prompts → faster LLM eval.
4. **AUTO_CONFIRM_SIM** — Lowered from 0.65 to 0.55. More pages skip slow LLM evaluation via auto-confirmation.
5. **Model validation at startup** — New `validate_models()` in `ralph_daemon.py`. Pings Ollama API, disables agents whose models are missing.
6. **Error detection order** — In `run_pi()`, "model not found" is now checked BEFORE "ollama" in stderr. Was causing infinite retries for nonexistent models.
7. **REPAIRER_MODEL** — Updated from nonexistent `gpt-oss-120b` to `gpt-oss:120b-cloud`.

---

## 2026-04-28 06:45 — Embedding-Based Relevance Detection Experiment

### Goal
"Can embeddings identify irrelevant pages (e.g. generic Python libraries created by SoftwareMapper)?"

### Method
1. Rebuilt wiki embeddings (291 pages with content chunks).
2. Built TVB centroid from 16 core pages.
3. Computed cosine similarity (centroid score).
4. Computed neighborhood purity (pct of top-30 neighbors also in core).
5. Created hybrid score: centroid x purity.
6. Combined with real word count (excluding template/placeholder text).

### Results

- **Embeddings alone are noisy** — wrongly flagged `neural-mass-model`, `bifurcation-theory`, `dynamical-systems-theory`
- **Graph distance resolves false positives** — neural-mass-model has 52 in-links, graph dist 0 from core
- **Hybrid score is useful for orphan detection** — catches `plotly` (generic) but not the math pages

### Tools Added
- `scripts/check_relevance.py` — embedding-only filter
- `scripts/combined_relevance.py` — graph distance + embedding filter
- `scripts/check_combined_relevance.py` — combined filter with decision logic

---

## 2026-04-28 13:30 — Immediate + Short-Term Fixes Applied

### 1. Constrained SoftwareMapper (13:30)

**Problem:** SoftwareMapper created 20 empty stubs for generic Python libraries (pandas, matplotlib, scipy, seaborn, sklearn, pytorch, pyvista, h5py, joblib, networkx, plotly, etc.)

**Fix:**
- Added `GENERIC_BLACKLIST` to `scripts/software_mapper.py` — blocks known generic libraries
- Added `_has_neuro_relevance()` check using keyword filter for LLM-identified tools  
- Deleted 13 existing empty stubs

### 2. Wired combined_relevance into Auditor (13:40)

**Problem:** No automated way to detect low-relevance pages

**Fix:**
- `scripts/auditor.py` now imports `combined_relevance`
- New `find_low_relevance_pages()` runs on each audit cycle
- Results: **80 low-relevance pages** (70 stubs + 10 unreachable+distant)
- Added to audit report under `low_relevance` key

### 3. Matcher speedup (13:45)

- Added title-match auto-confirm (sim ≥ 0.80 = immediate, no LLM)
- Increased `EVAL_BATCH_SIZE` 5 → 8 for fewer LLM calls
- Commits: `Matcher: attached sources to 33 pages` in overnight run

### 4. Improver KeyError bugs (13:50)

**Bug 1:** `KeyError: 'has_placeholder'` — `score_page()` returned an error dict without `has_placeholder` when `read_page()` failed.
- Fixed: `'error'` dicts now include all required keys
- Fixed: `build_priority_queue()` skips error dicts entirely
- Fixed: all downstream `.get()` used instead of `['key']`

**Bug 2:** `KeyError: 'score'` — error dicts didn't have `'score'` key, crashed `sorted()`.
- Fixed by skipping error dicts in queue

### Daemon Status

- **Running:** ✅ Started at 13:49, PID 275350
- **Improver:** ✅ First cycle active, 3 pages in progress (glasser-atlas, suma, xnat)
- **pi calls:** ✅ 9-47s per call, no timeouts
- **No restarts needed since fix**

---

## Remaining Work

### Short-term (this week)

- [ ] Delete remaining ~70 empty stubs flagged by relevance check
- [ ] Fix slug normalization: `bifurcation-theory` vs `bifurcation-analysis` (duplicate concepts)
- [ ] Add graph distance check to daemon startup (auto-flag new orphan pages)
- [ ] Test Repairer with gpt-oss:120b-cloud model (not yet tested)

### Medium-term

- [ ] Expand TVB core centroid (add mne-python, bids, diffusion-mri, tractography)
- [ ] Wire `score_pages.py` into daemon Dashboard
- [ ] Add orphan-linking agent (finds accepted pages with `graph_dist=999` and links them)

---

*This file is append-only. Each daemon session should add a dated section with what was learned.*


---

## 2026-04-28 14:00 — GitHub Actions Fix

### Problem
mkdocs build failed with AttributeError: dict has no endswith in hooks/obsidian_support.py line 123.

### Root Cause
Some pages have dict-style sources (title/url fields) while others have string sources. The hook assumed all sources were strings.

### Fix
hooks/obsidian_support.py: Added dict handling before string processing.

### Result
- Workflow: SUCCESS (https://maedoc.github.io/tvb-wiki/)
- Deployed at 2026-04-28T12:01:49Z
