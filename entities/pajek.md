---
created: 2024-01-15
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/bullmore-sporns-2009.md
- raw/papers/semanticscholar-d45f5742871a.md
tags:
- software-visualization
- graph-theory
- community-detection
- network-dynamics
- connectomics
- structural-connectivity
- functional-connectivity
- small-world-networks
- modularity
title: Pajek
type: entity
updated: '2026-05-04'
---

# Pajek

## Overview

**Pajek** (Slovene for "spider") is a widely-used network analysis software package designed for the analysis and visualization of large-scale networks and complex graphs. Originally developed by Vladimir Batagelj and Andrej Mrvar at the University of Ljubljana [@Batagelj1998], Pajek provides a comprehensive suite of tools for extracting, analyzing, and visualizing various types of network structures, making it an essential tool in the field of [[connectomics]] where brain connectivity data is represented as graph-based representations of [[structural-connectivity]] and [[functional-connectivity]] [@Bullmore2011]. The software handles networks with millions of vertices and edges efficiently, which is particularly important when working with whole-brain connectivity matrices derived from [[neuromorpho-toolkit|diffusion imaging]] or [[resting-state]] [[fMRI]] data. Pajek operates as free academic software and has become a standard tool in the network neuroscience community, with applications ranging from [[community-detection]] to [[network-hubs|hub identification]] in brain networks.

Pajek operates primarily through a graphical user interface (GUI), though batch processing capabilities exist via scripts for automated workflows. The software supports multiple native file formats: the `.net` format (also known as Pajek NET) for edge lists with vertex attributes, and the `.paj` format for complete project files including networks, partitions, vectors, and permutations. These formats have become de facto standards in network science research and facilitate data exchange between Pajek and other analysis tools.

## Motivation and Context

The development of Pajek emerged from the need to analyze complex network structures that characterize real-world systems, including biological, social, and information networks. In the context of [[computational-neuroscience]], traditional graph theory metrics have proven invaluable for understanding brain organization, but the sheer size of whole-brain connectivity matrices—often containing tens of thousands of brain regions—required specialized software capable of handling large-scale network analysis [@Rubinov2010]. Pajek addresses this need by implementing efficient algorithms for network decomposition, community detection, and centrality analysis, enabling researchers to identify important topological features of brain networks such as [[small-world-networks|small-world properties]], [[modularity]], and [[rich-club|rich-club]] phenomena.

The software's ability to handle multiplex networks and temporal networks has also made it valuable for studying dynamic aspects of brain connectivity, complementing approaches from [[dynamic-causal-modeling]] and [[neural-mass-models]]. Pajek's implementation of network-theoretic measures predates many currentToolbox solutions in Python, and its algorithms have influenced subsequent tool development in [[connectomics]].

## Key Features

Pajek offers an extensive array of network analysis capabilities that are directly applicable to brain connectivity research. The software implements several [[community-detection]] algorithms, including **VOS (Visualization of Similarity) clustering**—a method developed specifically for network community detection that optimizes a quality function combining modularity with spatial coherence—along with traditional hierarchical clustering approaches based on various similarity measures. Network centrality measures—including degree, betweenness, closeness, and eigenvector centrality—are computed efficiently, enabling the identification of [[brain-network|brain network]] hubs that serve as critical nodes for information integration [@Rubinov2010]. Pajek also supports network randomization and bootstrapping procedures, which are essential for statistical inference in [[connectomics]] studies where connectivity patterns are compared against null models.

The visualization engine produces high-quality network layouts using force-directed algorithms, with support for various layout strategies that can highlight different topological features. Notably, Pajek provides tools for network partitioning, clustering analysis, and the extraction of network cores, all of which are useful for characterizing the hierarchical organization of brain [[connectivity]]. The software exports to standard graph formats including GraphML, edge lists, and adjacency matrices, facilitating interoperability with Python-based workflows using packages such as NetworkX or graph-tool.

## Relationship to TVB and Whole-Brain Modeling

In the [[whole-brain-modeling]] ecosystem, Pajek serves primarily as an analysis and validation tool rather than a simulation engine. Researchers using [[the-virtual-brain]] or similar [[whole-brain-simulators]] often employ Pajek to analyze the structural connectivity matrices that define the anatomical skeleton of their [[personalized-brain-modeling|personalized]] brain models. The export from tractography tools such as [[mrtrix3]] or [[dsi-studio]] can be loaded directly into Pajek (in .net format) for quality control and topological characterization before being used as input to neural mass models.

Pajek's network metrics provide validation targets for whole-brain simulations, allowing researchers to compare simulated functional connectivity patterns against empirically observed [[functional-connectivity]] networks. The workflow typically involves: (1) exporting tractography data to Pajek .net format, (2) computing topological metrics (clustering coefficient, path length, modularity), (3) using these metrics to validate or optimizeTVB connectivity matrices, and (4) running simulations to generate predicted functional connectivity patterns. The combination of Pajek for network analysis and TVB for neural dynamics simulation represents a common workflow in [[connectome]]-based modeling studies, particularly those investigating [[brain-oscillations]] and [[epilepsy-modeling]].

## Related Software and Extensions

Pajek has influenced the development of several related tools in the network science and neuroimaging communities. The [[brain-connectivity-toolbox]] (BCT), a widely-used MATLAB library for brain network analysis, implements many of the same metrics available in Pajek and is often used in conjunction with connectivity datasets that were initially explored using Pajek [@Rubinov2010]. Other related tools include [[graph-tool]] and **bctpy**, Python implementations of graph-theoretic measures for brain connectivity analysis. For visualization specifically, [[brainnet-viewer]] provides specialized brain network rendering capabilities that integrate with neuroimaging data formats. The export formats supported by Pajek (including GraphML and edge list formats) have become de facto standards for exchanging network data between different analysis platforms, facilitating interoperability with [[connectome-mapper-3]] and other [[neuroimaging]] preprocessing pipelines.

## Key Papers

- Batagelj, V., & Mrvar, A. (1998). Pajek — A program for large network analysis. *Connections*, 21(2), 47-57.
- de Nooy, W., Mrvar, A., & Batagelj, V. (2011). *Exploratory Social Network Analysis with Pajek* (2nd ed.). Cambridge University Press.
- Batagelj, V., & Mrvar, A. (2004). Analysis and visualization of large networks. In M. Jünger & G. Mutzel (Eds.), *Graph Drawing Software* (pp. 77-103). Springer.
- Rubinov, M., & Sporns, O. (2010). Complex network measures of brain connectivity: Uses and interpretations. *Current Opinion in Neurobiology*, 20(3), 262-267.
- Bullmore, E. T., & Bassett, D. S. (2011). Brain graphs: Graphical models of the human brain connectome. *Annual Review of Clinical Psychology*, 7, 113-140.

## References

1. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
2. (authors unknown). *Complex Brain Networks: Graph Theoretical Analysis of Structural and Functional Systems*.
3. M. A. van den Boom, Nicholas M. Gregg, G. Valencia, B. Lundstrom, K. J. Miller, D. van Blooijs, G. Huiskamp, F. Leijten, G. Worrell, Dora Hermes. (2025). *ER-detect: a pipeline for robust detection of early evoked responses in BIDS-iEEG electrical stimulation data.*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2025.110389)