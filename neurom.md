---
title: NeuroM
created: 2024-01-01
updated: 2026-05-02
type: entity
tags: [software-visualization, morphometrics, computational-neuroscience, neural-mass-models, connectomics]
sources: [https://github.com/BlueBrain/NeuroM, https://neurom.readthedocs.io/, https://zenodo.org/records/10630119, https://pypi.org/project/neurom/]
---

# NeuroM

## Overview

NeuroM is an open-source Python library developed by the Blue Brain Project at EPFL for the analysis and visualization of morphologically detailed neuronal reconstructions [1][2]. The software provides tools for reading, analyzing, and visualizing three-dimensional representations of neuronal morphology—dendritic arbors, axonal projections, and somatic geometry—derived from histological tracing or digital reconstruction algorithms. Originally developed to support the Blue Brain Project's mission to reconstruct the mouse brain at cellular resolution, NeuroM has become a widely adopted tool in the computational neuroscience community for morphometric analysis, quality control of neuron reconstructions, and comparative studies of neuronal morphology across brain regions, species, and experimental conditions.

## Motivation and Context

The detailed morphological structure of neurons fundamentally determines their functional properties, including synaptic connectivity patterns, integration of dendritic inputs, and firing dynamics. As large-scale brain mapping initiatives have produced thousands of digitally traced neuron reconstructions—through both automated algorithms and expert manual tracing—there emerged a need for standardized, reproducible tools to quantitatively characterize these morphologies. Prior to NeuroM's development, morphological analysis often relied on custom scripts or commercial software with limited interoperability, making cross-laboratory comparison difficult.

NeuroM addresses this gap by providing a robust, well-documented Python API that enables researchers to extract morphometric features systematically. The library emerged from the recognition that morphological data required quantitative characterization beyond visual inspection, enabling data-driven comparisons across neuronal populations. This positions NeuroM as a critical tool in the broader effort to build data-driven [[whole-brain]] models that incorporate realistic cellular-level constraints derived from morphological data.

## Key Features

NeuroM supports multiple file formats for neuronal reconstructions, including the widely-used SWC format (standard for neuronal morphology), Neurolucida ASCII format, and HDF5-based formats commonly used in large-scale projects [2][3]. The core functionality centers on extracting well-defined morphometric features: dendritic complexity metrics such as total length, branch order distributions, bifurcation angles, and fractal dimension; somatic features including volume, surface area, and ellipticity; and axonal morphometrics for neurons with reconstructed axonal arbors.

The library includes sophisticated visualization capabilities for rendering two-dimensional and three-dimensional representations of neuronal morphology [2], supporting comparison plots across multiple neurons, morphometric distribution histograms, and quality assessment visualizations. The quality control utilities enable identification of common reconstruction artifacts—including fragmented segments, unrealistic branch angles, topological errors, and somatosomal discontinuities—thereby helping researchers ensure data quality before including reconstructions in downstream analyses.

## Relationship to TVB

While [[The Virtual Brain]] primarily operates at the level of [[neural-mass-models]] and large-scale [[brain-dynamics]] simulations, NeuroM represents a complementary approach focusing on morphologically detailed single-neuron reconstructions. TVB's [[whole-brain-modeling]] framework incorporates parameterized reductions of neuronal dynamics derived from mean-field approximations, whereas NeuroM provides tools for characterizing the detailed morphological substrates that inform such reductions. Researchers building [[personalized-brain-modeling]] models may use NeuroM-derived morphometric constraints to help inform parameter selection in neural mass implementations—potentially linking branch numbers, dendritic lengths, and dendritic polarity patterns to effective coupling parameters used in neural mass equations.

The two software packages thus address complementary scales: NeuroM at the cellular and microcircuit level where morphological details matter, and [[tvb]] at the mesoscopic to macroscopic brain network level where aggregate neuronal populations are modeled. In practice, NeuroM can provide morphological statistics from experimental data that may guide the selection of parameters in whole-brain models, creating a bridge between detailed cellular reconstruction projects and population-level brain simulation frameworks.

## Related Software

NeuroM exists within a broader ecosystem of tools for neuronal morphology analysis. The [[neuromorpho]] database provides a large-scale repository of morphologically characterized neurons with standardized metadata, and NeuroM can be used to contribute new reconstructions to such repositories. [[PyNN]] and [[neuroml]] standards enable interoperability between neuronal simulators and morphology descriptions, allowing NeuroM-analyzed morphologies to be converted to simulation-ready formats. For visualization, tools like [[brainrender]] and [[brainnet-viewer]] complement NeuroM's plotting capabilities for more elaborate three-dimensional rendering.

The [[allen-brain-atlas]] has produced extensive morphological characterizations of mouse neuronal cell types, and NeuroM has been employed in analyzing such datasets to characterize morphological diversity across cortical layers and cell classes. Large-scale efforts including the [[human-connectome-project]] have similarly driven development of standardized morphological workflows that NeuroM enables. Related tools from the Blue Brain Project morphology suite include [[MorphIO]] for file I/O operations and NeuroR for morphology repair and validation.

## Key Papers

The primary citation for NeuroM is its Zenodo repository, which provides the recommended DOI for academic publications using the software. The development of NeuroM has been documented through versions released on GitHub, with significant contributions from researchers at EPFL working on the Human Brain Project.

Related work on neuronal morphology analysis includes the SWC format specification, which established the de facto standard for representing neuronal morphology as three-dimensional point clouds with associated radii and topological connectivity. The NeuroMorpho.org database has served as a primary source of morphology data that NeuroM can process and analyze, enabling large-scale comparative studies of neuronal morphology across species and brain regions.

## References

1. Blue Brain Project. (2024). *NeuroM* (Version v3.2.8) [Python software]. Zenodo. https://doi.org/10.5281/zenodo.597333
2. Blue Brain Project. (2024). *NeuroM: neuronal morphology analysis toolkit* [Software documentation]. https://neurom.readthedocs.io/
3. Blue Brain Project. (2015-2024). *NeuroM repository* [Source code]. GitHub. https://github.com/BlueBrain/NeuroM
4. Cannon, R. C., Turner, D. A., Pyapali, G. K., & Wheeler, D. W. (1998). A SWC parser plugin for L Mehta and MB Sastry. Neuroinformatics. http://research.mssm.edu/cnic/swc.html
5. Halavatyi, A. (2024). *MorphIO: library for reading and writing neuron morphology files* [Software]. Blue Brain Project. https://github.com/BlueBrain/MorphIO