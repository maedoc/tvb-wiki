---
created: 2026-05-04
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/schirner-2018.md
- raw/papers/semanticscholar-109de470e443.md
tags:
- software-brain-modeling
- software-neuroimaging
title: HD-BET
type: entity
updated: '2026-05-04'
---

# HD-BET

## Overview

HD-BET (Hip-deep Brain Extraction Tool) is a deep learning-based software tool for automatic brain extraction—also known as skull stripping—from T1-weighted magnetic resonance imaging (MRI) scans. Developed by Isensee et al. and first presented at the MICCAI 2019 conference, HD-BET employs a 3D convolutional [[neural-network]] trained on the [[hcp-dataset]] and other publicly available brain imaging datasets to robustly segment brain tissue from surrounding anatomical structures including skull, dura, and venous sinuses. The tool addresses a fundamental preprocessing challenge in quantitative neuroimage analysis: obtaining a clean, accurate brain mask that excludes non-brain tissues while preserving the full brain parenchyma, including challenging regions such as the cerebellum and brainstem that are frequently eroded or over-segmented by classical threshold-based methods.

## Key Features

HD-BET incorporates several technical innovations that distinguish it from earlier brain extraction tools. The network architecture utilizes 3D convolutions with residual connections, enabling effective capture of volumetric context across the entire brain volume rather than processing slice-by-slice as in earlier 2D approaches. The model was trained using a composite loss function combining dice overlap with boundary-aware terms, which encourages precise segmentation especially near the brain surface where intensity gradients are subtle. The tool operates in a single forward pass without requiring registration to a template or parameter tuning for individual subjects, making it suitable for batch processing of large datasets.

A particularly notable feature is HD-BET's robustness to variations in acquisition parameters, field strength, and scanner manufacturers. The training data encompassed images from multiple sites including the [[human-[[connectome]]-project]], [[uk-biobank]], and various clinical cohorts, providing exposure to diverse imaging protocols. This generalization capability reduces the need for dataset-specific parameter adjustment that plagued earlier tools like BET (Brain Extraction Tool) from Fsl, which while widely used required careful threshold selection to avoid either under- or over-segmentation.

The software is distributed as a Python package with both command-line interface and programmatic API, enabling integration into automated preprocessing pipelines. It produces three outputs: a binary brain mask, a probability map of brain tissue membership, and the brain-extracted image itself. The probability map proves valuable for quality control and for flexible post-processing where partial volume voxels can be handled explicitly.

## Technical Considerations and Limitations

Several technical considerations affect HD-BET's practical deployment. The tool was optimized for T1-weighted MPRAGE and SPGR sequences commonly used in structural [[neuroimaging]]; performance degrades for T2-weighted, FLAIR, or contrast-enhanced images unless retrained on appropriate data. Memory requirements scale with the input volume size, typically requiring 8-12 GB of RAM for [[whole-brain]] volumes at 1mm isotropic resolution. Post-processing Steps such as cerebellar peduncle correction or brainstem refinement may be necessary for specific anatomical regions of interest.

Compared to classical approaches like BET or ROBEX, HD-BET generally achieves superior accuracy on diverse data but requires GPU acceleration for practical throughput. The deep learning model introduces dependencies on PyTorch and associated libraries, adding complexity to containerized environments. For large cohort studies, the computational overhead (approximately 30-60 seconds per volume on modern GPU hardware) must be weighed against quality improvements in downstream analyses.

## Relationship to TVB

HD-BET serves as a preprocessing component within the [[whole-brain-modeling]] ecosystem that includes [[the-virtual-brain]] (TVB). In TVB workflows, high-quality structural MRI preprocessing is essential for generating accurate [[structural-connectivity]] matrices from diffusion imaging data and for constructing personalized brain region parcellations. The brain-extracted images from HD-BET feed directly into subsequent pipeline stages including Freesurfer processing for cortical reconstruction and volume labeling, registration to [[mni-space]] template spaces, and generation of region-wise connectivities using tools like [[mrtrix3-connectome]]. While TVB does not directly depend on HD-BET, the tool exemplifies the modern preprocessing stack that enables reproducible large-scale brain mapping essential for personalized whole-brain simulations.

## Related Software

HD-BET operates within a broader ecosystem of brain extraction and neuroimaging preprocessing tools. Classical alternatives include the BET tool from Fsl, [[ants]], and Freesurfer's own brain masking routines, each offering different tradeoffs between automation, accuracy, and computational requirements. For diffusion imaging specifically, Mrtrix3 provides competing brain segmentation through mrrobustify, while pipeline frameworks like [[fmriprep]] and Qsiprep incorporate brain extraction as one stage in full preprocessing chains. The development of HD-BET reflects the broader transition toward deep learning-based methods in neuroimaging, alongside tools like [[synthseg]] for volumetric segmentation.

[[TVB]]
Freesurfer
Fsl
Mrtrix3
[[mni-space]]
[[structural-connectivity]]
[[mrtrix3-connectome]]
[[whole-brain-modeling]]
[[the-virtual-brain]]

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040)
3. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical [[fmri]] preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2025.1621244)