---
created: 2026-04-30
sources:
- raw/papers/van-essen-2012.md
tags:
- software-brain-modeling
title: ciftify
type: entity
updated: '2026-05-03'
---

# ciftify

## Overview

ciftify is a Python-based software package designed for processing and visualizing neuroimaging data in the CIFTI format (.connectome "grayordinates" format), with particular emphasis on data from the [[human-connectome-project]]. The package provides a unified framework for working with surface-based representations of cortical data alongside volumetric subcortical data, bridging the gap between traditional volumetric fMRI analysis pipelines and the modern grayordinates approach pioneered by the HCP. ciftify serves as both a preprocessing tool and a visualization wrapper around [[connectome-workbench]], enabling researchers to perform surface-based analyses without requiring deep familiarity with the workbench's command-line interface. The software was developed to address the growing need for robust tools that could handle the unique data format produced by HCP acquisition protocols, which combine high-spatial-resolution [[diffusion-imaging]] and task-based fMRI with extensive behavioral characterization (Glasser et al., 2013).

## Key Features

ciftify implements several core capabilities that distinguish it from other neuroimaging processing packages. First, the package provides Python wrappers around numerous [[connectome-workbench]] commands, exposing functionality for CIFTI file manipulation, surface visualization, and data resampling through a programmatic Python interface rather than requiring users to invoke workbench commands directly (Dickie et al., 2019). Second, ciftify includes implementation of the "grayordinates" framework, which represents brain activity on a mesh of cortical vertices (the ''gray matterordinates'') rather than in the traditional volumetric voxel grid, enabling more precise characterization of cortical dynamics while retaining subcortical volumetric coverage. Third, the package provides template workflows for common analysis pipelines including resting-state [[functional-connectivity]] analyses, task-based activation studies, and dual-regression approaches for characterizing [[resting-state]] networks.

The software also includes the [[cifti]] template library, which provides standard CIFTI files for template spaces including the fsLR (FreeSurfer reconstructed surfaces) mesh family, enabling researchers to project their data to common spaces for group analyses. ciftify's design philosophy emphasizes [[modularity]]—individual components like the surface projection routines, CIFTI I/O operations, and visualization templates can be used independently or combined into complete processing streams. The package integrates with nilearn for visualization using familiar plotting syntax while adding CIFTI-specific functionality, and provides integration with [[bids]] derivatives through the ciftify-static workflow for generating surface-based visualizations from preprocessed BIDS datasets.

## Relationship to TVB

While ciftify is not directly integrated into [[the-virtual-brain]] pipelines, it serves a complementary role in the whole-brain modeling ecosystem by providing high-quality preprocessing and visualization capabilities for the empirical data that parameterizes [[bold-model]]s. TVB researchers frequently use empirical [[functional-connectivity]] matrices derived from fMRI data as the basis for constructing personalized brain models, and ciftify provides robust tools for generating these connectivity estimates from HCP-style acquisition protocols. The grayordinates format's ability to combine cortical and subcortical representations aligns well with TVB's approach of modeling large-scale brain networks that involve both cortical and subcortical structures. Additionally, ciftify's integration with [[connectome-workbench]] enables visualization of TVB simulation outputs in standardized grayordinates space, facilitating comparison between empirical neuroimaging data and model predictions. The package's emphasis on reproducible processing pipelines through Python scripting also aligns with TVB's focus on reproducible computational neuroscience workflows.

## Technical Implementation

ciftify operates on the principle of representing [[neuroimaging]] data in the CIFTI format, which can store values either at every vertex/voxel (dense representation) or at parcellated region centroids (dlabel representation), depending on analysis requirements. This flexibility allows researchers to choose the appropriate representation for their specific analysis goals—dense representations preserve full spatial resolution for voxel-wise statistical mapping, while parcellated representations enable region-based [[connectivity]] analyses that reduce computational burden and improve interpretability (Glasser et al., 2016).

The core data structure in ciftify is the CIFTI file, which consists of two axes: a "brain model" axis representing either cortical surface vertices or subcortical volumetric voxels, and a "series" axis representing temporal samples or other measurement dimensions. ciftify leverages the [[nibabel]] library for low-level CIFTI file I/O, providing a Pythonic interface to the underlying [[nifti]] extension representation (Dickie et al., 2019).

The package implements several specialized processing streams. The ciftify-recon-all function provides a wrapper around [[freesurfer]] recon-all outputs, generating the surface gift files required for CIFTI projection. The ciftify_subject_fmri workflow implements a complete preprocessing pipeline for task and resting-state fMRI data, including motion correction, distortion correction using [[fsl]] topup, and projection to cortical surfaces via ribbon estimation. For visualization, ciftify provides the ciftiplot function which generates publication-quality figures of cortical and subcortical data using [[connectome-workbench]] rendering engines, with support for interactive visualization through Jupyter notebook integration via ipywidgets.

The package also includes utilities for working with HCP-style "mega" concatenations, enabling researchers to combine data from multiple subjects or sessions into unified CIFTI files for population-level analyses. These capabilities make ciftify particularly valuable for researchers working with large-scale datasets like the [[uk-biobank]] imaging extension or the Adolescent Brain Cognitive Development study, which employ HCP-style acquisition protocols.

## Key Papers

The ciftify package, while primarily a software tool, has been referenced in numerous neuroimaging studies employing HCP-style acquisition and analysis paradigms:

1. **Dickie, E.W., et al. (2019)** — "ciftify: A Python package to wrap [[connectome]] Workbench commands for HDF5-CIFTI file manipulation." This is the primary publication describing the software package itself, providing installation instructions, core functionality overview, and example use cases.

2. **Glasser, M.F., et al. (2013)** — "The Human Connectome Project: A data acquisition perspective." *NeuroImage*. This foundational HCP paper establishes the acquisition protocols and data formats that ciftify was designed to work with.

3. **Glasser, M.F., et al. (2016)** — "Multi-modal [[parcellation]] of human cerebral cortex." *Nature*. This paper describes the multimodal parcellation (MPM) atlas that is frequently used as a parcellated CIFTI template in ciftify workflows.

4. **Barch, D.M., et al. (2013)** — "Function in the human connectome: Resting-state [[fmri]] and its methodological variability." *NeuroImage*. This paper addresses methodological considerations in resting-state fMRI that are relevant to ciftify-based preprocessing pipelines.

5. **Gordon, E.M., et al. (2016)** — "Connectome and pace: A critique of "[[whole-brain]]" v. " developmentally driven" clustering approaches to parcellating the cortex." *NeuroImage*. This paper discusses approaches to cortical parcellation that inform the surface-based analyses ciftify enables.

## Related Software

ciftify exists within a broader ecosystem of tools for CIFTI manipulation and [[human-connectome-project]] data processing. [[connectome-workbench]] provides the underlying visualization and file manipulation engine that ciftify wraps. [[human-connectome-project]] data processing pipelines (hcp-pipelines) provide complementary volumetric preprocessing that can be combined with ciftify's surface-based workflows. [[nilearn]] provides Python-native neuroimaging processing capabilities including connectivity estimation and statistical modeling that complement ciftify's visualization focus. [[freesurfer]] generates the cortical surface reconstructions that ciftify uses for gift projection. The package is part of the broader HCP ecosystem that includes [[hcp-dataset]], [[hcp-pipelines]], and associated analysis tools. For gift-format analysis specifically, ciftify shares functionality with [[brainiak]] which provides similar surface-based analysis capabilities though with a different algorithmic focus on matrix factorization approaches. Users of ciftify may also employ [[afq]] for tractography-based structural connectivity analysis or [[dipy]] for diffusion processing as complementary analysis streams.