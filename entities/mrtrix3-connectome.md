---
created: 2026-04-23
sources:
- raw/papers/schirner-2018.md
- raw/papers/arxiv-2602.18715.md
- raw/papers/arxiv-2603.24176.md
- raw/papers/alfaro-almagro-2018.md
- raw/papers/semanticscholar-a324c47ea982.md
- raw/papers/semanticscholar-d801ad366cdb.md
- raw/papers/semanticscholar-4d73a30d5c84.md
- raw/papers/semanticscholar-380768cf42a8.md
tags:
- software-brain-modeling
- structural-connectivity
- connectomics
- diffusion-imaging
- tractography
title: MRtrix3 Connectome
type: entity
updated: '2026-05-04'
---

# MRtrix3 Connectome

## Overview

MRtrix3 Connectome is an automated end-to-end processing pipeline within the Mrtrix software suite for generating whole-brain [[structural-connectivity]] matrices from [[diffusion-mri]] data. It streamlines the complex multi-step workflow required to convert raw diffusion MRI acquisitions into weighted connectivity matrices suitable for network analysis and computational modeling in tools such as [[tvb]].

The pipeline was developed to provide reproducible, standardized connectome generation while maintaining the flexibility for researchers to customize specific processing steps. It integrates preprocessing, fiber orientation estimation, probabilistic [[tractography]], [[sift]] filtering (typically [[sift|SIFT2]] in modern implementations), and parcellation-based connectivity matrix construction into a unified framework.

## Key Features

### Automated Pipeline Stages
The Mrtrix3 [[connectome]] script executes the following stages in sequence:

1. **Preprocessing**: Denoising using the Marchenko-Pastur PCA (MP-PCA) method^1, Gibbs ringing removal, distortion correction using FSL TOPUP^2, bias field correction, and intensity normalization across subjects

2. **Tissue Segmentation**: Automated brain extraction and tissue segmentation (gray matter, [[white-matter]], CSF) for anatomically-constrained tractography^3

3. **Response Function Estimation**: Multi-shell multi-tissue (MSMT) response function estimation for constrained spherical deconvolution^4

4. **FOD Estimation**: Computation of fiber orientation distributions (FODs) using MSMT-CSD^4, enabling resolution of crossing fiber populations

5. **Tractography**: Probabilistic [[whole-brain]] [[tractography]] with anatomical constraints (ACT)^3 to reduce false positives

6. **SIFT2 Filtering**: Application of SIFT2 (Spherical-deconvolution Informed Filtering of Tractograms 2)^5 to correct for streamlines density biases using per-streamline weighting coefficients, superseding the original SIFT method that removed streamlines entirely

7. **Connectome Construction**: Mapping streamlines to a user-specified parcellation (e.g., [[desikan-killiany-atlas]], [[aal-atlas]], [[glasser-atlas]]) to generate a weighted connectivity matrix

### Key Capabilities

| Feature | Description |
|---------|-------------|
| Multi-atlas support | Compatible with Freesurfer, [[aal-atlas]], Harvard Oxford Atlas, and custom parcellations |
| Subject-specific | Generates personalized structural connectomes from individual diffusion scans |
| Weight options | Streamline count (SIFT2-weighted), mean FA, mean ADC, or FOD amplitude along bundles |
| Batch processing | Designed for efficient processing of multi-subject datasets |

## Relationship to TVB

MRtrix3 Connectome serves as a critical preprocessing component in [[tvb]] workflows by providing the [[structural-connectivity]] matrices required for whole-brain modeling:

1. **Input Generation**: The weighted [[connectivity]] matrices produced by MRtrix3 Connectome (typically using SIFT2-weighted streamline counts from million-scale tractograms) serve as the **weights** matrix in TVB simulations

2. **Transmission Delays**: Tractography-derived fiber lengths from MRtrix3 can be used to compute signal propagation delays between regions based on conduction velocity

3. **Individual Variability**: Subject-specific connectomes enable [[personalized-brain-modeling]] in TVB, capturing individual differences in network topology for clinical or research applications

4. **Integration**: MRtrix3 Connectome outputs (connectome weights and node-wise streamline lengths) can be exported for import into TVB's connectivity format, though users should verify that the [[parcellation]] region labels match between the MRtrix3 output and TVB's expected region naming convention

The quality of MRtrix3 Connectome outputs directly impacts TVB simulation results, making preprocessing choices (response function estimation, SIFT2 parameters, parcellation selection) important considerations for [[model-validation]].

## Key Papers

- **Tournier et al. (2019)**: "MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation" – *NeuroImage* – Comprehensive description of the MRtrix3 framework including the connectome pipeline

- **Smith et al. (2012)**: "Anatomically-constrained tractography: Improved diffusion MRI streamlines tractography through effective use of anatomical information" – *NeuroImage* – Foundation for the anatomical constraints used in the pipeline

- **Tournier et al. (2008)**: "Resolving crossing fibres using constrained spherical deconvolution: validation with diffusion-weighted imaging phantom data" – *NeuroImage* – Methodological basis for the CSD approach

- **Sotiropoulos & Zalesky (2019)**: "Building connectomes using diffusion MRI: why, how and but" – *Brain Connectivity* – Guidelines for validation and interpretation of connectome data, including critical discussion of tractography biases and connectome construction standard practices

- **Yeh et al. (2019)**: "Quantifying brain microstructure with diffusion MRI: Theory and [[parameter-estimation]]" – *NMR in Biomedicine* – Background on diffusion modeling methods

## Related Software

- [[tvb]] – [[the-virtual-brain]]; primary destination software for connectome matrices
- Mrtrix – Parent software suite containing the connectome pipeline
- Fsl – Used internally for distortion correction (TOPUP, eddy)^2
- Freesurfer – Often used for cortical parcellation input
- Dipy – Alternative diffusion analysis Python library
- [[ants]] – Optional registration tool for atlas alignment

## References

1. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](](https://doi.org/10.1016/j.neuroimage.2018.05.040))
2. Yifei Sun, James M. Shine, Robert D. Sanders, Robin F. H. Cash, Sharon L. Naismith, Fernando Calamante, Jinglei Lv. (2026). *A Data-Driven Method to Map the Functional Organisation of Human Brain White Matter*. [Link](](https://arxiv.org/abs/2602.18715))
3. Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu. *Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic*. [Link](](https://arxiv.org/abs/2603.24176))
4. (authors unknown). *Image Processing and Quality Control for the First 100,000 Brain Imaging Datasets from [[uk-biobank]]*.
5. Ido Haber, Aksel Jackson, A. Thielscher, Aviad Hai, G. Tononi. (2025). *TI-Toolbox: An Open-Source Software for Temporal Interference Stimulation Research*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.10.06.680781))
6. Benjamin S. Sipes, Fahimeh Arab, S. Nagarajan, Ashish Raj. (2026). *HONeD-in on Brain Activity: Deconvolving Passive Diffusion on the Structural Network from Functional Brain Signals*. bioRxiv. [DOI](](https://doi.org/10.64898/2026.01.05.697753))
7. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi-echo [[fmri]] denoising and preprocessing*. Imaging Neuroscience. [DOI](](https://doi.org/10.1162/IMAG.a.1198))
8. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](](https://doi.org/10.52294/001c.154022))