---
created: 2026-04-23
sources:
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/arxiv-2604.14259.md
- raw/papers/arxiv-2604.00163.md
- raw/papers/arxiv-2406.05002.md
- raw/papers/arxiv-2508.05288.md
- raw/papers/arxiv-2509.12873.md
- raw/papers/arxiv-2602.09535.md
- raw/papers/arxiv-2603.07524.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-2004e006655b.md
- raw/papers/glean-github.md
tags:
- software-brain-modeling
- neuroimaging-eeg
- neuroimaging-meg
- brain-oscillations
- resting-state
- software-tvb
title: FOOOF
type: entity
updated: '2026-05-04'
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

**Integration Ecosystem**: The package provides direct integration with MNE-Python and custom export to MATLAB[2], fitting naturally into standard [[neuroimaging]] pipelines.

## Relationship to TVB

FOOOF and [[TVB]] serve complementary roles in [[whole-brain]] modeling workflows. TVB generates simulated neural activity and resulting electrophysiological signals (EEG/MEG), while FOOOF provides the analytical framework to characterize the spectral properties of those simulations.

Key integration points include:

- **Validation of [[neural-mass-models]]**: FOOOF can parameterize power spectra from TVB simulations using neural mass models like [[jansen-rit]] or [[wilson-cowan]], allowing direct comparison between simulated and empirical spectral features. Researchers can tune model parameters (excitation/inhibition balance, synaptic time constants) to match observed 1/f exponents and oscillatory peak characteristics.

- **Aperiodic Activity Analysis**: The [[whole-brain-modeling]] approach in TVB naturally produces 1/f-distributed spectra. FOOOF's explicit modeling of aperiodic components enables researchers to study how [[structural-connectivity]] and local dynamics together shape the broadband spectral envelope observed in [[resting-state]] recordings.

- **Cross-Scale Validation**: When using [[tvb-multiscale]] for hybrid spiking-[[mean-field-theory|mean-field]] simulations, FOOOF can characterize spectra at different scales, validating that macroscopic oscillatory dynamics emerge appropriately from microscopic spiking activity.

## Key Papers

The foundational publication for FOOOF is:

- **Donoghue et al. (2020)**: "Parameterizing neural power spectra into periodic and aperiodic components" (Nature Neuroscience). This paper establishes the algorithm, validates it against simulated and empirical data, and demonstrates that spectral parameters differ between task conditions and clinical populations[1].

## Related Software

- [[TVB]] — Whole-brain simulation platform where FOOOF can analyze simulated EEG/MEG outputs
- [[Elephant]] — NeuralEnsemble toolkit for [[electrophysiology]] analysis; can be combined with FOOOF for comprehensive LFP processing
- [[NEST]] — Spiking network simulator; oscillatory spectra from NEST simulations can be analyzed with FOOOF
- [[MNE-Python]] — MEG/EEG analysis library with which FOOOF integrates directly
- SciPy — Underlying scientific computing framework for signal processing
- [[yasa]] — Sleep stage analysis package that incorporates FOOOF for spectral parameterization

## References

1. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](https://doi.org/10.3389/fncom.2025.1731161)
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *Arbor-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](https://arxiv.org/abs/2505.16861)
3. Qianyu Chen, Shujian Yu. (2026). *Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay*. [Link](https://arxiv.org/abs/2604.14259)
4. Ferdaus Anam Jibon, Fazlul Hasan Siddiqui, F. Deeba, Gahangir Hossain. *Epileptic Seizure Detection in Separate Frequency Bands Using Feature Analysis and Graph Convolutional Neural Network (GCN) from Electroencephalogram (EEG) Signals*. [Link](https://arxiv.org/abs/2604.00163)
5. Deepa Tilwani, Christian O'Reilly. *Deep Jansen-Rit Parameter Inference for Model-Driven Analysis of Brain Activity*. [Link](https://arxiv.org/abs/2406.05002)
6. Xuanyu Shen, Yu Hu. (2025). *Covariance spectrum in nonlinear recurrent neural networks*. [Link](https://arxiv.org/abs/2508.05288)
7. Gianluca Gaglioti, Alessandra Cardinale, Cosimo Lupo, Thierry Nieus, Federico Marmoreo, Elena Focacci, Robin Gutzen, Michael Denker, Andrea Pigorini, Marcello Massimini, Simone Sarasso, Pier Stanislao Paolucci, Giulia De Bonis. *Emergent complexity and rhythms in evoked and spontaneous dynamics of human whole-brain models after tuning through analysis tools*. [Link](https://arxiv.org/abs/2509.12873)
8. Irmantas Ratas, Kestutis Pyragas. (2026). *Parameter and hidden-state inference in mean-field models from partial observations of finite-size neural networks*. [Link](https://www.semanticscholar.org/paper/274d3afcf4f54ddb5bd2122157c2ab2a105b41ef)
9. Hongjie Jiang, Yifei Tang, Shuqiang Wang. *Neural Dynamics-Informed Pre-trained Framework for Personalized Brain Functional Network Construction*. [Link](https://arxiv.org/abs/2603.07524)
10. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
11. Marianna Angiolelli, D. Depannemaecker, H. Agouram, J. Régis, R. Carron, M. Woodman, L. Chiodo, P. Triebkorn, Abolfazl Ziaeemehr, Meysam Hashemi, Alexandre Eusebio, Viktor Jirsa, P. Sorrentino. (2025). *The Virtual Parkinsonian patient*. npj Systems Biology and Applications. [DOI](https://doi.org/10.1038/s41540-025-00516-y)
12. (authors unknown). *GLEAN: Group Level Exploratory Analysis of Networks*.