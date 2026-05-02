---
title: BrainSMASH
created: 2026-05-02
updated: 2026-05-02
type: entity
tags: [software-brain-modeling, software-visualization, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, spatial-analysis, null-models, statistical-testing, connectomics]
sources:
- https://github.com/murraylab/brainsmash
- https://brainsmash.readthedocs.io/
- https://doi.org/10.1016/j.neuroimage.2020.117038
---

## Overview

BrainSMASH (Brain Surrogate Maps with Autocorrelated Spatial Heterogeneity) is a Python-based computational platform for statistical testing of spatially autocorrelated brain maps. At its core, BrainSMASH generates surrogate brain maps whose spatial autocorrelation characteristics are quantitatively matched to those of an empirical target brain map, enabling researchers to construct appropriate null distributions for hypothesis testing. The software addresses a fundamental problem in [[neuroimaging]] research: conventional statistical tests assume independence between observations, but brain maps exhibit strong spatial autocorrelation due to the underlying [[structural-connectivity]]—adjacent brain regions tend to have similar values in [[fmri]], [[eeg]], [[meg]], and other neuroimaging modalities, violating this independence assumption.

The tool was developed by Joshua B. Burt and John D. Murray at Yale University's Murray Lab [@brainsmash-github], with contributions from Ross Markello at the Montreal Neurological Institute [@brainsmash-github], and was released in 2020 alongside the seminal paper "Generative modeling of brain maps with spatial autocorrelation" published in NeuroImage [@burt2020]. BrainSMASH provides implementations for both parcellated brain data (regional time series or summary statistics) and dense vertex-level cortical data, making it versatile for analyzing outputs from diverse neuroimaging pipelines including those using [[connectome-workbench]].

## Motivation and Background

The statistical analysis of brain maps presents unique challenges that distinguish it from standard statistical problems. When comparing two brain maps—for example, testing whether [[functional-connectivity]] patterns correlate with gene expression, or whether [[structural-connectivity]] predicts [[resting-state]] activity—the non-independence of nearby brain regions creates substantial methodological complications. Naive permutation tests that shuffle values across the brain without accounting for spatial structure produce anti-conservative p-values, inflating false positive rates and potentially leading to spurious conclusions about brain-behavior relationships.

This problem is particularly acute in [[connectomics]], where researchers increasingly examine relationships between multiple types of brain maps—structural connectivity matrices, functional connectivity derived from [[fmri]] or [[eeg]], gene expression data from the [[allen-brain-atlas]], and various derived metrics. The fundamental insight driving BrainSMASH's development is that to properly test hypotheses about brain map relationships, researchers need null models that preserve the spatial autocorrelation structure of the data while removing the specific relationship being tested. By generating surrogate maps that match the empirical variogram (a measure of spatial autocorrelation), BrainSMASH enables proper statistical inference in the presence of spatial dependence.

The conceptual framework builds on earlier null model approaches in brain imaging, including spin tests that rotate cortical surfaces (Alexander-Bloch et al., 2018) and Moran spectral randomization (Wagner & Dray, 2015). However, BrainSMASH's variogram-matching approach offers advantages in its generality: it works with any distance matrix (geodesic, Euclidean, or custom), applies equally well to parcellated and vertex-level data, and makes minimal assumptions about the underlying spatial generating process.

## Technical Approach

BrainSMASH implements a variogram-matching algorithm to generate surrogate brain maps [@burt2020]. The variogram quantifies how the variance of brain map values changes as a function of pairwise distance between regions—brain maps with strong spatial autocorrelation show high variance at small distances that plateaus at larger distances, while spatially independent maps have flat variograms [@brainsmash-docs]. The algorithm proceeds in three main steps: first, values from the empirical brain map are randomly permuted; second, the permuted values are smoothed at multiple spatial scales using a kernel (by default, exponential decay); third, the surrogate whose variogram best matches the empirical variogram is selected as the final surrogate map. This process is repeated many times to build a null distribution [@burt2020].

The software provides two primary classes for different data types [@brainsmash-docs]. The **Base** class handles parcellated brain maps (one value per region) and loads the full distance matrix into memory, making it computationally efficient for typical parcellations with 100-400 regions. The **Sampled** class addresses the memory constraints of dense vertex-level data (typically ~32,000 vertices per hemisphere), using memory-mapped arrays and random sampling to enable surrogate generation without loading the entire distance matrix [@brainsmash-docs]. Both classes support parameters controlling the smoothing kernel (defaulting to exponential decay), the proportion of nearest neighbors used during optimization, and whether to resample values from the empirical distribution.

For users working with [[connectome-workbench]] format files (CIFTI and GIFTI), BrainSMASH includes utilities for loading neuroimaging data and computing geodesic distance matrices from cortical surface meshes. The software can also handle volumetric data, computing 3D Euclidean distance matrices from arbitrary voxel coordinates. Goodness-of-fit functions allow users to evaluate how well their surrogate maps' variograms match the empirical data, helping to guide parameter selection.

## Key Features

BrainSMASH offers several capabilities that make it valuable for [[whole-brain-modeling]] and [[connectomics]] research. The tool supports **multiple data modalities**: cortical surface data (both hemispheres), subcortical volumetric data, and parcellated data from any brain parcellation scheme [@brainsmash-docs]. The **flexible distance specification** means users can provide geodesic distances from surface meshes, Euclidean distances from volumes, or any custom distance matrix reflecting the spatial structure of their data. The **resampling option** preserves the exact value distribution of the empirical brain map in each surrogate, though this may slightly degrade variogram matching—a option researchers can toggle based on their specific hypothesis [@brainsmash-docs].

