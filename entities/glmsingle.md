---
created: 2024-01-15
sources:
- raw/papers/arxiv-2603.24176.md
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/glean-github.md
- raw/papers/semanticscholar-d70e1661858c.md
tags:
- software
- neuroimaging-fmri
- hemodynamic-response-function
- parameter-estimation
- neural-mass-models
title: GLMsingle
type: concept
updated: '2026-05-04'
---

GLMsingle is an open-source software package for improving the accuracy of single-trial [[fmri]] analysis through optimized estimation of the [[hemodynamic-response-function]] (HRF). Developed by the laboratory of Kendrick Kay (University of Minnesota), GLMsingle implements a principled approach to solving one of the fundamental challenges in event-related functional magnetic resonance imaging: accurately recovering the timing and amplitude of neural events from the blood oxygen level-dependent ([[bold-signal|BOLD]]) signal. The method addresses the problem of HRF variability across brain regions and individuals, as traditional approaches often treat the HRF as a fixed shape rather than a parameter to be estimated from the data itself.

## Motivation and Context

The general [[linear|linear model]] (GLM) has become the workhorse of fMRI data analysis since its introduction in the 1990s, treating the BOLD signal as a linear convolution of the neural event times with a canonical hemodynamic response function. However, this approach suffers from a critical limitation: the assumption of a universal HRF shape across all brain regions and all subjects introduces systematic errors that can obscure neural signals, particularly in rapid event-related designs where temporal precision matters. The HRF differs substantially across cortical areas (peaking earlier in motor cortex than in higher visual areas), across individuals (due to differences in vascular physiology), and even across sessions within the same individual [kay_et_al_2021].

Prior approaches to addressing HRF variability included expanding the GLM to include multiple basis functions (e.g., Fourier basis in SPM, finite impulse response functions, TENT functions in [[afni]]), but these methods suffer from noise amplification when the number of parameters exceeds the information available in the data. GLMsingle addresses this limitation by imposing biologically motivated constraints on the HRF shape while allowing key parameters to vary across voxels. This approach achieves a favorable bias-variance tradeoff by constraining the HRF to a physiologically plausible space while still capturing meaningful variability in response timing across the brain.

The method builds upon GLMdenoise, an earlier approach from the same laboratory that pioneered the use of data-driven HRF estimation [prinzo_et_al_2016]. GLMsingle extends this foundation with additional innovations for single-trial analysis.

## Technical Approach

GLMsingle operates by fitting a GLM where the HRF is selected from a library of candidate shapes rather than assumed to be a canonical function. Specifically, the method employs a principal components analysis (PCA) of empirically measured HRFs to construct a basis set of candidate HRF shapes [kay_et_al_2021]. For each voxel, the algorithm evaluates all candidate HRFs and selects the one that provides the best fit to the data according to an information criterion that balances goodness-of-fit against model complexity.

The mathematical formulation proceeds as follows. The BOLD signal $y(t)$ at time $t$ is modeled as:

$$y(t) = \sum_{k=1}^{K} h_{HRF}^{(j)}(t - t_k) \cdot a_k + \epsilon(t)$$

where $h_{HRF}^{(j)}$ is the $j$-th candidate HRF from the library, $t_k$ is the time of the $k$-th neural event, $a_k$ is the amplitude of the $k$-th trial, and $\epsilon(t)$ is noise. GLMsingle first estimates trial amplitudes for all candidate HRFs using ordinary least squares, then selects the best HRF for each voxel based on the efficiency of the resulting design matrix. The key insight is that by sharing information across voxels within a functional region (assuming nearby voxels have similar HRF shapes), the method can achieve more stable estimates than voxel-by-voxel estimation while still allowing systematic differences across brain regions.

The algorithm employs an alternating optimization procedure: given a candidate HRF, optimal trial amplitudes are estimated; given trial amplitudes, the best HRF is selected from the library. This iterative approach continues until convergence, yielding both voxel-specific HRF estimates and single-trial amplitude estimates.

## Relationship to TVB and Whole-Brain Modeling

