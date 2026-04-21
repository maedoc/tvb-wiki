---
title: "K-Ion Exchange Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, metabolism, potassium, ion-dynamics]
sources: []
---

# K-Ion Exchange Model

A metabolic neural mass model incorporating extracellular potassium dynamics.

## Overview

The KIonEx model explicitly tracks:
- Extracellular potassium concentration [K⁺]_o
- Na⁺/K⁺-ATPase pump activity
- Glial buffering
- Vascular clearance

## Mathematical Formulation

**Potassium Dynamics:**
```
d[K⁺]_o/dt = α·firing_rate - β·glial_buffer - γ·vascular_clearance + pump(ATP)
```

## Related Concepts

- [[epileptor]] - Activity dynamics
- [[neural-mass-model]] - General framework
