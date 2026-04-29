---
title: BrainSpace
created: 2024-01-15
updated: 2026-04-29
type: entity
tags: [software-visualization, connectomics, neuroimaging-fmri, resting-state, brain-parcellations, functional-connectivity]
sources: [https://www.nature.com/articles/s41467-020-16367-w, https://brainspace.readthedocs.io/, https://pypi.org/project/brainspace/]
---

# BrainSpace

## Overview

BrainSpace is a Python toolbox for gradient-based analysis of cortical manifold learning and brain connectivity patterns, developed primarily at the Nathan Kline Institute for Psychiatric Research and Stanford University. The toolbox provides a comprehensive set of algorithms for analyzing functional connectivity data through cortical gradient decomposition, parcellation refinement, and manifold learning techniques, with particular emphasis on resting-state fMRI data. BrainSpace is designed to bridge the gap between raw neuroimaging data and connectome-level analyses, offering both preprocessing utilities and advanced gradient analysis methods in a unified environment[^1].

## Key Features

BrainSpace distinguishes itself through several core capabilities that address common bottlenecks in connectome research. The toolbox implements multiple gradient estimation methods including Diffusion Map Embedding, Laplacian Eigenmaps, and Related Embedding methods applied to functional connectivity matrices[^1]. These gradients can be generated at varying spatial scales, allowing researchers to investigate network organization across different resolutions.

The gradient analysis module supports several metrics commonly used in gradient-based connectivity analysis, including eigenvector centrality, gradient decomposition, and manifold learning techniques. For parcellation generation, BrainSpace provides implementations of boundary-based parcellation, winner-take-all clustering, and gradient-derived parcel generation applied to resting-state fMRI time series[^2]. The toolbox also includes null model generation procedures based on matrix randomization, which are essential for statistical inference regarding gradient stability.

A distinctive feature of BrainSpace is its implementation of macrostructural gradient analysis and associated visualization techniques, which enable the identification of principal axes of variation in cortical organization. This capability is particularly valuable for characterizing hierarchical organization of the cerebral cortex and for investigating inter-individual variability in brain functional architecture[^1]. The toolbox also includes visualization utilities for displaying gradient maps, connectivity matrices, and parcellation overlays on brain surfaces through integration with PyCortex and Connectome Workbench.

## Relationship to TVB

BrainSpace and [[TVB]] serve complementary roles in the whole-brain modeling ecosystem. While The Virtual Brain provides a simulation framework for generating synthetic brain dynamics using neural mass models and brain network connectivity, BrainSpace focuses on the analysis of empirical neuroimaging data through gradient-based methods. The connection between these tools becomes most apparent in the parameter fitting pipeline: BrainSpace-derived empirical connectivity matrices and gradient profiles can serve as structural connectivity inputs to TVB simulations, providing subject-specific connectivity profiles extracted from diffusion tensor imaging or functional MRI data[^3].

The workflow connecting these platforms typically involves using BrainSpace to preprocess and analyze resting-state fMRI data, extract functional connectivity networks and cortical gradients, and generate parcellated connectivity matrices that are then imported into TVB for forward simulations. This combined approach allows researchers to validate neural mass models against empirical functional connectivity patterns and to investigate how structural connectivity changes (as measured by DTI tractography) give rise to functional dynamics. The integration is particularly relevant for clinical applications such as epilepsy modeling and personalized brain modeling, where individual subject connectivity profiles can be used to tailor TVB simulations.

## Key Papers

The primary publication describing BrainSpace is "BrainSpace: toolbox for automated characterization of brain connectivity patterns," published in Nature Communications in 2020, which outlines the toolbox architecture and demonstrates its capabilities on both synthetic and real neuroimaging datasets[^1]. The software has been cited in numerous studies applying gradient-based network neuroscience methods to psychiatric and neurological populations[^4].

## Related Software

BrainSpace intersects with a broader ecosystem of connectomics tools. For fMRI preprocessing, it complements packages like [[fMRIPrep]] and [[AFQ]]. For surface-based visualization, the toolbox works alongside [[Connectome Workbench]] and [[PyCortex]]. For statistical analysis of brain maps, it shares functionality with [[BrainStat]] and [[NILearn]]. The Brain Connectivity Toolbox (BCT) provides overlapping graph-theoretic functionality, though BrainSpace emphasizes a more integrated workflow specifically optimized for gradient-based neuroimaging pipelines and cortical manifold analysis.

## References

[^1]: <https://www.nature.com/articles/s41467-020-16367-w>
[^2]: <https://brainspace.readthedocs.io/>
[^3]: <https://pypi.org/project/brainspace/>
[^4]: <https://scholar.google.com/scholar?q=BrainSpace+gradient+neuroimaging>