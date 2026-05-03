---
title: neuromaps
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [neuroimaging, neuroimaging-fmri, neuroimaging-dti, connectomics, parcellation]
sources: [markello-2022, buckner-2011, wu-2018, robinson-2014, alexander-bloch-2018, burt-2020]
---

# neuromaps

## Overview

neuromaps is an open-source Python toolbox that provides a unified framework for loading, transforming, and analyzing multimodal brain maps across different spatial representations—including volumetric (NIfTI) and surface-based (GIFTI, CIFTI) formats @markello-2022. Developed primarily by the Naturalistic and Computational Neuroscience Laboratory at McGill University, the toolbox addresses a fundamental challenge in contemporary neuroimaging: the integration of heterogeneous brain data from diverse modalities (functional MRI, diffusion imaging, PET, MEG/EEG) and atlases into a common coordinate system for comparative analysis. neuromaps enables researchers to perform parcel-based analyses, generate spatial null models for statistical testing, and transform brain maps between different parcellation schemes, making it a valuable utility for connectomics and computational neuroscience workflows @markello-2022.

## Motivation and Context

The neuroimaging field has witnessed an explosion of data types and atlases over the past decade. Researchers increasingly work with multiple modalities—resting-state fMRI for functional connectivity, diffusion tensor imaging (DTI) for structural connectivity, and positron emission tomography (PET) for molecular information—often using different brain parcellations (from the [[desikan-killiany-atlas]] to the [[schaefer-atlas]] to the [[glasser-atlas]]). Historically, translating between these representations required custom, fragmented code that was difficult to maintain and reproduce. neuromaps emerged to solve this integration problem by providing a standardized API for loading brain maps from any supported format, resampling them to any target parcellation, and performing statistical comparisons while accounting for spatial autocorrelation through appropriate null models @markello-2022.

The toolbox fits into the broader ecosystem of [[nilearn]] and [[brainiak]], extending their capabilities with specialized functions for spatial comparison and null model generation. It has become particularly valuable for the [[whole-brain-modeling]] community, where researchers need to compare empirical brain dynamics with simulated data from simulators like [[the-virtual-brain]] or [[nest]].

## Key Features

neuromaps provides several core functionalities that distinguish it from general neuroimaging toolboxes. First, the toolbox implements a flexible data structure for representing brain maps with accompanying metadata (space, atlas, description), allowing seamless conversion between different spatial representations. Users can load a volumetric parcellation and instantly obtain a surface-based version, or vice versa, with automatic handling of the underlying geometry @markello-2022.

Second, neuromaps includes sophisticated null model generation algorithms specifically designed for brain map statistics. These models preserve the spatial autocorrelation structure of the brain while shuffling the values of interest, enabling parametric tests that properly account for the non-independence of neighboring voxels—a critical issue that many standard statistical approaches ignore @alexander-bloch-2018. The toolbox implements several null model strategies including label permutation, spatial autocorrelation-preserving surrogates (SPAuth), and bootstrap approaches @burt-2020.

Third, the toolbox provides functions for comparing brain maps across modalities and atlases. This includes tools for computing similarity matrices between maps, assessing the correspondence between different parcellation schemes, and performing enrichment analyses to determine which brain regions are overrepresented in a given map. The comparison utilities support both voxel-wise and parcel-wise analyses, with appropriate multiple comparison correction @markello-2022.

Fourth, neuromaps offers integration with several popular atlases and data formats out of the box. Supported atlases include the [[schaefer-atlas]], [[glasser-atlas]], [[desikan-killiany-atlas]], [[brainnetome-atlas]], and others, while supported formats include NIfTI, CIFTI, Gifti, and dense connectivity matrices. The toolbox also includes interfaces to the [[human-connectome-project]] data ecosystem and can fetch atlas definitions programmatically @markello-2022.

## Relationship to TVB

neuromaps can complement [[the-virtual-brain|TVB]] in brain modeling workflows that require brain map comparison and contextualization. When researchers generate simulated brain dynamics using TVB's neural mass models, they may wish to compare the resulting regional time series, connectivity patterns, or spectral properties against empirical neuroimaging data. neuromaps provides transformation functions to bring both empirical and simulated data into a common coordinate space, and statistical comparison tools—including spatial autocorrelation-preserving null models—to assess the correspondence between simulated and empirical brain maps @markello-2022.

This integration is particularly relevant for [[model-validation]] workflows where simulated brain activity is benchmarked against real neuroimaging observations. However, it should be noted that neuromaps is not itself a preprocessing pipeline for TVB; rather, it provides general-purpose transformations and comparison tools that can be applied in conjunction with TVB or other whole-brain modeling frameworks. The two toolsets have been used together in published studies examining the relationship between structural connectivity and functional dynamics @markello-2022.

## Key Papers

- **Markello, R.D., Hansen, J.Y., Liu, Z.Q. et al. (2022).** neuromaps: structural and functional interpretation of brain maps. *Nature Methods*, 19, 1472–1479. DOI: 10.1038/s41592-022-01625-w — The primary publication introducing the neuromaps toolbox, including descriptions of the transformation framework, spatial null models, and curated brain map repository.

- **Markello, R.D. & Misic, B. (2021).** Comparing spatial null models for brain maps. *Neuroimage*, 236, 118052. — A methodological paper benchmarking different spatial null models for brain map comparison, which informs neuromaps' default null model selection.

- **Alexander-Bloch, A.F. et al. (2018).** On testing for spatial correspondence between maps of human brain structure and function. *Neuroimage*, 178, 540–551. — Describes the "spin test" spatial null model that randomizes cortical surfaces via spherical rotation to assess spatial correspondence.

- **Burt, J.B. et al. (2020).** Generative modeling of brain maps with spatial autocorrelation. *Neuroimage*, 220, 117038. — Introduces variogram-matching parametric models for spatial null hypothesis testing in volumetric brain maps.

- **Wu, J. et al. (2018).** Accurate nonlinear mapping between MNI volumetric and FreeSurfer surface coordinate systems. *Human Brain Mapping*, 39, 3793–3808. — Describes the registration fusion framework used for MNI152-to-fsaverage transformations in neuromaps.

- **Robinson, E.C. et al. (2014).** MSM: a new flexible framework for multimodal surface matching. *Neuroimage*, 100, 414–426. — Describes the Multimodal Surface Matching (MSM) framework for surface-to-surface transformations.

## Related Software

neuromaps interacts with several key tools in the neuroimaging ecosystem. It extends the capabilities of [[nilearn]] for volumetric and surface-based neuroimaging, providing specialized functions for brain map comparison that nilearn does not offer. The toolbox works alongside [[brain-connectivity-toolbox|bctpy]] for graph-theoretic analysis of connectivity matrices, complementing bct's network metrics with spatial comparison capabilities. For parcellation work, neuromaps integrates with the various atlas pages in this wiki including [[brain-parcellations]] in general, as well as specific atlases like the [[aal-atlas]] and the [[yeo-atlas]].

For surface visualization and rendering, neuromaps can be combined with [[brainrender]] or [[brainnet-viewer]] to produce publication-quality figures showing the spatial distribution of brain map values. The toolbox also integrates with [[_connectome-workbench]] for reading and writing CIFTI files, and with [[freesurfer]] for processing FreeSurfer-derived data.