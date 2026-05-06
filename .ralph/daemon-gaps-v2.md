# Daemon Gap Analysis & Remediation v2

## Analysis Date: 2026-05-06

### Current State Snapshot
| Metric | Value | Target | Priority |
|--------|-------|--------|----------|
| Total pages | 449 | 300+ | ✅ |
| Broken wikilinks | 120 | < 20 | 🔴 HIGH |
| Orphan pages | 46 | < 10 | 🔴 HIGH |
| Placeholder pages | 2 (nipal, neuroharmonize) | 0 | 🟡 |
| Missing frontmatter | 5 | 0 | 🟡 |
| Broken source refs | 105 | < 20 | 🟡 |
| Pages no sources | 20 | < 5 | 🟡 |
| Stale pages | 38 | < 10 | 🟡 |
| Full texts fetched | ~19 | 100+ | 🟡 |
| Daemon uptime | ~6 hours (PID 3563184) | — | ✅ |

### Top Broken Link Targets
1. **rest** — 26x (biggest offender; page was deleted, many pages still link)
2. **neuroimaging-fmri** — 5x
3. **jax** — 2x (was deleted, tvb/brainpy still link)
4. **neuroimaging-eeg** — 2x
5. **modeldb** — 2x
6. **brain-connectivity-toolkit** — 2x
7. Various single hits: sources_4, rate-based-neural-networks, brainstorm, brain-parcellation, cite:biswal2010, cite:glasser2013, cite:desikan2006, karl-j-friston, brain-decoding, jenkinson12, intrinsic-connectivity-networks, tbss

### Placeholder Pages (2 remaining)
- nipal (4 placeholders)
- neuroharmonize (4 placeholders)

### Missing Frontmatter (5 pages)
- nitrc (missing title, created, type, tags)
- petsurfer (missing title, created, updated, type, tags)
- neo (missing tags)
- hrf (missing title)
- desikan-killiany-atlas (missing tags)

## Iteration Plan

### Iteration 1: Fix the 26x `rest` broken link crisis
- Option: Create `rest.md` as a redirect/alias to `resting-state-vs-task-fmri.md` or a dedicated resting-state concept page
- Decision pending based on context of linking pages

### Iteration 2: Fix top broken targets (neuroimaging-fmri, jax, neuroimaging-eeg, modeldb, brain-connectivity-toolkit)
- Create stubs or redirect pages for each target
- Or fix linking pages if target is truly off-mission

### Iteration 3: Fix citation-style broken links (cite:biswal2010, etc.)
- These are malformed citation references in `calamity-atlas.md`
- Convert to proper pandoc citations or plain text

### Iteration 4: Fix remaining single-hit broken links
- brainstorm, brain-parcellation, brain-decoding, jenkinson12, intrinsic-connectivity-networks, tbss, rate-based-neural-networks

### Iteration 5: Fix missing frontmatter
- Add required fields to nitrc, petsurfer, hrf and missing tags to neo, desikan-killiany-atlas

### Iteration 6: Fix orphan pages
- Link orphans to relevant concept/entity pages

### Iteration 7: Restart daemon for PI_TIMEOUT change
- Current daemon started before PI_TIMEOUT 300→180s change
- Restart needed for efficiency improvement to take effect

### Iteration 8+: Ongoing monitoring
- After fixes, run Auditor to verify improvement
- Continue monitoring fulltext progress and Improver output
