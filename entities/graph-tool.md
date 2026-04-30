---
created: 2025-01-15
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/wang-etal-2015-gretna.md
- raw/papers/mijalkov-2017-braph.md
tags:
- software-graph-tool
- network-analysis
- graph-theory
- python-library
- community-detection
- connectomics
title: Graph-tool
type: entity
updated: '2026-04-30'
---

Graph-tool is a Python library for the efficient analysis and manipulation of network structures (graphs). It provides a comprehensive set of algorithms for [[graph-theory|graph-theoretic]] analysis, including community detection, network statistics, flow optimization, and spectral methods. Written in C++ with Python bindings using Boost, graph-tool offers performance comparable to compiled languages while maintaining the accessibility of a Python interface peixoto2014. The library was developed and is maintained by Tiago de Paula Peixoto and has been a widely used tool in [[computational-neuroscience]], particularly for analyzing [[brain-connectivity-toolbox|brain connectivity networks]] derived from [[neuroimaging]] data.

## Overview

Graph-tool emerged from the need for a fast, flexible, and open-source tool for network analysis that could handle large-scale networks efficiently. Unlike pure-Python network libraries, graph-tool leverages the Boost Graph Library (BGL) for core data structures and algorithms peixoto2014, providing C++-level performance for computationally intensive operations. This makes it particularly valuable in neuroscience applications where brain networks can contain thousands of nodes (brain regions) and edges (structural or functional connections), requiring efficient algorithms for [[community-detection|community detection]], [[modularity|modularity optimization]], and other network metrics.

The library supports both directed and undirected graphs, multigraphs, and provides tools for network generation, visualization, and statistical analysis. Its architecture allows for flexible vertex and edge property maps, enabling researchers to associate arbitrary data with network elements—a feature particularly useful when working with weighted [[structural-connectivity|structural connectivity]] matrices or [[functional-connectivity|functional connectivity]] graphs from [[fmri|fMRI]] or [[eeg|EEG]] data.

## Key Features

Graph-tool offers an extensive repertoire of network analysis algorithms relevant to connectomics research. The library includes implementations of several [[community-detection|community detection]] algorithms. While the `graph_tool.community` module includes the Louvain method, the library's primary focus for community detection is on stochastic block models (SBMs), which provide a statistically principled approach to hierarchical community detection peixoto2017. Additional algorithms available include label propagation and spectral algorithms based on the modularity matrix. These are essential for identifying functional modules or structural cores in brain networks, such as the [[default-mode-network|default mode network]] or somatomotor systems.

The library provides efficient implementations of core network metrics including degree distribution, [[small‑world‑networks|small‑world]] properties, [[scale‑free‑networks|scale‑free]] degree exponents, [[rich‑club|rich‑club]] coefficients, and betweenness centrality. For flow‑based analysis, graph‑tool includes algorithms for maximum flow/minimum cut computations, which can be applied to analyze information transfer pathways in brain networks. The library also supports block‑model inference, a hierarchical approach to network analysis that can reveal multi‑scale community structure in cortical networks peixoto2014sbm.

Graph‑tool integrates with popular Python scientific computing stacks including NumPy and SciPy, allowing seamless integration with neuroimaging pipelines using [[nilearn|nilearn]] or [[nibabel|nibabel]] for processing [[dti|DTI]] tractography data or [[bold‑signal|BOLD]] time series.

## Relationship to TVB

While graph‑tool is not a core component of [[the‑virtual‑brain|The Virtual Brain]] (TVB) simulator, it serves as a complementary tool for preprocessing and analyzing brain networks that can be used as input to TVB models. Researchers analyzing [[whole‑brain‑modeling|whole‑brain models]] often use graph‑tool to characterize the topological properties of empirical structural [[connectome|connectomes]] (derived from [[diffusion‑imaging|diffusion imaging]] or [[tractography|tractography]]) before constructing large‑scale brain network models in TVB.

The library is frequently used in conjunction with [[brain‑connectivity‑toolbox|the Brain Connectivity Toolbox (BCT)]] and [[bctpy|its Python port (bctpy)]], with each tool offering complementary strengths rubinov2010. Graph‑tool provides strong performance for large networks due to its C++ backend, while BCT offers a more extensive collection of neuroscience‑specific metrics. In TVB workflows, graph‑tool can be used to compute network metrics for validation or to identify [[network‑hubs|network hubs]] that inform [[personalized‑brain‑modeling|personalized brain model]] parameters.

## Key Papers

- **Peixoto, T. P. (2014).** “The graph‑tool python library.” figshare. Dataset.
- **Peixoto, T. P. (2017).** “Uncovering the structure of sparse graphs via stochastic block models.” *Journal of Physics: Conference Series*, 760(1), 012001.
- **Peixoto, T. P. (2014).** “Hierarchical block structures and high‑resolution model selection in large networks.” *Physical Review X*, 4(1), 011047.

## Related Software

Graph‑tool occupies a specific niche in the network analysis ecosystem alongside several related tools. [[bctpy|The Brain Connectivity Toolbox]] (bctpy) provides a larger collection of neuroscience‑specific network metrics but runs slower than graph‑tool for large networks rubinov2010. [[braph|Braph]] offers a MATLAB‑compatible Python approach for brain network analysis with a focus on [[connectomics|connectomics]] workflows. [[gretna|GRETNA]] provides a graphical interface for network analysis focused on neuroimaging data. For general‑purpose network analysis beyond neuroscience, [[network‑dynamics]] offers a broader but slower pure‑Python implementation. For [[community‑detection|community detection]] specifically, the [[graphvar|GraphVar]] package integrates graph‑theoretic analysis with statistical testing for neuroimaging applications.

## References

1. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
2. Wang, J., Wang, X., Xia, M., Liao, X., Evans, A., & He, Y. (2015). *GRETNA: a graph theoretical network analysis toolbox for MATLAB*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2015.04.016)
3. (authors unknown). *BRAPH: A Pipeline for Brain Connectivity Analysis*.