# Daemon Gap Analysis & Remediation Plan

## Analysis Date: 2026-05-06

### Current State Snapshot
| Metric | Value | Target (Month 1) | Gap |
|--------|-------|------------------|-----|
| Total pages | 437 | 300+ | ✅ |
| Raw papers | 1,645 | 300+ | ✅ |
| Full texts fetched | 8 (~0.5%) | N/A | 🔴 CRITICAL |
| Broken wikilinks | 82 | < 20 | 🔴 |
| Orphan pages | 48 | < 10 | 🟡 |
| Placeholder pages | 13 | 0 | 🟡 |
| Entities | 295 | 60+ | ✅ |
| Concepts | 140 | 65+ | ✅ |
| Comparisons | 6 | 10+ | 🔴 |
| Avg words/entity | 880 | 500+ | ✅ |
| Avg words/concept | 681 | 500+ | ✅ |
| Pages with sources | 438 (>99%) | >50% | ✅ |

### Gap 1: Full Text Coverage Nearly Zero (🔴 CRITICAL)
- **Only 8 of 1,645 papers have extracted full text**
- FullTextFetcher has only run ~2 cycles since deployment
- Top unfetched foundational papers: Breakspear 2017 (score 73), Ritter 2013 (69), Schirner 2018 (55), Deco 2013 (54)
- These are the most-cited, most-relevant papers — their absence cripples the Improver's ability to write deep, sourced content
- **Root cause**: 4h interval + daemon launch timing means it's barely fired; also many old papers lacked DOIs until yesterday's fix

### Gap 2: Missing Core Software Pages (🔴)
- **fsl** (9 broken inbound links), **freesurfer** (8), **spm** (5), **dipy** (4), **mrtrix3** (3), **pynn** (3)
- These are foundational neuroimaging tools referenced everywhere but have no wiki pages
- SoftwareMapper creates pages but the blacklist/filter may be too conservative, or the pages were deleted and never recreated

### Gap 3: Improver Inefficiency (🟡)
- Pi timeouts after 300s (3 retries) = 15 min burned per failed page
- Citation guard rejecting pages with citations that don't exist in raw/papers (e.g., niftynet's Gibson 2018)
- Word count dropping significantly on some edits (848 → 160), causing revert
- 3/5 pages failing per cycle recently
- **Impact**: ~60% of Improver cycles are wasted on retries/reverts

### Gap 4: Placeholder Pages Persist (🟡)
- 13 pages still have `*Placeholder*` text
- Improver is working through them at ~2-3/hour but some keep failing validation

### Gap 5: Low Comparison Page Count (🟡)
- Only 6 comparison pages vs target of 10+
- The SoftwareMapper should be creating more comparison pages (TVB vs NEST, ANTs vs FSL, etc.)

### Gap 6: Daemon Agent Scheduling Gaps (🟡)
- FullTextFetcher has only launched once or twice since daemon restart
- Some agents may be getting starved by long-running Improver cycles
- The concurrent thread model means all agents share the same process — if one hangs, others may not check in properly

## Remediation Plan

1. **Batch-fetch full texts NOW** — manually run FullTextFetcher with increased cap to catch up on all foundational papers
2. **Create missing core software stubs** — fsl, freesurfer, spm, dipy, mrtrix3, pynn
3. **Fix Improver citation guard** — allow citations to raw papers that exist as arxiv/semanticscholar slugs, not just exact title matches
4. **Bulk-remove remaining placeholders** — either fill or delete the last 13 placeholder pages
5. **Verify all agents are running** — check daemon state, ensure no agents are stuck
