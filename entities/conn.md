---
created: 2026-04-23
sources:
- https://doi.org/10.1089/brain.2012.0073
- https://doi.org/10.1016/j.neuroimage.2007.04.042
- https://doi.org/10.1101/2020.08.05.234243
- raw/papers/rubinov-sporns-2010.md
- raw/papers/smith-2013-connectomics.md
- raw/papers/woodman-2014.md
- raw/papers/semanticscholar-6f3539cb8f1c.md
- raw/papers/arxiv-2506.22951.md
tags:
- software-brain-modeling
- neuroimaging-fmri
- functional-connectivity
- resting-state
- connectomics
title: CONN
type: entity
updated: '2026-04-23'
---

# CONN

## Overview

**CONN** (Conn toolbox) is an open-source, MATLAB-based software package for the analysis and visualization of [[functional-connectivity|functional connectivity]] in [[neuroimaging-fmri|resting-state and task-based fMRI]] data. Developed primarily by Alfonso Nieto-Castanon and Susan Whitfield-Gabrieli at the McGovern Institute for Brain Research at MIT, CONN provides a comprehensive suite of tools for preprocessing, denoising, first-level and second-level analysis, and visualization of brain connectivity data.

The toolbox has become one of the most widely used platforms for resting-state fMRI connectivity analysis in the neuroimaging community. CONN implements the **Component-based Noise Correction Method (CompCor)**, a data-driven denoising approach that has become a standard preprocessing step in functional connectivity studies.

## Key Features

### Preprocessing and Denoising

CONN integrates preprocessing pipelines that include:
- **Motion correction** and **slice-timing correction**
- **Coregistration** and **normalization** to MNI space
- **CompCor denoising**: A principal component analysis-based method to remove physiological and motion artifacts without requiring external physiological recordings
- **Band-pass filtering** and **temporal smoothing** options
- **Scrubbing** of high-motion volumes

### Connectivity Analysis

The toolbox supports multiple connectivity measures:
- **Seed-based connectivity** analysis
- **Independent Component Analysis (ICA)** for network identification
- **Graph theory** metrics for network characterization
- **Dynamic connectivity** analysis for time-varying connectivity patterns
- **Effective connectivity** through [[dynamic-causal-modeling|Dynamic Causal Modeling (DCM)]] integration

### Statistical Analysis

CONN implements:
- **General Linear Model (GLM)** for group-level analyses
- **Multivariate parametric methods** for repeated measures
- **Non-parametric permutation tests** for robust statistical inference
- **Regression models** with multiple covariates and confound controls

## Usage in Whole-Brain Modeling

CONN serves as a critical preprocessing and analysis tool in the [[connectome-based-modeling|connectome-based modeling]] pipeline:

1. **Connectome Construction**: CONN generates [[functional-connectivity|functional connectivity matrices]] that serve as empirical constraints for [[whole-brain-modeling|whole-brain models]]. These matrices quantify inter-regional correlations in BOLD signals, providing the functional counterpart to [[structural-connectivity|structural connectivity]] derived from [[neuroimaging-dti|DTI]] tractography.

2. **Model Validation**: Simulated BOLD signals from neural mass models (e.g., [[neural-mass-models|Jansen-Rit]], [[wong-wang-model|Wong-Wang]]) can be compared against empirical CONN-derived connectivity patterns. This validation step is essential in [[the-virtual-brain|The Virtual Brain (TVB)]] workflows where model parameters are optimized to reproduce observed functional connectivity.

3. **Patient-Specific Models**: Individual subject connectivity maps from CONN can inform [[personalized-brain-modeling|personalized brain models]], particularly in clinical applications such as [[epilepsy-modeling|epilepsy]] and [[alzheimers-modeling|Alzheimer's disease]] where individual functional network alterations guide model parameterization.

4. **Multi-modal Integration**: CONN outputs can be combined with [[neuroimaging-dti|structural connectivity data]] from tools like [[software-ants|ANTs]] or FSL to constrain structural-functional coupling in multi-modal modeling approaches.

## Related Software

- [[the-virtual-brain|TVB]] — Whole-brain simulation platform that can use CONN-derived connectivity as input
- [[software-ants|ANTs]] — Advanced normalization and processing tools often used prior to CONN analysis
- [[software-fsl|FSL]] — Alternative fMRI analysis suite for preprocessing and first-level analysis
- [[software-spm|SPM]] — MATLAB-based statistical parametric mapping software; CONN operates as an SPM toolbox
- [[software-bct|BCT (Brain Connectivity Toolbox)]] — MATLAB toolbox for graph-theoretical analysis of connectivity matrices, complementary to CONN's graph theory functions

## References

- Whitfield-Gabrieli, S., & Nieto-Castanon, A. (2012). Conn: A functional connectivity toolbox for correlated and anticorrelated brain networks. *Brain Connectivity*, 2(3), 125-141. https://doi.org/10.1089/brain.2012.0073
- Behzadi, Y., Restom, K., Liau, J., & Liu, T. T. (2007). A component based noise correction method (CompCor) for BOLD and perfusion based fMRI. *NeuroImage*, 37(1), 90-101. https://doi.org/10.1016/j.neuroimage.2007.04.042
- Nieto-Castanon, A. (2020). Handbook of functional connectivity Magnetic Resonance Imaging methods in CONN. *Hilbert Press*. https://doi.org/10.1101/2020.08.05.234243
- www.nitrc.org/projects/conn — Official CONN project repository