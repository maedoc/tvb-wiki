---
created: 2026-04-21
sources:
- raw/papers/breakspear-2006.md
- raw/papers/wendling-2002.md
tags:
- neural-mass-models
- epilepsy
- ion-channels
- morris-lecar
- complex-dynamics
title: Larter-Breakspear Model
type: concept
updated: '2026-04-23'
---

# Larter-Breakspear Model

The Larter-Breakspear model is a conductance-based neural mass model that extends the Morris-Lecar equations to include three coupled populations.

## Overview

Originally developed by Larter et al. (1999) for seizure simulation, refined by Breakspear, Terry & Friston (2003).

## Model Architecture

### Three Populations

| Population | Variable | Description |
|------------|----------|-------------|
| **Pyramidal** | V | Main excitatory output |
| **Inhibitory** | W | Inhibitory interneurons |
| **Modulatory** | Z | Slow inhibition |

## Mathematical Formulation

**Membrane Potential:**
```
ẌV = -g_Ca·m_Ca(V)·(V-V_Ca) - g_K·W·(V-V_K) - g_L·(V-V_L)
       - g_Na·m_Na(V)·(V-V_Na) - coupling_terms + I
```

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| g_Ca | 1.0 | Calcium conductance |
| g_K | 2.0 | Potassium conductance |
| g_Na | 6.7 | Sodium conductance |
| d_v | 0.0-0.55 | E→E coupling modulation |

## References

1. Larter, R., Speelman, B., & Worth, R. M. (1999). A coupled ordinary differential equation lattice model for the simulation of epileptic seizures. *Chaos*, 9(3), 795–806. https://doi.org/10.1063/1.166453

2. Breakspear, M., Terry, J. R., & Friston, K. J. (2003). Modulation of excitatory synaptic coupling facilitates synchronization and complex dynamics in a biophysical model of neuronal dynamics. *Neurocomputing*, 52–54, 151–158. https://doi.org/10.1016/S0925-2312(02)00788-7

3. Honey, C. J., Kötter, R., Breakspear, M., & Sporns, O. (2007). Network structure of cerebral cortex shapes functional connectivity on multiple time scales. *Proceedings of the National Academy of Sciences*, 104(24), 10240–10245. https://doi.org/10.1073/pnas.0701519104

## Related Concepts

- [[neural-mass-model]] - Theoretical framework
- [[epilepsy-modeling]] - Seizure applications
- [[nonlinear-dynamics]] - Chaos and complexity