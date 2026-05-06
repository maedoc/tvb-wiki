---
created: 2025-01-15
sources:
- johnson2007combat
- fortin2018 harmonization
- neuroharmonize-github
- pomponio2019harmonization
- chen2012removing
- wachinger2020combat
- zhao2021longitudinal
- lee2022benchmark
- raw/papers/semanticscholar-a66d2f0a7ffe.md
- raw/papers/semanticscholar-2c80365048c0.md
- raw/papers/woodman-2014.md
tags:
- software-neuroharmonize
- neuroimaging-fmri
- neuroimaging-eeg
- resting-state
- connectomics
- functional-connectivity
- software-graphvar
- software-nilearn
- reproducibility
title: NeuroHarmonize
type: software
updated: '2026-05-06'
---

NeuroHarmonize is a Python toolbox for harmonizing [[neuroimaging]] data across sites, scanners, and acquisition sessions. It implements statistical methods to remove technical variability—such as differences in scanner hardware, acquisition parameters, and preprocessing pipelines—while preserving biologically meaningful signal. The tool is widely used in multi-site neuroimaging studies, particularly those analyzing [[resting-state]] [[functional-connectivity]] patterns, where uncontrolled site effects can confound true inter-individual differences and obscure group-level effects. [@fortin2018; @pomponio2019harmonization]

## Motivation and Context

The proliferation of multi-site neuroimaging consortia—such as the [[human-connectome-project]], [[abide]] (Autism Brain Imaging Data Exchange), [[uk-biobank]], and various clinical consortia—has greatly expanded the scale of available neuroimaging data. However, this expansion introduces a fundamental challenge: data collected across different institutions, scanner manufacturers (Siemens, Philips, GE), field strengths (1.5T, 3T, 7T), and acquisition protocols exhibit systematic differences that are unrelated to the biological variables of interest. These batch effects can manifest as spurious spatial patterns in [[functional-connectivity]] matrices, bias group comparisons, and undermine the reproducibility of findings. [@chen2012removing]

Traditional approaches to addressing site effects include ad hoc regression of site labels, [[linear]] detrending, and inclusion of site as a covariate in statistical models. These methods assume that site effects are simple and homogeneous, which often fails to capture the complex, signal-dependent nature of scanner artifacts. Moreover, some approaches risk removing true biological variance along with technical variance, particularly when site effects interact with the amplitude of the [[bold-signal]].

NeuroHarmonize addresses these limitations by implementing ComBat (ComBat Harmonization), originally developed for genomic data, in conjunction with neurobiologically-informed extensions. [@johnson2007combat] The method uses an empirical Bayes framework to borrow strength across features (e.g., brain regions or [[connectivity]] edges), yielding more stable estimates of site effects than feature-by-feature regression.

## Technical Approach

NeuroHarmonize implements several harmonization strategies, each with distinct assumptions and use cases:

**ComBat Harmonization** is the core method, modeling the observed signal as a linear combination of biological covariates (age, sex, diagnosis) and site/scanner effects. The method estimates batch parameters (location and scale shifts) for each feature using an empirical Bayes approach that pools information across features. The harmonized signal is obtained by regressing out the estimated batch effects while retaining biological signal.

Mathematically, for observation $y_{ij}$ at site $i$ and feature $j$:
$$y_{ij} = \alpha + X\beta + \gamma_i + \delta_i \epsilon_{ij}$$

where $\alpha$ is the intercept, $X$ is the biological covariate matrix with coefficients $\beta$, $\gamma_i$ is the additive batch effect for site $i$, $\delta_i$ is the multiplicative batch effect, and $\epsilon_{ij}$ is the residual error. ComBat estimates $\gamma_i$ and $\delta_i$ using empirical Bayes shrinkage toward prior distributions. [@johnson2007combat; @fortin2018]

**Harmonization with Covariate Adjustment** extends ComBat to handle continuous covariates and interactions between batch and biological variables. This approach allows researchers to model situations where the magnitude of scanner effects varies with disease status, age, or other factors of interest. [@wachinger2020combat] By specifying categorical or continuous covariates and their interactions with site, the method can accommodate heterogeneous batch effects across biological subgroups—for example, when scanner-related artifacts differ between clinical and control populations.

