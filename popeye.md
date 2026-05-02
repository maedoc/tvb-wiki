---
title: PopEye
created: 2026-05-02
updated: 2026-05-02
type: entity
tags: [software-brain-modeling, neuroimaging-fmri, parameter-estimation, software-visualization]
sources:
  - https://github.com/kdesimone/popeye
  - DeSimone et al. (2016). PopEye: a population receptive field estimation tool. Journal of Open Source Software, 1(8), 103.
---

# PopEye

## Overview
PopEye is an open-source Python toolbox for estimating population receptive fields (pRF) from fMRI data. Developed by Kevin DeSimone and colleagues, PopEye provides a comprehensive framework for mapping the representational structure of sensory and cognitive representations in the brain using quantitative models of neural population responses[^1]. The population receptive field model is a computational approach that quantifies the cumulative response properties of all neurons within a single neuroimaging voxel, enabling researchers to characterize the functional organization of cortical areas with unprecedented precision[^2].

The pRF approach builds on classical receptive field mapping techniques but extends them to the scale of fMRI voxels, where thousands of neurons contribute to the measured BOLD (blood oxygen level-dependent) signal. By modeling the relationship between visual (or other sensory) stimuli and the measured fMRI response, PopEye estimates the spatial position, size, and preference properties of neuronal populations underlying each voxel's response.

## Key Features
PopEye implements a complete pipeline for pRF estimation from raw fMRI data:

**pRF Model Fitting**: The toolbox implements several pRF models including the standard Gaussian model and the difference of Gaussians (DoG) model for characterizing antagonistic center-surround organization[^3]. Models are fit using a coarse-to-fine grid search followed by nonlinear optimization with SciPy for refined parameter estimation.

**Stimulus Reconstruction**: PopEye provides sophisticated tools for generating and handling visual stimuli—including bar stimuli, ring stimuli, wedge stimuli, and natural images—with precise timing information for modeling hemodynamic responses. The stimulus reconstruction pipeline accounts for important physics including display gamma, viewing distance, and pixel aspect ratio.

**Retinotopic Mapping**: The primary application domain is visual cortex retinotopy. PopEye can estimate cortical magnification, eccentricity preferences, and orientation selectivity across visual areas[^5]. The toolbox supports standard phase-encoded retinotopic mapping paradigms and provides built-in visualization of polar angle and eccentricity maps.

**Statistical Validation**: Built-in tools assess the goodness-of-fit using R² values, compare competing models using AIC/BIC criteria, and generate confidence intervals on parameter estimates via bootstrap resampling[^4]. Statistical thresholds help identify reliable pRF estimates versus noisy or ambiguous voxels.

**Surface-Based Analysis**: PopEye supports both volumetric and surface-based analysis workflows, integrating with FreeSurfer for cortical surface reconstruction and enabling visualization on inflated cortical meshes.

## Relationship to TVB
PopEye provides a complementary approach to [[the-virtual-brain]] in the broader ecosystem of computational neuroimaging:

**Functional Constraints for Whole-Brain Models**: PopEye-derived pRF parameters can inform the construction of biologically realistic [[dynamic-causal-modeling]] approaches in TVB. By characterizing the response properties of specific cortical regions (e.g., primary visual cortex, MT), PopEye adds functional constraints that go beyond anatomical connectivity.

**Multimodal Integration**: PopEye operates primarily on [[fmri]] data, while TVB simulates large-scale brain dynamics. Combining empirical pRF estimates with TVB's connectomic models creates opportunities for predictive validation—comparing simulated population responses against empirically estimated pRF properties.

**Visual System Modeling**: For researchers focusing on visual cortex dynamics, PopEye provides the empirical foundation for parameterizing TVB models of early visual processing. The quantitative characterization of receptive field properties serves as ground truth for validating computational models.

**Preprocessing Pipeline**: PopEye requires preprocessed fMRI time series, similar preprocessing requirements as TVB for extracting regional time series from empirical data. Both tools benefit from robust preprocessing pipelines using tools like [[afni]], [[fsl]], or [[spm]].

## The pRF Model
The Gaussian pRF model defines the expected fMRI response as a linear combination of a stimulus encoding function and a hemodynamic response function. Mathematically, the response $r(t)$ at time $t$ is modeled as:

$$r(t) = \text{HRF}(t) \ast \left[\int_{x} s(x,t) \cdot G(x; x_0, \sigma)\, dx\right]$$

where $s(x,t)$ is the stimulus at spatial position $x$ and time $t$, $G(x; x_0, \sigma)$ is a 2D Gaussian with center $x_0$ and standard deviation $\sigma$ (which defines the pRF size), and $\text{HRF}$ is the hemodynamic response function convolved with the stimulus encoding[^2]. The DoG model extends this by combining two Gaussians—a center Gaussian and a surround Gaussian with opposite polarity—to capture antagonistic center-surround organization observed in many visual neurons[^3].

## Software Dependencies
PopEye is written in Python and depends on NumPy, SciPy, and Matplotlib for numerical computation and visualization. It integrates with Nilearn for additional neuroimaging utilities and supports output in formats compatible with visualization tools like [[pysurfer-fixed]]. The toolbox is released under the MIT license, making it freely available for both academic and commercial use.

## Key Papers
The foundational PopEye publication (DeSimone et al., 2016) introduced the toolbox in the Journal of Open Source Software, providing comprehensive documentation and validation against established methods[^1]. The pRF methodology itself builds on seminal work from the Vision Sciences community, particularly the studies by Dumoulin and Wandell (2008) on population receptive field mapping in human visual cortex[^2]. The difference of Gaussians model for characterizing center-surround receptive field organization has roots in early retinal physiology research[^3]. Bootstrap resampling for confidence interval estimation in neuroimaging applications was established through foundational work in statistical inference[^4].

## Related Software
- [[afni]] — Comprehensive neuroimaging suite with preprocessing capabilities
- [[fsl]] — FMRIB Software Library for fMRI preprocessing and analysis
- [[spm]] — Statistical Parametric Mapping, MATLAB-based neuroimaging toolbox
- [[freesurfer]] — Cortical surface reconstruction and parcellation
- [[the-virtual-brain]] — Whole-brain simulation platform
- [[mne-python]] — Python toolbox for EEG/MEG analysis with some pRF capabilities
- [[pysurfer-fixed]] — Python library for cortical surface visualization

## References

[^1]: DeSimone, K., Rokem, A., & Schneider, K. (2016). PopEye: a population receptive field estimation tool. *Journal of Open Source Software*, 1(8), 103. https://doi.org/10.21105/joss.00103

[^2]: Dumoulin, S. O., & Wandell, B. A. (2008). Population receptive field estimates in human visual cortex. *NeuroImage*, 39(2), 647-660. https://doi.org/10.1016/j.neuroimage.2007.09.034

[^3]: Rodieck, R. W. (1965). Quantitative analysis of cat retinal ganglion cell response to visual stimuli. *Vision Research*, 5(11), 583-601. https://doi.org/10.1016/0042-6989(65)90033-7

[^4]: Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall/CRC.

[^5]: Wandell, B. A., Dumoulin, S. O., & Brewer, A. A. (2007). Visual field maps in human cortex. *Neuron*, 56(2), 366-383. https://doi.org/10.1016/j.neuron.2007.10.012

- Official repository: https://github.com/kdesimone/popeye
- PopEye documentation: https://popeye.readthedocs.io/