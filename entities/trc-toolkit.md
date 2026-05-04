---
created: 2025-01-15
sources:
- raw/papers/arxiv-2604.16463.md
- raw/papers/woodman-2014.md
- raw/papers/sanz-leon-2013.md
tags:
- software
- software-tvb
- whole-brain-modeling
- computational-neuroscience
- neuroimaging
- software-visualization
title: TRC Toolkit
type: entity
updated: '2026-05-04'
---

# TRC Toolkit

## Overview

The TRC (Temporal Response Computation) Toolkit is a specialized software package designed for the analysis and processing of time-series [[neuroimaging]] data, with particular emphasis on extracting and characterizing temporal response functions from [[fmri]], EEG, and MEG datasets. Originally developed to support [[whole-brain|whole-brain modeling]] workflows within [[the-virtual-brain]], the toolkit provides a standardized framework for estimating hemodynamic response functions (HRFs), stimulus-evoked neural responses, and event-related potential (ERP) waveforms across different modalities. The TRC Toolkit fills a critical gap in the neuroscience software ecosystem by offering unified methods for temporal response estimation that can be directly applied to parameterize [[neural-mass-models]] and whole-brain simulations.

## Key Features

The TRC Toolkit offers several core capabilities that distinguish it from other analysis packages. First, it implements a comprehensive library of canonical and custom [[hemodynamic-response-function]] models, including the double-gamma HRF, Poisson basis functions, and flexible Fourier-based representations that can capture individual-specific response shapes. Users can fit these models to empirical data using maximum likelihood estimation or Bayesian approaches with variational inference, making the toolkit suitable for both group-level analyses and [[personalized-brain-modeling]] applications.

Second, the toolkit provides robust methods for deconvolution of fMRI [[bold-signal|BOLD]] signals to estimate underlying neural activity, implementing algorithms such as Wiener filtering, Bayesian temporal deconvolution, and adaptive kernel regression. This functionality is particularly valuable for researchers working with [[resting-state]] data who need to characterize intrinsic fluctuations versus stimulus-evoked responses.

Third, the TRC Toolkit includes specialized visualization tools for displaying temporal response properties across cortical regions, with integration hooks for popular neuroimaging packages including [[nilearn]], [[mne-python]], and [[fieldtrip]]. The visualization module supports display of response latencies, amplitudes, and dispersion parameters as cortical maps or region-of-interest time series.

## Relationship to TVB

Within the [[the-virtual-brain]] ecosystem, the TRC Toolkit serves as a critical bridge between empirical neuroimaging data and the [[neural-mass-models]] used in whole-brain simulations.TVB's forward modeling pipeline requires accurate specification of temporal response properties to generate realistic simulated BOLD signals that can be directly compared with empirical data during [[model-validation]]. The toolkit enables researchers to extract patient-specific or group-specific HRF parameters from their data and feed these directly into TVB simulations via the [[tvb-library]] adapters.

Additionally, the TRC Toolkit supports TVB's [[parameter-estimation]] workflows by providing the inverse modeling capabilities needed to fit model parameters to empirical time series. When researchers use TVB to simulate [[brain-oscillations]] or [[epilepsy-modeling]] scenarios, the toolkit can assess goodness-of-fit by comparing simulated and empirical temporal response characteristics.

## Methodological Foundations

The mathematical core of the TRC Toolkit revolves around [[linear]] time-invariant (LTI) system identification for neural hemodynamic coupling. For fMRI data, the toolkit models the relationship between neural activity n(t) and observed BOLD signal y(t) through the hemodynamic response function h(t) as a convolution:

y(t) = h(t) * n(t) + ε(t)

where ε(t) represents measurement noise. The toolkit implements multiple approaches to invert this relationship, including frequency-domain deconvolution using the Fourier transform, time-domain FIR basis fitting, and parametric models that incorporate vascular physiology parameters such as the [[bold-model]] balloon model framework.

For EEG and MEG data, the toolkit provides equivalent functionality for characterizing event-related spectral perturbations and evoked response waveforms, enabling cross-modal integration with fMRI-derived HRF estimates.

## Related Software

The TRC Toolkit complements several established packages in the neuroimaging ecosystem. Unlike general-purpose analysis tools such as [[spm]] or [[fsl]], the TRC Toolkit focuses specifically on temporal response characterization with direct applications to computational modeling. It extends the functionality of [[eeglab]] for ERP analysis by adding Bayesian deconvolution methods, and provides alternative implementations to the temporal response function estimation in [[brainiak]].

For whole-brain modeling workflows, the toolkit integrates with [[connectome-workbench]] for visualization and with [[dipy]] for preprocessing of [[diffusion-imaging]] data when [[structural-connectivity]] estimates are needed alongside temporal response parameters.

## References

1. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f)
2. Woodman et al. (2014). *[[graphvar]]: A user-friendly toolbox for comprehensive graph analyses of functional brain [[connectivity]]*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)
3. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)