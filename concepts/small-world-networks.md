---
title: Small-World Networks
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [network-dynamics, connectomics]
sources: [raw/papers/watts-strogatz-1998.md, raw/papers/bullmore-sporns-2009.md, raw/papers/sporns-2011.md]
---

# Small-World Networks

Network topology characterized by high local clustering and short global path lengths.

## Definition

Small-world networks exhibit two key properties:
1. **High Clustering**: Nodes tend to form tightly interconnected local groups
2. **Short Path Lengths**: Most nodes can be reached from every other node by a small number of steps

## Mathematical Characterization

### Clustering Coefficient (C)
Measures local connectivity density:
- C = (number of triangles) / (number of connected triples)
- High C indicates local clustering

### Characteristic Path Length (L)
Average shortest path between all node pairs
- Small L indicates efficient global communication

### Small-World Index
σ = (C/C_random) / (L/L_random)
- σ > 1 indicates small-world topology

## Brain Networks

### Evidence
Brain networks consistently show small-world properties:
- **Structural**: White matter networks
- **Functional**: Resting-state correlation networks
- **Across species**: From C. elegans to humans

### Functional Significance
- **Local Processing**: Clustering supports specialized computation
- **Global Integration**: Short paths enable information transfer
- **Efficiency**: Balance of segregation and integration

## The Watts-Strogatz Model

duncan watts|Watts and Strogatz (1998) showed how small-world networks emerge:
1. Start with regular lattice (high C, high L)
2. Randomly rewire some edges
3. Result: High C maintained, L drops dramatically

## Brain Implications

Small-world topology is thought to support:
- **Functional Segregation**: Specialized local processing
- **Functional Integration**: Coordinated global activity
- **Robustness**: Resilience to localized damage

## Related Concepts
- [[graph-theory]] – Mathematical framework
- clustering-coefficient – Local connectivity
- path-length – Global efficiency
- [[connectomics]] – Brain network analysis
- [[brain-network]] – Network organization
