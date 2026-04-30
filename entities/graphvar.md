---
created: 2026-04-20
sources:
- raw/papers/woodman-2014.md
- raw/papers/arxiv-2604.16463.md
- raw/papers/rubinov-sporns-2010.md
- raw/papers/sporns-2011.md
- raw/papers/semanticscholar-0aeca1b592e6.md
- raw/papers/smith-2013-connectomics.md
tags:
- software-graphvar
- functional-connectivity
- network-dynamics
- brain-network
- neuroimaging-processing
title: GraphVar
type: entity
updated: '2026-04-30'
---

# GraphVar

GraphVar is a user-friendly MATLAB toolbox for comprehensive graph-theoretical analyses of functional brain [[connectivity]].

## Overview

GraphVar provides a graphical user interface (GUI) for performing graph-theoretical analyses of functional brain connectivity data, making network analysis accessible to researchers without programming expertise. It supports both seed-based and [[parcellation]]-based connectivity matrices from [[fmri]] and EEG/MEG data.

## Key Features

- **Graphical user interface**: No programming required
- **Comprehensive network metrics**: Wide range of graph-theoretical measures
- **Statistical comparisons**: Group comparisons with multiple comparison corrections
- **Multi-modal support**: fMRI and EEG/MEG connectivity matrices
- **Seed-based and parcellation-based**: Flexible connectivity input
- **MATLAB-based**: Integration with SPM and other [[neuroimaging]] tools

## Network Metrics

- Clustering coefficient
- Path length and efficiency
- [[modularity]] and [[community-detection]]
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
- [[network-dynamics]] — Connectivity patterns and changes

## Use Cases

- Clinical connectivity studies without programming
- Group comparisons of network properties
- [[resting-state]] network analysis
- Cognitive neuroscience graph analysis

## References

1. Woodman et al. (2014). *GraphVar: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](https://doi.org/10.1016/j.jneumeth.2014.07.015)
2. Xiaobo Liu. (2026). *MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis*. [Link](https://www.semanticscholar.org/paper/e7aaa4f4bb01e70064493684b4500a950f83460f)
3. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
4. (authors unknown). *Networks of the Brain*.
5. Mohammadtaha Parsayan, S. Andalib, T. L. Andersen, Habib Ganjgahi, P. Høilund-Carlsen, Abass Alavi, Mojtaba Zarei. (2025). *Odense-Oxford PET Image Analysis (OPETIA): An FSL-based toolbox for multimodal neuroimaging*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2025.121278)
6. (authors unknown). *Functional Connectomics from Resting-State fMRI*.