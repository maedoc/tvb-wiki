# Daemon Gap Analysis & Remediation v2

## Analysis Date: 2026-05-06

### Current State Snapshot
| Metric | Value | Target | Priority |
|--------|-------|--------|----------|
| Total pages | 471 (Librarian rebuilt catalog) | 300+ | ✅ |
| Broken wikilinks | 120 (stale audit) | < 20 | 🔴 HIGH |
| Orphan pages | 46 (stale audit) | < 10 | 🔴 HIGH |
| Placeholder pages | 2 (nipal, neuroharmonize) | 0 | 🟡 |
| Missing frontmatter | 5 → 0 | 0 | ✅ FIXED |
| Broken source refs | 105 | < 20 | 🟡 |
| Pages no sources | 20 | < 5 | 🟡 |
| Stale pages | 38 | < 10 | 🟡 |
| Full texts fetched | ~19 | 100+ | 🟡 |
| Daemon PID | 3919519 (restarted) | — | ✅ |

### Top Broken Link Targets (from latest stale audit)
1. **rest** — 26x (FIXED: created concepts/rest.md redirect)
2. **neuroimaging-fmri** — 5x (FIXED: created concept stub)
3. **jax** — 2x (FIXED: recreated redirect stub)
4. **neuroimaging-eeg** — 2x (FIXED: created concept stub)
5. **modeldb** — 2x (FIXED: created entity stub)
6. **brain-connectivity-toolkit** — 2x (FIXED: created entity stub)
7. Various others — all now have stubs created

## Completed in Iteration 1

### Created 19 new stubs to fix broken wikilinks
- concepts/rest.md (redirect to resting-state)
- concepts/neuroimaging-fmri.md
- concepts/neuroimaging-eeg.md
- concepts/brain-parcellation.md
- concepts/brain-decoding.md
- concepts/intrinsic-connectivity-networks.md
- concepts/rate-based-neural-networks.md
- concepts/tbss.md
- concepts/jenkinson12.md
- concepts/tournier19.md
- concepts/schaefer.md
- concepts/neural-simulation.md
- concepts/karl-j-friston.md
- entities/modeldb.md
- entities/brain-connectivity-toolkit.md
- entities/brainstorm.md
- entities/nnu-net.md
- entities/brian.md (redirect to brian2)
- entities/jax.md

### Fixed missing frontmatter (5 pages)
- entities/nitrc.md — added title, created, type, tags
- entities/petsurfer.md — cleaned malformed YAML with trailing spaces
- entities/neo.md — added meaningful tags
- entities/hrf.md — added title
- entities/desikan-killiany-atlas.md — added meaningful tags

### Fixed malformed citations/numeric refs
- xppaut.md, SynthSeg.md, Boutiques.md — changed `[[N]]` to `[N]`
- entities/calamity-atlas.md — removed `[[cite:...]]` brackets
- entities/neuroml.md — fixed `[[sources_4]]`

### Daemon maintenance
- Restarted daemon (old PID 3563184 → new PID 3919519)
- PI_TIMEOUT 300s→180s now active
- Pushed all commits to origin/main

## Next Iteration Plan (Iteration 2)

1. Wait for next Auditor run to get fresh audit numbers and verify broken link reduction
2. Address remaining orphan pages (need fresh audit data)
3. Address broken source refs (105)
4. Address pages with no sources (20)
5. Continue monitoring

## Current Status

All iteration 1 work complete. The daemon is running autonomously (PID 3919519) with:
- PI_TIMEOUT=180s active (efficiency improvement)
- 19 new stubs fixing all top broken link targets
- 5 missing frontmatter pages fixed
- Malformed citation/numeric refs fixed in 5 files
- All changes committed and pushed to origin/main

Next Auditor cycle will provide fresh metrics to guide remaining work on orphans, broken source refs, and pages without sources.
