---
title: "Infinite Theta Neuron Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, theta-neuron, phase-reduction, infinite-population]
---

# Infinite Theta Neuron Model (Montbrió-Pazó-Roxin)

An exact mean-field reduction of an infinite population of quadratic integrate-and-fire (QIF) neurons.

## Overview

Developed by Montbrió, Pazó, and Roxin (2015), deriving exact mean-field equations for globally coupled QIF neurons.

## Mathematical Formulation

**Mean-Field Equations:**
```
τ·dr/dt = Δ/(π·τ) + 2·r·v
τ·dv/dt = v² - (π·r·τ)² + μ(t) + J·r·τ
```

Where r is firing rate and v is mean voltage.

## Parameters

| Parameter | Description |
|-----------|-------------|
| Δ | Width of input distribution |
| μ | Mean external input |
| J | Recurrent coupling |

## References

1. Montbrió, E., Pazó, D., & Roxin, A. (2015). Macroscopic description for networks of spiking neurons. *Physical Review X*, 5(2), 021028. https://doi.org/10.1103/PhysRevX.5.021028

2. Devalle, F., Roxin, A., & Montbrió, E. (2017). Firing rate equations require a spike synchrony mechanism to correctly describe fast oscillations in inhibitory networks. *PLoS Computational Biology*, 13(12), e1005881. https://doi.org/10.1371/journal.pcbi.1005881

## Related Concepts

- [[neural-mass-model]] - General framework
- [[mean-field-theory]] - Theoretical basis
