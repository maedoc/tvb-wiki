---
title: "AFNI (Analysis of Functional NeuroImages)"
created: 2025-03-15
updated: 2025-04-23
type: entity
tags: [software-brain-modeling, neuroimaging-fmri, software-visualization, preprocessing-pipeline, whole-brain-modeling]
sources: []
---

## Overview

**AFNI** (Analysis of Functional NeuroImages) is a comprehensive, open-source software package for the analysis and visualization of functional and anatomical neuroimaging data, primarily developed at the National Institutes of Health (NIH). Developed since the mid-1990s by [[Robert-Cox]], AFNI provides a command-line driven environment for processing [[fmri|fMRI]] data, structural MRI, diffusion imaging, and other neuroimaging modalities.

AFNI is written primarily in C and distributed under an open-source license, making it freely available for academic and commercial use. The software is particularly valued for its advanced visualization capabilities, real-time fMRI processing capabilities (Cox et al., 2009), and extensive collection of command-line tools for preprocessing, statistical analysis, and post-processing of brain data.

## Key Features

### Preprocessing Pipeline
AFNI offers a complete preprocessing workflow including motion correction (3dvolreg), slice timing correction (3dTshift), spatial smoothing (3dBlurToFWHM), and intensity normalization. The software supports both voxel-wise and surface-based analyses through integration with [[FreeSurfer]] outputs and its companion surface mapping and analysis tool (SUMA).

### Statistical Analysis
The package provides robust tools for general linear model (GLM) analysis, including the `3dDeconvolve` and `3dREMLfit` programs for hemodynamic response modeling. AFNI's approach to multiple comparisons correction includes both traditional [[family-wise-error|family-wise error]] methods and modern [[false-discovery-rate|false discovery rate]] (FDR) corrections, along with cluster-based thresholding via `3dClustSim` (Cox et al., 2017).

### Real-Time fMRI
AFNI supports real-time fMRI analysis capabilities, enabling online data acquisition, quality assurance, and basic statistical processing during scanning sessions (Cox et al., 2009). This is particularly relevant for [[neurofeedback]] applications and quality control.

### Surface-Based Analysis (SUMA)
SUMA (Surface Mapping and Analysis) is AFNI's companion tool for surface-based visualization and analysis, supporting cortical surface rendering, surface-based registration, and cross-modal integration of volume and surface data.

### Visualization
The `afni` GUI provides interactive visualization of brain volumes, surface-rendered data, and time series plots. The software supports multiple color maps, anatomical underlays, and specialized displays for quality control.

## Relationship to TVB

AFNI and [[TVB|The Virtual Brain]] serve complementary roles in computational neuroscience. AFNI is primarily an analysis tool for empirical neuroimaging data, while TVB is a simulation platform for whole-brain modeling. Typical workflows involve:

1. Using AFNI for preprocessing raw [[resting-state|resting-state fMRI]] or task-based data
2. Computing [[functional-connectivity|functional connectivity]] matrices from preprocessed time series
3. Exporting these matrices for import into TVB as functional priors or validation targets for structural connectivity simulations

AFNI's ability to process [[diffusion-imaging|DTI/DWI]] data and generate fractional anisotropy maps also supports the construction of [[structural-connectivity|structural connectivity]] matrices through [[tractography|tractography]] pipelines.

## Comparison with Related Software

| Feature | AFNI | [[FSL]] | [[SPM]] |
|---------|------|---------|---------|
| Primary Language | C | C++ | MATLAB |
| License | Open source | Open source | Open source |
| Real-time Processing | Yes | Limited | No |
| Surface Analysis | Via SUMA | Yes | Yes |
| Command-line Focus | Strong | Strong | Moderate |
| SPM Interface | Yes (BRIK/HEAD) | Yes | N/A |

*Note: Real-time and surface analysis capabilities reflect typical usage patterns as of the last major software documentation; features may vary by version and specific implementation.*

## Related Software

- [[TVB]] -- Whole-brain simulation platform that can use AFNI-processed connectivity data
- [[FSL]] -- Alternative analysis package often used in conjunction with AFNI for specific processing steps
- [[ANTs]] -- Advanced normalization and registration tools frequently called from AFNI scripts
- [[FreeSurfer]] -- Cortical surface reconstruction used as input for surface-based AFNI analyses

## Key Papers

Cox, R.W. (1996). AFNI: software for analysis and visualization of functional magnetic resonance neuroimages. *Computers and Biomedical Research*, 29(3), 162-173.

Cox, R.W., & Hyde, J.S. (1997). Software tools for analysis and visualization of fMRI data. *NMR in Biomedicine*, 10(4-5), 171-178.

Cox, R.W., Jesmanowicz, A., & Hyde, J.S. (2009). Real-time fMRI with Afni. *Proceedings of the International Society for Magnetic Resonance in Medicine*, 17, 3269.

Cox, R.W., Chen, G., Glen, D.R., Reynolds, R.C., & Taylor, P.A. (2017). fMRI clustering in AFNI: false-positive rates redux. *Brain Connectivity*, 7(3), 152-171.

## References

1. Cox, R.W. (1996). AFNI: software for analysis and visualization of functional magnetic resonance neuroimages. *Computers and Biomedical Research*, 29(3), 162-173.
2. Cox, R.W., & Hyde, J.S. (1997). Software tools for analysis and visualization of fMRI data. *NMR in Biomedicine*, 10(4-5), 171-178.
3. Cox, R.W., Jesmanowicz, A., & Hyde, J.S. (2009). Real-time fMRI with Afni. *Proceedings of the International Society for Magnetic Resonance in Medicine*, 17, 3269.
4. Cox, R.W., Chen, G., Glen, D.R., Reynolds, R.C., & Taylor, P.A. (2017). fMRI clustering in AFNI: false-positive rates redux. *Brain Connectivity*, 7(3), 152-171.
5. AFNI Documentation: https://afni.nimh.nih.gov/
6. AFNI GitHub Repository: https://github.com/afni/afni
