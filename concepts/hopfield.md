---
created: 2026-04-21
sources:
- raw/papers/arxiv-2510.19146.md
- raw/papers/arxiv-2512.05252.md
- raw/papers/arxiv-2602.09535.md
- raw/papers/arxiv-2604.13719.md
- raw/papers/arxiv-2603.04149.md
- raw/papers/semanticscholar-71ffb8153870.md
- raw/papers/semanticscholar-c3d9674bec1b.md
- raw/papers/semanticscholar-62534125f066.md
tags:
- neural-mass-models
- associative-memory
- attractor-networks
- discrete
title: Hopfield Network
type: concept
updated: '2026-04-24'
---

# Hopfield Network

A recurrent neural network serving as an associative memory system.

## Overview

Developed by John Hopfield (1982, 1984), demonstrating how neural networks can store patterns as attractor states.

## Mathematical Formulation

**Update Rule:**
```
S_i(t+1) = sign(Σ_j W_ij · S_j(t) - θ_i)
```

**Hebbian Learning:**
```
W_ij = (1/N) · Σ_μ ξ_iμ · ξ_jμ
```

## References

1. Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 79(8), 2554–2558. https://doi.org/10.1073/pnas.79.8.2554

2. Hopfield, J. J. (1984). Neurons with graded response have collective computational properties like those of two-state neurons. *Proceedings of the National Academy of Sciences*, 81(10), 3088–3092. https://doi.org/10.1073/pnas.81.10.3088

## Related Concepts

- [[neural-mass-model]] - Continuous models