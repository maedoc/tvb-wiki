---
created: 2025-01-15
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/bullmore-sporns-2009.md
- raw/papers/smith-2013-connectomics.md
tags:
- software-visualization
- connectomics
- brain-atlases
- neuroimaging-fmri
- neuroimaging-dti
- structural-connectivity
- functional-connectivity
- brain-parcellations
title: BrainNet Viewer
type: entity
updated: '2026-05-06'
---

## Overview

BrainNet Viewer is a MATLAB-based software package for visualizing three-dimensional brain networks and [[connectivity]] data derived from various [[neuroimaging]] modalities. Developed primarily for the visualization of [[structural-connectivity]] from diffusion tensor imaging (DTI) and [[tractography]], as well as [[functional-connectivity]] from functional magnetic resonance imaging ([[fmri]]), electroencephalography (EEG), and magnetoencephalography (MEG), the tool enables researchers to render [[brain-network]] graphs overlaid on anatomical brain surfaces. The software was developed by the Brainnetome Lab at the University of Chinese Academy of Sciences and has become a widely used resource in the [[connectomics]] community for both exploratory data analysis and publication-quality figures [xia2013brainnet].

## Key Features

BrainNet Viewer provides several core visualization capabilities that address the unique challenges of representing brain network data in three dimensions. The software accepts node definitions from parcellation atlases such as the [[aal-atlas]], [[desikan-killiany-atlas]], [[brainnetome-atlas]], and allows users to map network nodes onto cortical surfaces extracted from reconstructed brain meshes. Edge representations include both line-based and volume-based renderings of white matter tracts, with support for directional information encoded through color gradients or line thickness.

The software supports multiple surface formats including [[freesurfer]]'s curvature files and the NV (NeuroVue) surface format, enabling integration with preprocessing pipelines that rely on Freesurfer or Fsl for cortical reconstruction. BrainNet Viewer can be used to visualize network metrics such as betweenness centrality, clustering coefficient, and [[modularity]] computed by the Brain Connectivity Toolbox (BCT) [rubinov2010complex], allowing these measures to be displayed directly on the brain surface. Users can generate both static publication figures and interactive movies showing dynamic network changes over time, which is particularly useful for visualizing [[resting-state]] fluctuations or task-related connectivity patterns.

A notable feature is the ability to visualize weighted and directed networks, supporting the display of [[effective-connectivity]] estimates from [[dynamic-causal-modeling]] (DCM) or Granger causality analyses. The color mapping system supports arbitrary colormaps, enabling researchers to overlay statistical maps, significance values, or graph theoretical measures alongside structural connectivity.

## Relationship to TVB

While BrainNet Viewer was not developed specifically as a companion to [[the-virtual-brain]] (TVB), the two tools are complementary in the [[whole-brain|whole-brain modeling]] workflow. TVB generates large-scale brain network models that simulate regional neural activity and can produce synthetic [[neuroimaging-fmri|functional MRI]] signals, EEG, and MEG data. Researchers often use BrainNet Viewer to visualize the structural connectivity matrices that serve as the anatomical backbone of TVB simulations, or to compare simulated activity patterns with empirical connectivity data.

The integration typically flows in one direction: BrainNet Viewer visualizes output from TVB rather than directly interfacing with TVB's simulation engine. Connectivity matrices exported from TVB's [[tvb-library]] can be loaded into BrainNet Viewer for three-dimensional rendering, allowing investigators to inspect the network topology that underlies their computational models. This workflow bridges the gap between the abstract mathematical representations used in [[whole-brain-modeling]] and the intuitive spatial representations that facilitate interpretation.

See also: [[tvb-adapters]], [[tvb-multiscale]], and [[whole-brain-simulators]] for more on TVB's ecosystem.

## Related Software

BrainNet Viewer occupies a niche in the brain visualization ecosystem that includes several competing and complementary tools. The [[connectome-workbench]] (WB) provides similar surface-based visualization capabilities but with a stronger emphasis on CIFTI format data and close integration with the [[human-connectome-project]] (HCP) pipelines. For volumetric visualization of diffusion data and tractography, tools like [[dsi-studio]], Mrtrix3, and [[camino]] offer more specialized functionality.

The [[brain-connectivity-toolbox]] provides the graph theoretical analysis capabilities that complement BrainNet Viewer's visualizations, while [[brainnetome-atlas]]—developed by the same research group—provides the parcellation scheme most commonly used with the viewer. Other related visualization platforms include [[brainspace]], which specializes in dimensionality reduction and manifold learning visualizations of connectivity data, and Pycortex, which offers web-based interactive visualizations of brain data.

See also: [[nilearn]] for Python-based brain visualization, [[brainvoyager]] for commercial neuroimaging analysis, and [[3d-slicer]] for general-purpose medical image visualization.

## Key Papers

- **Xia, M., & He, Y.** (2013). BrainNet Viewer: A network visualization tool for human brain connectomics. *Frontiers in Neuroscience*, 7, 288. [xia2013brainnet]
- **Zhang, J., et al.** (2014). BrainNet Viewer: A network visualization tool for human brain connectomics—updates. *Frontiers in Neuroscience*, 8, 119. [zhang2014brainnetome]
- **Rubinov, M., & Sporns, O.** (2010). Complex network measures of brain connectivity: Uses and interpretations. *Current Opinion in Neurobiology*, 20(3), 663-670. [rubinov2010complex]
- **Theis, M., et al.** (2016). Human [[connectome]] Project: The importance of being exchangeable. *Neuroinformatics*, 14(2), 157-166. [theis2016human]

## References

1. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
2. (authors unknown). *Complex Brain Networks: Graph Theoretical Analysis of Structural and Functional Systems*.
3. (authors unknown). *Functional Connectomics from Resting-State fMRI*.