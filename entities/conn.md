---
created: 2026-04-23
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/smith-2013-connectomics.md
- raw/papers/woodman-2014.md
- raw/papers/semanticscholar-6f3539cb8f1c.md
- raw/papers/arxiv-2506.22951.md
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-7b51fe740684.md
- raw/papers/wang-etal-2015-gretna.md
tags:
- software-brain-modeling
- neuroimaging-fmri
- functional-connectivity
- resting-state
- connectomics
title: CONN
type: entity
updated: '2026-05-18'
---

# CONN

CONN is a software toolbox used for the pre-processing and analysis of [[resting-state]] [[neuroimaging-fmri|functional MRI]] data, enabling seed-to-voxel correlation analyses that map inter-regional [[functional-connectivity|functional coupling]] across large-scale [[brain-network|brain networks]]. Empirical studies demonstrate its typical role in clinical pipelines: [[raw/papers/semanticscholar-7b51fe740684.md|Issa et al. (2026)]] performed all rs-fMRI pre-processing and group-level analysis with CONN to extract Local Coherence and Intrinsic Connectivity Contrast parameters for Alzheimer’s disease classification, while [[raw/papers/semanticscholar-6f3539cb8f1c.md|Caramia et al. (2026)]] used the toolbox to compute seed-based functional connectivity in frontal regions for cluster headache research. Within the broader methodological landscape surveyed by [[raw/papers/smith-2013-connectomics.md|Smith et al. (2013)]], such resting-state functional connectivity analyses constitute a central window into the brain’s [[connectomics|network-level organization]]. Graph-theoretical characterization of the resulting connectivity matrices is supported by complementary toolboxes, including the Brain Connectivity Toolbox introduced by [[raw/papers/rubinov-sporns-2010.md|Rubinov and Sporns (2010)]] for complex [[network-dynamics|network measures]] and the GraphVar interface described by [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]] for user-friendly graph analyses. Together, these resources position CONN as a practical preprocessing and connectivity-estimation engine within the connectomics ecosystem.

## Overview

**CONN** (Conn toolbox) is an open-source, MATLAB-based software package for the analysis and visualization of [[functional-connectivity|functional connectivity]] in [[fmri|[[resting-state]] and task-based fMRI]] data. Developed primarily by Alfonso Nieto-Castanon and Susan Whitfield-Gabrieli at the McGovern Institute for Brain Research at MIT, CONN provides a comprehensive suite of tools for preprocessing, denoising, first-level and second-level analysis, and visualization of brain connectivity data.

The toolbox has become one of the most widely used platforms for resting-state [[fmri]] [[connectivity]] analysis in the [[neuroimaging]] community. CONN implements the **Component-based Noise Correction Method (CompCor)**, a data-driven denoising approach that has become a standard preprocessing step in functional connectivity studies.

## Key Features

### Preprocessing and Denoising

CONN integrates preprocessing pipelines that include:
- **Motion correction** and **slice-timing correction**
- **Coregistration** and **normalization** to [[mni-space]]
- **CompCor denoising**: A [[principal-component-analysis]]-based method to remove physiological and motion artifacts without requiring external physiological recordings
- **Band-pass filtering** and **temporal smoothing** options
- **Scrubbing** of high-motion volumes

### Connectivity Analysis

The toolbox supports multiple connectivity measures:
- **Seed-based connectivity** analysis
- **[[ica|Independent Component Analysis]] (ICA)** for network identification
- **[[network-dynamics|Graph theory]]** metrics for network characterization
- **Dynamic connectivity** analysis for time-varying connectivity patterns
- **[[effective-connectivity]]** through [[dynamic-causal-modeling|Dynamic Causal Modeling (DCM)]] integration

### Statistical Analysis

CONN implements:
- **General [[linear|Linear Model]] (GLM)** for group-level analyses
- **Multivariate parametric methods** for repeated measures
- **Non-parametric permutation tests** for robust statistical inference
- **Regression models** with multiple covariates and confound controls

## Usage in Whole-Brain Modeling

CONN serves as a critical preprocessing and analysis tool in the [[connectome]]-based modeling pipeline:

1. **Connectome Construction**: CONN generates [[functional-connectivity|functional connectivity matrices]] that serve as empirical constraints for [[whole-brain-modeling|whole-brain models]]. These matrices quantify inter-regional correlations in BOLD signals, providing the functional counterpart to [[structural-connectivity|structural connectivity]] derived from [[dti|DTI]] tractography.

2. **Model Validation**: Simulated BOLD signals from neural mass models (e.g., [[neural-mass-models|Jansen-Rit]], [[wong-wang|Wong-Wang]]) can be compared against empirical CONN-derived connectivity patterns. This validation step is essential in [[tvb|The Virtual Brain (TVB)]] workflows where model parameters are optimized to reproduce observed functional connectivity.

3. **Patient-Specific Models**: Individual subject connectivity maps from CONN can inform [[personalized-brain-modeling|personalized brain models]], particularly in clinical applications such as [[epilepsy-modeling|epilepsy]] and [[alzheimers-modeling|Alzheimer's disease]] where individual functional network alterations guide model parameterization.

4. **Multi-modal Integration**: CONN outputs can be combined with [[dti|structural connectivity data]] from tools like [[ants]] or FSL to constrain structural-functional coupling in multi-modal modeling approaches.

## Related Software

- [[tvb|TVB]] — [[whole-brain]] simulation platform that can use CONN-derived connectivity as input
- ANTs — Advanced normalization and processing tools often used prior to CONN analysis
- FSL — Alternative fMRI analysis suite for preprocessing and first-level analysis
- SPM — MATLAB-based statistical parametric mapping software; CONN operates as an SPM toolbox
- BCT ([[brainvoyager]]) — MATLAB toolbox for graph-theoretical analysis of connectivity matrices, complementary to CONN's graph theory functions

## References

1. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
2. (authors unknown). *Functional [[connectomics]] from Resting-State fMRI*.
3. Woodman et al. (2014). *[[graphvar]]: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))
4. F. Caramia, A. Di Renzo, Irene Giardina, Davide Chiffi, G. Giuliani, G. Sebastianelli, Francesco Casillo, C. Abagnave, Francesca Conti, Francesca Lafavia, Marco Fiorelli, Mao-mei Song, Marta Altieri, Gianluca Coppola. (2026). *Multimodal MRI of episodic cluster headache reveals frontal cortical alterations and network-level connectivity changes*. The Journal of Headache and Pain. [DOI](](https://doi.org/10.1186/s10194-026-02282-6))
5. Ramiro Plüss, Hernán Villota, Patricio Orio. (2025). *Hemispheric-Specific Coupling Improves Modeling of Functional Connectivity Using [[wilson-cowan]] Dynamics*. [Link](](https://arxiv.org/abs/2506.22951))
6. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate [[brain-network]] dynamics*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
7. Sali Issa, Qi Wang, Ruinan Qi, Guangxi Peng, Shi Yin, Qinmu Peng. (2026). *An effective alzheimer disease diagnosis using [[resting-state-fmri]] images and broad learning system.*. Psychiatry research. Neuroimaging. [DOI](](https://doi.org/10.1016/j.pscychresns.2025.112133))
8. Wang, J., Wang, X., Xia, M., Liao, X., Evans, A., & He, Y. (2015). *Gretna: a graph theoretical network analysis toolbox for MATLAB*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2015.04.016))