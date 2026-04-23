---
created: 2026-04-21
sources:
- raw/papers/arxiv-2509.02799.md
- raw/papers/stefanescu-jirsa-2008.md
- raw/papers/semanticscholar-e1fa0a868dbe.md
- raw/papers/arxiv-2508.19134.md
- raw/papers/semanticscholar-a9ff4dda4e4c.md
- raw/papers/arxiv-2508.02633.md
- raw/papers/semanticscholar-7593809733f3.md
- raw/papers/arxiv-2604.17291.md
tags:
- neural-mass-models
- adaptation
- excitation-inhibition
- mean-field
title: Zerlaut Model
type: concept
updated: '2026-04-23'
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

## References

1. Zerlaut, Y., Chemla, S., Chavane, F., & Destexhe, A. (2018). Modeling mesoscopic cortical dynamics using mean-field models. *NeuroImage*, 182, 49–70. https://doi.org/10.1016/j.neuroimage.2018.01.001

2. di Volo, M., & Destexhe, A. (2019). Biologically plausible mean-field models of conductance-based networks of adaptive spiking neurons. *PLoS Computational Biology*, 15(6), e1006578. https://doi.org/10.1371/journal.pcbi.1006578

## Related Concepts

- [[neural-mass-model]] - General framework
- [[mean-field-theory]] - Theoretical basis