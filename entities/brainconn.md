---
created: 2026-05-13
sources:
- raw/papers/woodman-2014.md
tags:
- software-brain-modeling
- connectomics
- graph-theory
- network-dynamics
- structural-connectivity
- functional-connectivity
title: Brainconn
type: entity
updated: '2026-05-18'
---

**Brainconn** is an open-source Python package for graph-theoretical analysis of brain connectivity data. It provides a comprehensive suite of algorithms for computing network metrics on anatomical and functional brain networks, porting the widely-used [[brain-connectivity-toolbox]] (BCT) from MATLAB into idiomatic Python with NumPy and SciPy integration. The package enables researchers to characterize the topological organization of brain [[connectome]] data across scales, from single-subject [[structural-connectivity]] matrices to group-level [[functional-connectivity]] networks.

## Motivation and Context

The computational analysis of brain networks has become a central methodology in [[connectomics]], driven by the recognition that cognition, development, and disease are reflected in the large-scale [[network-dynamics]] of the brain. The [[brain-connectivity-toolbox]], originally developed in MATLAB by Rubinov and Sporns (2010), established a de facto standard for graph-theoretic analysis in neuroscience, with over 100 implementations of network metrics ranging from basic degree distributions to sophisticated [[community-detection]] algorithms and null-model generation. However, as the Python scientific computing ecosystem matured — with tools like [[dipy]] for [[diffusion-imaging]], [[nilearn]] for fMRI analysis, and [[the-virtual-brain]] for [[whole-brain-modeling]] — the need for a native Python implementation that could interoperate seamlessly with these tools became pressing.

Brainconn addresses this gap by providing a clean, dependency-light Python reimplementation of the core BCT algorithms. Unlike earlier efforts such as [[bctpy]], which attempted a more literal line-by-line translation, Brainconn emphasizes idiomatic Python design patterns, vectorised NumPy operations, and an API that integrates naturally with the PyData stack. This makes it particularly useful in research pipelines that combine network analysis with other Python-based [[neuroimaging]] or simulation tools, reducing the friction of switching between MATLAB and Python environments.

## Key Features

Brainconn implements network analysis functions across the major categories defined by [[graph-theory]]. **Node-level metrics** include degree (binary and weighted), betweenness centrality, eigenvector centrality, clustering coefficient, and participation coefficient — measures that identify [[network-hubs]], connector regions, and locally segregated processing clusters. **Global metrics** include characteristic path length, global and local efficiency, transitivity, and [[small-world-networks]] indices, which together quantify the brain's capacity for integrated and segregated information processing. **Community structure** is supported via modularity maximisation algorithms (Louvain and Newman-type spectral partitioning), enabling the identification of functional modules and [[brain-parcellations]] in connectivity data.

A distinctive strength of Brainconn is its unified handling of **weighted, directed, and signed networks**. Many brain connectivity analyses involve correlation matrices with both positive and negative values (e.g., [[functional-connectivity]] from [[resting-state]] [[fmri]]), and Brainconn provides appropriate normalisation schemes and distance transformations for each case. The package also includes null-model generation (random, lattice, and configuration-model surrogates) for statistical testing, and support for basic network comparison via measures such as Jaccard similarity and network-based overlap. All functions accept NumPy arrays as input and return standard NumPy types, making outputs immediately compatible with matplotlib visualisation, scipy statistical testing, and machine-learning pipelines built with [[nilearn]].

## Relationship to TVB

Brainconn occupies a natural position in the [[whole-brain-modeling]] workflow centered on [[the-virtual-brain]] (TVB). TVB simulations are built upon subject-specific [[structural-connectivity]] matrices, typically derived from [[diffusion-imaging]] and [[tractography]]. Before these matrices enter a TVB simulation, researchers often use Brainconn to compute their graph-theoretic properties — small-worldness, modular structure, hub architecture — as a quality-control step and to inform model parameterisation. For instance, regions identified by Brainconn as structural hubs may receive distinct local dynamics or coupling parameters in the neural mass model.

After simulation, TVB outputs time series of regional neural activity. This can be fed directly into Brainconn to compute simulated [[functional-connectivity]] matrices and their graph-theoretic properties, enabling quantitative comparison against empirical data from [[eeg]], [[meg]], or [[fmri]]. This structure-to-function validation loop — structural network analysis with Brainconn, simulation with TVB, functional network analysis again with Brainconn — is a standard pattern in [[personalized-brain-modeling]] studies and in computational investigations of brain disorders such as [[epilepsy-modeling]] and [[alzheimers-modeling]].

## Comparison to Related Tools

Brainconn sits amid a growing ecosystem of Python tools for brain network analysis. The original [[brain-connectivity-toolbox]] remains the gold standard for MATLAB users, and [[bctpy]] provides a direct Python port of that codebase, but both retain design decisions tied to the original MATLAB implementation. [[braph]] offers a MATLAB-based alternative with a graphical user interface and additional features for multilayer and temporal networks, but is tightly coupled to its own data structures. The [[graphvar]] toolbox extends graph-theoretic analysis into the domain of brain-behaviour correlations and dynamic connectivity, providing statistical frameworks that complement Brainconn's library-style approach. For large-scale networks exceeding ~10,000 nodes, general-purpose graph libraries such as [[pybraingraph]] and [[graph-tool]] offer C++-backed performance, though they lack the domain-specific normalisation and null-model construction designed specifically for neuroimaging data. Brainconn's niche is its balance of domain specificity, Python-native design, and easy interoperability with the broader [[whole-brain-modeling]] software stack.

## References

1. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain [[connectivity]]*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))