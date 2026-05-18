---
created: 2026-04-20
sources: []
tags:
- software-brain-modeling
- software-visualization
- neuroimaging-eeg
- neuroimaging-meg
- whole-brain-modeling
- structural-connectivity
- brain-oscillations
- epilepsy-modeling
title: SCIRun
type: entity
updated: 2026-05-18
---
SCIRun is a modular problem-solving environment developed at the University of Utah's Scientific Computing and Imaging Institute. First released in the late 1990s, it enables researchers to assemble computational workflows through a visual dataflow programming interface in which typed modules are wired together in a directed graph editor. Within [[computational-neuroscience]], it is best known for validated biophysical forward solvers that compute how neural currents propagate through realistic head geometries to produce measurable electromagnetic signals.

## Motivation and Context

The development of SCIRun was motivated by the gap between low-level numerical libraries and the high-level tools domain scientists require. Traditional software forces researchers to write custom scripts for each new problem, making parameter sweeps and pipeline sharing cumbersome. SCIRun addresses this by exposing modules with typed input and output ports; users build pipelines by dragging components into a network editor and drawing connections between ports. This supports rapid iteration on model parameters and anatomical geometries while preserving flexibility to substitute custom solvers.

For [[whole-brain-modeling]], this visual dataflow approach lets researchers interleave anatomical processing with biophysical simulation. Rather than chaining rigid scripts, investigators can modify mesh resolutions, tissue conductivities, or solver types within the same environment. The resulting workflows are transparent because the network graph documents every operation.

## Key Facts and Dates
SCIRun is developed by the Scientific Computing and Imaging Institute at the University of Utah as a problem-solving environment, or "computational workbench," in which researchers assemble workflows by wiring software modules in a visual programming interface [[raw/articles/scirun-sci-website.md|SCI Institute]]. The present codebase, SCIRun 5, constitutes a complete rewrite of the GUI front end and graphical components of the earlier SCIRun 4 release, introducing a more stable middle layer and integrated Python scripting capabilities [[raw/articles/scirun-github.md|SCIRun GitHub Repository]]. Implemented primarily in C++— comprising over 94 percent of the codebase— alongside CMake, C, and Python bindings, the project is distributed under the MIT License [[raw/articles/scirun-github.md|SCIRun GitHub Repository]].

The SCIRun 5 GitHub repository was created in February 2012, and active development continues through ongoing beta releases, with version v5.0-beta.2026 published in March 2026 [[raw/articles/scirun-github.md|SCIRun GitHub Repository]]. Documentation and binary downloads are maintained through the project's GitHub page and a dedicated Read the Docs site, while the main project homepage remains at scirun.org [[raw/articles/scirun-github.md|SCIRun GitHub Repository]]. Because the modular architecture exposes all parameters within each component, investigators can duplicate existing networks and construct new modules without leaving the visual dataflow environment [[raw/articles/scirun-sci-website.md|SCI Institute]].
## Forward Modeling Capabilities

SCIRun includes boundary element and finite element solvers that compute [[volume-conduction]] effects in realistic head models. These forward solvers construct the lead field matrix mapping sources to scalp potentials, incorporating tissue conductivity inhomogeneities across skin, skull, cerebrospinal fluid, and brain compartments. The resulting solutions provide a foundation for inverse algorithms that estimate source distributions from measured [[eeg]] or [[meg]] recordings. The environment also supports mesh generation and interactive visualization, allowing researchers to inspect anatomical models before simulation.

## Relationship to Related Software

SCIRun occupies a distinct niche by coupling validated biophysical forward solvers with a visual dataflow environment. Whereas [[brainstorm]] and [[econnectome]] present pre-assembled pipelines through MATLAB-based graphical interfaces, SCIRun exposes computation as typed modules wired in a network editor. This preserves flexibility to substitute custom solvers, though with a steeper learning curve than [[cartool]], which offers immediate [[source-localization]] via dedicated menus. The overlap with [[3d-slicer]] lies in anatomical visualization, but 3D Slicer is oriented toward general medical imaging rather than electromagnetic volume conduction. In EEG/MEG forward modeling, [[openmeeg]] offers a comparable boundary element solver, though it is typically invoked as a library rather than within a visual dataflow environment.

## Relationship to TVB

SCIRun serves a complementary role in the whole-brain-modeling ecosystem alongside [[the-virtual-brain]] (TVB). Whereas TVB focuses on large-scale [[neural-mass-models]] and [[network-dynamics]] simulations coupled through [[structural-connectivity]], SCIRun contributes the biophysical forward-modeling layer that translates simulated neural activity into electromagnetic signals. In integrated workflows, TVB generates population-level dynamics across a parcellated brain network, and SCIRun computes the forward solution that projects this activity onto scalp sensors, enabling comparison with EEG or MEG data. This synergy is valuable for investigating how macroscopic [[brain-oscillations]] or seizure dynamics in [[epilepsy-modeling]] manifest at the sensor level.
