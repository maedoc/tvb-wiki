---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-c893f42e33a6.md
- raw/papers/winkler-2014-palm.md
- raw/papers/semanticscholar-50e828bd956a.md
tags:
- neuroimaging-dti
- tract-based-spatial-statistics
- white-matter
- voxel-wise-analysis
- fsl
title: TBSS
type: concept
updated: '2026-05-06'
---

# TBSS (Tract-Based Spatial Statistics)

**TBSS** is a voxel-wise analysis pipeline for [[diffusion-mri]] data that projects [[fractional-anisotropy]] (FA) and other DTI-derived metrics onto a common “skeleton” of white-matter tracts, enabling robust cross-subject statistical comparison without full [[tractography]].

## Overview

TBSS addresses a key problem in voxel-wise DTI analysis: alignment of white-matter tracts across subjects is much harder than grey-matter alignment because tract shapes vary substantially. TBSS solves this by:
1. **Non-[[linear]] registration** of all subjects’ FA maps to a common target (usually FMRIB58_FA)
2. **White-matter tract skeleton creation** — derived from the mean FA image, representing centres of all tracts common to the group
3. **Projection** of each subject’s highest local FA values onto the skeleton
4. **Voxel-wise cross-subject statistics** on the skeletonised data

## Workflow in FSL

| Stage | Command | Output |
|-------|---------|--------|
| 1. Preprocessing | `dtifit` (FSL) | FA, MD, L1, L2, L3 maps |
| 2. Registration | `fnirt` / `tbss_1_preproc` | Warped FA volumes |
| 3. Skeletonisation | `tbss_2_reg` → `tbss_3_postreg` | Mean FA skeleton |
| 4. Projection | `tbss_4_prestats` | Skeletonised FA per subject |
| 5. Statistics | `randomise` | Voxel-wise group statistics |

## Outputs

TBSS produces voxel-wise statistics maps that can be thresholded and viewed on the MNI template or on individual subjects’ data. Common outputs include:
- Corrected p-value maps for group differences in FA
- Mean FA skeleton overlaid on MNI template
- Cluster-based statistics using TFCE (Threshold-Free Cluster Enhancement)

## Extensions

- **Modality extension** — TBSS now supports MD, L1 (axial diffusivity), and radial diffusivity analysis beyond FA
- **Longitudinal TBSS** — handles repeated measures with subject-specific registration
- **TBSS with crossing fibres** — integrates with BedpostX / multi-shell models

## Limitations

- Assumes FA is the primary metric of interest (though extended to other measures)
- Skeleton represents only the centres of tracts — misses tract edges and subcortical endpoints
- Voxel-wise analysis does not preserve tract-level topology
- Still requires careful quality control for registration accuracy

## Relationship to TVB

TBSS findings often feed into TVB workflows:
- **[[structural-connectivity]] calibration** — TBSS-derived FA values correlate with TVB structural [[connectivity]] weights
- **Pathology mapping** — TBSS-identified white-matter disruptions can be translated into TVB lesion or structural connectivity perturbation models
- **Validation** — TVB simulations can predict the functional consequences of TBSS-identified white-matter changes
- TBSS is implemented in [[fsl]] and integrates with preprocessing pipelines like [[qsiprep]]

## Related

- [[diffusion-tensor-imaging]] — underlying data modality
- [[fsl]] — software implementing TBSS
- [[whole-brain-tractography]] — complementary approach preserving tract topology
- [[white-matter]] — anatomy and function

## References

- Smith et al. (2006) — Tract-based spatial statistics: voxelwise analysis of multi-subject diffusion data. NeuroImage 31(4): 1487–1505. https://doi.org/10.1016/j.neuroimage.2006.02.024
- Smith et al. (2009) — TBSS with crossing fibres. NeuroImage 43(4): 623–635. https://doi.org/10.1016/j.neuroimage.2009.03.024