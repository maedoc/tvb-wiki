---
title: AFNI
created: 2024-01-15
updated: 2026-04-24
type: entity
tags: [software-brain-modeling, neuroimaging-fmri, neuroimaging-dti, software-visualization, dynamic-causal-modeling]
sources:
  - Cox 1996 (Computers and Biomedical Research)
  - Saad et al. 2004 (NeuroImage)
  - https://afni.nimh.nih.gov
---

# AFNI

## Overview
AFNI (Analysis of Functional NeuroImages) is an open-source software suite for processing, analyzing, and visualizing structural and functional neuroimaging data. Developed primarily at the National Institute of Mental Health (NIMH) by Robert Cox and colleagues beginning in 1994[^1], AFNI represents one of the three dominant neuroimaging analysis platforms alongside [[fsl]] and [[spm]]. The software is written in C with extensive command-line tools and provides both volume- and surface-based analysis capabilities through its integrated SUMA (Surface Mapping with AFNI) component.

## Key Features
The AFNI distribution encompasses a comprehensive toolchain for neuroimaging analysis:

**Preprocessing Pipeline**: Robust motion correction with Fourier interpolation, slice-timing correction for interleaved acquisitions, susceptibility distortion correction, spatial normalization to standard templates (MNI152, Talairach-Tournoux), Gaussian smoothing, and intensity normalization. AFNI's 3dvolreg and 3dalign tools are widely used for head motion correction in [[fmri]] studies.

**Statistical Framework**: Extensive implementations of general linear models (GLM) for block and event-related designs, mixed-effects models for hierarchical group analysis, ANOVA for factorial designs, and non-parametric permutation testing via 3dttest++ and 3dMEMA. The package provides multiple comparison correction via family-wise error rates, false discovery rate (FDR), and cluster-based thresholding.

**Connectivity Analysis**: Dedicated tools for resting-state functional connectivity including seed-based correlation (3dNetCorr), whole-brain covariance analysis, and independent component analysis (ICA) via 3dICA. Effective connectivity can be estimated through beta-series correlation, psychophysiological interaction (PPI), and [[dynamic-causal-modeling]] interfaces.

**Surface Mapping**: SUMA provides cortical surface reconstruction, inflation, and flattening capabilities, supporting FreeSurfer surface formats and CIFTI dense timeseries. Surface-volume alignment allows simultaneous visualization of subcortical and cortical activation patterns[^2].

**Real-Time Capabilities**: Unique among major neuroimaging packages, AFNI supports real-time [[fmri]] processing for neurofeedback experiments and clinical monitoring via the RT-Mon plugin architecture.

## Relationship to TVB
AFNI serves as an essential preprocessing and data extraction stage for [[the-virtual-brain]] workflows, bridging empirical neuroimaging and computational modeling:

**Structural Connectivity**: AFNI processes raw diffusion-weighted images and coordinates with [[ants]] (available as an optional extension) to generate structural connectivity matrices through probabilistic or deterministic tractography. These matrices define the anatomical connection weights between TVB network nodes.

**Functional Constraints**: AFNI-derived empirical functional connectivity matrices—computed from preprocessed resting-state fMRI via 3dNetCorr—provide target data for fitting [[neural-mass-models]] in TVB. The time series extraction capabilities (3dROIstats) enable comparison between simulated and empirical BOLD signals.

**Parcellation Alignment**: Through nonlinear registration to standard atlases (e.g., [[desikan-killiany-atlas]], [[glasser-atlas]]), AFNI ensures that region-of-interest time series map accurately to TVB node indices, critical for proper network topology in whole-brain models.

**Cross-Modal Integration**: Tools like 3dBrainSync enable alignment of [[eeg]]/[[meg]] source-localized activity with fMRI data, supporting multimodal validation of TVB simulations.

## Key Papers
The foundational AFNI publication (Cox, 1996) established the software's core philosophy of optimized C implementations for rapid volumetric analysis. Subsequent methodological developments include the SUMA surface mapping system (Saad et al., 2004), real-time fMRI capabilities, and modern statistical frameworks for group analysis. AFNI is widely cited in the neuroimaging literature and remains actively developed with regular updates from the NIMH Scientific and Statistical Computing Core.

## Related Software
- [[fsl]] — Alternative comprehensive neuroimaging analysis suite (FMRIB Software Library)
- [[spm]] — Statistical Parametric Mapping, MATLAB-based neuroimaging toolbox
- [[ants]] — Advanced Normalization Tools, integrated with AFNI for registration and segmentation
- [[freesurfer]] — Cortical surface reconstruction and parcellation, frequently used upstream of AFNI analysis
- [[the-virtual-brain]] — Whole-brain simulation platform utilizing connectivity matrices derived from AFNI preprocessing

## References

[^1]: Cox, R. W. (1996). AFNI: Software for analysis and visualization of functional magnetic resonance neuroimages. *Computers and Biomedical Research*, 29(3), 162–173. https://doi.org/10.1006/cbmr.1996.0014

[^2]: Saad, Z. S., Reynolds, R. C., Argall, R., Japee, S., & Cox, R. W. (2004). SUMA: An interface for surface-based intra- and inter-subject analysis with AFNI. *NeuroImage*, 22(1), 519–524. https://doi.org/10.1016/j.neuroimage.2004.01.024

- Official AFNI website: https://afni.nimh.nih.gov
- AFNI documentation repository: https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/
