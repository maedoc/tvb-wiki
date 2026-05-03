---
title: PALM
created: 2024-01-15
updated: 2026-05-03
type: software
tags: [software-visualization, neuroimaging-fmri, neuroimaging-pet, parameter-estimation, variational-bayes]
sources: []
---

# PALM

## Overview

PALM (Permutation Analysis of Linear Models) is a high-performance software toolbox for performing non-parametric statistical inference on neuroimaging data. Developed primarily by Anderson Winkler and colleagues at the University of Oxford, PALM implements permutation-based testing procedures that make minimal distributional assumptions, making it particularly robust for analyzing complex neuroimaging datasets where parametric assumptions may not hold. The tool operates on NIfTI format data and integrates with common neuroimaging preprocessing pipelines, enabling researchers to conduct mass univariate analyses with proper multiple comparison correction across the entire brain volume. PALM achieves computational efficiency through parallel processing and employs various permutation schemes including sign-flipping and row/column permutations for different design matrix structures.

## Key Features

PALM implements several innovative statistical procedures that distinguish it from conventional parametric approaches. The toolbox supports arbitrary linear models, allowing for complex experimental designs with multiple factors, covariates, and interactions. It provides exact permutation inference for small sample sizes and asymptotic approximations for larger datasets, ensuring computational feasibility regardless of study size. The software implements the celebrated theory developed by Anderson and Winkler for creating valid permutation tests under various dependence structures, making it applicable to both between-subject and within-subject designs. PALM also supports voxel-level and cluster-level inference, with cluster definition based on either topological thresholding or suprathreshold clusters.

A distinguishing capability of PALM is its implementation of threshold-free cluster enhancement (TFCE), which provides a continuous measure of cluster significance without requiring arbitrary cluster definition thresholds. This approach combines the benefits of voxel-wise and cluster-wise inference while avoiding the sensitivity to user-defined parameters that plagues traditional cluster-based methods. PALM additionally supports family-wise error (FWE) rate control via maximum statistic permutation, and false discovery rate (FDR) control via q-values, giving researchers flexibility in choosing their error criterion.

## Relationship to TVB

While PALM is not directly part of The Virtual Brain ecosystem, it serves a complementary role in the broader whole-brain modeling workflow. PALM is commonly used in the preprocessing and validation stages of [[whole-brain modeling]] projects, where researchers need to identify significant brain regions or networks from empirical neuroimaging data before constructing [[structural connectivity]] matrices or fitting [[neural mass models]]. The tool's ability to perform robust group-level comparisons makes it valuable for identifying differences in [[functional connectivity]] patterns between patient populations and controls, which can inform the specification of personalized [[brain network]] models in TVB. Additionally, PALM can be used to analyze simulated data from TVB, comparing model-derived patterns against empirical findings from real neuroimaging experiments.

## Technical Details

### Permutation Framework

PALM operates by generating an empirical reference distribution through random permutation of the data. For between-subject designs, this typically involves shuffling group labels; for within-subject designs, sign-flipping or exchangeable blocks may be used. The key theoretical contribution of the method is the demonstration that valid inference requires accounting for the dependency structure inherent in neuroimaging data—both across voxels within a single brain and across subjects within a study. PALM implements the exchangeability block and bilateral symmetry approaches that preserve relevant dependencies while creating valid permutations.

### Computational Architecture

The toolbox is written in MATLAB with C-MEX extensions for computationally intensive operations, ensuring compatibility with the broader neuroimaging software ecosystem while maintaining speed. PALM can be run interactively via its graphical user interface or scripted for automated batch processing. It integrates natively with tools from the [[fsl]] suite and can be incorporated into [[nipype]] workflows for reproducible pipelines.

## Relationship to Related Software

PALM occupies a similar niche as [[fsl-randomise]] in the FSL suite, which also implements permutation-based inference for neuroimaging data. However, PALM offers greater flexibility in model specification and supports a wider range of permutation schemes. Compared to [[SPM]]'s classical parametric approaches, PALM provides more robust inference when sample sizes are small or when distributional assumptions are violated. The tool differs from Bayesian approaches implemented in packages like [[DCM]] in that it provides frequentist inference rather than posterior probability maps, though the two approaches can be used complementarily.

## Key Papers

The theoretical foundation for PALM is established in Winkler et al. (2014), which describes the permutation framework and demonstrates its application to various neuroimaging paradigms. The TFCE method is described in Smith and Nichols (2009), which PALM implements. The exchangeability block framework draws on the seminal work of Anderson and Winkler in permutation testing theory.

## Related Software

- [[fsl]]
- [[fsl-randomise]]
- [[SPM]]
- [[nilearn]]
- [[nipype]]
- [[nifti]]
- [[connectome-workbench]]