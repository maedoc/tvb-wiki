---
created: 2026-04-21
sources:
- raw/papers/stefanescu-jirsa-2008.md
- raw/papers/arxiv-2509.02799.md
- raw/papers/semanticscholar-7c3337c880fd.md
- raw/papers/arxiv-2604.11971.md
- raw/papers/arxiv-2603.29903.md
tags:
- neural-mass-models
- reduction
- epileptor
- low-dimensional
title: Stefanescu-Jirsa Model
type: concept
updated: '2026-04-23'
---

# Stefanescu-Jirsa Model

A systematic dimensional reduction of the Epileptor yielding a 2D model that preserves essential seizure dynamics.

## Overview

Developed by Stefanescu and Jirsa (2011-2012), applying center manifold reduction to the 6D Epileptor.

## Mathematical Formulation

### Normal Form Near Saddle-Node

```
dv/dt = α - v² + w
dw/dt = -ε·(v - γ)
```

This is the universal unfolding of the saddle-node bifurcation.

## Parameters

| Parameter | Role |
|-----------|------|
| α | Distance to bifurcation |
| ε | Time-scale ratio |
| γ | Offset in slow variable |

## References

1. Stefanescu, R. A., & Jirsa, V. K. (2008). A low dimensional description of globally heterogeneous intracranial EEG. *NeuroImage*, 42(3), 1147–1158. https://doi.org/10.1016/j.neuroimage.2008.06.021

2. Stefanescu, R. A., & Jirsa, V. K. (2011). Reduced representations of heterogeneous micro-scale connectivity in brain networks. *PLoS Computational Biology*, 7(5), e1002007. https://doi.org/10.1371/journal.pcbi.1002007

## Related Concepts

- [[epileptor]] - Full 6D model
- [[bifurcation-theory]] - Mathematical foundation