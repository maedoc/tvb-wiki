---
title: NeuroM
created: 2025-01-15
updated: 2026-05-02
type: entity
tags: [software-neurom, software-visualization, neural-morphology, morphological-analysis, computational-neuroscience, python-tools]
sources:
  - "[NeuroM on Zenodo, Blue Brain Project EPFL](https://doi.org/10.5281/zenodo.597333)"
  - "[NeuroM GitHub Repository](https://github.com/BlueBrain/NeuroM)"
  - "[Computational Tools for Neuronal Morphometric Analysis: A Systematic Search and Review, Leite et al. 2024](https://doi.org/10.1007/s12021-024-09674-6)"
---

## Overview

NeuroM is an open-source Python library for the automated analysis and visualization of neuronal morphologies, designed to extract quantitative morphometric features from three-dimensional reconstructions of neurons. Developed by the Blue Brain Project at EPFL (École polytechnique fédérale de Lausanne), NeuroM provides a standardized framework for processing morphological data in the SWC file format (the de facto standard for neuronal reconstructions) and other common morphology formats such as ASC [[sources/0]].

## Motivation and Context

The field of neuronal morphology analysis has historically suffered from fragmented toolchains and inconsistent feature definitions across different research groups. Before NeuroM's development in the mid-2010s, researchers studying neuronal anatomy often relied on custom scripts or commercial software with limited accessibility and reproducibility. NeuroM emerged to address this methodological gap by providing a well-documented, rigorously tested, and extensible Python package that implements standardized morphometric algorithms [[sources/1]].

The tool fits within the broader ecosystem of [[connectomics]] and [[neural-mass-models]] research, where morphological data from different brain regions and cell types must be systematically characterized to parameterize biologically realistic models. NeuroM also addresses the growing need for quantitative comparisons across datasets, enabling statistical analyses of morphological differences between neuron types, brain regions, or experimental conditions [[sources/2]].

## Key Features

NeuroM provides an extensive suite of morphometric analysis capabilities organized into functional modules. The **soma analysis** component extracts fundamental properties including soma volume, surface area, and circularity, which are critical for distinguishing between neuronal subclasses. The **dendrite analysis** module computes branching metrics such as total dendritic length, branch order distributions, bifurcation angles, and the classical Sholl analysis profile, which quantifies the spatial complexity of axonal and dendritic arbors [[sources/0]].

NeuroM implements the Euclidean distance metric for computing fiber lengths, along with the ability to distinguish between different compartments (axon versus basal versus apical dendrites) based on SWC point type annotations. The software also supports **Tortuosity** calculations, measuring how much actual path length deviates from straight-line Euclidean distance—a morphometric feature relevant to signal conduction properties.

A particularly notable capability is NeuroM's **feature extraction pipeline**, which can process large batches of morphology files and generate summary statistics across populations. The package includes visualization utilities for rendering three-dimensional reconstructions with color-coded compartment types and diameter scaling, facilitating the generation of publication-quality figures. NeuroM follows a modular architecture allowing researchers to extend functionality through custom analysis plugins, and its command-line interface enables integration into larger neuroimaging processing pipelines [[sources/1]].

## Relationship to TVB

While NeuroM is not directly integrated into [[the-virtual-brain]] as a core component, it serves a complementary role in the broader whole-brain modeling ecosystem by providing the morphological data needed to constrain biologically detailed neuron models. [[the-virtual-brain]] operates primarily at the level of neural mass models and mean-field approximations, where the detailed morphological features extracted by NeuroM can inform the parameterization of dendritic delay distributions and synaptic integration properties. In personalized brain modeling workflows, NeuroM can be used to analyze morphological data from specific patients or subject populations, providing evidence-based constraints for [[personalized-brain-modeling]] applications. The morphological metrics produced by NeuroM are also compatible with [[neuroml]], providing a pathway to translate empirical morphology data into standardized specifications for large-scale network simulations.

## Key Papers

The primary citation for NeuroM is the software release archived on Zenodo by the Blue Brain Project at EPFL (2015-2024), which describes the package architecture and validation against established morphometric methods [[sources/0]]. Additional methodological references include works applying NeuroM to specific neuronal populations, demonstrating its utility in comparative morphological studies across brain regions and species. A systematic review of computational tools for neuronal morphometric analysis identified NeuroM as one of the three tools extracting the most features, alongside L-Measure and NeuroMorphoVis [[sources/2]]. The software has been employed in studies investigating structural plasticity, dendritic remodeling, and the relationship between morphology and electrophysiological properties.

## Related Software

NeuroM frequently appears in workflows alongside several other tools in the computational neuroscience ecosystem. Researchers often combine NeuroM with [[neuromorpho]] for accessing large-scale morphology databases, [[brainrender]] for visualization, [[neuron]] for biophysically detailed simulations, and [[neuroml]] for standardizing model specifications. The software is also compatible with [[bindsnet]] for spiking neural network construction and can interface with [[pycortex]] for cortical geometry handling. Other relevant tools include [[bluepyopt]] for neuron model optimization, [[lfpy]] for local field potential computations, and the [[brain-connectivity-toolkit]] for network-level analyses of morphological data. NeuroM is often used alongside [[the-virtual-brain]] in whole-brain modeling pipelines.

## References

- Blue Brain Project, EPFL. (2015-2024). *NeuroM* (Version 3.2.8) [Software]. Zenodo. https://doi.org/10.5281/zenodo.597333
- Leite, J., Nhoatto, F., Jacob Jr., A., Santana, R., & Lobato, F. (2024). Computational Tools for Neuronal Morphometric Analysis: A Systematic Search and Review. *Neuroinformatics*, 22, 353-377. https://doi.org/10.1007/s12021-024-09674-6
- Torben-Nielsen, B. (2014). An efficient and extendable Python library to analyze neuronal morphologies. *Neuroinformatics*, 12(4), 499-500. https://doi.org/10.1007/s12021-014-9232-7