---
title: "K-Ion Exchange Model"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, metabolism, potassium, ion-dynamics]
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

## References

1. Cressman, J. R., Ullah, G., Ziburkus, J., Schiff, S. J., & Barreto, E. (2009). The influence of sodium and potassium dynamics on excitability, seizures, and the stability of persistent states: I. Single neuron dynamics. *Journal of Computational Neuroscience*, 26(2), 159–170. https://doi.org/10.1007/s10827-008-0132-4

2. Ullah, G., Cressman, J. R., Barreto, E., & Schiff, S. J. (2009). The influence of sodium and potassium dynamics on excitability, seizures, and the stability of persistent states: II. Network and glial dynamics. *Journal of Computational Neuroscience*, 26(2), 171–183. https://doi.org/10.1007/s10827-008-0133-3

## Related Concepts

- [[epileptor]] - Activity dynamics
- [[neural-mass-model]] - General framework
