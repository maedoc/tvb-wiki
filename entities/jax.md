---
title: "JAX"
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [jax, machine-learning, differentiable-programming, python, numerical-computing]
sources: []
---

# JAX

**JAX** is a high-performance numerical computing library that combines Autograd (automatic differentiation) and XLA (Accelerated Linear Algebra). Developed by Google, JAX enables composable transformations of Python/NumPy functions: automatic differentiation, vectorisation via `vmap`, parallelisation via `pmap`, and just-in-time compilation to GPU/TPU via `jit`.

## Overview

JAX’s functional programming model and array-level parallelism make it well-suited to:
- **Neural network training** — natively via [Flax](https://github.com/google/flax) or [Equinox](https://github.com/patrick-kidger/equinox)
- **Differentiable simulation** — gradients through arbitrary numerical integrators
- **Scientific computing** — high-performance PDE/ODE solvers on accelerator hardware
- **Probabilistic programming** — [NumPyro](https://github.com/pyro-ppl/numpyro) uses JAX for fast Hamiltonian Monte Carlo

## Relationship to TVB

JAX intersects with TVB in three main ways:
- **BrainPy** — the [`[[brainpy]]`](brainpy.md) whole-bain simulation framework uses JAX as its primary backend to achieve **GPU acceleration** and **differentiable dynamics**
- **Differentiable TVB** — ongoing research uses JAX to make TVB fully differentiable, enabling gradient-based parameter optimisation and coupling with deep learning models
- **Accelerated solvers** — JAX-based ODE solvers can be plugged into TVB to run long simulations on GPU at orders-of-magnitude speed-ups over NumPy/C++ solvers
- **Neural mass model exploration** — JAX’s composable transformations make it trivial to experiment with thousands of parameter combinations in parallel

## Key Features

| Feature | Description |
|---------|-------------|
| **`grad`** | Reverse-mode automatic differentiation |
| **`vmap`** | Automatic vectorisation (parallel evaluation over batch dimensions) |
| **`jit`** | Just-in-time compilation to GPU/TPU via XLA |
| **`pmap`** | Parallel evaluation across multiple devices |

## Software

- Website: https://github.com/google/jax
- Documentation: https://jax.readthedocs.io/
- Install: `pip install jax jaxlib` (CPU); follow Google Cloud TPU or NVIDIA GPU instructions for accelerators

## Related

- [[`[[brainpy]]`](brainpy.md) — brain dynamics simulation framework built on JAX
- [[`[[the-virtual-brain]]`](the-virtual-brain.md) — TVB platform (future JAX integration planned)
- [[`[[machine-learning]]`](machine-learning.md) — general ML concepts and tools

## References

- Bradbury et al. (2018) — JAX: composable transformations of Python+NumPy programs. https://github.com/google/jax