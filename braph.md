---
title: BRAPH
created: 2025-01-15
updated: 2026-04-29
type: entity
tags: [software-brain-modeling, connectomics, graph-theory, neuroimaging-fmri, neuroimaging-mri, neuroimaging-eeg, neuroimaging-pet, network-dynamics]
sources: []
---

# BRAPH

## Overview

BRAPH (BRain Analysis using graPH theory) is a MATLAB-based software package for the analysis and visualization of brain connectivity data using graph theory methods. Originally developed by Mijalkov, Kakaei, Pereira, Westman, and Volpe and published in 2017, BRAPH provides a comprehensive framework for constructing connectivity matrices from neuroimaging data, calculating topological network measures, and performing statistical group comparisons. The software represents brain regions as nodes and inter-regional connections as edges, enabling researchers to characterize the topological architecture of the [[connectome]] at both global and nodal scales. BRAPH was designed to be accessible to researchers regardless of their programming experience, offering a graphical user interface (GUI) while maintaining a modular, object-oriented architecture that advanced users can extend through command-line scripting.

## Motivation and Context

The emergence of [[connectomics]] as a dominant paradigm in neuroscience created a pressing need for standardized tools to analyze brain network topology. Traditional neuroimaging analysis focused on regional activation patterns, but graph theory provided a mathematical framework for understanding the brain as an integrated system of interacting elements. Several toolboxes existed for this purpose—including the [[brain-connectivity-toolbox]], eConnectome, GAT, [[conn]], [[brainnet-viewer]], [[graphvar]], and GRETNA—yet each presented limitations such as requiring programming expertise, addressing only specific analysis aspects, or lacking extensibility for new methods.

BRAPH was developed to address these gaps by providing a fully integrated workflow that spans from raw neuroimaging data import to publication-ready figures. Its object-oriented architecture allows easy maintenance and customization, while its GUI makes graph theory analysis accessible to clinical researchers without computational backgrounds. A distinguishing feature of BRAPH is its support for longitudinal comparisons, enabling researchers to track changes in the same patients across multiple time points—a capability not commonly found in other toolboxes. The software has been successfully applied in studies of Alzheimer's disease, Parkinson's disease, and other neurodegenerative conditions to characterize [[network-dynamics]] alterations associated with pathology.

## Key Features

BRAPH supports analysis of brain networks derived from multiple neuroimaging modalities including structural magnetic resonance imaging (MRI), functional MRI (fMRI), positron emission tomography (PET), and electroencephalography (EEG). The software implements a complete analysis pipeline beginning with node definition using anatomical or functional [[brain-parcellations]] such as AAL, Desikan, Destrieux, Dosenbach, Power, or Craddock atlases. Users can also import custom parcellations or create new ones within the GUI.

For edge computation, BRAPH offers multiple correlation measures including Pearson, Spearman, and Kendall rank coefficients, as well as partial correlations with optional covariates. The resulting connectivity matrices can be analyzed as weighted or binary graphs, directed or undirected, with flexible thresholding approaches using either absolute correlation thresholds or fixed density thresholds. The software calculates comprehensive global network measures including [[small-world-networks]] properties (characteristic path length, clustering coefficient, small-worldness), [[modularity]], efficiency metrics, degree distribution characteristics, and transitivity. At the nodal level, BRAPH computes degree, strength, betweenness centrality, closeness centrality, and local efficiency, enabling identification of [[network-hubs]] and characterization of regional role in network organization.

For statistical inference, BRAPH implements non-parametric permutation tests with 10,000 iterations for group comparisons (cross-sectional and longitudinal), reporting one-tailed and two-tailed p-values based on 95% confidence intervals. The false discovery rate (FDR) correction using the Benjamini-Hochberg procedure addresses multiple comparisons when assessing nodal measures across brain regions. Network metrics can be normalized by comparison to random graphs with matching degree or weight distribution, following established procedures from the [[brain-connectivity-toolbox]].

## BRAPH 2.0 and Genesis

The newer BRAPH 2.0 version expands capabilities significantly by adding support for multilayer graph analysis, which captures connectivity patterns across multiple layers or modalities simultaneously. This advancement is particularly valuable for multimodal neuroimaging studies combining structural and functional connectivity data. BRAPH 2.0 also incorporates deep learning tools for brain connectivity analysis, including implementations for dense neural networks and graph convolutional neural networks.

A landmark feature of BRAPH 2.0 is the **Genesis** system, which enables researchers to create tailored distributions containing customized analysis pipelines integrated with the core BRAPH functionality. This community-oriented architecture allows research groups to develop specialized pipelines while maintaining a user-friendly GUI, promoting both reproducibility and extensibility. Custom distributions can be compiled with selected built-in elements and user-contributed methods, producing self-contained packages that can be shared and used by collaborators without programming expertise.

## Relationship to TVB

While BRAPH and [[the-virtual-brain]] (TVB) both fall within the domain of computational neuroscience and brain connectivity analysis, they serve complementary but distinct purposes in the research workflow. BRAPH is primarily an analysis tool focused on extracting topological metrics from empirical neuroimaging data—it characterizes the statistical properties of observed brain networks without generating predictions about brain dynamics. In contrast, TVB is a [[whole-brain-modeling]] simulator that constructs computational models of brain activity to simulate functional dynamics and predict how perturbations (e.g., stimulation) affect network behavior.

The two tools can be integrated in complementary research pipelines: BRAPH can be used to quantify topological properties of empirical brain networks from patient populations, while these metrics can then inform the parameterization of [[neural-mass-models]] within TVB for personalized brain modeling. Both tools share emphasis on [[structural-connectivity]] and [[functional-connectivity]] analysis, and both support various neuroimaging modalities. However, BRAPH focuses on graph-theoretic analysis of static or dynamic connectivity matrices, whereas TVB emphasizes forward modeling and simulation of brain dynamics grounded in anatomical connectivity.

## Related Software

BRAPH occupies a specific niche within the ecosystem of brain connectivity analysis tools, complementing several related packages:

- [[brain-connectivity-toolbox]] (BCT): The original MATLAB toolbox providing foundational graph theory measures; BRAPH adapted many measures from BCT
- [[bctpy]]: Python implementation of the Brain Connectivity Toolbox
- [[graphvar]]: Graph-theoretical analysis toolbox with focus on variability measures
- [[graph-tool]]: General-purpose network analysis library with Python bindings
- [[brainnet-viewer]]: Network visualization tool for brain connectivity graphs
- [[conn]]: Functional connectivity toolbox with GUI, focused on fMRI analysis
- [[nilearn]]: Python library for neuroimaging data preprocessing and analysis including connectivity

## Key Papers

The seminal BRAPH paper was published in PLOS ONE by Mijalkov et al. (2017): "BRAPH: A graph theory software for the analysis of brain connectivity." This paper demonstrated the software's capabilities through applications to structural MRI data comparing healthy controls, patients with amnestic mild cognitive impairment, and patients with Alzheimer's disease, as well as resting-state fMRI data comparing healthy controls and Parkinson's disease patients with mild cognitive impairment.

BRAPH 2.0 is described in a 2025 preprint: "BRAPH 2: a flexible, open-source, reproducible, community-oriented, easy-to-use framework for network analyses in neurosciences" (Chang et al., bioRxiv). The software has also been applied in multiple research studies investigating [[alzheimers-disease]], [[alzheimers-modeling]], and Parkinson's disease brain networks, demonstrating its utility for clinical connectomics research.