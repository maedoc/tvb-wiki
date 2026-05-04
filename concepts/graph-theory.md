---
created: 2025-01-15
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/newman-2010.md
- raw/papers/bullmore-sporns-2009.md
- raw/papers/sporns-2011.md
- raw/papers/arxiv-2603.21067.md
- raw/papers/smith-2013-connectomics.md
tags:
- network-dynamics
- connectomics
- structural-connectivity
- functional-connectivity
- neuroimaging-fmri
- neuroimaging-dti
- software-brain-modeling
title: Graph Theory
type: concept
updated: '2026-05-04'
---

# Graph Theory

Graph theory provides a mathematical framework for describing and analyzing networks—collections of nodes (vertices) connected by edges (links). In neuroscience, graph theory has become essential for characterizing brain [[connectivity]], enabling researchers to move beyond qualitative descriptions toward quantitative, reproducible metrics of network organization. The framework treats brain regions or neurons as nodes and the connections between them as edges, allowing the application of a rich arsenal of mathematical tools developed across network science to problems in [[neuroimaging]] and connectomics.

## Motivation and Context

The application of graph theory to brain networks emerged from the convergence of several scientific developments. Advances in [[diffusion-mri]] and [[tractography]] made it possible to reconstruct structural connectivity matrices from white matter tract integrity, while [[resting-state]] [[fmri]] enabled the extraction of functional connectivity based on synchronized blood-oxygen-level-dependent signal fluctuations. Researchers recognized that these connectivity matrices could be treated as graphs, applying the same analytical tools used in social networks, transport systems, and the internet to the organization of the brain. The seminal work by [[ed-bullmore]] and [[olaf-sporns]] (2009) established the field's vocabulary, while the Brain Connectivity Toolbox introduced by Rubinov & Sporns (2010) provided standardized software implementation. This bridge between network science and neuroscience proved remarkably fruitful, revealing that brain networks exhibit properties like small-world topology, modular organization, and hub nodes that are critical for understanding cognitive function and dysfunction.

## Graph Components and Types

A brain graph consists of **nodes** representing brain regions (defined by [[parcellation]] atlases such as Desikan-Killiany or Glasser) and **edges** representing either structural connections derived from [[diffusion-mri]] tractography or functional connections derived from statistical dependencies in [[fmri]], [[eeg]], or [[meg]] time series. Edges may be weighted (reflecting connection strength or probability) or binary (indicating presence or absence), and they may be directed (when causality can be inferred, as in [[effective-connectivity]] analysis) or undirected (when only correlation is available). The choice between these representations significantly affects the resulting network metrics; weighted networks preserve more information but introduce additional complexity in interpretation, while binary networks enable clearer comparisons but discard important gradient information about connection strength.

## Network Analysis Metrics

Graph theory provides both local measures characterizing individual nodes and global measures describing overall network organization. **Node degree**—the number of connections incident upon a node—provides the most basic characterization of regional importance, while **clustering coefficient** quantifies the density of connections among a node's neighbors, reflecting the tendency for brain regions to form functional modules. **Betweenness centrality** identifies nodes that serve as critical bridges in information transfer, while **global efficiency** (the inverse of the average shortest path length) measures how easily information can travel across the network. **Modularity** quantifies the strength of community structure, identifying groups of nodes that are densely connected internally but sparsely connected to other groups. Together, these metrics reveal that the brain exhibits small-world properties (high clustering combined with short path lengths), rich-club organization (dense connectivity among highly connected hubs), and hierarchical structure spanning multiple spatial scales.

## Brain Network Applications

Graph theoretical analysis has been applied to both **[[structural-connectivity]]** networks derived from diffusion imaging and **[[functional-connectivity]]** networks derived from resting-state or task-based [[fmri]]. Structural networks reveal the anatomical substrate of brain organization, while functional networks capture dynamic coordination patterns that emerge from this anatomy. The comparison of structural and functional networks has revealed both correspondence (areas that are structurally connected tend to be functionally coupled) and interesting divergences (areas that are not structurally connected may exhibit strong functional coupling through polysynaptic pathways). Recent work has extended graph analysis to dynamic functional connectivity, examining how network properties change over time and across cognitive states, providing insight into the flexible reconfiguration of brain networks supporting cognition.

## Software Tools

The analysis of brain networks relies on specialized software packages. The [[brain-connectivity-toolbox]] (BCT), developed by Rubinov and Sporns, provides the most comprehensive MATLAB implementation of network metrics and has become the field's standard reference implementation. Python alternatives include the `networkx` library for general network analysis and `igraph` (available in R and Python bindings), while the `[[bctpy]]` package provides Python bindings for the BCT functions. These tools enable researchers to compute the full range of network metrics, perform null model comparisons, and assess statistical significance across group analyses.

## Related Concepts

Graph theory forms the mathematical foundation for [[connectomics]], the comprehensive study of brain connectivity. The framework connects directly to [[brain-network]] analysis and [[network-hubs]] identification. The small-world property is characterized by the σ metric comparing clustering and path length to random networks. Similar concepts include [[modularity]] for community detection and [[rich-club]] for analyzing connectivity among highly connected nodes. Graph theoretical analysis also relates to [[network-dynamics]], which examines how network structure constrains and enables dynamic processes in neural systems.

## References

1. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
2. (authors unknown). *Networks: An Introduction*.
3. (authors unknown). *Complex Brain Networks: Graph Theoretical Analysis of Structural and Functional Systems*.
4. (authors unknown). *Networks of the Brain*.
5. Sakul Mahat, Sharmistha Guha, Jessica Bernard. (2026). *A Bayesian Framework for Quantifying Association Between Functional and Structural Data in Neuroimaging*. [Link](https://arxiv.org/abs/2603.21067)
6. (authors unknown). *Functional Connectomics from Resting-State fMRI*.