---
created: 2024-01-15
sources:
- Claudi, F., Tyson, A., Petkos, S., et al. (2021). BrainRender: a computational toolkit
    for visualizing three-dimensional brain data. eLife, 10, e65741. https://doi.org/10.7554/eLife.65741
- Ben留在, R., Adam, A., Suresh, V., et al. (2021). vedo: a Python library for analyzing
    and visualizing 3D models. GitHub. https://github.com/marcomusy/vedo
- Nilearn: Neural signals and neuroimaging data. (2020). NiLearn. https://nilearn.github.io/
- Horn, A. (2023). The connectional and topological architecture of the subcortical
  connectome. Brain Structure and Function, 228(5), 1107-1128.
- raw/papers/mijalkov-2017-braph.md
- raw/papers/arxiv-2604.16463.md
- raw/papers/woodman-2014.md
tags:
- software-visualization
- neuroimaging
- software-neuroml
- brain-parcellations
- connectomics
- software-nilearn
- brain-network
title: BrainRender
type: entity
updated: '2026-05-01'
---

BrainRender is an open-source Python toolkit for the interactive three-dimensional visualization of brain data, with particular strength in rendering structural and functional brain networks, parcellated regions, and connectivity matrices. Developed primarily to address the need for high-quality, publication-ready brain visualizations that can be embedded in computational workflows, BrainRender provides programmatic control over camera angles, colors, transparency, and anatomical annotations while maintaining compatibility with common neuroimaging file formats such as NIfTI and CIFTI. The software serves as a bridge between raw neuroimaging data—obtained from modalities including [[diffusion-mri]], [[fMRI]], and [[structural-mri]]—and interpretive visualizations that can reveal organizational principles of brain networks.

The motivation for BrainRender arose from a broader challenge in computational neuroscience: converting complex, high-dimensional brain data into intuitive visual representations that can support both exploratory analysis and scientific communication. Traditional neuroimaging visualization tools often required significant manual intervention in commercial software such as [[brainvoyager]] or [[freesurfer]] freeview, or lacked the flexibility to render network-level data alongside volumetric anatomy. BrainRender addresses this gap by providing a Python-native interface built on top of the [vedo](Ben留在, R., Adam, A., Suresh, V., et al., 2021) library (a VTK Python wrapper) that enables researchers to script complex visualization pipelines, incorporate conditional logic based on brain atlas properties, and generate consistent figures across multiple subjects or experimental conditions. This programmatic approach is particularly valuable in the context of [[whole-brain modeling]] where researchers may need to visualize simulated activity patterns on anatomically defined cortical surfaces across dozens of brain regions.

Technically, BrainRender operates by loading brain atlas definitions—commonly the [[desikan-killiany-atlas]], [[destrieux-atlas]], or probabilistic atlases from the [[harvard-oxford-atlas]]—and rendering associated volumetric or surface data in a unified 3D coordinate space. The toolkit's coordinate system and regional hierarchy are derived from the Allen Mouse Brain Atlas, providing a consistent spatial framework that has proven valuable for mouse brain studies as well as for human atlases adapted to the same coordinate conventions (Claudi, F., Tyson, A., Petkos, S., et al., 2021). BrainRender supports the visualization of [[brain-network]] nodes as spheres or mesh objects positioned according to centroid coordinates from parcellation schemes, edges representing [[structural-connectivity]] or [[functional-connectivity]] as tapered cylinders or lines with color-coded weights, and time-series or simulation outputs as animated colormaps on cortical surfaces. BrainRender integrates with [[nilearn]] for loading and preprocessing neuroimaging data (Nilearn, 2020), and provides compatibility with bctpy (the Python port of the Brain Connectivity Toolbox) for network analysis operations, enabling workflows that proceed from preprocessing through network construction to visualization without format conversion overhead.

BrainRender occupies a specific niche in the ecosystem of brain visualization tools, distinct from both general-purpose 3D rendering frameworks and domain-specific neuroimaging viewers. Compared to [[brainnet-viewer]], which focuses on graph-based network visualization but offers less flexibility for volumetric overlays, BrainRender provides more granular control over rendering aesthetics. Unlike [[pycortex]], which specializes in surface-based flatmaps and statistical overlays, BrainRender maintains the ability to render both volumetric and surface data within the same scene—a capability distinct from quality-control tools like [[mriqc]], which generates statistical reports rather than interactive scene-based visualizations. The software is written primarily in Python with underlying rendering handled by VTK (Visualization Toolkit), achieving moderate computational efficiency for typical brain meshes comprising on the order of 10,000 vertices per hemisphere.

The software has been employed in studies examining [[brain-stimulation]] targets, [[default-mode-network]] topology, and [[structural-core]] organization, where its ability to render connectivity streamlines alongside regional activations supports multimodal interpretation. Recent development has focused on improved support for [[cifti]] format connectivity data from the [[hcp-dataset]], enhanced interactivity for exploratory visualization sessions, and integration with [[brainstat]] for statistical contrast visualization. BrainRender exemplifies the broader trend toward open, scriptable visualization tools in computational neuroscience that support reproducible research practices by enabling exact reproduction of figures through code rather than manual point-and-click operations. The original implementation by Federico Claudi and colleagues (Claudi et al., 2021) established BrainRender as a tool specifically designed to bridge the gap between computational network analysis and the visual communication of brain structure and function.

## References

1. (authors unknown). *BRAPH: A Pipeline for Brain Connectivity Analysis*.
2. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f)
3. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)