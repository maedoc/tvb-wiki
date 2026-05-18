---
created: 2025-01-15
sources:
- raw/papers/joss-06590.md
- raw/papers/sanz-leon-2013.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-visualization
- neuroimaging
- neuroimaging-fmri
- neuroimaging-dti
- connectomics
- database-neurovault
title: Neurosift
type: entity
updated: '2026-05-18'
---

Neurosift is a web-based [[neuroimaging]] data visualization and analysis platform that runs directly in modern web browsers without requiring local software installation. Originally developed by Jeremy Moreau with ongoing support from the NeuroVault team, Neurosift provides interactive exploration of volumetric ([[nifti]]), surface-based ([[cifti]]/Gifti), and dense [[connectivity]] data, making it particularly valuable for [[whole-brain|whole-brain modeling]] workflows where researchers need to inspect structural connectivity matrices, functional connectivity maps, and simulation outputs.

## Overview

Neurosift functions as a zero-install alternative to desktop neuroimaging viewers like [[freeview]], fslview, or [[connectome-workbench]]. The platform loads neuroimaging files directly from URLs or local uploads, rendering them in an interactive 3D environment that supports cutting, rotating, and overlay capabilities. Unlike traditional viewers that require significant disk space and dependencies ([[freesurfer]], FSL), Neurosift runs entirely in the browser using WebGL, meaning researchers can share visualizations via simple URL links that embed the exact state of the viewer. This web-first architecture makes it especially useful for collaborative workflows where multiple investigators need to inspect the same data without coordinating software installations.

The platform supports the full range of neuroimaging formats used in [[connectome]]-based research, including NIfTI-1/2 for volumetric data, CIFTI for grayordinate-based connectivity results, Gifti for surface data, and dense matrix formats for tractography-derived connectivity data. Neurosift also integrates directly with [[neurovault]], allowing users to search, load, and visualize publicly shared neuroimaging datasets without downloading files first.

## Key Features

The core strength of Neurosift lies in its handling of multi-file neuroimaging datasets. For whole-brain connectivity analysis, researchers often work with several related files—a [[parcellation]] scheme, a connectivity matrix, and associated statistical maps. Neurosift can load these as a cohesive package, displaying the anatomical template while overlaying connectivity-based results. The platform supports transparent overlays with adjustable opacity, allowing users to inspect how statistical results from [[dynamic-causal-modeling]] or [[neural-mass-models]] align with underlying anatomical structures.

Surface-based visualization in Neurosift uses WebGL rendering of cortical and subcortical meshes, enabling smooth rotation, zoom, and slicing operations that would otherwise require heavy desktop software. The platform's CIFTI support is particularly relevant for [[human-connectome-project]] data, where grayordinate-based representations have largely replaced volumetric approaches for cortical analysis. Users can visualize [[resting-state]] networks, task-based activation patterns, and tractography streamlines in a unified interface.

Neurosift also provides basic connectivity matrix visualization, allowing users to view correlation or coherence matrices as heatmaps alongside the anatomical displays. This integrated view supports researchers working with [[structural-connectivity]] matrices derived from [[diffusion-imaging]] and [[tractography]] pipelines, as well as [[functional-connectivity]] matrices from [[fmri]] or [[meg]] data.

## Relationship to TVB

Neurosift can complement [[the-virtual-brain]] workflows in several valuable ways. TVB simulations produce output files in NIfTI format (regional time series, statistical maps) and connectivity matrices that researchers often need to inspect after simulation. Neurosift offers a lightweight way to visualize these outputs without launching the full TVB pipeline or desktop visualization tools. Researchers can upload their TVB simulation results to Neurosift for quick visual inspection, share links with collaborators for feedback, or compare simulation-derived connectivity patterns against empirical data from [[hcp-dataset]] or [[abide]] cohorts.

The platform may be particularly useful for the TVB community as it can help bridge the gap between simulation outputs and standard neuroimaging analysis. When validating whole-brain models against empirical neuroimaging data, investigators often need to overlay model-derived statistical maps onto anatomical templates—a task that Neurosift can handle efficiently for web-based collaboration.

## Related Software

Neurosift occupies a specific niche in the neuroimaging visualization landscape, positioned between lightweight quick viewers and fully featured analysis platforms. [[neurovault]] provides the data repository infrastructure that feeds Neurosift's search and loading capabilities. For more intensive analysis tasks, researchers typically turn to [[connectome-workbench]] (for CIFTI/surface data), [[fsl-melodic]], or [[freeview]] paired with FreeSurfer. For web-based quick visualization of simpler datasets, [[nilearn-datasets]] provides programmatic access similar to Neurosift's URL-based loading.

## Key Papers
Neurosift was formally introduced by [[raw/papers/joss-06590.md|Magland et al. (2024)]] in the *Journal of Open Source Software* as a browser-based tool for the visualization of neuroscience data, with a focus on NWB (Neurodata Without Borders) files and [[dandi]] archive exploration. [[raw/papers/joss-06590.md|Magland et al. (2024)]] published the work in volume 9, issue 97 of JOSS, documenting the software's architecture and its application to neurophysiological dataset visualization. The title and abstract of [[raw/papers/joss-06590.md|Magland et al. (2024)]] emphasize that the tool renders complex datasets within standard web browsers.

This tool occupies a complementary position alongside established platforms in the whole-brain modeling and connectivity analysis literature. [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]] presented [[the-virtual-brain|TVB]] as a simulator of primate brain network dynamics, and [[raw/papers/mijalkov-2017-braph.md|Mijalkov et al. (2017)]] developed BRAPH as a pipeline for brain connectivity analysis. [[raw/papers/joss-06590.md|Magland et al. (2024)]] designed Neurosift for interactive, browser-based visualization of neuroscience datasets, complementing these simulation and analysis platforms.

## References

1. (authors unknown). *Neurosift: DANDI exploration and NWB visualization in the browser*.
2. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
3. (authors unknown). *[[braph]]: A Pipeline for Brain Connectivity Analysis*.