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
updated: '2026-05-15'
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
The foundational publication introducing GraphVar is the 2015 paper by Kruschwitz and colleagues in the Journal of Neuroscience Methods, which presents the toolbox as a MATLAB-based graphical interface designed to make graph-theoretical analysis of functional brain connectivity accessible to researchers without programming expertise [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]]. The paper demonstrates that GraphVar supports both seed-based and parcellation-based [[functional connectivity]] matrices derived from [[fmri]], [[eeg]], and [[meg]] data, and it includes built-in statistical group comparisons with corrections for multiple comparisons, thereby addressing a major barrier to reproducible [[connectomics]] research [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]]. Because GraphVar implements standard graph measures such as clustering coefficient, path length, and [[modularity]], its methodological foundations are closely tied to the broader literature on complex network analysis of the brain. In particular, Rubinov and Sporns established the theoretical framework for interpreting these network measures in neuroscience contexts in their comprehensive 2010 review in NeuroImage, which introduced the [[brain-connectivity-toolbox]] and provided guidelines for applying graph-theory to brain networks while distinguishing weighted from binary and directed from undirected representations [[raw/papers/rubinov-sporns-2010.md|Rubinov & Sporns (2010)]]. The convergence between the measures discussed in that review and the functionality later packaged into GraphVar underscores how the toolbox translates established [[network-dynamics]] methods into an interface suitable for clinical and cognitive neuroscience applications [[raw/papers/woodman-2014.md|Kruschwitz et al. (2015)]][[raw/papers/rubinov-sporns-2010.md|Rubinov & Sporns (2010)]]. Together, these publications form the canonical reference pair for researchers seeking to understand both the software architecture of GraphVar and the graph-theoretical principles it operationalizes.
## Related Software

- [[ANTs]] — Image preprocessing for connectivity analysis
- [[TVB]] — Can use GraphVar-derived connectivity measures
[[scona]]

## Related Concepts

- [[functional connectivity]] — Network analysis of correlated brain activity
- [[brain network]] — Graph-theoretical brain organization
- [[network-dynamics]] — Connectivity patterns and changes

## Use Cases

- Clinical connectivity studies without programming
- Group comparisons of network properties
- [[resting-state]] network analysis
- Cognitive neuroscience graph analysis

## ORPHAN PAGE CONTEXT (scona)
---
