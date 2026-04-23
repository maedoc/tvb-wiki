---
title: AFNI
created: 2026-04-20
updated: 2026-04-23
type: entity
tags: [software-brain-modeling, neuroimaging-fmri, resting-state, task-based, whole-brain-modeling]
sources: []
---

# AFNI

## Overview

**AFNI** (Analysis of Functional Neuroimages) is an open-source software suite for the processing, analysis, and visualization of neuroimaging data, particularly functional magnetic resonance imaging (fMRI). AFNI was developed by Robert W. Cox at the Medical College of Wisconsin, with the first major publication in 1996 describing its foundational architecture. The software is written primarily in C and is distributed under an open-source license.

AFNI provides tools for preprocessing, statistical analysis, and visualization of brain imaging data across multiple modalities including fMRI, structural MRI, DTI, and EEG/MEG when co-registered with anatomical data. The software uses a modular command-line architecture with a Python-based scripting interface and supports both individual and group-level analyses.

## Key Features

### Preprocessing Pipeline
AFNI includes preprocessing capabilities for motion correction, slice-timing correction, spatial smoothing, spatial normalization to standard templates, and temporal filtering. The suite's preprocessing tools are designed to minimize artifacts while preserving biological signals.

### Statistical Analysis
The core statistical engine implements the general linear model (GLM) for task-based analysis, with both voxel-wise and region-of-interest approaches. AFNI includes methods for multiple comparisons correction, including spatial clustering thresholds and group comparison tools. The software supports permutation testing.

### Connectivity and Network Analysis
AFNI provides tools for resting-state fMRI analysis, including ICA-based artifact removal, seed-based correlation mapping, and Granger causality estimation. Tools are available for computing full correlation matrices for graph-theoretic analysis of functional connectivity networks.

### Surface and Volume-Based Analysis
The suite supports both volumetric and surface-based representations through integration with FreeSurfer and SUMA (Surface Mapping with AFNI), enabling cortical surface visualization and analysis.

### Real-Time fMRI
AFNI includes real-time fMRI capabilities, enabling online data quality monitoring and neurofeedback applications.

## Relationship to TVB

AFNI and The Virtual Brain (TVB) operate at different scales but can serve complementary roles in whole-brain modeling workflows:

1. **Data Preparation**: AFNI provides preprocessing pipelines that prepare empirical fMRI and DTI data for input into TVB. Preprocessed BOLD signals from AFNI can be used as empirical targets for TVB simulations.

2. **Structural Connectivity**: AFNI's tractography tools and DTI preprocessing capabilities (via integration with external tools like TrackVis or MRtrix) process diffusion data that can inform TVB's structural connectivity matrices.

3. **Validation**: TVB simulation outputs can be exported to AFNI-compatible formats for comparison with empirical data, enabling direct validation of neural mass model predictions against observed fMRI time series.

## Key Papers

- **Cox, R. W. (1996)**. AFNI: Software for analysis and visualization of functional magnetic resonance neuroimages. *Computers and Biomedical Research*, 29(3), 162-173. ([doi:10.1006/cbmr.1996.0014](https://doi.org/10.1006/cbmr.1996.0014)) — Original AFNI paper describing the foundational architecture and statistical framework.

- **Cox, R. W., & Hyde, J. S. (1997)**. Software tools for analysis and visualization of fMRI data. *NMR in Biomedicine*, 10(4-5), 171-178. — Early validation and methodology.

- **Cox, R. W., et al. (2017)**. FMRI clustering in AFNI: Preliminary results. *Frontiers in Neuroscience*, 11, 506. ([doi:10.3389/fnins.2017.00506](https://doi.org/10.3389/fnins.2017.00506)) — Updates on clustering and multiple comparisons correction methods.

- **Gorgolewski, K. J., et al. (2011)**. Nipype: A flexible, lightweight and extensible neuroimaging data processing framework in Python. *Frontiers in Neuroinformatics*, 5, 13. — Describes AFNI's integration into modern Python-based neuroimaging pipelines.

## Related Software

- [[TVB|The Virtual Brain]] — Large-scale brain network simulation framework that can use AFNI-preprocessed data
- [[FSL|FSL]] — Alternative neuroimaging analysis suite with overlapping functionality
- [[FreeSurfer|FreeSurfer]] — Structural analysis and cortical surface reconstruction often used with AFNI
- [[SPM|SPM]] — MATLAB-based statistical parametric mapping software
- [[Nipype|Nipype]] — Python framework that integrates AFNI with other neuroimaging tools

## References

1. Cox, R. W. (1996). AFNI: Software for analysis and visualization of functional magnetic resonance neuroimages. *Computers and Biomedical Research*, 29(3), 162-173. [doi:10.1006/cbmr.1996.0014](https://doi.org/10.1006/cbmr.1996.0014)

2. Cox, R. W., & Hyde, J. S. (1997). Software tools for analysis and visualization of fMRI data. *NMR in Biomedicine*, 10(4-5), 171-178.

3. Cox, R. W., Chen, G., Glen, D. R., Reynolds, R. C., & Taylor, P. A. (2017). FMRI clustering in AFNI: Preliminary results. *Frontiers in Neuroscience*, 11, 506. [doi:10.3389/fnins.2017.00506](https://doi.org/10.3389/fnins.2017.00506)

4. Gorgolewski, K. J., Auer, T., Calhoun, V. D., Craddock, R. C., Das, S., Duff, E. P., ... & Poldrack, R. A. (2011). Nipype: A flexible, lightweight and extensible neuroimaging data processing framework in Python. *Frontiers in Neuroinformatics*, 5, 13. [doi:10.3389/fninf.2011.00013](https://doi.org/10.3389/fninf.2011.00013)
