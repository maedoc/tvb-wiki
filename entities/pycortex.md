---
created: 2026-04-20
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
tags:
- software-visualization
- neuroimaging-fmri
- connectomics
- functional-connectivity
- structural-connectivity
- whole-brain-modeling
title: PyCortex
type: entity
updated: '2026-05-18'
---

PyCortex is a Python library for the visualization and manipulation of cortical surface data in human [[neuroimaging]]. It renders statistical maps, time series, and parcellated results directly on inflated or flattened cortical meshes, emphasizing vertex-level spatial precision over volume-based resampling. The library is designed for researchers who require pixel-accurate, publication-quality surface figures that retain the topological geometry of the cortical sheet.

## Motivation and Context

The Virtual Brain ([[the-virtual-brain]]) provides an open-source platform for simulating large-scale primate brain network dynamics by combining empirical structural connectivity with neural mass models [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. It supports forward models for EEG, MEG, and fMRI, enabling simulated signals to be compared directly against empirical recordings [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. The platform bridges computational modeling and multimodal neuroimaging by coupling subject-specific structural connectivity matrices with personalized brain models capable of reproducing individual resting-state [[functional-connectivity]] patterns [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. These simulation outputs—regional time series, [[bold-signal]] predictions, and [[effective-connectivity]] estimates—derive neuroscientific meaning only when mapped onto anatomical surfaces that define cortical topology [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. Conventional volume-based viewers resample surface signals onto a three-dimensional voxel grid, which can obscure the spatial relationships between adjacent gyral regions. Tools that preserve the native two-dimensional manifold of the cortical sheet allow model predictions to be inspected in the anatomical geometry that constrains emergent [[network-dynamics]] [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Relationship to TVB

TVB integrates computational modeling and multimodal neuroimaging by translating clinical neuroimaging data into mechanistic, simulation-ready models [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. Its personalized brain models are parameterized by structural connectivity derived from diffusion imaging and validated against empirical functional connectivity, establishing a forward-modeling framework for studying brain disorders through virtual patient simulations [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. PyCortex serves as a downstream visualization layer for TVB outputs exported in surface-compatible formats, placing simulated activity patterns in anatomical context with the vertex-level precision required for interpretable surface mapping [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]]. While [[tvb-webui]] provides built-in surface rendering for iterative model construction, PyCortex offers programmable control over figure specification that aligns with [[human-connectome-project]] surface conventions, including support for common parcellations such as the [[glasser-atlas]] and [[schaefer-atlas]]. Researchers therefore frequently use TVB for generative modeling of whole-brain dynamics and then employ PyCortex for final hypothesis exploration on the cortical sheet [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]].

## Position in the Visualization Ecosystem

PyCortex occupies a specialized niche alongside broader neuroimaging visualization tools. For volume-based inspection, [[fsl]] remains the standard; for alternative surface exploration, [[pysurfer]] provides comparable vertex-level rendering with a different API philosophy; and [[connectome-workbench]] serves as the official HCP viewer with native CIFTI interaction. PyCortex distinguishes itself through programmatic Python-level control and superior static figure generation, making it particularly valuable when reproducible publication-ready surface maps are required. It is commonly used to display high-resolution [[resting-state]] functional connectivity patterns, task-based statistical contrasts, and simulation-derived activity on the cortical surface within whole-brain modeling pipelines.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate [[brain-network]] dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain [[connectivity]]. [DOI](https://doi.org/10.1089/brain.2012.0120)