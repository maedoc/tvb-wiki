---
created: 2026-04-29
sources:
- Vos de Wael et al. (2020) NeuroImage
- Margulies et al. (2016) PNAS
- raw/papers/woodman-2014.md
- raw/papers/mijalkov-2017-braph.md
- raw/papers/arxiv-2603.29903.md
tags:
- software-brain-modeling
- software-visualization
- connectomics
- gradient-analysis
title: BrainSpace
type: entity
updated: '2026-04-30'
---

## Overview

BrainSpace is an open-source Python and MATLAB toolbox designed for the analysis of macroscale gradients in the [[connectome]]. Developed to address the growing interest in continuous, manifold-based representations of brain organization, BrainSpace provides a unified framework for identifying, aligning, and visualizing gradient patterns across the cerebral cortex. The toolbox implements state-of-the-art algorithms for dimensionality reduction and null model generation, enabling researchers to extract intrinsic patterns of [[functional-connectivity]] variation without relying on discrete [[brain-parcellations]].

## Motivation and Context

Traditional approaches to [[connectomics]] have relied heavily on parcellated representations of the brain, where the cortex is divided into discrete regions based on [[neuroimaging]] data. However, evidence has accumulated suggesting that brain organization is better represented as a continuous manifold rather than a set of disjoint parcels. Gradient analysis approaches this problem by identifying smooth, continuous axes of variation in [[functional-connectivity]] patterns, revealing the principal modes of co-variation that organize the brain's intrinsic activity [1].

The motivation for BrainSpace emerged from the need to unify the fragmented software landscape for gradient analysis. Prior to its development, researchers implemented gradient detection algorithms using disparate tools, often lacking proper null models for statistical validation or standardized procedures for cross-dataset alignment. BrainSpace addresses these limitations by providing a comprehensive, well-documented toolkit that implements best practices from the literature while remaining accessible to both Python and MATLAB users.

## Key Features

### Gradient Identification

BrainSpace implements multiple algorithms for gradient extraction, including diffusion map embedding, [[principal-component-analysis]], and Laplacian eigenmapping [1]. The toolbox uses *affinity kernels* to construct similarity matrices from [[functional-connectivity]] data, where the kernel bandwidth is adaptively determined based on the local density of data points. This approach ensures that gradients capture both local and global structure in the connectivity manifold.

### Gradient Alignment

A major challenge in gradient analysis is ensuring comparability across individuals or datasets. BrainSpace provides robust alignment procedures including Procrustes analysis and joint embedding approaches that identify correspondence between gradient maps from different subjects [1]. These methods are particularly valuable for group-level analyses and cross-dataset generalization, enabling researchers to characterize consistent gradient patterns across the [[hcp-dataset]] and other large-scale neuroimaging repositories.

### Null Models

Statistical validation of gradient results requires appropriate null models that preserve important confounds. BrainSpace implements several null model generation strategies, including spin permutations that preserve spatial proximity and Moran spectral randomization that maintains the spatial autocorrelation structure of the data [1][2]. These null models are essential for determining whether observed gradient patterns exceed chance expectations given the spatial embedding of cortical regions.

### Visualization

The toolbox provides integrated visualization capabilities for gradient maps, including surface-based rendering using [[pycortex]] and [[connectome-workbench]] formats. Researchers can visualize individual gradient maps, group-averaged patterns, or overlay gradient information on standard cortical surfaces. The visualization suite supports both publication-quality static figures and interactive exploration of three-dimensional gradient patterns.

## Relationship to The Virtual Brain

BrainSpace complements [[the-virtual-brain]] ([[tvb]]) in the analysis pipeline for [[whole-brain-modeling]]. While TVB focuses on *generating* simulated brain activity through [[neural-mass-models]] and [[structural-connectivity]] constraints, BrainSpace provides tools for *characterizing* the resulting gradient patterns in simulated data [1]. This combination enables researchers to compare simulated gradients against empirically-derived patterns from [[fmri]] data, facilitating model validation and parameter optimization. The gradient analysis capabilities in BrainSpace can be applied to TVB simulation outputs to assess how [[connectome]] parameters influence large-scale cortical organization.

## Key Papers

The foundational reference for cortical gradient analysis is the study by Margulies et al. (2016) in *Proceedings of the National Academy of Sciences*, which first demonstrated that continuous gradients could reveal the organizational structure of the cerebral cortex [1]. This work established gradient analysis as a valid approach for characterizing [[brain-network]] organization and demonstrated the method's sensitivity to individual differences in cortical functional architecture.

The primary reference for the BrainSpace software toolbox is the paper by Vos de Wael et al. (2020) in *NeuroImage*, which introduced the toolbox and demonstrated its application to resting-state [[fmri]] data from the [[human-connectome-project]] [1]. The software paper provides comprehensive documentation of the algorithms, null models, and alignment procedures implemented in BrainSpace, along with validation benchmarks demonstrating the toolbox's utility for gradient analysis across different datasets.

## Related Software

BrainSpace interacts with several other tools in the [[neuroimaging]] ecosystem. For [[diffusion-mri]] processing, it works alongside [[dipy]] and [[mrtrix3]] for tractography and connectivity reconstruction. For surface visualization, it integrates with [[freesurfer]] outputs and [[connectome-workbench]]. For statistical analysis, it complements [[nilearn]] and the [[brain-connectivity-toolbox]] ([[bctpy]]). For cortical parcel generation, it can be used with [[schaefer-atlas]] and other established parcellation schemes, though gradient analysis specifically aims to characterize continuous organization rather than discrete parcels.

## References

[1] Vos de Wael, R., Larivière, S., Zollei, L., et al. (2020). BrainSpace: Toolbox for exploratory analysis of brain gradients. *NeuroImage*, 223, 117302.

[2] Margulies, D. S., Ghosh, S. S., Goulas, A., et al. (2016). Situating the default-mode network along a principal gradient of macroscale cortical organization. *Proceedings of the National Academy of Sciences*, 113(44), 12574-12579.