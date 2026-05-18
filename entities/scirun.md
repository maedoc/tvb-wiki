---
title: SCIRun
created: 2026-05-18
updated: 2026-05-18
type: entity
tags: [software-brain-modeling, neuroimaging-eeg, neuroimaging-meg, whole-brain-modeling]
sources: []
---

SCIRun (Scientific Computing and Imaging Institute Run) is an interactive problem-solving environment for scientific computing and visualization originally developed at the University of Utah's Scientific Computing and Imaging Institute (SCI). First released in the late 1990s, it provides a visual programming framework in which researchers construct computational workflows by connecting modular components within a dataflow-directed graph. Within computational neuroscience, SCIRun has established itself as a standard platform for biophysical [[forward-model]]ing of [[eeg]] and [[meg]] signals and for solving [[source-localization]] problems using realistic head and brain geometries.

The architecture of SCIRun was motivated by the need to bridge the gap between general-purpose numerical libraries and the specialized analytical tools required by domain scientists. Traditional scientific software often forced researchers to write custom scripts for each new problem configuration, making parameter sweeps and pipeline sharing cumbersome. SCIRun addresses this limitation by treating computational modules as visual nodes with typed input and output ports; users assemble complete analysis pipelines by dragging modules into a network editor and drawing connections between ports. This dataflow paradigm supports rapid iteration on model parameters and anatomical geometries while preserving the flexibility to substitute custom solvers or integrate external data formats.

For neuroimaging applications, SCIRun includes solvers for the boundary element method (BEM) and finite element method (FEM) that compute [[volume-conduction]] effects in realistic head models. These forward solvers construct the lead field matrix mapping neural current sources to scalp-level electromagnetic potentials, incorporating tissue conductivity inhomogeneities across compartments such as skin, skull, cerebrospinal fluid, and brain. When head geometries are derived from individual anatomical imaging and segmented into accurate boundary or volume meshes, the resulting forward solutions supply the physical foundation for inverse algorithms that estimate source distributions from measured [[eeg]] or [[meg]] recordings. The environment additionally supports mesh generation, segmentation, and interactive three-dimensional visualization of anatomical data.

## Relationship to TVB

SCIRun occupies a complementary position in the [[whole-brain-modeling]] ecosystem alongside [[the-virtual-brain]] (TVB). Whereas TVB focuses on large-scale [[neural-mass-models]] and [[network-dynamics]] simulations coupled through structural connectomes, SCIRun contributes the biophysical forward-modeling layer required to translate simulated neural activity into observable electromagnetic signals. In an integrated workflow, TVB first generates population-level neuronal dynamics across a parcellated brain network, and SCIRun then computes the corresponding forward solution that projects this activity onto scalp sensors, enabling direct quantitative comparison with empirical [[eeg]] or [[meg]] data.

This synergy is especially valuable for research programs that investigate how macroscopic [[brain-oscillations]] or pathological propagation patterns manifest at the sensor level. Studies of seizure dynamics in [[epilepsy-modeling]], for instance, can simulate aberrant activity spreading across coupled connectome regions in TVB and then use SCIRun’s validated BEM and FEM solvers to predict the resulting scalp potential topography. By functioning as the biophysical bridge between population-level simulation and sensor-level observation, SCIRun extends TVB-based modeling into direct confrontation with experimental neuroimaging data.
