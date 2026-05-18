---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-c893f42e33a6.md
- raw/papers/winkler-2014-palm.md
- raw/papers/semanticscholar-50e828bd956a.md
- raw/papers/semanticscholar-89e6c89fac1d.md
tags:
- neuroimaging-dti
- tract-based-spatial-statistics
- white-matter
- voxel-wise-analysis
- fsl
title: TBSS
type: concept
updated: '2026-05-18'
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

TBSS's final statistical stage—voxel-wise cross-subject comparison on the white-matter skeleton—operates within the framework of permutation inference for the general linear model. [[raw/papers/winkler-2014-palm.md|Winkler et al. (2014)]] consolidated this framework, introducing a generalised statistic that remains robust under heteroscedasticity and evaluating strategies such as exchangeability blocks for complex experimental designs. [[raw/papers/winkler-2014-palm.md|Winkler et al. (2014)]] addressed the multiple-comparisons problem inherent in whole-brain analysis, providing guidelines that directly support FSL's `randomise` tool used in TBSS pipelines. [[raw/papers/winkler-2014-palm.md|Winkler et al. (2014)]] further compared permutation strategies including Freedman-Lane and Smith methods, establishing the statistical backbone that enables robust group inference in TBSS and related [[neuroimaging]] analyses.

In clinical research, TBSS has been applied to identify neurobiological markers linked to treatment response. [[raw/papers/semanticscholar-c893f42e33a6.md|Yang et al. (2025)]] used the TBSS procedure in [[fsl]] to conduct voxel-wise statistical analysis of tensor-based parameters—including [[fractional-anisotropy]], mean diffusivity, axial diffusivity, and radial diffusivity—in first-episode major depressive disorder patients after two weeks of SSRI treatment. [[raw/papers/semanticscholar-c893f42e33a6.md|Yang et al. (2025)]] found that the effective-treatment group showed significantly higher axial diffusivity and mean diffusivity values in the left cingulum hippocampal region compared to healthy controls. [[raw/papers/semanticscholar-c893f42e33a6.md|Yang et al. (2025)]] also demonstrated significant positive correlations between cingulum hippocampal fractional anisotropy and HAMD-17 clinical scores, suggesting that TBSS-derived [[white-matter]] measures can serve as predictors of antidepressant outcomes.

While TBSS collapses data onto a common skeleton, tractography-based methods preserve anatomical tract topology for group-level comparison. [[raw/papers/semanticscholar-50e828bd956a.md|Zhang et al. (2025)]] studied whole-brain white matter in 707 subjects from the [[hcp-dataset]] using diffusion MRI tractography combined with a fiber clustering pipeline and suprathreshold fiber cluster statistics. [[raw/papers/semanticscholar-50e828bd956a.md|Zhang et al. (2025)]] identified significant differences in specific pathways such as the arcuate fasciculus, corticospinal tract, and corpus callosum, linking these [[structural-connectivity]] variations to neurobehavioral measures. [[raw/papers/semanticscholar-50e828bd956a.md|Zhang et al. (2025)]] showed that tract-level analysis captures connectivity patterns at the anatomical pathway level, offering a complementary strategy to skeleton-based voxel-wise projection for studying population differences in brain networks.

## References

- Smith et al. (2006) — Tract-based spatial statistics: voxelwise analysis of multi-subject diffusion data. NeuroImage 31(4): 1487–1505. https://doi.org/10.1016/j.neuroimage.2006.02.024
- Smith et al. (2009) — TBSS with crossing fibres. NeuroImage 43(4): 623–635. https://doi.org/10.1016/j.neuroimage.2009.03.024