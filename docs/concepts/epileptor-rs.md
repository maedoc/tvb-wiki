---
title: "EpileptorRS"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, epilepsy, resting-state, stochastic]
sources: []
---

# Epileptor Resting State

An extension of the Epileptor model incorporating stochastic dynamics for resting-state and interictal activity simulation.

## Overview

The EpileptorRS extends the standard Epileptor with:
1. Multiplicative noise on slow variables
2. Metabolic/energy considerations
3. Enhanced parameter ranges for interictal dynamics

## Key Modifications

### Stochastic Terms

Added noise to slow permittivity variable z:
```
dz = deterministic_terms + σ_z·ξ(t)
```

## Applications

- Interictal spike generation
- Sleep modeling
- Long-term monitoring
- Seizure prediction

## Related Concepts

- [[epileptor]] - Base model
- [[resting-state]] - RS concepts
