---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/woodman-2014.md
tags:
- software-visualization
- neuroimaging-fmri
- brain-parcellation
- neuroimaging
title: PyCortex
type: entity
updated: '2026-05-11'
---

PyCortex is a Python library specialized in the visualization and manipulation of [[neuroimaging]] data represented on the cortical surface. Originally developed to support work with [[cifti]] file format (a container format for grayordinate data that combines cortical surface vertices with subcortical voxels), PyCortex provides high-quality interactive visualizations of statistical maps, time series, and parcellated data on inflated or flattened cortical meshes. The library is particularly valued in the human [[connectomics]] community for its ability to render group-level statistical results in a spatially interpretable manner, allowing researchers to visualize activation patterns, [[connectivity]] estimates, and derived metrics directly on the cortical sheet.

The motivation for PyCortex arose from the limitations of传统的 volume-based neuroimaging viewers when handling the increasingly common CIFTI format introduced as part of the Human Connectome Project. Volume-based tools such as [[fsl]] or [[freesurfer]] display data in voxel space, which requires resampling cortical data onto a volumetric grid—a process that introduces interpolation artifacts and obscures the topological relationships between adjacent cortical regions. PyCortex instead maintains data in its native surface representation, enabling pixel-precise visualization on highly tessellated meshes (typically ~32,000 vertices per hemisphere) without information loss. This approach is essential for displaying high-resolution resting-state [[functional-connectivity]] patterns, fine-grained [[brain-parcellation]] schemes such as the [[glasser-atlas]], and statistical contrasts derived from task-based [[fmri]] experiments.

Technically, PyCortex operates by loading CIFTI files via [[nibabel]] and mapping their cortical data onto vertex-level surface representations obtained from [[freesurfer]] or [[human-connectome-project]] pipelines. The library exposes a Python API for generating publication-quality figures using a declarative specification format: users define a "overlay" specifying which data to display (e.g., a z-statistic map from a group analysis), a "basemap" providing the anatomical reference mesh, and visual parameters such as colormap, thresholding, and transparency. Renderings can be exported as static SVG or PNG images, or viewed interactively in a web browser through an embedded viewer. PyCortex also supports animation of time series data, enabling visualization of dynamic states in resting-state or task-evoked connectivity patterns.

The relationship between PyCortex and [[the-virtual-brain]] is primarily through the visualization layer. TVB generates simulation outputs—including [[bold-signal]] predictions, [[effective-connectivity]] matrices, and regional time series—that can be mapped onto cortical surfaces for hypothesis exploration and results communication. While TVB's own [[tvb-webui]] provides internal surface visualization capabilities, some researchers prefer to export TVB outputs as CIFTI files and visualize them in PyCortex for its superior handling of multiple parcellation schemes and its integration with the wider HCP ecosystem. Additionally, PyCortex can be used to visualize structural connectivity matrices derived from [[diffusion-imaging]] pipelines (using tools like [[mrtrix3]] or [[dipy]]) as overlay maps on cortical anatomy, providing anatomical context for TVB [[whole-brain-modeling]] exercises.

Among PyCortex's notable features is its support for the "workbench" color scheme conventions established by the Human [[connectome]] Project, ensuring visual consistency with published HCP figures. The library handles both volumetric CIFTI files (containing subcortical voxels) and metric CIFTI files (cortical surface only), applying appropriate rendering strategies for each. It также предоставляет utility functions for mapping between different surface resolutions (e.g., from fsaverage to fsLR tessellations), enabling cross-study comparability. The interactive web viewer built on WebGL allows users to rotate, zoom, and click on regions to inspect underlying data values—a capability particularly useful during exploratory analysis phases of [[whole-brain-modeling]] workflows.

PyCortex complements rather than replaces other visualization ecosystem components. For pure volume-based viewing, [[fsl]] remains the standard; for vertex-level surface exploration, [[pysurfer]] offers similar capabilities but with different design philosophy; for atlas-based region inspection, [[brainspace]] provides advanced dimensionality reduction and clustering visualization. PyCortex excels when working with CIFTI-native data and when publication-quality static figures are required, filling a specific niche in the neuroimaging visualization landscape that aligns well with the input/output expectations of modern large-scale consortium projects like HCP and UK Biobank.

## Related Software

- [[the-virtual-brain]] — Brain simulation engine whose outputs can be visualized via PyCortex
- [[freesurfer]] — Primary source for cortical surface reconstructions used by PyCortex
- [[nibabel]] — Python library for loading CIFTI files that PyCortex depends on
- [[nilearn]] — Statistical learning for neuroimage data, often used alongside PyCortex for preprocessing
- [[human-connectome-project]] — Consortium whose CIFTI format PyCortex was designed to support
- [[connectome-workbench]] — The HCP's official visualization tool for CIFTI data
- [[brain-parcellation]] — [[parcellation]] schemes (e.g., Glasser, [[schaefer]]) that PyCortex can display
- [[glasser-atlas]] — High-resolution multimodal parcellation commonly visualized with PyCortex

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain Connectivity. [DOI](](https://doi.org/10.1089/brain.2012.0120))
3. Woodman et al. (2014). *[[graphvar]]: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))