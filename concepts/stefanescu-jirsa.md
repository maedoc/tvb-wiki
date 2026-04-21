---
title: "Stefanescu-Jirsa Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, reduction, epileptor, low-dimensional]
sources: [raw/papers/stefanescu-2011.md, raw/papers/stefanescu-2012.md]
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

## Related Concepts

- [[epileptor]] - Full 6D model
- [[bifurcation-theory]] - Mathematical foundation
