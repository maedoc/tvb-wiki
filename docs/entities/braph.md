---
created: 2026-04-28
sources:
- raw/papers/mijalkov-2017-braph.md
- raw/papers/braph-2 genesis.md
- raw/papers/rubinov-sporns-2010.md
tags:
- software-brain-modeling
- connectomics
- brain-networks
- matlab-toolbox
- neuroimaging
title: BRAPH
type: entity
updated: '2026-04-30'
---

# BRAPH

## Overview

BRAPH (Brain Analysis of GRaphs) is an open-source MATLAB toolbox designed for the analysis of brain [[connectivity]] data. Originally developed by researchers in the connectomics field, BRAPH provides a comprehensive pipeline for constructing, analyzing, and visualizing brain networks derived from [[neuroimaging]] data. The software supports multiple neuroimaging modalities and implements a wide range of graph-theoretic measures for characterizing [[brain-network]] topology.

As a specialized tool in the brain connectivity analysis ecosystem, BRAPH enables researchers to perform end-to-end analysis of [[connectome]] data, from raw neuroimaging preprocessing through network construction and topological characterization. Its MATLAB foundation makes it accessible to researchers familiar with the dominant platform in neuroimaging research (Mijalkov et al., 2017).

## Motivation and Context

The development of BRAPH addressed a growing need in [[connectomics]] research for standardized, open-source tools capable of analyzing brain networks across multiple imaging modalities. Unlike commercial software with limited extensibility, BRAPH was designed from the ground up to support the specific workflows common in brain connectivity studies (Mijalkov et al., 2017).

The toolbox emerged alongside other important software in the field, including the [[brain-connectivity-toolbox]] (BCT) and [[conn]], but with a focus on providing a complete pipeline rather than individual analysis components. This integrated approach allows researchers to maintain consistent methodology throughout their analysis workflow, reducing the potential for errors that can arise when switching between different software packages.

BRAPH has proven particularly valuable for researchers studying neurological conditions where brain network topology is altered, including [[alzheimers-disease]], [[schizophrenia-models]], and various forms of [[epilepsy-modeling]]. The toolbox's standardized implementations of network metrics enable cross-study comparisons and meta-analyses (Mijalkov et al., 2017).

## BRAPH 2.0 and Genesis

The release of BRAPH 2.0 represented a major evolution of the original toolbox. This update introduced a redesigned architecture with enhanced capabilities for brain network analysis while maintaining backward compatibility with workflows developed in the original software (Mijalkov et al., 2021).

Key enhancements in BRAPH 2.0 include improved [[community-detection]] algorithms, better support for weighted network analysis, enhanced visualization capabilities, and a more flexible framework for extending the software's functionality. The 2.0 release also introduced better integration with standard neuroimaging file formats and preprocessing pipelines (Mijalkov et al., 2021).

The [[genesis]] version maintains BRAPH's commitment to open-source development, with the software continuing to be freely available to the research community. This approach aligns with broader trends in [[connectomics]] toward reproducible, transparent research practices.

## Key Features

BRAPH provides comprehensive support for brain connectivity analysis across several categories:

**Multimodal Data Support:** BRAPH supports analysis of brain networks derived from various neuroimaging modalities including [[fmri]] (functional magnetic resonance imaging), structural MRI, [[eeg]] (electroencephalography), and positron emission tomography (PET). This versatility enables researchers to perform both [[structural-connectivity]] analysis using diffusion imaging data and [[functional-connectivity]] analysis using resting-state fMRI or EEG recordings.

**Graph-Theoretic Metrics:** The toolbox implements a wide range of network analysis measures including [[small-world-networks]] properties (clustering coefficient, characteristic path length), [[modularity]] and community detection, [[network-hubs]] identification, centrality measures (betweenness, degree, eigenvector), and network efficiency metrics (Rubinov & Sporns, 2010).

**Brain [[parcellation]] Support:** BRAPH works seamlessly with various [[brain-parcellations]] schemes, from standard anatomical atlases to data-driven parcellations. This flexibility allows researchers to analyze brain networks at different scales of resolution.

**Visualization Tools:** The toolbox includes dedicated visualization capabilities for brain networks, enabling researchers to visualize network topology in both 2D and 3D representations overlaid on brain anatomy.

## Relationship to TVB

BRAPH occupies a complementary role in the [[whole-brain-modeling]] ecosystem relative to [[the-virtual-brain]] (TVB). While TVB focuses on **simulation** of brain network dynamics using [[neural-mass-models]] and [[whole-brain-modeling]] approaches, BRAPH focuses on **analysis** of empirical brain connectivity data.

Researchers often use BRAPH in conjunction with TVB for the following workflows:

* **Empirical Analysis:** BRAPH analyzes empirical [[structural-connectivity]] or [[functional-connectivity]] data to characterize the topological properties of individual brain networks.
* **Model Parameterization:** The graph-theoretic metrics computed by BRAPH inform parameter selection for TVB simulations, such as connection strengths and conduction delays.
* **[[model-validation]]:** TVB simulations produce synthetic functional connectivity data that can be compared against empirical networks analyzed with BRAPH, using metrics like small-world properties, [[modularity]], and hub statistics.

This complementary relationship makes the combination of BRAPH and TVB particularly powerful for studying structure-function relationships in the brain. Researchers can use BRAPH to characterize empirical brain networks and then use TVB to build computational models that reproduce observed topological features.

## Key Papers

The primary references for BRAPH are:

1. **Mijalkov et al. (2017)** — "BRAPH: A Pipeline for Brain Connectivity Analysis" — Frontiers in Neuroinformatics. This paper introduces the original BRAPH toolbox and describes its capabilities for brain network analysis.

2. **Mijalkov et al. (2021)** — "BRAPH 2.0 Genesis: An Open-Source Toolbox for Brain Connectivity Analysis" — Frontiers in Neuroinformatics. This paper describes the major update to BRAPH 2.0 with enhanced analysis capabilities.

3. **Rubinov & Sporns (2010)** — "Complex Network Measures of Brain Connectivity: Uses and Interpretations" — NeuroImage. This foundational paper provides the theoretical background for many graph-theoretic measures implemented in BRAPH.

## Related Software

- [[brain-connectivity-toolbox]] — MATLAB toolbox for graph-theoretic brain network analysis
- [[conn]] — MATLAB toolbox for connectivity analysis in fMRI data
- [[brainnet-viewer]] — Visualization software for brain networks
- [[graphvar]] — Graph-theoretic analysis toolbox for neuroimaging
- [[graph-tool]] — Open-source software for network analysis
- [[bctpy]] — Python bindings for the Brain Connectivity Toolbox
- [[nilearn]] — Python library for neuroimaging data analysis
- [[the-virtual-brain]] — [[whole-brain]] simulation platform