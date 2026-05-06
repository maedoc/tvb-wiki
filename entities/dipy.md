---
title: "Dipy"
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [software-dipy, neuroimaging-dti, tractography, python, image-processing]
sources: []
---

# Dipy

**Dipy** (Diffusion Imaging in Python) is an open-source Python library for the analysis of diffusion MRI data. It provides tools for preprocessing, reconstruction, tractography, and statistical analysis of diffusion-weighted imaging (DWI).

## Overview

Dipy provides:
- DWI preprocessing (denoising, motion correction, eddy current correction)
- Diffusion tensor imaging (DTI) and multi-compartment model fitting
- Constrained spherical deconvolution (CSD) for fiber orientation distribution (FOD)
- Deterministic and probabilistic tractography algorithms
- Diffusion MRI registration and resampling
- Interactive visualization of fiber tracts and ODFs

## Key Capabilities

| Feature | Description |
|---------|-------------|
| **Denoising** | Non-local means and local PCA for noise suppression |
| **Model Fitting** | DTI, DKI, CSD, NODDI, and other multi-compartment models |
| **Tractography** | EuDX, deterministic, probabilistic, and particle filtering tracking |
| **FOD Reconstruction** | Constrained spherical deconvolution for crossing fibers |
| **Registration** | Affine and non-linear registration of diffusion data |
| **Visualization** | Interactive tract and ODF visualization with Fury |

## Relationship to TVB

Dipy is a critical preprocessing tool for TVB connectome construction:
- **Fiber tracking** (tractography) generates the structural connectivity matrix used in TVB simulations
- **FOD reconstruction** (CSD) improves fiber crossing detection, yielding more accurate connectivity
- **Denoising** and **correction** improve the quality of DWI data before tractography
- Dipy-generated tractograms can be parcellated using FreeSurfer or AAL atlases for TVB input
- Dipy integrates with [[nibabel]] for neuroimaging I/O and with [[tvb]] via Python scripting

## Software Ecosystem

- [[mrtrix3]] — alternative tractography suite with complementary algorithms
- [[fsl]] — FSL's BEDPOSTX/PROBTRACKX is an alternative DTI pipeline
- [[nibabel]] — Dipy depends on nibabel for NIfTI/CIFTI handling
- [[tvb]] — imports Dipy-generated connectivity matrices

## References

- Dipy website: https://dipy.org/
- Garyfallidis et al. (2014) — Dipy: a library for the analysis of diffusion MRI data
- Garyfallidis et al. (2012) — QuickBundles: a method for tractography simplification
