---
created: 2026-04-21
sources:
- raw/papers/arxiv-2512.22093.md
- raw/papers/wilson-cowan-1972.md
- raw/papers/arxiv-2510.02545.md
- raw/papers/arxiv-2306.15859.md
- raw/papers/arxiv-2511.16252.md
tags:
- neural-mass-models
- linear
- testing
- baseline
title: Linear Model
type: concept
updated: '2026-04-23'
---

# Linear Model

A simple linear dynamical system used for testing, validation, and baseline comparisons.

## Overview

The Linear model provides known analytical solutions and simple dynamics for testing algorithms.

## Mathematical Formulation

```
dx/dt = a·x + b·u
```

## Use Cases

- Testing integration schemes
- Debugging coupling implementation
- Education
- Benchmarking

## References

1. Wilson, H. R., & Cowan, J. D. (1972). Excitatory and inhibitory interactions in localized populations of model neurons. *Biophysical Journal*, 12(1), 1–24. https://doi.org/10.1016/S0006-3495(72)86068-5

## Related Concepts

- [[neural-mass-model]] - General framework