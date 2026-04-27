---
created: 2026-04-20
sources:
- raw/papers/makeig-1996.md
- raw/papers/arxiv-2510.12910.md
- raw/papers/arxiv-2604.11971.md
tags:
- ica
- neuroimaging-eeg
- neuroimaging-meg
- neuroimaging-fmri
title: Independent Component Analysis
type: concept
updated: '2026-04-27'
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

## References

1. (authors unknown). *Independent component analysis of electroencephalographic data*.
2. Neda Abdollahpour, N. Sertac Artan, Ian Daly, Mohammadreza Yazdchi, Zahra Baharlouei. (2025). *[[effective-connectivity]]-Based Unsupervised Channel Selection Method for EEG*. [Link](https://arxiv.org/abs/2510.12910)
3. Sunia Tanweer, Narayan Puthanmadam Subramaniyam, Firas A. Khasawneh. (2026). *Classification of Epileptic iEEG using Topological Machine Learning*. [Link](https://arxiv.org/abs/2604.11971)