---
title: FOOOF
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [software-brain-modeling, neuroimaging-eeg, neuroimaging-meg, brain-oscillations, resting-state, software-tvb]
sources:
  - https://doi.org/10.1038/s41593-020-00744-x
  - https://fooof-tools.github.io/
---

# FOOOF

## Overview

**FOOOF** (Fitting Oscillations & One Over F) is an open-source Python toolbox for parameterizing neural power spectra. Developed by the Voytek Lab at UC San Diego[1], FOOOF separates electrophysiological power spectra into their constituent components: aperiodic 1/f-like activity and periodic oscillatory peaks. This decomposition enables quantitative analysis of both the background signal (reflecting underlying physiological processes) and the rhythmic oscillations characteristic of neural activity.

The tool addresses a fundamental challenge in neural signal analysis: power spectra from electrophysiological recordings (EEG, MEG, ECoG, LFP) contain both broadband, aperiodic activity following a power-law distribution and narrower-band oscillatory components. Traditional analysis often conflates these or uses arbitrary filtering approaches. FOOOF provides a model-based framework that fits a Gaussian to each oscillatory peak and a knee-supporting exponential to the aperiodic component, returning interpretable parameters for each.

## Key Features

FOOOF implements a robust fitting algorithm with several key capabilities[1]:

**Aperiodic Component Modeling**: The tool models the background 1/f activity using $\log(P) = b - \log(k + F^\chi)$, where $b$ is offset, $k$ is knee frequency (optional), and $\chi$ is the exponent. This captures the broadband power-law dynamics thought to reflect synchronized populations of neurons and synaptic filtering.

**Oscillatory Peak Detection**: FOOOF identifies and parameterizes putative oscillatory peaks using Gaussian functions, returning center frequency, amplitude, and bandwidth for each detected rhythm. This enables quantitative comparison of alpha, beta, theta, and other canonical frequency bands across conditions or subjects.

**Knee Detection**: The algorithm can detect and fit "knees" in the aperiodic spectrum—frequency points where the power-law slope changes—potentially indexing distinct physiological processes at different scales.

**Multi-Spectrum Support**: FOOOF efficiently handles collections of spectra from multiple channels, trials, or subjects, with built-in parallelization and batch processing capabilities.

**Integration Ecosystem**: The package provides direct integration with MNE-Python and custom export to MATLAB[2], fitting naturally into standard neuroimaging pipelines.

## Relationship to TVB

FOOOF and [[TVB]] serve complementary roles in whole-brain modeling workflows. TVB generates simulated neural activity and resulting electrophysiological signals (EEG/MEG), while FOOOF provides the analytical framework to characterize the spectral properties of those simulations.

Key integration points include:

- **Validation of Neural Mass Models**: FOOOF can parameterize power spectra from TVB simulations using neural mass models like [[jansen-rit]] or [[wilson-cowan]], allowing direct comparison between simulated and empirical spectral features. Researchers can tune model parameters (excitation/inhibition balance, synaptic time constants) to match observed 1/f exponents and oscillatory peak characteristics.

- **Aperiodic Activity Analysis**: The [[whole-brain-modeling]] approach in TVB naturally produces 1/f-distributed spectra. FOOOF's explicit modeling of aperiodic components enables researchers to study how structural connectivity and local dynamics together shape the broadband spectral envelope observed in [[resting-state]] recordings.

- **Cross-Scale Validation**: When using [[tvb-multiscale]] for hybrid spiking-mean-field simulations, FOOOF can characterize spectra at different scales, validating that macroscopic oscillatory dynamics emerge appropriately from microscopic spiking activity.

## Key Papers

The foundational publication for FOOOF is:

- **Donoghue et al. (2020)**: "Parameterizing neural power spectra into periodic and aperiodic components" (Nature Neuroscience). This paper establishes the algorithm, validates it against simulated and empirical data, and demonstrates that spectral parameters differ between task conditions and clinical populations[1].

## Related Software

- [[TVB]] — Whole-brain simulation platform where FOOOF can analyze simulated EEG/MEG outputs
- [[Elephant]] — NeuralEnsemble toolkit for electrophysiology analysis; can be combined with FOOOF for comprehensive LFP processing
- [[NEST]] — Spiking network simulator; oscillatory spectra from NEST simulations can be analyzed with FOOOF
- [[MNE-Python]] — MEG/EEG analysis library with which FOOOF integrates directly
- SciPy — Underlying scientific computing framework for signal processing
- YASA — Sleep stage analysis package that incorporates FOOOF for spectral parameterization

## References

1. Donoghue, T., Haller, M., Peterson, E. J., Varma, P., Sebastian, P., Gao, R., (...) & Voytek, B. (2020). Parameterizing neural power spectra into periodic and aperiodic components. *Nature Neuroscience*, 23(12), 1655-1665. https://doi.org/10.1038/s41593-020-00744-x

2. Voytek Lab. (n.d.). FOOOF: Fitting Oscillations & One Over F. Documentation and source code available at https://fooof-tools.github.io/