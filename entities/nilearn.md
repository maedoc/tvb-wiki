---
created: 2024-01-15
sources:
- raw/papers/mijalkov-2017-braph.md
- raw/papers/arxiv-2604.16463.md
- raw/papers/woodman-2014.md
tags:
- neuroimaging
- machine-learning
- software-visualization
- functional-connectivity
- resting-state
title: Nilearn
type: entity
updated: '2026-05-13'
---

**Nilearn** is a Python library for fast and easy statistical learning on [[neuroimaging]] data. It provides tools for decoding, predictive modeling, [[connectivity]] analysis, and visualization of functional MRI data, making a bridge between the broader [[machine-learning]] ecosystem and the specific data structures used in neuroscience research.

## Overview
SUIT (Spatial Unbiased Infratentorial Template) is a [[neuroimaging]] software toolkit specialized for analyzing the human cerebellum and brainstem. The cerebellum is increasingly recognized as a key component of large-scale [[brain-network|brain networks]] implicated in conditions such as epilepsy Matsubara et al. 2026, yet its characterization remains challenging because anatomical depth, complex folding, and unfavorable source orientations relative to standard [[neuroimaging]] sensors consistently limit detectability Matsubara et al. 2026. SUIT addresses these challenges by providing spatial normalization and anatomical template procedures targeted specifically at infratentorial structures, enabling more precise alignment and region definition than conventional whole‑brain templates typically afford. By furnishing dedicated coordinate frameworks for cerebellar and brainstem anatomy, SUIT supports the broader effort to map [[functional-connectivity|functional network]] organization across the entire brain Power et al. 2011 and complements the growing ecosystem of connectivity analysis tools, including graph‑theoretic platforms such as [[braph]] for multimodal network analysis [[braph]] and [[graphvar]] for graph‑theoretical analysis of functional brain connectivity Kruschwitz et al. 2015.

## Motivation and Context

The proliferation of large‑scale neuroimaging datasets—particularly those from the [[human-connectome-project]], [[abide]], and [[uk-biobank]]—created a need for tools that could apply modern machine learning methods to brain imaging data at scale. Traditional neuroimaging analysis packages like [[spm]] and [[fsl]] focused primarily on mass univariate statistics ( voxel‑wise General Linear Models), leaving a gap for multivariate and pattern analysis approaches that had proven powerful in computer vision and cognitive neuroscience. Nilearn emerged to fill this gap by providing declarative interfaces for common neuroimaging operations while leveraging the robust implementations in [[nibabel]] for file I/O and [[nipype]] for pipeline construction. It can also be combined with other neuroimaging toolkits such as [[suit]] for specialized cerebellar analyses. The library's design philosophy emphasizes accessibility: researchers can perform complex analyses with minimal code while maintaining the flexibility to customize every aspect of the workflow.

## Key Features

The decoding capabilities in nilearn support both classification and regression problems, with built‑in cross‑validation schemes appropriate for neuroimaging data. The searchlight implementation allows focal pattern analysis by滑动 windows across the brain, identifying regions where multivariate patterns discriminate conditions. For connectivity analysis, nilearn implements correlation‑based methods, partial correlation, and regularized inverse covariance estimation. The library includes implementations of common atlas representations ([[aal-atlas]], [[desikan‑killiany‑atlas]], [[yeo‑atlas]]) and can project data between volumetric and surface representations. Visualization tools generate publication‑quality figures including glass brain views, connectome circular diagrams, and interactive HTML reports.

## Relationship to TVB

Nilearn complements [[the-virtual-brain]] in several important ways in the [[whole-brain|whole‑brain modeling]] pipeline. First, nilearn is frequently used to estimate functional connectivity matrices from [[resting‑state|resting‑state fMRI]] data, which serve as empirical targets for TVB model fitting or as initialization for model coupling parameters. Second, machine learning decoding approaches in nilearn can identify brain regions and networks relevant for validating TVB model predictions against experimental data— researchers can decode cognitive states from simulated TVB activity and compare to actual fMRI patterns. Third, nilearn's visualization routines produce figures of brain networks and connectivity matrices that mirror TVB output, facilitating comparison between empirical and simulated connectomes. Both nilearn and TVB are Python‑based tools that integrate with the broader neuroimaging ecosystem, and nilearn‑derived connectivity matrices commonly seed TVB neural mass model parameters in [[personalized‑brain‑modeling]] workflows. Additionally, nilearn's atlas handling and parcellation tools ([[brain‑parcellations]]) can generate region definitions used to configure TVB brain network simulations.

## ORPHAN PAGE CONTEXT (suit)
---

## References

1. (authors unknown). *BRAPH: A Pipeline for Brain Connectivity Analysis*.
2. Xiaobo Liu. (2026). *MLE‑Toolbox: An Open‑Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f))
3. Woodman et al. (2014). *GraphVar: A user‑friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))