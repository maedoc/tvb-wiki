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
updated: '2026-05-18'
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
MRtrix3 provides a comprehensive command-line environment for [[diffusion-imaging]] analysis, with its processing pipeline spanning from raw data preprocessing through [[connectome]] construction. In clinical neuroimaging studies, researchers employ MRtrix3 specifically for diffusion-based [[tractography]] and subsequent connectome reconstructions. For instance, in a study of Parkinson's disease patients with freezing of gait, investigators acquired diffusion-weighted MRI and used MRtrix3 for structural connectivity analysis alongside resting-state fMRI processed with the CONN toolbox, revealing alterations in limbic, putaminal, parietal, and cerebellar connectivity patterns [[raw/papers/semanticscholar-a6b8919e7fe8.md|Lê et al. (2026)]]. The diffusion MRI analysis workflow generally encompasses sequential stages including preprocessing operations such as denoising and registration, local fiber reconstruction from diffusion data, tractography generation, and post-processing of tractograms including connectivity and bundle analyses [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]. Within the broader neuroimaging software ecosystem, graph-theoretical analysis platforms such as BRAPH complement tractography tools by providing standardized pipelines for constructing and analyzing brain networks from connectivity data [[raw/papers/mijalkov-2017-braph.md|Mijalkov et al. (2017)]].
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

1. Quynh Lê, Arichena Manmatharayan, Mashaal Syed, Ki-Sang Kang, Tsao‐Wei Liang, Mahdi Alizadeh, Chengyuan Wu. (2026). *Structural and [[functional-connectivity]] in Parkinson's Disease Patients With Freezing of Gait and Other Gait Disturbances*. Clinical [[neuroimaging]]. [DOI](https://doi.org/10.1002/neo2.70042)
2. Emmanuelle Renauld, Arnaud Boré, Charles Poirier, Alex Valcourt-Caron, Philippe Karan, Antoine Théberge, Guillaume Théaud, Manon Edde, P. Poulin, Gabriel Girard, Jean-Christophe Houde, A. Gagnon, Etienne St-Onge, Graham Little, Jon Haitz Legarreta, Stanislas Thoumyre, G. Grenier, Zineb El Yamani, Mario Ocampo Pineda, Matteo Battochio, Vincent Beaudoin, Alexandre Joanisse, Laurent Petit, F. Rheault, Maxime Descoteaux. (2026). *Tractography analysis with the scilpy toolbox*. Aperture Neuro. [DOI](https://doi.org/10.52294/001c.154022)
3. (authors unknown). *[[braph]]: A Pipeline for Brain Connectivity Analysis*.