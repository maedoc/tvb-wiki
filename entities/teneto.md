---
created: 2026-05-13
sources:
- raw/papers/woodman-2014.md
- raw/papers/thompson-2017.md
tags:
- software-brain-modeling
- network-dynamics
- functional-connectivity
- connectomics
- graph-theory
- resting-state
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
title: Teneto
type: entity
updated: '2026-05-19'
---

# Teneto

Teneto is an open-source Python package that implements temporal network theory for the analysis of time-varying brain connectivity, released alongside the foundational methodological paper by [[raw/papers/thompson-2017.md|Thompson et al. (2017)]]. The software provides a comprehensive suite of temporal network measures — including temporal centrality, temporal closeness, burstiness, fluctuability, volatility, reachability latency and temporal efficiency — that are specifically designed to quantify how topological relationships between brain regions evolve over time rather than collapsing an entire scanning session into a single static graph [[raw/papers/thompson-2017.md|Thompson et al. (2017)]]. By operating on the full sequence of time-resolved connectivity snapshots, Teneto treats temporal ordering and path constraints as intrinsic features of the [[connectome]], offering a rigorous alternative to applying conventional graph metrics independently within each sliding window [[raw/papers/thompson-2017.md|Thompson et al. (2017)]].

The package was first validated on [[resting-state]] [[fmri]] data, where its measures proved sensitive to both between-subject and between-task differences in [[dynamic functional connectivity]], demonstrating that temporal network properties carry information beyond what is captured by static summary statistics [[raw/papers/thompson-2017.md|Thompson et al. (2017)]]. In addition to its algorithmic library, Teneto includes plotting functions that facilitate visual exploration of temporal network structure, supporting the mapping of time-varying connectivity patterns onto standard neuroimaging parcellations [[raw/papers/thompson-2017.md|Thompson et al. (2017)]]. As a freely available Python toolkit, it bridges the methodological gap between abstract temporal graph theory and empirical neuroscience, enabling researchers to characterize the non-stationary dynamics of large-scale [[brain network]] architectures in health and disease [[raw/papers/thompson-2017.md|Thompson et al. (2017)]].

## Overview

Teneto is an open-source Python package for the analysis of **temporal networks** — networks whose edges and topology change as a function of time. In computational neuroscience, Teneto is primarily used to quantify [[dynamic functional connectivity]] — the time-varying statistical dependencies between brain regions observed in [[resting-state]] [[fmri]], [[eeg]], and [[meg]] recordings. Unlike static [[graph-theory]] toolboxes that treat each time window independently, Teneto provides algorithms specifically designed for the temporal dimension: it models the brain not as a single [[connectome]], but as a sequence of network snapshots whose transitions and reconfigurations carry information about ongoing [[brain-dynamics]].

The package fills a critical gap between standard [[connectivity]] analysis and the growing recognition that [[functional-connectivity]] is non-stationary. Where tools like the [[brain-connectivity-toolbox]] or [[bctpy]] compute graph metrics on a single aggregated adjacency matrix, Teneto operates on the full time-resolved network representation — often called a *temporal network* or *time-varying graph* — and provides measures that capture how network topology evolves across seconds to minutes.

## Motivation and Context

The motivation for Teneto arises from a fundamental observation in [[neuroimaging]]: the brain's functional architecture is not fixed. Even during undirected [[resting-state]] conditions, large-scale [[brain-network|brain networks]] reconfigure on timescales of seconds to tens of seconds, entering and leaving configurations that resemble canonical systems such as the [[default-mode-network]]. Standard static [[functional-connectivity]] analysis — computing a single [[Pearson correlation]] matrix over an entire scan — collapses this temporal richness into one number per edge. Sliding-window approaches partially recover temporal structure but still apply static graph measures to each window independently, ignoring relationships between successive windows and temporal ordering effects.

Teneto addresses this by treating time as a first-class dimension in network analysis. The package implements measures drawn from the broader field of temporal network theory, which was developed across disciplines including sociology, epidemiology, and physics, and adapts them to the specific demands of neuroimaging data — namely, the relatively short time series and high dimensionality characteristic of [[brain-parcellations]] with 100–1000 regions. This makes Teneto particularly valuable for studies investigating how dynamic reconfigurations of [[functional-connectivity]] relate to cognition, arousal, or clinical state, including [[schizophrenia-models]] and [[consciousness-models]].

