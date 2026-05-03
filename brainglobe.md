---
title: BrainGlobe
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software-brain-modeling, software-visualization, brain-parcellations, neuroanatomy, computational-neuroscience, parcellation, atlases]
sources: [brainglobe-atlasapi-2020]
---

# BrainGlobe

## Overview

BrainGlobe is an open-source suite of interoperable Python tools for computational neuroanatomy, developed and maintained by the BrainGlobe Initiative. The platform provides a collection of software packages designed to facilitate the analysis, visualization, and processing of neuroanatomical data across multiple species and imaging modalities. Originally launched in 2020, BrainGlobe has grown to encompass over 17 independent software packages addressing various aspects of brain mapping, from automated cell detection to three-dimensional anatomical registration and visualization. The initiative emphasizes modularity and interoperability, allowing researchers to combine different tools within the BrainGlobe ecosystem or integrate them with external software packages commonly used in computational neuroscience workflows.

## Key Features

### Atlas Infrastructure

The **BrainGlobe Atlas API** (brainglobe-atlasapi) serves as the foundational component of the suite, providing a unified interface for accessing multiple neuroanatomical atlases programmatically. This addresses a persistent challenge in computational neuroanatomy: the fragmentation of brain atlas data across different formats, coordinate systems, and species. The API supports atlases for mouse, rat, zebrafish, and other species, including the [[allen-brain-atlas]] and various developmental atlases. Each atlas includes a reference image, annotation image with region labels, surface meshes in OBJ format, and hierarchical structure information in JSON format. The standardized data format enables consistent processing pipelines regardless of the underlying atlas source. The API integrates with [[brain-parcellations]] tools to provide region-of-interest definitions for downstream analyses.

### Visualization with brainrender

**brainrender** is the three-dimensional visualization package of the suite, capable of rendering neuroanatomical data in atlas space using Python. The software can visualize brain regions, individual neurons, tractography data, and other anatomical structures, with support for interactive exploration innapari. brainrender produces publication-quality figures and has been used extensively in studies requiring detailed anatomical visualization. The package integrates with napari for seamless embedding within modern Python-based neuroimaging workflows.

### Registration and Segmentation

**brainreg** provides automated three-dimensional brain registration, supporting multiple species and atlases through a registration framework that aligns experimental data to standard coordinate spaces. This enables quantitative comparisons across specimens and laboratories by transforming diverse datasets into a common reference frame using techniques from [[diffusion-imaging]] and [[tractography]]. Complementing registration, **cellfinder** offers automated three-dimensional cell detection in large microscopy images, addressing the computational challenge of quantifying cellular distributions in whole-brain datasets. **brainglobe-segmentation** extends these capabilities to anatomical structure segmentation within common coordinate spaces.

### Morphology Analysis

**morphapi** provides programmatic access to neuronal morphology data, enabling researchers to download and analyze reconstructed neuron geometries from public repositories. This capability supports research into [[neural-mass-models]] and detailed anatomical characterization of neuronal populations. When combined with the visualization and analysis tools in the suite, morphapi enables comprehensive characterization of neuronal morphology across brain regions.

## Relationship to TVB

BrainGlobe and [[the-virtual-brain]] (TVB) address complementary aspects of whole-brain modeling. While TVB focuses on large-scale neural dynamics and [[whole-brain-modeling]] using [[neural-mass-models]] and [[connectomics]], BrainGlobe provides the anatomical infrastructure necessary for creating detailed brain models. The integration potential lies in using BrainGlobe's atlas infrastructure to define brain regions and parcellations within TVB simulations. Both platforms are written in Python and emphasize open-source development, facilitating potential toolchain integration. Researchers building personalized brain models can leverage BrainGlobe atlases to define region boundaries, then supply these to TVB for dynamical simulations. This combination is particularly valuable for [[personalized-brain-modeling]] workflows where individual anatomical data must be mapped onto standardized coordinate systems.

## Key Papers

The BrainGlobe Atlas API is documented in a peer-reviewed publication: Claudi, F., Petrucco, L., Tyson, A. L., Branco, T., Margrie, T. W. and Portugues, R. (2020). BrainGlobe Atlas API: a common interface for neuroanatomical atlases. *Journal of Open Source Software*, 5(54), 2668. [https://doi.org/10.21105/joss.02668](https://doi.org/10.21105/joss.02668)

## Related Software

BrainGlobe integrates with several other tools in the computational neuroscience ecosystem. For visualization, it complements [[brainnet-viewer]] and [[brainrender]]. For atlas-related functionality, it works alongside [[nilearn]] and [[freesurfer]] for human neuroimaging, and [[fsl]] for general neuroimaging processing. The suite can be combined with [[dipy]] for diffusion imaging analysis and [[mrtrix3]] for tractography. For cell detection and microscopy analysis, it addresses similar domains as cellfinder. The modular architecture allows researchers to incorporate BrainGlobe into workflows using [[nipype]] for pipeline orchestration, enabling integration with nearly any Python-based neuroimaging processing chain. The atlas data can be read using [[nibabel]] for NIfTI file handling, and the resulting parcellations may be used in [[epilepsy-modeling]] and [[brain-stimulation]] studies.

## Summary

BrainGlobe provides essential infrastructure for computational neuroanatomy, offering standardized atlas interfaces, visualization, registration, and analysis tools essential for modern neuroscience research. Its Python-based architecture and emphasis on interoperability make it a valuable component in whole-brain modeling workflows, particularly when combined with dynamical simulation platforms like TVB.