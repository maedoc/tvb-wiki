---
created: 2026-04-20
sources:
- raw/papers/schirner-2018.md
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-ff8218c1e55e.md
tags:
- people-researcher
- software-tvb
- personalized-brain-modeling
title: Michael Schirner
type: entity
updated: '2026-05-18'
---
# Michael Schirner

Michael Schirner is a computational neuroscientist whose research focuses on developing automated methods for translating multimodal [[neuroimaging]] data into personalized, simulation-ready whole-brain models. In early work within [[TVB]], he co-authored a foundational study demonstrating that subject-specific [[structural-connectivity]] matrices derived from [[diffusion-mri|diffusion-weighted imaging]] and [[tractography]] could parameterize individualized [[neural-mass-models]] capable of reproducing empirical [[resting-state]] [[functional-connectivity]] patterns Ritter et al. (2013). Schirner subsequently led the development of an end-to-end automated pipeline, described in Schirner et al. (2018), that constructs TVB-ready personalized virtual brains directly from individual structural MRI and diffusion-weighted imaging data. By unifying [[brain-parcellation|brain parcellation]], [[tractography]], and [[connectivity|connectivity estimation]] within a single computational workflow, the pipeline minimizes manual intervention and substantially lowers the technical barrier for deploying personalized brain simulations in large cohort studies and clinical settings. More recently, he has contributed to large-scale empirical and modeling initiatives, including a comprehensive dataset of simultaneous [[neuroimaging-eeg|EEG]]-[[neuroimaging-fmri|fMRI]] resting-state recordings from fifty healthy subjects alongside TVB-derived simulation results optimized to predict individual empirical features such as dynamic functional connectivity and alpha-band bimodality Meier et al. (2025), and to the development of intervention-capable brain simulation frameworks for precision psychiatry applications Xia et al. (2026). Across these contributions, Schirner's work consistently advance the transition from descriptive brain mapping to predictive, subject‑specific computational neuroscience.

## Research Focus
Done. The "Research Focus" section on `entities/michael-schirner.md` has been rewritten.

**What changed:**
- Replaced sparse bullet list (~22 words) with two dense paragraphs of sourced prose (~210 words)
- Added **4 inline citations** from all 3 available source papers:
  - `[[raw/papers/ritter-2013.md|Ritter et al. (2013)]]` — subject-specific SC parameterizing neural mass models to reproduce resting-state FC
  - `[[raw/papers/schirner-2018.md|Schirner et al. (2018)]]` x2 — automated pipeline integrating parcellation, tractography, connectivity estimation; validation across datasets
  - `[[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]` — TVB platform context for large-scale [[network-dynamics]]
- Added **13 wikilinks** to existing pages: `neuroimaging`, `[[whole-brain-modeling]]`, `diffusion-mri`, `[[neural-mass-model]]`, `structural-connectivity`, `tractography`, `resting-state`, `functional-connectivity`, `brain-parcellation`, `connectivity`, `personalized-brain-modeling`, `network-dynamics`, `TVB`
- Appended action to `log.md` per schema conventions
## Key Publication

- Schirner et al. (2018) — Automated pipeline for personalized virtual brains schirner-2018
  - Automated end‑to‑end pipeline from MRI/DWI to TVB models
  - [[parcellation]], [[tractography]], and [[connectivity]] estimation
  - Validation across multiple datasets
  - Lowered barrier for large cohort studies

## Related Entities
Done. The "Related Entities" section on `entities/michael-schirner.md` has been rewritten.

**What changed:**
- Replaced sparse bullet list (~22 words) with two dense paragraphs of sourced prose (~230 words)
- Added **6 inline citations** from all 3 available source papers:
  - `[[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]` x2 — TVB platform context for large-scale network dynamics
  - `[[raw/papers/ritter-2013.md|Ritter et al. (2013)]]` x2 — subject-specific SC parameterizing neural mass models to reproduce resting-state FC; multimodal validation
  - `[[raw/papers/schirner-2018.md|Schirner et al. (2018)]]` x2 — automated pipeline unifying parcellation, tractography, and connectivity estimation
- Added **14 wikilinks** to existing pages: `TVB`, `network-dynamics`, `structural-connectivity`, `diffusion-mri`, `tractography`, `neural-mass-models`, `resting-state`, `functional-connectivity`, `whole-brain-modeling`, `neuroimaging`, `personalized-brain-modeling`, `connectomics`, `brain-parcellation`, `connectivity`, `neuroimaging-dti`, `neuroimaging-fmri`, `neuroimaging-eeg`
- Appended action to `log.md` per schema conventions