**Longitudinal Harmonization** addresses the case where individuals are scanned multiple times at different sites, enabling both cross-sectional and within-subject harmonization. This extension of ComBat (often implemented in separate packages such as LongituComBat or via neuroCombat's longitudinal mode) models both between-site and within-subject variability while preserving expected biological change over time. [@zhao2021longitudinal] NeuroHarmonize provides utilities for handling such designs, though researchers should verify compatibility with their specific longitudinal data structure.

## Key Features

NeuroHarmonize provides a flexible API compatible with the [[nilearn]] and [[numpy]] ecosystems, accepting input data as NumPy arrays or [[nifti]] images. The toolbox supports harmonization of various neuroimaging-derived features, including regional [[bold-signal]] time series, [[functional-connectivity]] matrices computed via [[nilearn]] or custom pipelines, gray matter volumes from VBM preprocessing, and cortical thickness measures from [[freesurfer]].

A distinguishing feature is the preservation of known biological variance. Unlike simpler regression approaches that may remove any variance correlated with site, NeuroHarmonize's empirical Bayes framework constrains batch effect estimates to reasonable ranges, reducing the risk of over-harmonization. The method optionally supports including age-by-site or diagnosis-by-site interactions to allow for different site effects across groups. [@pomponio2019harmonization]

The toolbox includes diagnostic utilities for assessing harmonization efficacy: comparison of connectivity distributions before and after harmonization, site-stratified [[principal-component-analysis]], and tests for residual site effects. These tools help researchers verify that harmonization has succeeded without inadvertently removing biological signal. [@lee2022benchmark]

## Relationship to TVB

NeuroHarmonize is indirectly related to [[tvb]] (The Virtual Brain) workflows through its role in preprocessing [[functional-connectivity]] data that may serve as input to [[whole-brain-modeling]] pipelines. [[tvb]] leverages empirical [[functional-connectivity]] matrices derived from [[fmri]] or [[meg]] data as the basis for constructing personalized brain network models. When connectivity data originates from multi-site cohorts, harmonization via NeuroHarmonize can reduce scanner-related artifacts before fitting TVB's [[neural-mass-models]] to empirical data.

The relationship is primarily at the data preparation stage rather than direct software integration. Researchers using TVB may employ NeuroHarmonize as part of a broader preprocessing pipeline that includes [[bids]]-compatible tools, [[fmriprep]] for [[bold-signal]] preprocessing, and connectivity estimation via [[nilearn]] or custom scripts. The harmonized connectivity matrices can then be imported into TVB for model inversion or simulation.

## Key Papers

| Paper | Year | Citation | Relevance |
|-------|------|----------|------------|
| Johnson et al. | 2007 | [@johnson2007combat] | Original ComBat method for genomic data |
| Fortin et al. | 2018 | [@fortin2018] | ComBat adaptation for neuroimaging (neuroCombat) |
| Pomponio et al. | 2019 | [@pomponio2019harmonization] | Harmonization of cortical thickness across sites |
| Chen et al. | 2012 | [@chen2012removing] | Removing batch effects in neuroimaging |
| Wachinger et al. | 2020 | [@wachinger2020combat] | ComBat with covariate interactions |
| Zhao et al. | 2021 | [@zhao2021longitudinal] | Longitudinal ComBat methods |
| Lee et al. | 2022 | [@lee2022benchmark] | Benchmarking harmonization methods |

## Related Software

NeuroHarmonize addresses a similar problem to other harmonization tools in the neuroimaging ecosystem. [[graphvar]] provides graph-theoretical analysis of connectivity matrices and includes some harmonization capabilities. The R package `neuroCombat` offers ComBat harmonization for neuroimaging data. [[nilearn]] includes utilities for confound regression that address some harmonization use cases, though with less sophisticated statistical machinery. Tools like [[c-pac]] and [[fmriprep]] include optional harmonization modules that integrate ComBat-style approaches. Cross-platform harmonization methods are an active area of development in the [[reproducibility]] literature for multi-site neuroimaging studies.

The choice between tools depends on the specific study design: NeuroHarmonize offers flexibility for custom analyses, while integrated pipelines like [[c-pac]] provide end-to-end processing for standardized datasets.

## References

1. Zheng Ren, Patrick S. Sadil, Martin A. Lindquist. (2026). *MV-ComBat and MV-CovBat: Multivariate Frameworks for Joint Harmonization of Multi-Metric Neuroimaging Data*. bioRxiv. [DOI](https://doi.org/10.64898/2026.02.05.704069)
2. Zhen Zhou, B. Fischl, I. Aganj. (2025). *Harmonization of Structural Brain Connectivity Through Distribution Matching*. Human Brain Mapping. [DOI](https://doi.org/10.1002/hbm.70257)
3. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)