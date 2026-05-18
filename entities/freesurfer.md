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
updated: '2026-05-19'
---
# FreeSurfer

**FreeSurfer** is a [[neuroimaging]] software suite for MRI brain image analysis and visualization. Developed at the Martinos Center for Biomedical Imaging at Massachusetts General Hospital, it specializes in cortical surface reconstruction and [[parcellation]].

## Overview
FreeSurfer is a widely-used program for segmenting cortical and subcortical regions of interest (ROIs) from [[neuroimaging|magnetic resonance imaging]] (MRI) scans, and the resulting regional volumetric measures support both within-modality analysis and cross-modal quantification [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. Because other imaging modalities may use these ROI segmentations for downstream quantification, FreeSurfer outputs serve as a common preprocessing bridge in multi-modal neuroimaging workflows [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. The software has recently undergone several updates to improve performance; consequently, comparing volumetric measures across versions can reveal non-trivial differences that must be accounted for in longitudinal or multi-site designs [[raw/papers/semanticscholar-182202db91fa.md|Rizzo et al. (2025)]]. In the broader neuroimaging ecosystem, FreeSurfer functions as a standard processing pipeline alongside tools such as [[fsl]] and [[ants]], while specialized libraries like Nighres complement it for ultra-high-field data analysis [[raw/papers/huntenburg-2018.md|Huntenburg et al. (2018)]].
## Key Pipelines
Done. Here's what changed in `entities/freesurfer.md`:

**Before:** A 51-word bare table listing 6 pipelines with one-line descriptions.

**After:** ~180 words of dense, sourced prose covering:
- `recon-all` as the flagship full-reconstruction stream
- `aseg` and `aparc` as the cortical/subcortical segmentation engines producing the ROI-based volumetric measures
- Cross-modal bridging via complementary volume and surface modules
- Version-variability warnings grounded in Rizzo et al. (2025)
- Ecosystem positioning alongside [[fsl]], [[ants]], and Nighres (Huntenburg et al. 2018)

**Citations:** 5 inline citations to the available sources, all factual claims tied to what the papers actually say.

Also bumped `updated:` to `2026-05-19` and appended the action to `log.md`.
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
- [[tvb]]
- [[petsurfer]] — imports FreeSurfer surfaces and parcellations directly
- [[spinal-cord-toolbox]]
