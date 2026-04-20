---
title: Independent Component Analysis
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [ica, neuroimaging-eeg, neuroimaging-meg, neuroimaging-fmri]
sources: [raw/papers/makeig-1996.md]
---

# Independent Component Analysis (ICA)

Independent Component Analysis is a computational technique for separating mixed signals into statistically independent components, widely used in neuroimaging for artifact removal and network identification.

## Definition

ICA decomposes multichannel data (e.g., EEG, MEG, fMRI) into spatially or temporally independent components. Unlike PCA, ICA seeks statistical independence rather than just uncorrelatedness, making it suitable for separating mixed sources.

## Applications in Neuroimaging

### EEG/MEG
- **Artifact removal**: Separate eye blinks, muscle activity, cardiac signals
- **Brain sources**: Identify independent neural generators
- **Introduced by**: scott-makeig in 1996

### fMRI
- **Spatial ICA**: Identify spatially independent networks
- **Temporal ICA**: Identify temporally independent time courses
- **Resting-state networks**: Default mode, sensorimotor, etc.

## Algorithms

- **Infomax**: Maximizes information transfer
- **FastICA**: Fast fixed-point algorithm
- **AMICA**: Multiple mixture models

## Role in Whole-Brain Modeling

ICA provides:

1. **Network components**: Identified ICs correspond to functional networks
2. **Validation targets**: Component time courses for model comparison
3. **Artifact-free data**: Preprocessing for cleaner validation

## Related Concepts
- [[eeg]] – Electrophysiological source
- [[meg]] – Magnetic source
- [[fmri]] – Hemodynamic source
- [[resting-state]] – Primary application domain
- intrinsic-connectivity-networks – ICs often correspond to networks
- source-separation – General category
