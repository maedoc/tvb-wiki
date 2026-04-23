---
created: 2026-04-23
sources:
- raw/papers/schirner-2018.md
- raw/papers/arxiv-2602.18715.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/alfaro-almagro-2018.md
- raw/papers/semanticscholar-a324c47ea982.md
tags:
- software-brain-modeling
- structural-connectivity
- connectomics
- diffusion-imaging
- tractography
title: MRtrix3 Connectome
type: entity
updated: '2026-04-23'
---

# MRtrix3 Connectome

## Overview

MRtrix3 Connectome is an automated end-to-end processing pipeline within the [[mrtrix]] software suite for generating whole-brain [[structural-connectivity]] matrices from [[diffusion-mri]] data. It streamlines the complex multi-step workflow required to convert raw diffusion MRI acquisitions into weighted connectivity matrices suitable for network analysis and computational modeling in tools such as [[tvb]].

The pipeline was developed to provide reproducible, standardized connectome generation while maintaining the flexibility for researchers to customize specific processing steps. It integrates preprocessing, fiber orientation estimation, probabilistic [[tractography]], [[sift]] filtering (typically [[sift|SIFT2]] in modern implementations), and parcellation-based connectivity matrix construction into a unified framework.

## Key Features

### Automated Pipeline Stages
The MRtrix3 Connectome script executes the following stages in sequence:

1. **Preprocessing**: Denoising using the Marchenko-Pastur PCA (MP-PCA) method^1, Gibbs ringing removal, distortion correction using FSL TOPUP^2, bias field correction, and intensity normalization across subjects

2. **Tissue Segmentation**: Automated brain extraction and tissue segmentation (gray matter, white matter, CSF) for anatomically-constrained tractography^3

3. **Response Function Estimation**: Multi-shell multi-tissue (MSMT) response function estimation for constrained spherical deconvolution^4

4. **FOD Estimation**: Computation of fiber orientation distributions (FODs) using MSMT-CSD^4, enabling resolution of crossing fiber populations

5. **Tractography**: Probabilistic whole-brain [[tractography]] with anatomical constraints (ACT)^3 to reduce false positives

6. **SIFT2 Filtering**: Application of SIFT2 (Spherical-deconvolution Informed Filtering of Tractograms 2)^5 to correct for streamlines density biases using per-streamline weighting coefficients, superseding the original SIFT method that removed streamlines entirely

7. **Connectome Construction**: Mapping streamlines to a user-specified parcellation (e.g., [[desikan-killiany-atlas]], [[aal-atlas]], [[glasser-atlas]]) to generate a weighted connectivity matrix

### Key Capabilities

| Feature | Description |
|---------|-------------|
| Multi-atlas support | Compatible with Freesurfer, [[aal-atlas]], [[harvard-oxford-atlas]], and custom parcellations |
| Subject-specific | Generates personalized structural connectomes from individual diffusion scans |
| Weight options | Streamline count (SIFT2-weighted), mean FA, mean ADC, or FOD amplitude along bundles |
| Batch processing | Designed for efficient processing of multi-subject datasets |

## Relationship to TVB

MRtrix3 Connectome serves as a critical preprocessing component in [[tvb]] workflows by providing the [[structural-connectivity]] matrices required for whole-brain modeling:

1. **Input Generation**: The weighted connectivity matrices produced by MRtrix3 Connectome (typically using SIFT2-weighted streamline counts from million-scale tractograms) serve as the **weights** matrix in TVB simulations

2. **Transmission Delays**: Tractography-derived fiber lengths from MRtrix3 can be used to compute signal propagation delays between regions based on conduction velocity

3. **Individual Variability**: Subject-specific connectomes enable personalized brain modeling in TVB, capturing individual differences in network topology for clinical or research applications

4. **Integration**: MRtrix3 Connectome outputs (connectome weights and node-wise streamline lengths) can be exported for import into TVB's connectivity format, though users should verify that the parcellation region labels match between the MRtrix3 output and TVB's expected region naming convention

The quality of MRtrix3 Connectome outputs directly impacts TVB simulation results, making preprocessing choices (response function estimation, SIFT2 parameters, parcellation selection) important considerations for model validation.

## Key Papers

- **Tournier et al. (2019)**: "MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation" – *NeuroImage* – Comprehensive description of the MRtrix3 framework including the connectome pipeline

- **Smith et al. (2012)**: "Anatomically-constrained tractography: Improved diffusion MRI streamlines tractography through effective use of anatomical information" – *NeuroImage* – Foundation for the anatomical constraints used in the pipeline

- **Tournier et al. (2008)**: "Resolving crossing fibres using constrained spherical deconvolution: validation with diffusion-weighted imaging phantom data" – *NeuroImage* – Methodological basis for the CSD approach

- **Sotiropoulos & Zalesky (2019)**: "Building connectomes using diffusion MRI: why, how and but" – *Brain Connectivity* – Guidelines for validation and interpretation of connectome data, including critical discussion of tractography biases and connectome construction best practices

- **Yeh et al. (2019)**: "Quantifying brain microstructure with diffusion MRI: Theory and parameter estimation" – *NMR in Biomedicine* – Background on diffusion modeling methods

## Related Software

- [[tvb]] – The Virtual Brain; primary destination software for connectome matrices
- [[mrtrix]] – Parent software suite containing the connectome pipeline
- [[fsl]] – Used internally for distortion correction (TOPUP, eddy)^2
- [[freesurfer]] – Often used for cortical parcellation input
- [[dipy]] – Alternative diffusion analysis Python library
- [[ants]] – Optional registration tool for atlas alignment

## References

^1: Veraart, J., Novikov, D. S., Christiaens, D., Ades-aron, B., Sijbers, J., & Fieremans, E. (2016). Denoising of diffusion MRI using random matrix theory. *NeuroImage*, 142, 394-406.

^2: Andersson, J. L., Skare, S., & Ashburner, J. (2003). How to correct susceptibility distortions in spin-echo echo-planar images: application to diffusion tensor imaging. *NeuroImage*, 20(2), 870-888.

^3: Smith, R. E., Tournier, J. D., Calamante, F., & Connelly, A. (2012). Anatomically-constrained tractography: Improved diffusion MRI streamlines tractography through effective use of anatomical information. *NeuroImage*, 62(3), 1924-1938.

^4: Jeurissen, B., Tournier, J. D., Dhollander, T., Connelly, A., & Sijbers, J. (2014). Multi-tissue constrained spherical deconvolution for improved analysis of multi-shell diffusion MRI data. *NeuroImage*, 103, 411-426.

^5: Smith, R. E., Tournier, J. D., Calamante, F., & Connelly, A. (2015). SIFT2: Enabling dense quantitative assessment of brain white matter connectivity using streamlines tractography. *NeuroImage*, 119, 338-351.