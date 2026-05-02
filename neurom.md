---
title: NeuroM
created: 2024-01-15
updated: 2026-05-02
type: entity
tags: [software-neurom, neural-morphology, neuronal-morphology, software-visualization, connectomics, neuroanatomy, python-toolbox, computational-neuroscience]
sources:
  - https://github.com/BlueBrain/NeuroM
  - https://neurom.readthedocs.io/en/stable/
  - https://www.ebrains.eu/tools/neurom-2
  - https://github.com/BlueBrain/MorphIO
  - https://portal.bluebrain.epfl.ch/resources/software/morphology-suite/
---

## Overview

NeuroM is an open-source Python toolbox designed for the analysis and processing of neuronal morphologies—three-dimensional reconstructions of neuronal structure including dendritic arbors, axonal projections, and somatic geometries [[1]](https://doi.org/10.5281/zenodo.597333). Originally developed as part of the Blue Brain Project at EPFL (École Polytechnique Fédérale de Lausanne), NeuroM provides a standardized interface for reading, writing, and quantitatively analyzing morphological data from various file formats (SWC, ASC, H5), making it an essential tool in [[computational-neuroscience]] workflows that involve detailed single-neuron modeling. The software enables researchers to extract morphometric features—such as branch order distributions, tortuosity metrics, and total dendritic length—that are crucial for building biophysically realistic [[spiking-neural-networks]] and validating [[neural-mass-models]] against empirical data.

## Motivation and Context

The characterization of neuronal morphology has become increasingly important in the era of large-scale brain initiatives and [[connectome]] mapping projects [[2]](https://link.springer.com/content/pdf/10.1007/s40708-016-0041-7). Traditionally, neuronal morphologies were analyzed using labor-intensive manual methods or proprietary software packages that lacked interoperability. NeuroM emerged to address this fragmentation by providing a unified, programmable interface that can handle diverse morphology file formats and extract quantitative descriptors in a reproducible manner. This capability is particularly relevant for [[whole-brain-modeling]] efforts like [[the-virtual-brain]], where region-specific neural populations require accurate morphometric parameters to calibrate [[neural-mass-models]] and establish proper [[excitation-inhibition-balance]]. By enabling automated morphometric analysis at scale, NeuroM facilitates the construction of data-driven brain models that respect the anatomical diversity observed in empirical measurements.

## Key Features

NeuroM offers several core functionalities that distinguish it from general-purpose visualization tools. First, the toolbox provides robust file format handling through pluggable readers that support SWC (a de facto standard for morphology data), ASC (Neurolucida format), and HDF5-based morphology files compatible with the [[neurodata-without-borders]] (NWB) standard. Second, its morphometric extraction capabilities include measurements such as total cable length, number of branches, branch angle distributions, and bifurcation asymmetry—quantities that inform parameter selection in neural simulation engines like [[brian]], [[nest]], and [[neuron]]. Third, NeuroM includes visualization routines for rendering neuronal reconstructions in three dimensions, which is valuable for quality control and for generating figures in publications. Finally, the toolbox supports statistical aggregation across populations of neurons, enabling researchers to compute population-level distributions of morphometric features that can be used to constrain [[network-dynamics]] models.

## Relationship to TVB

While [[the-virtual-brain]] (TVB) operates primarily at the level of [[whole-brain]] network dynamics and does not directly simulate individual neuronal morphologies, NeuroM complements TVB in several important ways. TVB's population-level models require anatomical priors—including regional volumes, connectivity weights, and delays—that can be informed by morphometric data processed through NeuroM. For example, when constructing TVB's [[neural-mass-model]] instances, the aggregate dendritic length and branching statistics of neurons in each brain region can be used to tune mean-field coupling parameters. Moreover, for TVB's epilepsy modeling applications (see [[epilepsy-modeling]]), the detailed morphology of specific neuronal subtypes (e.g., pyramidal cells versus interneurons) influences the excitability parameters fed into the [[epileptor]] model. NeuroM thus serves as an upstream processing tool that bridges empirical morphological data and the phenomenological models employed in TVB simulations.

## Key Papers

The primary reference for NeuroM is its software repository with archived releases on Zenodo [[1]](https://doi.org/10.5281/zenodo.597333). The NeuroM GitHub repository provides the canonical source code and release history, documenting all versions including the current major version v3 (released in 2021) which introduced major refactoring including renaming all "neuron" classes to "morphology" classes for consistency with the broader Neuroinformatics community [[3]](https://neurom.readthedocs.io/en/stable/migration.html). Version v4 was released in 2024, marking MorphIO as a required dependency and transitioning NeuroM to use MorphIO objects via composition rather than inheritance.

NeuroM is part of the broader Blue Brain Project morphology tooling ecosystem, which includes related tools for morphology repair (NeuroR), synthesis (NeuroTS), and visualization (NeuroMorphoVis) [[4]](https://portal.bluebrain.epfl.ch/resources/software/morphology-suite/). For context on neuronal morphology analysis in computational neuroscience, see also the review on morphometric analysis tools [[2]](https://link.springer.com/content/pdf/10.1007/s40708-016-0041-7).

## Architecture and Version History

NeuroM v3 represented a significant architectural shift, migrating from a custom morphology reader to dependence on [[MorphIO]] for underlying file I/O operations. MorphIO is a C++ and Python library developed by the Blue Brain Project that provides robust, validated reading and writing of morphology files in SWC, ASC, and H5 formats. This migration improved compatibility with the NeuroData Without Borders (NWB) standard and reduced code duplication across the Blue Brain morphology tooling ecosystem.

The v4 series (current as of 2025) introduced breaking changes including requiring MorphIO objects rather than file paths to be passed to the Morphology class, and replacing iterator methods with properties for improved performance. These changes reflect the maturation of the tool from a research prototype to a production-grade component used in EBRAINS Cellular Level Simulation Platform workflows.

## Related Software

- [[the-virtual-brain]] — Whole-brain modeling platform that uses morphometric features to calibrate neural mass models
- [[brian]] — Spiking neural network simulator that can utilize morphology-derived parameters
- [[neuron]] — NEURON environment for detailed neuronal simulations with morphologically realistic cells
- [[nest]] — Neural simulation tool for large-scale spiking network simulations
- [[neuroml]] — NeuroML standard for exchanging neuronal and network specifications
- [[neurodata-without-borders]] — NWB standard for neurophysiology data including morphology
- [[morphio]] — C++ and Python library for reading and writing neuronal morphology files, upon which NeuroM v3+ depends
- [[neuror]] — Blue Brain tool for repairing and curating morphology reconstructions
- [[neurots]] — Blue Brain tool for synthesizing neuronal morphologies based on statistical profiles

## References

[1] Blue Brain Project. (2024). *NeuroM* (Version v4.0.4) [Software]. Zenodo. https://doi.org/10.5281/zenodo.597333

[2] Shillcock, J.C., Hawrylycz, M., Hill, S., & Peng, H. (2016). Reconstructing the brain: from image stacks to neuron synthesis. *Brain Informatics*, 3(4), 205-209. https://doi.org/10.1007/s40708-016-0041-7

[3] NeuroM Documentation. (2024). *Migration to v3 version*. https://neurom.readthedocs.io/en/stable/migration.html

[4] Blue Brain Project. (2024). *Morphology Suite*. EPFL. https://portal.bluebrain.epfl.ch/resources/software/morphology-suite/