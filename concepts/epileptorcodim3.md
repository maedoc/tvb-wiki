---
title: "EpileptorCodim3"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, epilepsy, codimension-3, bifurcation, seizure]
sources: [raw/papers/saggio-2017.md]
---

# Epileptor Codimension-3

A comprehensive unfolding of the Epileptor dynamics revealing the complete bifurcation structure. This model identifies the organizing center governing all seizure-related transitions.

## Overview

Developed by Saggio et al. (2017), the EpileptorCodim3 performs a codimension-3 bifurcation analysis of the Epileptor.

## Mathematical Foundation

### Codimension-3 Unfolding

The seizure dynamics emerge from a **Degenerate Bogdanov-Takens point** where:
- Saddle-node bifurcation (seizure onset)
- Hopf bifurcation (oscillation onset)  
- Homoclinic bifurcation (seizure offset)

all coalesce.

### Normal Form

```
dx/dt = y
dy/dt = μ₁ + μ₂·x + μ₃·y + x² + x·y
```

## Bifurcation Scenarios

1. **Saddle-Node/Homoclinic**: Typical seizure pattern
2. **Subcritical Hopf**: Abrupt onset with bistability
3. **Saddle-Node Loop**: Brief paroxysmal events
4. **Shilnikov**: Spike-and-wave complexes

## Related Concepts

- [[epileptor]] - Original 6D model
- [[bifurcation-theory]] - Mathematical foundation
- [[epilepsy-modeling]] - Clinical applications
