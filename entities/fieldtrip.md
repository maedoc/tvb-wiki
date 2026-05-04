---
created: 2025-01-15
sources:
- Oostenveld et al.
- Computational Intelligence and Neuroscience
- FieldTrip website documentation
- Donders Institute
- raw/papers/doi-10-1155-2011-156869.md
tags:
- software-neuroimaging
- neuroimaging-eeg
- neuroimaging-meg
- neuroimaging-meg-eeg-toolbox
- software-visualization
- source-localization
- time-frequency-analysis
- resting-state
- functional-connectivity
- source-separation
title: FieldTrip
type: entity
updated: '2026-05-04'
---

FieldTrip is a MATLAB toolbox for neurophysiology data analysis that provides comprehensive functionality for preprocessing, source reconstruction, time-frequency analysis, and statistical inference on MEG and EEG recordings. Developed and maintained by the Donders Institute for Brain, Cognition and Behaviour at Radboud University Nijmegen, FieldTrip has become one of the most widely used open-source toolboxes for analyzing electromagnetic brain signals since its initial release in 2002 [@Oostenveld2011]. The toolbox implements state-of-the-art algorithms for forward modeling, inverse solutions, and connectivity analysis, making it essential infrastructure for researchers studying human brain dynamics through non-invasive electrophysiology.

## Motivation and Context

The analysis of MEG and EEG data presents substantial methodological challenges that motivated the development of FieldTrip. Unlike fMRI, which measures the hemodynamic response with poor temporal resolution, electromagnetic brain signals capture neural activity with millisecond precision but require sophisticated signal processing to reconstruct the intracranial sources from extracranial sensor recordings. Before FieldTrip, researchers typically relied on commercial software with limited flexibility or home-grown scripts that were difficult to share and reproduce. FieldTrip addressed this gap by providing a unified, well-documented framework that implements best practices from the literature while allowing complete customization. The toolbox's design emphasizes transparency, reproducibility, and methodological rigor—principles that have influenced the broader computational neuroscience ecosystem.

## Core Functionality

FieldTrip provides an extensive suite of functions organized into several interconnected modules. The preprocessing pipeline handles reading data from nearly all major MEG and EEG systems, applying digital filters, artifact rejection (including independent component analysis via [[ica]]), epoching, and baseline correction. For source reconstruction, FieldTrip implements multiple forward modeling approaches including the boundary element method (BEM) and finite element method (FEM), with support for individual anatomical MRI processing via integration with [[freesurfer]] and [[mni-space]] templates. The inverse solution implementations span methods from beamforming (LCMV) and minimum-norm estimates (wMNE) to beamformers and [[source-localization]] algorithms including [[eloreta]] and [[sloreta]].

The time-frequency analysis module computes wavelet transforms, multitaper spectra, and Hilbert transforms for examining oscillatory dynamics across frequency bands relevant to [[brain-oscillations]] research. Connectivity analysis functions enable estimation of [[effective-connectivity]] and [[functional-connectivity]] in the frequency domain, including coherence, phase-locking value, and granger causality. Statistical inference is supported through nonparametric permutation tests that properly account for multiple comparisons across space, time, and frequency.

## Integration with Other Tools

FieldTrip integrates with the broader neuroimaging ecosystem through standardized data formats and interoperability layers. The toolbox fully supports [[bids]] (Brain Imaging Data Structure) for organizing and sharing datasets, and can exchange processed data with tools like [[mne-connectivity]] (via Python conversion), [[eeglab]], and [[brainstorm]]. Source-reconstructed data can be mapped to cortical surfaces for visualization using [[connectome-workbench]] or [[brainnet-viewer]], enabling integration with [[connectome]] analyses and [[brain-parcellations]] such as [[aal-atlas]], [[destrieux-atlas]], and [[schaefer-atlas]].

## Relationship to TVB

While FieldTrip focuses on electrophysiology data analysis rather than whole-brain simulation, it plays a complementary role in [[the-virtual-brain]] workflows. Researchers frequently use FieldTrip to preprocess and analyze MEG/EEG recordings that serve as empirical validation data for TVB simulations. The source-localized time series produced by FieldTrip can be exported and compared against TVB's simulated brain dynamics, enabling validation of [[whole-brain-modeling]] parameters against empirical data. Conversely, TVB's generative modeling framework can be used to generate predictions that are tested against real data processed through FieldTrip, creating a closed loop between empirical analysis and computational modeling that advances understanding of [[brain-dynamics]] in both normal and clinical populations.

---

**References**

- Oostenveld, R., Fries, P., Maris, E., & Schoffelen, J.-M. (2011). FieldTrip: Open source software for advanced analysis of MEG, EEG, and invasive electrophysiological data. *Computational Intelligence and Neuroscience*, 2011, 156869. https://doi.org/10.1155/2011/156869