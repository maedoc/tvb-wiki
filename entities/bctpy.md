---
created: 2025-01-15
sources:
- https://github.com/aestrivex/bctpy
- https://doi.org/10.1016/j.neuroimage.2010.07.033
- https://doi.org/10.1038/nrn2576
- raw/papers/sanz-leon-2013.md
- raw/papers/rubinov-sporns-2010.md
- raw/papers/ritter-2013.md
tags:
- software-bct
- software-graph-tool
- connectomics
- network-dynamics
- graph-theory
title: BCTpy
type: entity
updated: '2026-04-29'
---

## Overview

BCTpy (Brain Connectivity Toolbox in Python) is the Python implementation of the widely-used Brain Connectivity Toolbox (BCT), originally developed in MATLAB by Olaf Sporns and colleagues at the Institute for Neuroinformatics. It provides a comprehensive set of algorithms for analyzing structural and functional brain networks derived from neuroimaging data, including [[dti]] tractography, [[fmri]], [[eeg]], and [[meg]] measurements. The library implements metrics from [[graph-theory]] and [[network-dynamics]] that characterize topological properties of brain networks, enabling researchers to quantify [[small-world-networks]], [[modularity]], [[community-detection]], [[rich-club]] organization, and other network phenomena central to [[connectomics]] research.

The Python version emerged to address the growing need for open-source, scriptable network analysis tools compatible with modern neuroimaging workflows in Python. Unlike GUI-based analysis packages, BCTpy operates as a library of functions that can be integrated into automated processing pipelines, making it particularly valuable for [[reproducibility]] in large-scale studies such as the [[human-connectome-project]] and [[uk-biobank]].

## Key Features

BCTpy implements a comprehensive set of network analysis functions spanning several categories of graph-theoretic metrics (Rubinov & Sporns, 2010). **Node centrality metrics** include degree, strength, betweenness centrality, and eigenvector centrality, which identify [[network-hubs]] and influential brain regions. **Path-based metrics** compute characteristic path length, efficiency, and radius, quantifying how quickly information can travel between regions. **Clustering and community metrics** calculate clustering coefficient, transitivity, and provide implementations of modularity optimization algorithms (including Louvain and spectral partitioning) for detecting [[brain-parcellations]] and functional modules. PageRank centrality is also implemented for identifying important nodes based on network [[connectivity]] patterns.

The library excels at **network comparison** functionality, implementing null model generation (graph-theoretic [[random-networks]], configuration models), network-based statistic for mass-univariate testing, and methods for comparing [[structural-connectivity]] to [[functional-connectivity]] matrices (Zalesky et al., 2010). **Regional features** can be computed for parcellated brains, including node degree distribution analysis, hub identification, and participation coefficient calculation that quantifies how regions integrate information across modules. Additional features include simulation of network growth models ([[preferential-attachment]], duplication-divergence), analysis of motifs and subgraphs, and handling of weighted, directed, and bipartite networks.

## Relationship to TVB

BCTpy interfaces naturally with [[the-virtual-brain]] (TVB), a [[whole-brain-modeling]] simulator that uses anatomical connectomes to constrain large-scale network dynamics. TVB's connectivity matrices—typically derived from [[diffusion-imaging]] tractography—can be directly analyzed using BCTpy to extract graph-theoretic features that inform parameter choices or validate model substrates. Conversely, TVB simulation outputs (time series of regional activity) can be processed through BCTpy's functional connectivity estimators to compare simulated dynamics against empirical [[resting-state]] networks.

In practice, many TVB users employ BCTpy in their preprocessing pipeline: computing the structural [[small-world-networks]] properties of the empirical [[connectome]], identifying hub regions for model parameterization, and comparing simulated versus empirical network topology. The combination of BCTpy's topological analysis with TVB's biophysically-grounded simulations enables researchers to bridge the gap between anatomical structure and functional dynamics in [[personalized-brain-modeling]] frameworks.

## Key Papers

The seminal BCT paper by Rubinov and Sporns (2010), published in NeuroImage, established the original MATLAB toolbox and remains the foundational reference for network neuroscience methodology. This paper comprehensively describes the network analysis metrics implemented in both the original BCT and its Python derivative, and it has become one of the most cited works in connectomics (over 10,000 citations). Users of BCTpy should cite this work when applying the toolbox's metrics to their analyses.

For background on the broader field of [[brain-network]] analysis, the review by Bullmore and Sporns (2009) provides essential context on graph theoretical approaches to brain connectivity. This article established the theoretical foundations for analyzing complex brain networks and introduced many of the key concepts (small-worldness, modularity, hub architecture) that BCTpy enables researchers to quantify empirically.

The network-based statistic (NBS) method introduced by Zalesky et al. (2010) provides the statistical framework for controlling family-wise error rate in mass-univariate comparisons of brain networks—a capability directly implemented in BCTpy's network comparison functions. This methodological advance is essential for conducting group-level analyses of structural and functional connectivity differences.

## Related Software

BCTpy occupies a niche in the Python ecosystem for brain network analysis, complementing rather than replacing other graph analysis libraries. [[graph-tool]] provides a more general-purpose network analysis library with highly optimized C++ backends, suitable for very large networks but requiring more specialized knowledge. [[braph]] offers a MATLAB-friendly alternative with GUI components. For connectome-specific workflows, the [[brainspace]] library implements complementary dimensionality reduction and manifold learning approaches, while the Connectome Mapper Toolkit ([[connectome-mapper-3]]) provides end-to-end preprocessing pipelines that can export to BCTpy format. Whole-brain simulators like [[the-virtual-brain]] and neural simulation environments such as [[nest]] frequently employ BCTpy for network analysis of their outputs.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
3. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal [[neuroimaging]]*. Brain Connectivity. [DOI](https://doi.org/10.1089/brain.2012.0120)