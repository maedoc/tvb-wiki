---
title: "Wong-Wang Excitatory-Inhibitory Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, fmri, bold, excitation-inhibition, resting-state]
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

## References

1. Wong, K. F., & Wang, X. J. (2006). A recurrent network mechanism of time integration in perceptual decisions. *Journal of Neuroscience*, 26(4), 1314–1328. https://doi.org/10.1523/JNEUROSCI.3733-05.2006

2. Deco, G., Kringelbach, M. L., Jirsa, V. K., & Ritter, P. (2017). The dynamics of resting fluctuations in the brain: Metastability and its dynamical cortical core. *Scientific Reports*, 7, 3095. https://doi.org/10.1038/s41598-017-03074-5

## Related Concepts

- [[wong-wang]] - Reduced single-population version
- [[neural-mass-model]] - General framework
