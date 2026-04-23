---
created: 2026-04-21
sources:
- raw/papers/arxiv-2508.04824.md
- raw/papers/semanticscholar-9e6c3252d305.md
- raw/papers/breakspear-2006.md
- raw/papers/wendling-2002.md
- raw/papers/semanticscholar-7733d5476149.md
- raw/papers/arxiv-2306.15787.md
tags:
- neural-mass-models
- epilepsy
- resting-state
- stochastic
title: EpileptorRS
type: concept
updated: '2026-04-23'
---

# Epileptor Resting State

An extension of the Epileptor model incorporating stochastic dynamics for resting-state and interictal activity simulation.

## Overview

The EpileptorRS extends the standard Epileptor with:
1. Multiplicative noise on slow variables
2. Metabolic/energy considerations
3. Enhanced parameter ranges for interictal dynamics

## Key Modifications

### Stochastic Terms

Added noise to slow permittivity variable z:
```
dz = deterministic_terms + σ_z·ξ(t)
```

## Applications

- Interictal spike generation
- Sleep modeling
- Long-term monitoring
- Seizure prediction

## References

1. Jirsa, V. K., Stacey, W. C., Quilichini, P. P., Ivanov, A. I., & Bernard, C. (2014). On the nature of seizure dynamics. *Brain*, 137(8), 2210–2230. https://doi.org/10.1093/brain/awu133

2. Proix, T., Bartolomei, F., Chauvel, P., Bernard, C., & Jirsa, V. K. (2014). Permittivity coupling across brain regions determines seizure recruitment in partial epilepsy. *Journal of Neuroscience*, 34(45), 15009–15021. https://doi.org/10.1523/JNEUROSCI.1570-14.2014

## Related Concepts

- [[epileptor]] - Base model
- [[resting-state]] - RS concepts