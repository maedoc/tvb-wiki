---
title: "Epileptor Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, epilepsy, seizure-dynamics, bifurcation, jirsa]
sources: [raw/papers/jirsa-2014.md, raw/papers/proix-2014.md]
---

# Epileptor Model

The Epileptor is a composite neural mass model specifically designed to capture the phenomenology of epileptic seizures. It combines two coupled dynamical systems representing distinct physiological processes during seizure generation.

## Overview

Developed by Jirsa et al. (2014), the Epileptor model provides a mathematical framework for understanding seizure initiation, propagation, and termination.

## Model Architecture

### Two Subsystems

| Subsystem | Variables | Description |
|-----------|-----------|-------------|
| **Population 1** | x₁, y₁, z | Main epileptic activity |
| **Population 2** | x₂, y₂, g | Subcortical inhibition |

## Mathematical Formulation

**Population 1:**
```
ẋ₁ = y₁ - f₁(x₁, z) + I_ext₁ + K_vf·c_pop₁
ẏ₁ = c - d·x₁² - y₁
ż = r·(4(x₁ - x₀) - z + K_s·c_pop₁)
```

**Population 2:**
```
ẋ₂ = -y₂ + x₂ - x₂³ + I_ext₂ + 0.002g - 0.3(z-3.5) + K_f·c_pop₂
ẏ₂ = (-y₂ + f₂(x₂)) / τ
```

**Output:** Output = -x₁ + x₂

## Key Parameters

| Parameter | Value | Role |
|-----------|-------|------|
| x₀ | -1.6 | Epileptogenicity (main bifurcation parameter) |
| r | 0.00035 | Timescale ratio |
| slope | 0.0 | Discharge slope |

## Dynamical Regimes

1. **Interictal**: x₀ < -2.0, stable fixed point
2. **Pre-ictal**: -2.0 < x₀ < -1.5, intermittent bursts
3. **Ictal**: x₀ > -1.5, sustained rhythmic activity

## Related Concepts

- [[epilepsy-modeling]] - General framework
- [[neural-mass-model]] - Theoretical foundation
- [[bifurcation-analysis]] - Dynamical analysis
- [[EpileptorCodim3]] - Codimension-3 variant
- [[EpileptorRS]] - Resting state variant
