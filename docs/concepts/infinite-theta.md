---
title: "Infinite Theta Neuron Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, theta-neuron, phase-reduction, infinite-population]
sources: [raw/papers/montbrio-2015.md]
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

## Related Concepts

- [[neural-mass-model]] - General framework
- [[mean-field-theory]] - Theoretical basis