The software includes **parallelization** capabilities for generating many surrogate maps simultaneously using Python's multiprocessing framework, **batch processing** support for running multiple brain maps through the same pipeline, and **deterministic seeding** for reproducible research [@brainsmash-docs]. A critical feature is the **variogram evaluation module**, which quantifies how well surrogates match the empirical autocorrelation structure and helps users select appropriate parameters. The integration with [[connectome-workbench]] makes BrainSMASH particularly useful for analyzing data from the [[human-connectome-project]] and similar large-scale neuroimaging initiatives.

## Relationship to Whole-Brain Modeling

BrainSMASH plays an important but distinct role in the [[whole-brain-modeling]] ecosystem [@burt2020; @markello2021]. While [[TVB]] and similar simulators generate forward models that predict brain activity from anatomical connectivity and neural dynamics, BrainSMASH addresses the complementary problem of statistical inference: given observed brain maps (from empirical data or from simulations), how should we test hypotheses about relationships between brain regions or between brain maps and other variables?

In practice, BrainSMASH integrates with whole-brain modeling workflows in several ways. Researchers using TVB can generate simulated brain maps (regional time series, frequency spectra, or derived metrics) and use BrainSMASH to test whether observed relationships in empirical data could arise by chance given the spatial autocorrelation structure. Conversely, when comparing TVB simulation outputs to empirical brain maps, BrainSMASH provides proper null models for assessing correspondence. The tool complements other analysis packages in the TVB ecosystem, including [[nilearn]] for general neuroimaging processing, [[brainspace]] for dimensionality reduction and manifold learning, and [[BCTpy]] for graph-theoretic analysis [@burt2020].

## Key Papers

The primary reference for BrainSMASH is Burt, J.B., Helmer, M., Shinn, M.W., Anticevic, A., & Murray, J.D. (2020). "Generative modeling of brain maps with spatial autocorrelation" published in NeuroImage (Volume 220, 117038). This paper introduces the variogram-matching method, demonstrates its application to cortical and subcortical data, shows how spatial autocorrelation inflates false positive rates in brain map comparisons, and applies the method to gene set enrichment analysis testing relationships between genetic data and brain structure. The authors show that failing to account for spatial autocorrelation leads to substantially inflated false positive rates—in some cases changing p-values by several orders of magnitude.

Related methodological work includes the earlier spatial autoregressive approach by Burt et al. (2018) exploring hierarchy in cortical networks, and the comparison of spatial null models by Markello and Misic (2021) evaluating BrainSMASH and alternative methods. The broader context includes foundational work on spin tests (Alexander-Bloch et al., 2018), Moran spectral randomization (Wagner & Dray, 2015), and network-based statistics (Zalesky et al., 2010).

## Related Software

BrainSMASH addresses a specific statistical need that complements several other tools in the neuroimaging ecosystem. For general surface-based visualization and analysis, [[connectome-workbench]] provides the primary tools for working with CIFTI format files and computing surface distances—BrainSMASH's Workbench utilities integrate directly with this ecosystem. The [[brainspace]] library provides complementary manifold learning and dimensionality reduction approaches for brain network data.

Alternative null model approaches include the **neuromapr** R package implementing multiple null model methods including variogram matching, and the **brainSMASH** approach has been ported to other frameworks. For whole-brain simulation and modeling, researchers often combine BrainSMASH's statistical framework with simulators like [[TVB]], [[NEST]] for spiking neural networks, or [[brian2]] for neural modeling. The analysis of brain maps from any of these tools benefits from proper spatial null models when testing hypotheses about brain organization.

## References

- **burt2020** — Burt, J.B., Helmer, M., Shinn, M.W., Anticevic, A., & Murray, J.D. (2020). Generative modeling of brain maps with spatial autocorrelation. *NeuroImage*, 220, 117038. https://doi.org/10.1016/j.neuroimage.2020.117038

- **markello2021** — Markello, R.D., & Misic, B. (2021). Comparing spatial null models for brain maps. *NeuroImage*, 236, 118052. https://doi.org/10.1016/j.neuroimage.2021.118052

- **brainsmash-github** — BrainSMASH GitHub Repository. https://github.com/murraylab/brainsmash

- **brainsmash-docs** — BrainSMASH Documentation. https://brainsmash.readthedocs.io/

- Viladomat, J., Mazumder, R., McInturff, A., McCauley, D. J., & Hastie, T. (2014). Assessing the significance of global and local correlations under spatial autocorrelation: A nonparametric approach. *Biometrics*, 70(2), 409-418.

- Alexander-Bloch, A.F., Shou, H., Liu, S., Patel, T.D., Blob, Z., Raznahan, A., ... & Bullmore, E.T. (2018). On testing for spatial correspondence between maps of human brain structure and function. *NeuroImage*, 178, 540-551.

- Wagner, H.H., & Dray, S. (2015). Generating spatially constrained null models for community ecology analysis. *Ecological Informatics*, 30, 292-301.

- Zalesky, A., Fornito, A., & Bullmore, E.T. (2010). Network-based statistic: Identifying differences in brain networks. *NeuroImage*, 53(4), 1197-1207.