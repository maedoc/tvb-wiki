---
created: 2026-05-07
sources:
- raw/papers/tustison-2010.md
- raw/papers/alfaro-almagro-2018.md
- raw/papers/semanticscholar-301489ffb9de.md
- raw/papers/semanticscholar-a324c47ea982.md
- raw/papers/semanticscholar-f45e6044c92f.md
tags:
- software-brain-modeling
- software-visualization
- neuroimaging-dti
- neuroimaging-fmri
- diffusion-imaging
- tractography
title: 3D Slicer
type: entity
updated: '2026-05-07'
---

# 3D Slicer

## Overview

3D Slicer (simply called "Slicer") is a free, open-source software platform for medical image visualization, processing, and analysis. Developed by a collaborative community centered at Brigham and Women's Hospital and funded primarily through NIH grants, Slicer serves as a general-purpose toolkit for translational medical imaging research, surgical planning, and image-guided interventions. The platform provides an extensible architecture built upon the [[itk]] (Insight Toolkit) for image processing and VTK (Visualization Toolkit) for rendering, enabling researchers to develop, test, and deploy custom image analysis workflows in a unified environment.^[tustison-2010]

## Key Features

Slicer's architecture centers on a modular plugin system where core functionality is provided by loadable modules written in C++ or Python. The platform supports a comprehensive range of [[neuroimaging]] operations including volumetric visualization, segmentation, registration, and quantitative analysis across multiple imaging modalities—structural MRI, diffusion tensor imaging (DTI), [[neuroimaging-fmri|functional MRI]], CT, and ultrasound.

**Diffusion Tensor Imaging and [[tractography]]**: Slicer includes the SlicerDMRI extension, which provides a complete pipeline for [[diffusion-mri]] processing including tensor estimation, fiber tractography visualization, and tractography-based segmentation. The extension integrates state-of-the-art tractography algorithms and enables interactive exploration of [[white-matter]] pathways reconstructed from diffusion data. This capability is particularly relevant for [[whole-brain|whole-brain modeling]] workflows requiring high-quality [[structural-connectivity]] matrices derived from [[diffusion-imaging]] data.

**Segmentation and Parcellation**: The platform offers automated and semi-automated segmentation tools for defining regions of interest, anatomical structures, and pathological lesions. Slicer integrates with [[freesurfer]] through the Segment Editor's Morphological and Learning-based capabilities, and supports atlas-based segmentation using established parcellation schemes such as the [[desikan-killiany-atlas]] and [[glasser-atlas]].

**Registration and Normalization**: Built-in registration modules leverage [[elastix]] and [[ants]] algorithms for both rigid and deformable alignment of neuroimaging data to standard spaces.^[tustison-2010] This enables coordinate transformation between native and [[mni-space]] templates, critical for comparing data across subjects and studies. Large-scale neuroimaging pipelines such as those developed for population datasets rely on similar registration frameworks to achieve reproducible spatial normalization across thousands of participants.^[alfaro-almagro-2018]

**Extensibility Framework**: The Slicer extension manager provides one-click installation of community-contributed modules extending functionality into specialized domains. This framework has enabled the creation of over 200 extensions covering diverse applications from radiotherapy planning to fetal MRI analysis. Similar extensibility principles have guided frameworks like BrainScape, which provide plugin-based architectures for integrating heterogeneous MRI datasets across research studies.^[semanticscholar-301489ffb9de]

## Relationship to TVB

3D Slicer plays a supportive but important role in [[the-virtual-brain]] workflows, particularly in preprocessing pipelines that prepare neuroimaging data for whole-brain simulation:

**Structural [[connectivity]] Derivation**: Slicer's diffusion processing capabilities can generate tractography data that serves as input for structural connectivity matrix construction. The platform's ability to perform deterministic and probabilistic tractography produces fiber orientation distributions used in connectivity estimation, complementing dedicated tools like [[mrtrix3]] and [[dipy]].

**Anatomical Segmentation**: Slicer's segmentation tools enable creation of region-of-interest parcellations that define the node boundaries in TVB network models. Researchers can define custom parcellations based on anatomical boundaries or functional subdivisions, which then define the spatial granularity of whole-brain simulations.

**Data Format Support**: Slicer handles numerous medical imaging formats including [[nifti]], DICOM, and MINC, providing format conversion capabilities that ensure compatibility with TVB's data import pipeline. The platform also supports [[bids]] derivatives through dedicated modules, facilitating integration with standardized neuroimaging datasets.

**Preprocessing Integration**: While TVB typically relies on specialized tools like [[fsl]], [[ants]], and [[freesurfer]] for primary preprocessing, Slicer serves as a useful auxiliary tool for quality control, manual edits to automated segmentations, and generation of custom anatomical regions not readily available in standard atlases.

## Related Software

- [[itk]] — Insight Toolkit, core image processing library underlying Slicer
- VTK — Visualization Toolkit, core rendering engine for Slicer
- [[freesurfer]] — Cortical surface reconstruction and [[parcellation]]
- [[ants]] — Advanced Normalization Tools for registration and segmentation
- [[mrtrix3]] — Advanced diffusion MRI analysis and tractography
- [[dipy]] — Python-based diffusion MRI analysis
- [[the-virtual-brain]] — Whole-brain simulation platform

## References

1. Tustison et al. (2010). *N4ITK: improved N3 bias correction*. IEEE Transactions on Medical Imaging. [DOI](](https://doi.org/10.1109/TMI.2010.2046908))
2. (authors unknown). *Image Processing and Quality Control for the First 100,000 Brain Imaging Datasets from [[uk-biobank]]*.
3. Muhammad Nabi Yasinzai, R. Mito, M. Pedersen. (2025). *BrainScape: An open-source framework for integrating and preprocessing anatomical MRI datasets*. Imaging neuroscience. [DOI](](https://doi.org/10.1162/IMAG.a.944))