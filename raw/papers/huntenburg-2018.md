---
title: "Nighres: processing tools for high-resolution neuroimaging"
created: 2026-04-30
updated: 2026-04-30
type: paper
authors: ["Judith M. Huntenburg", "Christopher J. Steele", "Pierre-Louis Bazin"]
year: 2018
venue: "GigaScience"
doi: "10.1093/gigascience/giy082"
tags: [software-visualization, neuroimaging, laminar-analysis, cortical-analysis, brain-segmentation, paper-methods]
sources: []
---

# Nighres: processing tools for high-resolution neuroimaging

**Authors:** Judith M. Huntenburg, Christopher J. Steele, Pierre-Louis Bazin  
**Year:** 2018  
**Venue:** GigaScience

## Key Contributions

- Released Nighres as an open-source Python package for high-resolution neuroimaging processing
- Made CBS High-Res Brain Processing Tools accessible through a documented Python interface
- Included functions from the IMCN imaging toolkit
- Provided tools for laminar analysis including volumetric layering and cortical depth estimation

## Abstract Summary

Nighres is a Python package for processing high-resolution neuroimaging data, developed out of the CBS High-Res Brain Processing Tools. The package provides functions for brain extraction, segmentation, cortex reconstruction, and laminar analysis of high-resolution MRI data. It aims to make these tools easier to install, use and extend for the neuroimaging community. The package includes modules for brain processing, cortex extraction, laminar analysis, filtering, intensity mapping, and surface visualization.

## Key Algorithms

### MGDM Segmentation
Multi-Atlas Multi-Cloud Decomposition with Markov Random Fields for robust tissue classification including gray matter, white matter, and CSF probabilities.

### CRUISE Cortex Extraction
Cortical Reconstruction Using Implicit Surface Evolution for topologically correct cortical surface extraction from segmented data.

### Volumetric Layering
Equivolumetric layering of cortical sheet based on Waehnert et al. (2014), computing continuous depth estimates from inner to outer cortical surface.

## Relationship to Other Tools

Nighres complements standard neuroimaging processing pipelines like FreeSurfer, FSL, and ANTs by providing specialized tools for high-resolution data analysis. It integrates with nilearn for visualization and nibabel for NIfTI handling.