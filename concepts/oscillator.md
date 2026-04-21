---
title: "Generic 2D Oscillator"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, oscillator, phase-plane, universal]
sources: [raw/papers/fitzhugh-1961.md, raw/papers/stefanescu-2010.md]
---

# Generic 2D Oscillator

A universal two-dimensional oscillator model capable of exhibiting various dynamical regimes.

## Overview

Provides a flexible framework for neural excitability, oscillatory dynamics, and phase-plane analysis.

## Mathematical Formulation

**Canonical Form:**
```
dV/dt = d·τ·(-f(V) - W + I)
dW/dt = d·(g(V) - b·W + a)
```

## Dynamical Regimes

1. Fixed point
2. Excitable
3. Limit cycle
4. Bistable

## Related Concepts

- [[neural-mass-model]] - General framework
- [[bifurcation-theory]] - Dynamical transitions
