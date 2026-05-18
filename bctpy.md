---
title: BCTpy
created: 2025-01-15
updated: 2026-05-18
type: entity
tags: [software-brain-modeling, connectomics, network-dynamics, structural-connectivity, functional-connectivity, whole-brain-modeling]
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
---

BCTpy is the Python implementation of the [[brain-connectivity-toolbox|Brain Connectivity Toolbox]], a software library for analyzing structural and functional brain networks using graph-theoretic measures originally developed by Mikail Rubinov and Olaf Sporns. It provides researchers with programmable access to topological metrics for connectivity matrices derived from neuroimaging data.

## Motivation and Context

The analysis of brain connectivity relies on graph-theoretic methods that quantify topological organization in structural and functional networks. [[raw/papers/rubinov-sporns-2010.md|Rubinov & Sporns (2010)]] introduced the Brain Connectivity Toolbox and provided a comprehensive review of complex network measures, establishing standardized interpretations for metrics applied to weighted, binary, directed, and undirected graph representations of brain connectivity. These measures are essential for characterizing the diverse connectivity patterns observed in empirical [[connectomics]] research across modalities such as [[fmri]], [[eeg]], [[meg]], and [[dti]] [[tractography]]. Modern whole-brain modeling platforms such as [[the-virtual-brain]] depend on reproducible, validated methods for quantifying anatomical and functional connectivity patterns across individuals [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]], and subject-specific structural connectivity parameterizations are essential for reproducing individual functional connectivity in personalized modeling workflows [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. A Python-based implementation of these graph-theoretic algorithms facilitates integration with contemporary scientific computing ecosystems and promotes [[reproducibility]] in network analysis pipelines.

## Key Features

BCTpy implements graph-theoretic metrics spanning node centrality, path-based characterization, and community detection as reviewed by [[raw/papers/rubinov-sporns-2010.md|Rubinov & Sporns (2010)]]. Node-level functions identify influential regions and [[network-hubs]], path-based metrics quantify global integration, and modular decomposition algorithms detect community structure within [[brain-parcellations]]. The library supports weighted and directed networks that preserve continuous connection strengths obtained from [[diffusion-imaging]] tractography, aligning with the graph representation principles discussed by [[raw/papers/rubinov-sporns-2010.md|Rubinov & Sporns (2010)]] and the structural connectivity frameworks used to parameterize personalized brain simulations [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. These capabilities enable quantification of [[small-world-networks]] topology and [[modularity]] in connectivity matrices derived from neuroimaging pipelines.

## Relationship to TVB

In whole-brain modeling workflows, graph-theoretic analysis applies to the structural and functional connectivity matrices that constrain simulations. [[raw/papers/sanz-leon-2013.md|Sanz Leon et al. (2013)]] showed that [[the-virtual-brain]] constructs personalized models by combining empirical [[structural-connectivity]] matrices—typically derived from diffusion MRI [[tractography]]—with [[neural-mass-models]] to simulate large-scale brain dynamics. [[raw/papers/ritter-2013.md|Ritter et al. (2013)]] further demonstrated that subject-specific structural connectivity parameterizations can reproduce individual [[resting-state]] functional connectivity patterns, bridging anatomical structure and emergent functional dynamics. Because BCTpy handles both binary and weighted graph representations, it accommodates the full range of connectivity data produced by neuroimaging pipelines, from thresholded tractography streamlines to continuous functional correlation matrices, consistent with the multimodal integration framework described by [[raw/papers/ritter-2013.md|Ritter et al. (2013)]]. Researchers can thus apply the network measure interpretations established by [[raw/papers/rubinov-sporns-2010.md|Rubinov & Sporns (2010)]] to quantify topological properties in both empirical structural matrices and simulated functional connectivity outputs, providing objective benchmarks for model validation in [[whole-brain-modeling]] studies.
