---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-182202db91fa.md
- raw/papers/cbs-tools.md
- raw/papers/huntenburg-2018.md
- raw/papers/schirner-2018.md
- raw/papers/wang-etal-2015-gretna.md
- raw/papers/semanticscholar-0f134e817e53.md
tags:
- software-freesurfer
- neuroimaging-fmri
- image-processing
- parcellation
- cortical-surface
title: FreeSurfer
type: entity
updated: '2026-05-18'
---

# FreeSurfer

**FreeSurfer** is a [[neuroimaging]] software suite for MRI brain image analysis and visualization. Developed at the Martinos Center for Biomedical Imaging at Massachusetts General Hospital, it specializes in cortical surface reconstruction and [[parcellation]].

## Overview

FreeSurfer is a widely-used program for automated segmentation of cortical and subcortical regions of interest from structural magnetic resonance imaging scans, producing anatomical [[parcellation]]s that serve as the basis for subsequent [[neuroimaging]] analyses [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. Regional volumetric measures can be calculated directly from these segmentations, and the resulting region-of-interest definitions are routinely employed by other imaging modalities for targeted quantification [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. The software has recently undergone successive updates to improve performance, reflecting ongoing refinement of its underlying algorithms [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. Within the broader [[neuroimaging]] software landscape, FreeSurfer functions as a standard processing pipeline alongside established alternatives such as [[fsl]] and [[ants]] [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]]. While these conventional pipelines provide reliable workflows for standard-resolution acquisitions, the anatomical detail preserved at ultra-high-field strengths has motivated the development of complementary frameworks that extend rather than replace standard methods [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]]. This layered ecosystem positions FreeSurfer as a foundational preprocessing tool whose outputs—cortical and subcortical segmentations, volumetric estimates, and regional [[parcellation]]s—enable a wide range of downstream neuroimaging and network analyses [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]][[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]].

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
- **Surface meshes** (pial, [[white-matter]]) provide anatomical geometry for visualization
- **Cortical thickness** and **surface area** inform region-specific parameter choices in [[neural-mass-models]]
- **Subcortical segmentation** (aseg) adds deep brain structures to the [[connectome]]
- FreeSurfer-derived parcellations are used by the [[human-connectome-project]] and many TVB workflows

## Parcellation Schemes

FreeSurfer implements several standard parcellations:
- **Desikan-Killiany** (68 cortical regions) — widely used in TVB
- **Destrieux** (148/164 regions) — finer-grained atlas
- **Glasser/MMP** — HCP multi-modal parcellation (via HCP plugin)
- [[aal-atlas]] and [[schaefer-atlas]] atlases can be mapped to FreeSurfer surfaces

## Software Ecosystem

- [[fsl]] — often used together for preprocessing
- [[ants]] — alternative registration
- [[brain-map]] — MEG/EEG source analysis using FreeSurfer surfaces
- [[tvb]] — imports FreeSurfer surfaces and parcellations directly

## References

FreeSurfer is a widely used program for segmenting cortical and subcortical regions of interest from MRI scans, with regional volumetric measures routinely calculated from these segmentations and employed by other imaging modalities for quantification [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. Because FreeSurfer has recently undergone several updates to improve segmentation performance, comparative studies have begun systematically evaluating how volumetric measures vary across different software versions [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. These segmentation-derived volumetrics therefore remain central to the broader neuroimaging pipeline, even as researchers scrutinize the consistency of regional measures across software updates [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]].

For ultra-high-field acquisitions (7T and above), traditional processing pipelines developed for standard-resolution 3T data often fail to preserve the detailed anatomical information required for fine-grained laminar analysis, motivating the development of complementary high-resolution toolkits that provide specialized functions for cortical depth estimation and tissue segmentation [[raw/papers/cbs-tools.md|Bazin et al. (2012)]]. In that regime, the Nighres Python package complements standard neuroimaging processing pipelines like FreeSurfer, [[fsl]], and [[ants]] by translating the earlier CBS Tools algorithms into an accessible Python interface with modules for brain processing, cortex extraction, volumetric layering, and surface visualization [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]]. Because Nighres integrates with nibabel and nilearn for NIfTI handling and downstream visualization, these laminar-analysis capabilities extend FreeSurfer's foundational outputs rather than replacing them [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]].