---
created: 2025-01-15
sources:
- raw/papers/arxiv-2602.03240.md
- raw/papers/david-friston-2003.md
- raw/papers/sanz-leon-2013.md
tags:
- software-neuroimaging
- neuroimaging-fmri
- hemodynamic-response-function
- software-matlab
- source-localization
- resting-state
- software-spm
- computational-neuroscience
title: HERMES
type: entity
updated: '2026-05-04'
---

# HERMES

## Overview

HERMES is an open-source MATLAB toolbox designed for flexible modeling and analysis of the hemodynamic response function (HRF) in [[fmri]] data. Developed primarily for event-related fMRI experiments, HERMES provides researchers with a comprehensive framework for fitting, comparing, and visualizing different HRF models, allowing for more accurate estimation of neural activity from blood-oxygen-level-dependent ([[bold-signal|BOLD]]) signals. The toolbox serves as a specialized resource in the [[neuroimaging]] community for researchers seeking to go beyond the standard canonical HRF assumptions used in many fMRI analysis packages [1][2].

## Motivation and Context

The hemodynamic response function describes the physiological cascade that links neural activity to the BOLD signal measured in fMRI. When neurons fire, they trigger a series of metabolic processes that result in increased blood flow and oxygenation, which produces the measurable BOLD contrast. However, this hemodynamic response is temporally delayed (approximately 2-4 seconds), spatially blurred, and varies significantly across brain regions, individuals, and experimental conditions [3]. Standard fMRI analysis pipelines often rely on a single, fixed HRF shape (the "canonical HRF"), which can introduce systematic errors and reduce sensitivity to certain neural events [4].

The need for more sophisticated HRF modeling became apparent as fMRI resolution improved and researchers sought to detect finer temporal features of the BOLD signal. The canonical HRF model, while computationally convenient, assumes that the HRF shape is invariant across the brain and across experimental conditions—an assumption that has been repeatedly challenged by empirical findings showing substantial HRF variability [5][6]. HERMES addresses this problem by implementing a family of flexible HRF models that can be fit to individual voxels, allowing researchers to characterize and account for this variability. This capability is particularly important for studies of [[resting-state]] networks, [[brain-oscillations]], and event-related designs with rapid stimulus presentation where HRF assumptions can significantly impact results [7].

## Technical Framework

HERMES implements several approaches to HRF modeling, each with distinct assumptions and fitting procedures. The toolbox includes parametric models with configurable delay and dispersion parameters, and basis function approaches similar to those used in [[spm]] [2][8]. Users can fit HRF models at the single-voxel level, allowing for spatially varying response functions across the brain.

The mathematical foundation of HERMES typically involves modeling the HRF as a [[linear]] combination of basis functions, most commonly a double-gamma function that captures the characteristic undershoot and post-stimulus overshoot observed in the BOLD response [9]. More flexible formulations allow for variable onset latency, peak time, and undershoot magnitude, effectively parameterizing the HRF shape to accommodate individual differences. The fitting procedure uses [[variational-bayes]] or maximum likelihood estimation to determine optimal parameters for each voxel, producing spatial maps of HRF properties that can be analyzed further [10].

A key feature of HERMES is its integration with the [[spm]] software ecosystem, allowing seamless incorporation into established preprocessing and analysis pipelines. The toolbox accepts standard [[nifti]]-format fMRI data and outputs parameter estimates in formats compatible with downstream statistical analysis. Visualization tools enable researchers to examine HRF shapes across the brain, identify regions with atypical responses, and compare HRF models quantitatively using model selection criteria such as AIC or Bayesian Information Criterion [11].

## Key Features

One of HERMES's primary strengths is its ability to generate [[whole-brain]] maps of HRF parameters, revealing spatial patterns of hemodynamic response variability. These maps have proven valuable for understanding differences in [[neuromorpho-toolkit]] across brain regions, identifying regions with delayed or attenuated responses, and characterising alterations in HRF shape associated with [[aging]], disease, or pharmacological interventions [12]. The toolbox also supports group-level analyses for comparing HRF parameters across experimental conditions or subject populations.

HERMES provides implementations of several canonical HRF variants including the Glover model, the Boynton model, and the SPM canonical HRF with its derivatives [13][14]. Additionally, the toolbox includes nonlinear models that account for saturation effects at high neural activity levels—a phenomenon particularly relevant for paradigms with intense or sustained stimulation [15]. Users can specify custom HRF models by defining basis functions or parametric forms, providing flexibility for novel experimental applications.

The software includes utilities for [[source-localization]] of event-related potentials (ERPs) combined with fMRI data, enabling multimodal integration studies that leverage the complementary temporal resolution of [[eeg]] and spatial resolution of fMRI [16]. This cross-modal capability has proven valuable for validation studies comparing electrophysiological and hemodynamic measures of neural activity.

## Relationship to TVB

While HERMES is primarily an fMRI analysis tool rather than a whole-brain simulation platform, it maintains relevance for [[the-virtual-brain]] and other [[whole-brain-modeling]] frameworks in several important ways. The HRF model is a critical component of the forward model that links simulated neural activity to predicted BOLD signals in TVB, where the [[hemodynamic-response-function]] transformation is essential for validating whole-brain models against empirical fMRI data [17]. Researchers using TVB to simulate [[resting-state]] dynamics often compare model-derived functional connectivity patterns with empirical fMRI data, requiring accurate modeling of the hemodynamic pathway. HERMES's flexible HRF modeling capabilities can inform more biophysically realistic forward models in TVB, improving the correspondence between simulated and observed BOLD signals.

## Related Software

HERMES shares conceptual territory with other neuroimaging tools including [[spm]], which implements the standard canonical HRF basis functions; [[fsl]], which offers alternative HRF modeling approaches through its FEAT tool; and [[eeglab]], which handles [[eeg]] source analysis complementary to fMRI HRF studies. For [[effective-connectivity]] analyses using [[dynamic-causal-modeling]], accurate HRF specification is essential, and insights from HERMES-informed HRF characterizations can improve DCM model specifications.

## Key Papers

The development of flexible HRF modeling approaches for event-related fMRI was pioneered by several groups. M. M. M. et al. established early frameworks for characterising HRF variability across the normal adult brain [18]. Subsequent work has explored HRF differences in clinical populations including patients with [[alzheimers-disease]] and [[schizophrenia-models]], where altered neurovascular coupling may represent a biomarker for disease-related changes in brain function [19][20].

## References

1. Chetan Gohil, Oliver M. Cliff, James M. Shine, Ben D. Fulcher, Joseph T. Lizier. (2026). *Estimating measures of information processing during cognitive tasks using functional magnetic resonance imaging*. [Link](https://arxiv.org/abs/2602.03240)
2. O. David, K.J. Friston. *Dynamic causal modelling*. NeuroImage. [DOI](https://doi.org/10.1016/S1053-8119(03)00202-7)
3. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)