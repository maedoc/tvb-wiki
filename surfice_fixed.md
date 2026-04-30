---
title: SurfIce
created: 2025-01-15
updated: 2026-04-30
type: entity
tags: [software-visualization]
sources:
  - https://www.nitrc.org/projects/surfice/
  - https://github.com/neurolabusc/surf-ice
  - https://doi.org/10.1038/s41592-025-02764-6
---

SurfIce is a specialized surface visualization and rendering software designed for neuroimaging and connectomics research. It provides interactive tools for viewing, manipulating, and analyzing three-dimensional brain surface representations derived from magnetic resonance imaging (MRI) data, including cortical meshes, white matter surfaces, and inflated brain geometries. The software is widely used in the human connectome community for visualizing [[structural-connectivity]] data, [[brain-parcellations]], and functional imaging results overlaid on brain surfaces.

## Overview

SurfIce serves as a lightweight, cross-platform alternative to larger neuroimaging visualization suites while maintaining compatibility with standard file formats used in the field. The software natively supports [[GIFTI]] surface geometry files, [[NIFTI]] volumetric data (both for overlay visualization and as background images), and various atlas-based parcellation schemes. Researchers use SurfIce primarily for inspecting cortical reconstructions from [[FreeSurfer]], visualizing [[connectome]] data mapped onto brain surfaces, and creating publication-quality figures demonstrating brain network topologies (Rorden, 2025).

The software emerged from the need for a dedicated surface viewer that could handle the high-resolution meshes produced by modern segmentation pipelines. Unlike volumetric visualization tools that operate on three-dimensional image stacks, SurfIce is optimized for triangular mesh representations of the cortical sheet, enabling smooth rendering of inflated hemispheres and flattened cortical patches commonly used in [[resting-state]] functional connectivity studies.

## Key Features

SurfIce provides several capabilities essential for whole-brain modeling and connectomics workflows. The software supports multiple surface representations simultaneously, allowing researchers to toggle between raw cortical reconstructions, smoothed meshes, and inflated anatomies within a single session. This flexibility is particularly valuable when comparing [[structural-connectivity]] pathways derived from [[diffusion-imaging]] with functional networks estimated from [[fMRI]] data.

The software includes built-in support for applying colormaps and scalar overlays to surfaces, enabling visualization of [[functional-connectivity]] matrices, [[structural-core]] regions, or any vertex-wise metric computed in downstream analysis. Researchers can customize color scales, set transparency levels for overlapping surfaces, and export rendering snapshots for inclusion in manuscripts or presentations.

Surface-based operations in SurfIce include resampling between different mesh resolutions, computing sulcal depth maps, and generating curvature estimates from vertex positions. These operations support the parcellation-based analysis approaches common in modern [[whole-brain-modeling]], where brain regions are defined anatomically and their interactions modeled using [[neural-mass-models]] or [[dynamic-causal-modeling]] frameworks.

The software also supports visualization of tractography streamlines and connectome networks. It can load fiber tracking data in formats used by TrackVis (TRK), MRTrix (TCK), and other diffusion imaging tools, allowing researchers to visualize white matter pathways alongside cortical surfaces (Rorden, 2025).

## Relationship to TVB

SurfIce complements [[The Virtual Brain]] (TVB) by providing visualization capabilities for the cortical surfaces and connectivity matrices that form the anatomical basis of TVB simulations. In TVB workflows, researchers first derive [[structural-connectivity]] from [[diffusion-imaging]] data using tools like [[MRtrix3]] or [[DSI Studio]], then generate cortical surfaces using FreeSurfer. The resulting surfaces can be inspected and validated in SurfIce before importing into TVB for simulation.

TVB's simulation engine operates on a nodes-and-edges representation where brain regions correspond to cortical parcels, and SurfIce provides a natural way to visualize which parcels are included in a given model. Researchers working on [[personalized-brain-modeling]] applications often use SurfIce to compare individual subject parcellations against standard atlases like [[Desikan-Killiany atlas]] or [[Schaefer atlas]], ensuring that TVB simulations accurately represent the intended anatomical decomposition.

## Relationship to Other Visualization Tools

SurfIce occupies a niche in the neuroimaging visualization ecosystem alongside tools like [[Connectome Workbench]] (wb_view), [[BrainNet Viewer]], and the integrated viewers in [[FreeView]] (FreeSurfer's viewer) and [[3D Slicer]]. While Connectome Workbench offers more extensive capabilities for handling CIFTI files and large dataset collections, SurfIce provides a simpler interface for common surface viewing tasks. The software is particularly well-suited for quick inspection workflows and for creating simple visualizations without the overhead of larger packages.

Unlike volumetric-only viewers such as [[ITK-SNAP]] or [[fsleyes]], SurfIce's surface-centric design makes it particularly appropriate for connectomics applications where the topological relationships between cortical regions are central to the analysis. The software's lightweight footprint also makes it accessible for researchers working on computational resources with limited graphical capabilities. Unlike these heavier alternatives, SurfIce runs efficiently on older hardware by offering both a modern OpenGL 3.3 version and a legacy OpenGL 2.1 version for compatibility with older graphics cards.

## Related Software

- [[Connectome Workbench]] — comprehensive neuroimaging visualization suite
- [[FreeSurfer]] — cortical reconstruction and segmentation
- [[BrainNet Viewer]] — network visualization on brain surfaces
- [[nilearn]] — Python library for neuroimaging data visualization
- [[3D Slicer]] — general-purpose medical image computing platform

## Key Papers

- Rorden, C. (2025). Surfice: visualizing neuroimaging meshes, tractography streamlines and connectomes. *Nature Methods*, 22, 1615-1616. https://doi.org/10.1038/s41592-025-02764-6

## References

1. Rorden, C. (2025). Surfice: visualizing neuroimaging meshes, tractography streamlines and connectomes. *Nature Methods*, 22, 1615-1616. https://doi.org/10.1038/s41592-025-02764-6

2. Marcus, D. S. et al. (2011). Informatics and data science: The Human Connectome Project. *Frontiers in Neuroinformatics*, 5, 4.

3. Tournier, J.-D. et al. (2019). MRtrix3: A fast, flexible and robust pipeline for neuroimage processing. *Neuroimage*, 202, 116137.

4. Saad, Z. S. et al. (2004). SUMA: An interactive tool for neuroanatomy. In *2004 2nd IEEE International Symposium on Biomedical Imaging: Nano to Macro* (Vol. 2, pp. 1510-1513). IEEE.

5. Dale, A. M., Fischl, B., & Sereno, M. I. (1999). Cortical surface-based analysis. I. Segmentation and surface reconstruction. *Neuroimage*, 9(2), 179-194.

6. Sherif, T. et al. (2015). CBRAIN: a web-based, distributed computing platform for collaborative neuroimage research. *Frontiers in Neuroinformatics*, 8, 89.