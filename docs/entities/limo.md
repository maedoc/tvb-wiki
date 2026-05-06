---
created: 2025-01-15
sources:
- raw/papers/arxiv-2604.16463.md
- raw/papers/sanz-leon-2013.md
- raw/papers/woodman-2014.md
tags:
- software-modeling
- neuroimaging-eeg
- neuroimaging-meg
- statistical-analysis
- eeglab
title: Limo
type: entity
updated: '2026-05-04'
---

# Limo

## Overview

Limo ([[linear]] Modeling) is a MATLAB-based toolbox for the statistical analysis of electroencephalography (EEG) and magnetoencephalography (MEG) data. The toolbox implements mass univariate linear modeling approaches, allowing researchers to perform voxel-based or vertex-based analyses across the entire scalp or cortical surface. Limo provides a comprehensive framework for estimating linear models at each electrode or source location separately, enabling the detection of spatio-temporal patterns of neural activity related to experimental conditions, cognitive processes, or clinical markers. The tool is designed to integrate seamlessly with [[eeglab]], one of the most widely used open-source environments for EEG and MEG data processing, making it accessible to the broad [[neuroimaging]] community.

## Key Features

Limo implements several key functionalities that distinguish it from traditional ERP analysis approaches. The toolbox supports **mass univariate testing**, where a separate statistical test is performed at each electrode or source location, providing fine-grained spatio-temporal resolution of neural effects without the need for a priori region-of-interest selection. This approach is particularly valuable in exploratory analyses where the spatial distribution of effects is unknown. Limo provides implementations of **General Linear Model (GLM)** analysis for both categorical (e.g., condition contrasts) and continuous (e.g., behavioral correlations) predictors, allowing flexible modeling of experimental designs ranging from simple A/B comparisons to complex mixed-effects layouts.

The toolbox incorporates rigorous approaches to **multiple comparisons correction**, implementing cluster-based permutation tests, false discovery rate (FDR) control, and family-wise error rate (FWER) adjustments. These corrections are essential given the thousands of tests performed across electrodes and time points. Limo also supports **time-frequency decomposition** using wavelet or Hilbert transform methods, enabling the analysis of oscillatory activity in different frequency bands (delta, theta, alpha, beta, gamma) and the relationship between phase and amplitude across these bands. The toolbox handles both **between-subject and within-subject designs**, with options for random effects modeling and mixed-design analyses.

## Relationship to TVB

While Limo operates primarily in the analysis domain rather than forward modeling, it maintains important connections to whole-brain simulation frameworks like [[the-virtual-brain]]. Both tools share a commitment to **computational modeling** of brain activity—TVB simulates large-scale [[network-dynamics]] using [[neural-mass-models]], while Limo provides the statistical inverse methods needed to **parameterize such models from empirical data**. In practice, researchers using TVB for [[personalized-brain-modeling]] often employ Limo (or similar EEG/MEG analysis toolboxes like Fieldtrip and [[eeglab]] directly) to extract empirical features—such as ERP amplitudes, oscillation power spectra, or connectivity estimates—that serve as targets for model fitting and parameter estimation. The relationship is thus complementary: Limo enables the data-driven characterization of individual [[brain-dynamics]] that TVB then reproduces in silico.

Limo also supports the broader workflow of **[[functional-connectivity]]** analysis, computing correlation-based or coherence-based measures that can inform the construction of [[whole-brain]] connectomes. These connectivity estimates, typically derived from [[resting-state]] or task-based EEG/MEG recordings, can be used to define the **[[structural-connectivity]]** matrices that constrain TVB simulations. Additionally, the toolbox's [[source-localization]] capabilities, when combined with head models from techniques like boundary-element-method or finite-element-method, provide the cortical activity estimates needed for comparison with TVB forward predictions.

## Key Papers

The Limo toolbox was introduced by Arnaud Delorme and colleagues, building on the mass univariate analysis philosophy pioneered in the [[fmri]] community. Key methodological publications establishing the theoretical foundation for mass univariate EEG analysis appeared in the early 2000s, establishing the statistical framework that Limo implements. The toolbox has been applied in numerous studies of cognitive neuroscience, including research on **working memory**, **attention**, **perception**, and **clinical populations** such as patients with schizophrenia or epilepsy. Several validation studies have demonstrated Limo's ability to recover known experimental effects from simulated and empirical EEG data, providing confidence in its statistical inference procedures.

## Technical Implementation

Limo operates on EEG/MEG data structured in the EEGLAB format, expecting data matrices organized as channels × time points × trials (or epochs). The basic workflow involves first **preprocessing** the data using EEGLAB functions (filtering, artifact rejection, epoching), then specifying the linear model design matrix with condition codes and potential covariates. The core estimation procedure fits a GLM at each electrode or source location using ordinary least squares or, for repeated-measures designs, mixed-effects approaches. Test statistics are computed for relevant contrasts (e.g., condition A vs. condition B), and p-values are adjusted for the multiple tests performed across the spatio-temporal domain.

The toolbox stores results in structured formats that integrate with EEGLAB's data visualization functions, enabling the creation of scalp maps, topographic animations, and butterfly plots showing significant time windows. Output includes both raw test statistics and p-value maps, allowing researchers to set custom thresholds or visualize the full statistical landscape. Limo's modular architecture allows researchers to customize individual analysis Steps—using custom preprocessing pipelines, alternative GLM estimators, or novel multiple comparison corrections—while maintaining compatibility with the core analysis framework.

## Related Software

Limo belongs to a broader ecosystem of EEG/MEG analysis tools that share similar philosophical commitments to mass univariate analysis and open-source distribution. **[[eeglab]]** provides the primary integration platform, including the data structures, visualization tools, and preprocessing pipelines that Limo extends. **Fieldtrip**, developed at the Donders Institute, offers comparable mass univariate capabilities with additional features for source analysis and beamforming, representing the main alternative to Limo for EEG/MEG statistical modeling. **Mne Python** provides a Python-based alternative implementing similar functionality, with growing adoption in the research community. Within the TVB ecosystem, Limo's output can inform **[[parameter-estimation]]** procedures and **[[model-validation]]** workflows, where empirical EEG features derived from Limo are compared against simulated activity. Tools for **[[connectivity]]** estimation such as **[[eegnet]]** or **[[sift]]** complement Limo's analysis by providing frequency-domain and information-theoretic connectivity measures.

## References

1. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f))
2. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate [[brain-network]] dynamics*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
3. Woodman et al. (2014). *[[graphvar]]: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))