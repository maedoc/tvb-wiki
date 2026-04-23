---
created: 2026-04-20
sources:
- raw/papers/ritter-2013.md
- raw/papers/schirner-2018.md
- raw/papers/arxiv-2603.07524.md
- raw/papers/sanz-leon-2013.md
- raw/papers/zavaglia-2006.md
tags:
- whole-brain-modeling
- software-tvb
- neuroimaging-dti
- neuroimaging-fmri
- personalized-brain-modeling
title: Personalized Brain Modeling
type: concept
updated: '2026-04-23'
---

# Personalized Brain Modeling

Personalized brain modeling refers to the construction of subject-specific computational brain models from individual neuroimaging data.

## Definition

Personalized (or patient-specific) brain modeling uses an individual's structural connectivity (from diffusion MRI), functional data (fMRI/EEG), and anatomical scans to create a unique virtual brain model that captures their specific neural architecture and dynamics.

## Methodology

### Data Sources
1. **Structural MRI** — Anatomical reference and parcellation
2. **Diffusion-weighted MRI** — White matter tractography and connectivity
3. **Functional MRI or EEG** — Target functional patterns for validation

### Pipeline Steps
1. **Brain parcellation** — Divide cortex into regions of interest
2. **Tractography** — Reconstruct white matter pathways
3. **Connectivity matrix** — Quantify structural connections
4. **Model parameterization** — Set up neural mass models per region
5. **Simulation and validation** — Match simulated to empirical signals

## Key Tools

- [[TVB]] — Primary platform for personalized whole-brain modeling
- [[ANTs]] — Image registration and preprocessing
- [[GraphVar]] — Connectivity analysis for validation

## Applications

- **Clinical simulation** — Virtual patient models for treatment planning
- **Epilepsy research** — Seizure propagation modeling
- **Stroke recovery** — Predicting functional reorganization
- **Neurodegeneration** — Tracking disease progression
- **Brain stimulation** — Optimizing neuromodulation protocols

## Key Publications

- Ritter et al. (2013) — Multimodal integration for personalized models ritter-2013
- Schirner et al. (2018) — Automated pipeline construction schirner-2018

## Related Concepts

- [[whole brain]] — Whole-brain modeling scope
- [[structural connectivity]] — Connectivity from diffusion MRI
- [[functional connectivity]] — Validation target
- [[neural mass model]] — Regional dynamics model