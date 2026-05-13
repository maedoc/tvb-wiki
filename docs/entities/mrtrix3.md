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
updated: '2026-05-13'
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

The MRtrix3 command suite implements a comprehensive diffusion MRI pipeline that moves from raw data preprocessing to [[whole-brain]] connectome construction. Preprocessing stages such as denoising and motion correction clean diffusion-weighted imaging data before local fiber reconstruction, ensuring that downstream analyses operate on high-quality signals [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]. Commands including dwidenoise suppress thermal noise in DWI volumes, mrdegibbs removes Gibbs ringing artifacts, and dwipreproc corrects motion and eddy-current distortions. The dwi2response command calibrates the tissue response function, while dwi2fod estimates the fiber orientation distributions that drive subsequent [[tractography]] algorithms [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]. These preprocessing and reconstruction stages produce the crossing-fiber representations required for accurate structural connectivity mapping [[raw/papers/semanticscholar-a6b8919e7fe8.md|Lê et al. (2026)]].

For [[structural-connectivity]] analysis, MRtrix3 performs diffusion-based tractography and subsequent connectome reconstructions that transform streamlines into weighted connectivity matrices [[raw/papers/semanticscholar-a6b8919e7fe8.md|Lê et al. (2026)]]. The tckgen command generates streamlines through probabilistic [[tractography]], while tck2connectome maps these tractograms onto a [[parcellation]] to produce the [[connectome]] matrices used in network simulations. Post-processing with [[sift]] and SIFT2 refines streamline density to match underlying fiber distributions, yielding connectivity weights that integrate into brain network analysis pipelines [[raw/papers/semanticscholar-380768cf42a8.md|Renauld et al. (2026)]]. These MRtrix3 outputs feed directly into downstream graph-theoretic analysis of structural brain networks [[raw/papers/mijalkov-2017-braph.md|Mijalkov et al. (2017)]], forming a critical bridge between [[diffusion-mri]] and computational [[connectomics]].

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