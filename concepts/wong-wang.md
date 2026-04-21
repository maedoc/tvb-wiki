---
title: "Wong-Wang Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, fmri, bold, resting-state, mean-field, decision-making]
sources: [raw/papers/wong-wang-2006.md, raw/papers/deco-2013.md]
---

# Wong-Wang Model

The reduced Wong-Wang model is a simplified neural mass model derived from spiking network simulations. It is particularly effective for modeling fMRI BOLD signals and resting-state functional connectivity.

## Overview

The model was developed by Wong and Wang (2006) as a reduction of a recurrent cortical network. Deco et al. (2013) adapted it for whole-brain resting-state modeling.

## Mathematical Formulation

### Core Equation

```
dS/dt = -S/τ_s + (1 - S) · γ · H(x)
```

Where S is NMDA synaptic activity.

### Input-Output Function

```
H(x) = (a·x - b) / (1 - exp(-d·(a·x - b)))
```

## Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| a | 0.270 nC⁻¹ | Input gain |
| b | 0.108 kHz | Input shift |
| d | 154 ms | Sigmoid steepness |
| γ | 0.641 | Kinetic parameter |
| τ_s | 100 ms | NMDA decay |
| w | 0.6 | Recurrent weight |
| J_N | 0.2609 nA | Coupling strength |
| I_o | 0.33 nA | Background input |

## Related Concepts

- [[wong-wang-exc-inh]] - Extended E-I version
- [[neural-mass-model]] - Theoretical framework
- [[resting-state]] - RS network modeling
- [[bold-signal]] - BOLD physics
