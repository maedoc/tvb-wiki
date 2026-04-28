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

### Critical Bug Discovered: Meta-Commentary Contamination

**Symptom:** Improver rewrites contain passages like:

```markdown
The corrected EBRAINS page is now complete. Here's a summary of the fixes applied:

1. **Added inline citations**: References specific papers with author names...
2. **Fixed dubious/unverified claims**: Removed "co-development agreements"...
```

Instead of encyclopedic prose, the model outputs a *review of its own changes*.

**Root Cause:** The revision prompt (improver.py ~line 604) says:

> "Your edit to `{slug}` was flagged for issues. Fix these issues and return the complete updated page..."

This conversational framing trains the model to explain what it's doing rather than just doing it.

**Affected Pages:**
- `entities/ebrains.md` — "The corrected EBRAINS page is now complete..."
- `entities/brainsuite.md` — "The document has been fixed. Here's a summary..."
- `entities/scirun.md` — "The file has been fixed with all the issues addressed..."
- `entities/open-source-brain.md` — Partial contamination (earlier batch)

**Fix:** Add explicit guardrail to revision prompt:
> "Output ONLY the final markdown content. Do NOT explain your changes, summarize what you did, or add any meta-commentary."

### Meta-Commentary Fix: VERIFIED (21:35–22:33)

All 3 previously-corrupted pages re-rewritten cleanly:
- No "The corrected page..." openings
- No numbered lists of changes
- No "Here's a summary..."

Word counts after clean rewrite: ebrains 1057w, scirun 1396w, brainsuite 1326w.

### Throughput Benchmarks

| Agent | Items/Hour | Bottleneck |
|-------|-----------|------------|
| Improver | ~3 pages | Writer + reviewer + potential revision |
| RefFormatter | ~60 pages | Fast (regex) |
| CrosslinkApplier | ~60–160 pages | Fast (regex) |
| Matcher | ~57–61 pages | LLM eval of ambiguous matches |
| Ingestor | ~7 papers | API rate limits (Semantic Scholar 429) |
| DeepResearch | ~76 papers/6h | Search + analysis + synthesis |

### Model Reliability

| Model | Use | Reliability | Notes |
|-------|-----|-------------|-------|
| minimax-m2.5:cloud | Writer | Good (1–4 min/output) | Occasional empty output |
| glm-5.1:cloud | Reviewer | Fast (~15s) | Good at catching factual issues |
| gpt-oss:120b-cloud | Repairer | Unknown | Not yet tested in production |

### Error Patterns

1. **"Empty output"** — ~3/session. Usually resolves on retry.
2. **"Model not found"** — Now caught at startup.
3. **"429 rate limited"** — Semantic Scholar. Backoff works.
4. **"Batch evaluation failed"** — Matcher falls back to per-page.

### Remaining TODOs

- [x] Fix revision prompt guardrail
- [x] Revert 3 corrupted pages
- [ ] Consider making Improver skip revision loop for speed
- [ ] Add score_pages.py output to Auditor cycle
- [ ] Consider capping Matcher LLM eval time

---

## 2026-04-27 22:37 – 2026-04-28 06:33 — 8-Hour Overnight Run

### Results Summary

| Agent | Commits | Impact |
|-------|---------|--------|
| **Improver** | 7 | 21 pages rewritten (avg ~1000 words) |
| **Matcher** | 2 | 48 pages got new sources |
| **Repairer** | 1 | 29 issues fixed |
| **CrosslinkApplier** | 1 | 25 pages linked |
| **RefFormatter** | 1 | 3 pages fixed |
| **Ingestor** | 1 | 3 papers fetched |
| **DeepResearch** | 1 | 25 papers discovered |
| **Auditor** | 1 | 590 issues audited |
| **Librarian** | 1 | Catalog rebuilt |
| **SoftwareMapper** | 1 | 20 new software pages created |

**Total commits:** 18 (including the auto-commit)
**Total pages improved:** 21 rewritten + 48 sourced + 25 linked + 29 repaired + 20 created = **143 pages touched**

### Quality Verification

**Meta-commentary fix held overnight.** Spot-checks of fmriprep, genesis, sloreta, clinica show:
- Dense, cited, encyclopedic prose
- No "Here's a summary..." contamination
- Proper frontmatter with sources
- Technical detail with biological grounding

Example: `entities/fmriprep.md` — 998 words, proper inline citations, explains pipeline stages, relates to BIDS/MNI/TVB ecosystem.

### Error Rates (8-hour window)

| Error | Count | Rate | Notes |
|-------|-------|------|-------|
| Empty output | ~19 | ~3.3% | All resolved on retry |
| Timeout | ~8 | ~1.4% | Mostly Matcher eval |
| Batch eval failed | ~2 | n/a | Normal fallback |
| Model not found | 0 | 0% | Startup validation working |
| Death spiral | 0 | 0% | Error detection order fixed |
| Repairer LLM fail | 0 | 0% | Model fix working |

### New Issue: SoftwareMapper Scope Creep

SoftwareMapper created 20 pages for generic Python libraries (pandas, matplotlib, scipy, scikit-learn, pytorch, seaborn, statsmodels, networkx, etc.). These have empty content (just a heading) and `tags: [software-brain-modeling]`. Not TVB-relevant.

**Recommendation:** Constrain SoftwareMapper to neuroscience-specific tools or skip it until prompt is hardened.

### Daemon Health

- **Uptime:** ~8 hours continuous
- **No restarts required**
- **No manual intervention required**
- **All scheduled agents completed at least one cycle**
- **Improver ran 7 times (~hourly)**
- **Matcher ran 2 times (~every 6h)**

### Throughput Projection

At current rate (~3 pages/hour for Improver):
- **Per day:** ~72 pages rewritten
- **Per week:** ~504 pages rewritten
- **Remaining weak pages:** ~81 (score < 20) + ~146 medium (score 20–59)
- **ETA to zero weak pages:** ~27 hours of Improver runtime
- **ETA to zero medium pages:** ~73 additional hours

---

## Historical Notes

### Pre-2026-04-27 Issues (Fixed)

- Writer model was kimi-k2.5:cloud → switched to minimax-m2.5:cloud
- 254 broken wikilinks → fixed via redirection and stub creation
- 114 placeholder pages → 87 remain (27 core software filled)
- 52 thin narrative pages → 0 remain after bulk rewrite

---

*This file is append-only. Each daemon session should add a dated section with what was learned.*
