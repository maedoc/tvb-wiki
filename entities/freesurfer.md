---
title: "FreeSurfer"
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [software-freesurfer, neuroimaging-fmri, image-processing, parcellation, cortical-surface]
sources: []
---

# FreeSurfer

**FreeSurfer** is a neuroimaging software suite for MRI brain image analysis and visualization. Developed at the Martinos Center for Biomedical Imaging at Massachusetts General Hospital, it specializes in cortical surface reconstruction and parcellation.

## Overview

FreeSurfer provides tools for:
- Automated cortical surface reconstruction from T1-weighted MRI
- Subcortical and cortical segmentation
- Cortical thickness measurement
- Surface-based registration to standard atlases
- Functional data projection to cortical surfaces
- Automated parcellation into anatomical or functional regions

## Key Pipelines

| Pipeline | Purpose |
|----------|---------|
| **recon-all** | Full structural processing pipeline |
| **aseg** | Automatic subcortical segmentation |
| **aparc** | Cortical parcellation (Desikan-Killiany, Destrieux) |
| **mris_volseg** | Volume-based segmentation |
| **bbregister** | Boundary-based registration to functional data |
| **mri_surf2surf** | Surface data resampling |

## Relationship to TVB

FreeSurfer outputs are essential for TVB personalized modeling:
- **Cortical parcellation** (aparc) defines region labels for the 68-region or 164-region brain model
- **Surface meshes** (pial, white matter) provide anatomical geometry for visualization
- **Cortical thickness** and **surface area** inform region-specific parameter choices in neural mass models
- **Subcortical segmentation** (aseg) adds deep brain structures to the connectome
- FreeSurfer-derived parcellations are used by the [[human-connectome-project]] and many TVB workflows

## Parcellation Schemes

FreeSurfer implements several standard parcellations:
- **Desikan-Killiany** (68 cortical regions) — widely used in TVB
- **Destrieux** (148/164 regions) — finer-grained atlas
- **Glasser/MMP** — HCP multi-modal parcellation (via HCP plugin)
- [[aal]] and [[schaefer]] atlases can be mapped to FreeSurfer surfaces

## Software Ecosystem

- [[fsl]] — often used together for preprocessing
- [[ants]] — alternative registration
- [[brainstorm]] — MEG/EEG source analysis using FreeSurfer surfaces
- [[tvb]] — imports FreeSurfer surfaces and parcellations directly

## References

- FreeSurfer website: https://surfer.nmr.mgh.harvard.edu/
- Dale et al. (1999) — Cortical surface-based analysis
- Fischl et al. (2004) — Automatically parcellating the human cerebral cortex
