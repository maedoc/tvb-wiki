---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-a6b8919e7fe8.md
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-mrtrix
- neuroimaging-dti
- tractography
- image-processing
title: MRtrix3
type: entity
updated: '2026-05-06'
---

# MRtrix3

**MRtrix3** is an open-source software suite for [[diffusion-mri]] analysis, with particular emphasis on [[tractography]] and [[connectome]] construction. It provides a comprehensive set of tools for processing, analyzing, and visualizing diffusion-weighted imaging data.

## Overview

MRtrix3 provides:
- Advanced diffusion model fitting (CSD, multi-shell multi-tissue CSD)
- Robust tractography algorithms (iFOD1, iFOD2, FACT, deterministic)
- Connectome construction from tractography and [[parcellation]]
- Fixel-based analysis for population studies
- Advanced visualization with OpenGL-based tract rendering
- Scripting interfaces for reproducible pipelines

## Key Commands

| Command | Purpose |
|---------|---------|
| **dwidenoise** | MP-PCA denoising of DWI data |
| **mrdegibbs** | Gibbs ringing removal |
| **dwipreproc** | Preprocessing (motion/distortion correction) |
| **dwi2response** | Response function estimation |
| **dwi2fod** | Fiber orientation distribution estimation |
| **tckgen** | Tractography generation |
| **tck2connectome** | Connectome matrix generation |
| **SIFT/SIFT2** | Streamline filtering by density matching |

## Relationship to TVB

MRtrix3 is a premier tool for TVB [[connectivity]] preparation:
- **Multi-tissue CSD** and **SIFT2** provide biologically plausible streamline densities for connectivity weights
- **Connectome construction** (tck2connectome) directly outputs matrices usable by TVB
- **Parcellation integration** with FreeSurfer, AAL, and custom atlases
- The [[structural-connectivity]] pipeline in many TVB workflows uses MRtrix3 for tractography
- MRtrix3's robust crossing-fiber handling improves connectivity accuracy in regions like the centrum semiovale

## Software Ecosystem

- [[fsl]] — FSL's PROBTRACKX is a widely used alternative
- [[dipy]] — Python-based alternative with complementary algorithms
- [[freesurfer]] — parcellation input for MRtrix3 connectomes
- [[tvb]] — uses MRtrix3 connectomes for [[whole-brain]] simulation

## References

- MRtrix3 website: https://www.mrtrix.org/
- Tournier et al. (2019) — MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation
- Smith et al. (2012) — Anatomically-constrained tractography
- [[sift]]: Smith et al. (2013) — SIFT: Spherical-deconvolution informed filtering of tractograms