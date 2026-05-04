---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-380768cf42a8.md
- raw/papers/semanticscholar-eb4197c24bf2.md
tags:
- software-visualization
- neuroimaging
- neuroimaging-fmri
- brain-parcellations
title: PyCortex
type: entity
updated: '2026-04-30'
---

## Overview

PyCortex is an open-source Python library designed for the visualization and analysis of [[neuroimaging]] data on cortical surfaces. Developed by James Gao at the Gallant Lab at the University of California, Berkeley, PyCortex provides a streamlined interface for rendering volumetric brain imaging data—particularly functional magnetic resonance imaging ([[fmri]]) signals—onto three-dimensional cortical meshes derived from structural MRI scans. The software operates as a middle layer between raw neuroimaging data formats (such as [[nifti]]) and interactive web-based or standalone visualization outputs, making it especially valuable for researchers working with surface-based representations of brain activity.

The core functionality of PyCortex revolves around its ability to warp volumetric fMRI data onto a standardized cortical surface, enabling researchers to visualize activation patterns in a way that respects the underlying anatomy of the cerebral cortex. Unlike volume-based visualizations that display data in voxel grids, surface-based representations preserve the topological relationships between brain regions and reveal patterns of activation that follow the folded structure of the cortical sheet. This capability has made PyCortex a popular tool in the [[connectomics]] and [[whole-brain|whole-brain modeling]] communities, where surface representations are frequently used to display functional connectivity patterns, dynamic activity states, and model outputs.

## Key Features

PyCortex distinguishes itself through several technical capabilities that address common challenges in neuroimaging visualization. First, the software accepts pre-processed cortical surfaces from external segmentation tools such as [[freesurfer]], rather than implementing its own reconstruction pipeline. PyCortex reads FreeSurfer output files (including surfaces, cortical depth maps, and registration transforms) and uses them to project volumetric data onto the cortical mesh. This approach allows researchers to leverage established preprocessing pipelines while benefiting from PyCortex's specialized visualization capabilities.

Second, PyCortex provides a sophisticated API for mapping volumetric time-series data onto cortical surfaces through surface-based averaging. The software handles the complex transformation from volumetric to surface space by projecting fMRI signal intensities onto vertices of the cortical mesh, accounting for the anatomical geometry of the cortex. This projection can be performed using various interpolation schemes, allowing users to balance spatial precision against signal smoothing.

Third, the library includes extensive support for working with brain parcellations, including standard atlases such as the [[desikan-killiany-atlas]], [[destrieux-atlas]], and [[glasser-atlas]]. Researchers can overlay parcel boundaries on functional activation maps, facilitating the interpretation of activation patterns in terms of anatomically defined regions of interest. The software also supports custom parcellations, enabling visualization of results from novel segmentation approaches.

Fourth, PyCortex offers export capabilities that generate interactive HTML visualizations using WebGL, allowing researchers to share detailed brain maps through web browsers without requiring specialized visualization software on the viewer's machine. These exports are self-contained and include built-in controls for rotating, zooming, and slicing the cortical surface, making them ideal for supplementary materials in publications or presentations.

## Relationship to TVB

PyCortex occupies an important niche in the [[the-virtual-brain]] (TVB) ecosystem, particularly during the post-processing and visualization stages of whole-brain modeling workflows. TVB simulates large-scale brain dynamics using [[neural-mass-models]] or [[spiking-neural-networks]] driven by [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI) data. The output of these simulations—typically time series of regional activation or connectivity estimates—can be visualized using PyCortex to display the evolving activity patterns on a realistic cortical surface.

The relationship between TVB and PyCortex is primarily unidirectional: TVB generates model outputs in volumetric or regional form, and PyCortex provides the visualization layer that renders these outputs in an anatomically meaningful way. Researchers using TVB often employ PyCortex to examine spatial patterns of seizure-like activity in [[epilepsy-modeling]] studies, to visualize changes in [[functional-connectivity]] patterns across different brain states, and to display the results of [[personalized-brain-modeling]] workflows that generate patient-specific brain simulations. While PyCortex does not directly interface with TVB's simulation engine, the two tools are frequently used in succession within pipelines for connectome-based research.

## Key Papers

PyCortex was introduced through the publication "Introducing pycortex: a Python package for interactive visualization of fMRI data on inflated cortical surfaces" by James Gao, Stephan Niekamp, An‑Tzu Lin, and Jack Gallant, published in Frontiers in Neuroinformatics in 2015. The paper demonstrated the software's capabilities for surface‑based neuroimaging visualization and highlighted the utility of the tool for displaying group‑level activation maps, individual subject data, and dynamic time‑series on cortical surfaces. The publication established PyCortex as an accessible visualization option for researchers working with surface‑based neuroimaging data.

The software has been cited in numerous studies employing [[resting-state]] fMRI analysis, [[default‑mode‑network]] characterization, and connectome‑wide investigations of functional connectivity. Researchers have used PyCortex to visualize results from [[dynamic‑causal‑modeling]] analyses, to display outputs from [[connectivity]] decomposition methods, and to generate figures for studies investigating [[brain‑oscillations]] and large‑scale network dynamics.

## Related Software

PyCortex operates within a broader ecosystem of neuroimaging visualization tools, and understanding its position relative to alternatives helps clarify its appropriate use cases. The [[connectome-workbench]] offers similarly surface‑based visualization capabilities but with a more comprehensive suite of tools for exploring neuroimaging datasets, particularly those from the [[hcp-dataset]]. [[brainnet‑viewer]] provides another alternative for surface‑based visualization with a focus on network visualization, though it uses a different underlying visualization framework.

For volumetric visualization, [[freesurfer]]'s built‑in tools and [[fsl]] remain widely used, while [[nilearn]] provides Python‑native interfaces to both volume and surface‑based visualization within a machine‑learning‑focused framework. The [[brain‑dynamics‑toolbox]] and [[bctpy]] (Brain Connectivity Toolbox) complement PyCortex by providing analysis capabilities that precede visualization, enabling researchers to compute [[network‑dynamics]] metrics, perform [[community‑detection]], and analyze [[modularity]] before rendering results on cortical surfaces. For projects requiring integration with [[tvb]] simulations, researchers may use PyCortex alongside [[nilearn]] or matplotlib for complete analysis and visualization pipelines.

Unlike specialized whole‑brain simulators such as TVB or tools designed for [[neural‑mass‑models]] implementation like [[brian2]] or [[nest]], PyCortex focuses exclusively on visualization and does not provide analysis, simulation, or modeling capabilities. This specialization allows the software to maintain a focused API and lightweight dependencies while providing robust visualization functions.