## Key Features

Teneto provides several classes of temporal network measures beyond what is available in static [[graph-theory]] toolboxes. **Temporal centrality** measures — including temporal betweenness centrality and temporal closeness — identify nodes that are not merely central in any one snapshot, but are consistently influential across time, accounting for the fact that information cannot travel backward in time. **Burstiness analysis** quantifies the temporal clustering of edge activations, distinguishing regions that communicate in dense, intermittent bursts from those with steady, tonic coupling — a distinction relevant to theories of metastable [[brain-dynamics]].

The package also implements **temporal [[community-detection]]**, extending static [[modularity]] optimization to find groups of brain regions that maintain coherent co-fluctuation patterns over extended intervals. **Temporal motifs** — small subgraph patterns embedded in the time-resolved network — can be counted and compared against null models, providing a microscale analog to static motif analysis. For statistical rigor, Teneto includes a suite of **temporal null models** that preserve selected properties of the empirical temporal network (such as the event-count distribution per edge or the overall contact sequence) while randomizing others, enabling researchers to test whether observed temporal structure exceeds chance expectations.

A further practical strength is Teneto's **interoperability**. The package accepts time series data in numpy arrays and can output temporal network representations compatible with standard neuroimaging visualization tools, facilitating integration into pipelines built around [[mne-python]], [[nilearn]], or [[the-virtual-brain]].

## Relationship to TVB

Teneto serves a complementary role in the [[whole-brain-modeling]] ecosystem centered on [[the-virtual-brain]] (TVB). TVB simulates regional neural activity time series by coupling [[neural-mass-models]] through an empirical [[structural-connectivity]] matrix. The resulting simulated time series — analogous to empirical [[fmri]], [[eeg]], or [[meg]] recordings — can be fed directly into Teneto to compute temporal network measures on the simulated dynamics.

This pipeline enables a powerful form of [[model-validation]]: researchers can compare the temporal network properties of simulated data against those of empirical data, assessing not only whether a model reproduces static [[functional-connectivity]] patterns but also whether it captures the time-resolved reconfiguration dynamics observed in real brains. For example, TVB simulations parameterized with personalized [[connectome]] data can be evaluated using Teneto's burstiness and temporal community measures to determine whether they replicate the metastable switching behavior characteristic of [[resting-state]] brain activity. Conversely, Teneto's temporal null models can be used to construct surrogate connectome dynamics that serve as benchmarks for TVB simulations, helping disentangle structure-driven from dynamics-driven temporal features.

## Key Papers

The foundational reference for the application of temporal network theory to neuroimaging is Thompson et al. (2017), published in *[[netneuroscience|Network Neuroscience]]*, which articulates the transition from static to temporal network approaches and introduces the conceptual framework underlying Teneto's design. The software itself is described in a dedicated methods paper providing documentation of the package's API, algorithms, and validation against synthetic benchmarks. For users applying Teneto to dynamic functional connectivity analysis, the broader literature on time-varying brain connectivity — including work demonstrating that dynamic FC features carry individual-specific fingerprints and track cognitive state transitions — provides the empirical motivation for temporal network analysis in neuroimaging.

## Related Software

Teneto occupies a distinct niche complementing existing neuroimaging analysis tools. [[bctpy]] and the [[brain-connectivity-toolbox]] provide comprehensive static graph measures but do not model temporal network structure. [[graphvar]] extends graph-theoretic analysis to dynamic connectivity but operates primarily in MATLAB and emphasizes brain-behavior correlations rather than native temporal network measures. [[mne-connectivity]] computes time-resolved connectivity from [[mne-python]] data structures, generating the time series that can subsequently be analyzed by Teneto. [[brainspace]] implements gradient-based dimensionality reduction of connectivity patterns, complementary to Teneto's network-science approach. The general-purpose Python network analysis library provides lower-level graph manipulation but lacks neuroscience-specific temporal constructs.

## References

1. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))