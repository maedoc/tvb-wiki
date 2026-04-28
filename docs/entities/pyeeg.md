---
created: 2024-01-15
sources:
- https://doi.org/10.1155/2011/406391
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3070217/
- https://doi.org/10.1002/hbm.20346
tags:
- neuroimaging-eeg
- software-visualization
- computational-neuroscience
- neural-mass-models
title: PyEEG
type: entity
updated: '2026-04-28'
---

# PyEEG

## Overview

PyEEG is an open-source Python library for analyzing electroencephalography (EEG) data, developed primarily by Forrest Sheng Bao and colleagues at Texas Tech University. The library provides efficient implementations of feature extraction algorithms commonly used in EEG-based research, particularly those derived from [[nonlinear-dynamics]] and information theory. Originally released in 2010, PyEEG has become a foundational tool in the [[computational-neuroscience]] and [[neuroimaging]] communities for quantifying neural dynamics from electrophysiological recordings. The package is designed to complement existing EEG analysis frameworks such as [[EEGLAB]] and [[fieldtrip]] by providing optimized Python implementations of advanced analytical methods that were previously available only in MATLAB toolboxes or required custom implementation.

The library focuses on extracting features that capture the nonlinear and complex dynamics of neural activity, which standard spectral methods often fail to adequately characterize. These nonlinear measures have proven particularly valuable for studying conditions such as epilepsy, where seizure dynamics exhibit highly nonlinear behavior, and for investigating cognitive processes involving neural oscillations and synchronization. PyEEG's modular design allows researchers to easily integrate its functions into larger analysis pipelines built with tools like [[nipype]] or [[mne-python]].

## Key Features

PyEEG provides a comprehensive suite of algorithms for EEG feature extraction, organized into several categories that reflect different aspects of neural signal properties. The library's strength lies in its implementation of entropy-based measures and nonlinear dynamics parameters that quantify the complexity and predictability of neural time series.

**Entropy Measures**: The library includes implementations of sample entropy (SampEn), approximate entropy (ApEn), and permutation entropy (PermEn). Sample entropy measures the regularity of a time series by computing the conditional probability that two sequences of similar pattern will remain similar at the next point, making it robust to noise and suitable for short data segments. Approximate entropy similarly quantifies regularity but uses a correlation integral approach. These entropy measures have been extensively used to characterize changes in neural dynamics associated with anesthesia, sleep, and neurological disorders.

**Spectral Analysis**: PyEEG implements spectral decomposition methods including fast Fourier transform (FFT)-based power spectral density estimation and wavelet transforms. The library also provides functions for computing spectral entropy, which quantifies the uniformity of the power distribution across frequencies. Band-specific power can be extracted for canonical frequency bands including delta (0.5–4 Hz), theta (4–8 Hz), alpha (8–13 Hz), beta (13–30 Hz), and gamma (30–100 Hz) oscillations.

**[[connectivity]] Measures**: The library includes implementations of phase locking value (PLV) and phase lag index (PLI), which quantify the degree of phase synchronization between EEG channels. These measures are essential for studying [[functional-connectivity]] patterns in [[resting-state]] networks and during task-based paradigms. PLV computes the consistency of phase differences between signals, while PLI is more robust to [[volume-conduction]] artifacts.

**Nonlinear Dynamics Parameters**: PyEEG provides implementations of Lyapunov exponents, correlation dimension, and recurrence quantification analysis. These measures characterize the chaotic or deterministic nature of neural dynamics and are particularly relevant for studying epileptic seizures, where the transition to ictal states involves changes in nonlinear coupling.

## Technical Implementation

The core functions in PyEEG are implemented in Python with optional Cython acceleration for computationally intensive operations. The input format follows standard conventions—continuous or epoched EEG data represented as NumPy arrays with dimensions corresponding to channels and time points. Sampling frequency must be specified for appropriate frequency-domain analysis.

The entropy functions accept parameters controlling the embedding dimension (m) and tolerance (r) for similarity assessment. For sample entropy, typical values include m = 2 and r = 0.2 times the standard deviation of the signal, though these must be chosen carefully based on the data length and sampling rate to ensure reliable estimates. The library provides guidance on parameter selection through documentation and example scripts.

