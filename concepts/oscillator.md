---
title: "Generic 2D Oscillator"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, oscillator, phase-plane, universal]
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

## References

1. Fitzhugh, R. (1961). Impulses and physiological states in theoretical models of nerve membrane. *Biophysical Journal*, 1(6), 445–466. https://doi.org/10.1016/S0006-3495(61)86902-6

2. Nagumo, J., Arimoto, S., & Yoshizawa, S. (1962). An active pulse transmission line simulating nerve axon. *Proceedings of the IRE*, 50(10), 2061–2070. https://doi.org/10.1109/JRPROC.1962.288235

## Related Concepts

- [[neural-mass-model]] - General framework
- [[bifurcation-theory]] - Dynamical transitions
