---
created: 2026-05-04
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-9552467d25c9.md
- raw/papers/semanticscholar-9e0528124f6e.md
- raw/papers/semanticscholar-ce1b27301b4d.md
- raw/papers/semanticscholar-929b90566fc8.md
tags:
- software-brain-modeling
title: CCEytools
type: entity
updated: '2026-05-11'
---

# CCEytools

**Note:** This entry appears to have been created as a placeholder for Python-based brain [[connectivity]] and modeling tools. No standalone tool called "CCEytools" specifically exists in the literature; however, this entry serves as a reference point for the ecosystem of Python packages used for brain connectivity analysis, neural signal processing, and [[whole-brain|whole-brain modeling]] in the TVB community.

## Overview

CCEytools represents (or perhaps was intended to represent) a category of Python-based computational tools for analyzing brain connectivity and dynamical systems in the context of whole-brain modeling. The name may have been inspired by similar toolkits in the field—combining "CC" (possibly referring to connectivity or cortico-cortical) with "Ey" (possibly a partial derivation from Python or "analysis") and "tools" to denote a software package. Within the [[tvb|The Virtual Brain]] and broader [[connectomics]] ecosystems, researchers frequently assemble toolchains from multiple Python packages rather than relying on a single monolithic application.

The Python ecosystem for brain connectivity analysis has matured considerably, with packages like [[nilearn]] providing interfaces for [[neuroimaging]] data handling, and [[bctpy]] implementing graph-theoretical network metrics.

## Relationship to TVB

[[the-virtual-brain]] (TVB) is a comprehensive platform for whole-brain modeling that integrates [[structural-connectivity]] derived from [[diffusion-imaging]] with [[neural-mass-models]] to simulate [[brain-dynamics]]. While TVB provides its own built-in analysis tools through the [[tvb-library]], researchers often complement TVB workflows with external Python packages for specialized tasks such as:

- Preprocessing of neuroimaging data using packages like [[mne-python]] for [[electrophysiology]]
- Advanced connectivity metrics unavailable in TVB's core distribution
- Graph-theoretical analyses using [[bctpy]] or similar packages
- Connectivity-based [[parcellation]] using Nilearn functionality
- Source reconstruction and beamforming for M/EEG data

The term "CCEytools" may have emerged from discussions about external Python tools to augment TVB's native capabilities, though no single unified package by that exact name was ever developed or released.

## Key Related Python Packages

### Connectivity Analysis

Several dedicated packages exist for computing functional and [[effective-connectivity]] from neuroimaging data:

- **[[mne-connectivity]]** (extends Mne Python): Provides connectivity measures including coherence, phase locking value, amplitude envelope correlation, and granger causality for MEG, EEG, and iEEG data.

- **[[graphvar]]**: Offers graph-theoretical network analysis with a focus on connectivity matrices and their topological properties, useful for analyzing [[resting-state]] networks derived from TVB simulations.

- **EEGraph**: A Python library for modeling EEG data as graphs with various connectivity measures including cross-correlation, Pearson correlation, coherence, and directed transfer function.

- **Neuropycon/ephypype**: Provides pipelines for electrophysiology connectivity analysis, integrated with [[nipype]] for workflow management.

### Structural Connectivity and Network Analysis

- **[[bctpy]]**: The Brain Connectivity Toolbox ported to Python, offering over 200 network metrics including degree distribution, betweenness centrality, [[modularity]], and [[rich-club]] coefficients.

- **[[dipy]]**: Comprehensive diffusion imaging processing library that includes [[tractography]] algorithms essential for deriving structural connectivity matrices used as TVB input.

- **[[mrtrix3]]**: Advanced [[diffusion-mri]] analysis suite with tractography capabilities.

### Connectome Embedding and Advanced Methods

- **Cepy** ([[connectome]] embedding): Implementation of the connectome embedding (CE) framework that learns vector representations of brain regions capturing higher-order topological relationships.

- **[[brainspace]]**: Implements representations of [[brain-network]] data through manifold learning and alignment techniques.

### General Neuroimaging Utilities

- **Nilearn**: Provides easy access to neuroimaging data formats, mass-univariate analysis, and [[machine-learning]] pipelines for brain data.

- **Mne Python**: The foundational package for electrophysiology data analysis, including preprocessing, source estimation, and time-frequency analysis.

- **[[nitime]]**: Time-series analysis library specifically designed for neuroscience data.

## Key Papers and Methods

Several foundational publications describe the methods implemented in these tools:

The work on connectome embedding by Rosenthal et al. (2018) demonstrated how embedded vector representations of connectomes can reveal higher-order structure-function relationships. This method, implemented in Cepy, provides an approach complementary to TVB's own connectivity analyses.

The canonical paper by Bastos and Schoffelen (2016) provides a critical review of [[functional-connectivity]] measures and their interpretation, offering guidance on when to use directed versus undirected measures—knowledge that informs proper tool selection.

For graph-theoretical approaches, Rubinov and Sporns (2010) established the foundational network metrics now implemented in [[bctpy]] and used throughout the connectomics field.

## Usage in Whole-Brain Modeling Workflow

A typical research workflow combining TVB with external connectivity tools might proceed as follows:

First, structural connectivity is derived from diffusion-weighted MRI using Mrtrix3 or Dipy, producing fiber tracts that are segmented using a parcellation atlas such as [[desikan-killiany-atlas]] or [[schaefer-atlas]]. This yields a connectivity matrix representing [[white-matter]] streamline counts between brain regions.

Next, TVB uses this structural connectivity matrix to configure whole-brain simulations using neural mass models such as the [[jansen-rit-model]] or [[wong-wang-model]]. The simulated dynamics can then be analyzed using external tools to compute functional connectivity matrices from the simulated time series.

Finally, graph-theoretical analyses via [[bctpy]] can characterize the emergent network topology, while connectivity tools enable comparison with empirically observed connectivity patterns. These cross-tool analyses help validate whole-brain models and identify where simulated dynamics diverge from empirical observations.

## Related Software Entities

- [[the-virtual-brain]] — Primary whole-brain simulation platform
- Mne Python — Electrophysiology analysis foundation
- Nilearn — Neuroimaging data handling
- [[bctpy]] — Graph-theoretical network analysis
- [[brain-connectivity-toolbox]] — Original MATLAB network toolbox
- [[nest]] — Neural simulator for detailed spiking network models
- [[epilepsy-modeling]] — Clinical applications of whole-brain modeling
- [[personalized-brain-modeling]] — Individualized brain models in TVB

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))