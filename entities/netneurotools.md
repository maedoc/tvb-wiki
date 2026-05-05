---
created: 2025-01-15
sources:
- https://github.com/netneurolab/netneurotools
- https://netneurotools.readthedocs.io/
- https://www.biorxiv.org/content/10.1101/2025.02.14.638374v1
- raw/papers/wang-etal-2015-gretna.md
- raw/papers/woodman-2014.md
- raw/papers/arxiv-2601.03796.md
tags:
- software-neuroinformatics
- network-neuroscience
- python-toolbox
- connectomics
- brain-network
- graph-theory
title: netneurotools
type: entity
updated: '2026-05-05'
---

Netneurotools is a Python toolbox for network neuroscience research, developed by the [[netneuroscience|Network Neuroscience]] Lab at McGill University's Brain Imaging Centre. The package provides a collection of functions for analyzing brain [[connectivity]] data, computing network-level metrics, and working with structural and functional connectomes. It emerged from the increasing availability of large-scale [[connectome]] datasets and the need for standardized, reproducible tools in the network neuroscience community [[cite:netneurotools-github]].

## Overview

Netneurotools serves as a bridge between raw [[neuroimaging]] data and network-theoretic analyses that characterize brain connectivity patterns. The toolbox implements graph-theoretic measures from the brain connectivity literature, including metrics for network segregation (clustering coefficient, [[modularity]]), integration (path length, efficiency), and centralities (degree, betweenness, eigenvector) [[cite:netneurotools-github]]. Beyond metric computation, netneurotools provides utilities for working with common neuroimaging file formats, [[brain-parcellations]], and coordinate systems that facilitate the construction of connectivity matrices from imaging data.

The software is designed to integrate with the broader Python neuroimaging ecosystem, particularly libraries such as Nilearn, [[nibabel]], and [[bctpy]]. This interoperability allows researchers to incorporate netneurotools functions into existing preprocessing and analysis pipelines that handle [[fMRI]], [[diffusion-imaging]], or [[dti]] data. The package emphasizes functional convenience, providing high-level functions that combine multiple operations—such as loading a parcellation, extracting time series, and computing connectivity matrices—into single function calls [[cite:netneurotools-docs]].

## Key Features

Netneurotools offers several categories of functionality that support end-to-end network neuroscience analyses. The **datasets module** provides automatic fetching utilities for common brain atlases and template surfaces, including the Schaefer 2018 parcellation [[cite:schaefer2018]], Cammoun 2012 [[cite:cammoun2012]], MMP atlas [[cite:mmp]], Tian [[cite:tian2020]] andVon Economo [[cite:voneconomo]] atlases. Additional fetchers provide access to Freesurfer meshes (fsaverage), FSLR surfaces, CIVET templates, and the Conte69 [[cite:conte69]] hemisphere template [[cite:netneurotools-api]].

The **networks module** handles construction and manipulation of brain networks, including functions for creating consensus networks from multiple datasets (func_consensus, struct_consensus), network randomization with degree/length preservation (randmio_und), and thresholding/binarization utilities. These functions support generation of both empirical connectivity networks and surrogate networks for null model comparisons [[cite:netneurotools-api]].

Network metric computation forms a core component of the toolbox within the **metrics module**, implementing graph-theoretic measures adapted from the Brain Connectivity Toolbox [[cite:bct]]. These include global metrics (characteristic path length, global efficiency, clustering coefficient, modularity) and node-level metrics (degree, strength, betweenness centrality, eigenvector centrality, PageRank). The package also includes advanced metrics such as navigability [[cite:navigability]], search information [[cite:searchinfo]], path transitivity, communicability, diffusion efficiency, and mean first passage time [[cite:netneurotools-api]].

The **stats module** provides statistical functions optimized for network neuroscience, including efficient Pearson correlation implementations (efficient_pearsonr, weighted_pearsonr), permutation tests (permtest_1samp, permtest_rel), and regression utilities with dominance analysis (residualize, get_dominance_stats) [[cite:netneurotools-api]].

Additional modules include **plotting** (brain surface visualization using pyvista, heatmaps), **spatial** (Moran's I, Geary's C, Lee's L for spatial autocorrelation), **modularity** (consensus modularity, [[community-detection]]), and **interface** ([[cifti]], GIFTI, FreeSurfer file handling) [[cite:netneurotools-docs]].

## Relationship to TVB

Netneurotools relates to [[the-virtual-brain]] through complementary analysis workflows, though the two tools serve distinct purposes in the computational neuroscience pipeline. TVB focuses on **generating** simulated brain activity through [[whole-brain-modeling]] with [[neural-mass-models]] running on [[structural-connectivity]] scaffolds, while netneurotools focuses on **analyzing** empirical or simulated brain networks using graph-theoretic approaches.

In practice, researchers using TVB may employ netneurotools to analyze the simulated [[functional-connectivity]] patterns produced by TVB simulations, comparing them against empirical functional connectivity from [[resting-state]] fMRI datasets. The network metrics computed by netneurotools can serve as summary statistics for comparing different TVB parameter configurations, validating models against empirical data, or characterizing the dynamical properties of simulated brain activity. The toolbox's atlas fetching utilities and [[parcellation]] handling align well with TVB's use of brain atlases to define regional node structure in whole-brain models.

## Related Software

Netneurotools operates within an ecosystem of Python tools for network neuroscience and brain connectivity analysis. Related packages include [[bctpy]] (Brain Connectivity Toolbox in Python), which provides a comprehensive set of network metrics; [[brainspace]] for manifold learning and dimensionality reduction on connectivity data; and Nilearn for general neuroimaging data manipulation and decoding. The toolbox also complements connectivity-focused packages such as [[mne-connectivity]] for EEG/MEG connectivity analysis.

For [[whole-brain|whole-brain modeling]] workflows, netneurotools can be combined with TVB's [[tvb-library]] to create analysis pipelines that compare simulated and empirical network properties, supporting the goal of [[personalized-brain-modeling]] through parameter optimization and [[model-validation]].

## Key Papers

- Liu ZQ, Bazinet V, Hansen JY, Milisav F, Luppi AI, Ceballos EG, Farahani A, Suarez LE, Shafiei G, Markello RD, Misic B. "netneurotools: a trainee-oriented approach to network neuroscience." *bioRxiv* (2025). [[cite:netneurotools-paper]]

- Hansen JY, Shafiei G, Markello RD, et al. "Mapping neurotransmitter systems to the structural and functional organization of the human neocortex." *Nature Neuroscience* (2022). [[cite:neuromaps]]

- Markello RD, Hansen JY, Liu ZQ, et al. "[[neuromaps]]: structural and functional interpretation of brain maps." *Nature Methods* (2022). [[cite:neuromaps-paper]]

- Suarez LE, Markello RD, Betzel RF, Misic B. "Linking structure and function in macroscale brain networks." *Trends in Cognitive Sciences* (2020). [[cite:structure-function]]

## References

1. Wang, J., Wang, X., Xia, M., Liao, X., Evans, A., & He, Y. (2015). *GRETNA: a graph theoretical network analysis toolbox for MATLAB*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2015.04.016)
2. Woodman et al. (2014). *[[graphvar]]: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)
3. Christopher Gabaldon, Adria Mulero, Rong Wang, Daniel A. Martin, Sabrina Camargo, Qian-Yuan Tang, Ignacio Cifre, Changsong Zhou, Dante R. Chialvo. (2026). *Data-driven inference of brain dynamical states from the r-spectrum of correlation matrices*. [Link](https://arxiv.org/abs/2601.03796)