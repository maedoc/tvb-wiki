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
updated: '2026-05-18'
---

SCIRun (Scientific Computing and Imaging Institute Run) is a modular problem-solving environment developed at the University of Utah that enables researchers to assemble computational workflows through a visual dataflow programming interface. First released in the late 1990s, the software treats computational modules as typed nodes that users wire together in a directed graph editor. Within [[computational-neuroscience]], it is best known for validated biophysical forward solvers that compute how neural currents propagate through realistic head geometries to produce measurable electromagnetic signals.

The development of SCIRun was motivated by the gap between low-level numerical libraries and the high-level tools domain scientists require. Traditional scientific software forces researchers to write custom scripts for each new problem configuration, making parameter sweeps and pipeline sharing cumbersome. SCIRun addresses this limitation by exposing modules with typed input and output ports; users build analysis pipelines by dragging components into a network editor and drawing connections between ports. This paradigm supports rapid iteration on model parameters and anatomical geometries while preserving the flexibility to substitute custom solvers or integrate external data formats.

## Key Features and Technical Capabilities

For neuroimaging applications, SCIRun includes solvers for the boundary element method (BEM) and finite element method (FEM) that compute [[volume-conduction]] effects in realistic head models. These forward solvers construct the lead field matrix mapping neural current sources to scalp-level electromagnetic potentials, incorporating tissue conductivity inhomogeneities across skin, skull, cerebrospinal fluid, and brain compartments. When head geometries are derived from individual anatomical scans and segmented into accurate boundary or volume meshes, the resulting forward solutions supply the physical foundation for inverse algorithms that estimate source distributions from measured [[eeg]] or [[meg]] recordings. The environment additionally supports mesh generation, segmentation, and interactive three-dimensional visualization.

## Relationship to Related Software

SCIRun occupies a distinct niche among neuroimaging toolboxes by coupling validated biophysical forward solvers with a visual dataflow programming environment. Whereas [[brainstorm]] and [[econnectome]] present pre-assembled pipelines through graphical user interfaces built atop MATLAB, SCIRun exposes the underlying computation as typed modules that users wire together in a network editor. This architectural choice preserves the flexibility to substitute custom solvers or insert geometry-processing steps between anatomical images and the forward solution, though the trade-off is a steeper initial learning curve compared to environments like [[cartool]] that offer immediate access to [[source-localization]] via dedicated menus. The overlap with [[3d-slicer]] lies in anatomical visualization and mesh manipulation, but 3D Slicer's plugin architecture is oriented toward general medical image computing rather than the specific physics of electromagnetic volume conduction. Consequently, Slicer is more commonly encountered in preprocessing pipelines that prepare structural data for downstream simulation, while SCIRun operates as the forward-modeling layer that projects neural currents onto scalp sensors.

## Relationship to TVB

SCIRun serves a complementary role in the [[whole-brain-modeling]] ecosystem alongside [[the-virtual-brain]] (TVB). Whereas TVB focuses on large-scale [[neural-mass-models]] and [[network-dynamics]] simulations coupled through [[structural-connectivity]], SCIRun contributes the biophysical forward-modeling layer required to translate simulated neural activity into observable electromagnetic signals. In an integrated workflow, TVB generates population-level neuronal dynamics across a parcellated brain network, and SCIRun computes the corresponding forward solution that projects this activity onto scalp sensors, enabling direct comparison with empirical [[eeg]] or [[meg]] data. This synergy is especially valuable for research programs investigating how macroscopic [[brain-oscillations]] or pathological propagation patterns manifest at the sensor level, such as studies of seizure dynamics in [[epilepsy-modeling]].