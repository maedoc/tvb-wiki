---
title: BrainGlobe
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software-brain-modeling, software-visualization, brain-parcellations, connectomics, neuroimaging, atlas, python]
sources:
  - https://doi.org/10.21105/joss.02668
  - https://brainglobe.info/documentation/brainglobe-atlasapi/index.html
  - https://github.com/brainglobe/brainreg
  - https://github.com/brainglobe/cellfinder
---

# BrainGlobe

## Overview

BrainGlobe is an open-source Python software ecosystem for neuroanatomical analysis, providing a unified framework for working with brain atlases, performing image registration, segmenting anatomical structures, and visualizing three-dimensional brain data. Developed primarily by the [Atlases and Anatomy][] team at the Sainsbury Wellcome Centre for Neural Circuits and Behaviour, BrainGlobe offers a modular collection of tools that address the fragmented landscape of neuroanatomy software by providing consistent Python APIs across diverse formats and atlases [[1]].

## Motivation and Context

The field of neuroimaging suffers from a proliferation of incompatible atlas formats, segmentation pipelines, and visualization tools, each developed in isolation by different research groups. Historically, researchers wanting to work with brain atlases had to navigate a maze of specialized software: FreeSurfer for cortical parcellation, ANTs for image registration, FSL for voxel-based statistics, Connectome Workbench for surface-based visualization, and BrainVisa for French neuroimaging data. Each tool uses its own native formats, coordinate systems, and processing pipelines, creating substantial friction when trying to combine them in a single analysis workflow.

BrainGlobe emerged from the practical need to streamline these workflows, particularly for projects involving cell distribution analysis, connectomics, and whole-brain modeling. The Virtual Brain project and similar whole-brain simulation frameworks require precise anatomical parcellations to define network nodes, yet the process of converting between atlas formats and performing registration was historically a manual and error-prone process. BrainGlobe addresses this by providing a unified Atlas API that can load, manipulate, and convert between dozens of brain atlases through a consistent Python interface, abstracting away the underlying format complexity.

## Key Features

### Atlas Management

The core of BrainGlobe is its **Atlas API**, which provides a standardized interface for loading and querying brain atlases. Supported atlases include the Allen Mouse Brain Atlas, Allen Human Brain Atlas, Enhanced and Unified Mouse Brain Atlas, Waxholm Space rat brain atlas, and numerous others spanning multiple species including mouse, rat, zebrafish, axolotl, and cavefish [[2]]. The API handles coordinate space transformations automatically, allowing researchers to work in native scanner space, MNI space, or atlas space without manual conversion.

### Brain Registration

**brainreg** is BrainGlobe's automated registration pipeline that aligns sample brains to a reference atlas. Built on ANTsPy and NiftyReg, brainreg supports both linear and deformable registration, with optional prior-based refinement for specific anatomical structures [[3]]. The tool produces both transformation matrices and warped segmentations, enabling downstream analyses that require spatial normalization.

### Cell Detection

**cellfinder** addresses a specific need in neuroanatomy: classifying and localizing cells in cleared tissue or histology images. Given a three-dimensional image stack, cellfinder uses a deep learning classifier to distinguish neuronal from non-neuronal cells and reports their positions in atlas-compatible coordinates [[4]]. This is particularly valuable for projects mapping injection sites, lesion volumes, or developmental cell distributions.

### Visualization

BrainGlobe includes integration with brainrender for three-dimensional visualization of atlas structures, registered images, and anatomical annotations. The visualization layer supports interactive exploration, screenshot generation, and animation for presentations. Combined with Napari integration for general image viewing, BrainGlobe provides end-to-end visualization of neuroanatomical data.

## Relationship to TVB

BrainGlobe interfaces with [[tvb]] and [[the-virtual-brain]] through atlas-based parcellation workflows used to define brain region nodes in whole-brain connectivity models. When constructing a personalized brain model, researchers often begin with diffusion tensor imaging (DTI) to obtain structural connectivity, then use an atlas to define the network nodes and extract time series from fMRI or EEG data. BrainGlobe's standardized atlas formats facilitate this process, enabling more reproducible TVB workflows across laboratories. The Python-native design of BrainGlobe also aligns well with TVB's own Python scripting interface, allowing direct integration in scripts that prepare personalized connectivity matrices.

## Related Software

BrainGlobe occupies a unique niche but connects to several established tools in the neuroimaging ecosystem. For atlas manipulation, it parallels nilearn's fetching utilities but provides more comprehensive editing capabilities. For visualization, it complements brainrender rather than replacing it, acting as the data preparation layer. For registration, it builds on ANTs and NiftyReg by providing higher-level automation. For surface-based work, it complements Connectome Workbench by focusing on volume-based analyses. The Python packaging also positions BrainGlobe alongside nipype as infrastructure for building reproducible neuroimaging pipelines.

## Technical Notes

BrainGlobe's architecture separates concerns into independent Python packages that can be installed individually or as a full stack. The core brainreg package manages registration, while brainglobe-atlasapi handles atlas loading, and cellfinder provides cell classification. All packages share common conventions: NIfTI input/output, optional configuration files in YAML, and logging through Python's standard logging module. Atlases are distributed through a dedicated download API that caches data locally after first use, reducing network dependencies in repeated analyses.

## References

[1] Claudi, F., Petrucco, L., Tyson, A. L., Branco, T., Margrie, T. W. and Portugues, R. (2020). BrainGlobe Atlas API: a common interface for neuroanatomical atlases. *Journal of Open Source Software*, 5(54), 2668. https://doi.org/10.21105/joss.02668

[2] BrainGlobe Documentation. Brainglobe Atlas API. https://brainglobe.info/documentation/brainglobe-atlasapi/index.html

[3] BrainGlobe GitHub. brainreg repository. https://github.com/brainglobe/brainreg

[4] BrainGlobe GitHub. cellfinder repository. https://github.com/brainglobe/cellfinder