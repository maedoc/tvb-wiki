---
created: 2026-05-06
sources:
- raw/papers/arxiv-2507.20990.md
- raw/papers/semanticscholar-9afbfd2d37be.md
- raw/papers/semanticscholar-39decd6e7d9f.md
- raw/papers/semanticscholar-2d6ce9a9b368.md
tags:
- jax
- machine-learning
- differentiable-programming
- python
- numerical-computing
title: JAX
type: entity
updated: '2026-05-10'
---

# JAX

**JAX** is a high-performance numerical computing library that combines Autograd (automatic differentiation) and XLA (Accelerated [[linear]] Algebra). Developed by Google, JAX enables composable transformations of Python/NumPy functions: automatic differentiation, vectorisation via `vmap`, parallelisation via `pmap`, and just-in-time compilation to GPU/TPU via `jit`.

## Overview

JAX’s functional programming model and array-level parallelism make it well-suited to:
- **[[neural-network]] training** — natively via [Flax](](https://github.com/google/flax)) or [Equinox](](https://github.com/patrick-kidger/equinox))
- **Differentiable simulation** — gradients through arbitrary numerical integrators
- **Scientific computing** — high-performance PDE/ODE solvers on accelerator hardware
- **Probabilistic programming** — [NumPyro](](https://github.com/pyro-ppl/numpyro)) uses JAX for fast Hamiltonian Monte Carlo

## Relationship to TVB

JAX intersects with TVB in three main ways:
- **BrainPy** — the [`[[brainpy]]`](](brainpy.md)) whole-bain simulation framework uses JAX as its primary backend to achieve **GPU acceleration** and **differentiable dynamics**
- **Differentiable TVB** — ongoing research uses JAX to make TVB fully differentiable, enabling gradient-based parameter optimisation and coupling with deep learning models
- **Accelerated solvers** — JAX-based ODE solvers can be plugged into TVB to run long simulations on GPU at orders-of-magnitude speed-ups over NumPy/C++ solvers
- **[[neural-mass-models|Neural mass model]] exploration** — JAX’s composable transformations make it trivial to experiment with thousands of parameter combinations in parallel

## Key Features

| Feature | Description |
|---------|-------------|
| **`grad`** | Reverse-mode automatic differentiation |
| **`vmap`** | Automatic vectorisation (parallel evaluation over batch dimensions) |
| **`jit`** | Just-in-time compilation to GPU/TPU via XLA |
| **`pmap`** | Parallel evaluation across multiple devices |

## Software

JAX is an open-source Python library for composable function transformations, first described by [[raw/papers/semanticscholar-39decd6e7d9f.md|Bradbury et al. (2018)]]. Its XLA-backed just-in-time compiler generates machine code for CPU, GPU, and TPU from a single NumPy-like API, delivering substantial performance gains over imperative array frameworks. In cosmological emulation, [[raw/papers/arxiv-2507.20990.md|Reeves et al. (2025)]] report that their JAX-based pipeline achieves three to four orders of magnitude speed-up over a standard Python implementation, evaluating one-loop power spectrum predictions in 1.2 ms on a CPU and 0.2 ms on a GPU; end-to-end Markov chain Monte Carlo inference then converges in minutes on a GPU rather than hours or days.

A hallmark of JAX as a software platform is its native support for automatic differentiation, which enables gradient-based optimization and differentiable programming without external autodiff toolkits. [[raw/papers/arxiv-2507.20990.md|Reeves et al. (2025)]] exploit this capability for Fisher forecasting and gradient-based parameter searches, while [[raw/papers/semanticscholar-39decd6e7d9f.md|Wang and Lai (2025)]] build physics-informed neural networks for ice-shelf data assimilation directly on JAX's automatic-differentiation primitives. Accessibility is reinforced by community packaging practices: [[raw/papers/semanticscholar-39decd6e7d9f.md|Wang and Lai (2025)]] distribute tutorial Colab notebooks with their solver so that users can reproduce results and adapt the code to new inverse problems.

Within whole-brain modeling, JAX operates less as a monolithic application and more as a portable execution backend. [[raw/papers/semanticscholar-9afbfd2d37be.md|Martin et al. (2025)]] show that the [[tvb-library|Virtual Brain]] Ontology can export standardized simulation metadata to executable JAX code alongside other platforms, bridging reproducible experiment descriptions with accelerator-ready performance. When combined with the GPU speed-ups reported by [[raw/papers/arxiv-2507.20990.md|Reeves et al. (2025)]] and the differentiable inverse-modeling capabilities demonstrated by [[raw/papers/semanticscholar-39decd6e7d9f.md|Wang and Lai (2025)]], this portability positions JAX as a practical substrate for large-scale, differentiable [[brain-dynamics|brain-network]] simulations.

## Related

- [[brainpy]] — [[brain-dynamics]] simulation framework built on JAX
- [[open-source-brain]] — TVB platform (future JAX integration planned)
- [[machine-learning]] — general ML concepts and tools

## References

- Bradbury et al. (2018) — JAX: composable transformations of Python+NumPy programs. https://github.com/google/jax