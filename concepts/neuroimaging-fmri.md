---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-e08252ec3941.md
- raw/papers/semanticscholar-a6fa6ab4802f.md
- raw/papers/semanticscholar-c836b6f72ba9.md
tags:
- neuroimaging-fmri
- bold
- functional-connectivity
- resting-state
title: Functional MRI
type: concept
updated: '2026-05-18'
---

# Functional MRI

**Functional Magnetic Resonance Imaging ([[fmri]])** is a [[neuroimaging]] technique that measures brain activity by detecting changes in blood flow. It is the dominant method for mapping human brain function in vivo.

## Overview
Simulation-based inference (SBI) encompasses a family of [[bayesian|Bayesian]] methods for situations where the likelihood of observed data cannot be expressed in closed form, yet forward simulation from a generative model remains feasible [[raw/papers/arxiv-2601.22367.md|Sun et al. (2026)]]. The core idea is to circumvent explicit likelihood evaluation by learning an approximate posterior distribution over model parameters from large ensembles of synthetically generated data sets [[raw/papers/arxiv-2601.22367.md|Sun et al. (2026)]]. In neuroscience, this paradigm addresses a fundamental obstacle: models of [[network-dynamics|network dynamics]] and [[connectomics|brain connectivity]] are typically high-dimensional coupled systems with analytically intractable likelihoods, rendering conventional Bayesian approaches computationally prohibitive [[raw/papers/arxiv-2506.04558.md|Fan & White (2025)]].

Modern SBI replaces iterative Markov-chain Monte Carlo samplers with [[neural-network|neural networks]] trained as amortized conditional density estimators [[raw/papers/arxiv-2601.22367.md|Sun et al. (2026)]]. Once trained, these estimators map from an observed data set to a posterior sample in a single forward pass, eliminating per-dataset simulation or inference-time MCMC [[raw/papers/arxiv-2601.22367.md|Sun et al. (2026)]]. Fan and White [[raw/papers/arxiv-2506.04558.md|(2025)]] introduced Amortised Hierarchical Sequential Neural Posterior Estimation to target intractable likelihoods in multiple-network models, scaling inference for resting-state [[neuroimaging-fmri|fMRI]] data well beyond traditional methods [[raw/papers/arxiv-2506.04558.md|Fan & White (2025)]]. Sun, Nicholls, and Lee [[raw/papers/arxiv-2601.22367.md|(2026)]] further extended amortization to Generalized Bayesian Inference, demonstrating that a single neural posterior estimator conditioned on both data and temperature achieves competitive approximations across SBI benchmarks including the chaotic Lorenz-96 system [[raw/papers/arxiv-2601.22367.md|Sun et al. (2026)]].
## Relationship to TVB

fMRI is the primary empirical constraint for TVB [[whole-brain]] models:
- TVB simulates BOLD signals from [[neural-mass-models]] using the [[hrf|hemodynamic response function]]
- Resting-state [[functional-connectivity]] matrices calibrate TVB [[structural-connectivity]] weights
- TVB predicts task-evoked BOLD changes that can be validated against task fMRI
- TVB models [[effective-connectivity]] via DCM and compare to fMRI-derived [[connectivity]]

[[sbi]]

## Related

- [[bold-signal]] — BOLD signal modeling and hemodynamics
- [[resting-state-vs-task-fmri]] — comparison of paradigms
- [[neuroimaging-eeg]] — complementary electrophysiological imaging
- [[dandi]] — archive for neurophysiology and neuroimaging data

## ORPHAN PAGE CONTEXT (sbi)
---

## References

1. Mennahtullah Mabrouk, Reem Reda, Hana Hisham, Abdelrahman Hazem, Bola Hosny, Hossam Elsawaf, Saif Elaswad, Sameh Sherif. (2025). *A Hybrid Learning Approach for Detection of Autism Spectrum Disorder Using fMRI Data*. 2025 13th International Japan-Africa Conference on Electronics, Communications, and Computations (JAC-ECC). [DOI](https://doi.org/10.1109/JAC-ECC67970.2025.11417627)
2. L. Raimondo, Jurjen Heij, Tomas Knapen, Jeroen C. W. Siero, W. van der Zwaag, Serge O. Dumoulin. (2025). *Does the Cortical-Depth Dependence of the Hemodynamic Response Function Differ Between Age Groups?*. Brain Topography. [DOI](https://doi.org/10.1007/s10548-025-01107-0)
3. N. J. Fesharaki, Artemy Vinogradov, David Ress, Jung Hwan Kim. (2026). *Spatial evolution in temporal dynamics of hemodynamic response function in human superior colliculi with ultra-high-resolution MRI at 9.4T*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2026.1741923)