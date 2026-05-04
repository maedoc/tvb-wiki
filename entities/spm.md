---
title: SPM (Statistical Parametric Mapping)
created: 2024-01-15
updated: 2026-05-04
type: entity
tags: [software, neuroimaging-fmri, neuroimaging-eeg, neuroimaging-meg, neuroimaging, dynamic-causal-modeling]
sources:
  - Friston, K. J., Holmes, A. P., Worsley, K. J., Poline, J. B., Frith, C. D., & Frackowiak, R. S. (1994). Statistical parametric maps in functional imaging: A general linear approach. Human Brain Mapping, 2(4), 189-210.
  - Penny, W. D., Stephan, K. E., Mechelli, A., & Friston, K. J. (2011). Comparing dynamic causal models of FMRI. NeuroImage, 55(4), 1335-1352.
  - Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. NeuroImage, 19(4), 1273-1302.
---

SPM (Statistical Parametric Mapping) is a software toolbox for analyzing neuroimaging data, primarily developed and maintained by the Wellcome Trust Centre for Neuroimaging at University College London. Originally released in ~1991 (SPM91), SPM provides a unified framework for preprocessing, statistical modeling, and visualization of data from multiple neuroimaging modalities including [[fmri|fMRI]], [[eeg|EEG]], and [[meg|MEG]]. The software implements the General Linear Model (GLM) approach to statistical analysis of brain imaging data, treating each voxel as a dependent variable in a linear regression framework [@friston1994statistical].

## Relationship to TVB

SPM occupies an important position in the [[the-virtual-brain]] ecosystem as a preprocessing and analysis option for generating input data used in whole-brain modeling. TVB's connectivity pipelines can accept parcellated time series data that has been preprocessed using SPM, particularly for [[functional-connectivity]] analyses. The software's robust implementation of [[hemodynamic-response-function]] (HRF) modeling and batch processing capabilities make it suitable for handling large neuroimaging datasets that feed into TVB's [[structural-connectivity]] matrices derived from [[dti|DTI]] tractography. Additionally, SPM's [[dynamic-causal-modeling]] (DCM) framework, which was developed by the same research group led by Karl Friston, provides an alternative approach to effective connectivity estimation that complements TVB's neural mass model implementations [@friston2003dynamic]. Users often use SPM for initial data quality control and group-level statistics before exporting region-wise time series to TVB for dynamical systems analysis.

## Key Features

SPM is implemented in MATLAB and employs a modular architecture that facilitates integration with other neuroimaging tools including [[fsl]], [[afni]], and [[nipype]] (which provides Python wrappers around SPM and other tools). The software implements canonical HRF models with optional temporal and dispersion derivatives for improved modeling of the hemodynamic response in [[resting-state]] and task-based fMRI experiments. For EEG and MEG analysis, SPM provides source reconstruction algorithms based on beamforming and minimum norm estimates, along with tools for time-frequency decomposition and phase-synchrony analysis. The toolbox includes comprehensive data visualization capabilities for displaying statistical parametric maps overlaid on anatomical templates in [[mni-space]], as well as network visualization tools for presenting connectivity results.

## Key Papers

- Friston, K. J., Holmes, A. P., Worsley, K. J., Poline, J. B., Frith, C. D., & Frackowiak, R. S. (1994). Statistical parametric maps in functional imaging: A general linear approach. Human Brain Mapping, 2(4), 189-210.
- Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. NeuroImage, 19(4), 1273-1302.
- Penny, W. D., Stephan, K. E., Mechelli, A., & Friston, K. J. (2011). Comparing dynamic causal models of FMRI. NeuroImage, 55(4), 1335-1352.

## Technical Implementation

The statistical framework in SPM is built upon the General Linear Model, which relates observed brain signal at each voxel to a linear combination of explanatory variables (design matrix) plus error terms. For fMRI analysis, this approach enables modeling of task effects, confounds, and between-subject variance through appropriate column selection in the design matrix [@friston1994statistical]. SPM implements classical and Bayesian estimation schemes, with the Bayesian approach providing posterior probability maps for activation and explicit modeling of uncertainty in parameter estimates. The software uses random field theory for family-wise error correction across multiple comparisons, ensuring valid statistical inference across the entire brain volume.

## Related Software

SPM shares conceptual and development lineage with [[fieldtrip]], another toolbox from the UCL neuroimaging group that focuses on EEG and MEG source analysis. Within the broader neuroimaging ecosystem, SPM is often used alongside [[nilearn]] for machine learning applications on brain imaging data, [[mne-connectivity]] for functional connectivity estimation, and [[bids|BIDS]]-compatible preprocessing pipelines like [[fmriprep]] for initial data preparation before statistical analysis.