For spectral analysis, PyEEG implements both parametric (Burg method) and non-parametric (Welch's method) approaches. The spectral entropy function computes the normalized Shannon entropy of the power spectral density, providing a single value characterizing the complexity of the frequency distribution. This measure has been shown to track changes in arousal states and anesthetic depth. Specifically, it quantifies the irregularity or randomness in the frequency content of the signal by treating the power spectrum as a probability distribution and calculating the Shannon entropy across frequency bins.

The connectivity functions operate on multi-channel data, computing pairwise synchronization measures across all channel combinations. Output can be represented as connectivity matrices suitable for further graph-theoretical analysis using tools like the [[brain-connectivity-toolbox]] or [[bctpy]].

## Relationship to TVB

PyEEG intersects with [[the-virtual-brain]] (TVB) primarily through its utility in parameter fitting and validation of whole-brain models. TVB simulates large-scale brain dynamics using [[neural-mass-models]] such as the [[jansen-rit-model]] or [[wong-wang-model]], producing synthetic EEG signals as one of several output modalities. Extracting features from empirical EEG data using PyEEG enables researchers to fit model parameters by minimizing the distance between simulated and observed features—a process essential for [[personalized-brain-modeling]].

The entropy and connectivity measures implemented in PyEEG are particularly valuable for this purpose because they capture aspects of neural dynamics that simple spectral power cannot. For example, when modeling epilepsy with the [[epileptor]] model, matching sample entropy or correlation dimension between simulated and real EEG provides better约束 of the underlying dynamical systems parameters than power spectral fitting alone. TVB's architecture supports external data adapters, enabling integration with PyEEG-based analysis pipelines for such validation workflows.

Furthermore, PyEEG's feature extraction capabilities complement TVB's forward modeling pipeline. TVB implements multiple[[forward-model]] approaches for generating observable EEG, MEG, and [[fmri]] signals from neural population activity. Comparing features extracted from these simulated signals with empirical features using PyEEG functions provides a validation framework for [[whole-brain]] models.

## Related Software

PyEEG is part of a broader ecosystem of EEG analysis tools, each with distinct strengths. [[EEGLAB]] is a comprehensive MATLAB-based toolbox offering preprocessing, independent component analysis (ICA), and clustering, with extensive plugin support. [[fieldtrip]] provides a MATLAB framework emphasizing forward modeling and source analysis with strong ties to [[dynamic-causal-modeling]]. [[mne-python]] offers a modern Python alternative with sophisticated source estimation, connectivity analysis, and integration with the PyData ecosystem. For nonlinear dynamics analysis specifically, [[ nonlinearity]] toolboxes and custom implementations using [[scipy]] or [[torch]] provide alternative approaches to Lyapunov exponent estimation and recurrence quantification.

## Key Papers

The foundational paper describing PyEEG (Bao et al., 2011) established the library's architecture and demonstrated its applicability to epilepsy research. Subsequent work has applied PyEEG-derived features to studies of anesthesia mechanisms, sleep stage classification, and working memory. The library has been cited in numerous studies validating [[neural-mass-model]] predictions against empirical EEG data, particularly in the context of whole-brain [[epilepsy-modeling]] initiatives.

A key methodological reference for the connectivity measures is the Phase Lag Index paper by Stam and colleagues (2007), which introduced PLI as a measure of phase synchronization that is less affected by volume conduction and common source artifacts compared to traditional phase coherence measures.

## References

1. Bao FS, Liu X, Zhang C. PyEEG: An Open Source Python Module for EEG/MEG Feature Extraction. Computational Intelligence and Neuroscience. 2011;2011:406391. doi:10.1155/2011.406391

2. Stam CJ, Nolte G, Daffertshofer A. Phase lag index: Assessment of functional connectivity from multichannel EEG and MEG with diminished bias from common sources. Human Brain Mapping. 2007;28(11):1178-1193. doi:10.1002/hbm.20346

3. Vinck M, Oostenveld R, van Wingerden M, Battaglia F, Pennartz CM. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. Neuroimage. 2011;55(4):1548-1565. doi:10.1016/j.neuroimage.2011.01.055