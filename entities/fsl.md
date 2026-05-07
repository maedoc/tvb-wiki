---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-0aeca1b592e6.md
- raw/papers/Renton2024.md
- raw/papers/huntenburg-2018.md
tags:
- software-fsl
- neuroimaging-fmri
- neuroimaging-dti
- image-processing
- statistics
title: FSL
type: entity
updated: '2026-05-07'
---

# FSL

**FSL** (FMRIB Software Library) is a comprehensive library of analysis tools for [[neuroimaging-fmri|functional MRI]] ([[fmri]]), MRI, and DTI brain imaging data. Developed at the Wellcome Centre for Integrative [[neuroimaging]] at the University of Oxford, FSL is one of the most widely used neuroimaging software packages in the world [Smith et al. 2004].

## History and Motivation

FSL emerged from the Oxford FMRIB (Functional Magnetic Resonance Imaging of the Brain) group in the 1990s, driven by the need for robust, automated analysis pipelines capable of handling the growing volume of neuroimaging data [Smith et al. 2004]. Prior to FSL, researchers relied on fragmented, often manual processing workflows with limited reproducibility. FSL addressed this gap by providing an integrated suite of tools that cover the full analysis pipeline — from raw acquisition to statistical inference — within a cohesive framework [Jenkinson et al. 2012]. The software remains freely available to academic users, contributing to its widespread adoption across the neuroimaging community.

## Overview

FSL provides tools for:
- fMRI preprocessing and statistical analysis
- Structural MRI segmentation and registration
- [[diffusion-mri]] [[tractography]] and analysis
- Brain extraction (BET) and tissue segmentation
- General [[linear|linear model]] (GLM) and mixed-effects analysis

## Key Tools

FSL comprises a comprehensive suite of command-line tools that form the backbone of many neuroimaging pipelines. **BET** (Brain Extraction Tool) performs automated skull stripping by fitting a deformable mesh to the brain boundary, producing a binary brain mask essential for subsequent processing steps [Smith et al. 2004]. **FLIRT** (FMRIB's Linear Image Registration Tool) implements rigid-body and affine registration using correlation ratio as the default cost function, with mutual information available for multi-modal alignment [Jenkinson et al. 2012]. **FNIRT** (FMRIB's Non-linear Image Registration Tool) extends this with B-spline warping for fine-grained alignment between native and standard space.

For tissue segmentation, **FAST** (FMRIB's Automated Segmentation Tool) uses a hidden Markov random field model to classify brain volumes into grey matter, white matter, and CSF [Smith et al. 2004].

In fMRI analysis, **FEAT** (FMRIB's Expert Analysis Tool) provides a complete first-level pipeline encompassing preprocessing (motion correction, spatial smoothing, high-pass filtering), hemodynamic response modeling via the general linear model, and mixed-effects group statistics [Smith et al. 2004]. **MELODIC** performs probabilistic independent component analysis (ICA) for data-driven decomposition of resting-state or task fMRI into spatially independent networks, enabling identification of [[intrinsic-connectivity-networks]] [Jenkinson et al. 2012].

In diffusion imaging, **TBSS** (Tract-Based Spatial Statistics) enables voxelwise analysis of [[fractional-anisotropy]] maps by projecting white-matter skeletons onto which group differences can be tested [Smith et al. 2004]. **BEDPOSTX** fits a ball-and-stick model to estimate diffusion parameters and principal fiber orientations per voxel, while **PROBTRACKX** uses these estimates to perform probabilistic tractography for reconstructing [[structural-connectivity]] pathways. These diffusion tools are integrated into broader [[whole-brain]] workflows including [[the-virtual-brain]] simulations and [[connectome]] construction pipelines, and are distributed through containerized platforms like Neurodesk for reproducible analysis across computing environments.

## Relationship to TVB

FSL tools are commonly used in TVB preprocessing pipelines:
- **Brain extraction** (BET) generates the cortical surface mask
- **Segmentation** (FAST) produces grey matter, [[white-matter]], and CSF maps
- **Registration** (FLIRT/FNIRT) aligns subject anatomy to standard atlases
- **Tractography** (BEDPOSTX + PROBTRACKX) generates [[structural-connectivity]] matrices used as TVB input
- [[tbss]] and bedpostx outputs feed into [[whole-brain]] [[connectome]] construction for [[the-virtual-brain]] simulations

## Software Ecosystem

FSL is part of a broader neuroimaging toolchain:
- [[freesurfer]] — cortical surface reconstruction (often used together)
- [[ants]] — alternative registration tool
- [[spm]] — alternative statistical analysis package
- [[mrtrix3]] — alternative DTI/tractography suite
- [[dipy]] — Python-based diffusion analysis

## References

1. Mohammadtaha Parsayan, S. Andalib, T. L. Andersen, Habib Ganjgahi, P. Høilund-Carlsen, Abass Alavi, Mojtaba Zarei. (2025). *Odense-Oxford PET Image Analysis (OPETIA): An FSL-based toolbox for multimodal neuroimaging*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2025.121278)
2. (authors unknown). *Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging*.
3. (authors unknown). *Nighres: processing tools for high-resolution neuroimaging*.