---
title: "Hopfield Network"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-mass-models, associative-memory, attractor-networks, discrete]
sources: [raw/papers/hopfield-1982.md, raw/papers/hopfield-1984.md]
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

**Energy Function:**
```
E = -(1/2) · Σ_ij W_ij · S_i · S_j
```

## Related Concepts

- [[neural-mass-model]] - Continuous models
