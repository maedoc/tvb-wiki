---
created: 2026-04-29
sources:
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/woodman-2014.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-r
- neuroimaging
- cifti
- human-connectome-project
- grayordinates
- fmri
- brain-atlases
title: CITItools
type: entity
updated: '2026-04-30'
---

CITItools (ciftiTools) is an R package for reading, writing, visualizing, and manipulating CIFTI ([[connectivity]] Informatics Technology Initiative) format files in [[neuroimaging]] workflows. The package provides a unified environment for working with grayordinate-based brain imaging data, combining cortical surface vertices with subcortical voxel data in a single file format pioneered by the [[human-connectome-project]]. Originally developed by Amanda Mejia, Damon Pham, and John Muschelli, ciftiTools is available on CRAN and has become a standard tool for R-based neuroimaging analysis pipelines [1][2].

## Technical Background

CIFTI files store brain imaging data in "grayordinates" — a hybrid representation that combines the cortical surface (approximately 32,000 vertices per hemisphere) with volumetric subcortical structures including the cerebellum and basal ganglia. This format was introduced by the [[human-connectome-project]] to address limitations of purely volumetric or purely surface-based neuroimaging data representations. The [[cifti]] format supports three primary intents: "dtseries" for time-series data (such as [[fmri]]), "dscalar" for continuously-valued scalar data, and "dlabel" for categorical parcellations and labels [3].

The ciftiTools package introduces the "xifti" object class, which encapsulates both the data matrix and associated metadata including surface geometry, medial wall masks, and subcortical structure labels. This design enables convenient access to neuroimaging data while maintaining compatibility with the underlying CIFTI specification.

## Key Features

The package provides comprehensive functionality across several domains. For data I/O, ciftiTools supports reading and writing CIFTI files with `read_cifti` and `write_cifti` functions, alongside conversion between GIFTI surface files and [[nifti]] volumetric formats. Visualization capabilities include `view_xifti_surface` for interactive 3D cortical rendering using the rgl package, and `view_xifti_volume` for subcortical volume visualization on MNI templates.

Processing operations include geodesic surface smoothing and resampling to different mesh resolutions (e.g., 10k, 32k vertices per hemisphere), implemented via the [[connectome-workbench]] command-line tools. The package also includes mathematical operations implemented as S3 methods, allowing direct arithmetic and transformation of xifti objects within R.

For [[parcellation]] workflows, ciftiTools provides built-in support for the Schaefer parcellation (100–1000 parcels) and Yeo functional networks (7 and 17 networks), facilitating region-of-interest analyses common in [[connectome]] studies.

## Relationship to TVB and Other Tools

ciftiTools serves a complementary role in the [[tvb]] ecosystem by enabling preprocessing and analysis of HCP-style datasets that may be used as empirical priors or validation targets for [[whole-brain]] simulations. Researchers can use ciftiTools to extract connectivity matrices from empirical CIFTI data, which can then serve as structural connectome inputs for TVB simulations. Conversely, simulated [[bold-signal|BOLD]] signals from TVB can be visualized and compared with empirical data using ciftiTools.

The package integrates with the broader neuroimaging ecosystem: it depends on [[connectome-workbench]] for computationally intensive operations, uses [[gift]] format for surface geometry, and complements Python tools such as [[nilearn]] and [[pycortex]]. Unlike the cifti R package which supports all CIFTI intents but offers limited functionality, ciftiTools provides a user-friendly interface specifically optimized for dscalar, dtseries, and dlabel intents common in fMRI analysis.

## Key Packages Summary

| Package | Language | Read CIFTI | Write CIFTI | Visualize | External Dependency |
|---------|----------|------------|-------------|-----------|---------------------|
| ciftiTools | R | ✓ | ✓ | ✓ | Connectome Workbench |
| nilearn | Python | ✗ | ✗ | ✓ | NiBabel |
| cifti-matlab | MATLAB | ✓ | ✓ | ✗ | None |
| hcp-utils | Python | ✓ | ✗ | ✓ | nilearn, NiBabel |

## Key Papers

1. Pham, D. D., Muschelli, J., & Mejia, A. F. (2022). ciftiTools: A package for reading, writing, visualizing, and manipulating CIFTI files in R. NeuroImage, 250, 118877.

## References

1. R. A. Benn, Ting Xu, R. Mars, Magdalena Boch, Léa Roumazeilles, K. Heuer, Roberto Toro, D. Margulies, J. Manzano-Patrón, Paula Montesinos, C. Galán-Arriola, G. López-Martín, J. Sanchez-González, E. P. Duff, Borja Ibáñez. (2025). *Precon_all: A species-agnostic automated pipeline for non-human cortical surface reconstruction*. bioRxiv. [DOI](https://doi.org/10.1101/2025.04.16.649072)
2. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)
3. (authors unknown). *BRAPH: A Pipeline for Brain Connectivity Analysis*.