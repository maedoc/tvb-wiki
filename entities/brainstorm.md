---
created: 2024-01-15
sources:
- https://neuroimage.usc.edu/brainstorm/
- raw/papers/10.1152-jn.00194.2011.md
- raw/papers/10.1016-j.neuroimage.2011.09.015.md
- raw/papers/arxiv-2604.16463.md
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2505.16861.md
tags:
- software-neuroimaging
- neuroimaging-eeg
- neuroimaging-meg
- software-visualization
- software-brain-modeling
title: Brainstorm
type: entity
updated: '2026-05-07'
---

**Brainstorm** is a collaborative, open-source MATLAB and Python application dedicated to magnetoencephalography (MEG), electroencephalography (EEG), stereo-EEG (sEEG), and electrocorticography (ECoG) data analysis and visualization [[citation:1]]. Developed primarily at the University of Southern California, Brainstorm provides an integrated graphical user interface (GUI) and scripting environment that encompasses the full pipeline from raw recordings to statistical analysis and visualization of source-reconstructed brain activity.

## Overview and Capabilities

Brainstorm is designed to address the complete neuroimaging analysis workflow within a unified environment. The software supports data import from all major MEG and EEG systems, including CTF, 4D Neuroimaging (BTi), Neuromag/Elekta, Brain Products, and various EEG amplifier formats [[citation:1]]. Preprocessing capabilities include bandpass and notch filtering, artifact rejection techniques such as independent component analysis (ICA), signal-space projection (SSP), and signal-space separation (SSS) for ambient noise cancellation [[citation:2]]. These preprocessing tools enable researchers to clean recordings contaminated by eye movements, muscle artifacts, and environmental interference before downstream analysis.

The software offers multiple approaches to source localization, which refers to the inference of brain activity origins from sensor-level recordings. Brainstorm implements distributed inverse solutions including minimum norm estimation (MNE) [[citation:3]], dynamic statistical parametric mapping (dSPM) [[citation:4]], and standardized low-resolution brain electromagnetic tomography (sLORETA) [[citation:5]], each with different assumptions about source smoothness and depth weighting. Beamforming approaches such as the linearly constrained minimum variance (LCMV) beamformer enable spatially selective reconstruction of activity from specific brain regions [[citation:3]]. Users can also perform equivalent current dipole fitting for focal epileptic activity or event-related responses. Forward models incorporating realistic head geometry derived from [[freesurfer]] cortical reconstructions account for skull and tissue conductivity effects.

For time-frequency analysis, Brainstorm provides spectral decomposition using multitaper methods and Morlet wavelets, enabling computation of oscillatory power across canonical frequency bands (delta, theta, alpha, beta, gamma) [[citation:1]]. [[functional-connectivity]] measures including coherence, phase-locking value, and granger causality can be computed at both sensor and source levels, facilitating investigation of inter-regional coupling in [[resting-state]] and task-based paradigms. The software includes statistical tools for group-level analysis using parametric tests and nonparametric permutations, with correction for multiple comparisons across space and time.

## Relationship to TVB

Brainstorm and [[the-virtual-brain]] (TVB) serve complementary roles in the whole-brain modeling pipeline. While Brainstorm performs sensor-to-source reconstruction to obtain anatomically constrained time series, TVB simulates large-scale brain dynamics using [[neural-mass-models]] and [[structural-connectivity]] derived from diffusion imaging [[citation:6]]. This creates a natural workflow where Brainstorm-derived source time series serve as empirical initialization or validation for TVB simulations, particularly in studies of [[epilepsy-modeling]] where patient-specific seizure dynamics are reconstructed and then predicted using computational models.

Conversely, TVB's realistic forward models can generate synthetic MEG/EEG data that may be compared against Brainstorm-reconstructed activity from empirical recordings. This bidirectional integration enables researchers to test whether observed connectivity patterns and spectral properties arise from known underlying dynamics captured by whole-brain models. Both platforms share compatibility with [[freesurfer]] cortical surfaces and standard [[neuroimaging]] formats (NIfTI, CIFTI), facilitating data exchange. The relationship is particularly relevant for [[brain-stimulation]] research, where TVB predicts the network effects of stimulation while Brainstorm validates predicted sensor-level responses.

## Software Ecosystem

Brainstorm operates as a MATLAB-based toolbox with optional Python bindings, distributed under the GPL v2 open-source license [[citation:1]]. The software maintains active development and a user community through its website (https://neuroimage.usc.edu/brainstorm/). Related toolboxes in the MEG/EEG ecosystem include [[eeglab]], [[fieldtrip]], and [[mne-python]], which share overlapping functionality but differ in their primary focus—EEGLAB emphasizes EEG preprocessing [[citation:7]], MNE-Python offers Python-native source imaging [[citation:8]], while Brainstorm balances comprehensiveness with accessibility for clinical users. The MLE-Toolbox represents a more recent addition to this ecosystem, offering integrated machine learning classifiers and automated report generation while maintaining interoperability with established platforms including Brainstorm [[citation:9]].

## References

1. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f))
2. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
3. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale [[co-simulation]] Framework with a Case Study on Neural-Level Seizure Generation and [[whole-brain]] Propagation*. [Link](](https://arxiv.org/abs/2505.16861))