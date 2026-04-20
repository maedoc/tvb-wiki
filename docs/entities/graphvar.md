---
title: GraphVar
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: [software-graphvar, functional-connectivity, network-dynamics, brain-network, neuroimaging-processing]
sources: [raw/papers/woodman-2014.md]
---

# GraphVar

GraphVar is a user-friendly MATLAB toolbox for comprehensive graph-theoretical analyses of functional brain connectivity.

## Overview

GraphVar provides a graphical user interface (GUI) for performing graph-theoretical analyses of functional brain connectivity data, making network analysis accessible to researchers without programming expertise. It supports both seed-based and parcellation-based connectivity matrices from fMRI and EEG/MEG data.

## Key Features

- **Graphical user interface**: No programming required
- **Comprehensive network metrics**: Wide range of graph-theoretical measures
- **Statistical comparisons**: Group comparisons with multiple comparison corrections
- **Multi-modal support**: fMRI and EEG/MEG connectivity matrices
- **Seed-based and parcellation-based**: Flexible connectivity input
- **MATLAB-based**: Integration with SPM and other neuroimaging tools

## Network Metrics

- Clustering coefficient
- Path length and efficiency
- Modularity and community detection
- Betweenness and degree centrality
- Small-worldness indices

## Key Publications

- Woodman et al. (2014) — GraphVar toolbox introduction woodman-2014

## Related Software

- [[ANTs]] — Image preprocessing for connectivity analysis
- [[TVB]] — Can use GraphVar-derived connectivity measures

## Related Concepts

- [[functional connectivity]] — Network analysis of correlated brain activity
- [[brain network]] — Graph-theoretical brain organization
- network dynamics — Connectivity patterns and changes

## Use Cases

- Clinical connectivity studies without programming
- Group comparisons of network properties
- Resting-state network analysis
- Cognitive neuroscience graph analysis
