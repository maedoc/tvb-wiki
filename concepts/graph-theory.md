---
created: 2026-04-20
sources:
- raw/papers/rubinov-sporns-2010.md
- raw/papers/newman-2010.md
- raw/papers/bullmore-sporns-2009.md
- raw/papers/sporns-2011.md
- raw/papers/power-2010.md
- raw/papers/smith-2013-connectomics.md
tags:
- connectomics
- network-dynamics
title: Graph Theory
type: concept
updated: '2026-04-24'
---

# Graph Theory

Mathematical framework for studying networks, applied to brain connectivity analysis.

## Definition

Graph theory provides a language and set of tools for describing and analyzing networks. In neuroscience, it enables quantitative characterization of brain connectivity patterns.

## Basic Concepts

### Graph Components
- **Nodes (vertices)**: Brain regions, neurons, or other elements
- **Edges (links)**: Connections between nodes (structural or functional)
- **Weights**: Connection strengths
- **Direction**: Anatomical directionality (when known)

### Graph Types
- **Binary vs Weighted**: Presence vs strength of connections
- **Directed vs Undirected**: Asymmetric vs symmetric connections
- **Signed**: Excitatory vs inhibitory connections

## Network Measures

### Local Measures
- **Degree**: Number of connections to a node
- **Clustering Coefficient**: Density of local connections
- **Betweenness Centrality**: Role in connecting other nodes

### Global Measures
- **Characteristic Path Length**: Average shortest path
- **Global Efficiency**: Inverse of path length
- **Modularity**: Community structure strength

### Specialized Measures
- small-world-networks|Small-world: σ = (C/C_random)/(L/L_random)
- rich-club|Rich-club: Connectivity between high-degree nodes
- **Assortativity**: Degree correlation between connected nodes

## Brain Network Applications

### Structural Networks
- White matter tractography graphs
- Regional parcellation as nodes
- Connection probability as weights

### Functional Networks
- Correlation-based connectivity
- Thresholding and binarization
- Dynamic network analysis

## Software Tools
- brain-connectivity-toolbox|Brain Connectivity Toolbox
- NetworkX (Python)
- igraph (R/Python)

## Related Concepts
- [[connectomics]] – Field of connectivity research
- [[brain-network]] – Network organization
- [[network-hubs]] – Highly connected nodes
- [[modularity]] – Community structure
- network-dynamics – Dynamic processes