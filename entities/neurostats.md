---
created: 2025-01-15
sources:
- raw/papers/arxiv-neurostatx.md
tags:
- software-visualization
- neuroimaging-fmri
- machine-learning
- statistical-analysis
title: NeuroStats
type: software
updated: '2026-05-18'
---
## Overview

NeuroStats is a statistical analysis toolbox designed for the analysis of neuroimaging data, with particular emphasis on [[resting-state]] [[functional connectivity]] analysis in [[fMRI]] datasets. The software provides a comprehensive suite of statistical methods for characterizing brain network properties, including measures of [[functional connectivity]], [[structural connectivity]], and [[effective connectivity]]. Originally developed to address the need for rigorous statistical frameworks in [[connectomics]] research, NeuroStats has become a widely used tool in the neuroimaging community for both hypothesis-driven and exploratory analyses of brain imaging data.

## Motivation and Context

The field of [[neuroimaging]] has seen an explosion of large-scale datasets, particularly following initiatives such as the [[human-connectome-project]] and [[uk-biobank]]. Analyzing these datasets presents significant statistical challenges, including the need to handle high-dimensional data, correct for multiple comparisons, and account for complex dependencies in brain network metrics. NeuroStats was developed to address these challenges by providing a standardized, well-validated framework for statistical inference on neuroimaging-derived metrics.

Traditional approaches to neuroimaging analysis often relied on mass-univariate methods such as [[bold-model]]-based analysis, which treat each brain voxel or region independently. While these methods remain useful for hypothesis-driven studies, they are ill-suited for characterizing the distributed patterns of [[brain network]] dynamics that underlie cognitive processes. NeuroStats instead provides multivariate statistical tools that can capture these complex patterns, making it particularly valuable for [[bold-model]] applications where the interaction between multiple brain regions is of primary interest.

## Key Features

NeuroStats provides a comprehensive set of statistical tools organized into several major categories. **[[connectivity]] analysis** tools include methods for computing and testing pairwise connectivity matrices, with support for both Pearson correlation and more sophisticated measures such as partial correlation and mutual information. The toolbox implements both parametric and non-parametric statistical tests for comparing connectivity patterns between groups, including permutation-based approaches that are robust to the non-normal distribution characteristics often observed in [[resting-state fMRI]] data.

For **network-level analysis**, NeuroStats implements graph-theoretic measures including [[modularity]], centrality, clustering coefficient, and path length metrics. These measures characterize the topological properties of brain networks at the whole-brain level, allowing researchers to assess features such as [[small-world-networks]] organization and [[rich-club]] connectivity. The software includes tools for comparing network topologies between populations and for assessing the significance of network features through permutation testing.

The toolbox also provides **surface-based statistical tools** that enable analysis of neuroimaging data in [[freesurfer]] or [[cifti]] format. These tools are particularly useful for working with data from the [[human-connectome-project]], which uses [[cifti]] format to represent cortical thickness and other surface-based metrics. NeuroStats supports vertex-level statistical analysis with appropriate multiple comparison correction, including false discovery rate control and family-wise error correction.

Additionally, NeuroStats includes **longitudinal analysis** tools for modeling changes in brain structure and function over time. These tools support mixed-effects models that can account for within-subject correlations, making them suitable for analyzing [[developmental-trajectories]], [[aging]] effects, or disease progression in longitudinal neuroimaging studies.

## Relationship to TVB

NeuroStats complements [[the-virtual-brain]] ([[TVB]]) by providing post-processing and statistical analysis capabilities for [[bold-model]] outputs. When using TVB to simulate brain dynamics, researchers often need to validate their models against empirical neuroimaging data by comparing simulated [[functional connectivity]] patterns with observed data from [[fMRI]] or [[meg]] recordings. NeuroStats provides the statistical framework for these comparisons, including tools for computing connectivity matrices from simulated time series and for assessing the similarity between model-derived and empirical connectivity patterns.

The integration between NeuroStats and TVB workflows is particularly valuable in the context of [[personalized-brain-modeling]], where model parameters are fitted to individual subject data. After fitting a TVB model to a subject's [[structural connectivity]] matrix derived from [[diffusion imaging]], researchers can use NeuroStats to compare the resulting simulated dynamics with the subject's empirical [[resting-state]] data. This validation step is essential for ensuring that personalized models accurately capture individual-specific brain dynamics before using them for predictive applications such as [[epilepsy modeling]] or [[brain-stimulation]] targeting.

Furthermore, NeuroStats can be used to analyze the **parameter sensitivity** of TVB models by generating summary statistics from large ensembles of simulations and testing which model parameters most significantly influence output metrics. This application supports the [[parameter-estimation]] workflow in TVB, helping researchers identify which biological parameters most strongly determine the dynamics of interest.

## Related Software

NeuroStats shares conceptual overlap with several other neuroimaging analysis platforms. [[brainstat]] provides similar statistical functionality with a focus on surface-based neuroimaging analysis, while [[nilearn]] offers machine learning tools for neuroimaging data in Python. The [[brain-connectivity-toolbox]] (BCT) provides graph-theoretic network analysis functions, and [[bctpy]] offers a Python implementation of the same functionality. For connectivity analysis in Python, [[mne-connectivity]] provides complementary tools for [[eeg]] and [[meg]] data, and [[brainpy]] offers neural simulation and analysis capabilities.
