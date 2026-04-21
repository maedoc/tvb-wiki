---
title: "Wong-Wang Excitatory-Inhibitory Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, fmri, bold, excitation-inhibition, resting-state]
sources: [raw/papers/wong-wang-2006.md, raw/papers/deco-2014.md]
---

# Wong-Wang Excitatory-Inhibitory Model

An extended version of the reduced Wong-Wang model with separate excitatory (E) and inhibitory (I) populations.

## Overview

The E-I extension maintains the biophysical grounding of the original while adding explicit inhibitory dynamics.

## Model Architecture

### Two Populations

| Population | Variable | Timescale |
|------------|----------|-----------|
| **Excitatory** | S_E | τ_E = 100 ms |
| **Inhibitory** | S_I | τ_I = 10 ms |

## Mathematical Formulation

**Excitatory:**
```
dS_E/dt = -S_E/τ_E + (1 - S_E) · γ_E · H_E(x_E)
x_E = w_+·J_N·S_E - J_i·S_I + I_o + J_N·C·Σ(S_E_j)
```

**Inhibitory:**
```
dS_I/dt = -S_I/τ_I + γ_I · H_I(x_I)
x_I = w_+·J_N·S_E - J_i·S_I + I_o
```

## Related Concepts

- [[wong-wang]] - Reduced single-population version
- [[neural-mass-model]] - General framework
