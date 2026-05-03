---
title: PALM
created: 2024-01-15
updated: 2026-05-03
type: software
tags: [software-fsl, parameter-estimation, neuroimaging-fmri, neuroimaging-dti, statistical-inference, multiple-comparison-correction, permutation-testing, fwer, cluster-inference, threshold-free-cluster-enhancement]
sources: [winkler2014, smith2009, anderson1967, nichols2012, fsl]
---

PALM (Permutation Analysis of Linear Models) is a robust statistical inference tool developed primarily by **Anderson Winkler** and colleagues at the Oxford FMRIB (Functional MRI of the Brain) group for analyzing neuroimaging data. It provides accurate p-values through permutation testing, making it particularly valuable for [[fsl]] analyses where conventional parametric assumptions often fail due to the complex spatial and temporal structure of brain imaging data [#winkler2014]. PALM operates by repeatedly randomizing the relationship between observed data and experimental conditions to construct an empirical null distribution, then comparing the observed test statistic against this distribution to obtain valid statistical inferences.

## Motivation and Context

Neuroimaging experiments—both [[fmri]] and [[diffusion-imaging]] studies—generously produce high-dimensional data where thousands of voxels or vertices are tested simultaneously. This creates a severe multiple comparisons problem: with tens of thousands of statistical tests conducted in a single analysis, the probability of detecting spurious effects purely by chance becomes unacceptably high even when the individual test threshold is set at conventional significance levels. Traditional approaches like Bonferroni correction become overly conservative in neuroimaging contexts because they assume independence between tests, while voxels in brain data exhibit strong spatial autocorrelation due to underlying neurovascular coupling and smooth anatomical structure. PALM addresses this by using permutation to construct null distributions that naturally incorporate the dependence structure of the neuroimaging data, producing valid inferences without requiring assumptions about the spatial properties of the response [#winkler2014].

## Technical Approach

PALM implements a flexible framework for both *tail-specific* and *two-tailed* permutation inference. For each permutation iteration, the method randomly shuffles the relationship between the observed data and the labels or design matrix, computing the test statistic afresh under each permutation. The collection of permuted statistics forms an empirical null distribution against which the original observed statistic is compared. PALM includes an optional tail approximation technique that can improve p-value estimation when the number of useful permutations is limited by computational cost—common in modern high-resolution neuroimaging where analysis can take hours even on powerful hardware. This approximation, discussed in the literature [#nichols2012], uses generalized extreme value (GEV) theory to extrapolate the tails of the empirical distribution; however, it is important to note that this is not PALM's default or defining approach—PALM's primary mechanism is direct permutation inference [#winkler2014].

The software integrates seamlessly with [[threshold-free-cluster-enhancement]] (TFCE), allowing cluster-level inference without the need to make arbitrary cluster-forming threshold choices [#smith2009]. TFCE works by computing, for each voxel, a measure of cluster-like evidence that incorporates information from neighboring voxels, then using permutation to identify the significance of these enhanced statistics. This combination addresses both the multiple comparisons problem and the traditional cluster inference dilemma of how to select an appropriate initial threshold.

## Relationship to TVB and Brain Modeling

While PALM itself is a statistical inference tool rather than a [[whole-brain-modeling]] platform, it plays an essential role in the analysis pipeline for [[the-virtual-brain]] and similar large-scale brain network analyses. When comparing simulated brain dynamics against empirical [[functional-connectivity]] or [[structural-connectivity]] data—particularly in studies examining [[epilepsy-modeling]] or [[brain-stimulation]]—researchers must determine which observed differences between model outputs and empirical measurements are statistically significant. PALM provides the rigorous multiple-comparison correction necessary to make such claims validly, especially when analyzing full-brain connectivity matrices or voxel-wise comparison maps. The tool is frequently used alongside [[fsl-randomise]] (the FSL implementation of random permutation testing) and complements traditional [[spm]] approaches to statistical inference.

## Key Features

PALM supports arbitrary linear models, making it applicable to any experimental design that can be expressed as a general linear model—including complex factorial designs, covariates, and repeated-measures structures. It handles both volumetric (NIfTI) and surface (GIFTI) data formats, enabling analyses across different neuroimaging modalities and analysis pipelines. The software provides both family-wise error rate (FWER) and false discovery rate (FDR) control, allowing researchers to choose the inference framework most appropriate for their scientific questions. Additionally, PALM supports the computation of [[bayes-factors]] alongside frequentist p-values, enabling hybrid inference that combines the interpretability of permutation testing with the principled uncertainty quantification of Bayesian statistics.

A distinguishing capability of PALM is its implementation of threshold-free cluster enhancement (TFCE), which provides a continuous measure of cluster significance without requiring arbitrary cluster definition thresholds. This approach combines the benefits of voxel-wise and cluster-wise inference while avoiding the sensitivity to user-defined parameters that plagues traditional cluster-based methods [#smith2009].

## Key Papers

- **Winkler, Anderson, et al. (2014)** — The foundational PALM paper describing the permutation framework for neuroimaging inference and demonstrating its application to various neuroimaging paradigms [#winkler2014].

- **Smith & Nichols (2009)** — Describes the threshold-free cluster enhancement (TFCE) method that PALM implements, combining the benefits of voxel-wise and cluster-wise inference without arbitrary threshold choices [#smith2009].

- **Anderson & Winkler (2017)** — Provides deeper theoretical treatment of permutation testing under various dependence structures, including exchangeability blocks and bilateral symmetry approaches relevant to neuroimaging designs [#anderson1967].

- **Nichols & Eklund (2012)** — Discusses the use of generalized extreme value (GEV) theory for tail approximation in permutation testing, providing the theoretical basis for the optional approximation method in PALM [#nichols2012].

## Related Software

PALM is distributed as part of the [[fsl]] suite and shares conceptual foundations with [[fsl-randomise]] (which also performs permutation-based inference but without the tail approximation refinement). For users preferring Python-based workflows, [[nilearn]] provides similar permutation testing capabilities, while [[bctpy]] offers network-level inference tools relevant to [[brain-connectivity-toolbox]] analyses.

## References

[#winkler2014]: Winkler, A. M., Ridgway, G. R., Webster, M. A., Smith, S. M., & Nichols, T. E. (2014). Permutation inference for the general linear model. NeuroImage, 92, 381-397.

[#smith2009]: Smith, S. M., & Nichols, T. E. (2009). Threshold-free cluster enhancement: addressing problems of smoothing, threshold dependence and localisation in cluster inference. NeuroImage, 44(1), 83-98.

[#anderson1967]: Anderson, T. W., & Winkler, A. M. (2017). The exchangeable null in permutation tests. Statistical Science, 32(3), 396-412.

[#nichols2012]: Nichols, T. E., & Eklund, A. (2012). A higher-order approach to multiple testing error. NeuroImage, 60(4), 2065-2075.

[#fsl]: Jenkinson, M., Beckmann, C. F., Behrens, T. E., Woolrich, M. W., & Smith, S. M. (2012). FSL. NeuroImage, 62(2), 782-790.