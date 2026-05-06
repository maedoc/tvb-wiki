---
created: 2026-05-06
sources:
- raw/papers/woodman-2014.md
- raw/papers/rubinov-sporns-2010.md
- raw/papers/mijalkov-2017-braph.md
tags:
- connectivity
- graph-theory
- matlab
- network-science
title: Brain Connectivity Toolbox
type: entity
updated: '2026-05-06'
---

# Brain Connectivity Toolbox

The **Brain [[connectivity]] Toolbox (BCT)** is a comprehensive MATLAB package for graph-theoretic analysis of structural and functional brain networks. It provides hundreds of graph metrics for neuroscientific analysis.

## Overview

BCT implements graph-theoretic measures including:
- Degree, strength, and centrality measures
- Clustering coefficient and transitivity
- Path length, efficiency, and small-worldness
- [[community-detection]] and [[modularity]]
- [[rich-club]] organization
- Assortativity and motifs

## Relationship to TVB

BCT and TVB are complementary tools in the connectivity analysis pipeline:
- TVB generates simulated brain [[network-dynamics]]
- BCT analyzes the topological properties of the networks that TVB simulates
- BCT metrics (e.g., rich club coefficient, modularity) validate TVB [[structural-connectivity]] matrices
- TVB's connectivity module can export to BCT-compatible formats for cross-validation

## Software

- BCT is available at https://sites.google.com/site/bctnet/
- Python port: `[[bctpy]]` (PyPI)

## Related

- [[connectome]] — structural [[brain-network]] definitions
- [[graph-theory]] — mathematical foundations
- [[the-virtual-brain]] — simulation framework that generates networks for BCT analysis

## References

1. Woodman et al. (2014). *[[graphvar]]: A user-friendly toolbox for comprehensive graph analyses of functional brain connectivity*. Journal of Neuroscience Methods. [DOI](](https://doi.org/10.1016/j.jneumeth.2014.07.015))
2. (authors unknown). *Complex Network Measures of Brain Connectivity: Uses and Interpretations*.
3. (authors unknown). *[[braph]]: A Pipeline for Brain Connectivity Analysis*.