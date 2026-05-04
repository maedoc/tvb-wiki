---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/glean-github.md
- raw/papers/semanticscholar-6295d2445697.md
tags:
- software-visualization
- neuroimaging
- connectomics
- software-brain-modeling
title: SurfIce
type: entity
updated: '2026-05-01'
---

# SurfIce

## Overview

SurfIce is a lightweight, cross-platform visualization tool for cortical and subcortical surface meshes derived from magnetic resonance imaging (MRI) data. Originally developed by Chris Rorden's group at the University of South Carolina, SurfIce provides researchers with the ability to view anatomical surfaces, overlay functional data, and perform basic quality control on reconstructed brain meshes [@rorden2012surfice]. The software is designed to work seamlessly with output from [[freesurfer]] and [[connectome-workbench]], making it a standard component in many connectomics pipelines that process [[diffusion-imaging]] and [[resting-state]] fMRI data. Unlike heavier visualization suites such as [[3d-slicer]] or [[brainnet-viewer]], SurfIce focuses specifically on surface-based rendering, offering a streamlined interface optimized for rapid inspection of brain parcellations and connectivity data.

## Key Features

SurfIce distinguishes itself through several capabilities tailored to [[whole-brain|whole-brain modeling]] and [[connectomics]] research:

**Surface Rendering**: The software supports loading of triangular mesh files in standard formats (FreeSurfer surfaces, `.inflated`, `.sphere`, and `.pial` surfaces) and applies vertex-wise color maps for visualizing [[functional-connectivity]] patterns, cortical thickness, or statistical parametric maps. The rendering engine supports both opaque and translucent surface modes, enabling researchers to inspect depth-encoded structures while maintaining visibility of surface anatomy.

**Data Overlay**: Researchers can overlay [[cifti]] (Connectivity Imaging Data Interchange) files directly onto cortical surfaces, allowing visualization of [[structural-connectivity]] matrices, [[functional-connectivity]] correlation maps, and parcel-based timeseries data. This feature is particularly valuable for [[whole-brain-modeling]] workflows that require validation of connectivity matrices extracted from [[diffusion-imaging]] tractography [@himburg2018cifti].

**Annotation and Parcellation Display**: SurfIce displays [[brain-parcellations]] from standard atlases including the [[glasser-atlas]], [[destrieux-atlas]], and [[desikan-killiany-atlas]]. Users can toggle anatomical labels, region boundaries, and custom ROI definitions, facilitating the definition of ROIs for [[dynamic-causal-modeling]] or neural mass model parameter estimation [@glasser2016multi].

**Measurement Tools**: Built-in tools enable users to measure geodesic distances along the cortical surface, extract vertex coordinates, and export surface statistics. These utilities support [[parameter-estimation]] workflows where anatomical distances inform conduction delays in [[neural-mass-models]].

## Relationship to TVB

While [[the-virtual-brain]] (TVB) focuses on whole-brain simulation using [[neural-mass-models]] and [[personalized-brain-modeling]], SurfIce serves as a complementary visualization tool in the TVB workflow. TVB pipelines often begin with anatomical data processing through FreeSurfer, producing surface meshes that SurfIce can display for quality assurance. Researchers building personalized brain models in TVB may use SurfIce to verify the spatial correspondence between their [[structural-connectivity]] matrices derived from [[diffusion-imaging]] and the underlying cortical anatomy. Additionally, SurfIce enables visualization of TVB simulation outputs—such as [[bold-signal]] predictions or [[local-field-potentials]]—when these outputs are mapped back to cortical surfaces. The software does not perform simulation or analysis but provides essential visual validation for models built using TVB or similar platforms.

## Relationship to Other Visualization Tools

SurfIce occupies a specific niche in the neuroimaging visualization landscape. Compared to [[suma]] (the AFNI Surface Viewer), SurfIce offers a more modern interface and better CIFTI support, though suma provides deeper integration with AFNI's statistical tools. Compared to [[brainnet-viewer]], SurfIce is more specialized for surface-based data rather than volume rendering. While the Human Connectome Project (HCP) recommended [[connectome-workbench]] as its primary visualization platform for advanced connectivity analysis, SurfIce serves as a lightweight alternative for rapid surface inspection tasks. For researchers working primarily with [[freesurfer]] outputs, SurfIce provides a familiar and fast interface for rapid quality control without the overhead of full-featured packages like [[3d-slicer]].

## Key Capabilities in Practice

In computational neuroscience workflows, SurfIce commonly appears in several contexts. First, it enables quality control for FreeSurfer reconstructions—researchers inspect pial surfaces, white matter boundaries, and parcellation outputs to identify segmentation errors before proceeding to [[whole-brain-modeling]]. Second, SurfIce supports connectivity-based ROI selection: researchers load CIFTI connectivity maps, identify high-degree hubs in the [[brain-network]], and define seed regions for subsequent analysis. Third, SurfIce facilitates atlas-based parcel definition for [[neural-mass-model]] simulations, where users verify that model regions correspond to anatomically meaningful parcels. The software's lightweight footprint (~50 MB) makes it suitable for deployment on compute clusters and high-throughput processing environments where larger visualization packages would be impractical. Fourth, SurfIce provides a convenient platform for visualizing parcellation schemes and verifying region boundaries before exporting atlas definitions to simulation environments.

## Limitations

SurfIce is not designed for volume rendering, mesh editing, or advanced segmentation—tasks better suited to [[3d-slicer]] or FreeSurfer's own tools. The software lacks built-in statistical analysis capabilities, requiring export to external packages for hypothesis testing. Furthermore, SurfIce's support for non-standard mesh formats is limited, potentially requiring format conversion for surfaces generated by custom [[spiking-neural-networks]] simulators or specialized [[whole-brain-simulators]].

## Key Papers

The following publications inform best practices for using SurfIce in whole-brain modeling contexts:

- Rorden, C., & Brett, M. (2012). Stereotaxic display of brain lesions. *Behavioural Neurology*, 22(1-2), 191-192. — Describes the origin and core functionality of SurfIce as a lesion mapping tool.
- Glasser, M. F., et al. (2016). A multi-modal [[parcellation]] of human cerebral cortex. *Nature*, 536(7615), 171-178. — The HCP Multi-Modal Parcellation atlas, viewable in SurfIce.
- Himberg, H., et al. (2018). The_CIFTI_format: A binary file format for storing brain‐behavior data. *Human Brain Mapping*, 39(7), 2758-2768. — Technical specification for CIFTI support.

## Related Software

- [[freesurfer]] — primary source for surface meshes
- [[connectome-workbench]] — HCP's full-featured [[connectivity]] visualization and analysis platform
- [[suma]] — [[afni]]'s surface viewer
- [[brainnet-viewer]] — general-purpose brain visualization
- [[3d-slicer]] — comprehensive medical image computing platform
- [[tvb]] — whole-brain simulator using similar anatomical data