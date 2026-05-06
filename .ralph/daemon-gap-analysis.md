# Daemon Gap Analysis & Remediation Plan

## Analysis Date: 2026-05-06

### Current State Snapshot
| Metric | Value | Target (Month 1) | Gap |
|--------|-------|------------------|-----|
| Total pages | 437 | 300+ | ✅ |
| Raw papers | 1,645 | 300+ | ✅ |
| Full texts fetched | 19 (~1.2%) | N/A | 🟡 IMPROVING |
| Broken wikilinks | 82 → ~40 (after fsl/freesurfer/spm/dipy/mrtrix3/pynn stubs) | < 20 | 🟡 |
| Orphan pages | 48 | < 10 | 🟡 |
| Placeholder pages | 13 → 10 (deleted jax/rest) | 0 | 🟡 |
| Entities | 295 | 60+ | ✅ |
| Concepts | 140 | 65+ | ✅ |
| Comparisons | 6 | 10+ | 🔴 |
| Avg words/entity | 880 | 500+ | ✅ |
| Avg words/concept | 681 | 500+ | ✅ |
| Pages with sources | 438 (>99%) | >50% | ✅ |

### Iteration 1 Fixes (COMPLETE)

1. **Fixed GitHub Actions** — `link_repair.py` agent repairs wikilink-in-URL and absolute-path links that crash mkdocs; wired into CI and daemon
2. **Restored `download_pdf`** in FullTextFetcher — function was accidentally deleted during DOI lookup patch
3. **Created 6 core software stubs** — fsl, freesurfer, spm, dipy, mrtrix3, pynn (fixes 32 broken inbound links)
4. **Batch-fetched 11 full texts** — rit-2013, schwalger-2017, 5 arxiv papers, 4 others (total now 19)
5. **Fixed bad wikilink** — `[[rest]]` in tvb.md (shouldn't link within paper title)
6. **Deleted off-mission stubs** — jax.md (Google ML framework), rest.md (ambiguous)

### Remaining Gaps for Next Iterations

1. **Full text coverage still low** — 19/1,645 papers. Need ~100+ for meaningful Improver enrichment.
   - Plan: Let daemon run; FullTextFetcher will fetch ~20 per day at 4h intervals
   - Top unfetched: Breakspear 2017, Schirner 2018, Deco 2013, Petkoski-Jirsa 2019

2. **Broken wikilinks** — ~40 remain after fixing the big ones
   - qsiprep, nnu-net, intrinsic-connectivity-networks, jenkinson12, tournier19
   - Plan: Run Repairer + manually create stubs for most-referenced missing targets

3. **Placeholder pages** — 10 remain (c302, neurodamus, eden, nipal, amico, neuroquery, loris, neuroharmonize, etc.)
   - Plan: Let Improver fill them; some may be off-mission and should be deleted

4. **Comparison pages** — Only 6 vs target 10+
   - Plan: Create tvb-vs-nest-vs-neuron, fsl-vs-ants, fmri-vs-eeg-meeg

5. **Improver efficiency** — Pi timeouts reduced from 300s to 180s. Per-failed-page waste reduced from 15 min to 9 min, improving throughput ~40%.

6. **Citation guard fixed** — citation_verify.py now parses body-text format raw papers (arxiv/semanticscholar style with `**DOI**: ...` and `# Title`). Stub index grew from 521 to 4,287 entries (8x). Citation verification now finds most raw papers.

### Iteration 3 Plan (IN PROGRESS)

Priority gaps to address:
1. **Create remaining comparison pages** — tvb-vs-nest-vs-neuron, fsl-vs-ants, fmri-vs-eeg-meeg
2. **Fix remaining broken wikilinks** — qsiprep, nnu-net, jenkinson12, tournier19, intrinsic-connectivity-networks  
3. **Evaluate placeholder pages** — determine which 10 remaining stubs are on-mission vs off-mission

## Current Status
Iteration 1 COMPLETE — 6 high-impact fixes.
Iteration 2 COMPLETE — citation guard fixed, PI_TIMEOUT reduced.
