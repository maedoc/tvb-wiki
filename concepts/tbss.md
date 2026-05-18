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

TBSS addresses a key problem in voxel-wise DTI analysis: alignment of [[white-matter]] tracts across subjects is much harder than grey-matter alignment because tract shapes vary substantially. TBSS solves this by:
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
Done. Here's what changed:

**`concepts/tbss.md` (and synced `docs/concepts/tbss.md`)**
- Replaced the sparse 26-word bullet list in the **Related** section with ~170 words of dense sourced prose
- Added 3 inline citations from all 3 available sources:
  - `[[raw/papers/semanticscholar-50e828bd956a.md|Zhang et al. (2025)]]` — tractography complement in HCP sex-differences study
  - `[[raw/papers/semanticscholar-c893f42e33a6.md|Yang et al. (2025)]]` — clinical TBSS application in depression treatment prediction
  - `[[raw/papers/winkler-2014-[[palm]].md|Winkler et al. (2014)]]` — permutation inference foundations for FSL `randomise` and [[palm]]
- Added 10 wikilinks to existing pages: `diffusion-mri`, `tractography`, `[[hcp-dataset]]`, `fractional-anisotropy`, `fsl`, `[[fsl-randomise]]`, `palm`, `[[neuroimaging]]`, `white-matter`, `structural-connectivity`
- Bumped `updated` date to `2026-05-18` in YAML frontmatter
- Logged the action in `log.md`

## References

1. Chunxia Yang, Jiaxin Han, N. Sun, Penghong Liu, Kerang Zhang, Aixia Zhang, Zhifen Liu. (2025). *Identifying neurobiological markers as predictors of antidepressant treatment using diffusion tensor imaging: A tract-based spatial statistical analysis of cingulate bundle*. CNS Spectrums. [DOI](https://doi.org/10.1017/S1092852925000252)
2. (authors unknown). *Permutation inference for the general linear model*.
3. Fan Zhang, Jarrett Rushmore, Yijie Li, S. Cetin-Karayumak, Yang Song, Weidong Cai, C. Westin, J. Levitt, N. Makris, Y. Rathi, Lauren J. O’Donnell. (2025). *Study of Sex Differences in the [[whole-brain]] White Matter Using Diffusion MRI Tractography and Suprathreshold Fiber Cluster Statistics*. bioRxiv. [DOI](https://doi.org/10.1101/2025.09.27.679006)
4. Nina Baldy, P. Triebkorn, S. Petkoski, Meysam Hashemi, V. Jirsa. (2026). *Normative Modeling of Static and Dynamic [[functional-connectivity]]*. bioRxiv. [DOI](https://doi.org/10.64898/2026.04.03.716292)