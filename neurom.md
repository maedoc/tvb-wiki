---
title: NeuroM
created: 2025-01-15
updated: 2026-05-02
type: entity
tags: [software-neurom, neuromorphic-computing, software-visualization, neural-mass-models, spiking-neural-networks, python, morphology-analysis]
sources:
  - https://doi.org/10.5281/zenodo.597333
  - https://doi.org/10.1007/s40708-016-0041-7
  - https://portal.bluebrain.epfl.ch/resources/software/morphology-suite/
  - https://neurom.readthedocs.io/
---

# NeuroM

## Overview

NeuroM is an open-source Python toolkit for the analysis, processing, and visualization of neuronal morphologies. Developed primarily at the Blue Brain Project, it provides a standardized interface for reading, validating, and extracting morphometric features from digital reconstructions of neurons and glial cells. The software supports common morphological file formats including SWC, ASC (Automatically Generated ASC files), and H5, enabling interoperability between different reconstruction tools and neuroscience databases [Blue Brain Portal; NeuroM Documentation].

## Key Features

NeuroM offers a comprehensive suite of capabilities for morphological analysis. At its core, the toolkit provides robust parsing of neuronal reconstructions, converting diverse file formats into a canonical internal representation. The **validation module** performs quality control checks on morphological data, detecting common artifacts such as incorrect branching order, inappropriate diameters, or fragmented neurites. This validation is particularly valuable for large-scale datasets where manual inspection would be prohibitively expensive [NeuroM Documentation].

The **morphometric extraction** functionality computes dozens of quantitative features including total length, number of branches, branch order distributions, and tapering profiles [NeuroM API Documentation]. These metrics enable quantitative comparisons between cell types, developmental stages, or disease states. The **visualization module** produces publication-quality 2D and 3D renderings of neuronal morphologies, with options to overlay quantitative information such as local diameter or branch order.

NeuroM's design emphasizes **extensibility** through a plugin-like architecture. Users can define custom morphometric features through a declarative API. The command-line interface facilitates batch processing of entire datasets, making it suitable for high-throughput analysis pipelines. The toolkit is used extensively in the EBRAINS Cellular Level Simulation Platform for cortical microcircuit reconstruction [Blue Brain Portal].

## Relationship to TVB

While NeuroM focuses on single-neuron morphology, it is conceptually related to [[whole-brain modeling]] approaches used in [[The Virtual Brain]] (TVB). In TVB, large-scale network models often incorporate neural mass representations that abstract the collective activity of many neurons. Understanding the morphological diversity of underlying neurons can inform the parameterization of such mass models, particularly when modeling region-specific dynamics.

More directly, NeuroM can complement TVB workflows that incorporate detailed single-neuron models. When building biologically realistic spiking neural network models—whether in TVB's [[tvb-multiscale]] framework or in other simulators like [[NEST]] or [[Brian2]]—morphological data provides constraints on neuronal properties. The morphometric profiles extracted by NeuroM can inform the distribution of parameters such as dendritic length and synaptic density across neuron populations.

Additionally, NeuroM contributes to the broader ecosystem of [[neuroinformatics]] tools that support reproducible neuroscience research, aligning with TVB's emphasis on open science and collaborative model development. NeuroM's output can be integrated with [[neuroml]]-based workflows, providing a standardized format for exchanging morphological data across simulation platforms [Shillcock et al., 2016].

## Key Papers

The primary citation for NeuroM is its Zenodo archive, which documents the software version and authorship [NeuroM Zenodo Archive, DOI: 10.5281/zenodo.597333]. NeuroM emerged from the Blue Brain Project's efforts to standardize morphological data analysis, as described in the workflow paper by Shillcock et al. (2016), which discusses the integration of NeuroM in the BigNeuron initiative for automated neuronal reconstruction and analysis [Shillcock et al., 2016, DOI: 10.1007/s40708-016-0041-7]. Users often cite NeuroM in combination with related tools like [[neuromorpho]] or [[neuroml]] when describing morphological analysis pipelines.

## Related Software

- [[neuromorpho]] — Database of neuronal morphologies
- [[neuroml]] — NeuroML standardized format for neuron models
- [[neuromorpho-toolkit]] — Morphological analysis toolkit for NeuroMorpho.org
- [[SWC]] — Common format for neuronal morphology data
- [[MorphIO]] — Library for reading/writing morphology files (used by NeuroM)
- [[LFPy]] — Python package for calculating local field potentials
- [[neuron]] — NEURON simulator for electrophysiological modeling

## References

- Blue Brain Project. (2024). Morphology Suite. NeuroM Documentation. https://neurom.readthedocs.io/
  
- NeuroM Zenodo Archive. (2024). NeuroM (Version v3.2.8). Blue Brain Project, EPFL. https://doi.org/10.5281/zenodo.597333

- Shillcock, J. C., Hawrylycz, M., Hill, S., & Peng, H. (2016). Reconstructing the brain: from image stacks to neuron synthesis. Brain Informatics, 3(4), 205–219. https://doi.org/10.1007/s40708-016-0041-7