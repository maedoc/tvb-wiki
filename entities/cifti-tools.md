---
created: 2025-01-15
sources:
- GlasserEtAl2013
- MarcusEtAl2011
- nibabel-docs
- raw/papers/doi-10-3389-fninf-2011-00004.md
tags:
- software-neuroimaging
- neuroimaging-fmri
- data-format
- human-connectome-project
- software-visualization
- software-dti-tk
title: CIFTI Tools
type: entity
updated: '2026-05-05'
---

CIFTI (Connectivity InFormatics Initiative) tools encompass a family of software utilities designed to work with the CIFTI data format, a specialized file format developed by the Human Connectome Project (HCP) for storing dense connectivity data from neuroimaging studies [@GlasserEtAl2013]. The format addresses fundamental limitations of older neuroimaging formats by enabling representation of both surface-based (cortical) and volumetric (subcortical) data within a single file, making it particularly well-suited for whole-brain connectivity analyses central to [[whole-brain-modeling]] approaches.

## Motivation and Context

Traditional neuroimaging formats such as NIfTI were originally designed for volumetric data but struggled with the complexity of modern multi-modal connectivity datasets. When researchers began combining [[fMRI]] connectivity matrices with [[structural-connectivity]] estimates from diffusion imaging, the mismatch between surface-based cortical representations and volumetric subcortical structures created significant file management challenges. The HCP addressed this by developing CIFTI as a unified format capable of representing brain-wide connectivity data in a single file while maintaining compatibility with established neuroimaging frameworks [@MarcusEtAl2011]. This development proved particularly valuable for [[the-virtual-brain]] workflows that typically combine multiple neuroimaging modalities to construct personalized [[connectome]]-based models.

## Key Features

The CIFTI format supports several critical features for connectivity analysis. **Grayordinate representation** combines cortical gray matter surfaces (represented as vertices) with subcortical volumes (voxels) into a unified coordinate system, eliminating the need for separate file handling [@GlasserEtAl2013]. **Dense connectivity** storage enables storage of complete connectivity matrices between all grayordinates rather than just parcel-based summaries, preserving the full information content of [[resting-state]] fMRI analyses. The format specification also supports time series data, allowing storage of complete BOLD-signal time courses alongside connectivity matrices. CIFTI files use extensions `.dtseries.nii` for time series and `.dscalar.nii` for scalar data, both built on the NIfTI-2 header structure for improved metadata handling.

## Primary Software Tools

**Connectome Workbench** serves as the primary visualization and analysis environment for CIFTI data. Developed by the HCP, workbench provides graphical interfaces for viewing surface-based data, creating brain figures, and performing basic connectivity analyses. The command-line utilities (`wb_command`) enable batch processing and scripted workflows essential for reproducible research pipelines. Workbench integrates closely with HCP pipelines but functions independently for general CIFTI manipulation.

**ciftify** provides a Python-based framework for CIFTI data processing within the [[nipype]] ecosystem. The package offers routines for converting between CIFTI and other formats, surface projection utilities, and integration with [[fmriprep]] outputs. ciftify workflows are commonly used when preparing HCP-style data for [[personalized-brain-modeling]] pipelines that require CIFTI-formatted time series inputs.

**nibabel** provides programmatic Python access to CIFTI files through its `cifti2` module, enabling custom analysis scripts to read and write CIFTI data without external dependencies [@nibabel-docs]. This low-level access is essential for developers building custom connectivity pipelines.

## Key Papers

- Glasser, M. F., et al. (2013). The minimal preprocessing pipelines for the Human Connectome Project. *NeuroImage*, 80, 105-124. [[https://doi.org/10.1016/j.neuroimage.2013.04.127]]
- Marcus, D., et al. (2011). Informatics and data mining tools and strategies for the Human Connectome Project. *Frontiers in Neuroinformatics*, 5, 4. [[https://doi.org/10.3389/fninf.2011.00004]]

## Relationship to TVB

The Virtual Brain integrates with CIFTI tools primarily through its connectivity pipeline. TVB accepts [[structural-connectivity]] matrices derived from diffusion imaging data, which may be stored in CIFTI-compatible formats when originating from HCP-derived datasets. The TVB library includes adapters for reading neuroimaging data, and while TVB's native format uses custom XML/CSV structures, users frequently convert CIFTI connectivity outputs to TVB-compatible matrices using workbench's `wb_command -cifti-math` utilities. The relationship remains indirect—TVB consumes the processed connectivity matrices rather than CIFTI files directly—but CIFTI-derived structural and functional connectomes provide valuable inputs for [[personalized-brain-modeling]] applications. Researchers working with [[hcp-dataset]] or [[uk-biobank]] imaging data often employ CIFTI tools as part of the preprocessing pipeline before TVB model construction.

## Related Software

- [[TVB]] — The Virtual Brain
- [[cifti]] — CIFTI format specification
- [[connectome-workbench]] — Primary visualization environment
- [[nipype]] — Python workflow framework used by ciftify

## References

1. (authors unknown). *Informatics and Data Mining Tools and Strategies for the Human Connectome Project*.