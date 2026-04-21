---
title: "Larter-Breakspear Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, epilepsy, ion-channels, morris-lecar, complex-dynamics]
sources: [raw/papers/larter-1999.md, raw/papers/breakspear-2003.md, raw/papers/honey-2007.md]
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

## Related Concepts

- [[neural-mass-model]] - Theoretical framework
- [[epilepsy-modeling]] - Seizure applications
- [[nonlinear-dynamics]] - Chaos and complexity
