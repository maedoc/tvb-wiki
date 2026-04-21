---
title: "Zerlaut Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, adaptation, excitation-inhibition, mean-field]
sources: [raw/papers/zerlaut-2018.md, raw/papers/mvj-2018.md]
---

# Zerlaut Model

A mean-field model of interacting excitatory and inhibitory populations with spike-frequency adaptation.

## Overview

Developed by Zerlaut and colleagues (2018), deriving mean-field equations from integrate-and-fire neurons with adaptation currents.

## Model Architecture

### Two Populations with Adaptation

| Population | Description |
|------------|-------------|
| **Excitatory** | Pyramidal cells with adaptation |
| **Inhibitory** | Interneurons (no adaptation) |

## Mathematical Formulation

**Excitatory firing rate:**
```
τ_m·dν_E/dt = -ν_E + Φ_E(I_eff_E - W·a)
```

**Inhibitory firing rate:**
```
τ_m·dν_I/dt = -ν_I + Φ_I(I_eff_I)
```

**Adaptation:**
```
τ_a·da/dt = -a + ν_E
```

## Related Concepts

- [[neural-mass-model]] - General framework
- [[mean-field-theory]] - Theoretical basis
