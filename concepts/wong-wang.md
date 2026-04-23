---
created: 2026-04-21
sources:
- raw/papers/wendling-2002.md
- raw/papers/semanticscholar-cc2129666e15.md
- raw/papers/semanticscholar-15a4a438614f.md
- raw/papers/semanticscholar-807668ceea0a.md
- raw/papers/semanticscholar-71ffb8153870.md
tags:
- neural-mass-models
- fmri
- bold
- resting-state
- mean-field
- decision-making
title: Wong-Wang Model
type: concept
updated: '2026-04-23'
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

## References

1. Wong, K. F., & Wang, X. J. (2006). A recurrent network mechanism of time integration in perceptual decisions. *Journal of Neuroscience*, 26(4), 1314–1328. https://doi.org/10.1523/JNEUROSCI.3733-05.2006

2. Deco, G., Ponce-Alvarez, A., Mantini, D., Romani, G. L., Hagmann, P., & Corbetta, M. (2013). Resting-state functional connectivity emerges from structurally and dynamically shaped slow linear fluctuations. *Journal of Neuroscience*, 32(27), 11239–11252. https://doi.org/10.1523/JNEUROSCI.1091-12.2013

## Related Concepts

- [[wong-wang-exc-inh]] - Extended E-I version
- [[neural-mass-model]] - Theoretical framework
- [[resting-state]] - RS network modeling
- [[bold-signal]] - BOLD physics