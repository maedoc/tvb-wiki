---
title: Modularity
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [network-dynamics, connectomics]
sources: [raw/papers/newman-2010.md, raw/papers/bullmore-sporns-2009.md, raw/papers/sporns-2011.md]
---

# Modularity

Organization of networks into communities or modules with dense internal connections and sparse external connections.

## Definition

Modularity refers to the degree to which a network can be divided into clearly separated groups (modules or communities), where nodes within a module are more densely connected to each other than to nodes in other modules.

## Mathematical Formulation

### Modularity (Q)
Q = (1/2m) * Σ_ij [A_ij - (k_i * k_j / 2m)] * δ(c_i, c_j)

Where:
- A_ij = connection weight between nodes i and j
- k_i = degree of node i
- m = total number of edges
- c_i = community assignment of node i
- δ = Kronecker delta (1 if same community, 0 otherwise)

### Interpretation
- Q > 0.3 indicates significant modular structure
- Higher Q = stronger community structure

## Brain Networks

### Cortical Modules
Brain networks show modular organization:
- **Sensory/Motor**: Visual, auditory, somatomotor
- **Cognitive**: Default mode, fronto-parietal, attention
- **Subcortical**: Basal ganglia, thalamus

### Functional Significance
- **Specialization**: Modules support specialized processing
- **Integration**: Inter-module connections enable integration
- **Evolution**: Modular organization facilitates evolution

## Community Detection Methods

### Algorithms
- **Louvain**: Fast, widely-used greedy optimization
- **Spectral**: Based on graph Laplacian
- **Walktrap**: Random walk-based approach
- **Infomap**: Information-theoretic approach

### Challenges
- **Resolution limit**: May miss small communities
- **Null models**: Choice affects results
- **Multiscale**: Modules at different scales

## Modularity in Brain Function

### Segregation and Integration
- **Modularity supports segregation**: Specialized processing
- **Inter-module edges support integration**: Global coordination
- **Balance**: Healthy brain shows optimal balance

### Development and Disease
- **Development**: Modular structure emerges during development
- **Aging**: Changes in modularity with age
- **Disease**: Altered modularity in psychiatric/neurological conditions

## Related Concepts
- community-detection – Finding network modules
- [[graph-theory]] – Mathematical framework
- [[brain-network]] – Network organization
- [[connectomics]] – Brain network analysis
- [[small-world-networks]] – Topology with modules
