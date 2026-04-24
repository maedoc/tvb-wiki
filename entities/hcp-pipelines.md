---
created: 2026-04-23
sources:
- raw/papers/glasser-2013.md
- raw/papers/smith-2013-hcp.md
- raw/papers/van-essen-2013.md
- raw/papers/schirner-2018.md
- raw/papers/barch-2013.md
- raw/papers/van-essen-2012.md
tags:
- software-brain-modeling
- database-hcp
- structural-connectivity
- functional-connectivity
- neuroimaging-fmri
- neuroimaging-dti
- connectomics
- tractography
title: HCP Pipelines
type: entity
updated: '2026-04-24'
---

# HCP Pipelines

## Overview

The **HCP Pipelines** are open-source neuroimaging preprocessing pipelines developed by the [[Human Connectome Project]] to standardize the processing of multimodal brain imaging data. These pipelines implement a surface-based analysis framework that emphasizes cross-modal alignment while applying minimal yet effective preprocessing to preserve data quality [[Glasser et al., 2013]](raw/papers/glasser-2013.md).

The pipelines process three primary imaging modalities acquired on the HCP's customized 3T Siemens Prisma scanners: structural MRI (T1w and T2w at 0.7mm resolution), functional MRI (resting-state and task-based with multiband acceleration), and diffusion MRI (high angular resolution with b-values up to 3000 s/mm²). The software is implemented as a set of shell scripts and Python utilities distributed under an open-source license, enabling reproducible processing across research sites [[Van Essen et al., 2013]](raw/papers/van-essen-2013.md).

## Key Features

### Structural Preprocessing
The structural pipeline performs: bias field correction, brain extraction, tissue segmentation, and cortical surface reconstruction using FreeSurfer algorithms adapted for the HCP acquisition protocol. The pipeline generates cortical surface meshes in both native and standard space (fs_LR 32k), enabling vertex-wise analysis across subjects.

### Functional Preprocessing
The fMRI pipeline implements: gradient nonlinearity distortion correction, motion correction using FLIRT, EPI distortion correction using TOPUP, registration to structural images, and minimal temporal filtering. Critically, the pipeline maps volumetric fMRI data to the cortical surface, enabling surface-based connectivity analysis [[Smith et al., 2013]](raw/papers/smith-2013-hcp.md).

### Diffusion Preprocessing
The dMRI pipeline applies: susceptibility-induced distortion correction, eddy current correction including motion correction, bias field correction, and registration to structural images. The output includes preprocessed dMRI volumes ready for tractography and diffusion model fitting.

### Quality Assurance
Each pipeline includes automated quality assessment metrics and visual inspection checkpoints. The HCP QC framework scores data usability and identifies artifacts that may affect downstream analysis.

## Relationship to TVB

The HCP Pipelines provide essential preprocessing for connectome-based whole-brain modeling in [[TVB]]. The pipeline outputs directly support TVB workflows:

- **Structural Connectivity**: The cortical surface meshes (in fs_LR space) serve as the anatomical scaffolding for TVB simulations, with surface vertices mapping to network nodes.

- **Tractography-derived Connectivity**: Preprocessed dMRI enables probabilistic tractography using tools like MRtrix3 or FSL's PROBTRACKX, generating structural connectivity matrices that constrain TVB network dynamics.

- **Functional Validation**: The resting-state networks identified in HCP data provide empirical targets for validating TVB simulations against observed [[functional-connectivity]] patterns.

The **HCP Connectome Workbench** software, distributed alongside the pipelines, provides visualization tools compatible with TVB output formats, facilitating comparison of simulated and empirical connectivity patterns.

## Key Papers

- **Glasser et al. (2013)** — Foundational paper describing the minimal preprocessing pipelines, surface-based analysis framework, and cross-modal alignment. *NeuroImage*, DOI: 10.1016/j.neuroimage.2013.04.127

- **Smith et al. (2013)** — Describes HCP resting-state fMRI processing, group-level functional connectivity analysis, and identification of major resting-state networks at high resolution. *NeuroImage*, DOI: 10.1016/j.neuroimage.2013.05.099

- **Van Essen et al. (2013)** — Overview of the Human Connectome Project, including imaging protocols, data acquisition, and the role of preprocessing pipelines in enabling open data sharing. *NeuroImage*, DOI: 10.1016/j.neuroimage.2013.04.024

- **Sotiropoulos et al. (2013)** — Details of the diffusion MRI acquisition and preprocessing, including noise modeling and distortion correction strategies optimized for high angular resolution data.

## Related Software

- [[TVB]] — Whole-brain simulation platform using HCP-derived connectivity
- [[Human Connectome Project]] — The parent initiative distributing data and tools
- [[FSL]] — Underlying library for various pipeline stages (FLIRT, TOPUP, BET)
- [[FreeSurfer]] — Cortical surface reconstruction algorithms
- [[Connectome Workbench]] — Visualization and data format conversion
- [[MRtrix3]] — Alternative/complementary tractography tool
- [[ANTs]] — Advanced normalization tools compatible with HCP outputs
- [[DataLad]] — Data management for HCP dataset versioning

## References

1. Glasser, M.F., et al. (2013). The minimal preprocessing pipelines for the Human Connectome Project. *NeuroImage*, 80, 105-124.
2. Smith, S.M., et al. (2013). Resting-state fMRI in the Human Connectome Project. *NeuroImage*, 80, 144-168.
3. Van Essen, D.C., et al. (2013). The WU-Minn Human Connectome Project: An overview. *NeuroImage*, 80, 62-79.
4. Sotiropoulos, S.N., et al. (2013). Effects of image reconstruction on fibre orientation mapping from diffusion MRI. *NeuroImage*, 81, 371-384.
5. HCP Pipelines Documentation: https://github.com/Washington-University/HCPpipelines