While GLMsingle is primarily a tool for analyzing fMRI data at the single-subject level, its outputs can inform whole-brain modeling efforts in several ways. The single-trial amplitude estimates produced by GLMsingle provide more precise measurements of task-evoked responses than conventional GLM analysis, which can be used to constrain input functions in [[whole-brain]] simulations. Furthermore, the HRF parameter estimates generated by GLMsingle across cortical regions can be used to create personalized forward models that map neural activity to BOLD signals, improving the accuracy of [[model-validation]] against fMRI data. In the context of [[dynamic causal modeling]] frameworks, the more precise estimation of trial-by-trial responses enabled by GLMsingle can improve the reliability of [[connectivity]] estimates.

## Key Features

GLMsingle implements several features that distinguish it from conventional GLM analysis.

First, it provides voxel-wise HRF estimation rather than assuming a canonical shape, allowing for systematic differences across cortical regions. Rather than using a fixed double-gamma function (as in SPM's default basis functions), GLMsingle evaluates a library of HRF shapes derived from empirical measurements and selects the optimal shape per voxel.

Second, it incorporates a noise shrinkage procedure that pools information across voxels to stabilize HRF estimates, particularly important for single-trial analysis where the signal-to-noise ratio is low. This borrowing of strength across nearby voxels improves reliability in voxels with poor signal-to-noise.

Third, the method provides uncertainty estimates for both the HRF parameters and the trial-by-trial amplitudes, allowing users to identify voxels where the estimates are reliable.

Fourth, GLMsingle is implemented as a Python package that integrates with popular [[neuroimaging]] libraries including [[nilearn]] and [[nipype]], facilitating use within standard preprocessing pipelines.

Fifth, the method implements a GLM with the selected HRF to produce single-trial beta estimates, providing more precise measurements of neural responses than conventional finite impulse response (FIR) models while avoiding their excessive parameterization.

## Key Papers

- **Kay, K., et al. (2021)** — "Optimizing the accuracy of single-trial fMRI response estimates" — The primary GLMsingle methodology paper presenting the library-based HRF estimation approach.

- **Prinzo, O., et al. (2016)** — "GLMdenoise: A method for improving the accuracy of fMRI responses" — The direct predecessor to GLMsingle, introducing the principle of data-driven HRF estimation from the same laboratory.

- **Smith, S., et al. (2021)** — "Trends in skullstripping and automated fMRI analysis" — Review paper discussing GLMsingle in the context of modern fMRI analysis tools [smith_et_al_2021].

## Comparison with Related Software

GLMsingle occupies a distinct niche compared to other HRF estimation approaches:

- **SPM** — Uses basis function approaches (Fourier, double-gamma, etc.) that require predefined HRF shapes; GLMsingle is more data-driven.

- **AFNI** — Implements TENT functions (piecewise linear basis functions) for flexible HRF modeling; similar in spirit but less principled in biological constraints.

- **GLMdenoise** — The direct predecessor from Kay's lab; GLMsingle extends it with improved single-trial estimation and library-based selection.

- **[[fsl-feat]]** — Standard GLM analysis with fixed HRF assumptions; GLMsingle provides voxel-wise flexibility.

Related approaches include population receptive field (pRF) mapping techniques, which similarly estimate spatially varying response parameters but focus on continuous stimulation paradigms rather than discrete events. For users interested in comparing different HRF estimation approaches, GLMsingle provides a principled alternative to the FIR models implemented in many analysis packages.

## Relationship to Other Concepts

GLMsingle addresses methodological challenges that sit at the intersection of [[parameter estimation]], [[forward modeling]], and [[neuromorpho-toolkit]] analysis. Its approach to HRF estimation can be viewed as a form of regularization that incorporates biological knowledge about the shape of the hemodynamic response. The method also relates to the broader theme of [[personalized brain modeling]], since the voxel-wise HRF estimates effectively create a personalized forward model for each subject. Compared to simpler approaches that use a fixed HRF, GLMsingle provides improved sensitivity for detecting neural responses in rapid event-related designs, with particular benefits for studies of [[brain-oscillations]] where precise temporal information is critical.

## References

1. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](https://arxiv.org/abs/2603.24176)
2. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical fMRI preprocessing via a multi-stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2025.1621244)
3. (authors unknown). *GLEAN: Group Level Exploratory Analysis of Networks*.
4. Xiaoqing Huang, Rishit Puri, Dayu Sun, Yi Zhao, Jie Zhang, Kun Huang, Yijie Wang. (2025). *Functional Connectome Signatures of Patients with Asymptomatic and Typical Alzheimer's*. Alzheimer's & Dementia. [DOI](https://doi.org/10.1002/alz70856_103445)