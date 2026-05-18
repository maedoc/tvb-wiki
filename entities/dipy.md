---
created: 2026-05-06
sources:
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/huntenburg-2018.md
- raw/papers/semanticscholar-0aeca1b592e6.md
tags:
- software-dipy
- neuroimaging-dti
- tractography
- python
- image-processing
title: Dipy
type: entity
updated: '2026-05-18'
---

# Dipy

**Dipy** ([[diffusion-imaging]] in Python) is an open-source Python library for the analysis of [[diffusion-mri]] data. It provides tools for preprocessing, reconstruction, [[tractography]], and statistical analysis of diffusion-weighted imaging (DWI).

## Overview
DIPY is an open-source Python library for [[diffusion-mri]] analysis that serves as a computational foundation for the neuroimaging software ecosystem. [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]] describe how downstream toolboxes such as scilpy leverage DIPY's strengths to implement dMRI processing workflows spanning preprocessing operations such as denoising, registration, and local fiber reconstruction. [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]] These early pipeline stages transform raw diffusion-weighted acquisitions in preparation for subsequent tracking and connectivity analyses. [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]

The pipeline extends from these initial stages to [[tractography]] generation and post-processing of tractograms, including connectivity and bundle analyses. [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]] These capabilities allow researchers to move from reconstructed diffusion data to tractogram representations that support assessments of structural connectivity and white-matter bundle organization. [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]] By spanning preprocessing through post-processing, DIPY-based workflows enable the comprehensive analysis of brain fiber architectures from raw acquisitions to connectivity assessments. [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]
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

Dipy is a critical preprocessing tool for TVB [[connectome]] construction:
- **Fiber tracking** (tractography) generates the [[structural-connectivity]] matrix used in TVB simulations
- **FOD reconstruction** (CSD) improves fiber crossing detection, yielding more accurate [[connectivity]]
- **Denoising** and **correction** improve the quality of DWI data before tractography
- Dipy-generated tractograms can be parcellated using [[freesurfer]] or AAL atlases for TVB input
- Dipy integrates with [[nibabel]] for [[neuroimaging]] I/O and with [[tvb]] via Python scripting

## Software Ecosystem

- [[mrtrix3]] — alternative tractography suite with complementary algorithms
- [[fsl]] — FSL's BEDPOSTX/PROBTRACKX is an alternative DTI pipeline
- [[nibabel]] — Dipy depends on nibabel for [[nifti]]/[[cifti]] handling
- [[tvb]] — imports Dipy-generated connectivity matrices

## References

1. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)
2. (authors unknown). *Nighres: processing tools for high-resolution neuroimaging*.
3. Mohammadtaha Parsayan, S. Andalib, T. L. Andersen, Habib Ganjgahi, P. Høilund-Carlsen, Abass Alavi, Mojtaba Zarei. (2025). *Odense-Oxford PET Image Analysis (OPETIA): An FSL-based toolbox for multimodal neuroimaging*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2025.121278)