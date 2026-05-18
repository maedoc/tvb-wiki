---
created: 2026-05-06
sources:
- raw/papers/arxiv-2507.20990.md
- raw/papers/semanticscholar-9afbfd2d37be.md
- raw/papers/semanticscholar-39decd6e7d9f.md
- raw/papers/semanticscholar-2d6ce9a9b368.md
- raw/papers/deistler-2025-jaxley.md
tags:
- jax
- machine-learning
- differentiable-programming
- python
- numerical-computing
title: JAX
type: entity
updated: '2026-05-18'
---

# JAX

**JAX** is a high-performance numerical computing library that combines Autograd (automatic differentiation) and XLA (Accelerated [[linear]] Algebra). Developed by Google, JAX enables composable transformations of Python/NumPy functions: automatic differentiation, vectorisation via `vmap`, parallelisation via `pmap`, and just-in-time compilation to GPU/TPU via `jit`.

## Overview

JAX’s functional programming model and array-level parallelism make it well-suited to:
- **[[neural-network]] training** — natively via [Flax](](https://github.com/google/[[flax]])) or [Equinox](](https://github.com/patrick-kidger/equinox))
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
The Virtual Brain Ontology (TVB-O) treats JAX as a simulation platform alongside [[the-virtual-brain]] and Julia, generating executable simulation code and exporting FAIR metadata and provenance-aware reports from model specifications [[raw/papers/semanticscholar-9afbfd2d37be.md|Martin et al. (2025)]]. [[raw/papers/semanticscholar-39decd6e7d9f.md|Wang & Lai (2025)]] distribute DIFFICE-jax as a user-friendly [[python]] library written in JAX, providing tutorial examples with Colab notebooks so users at different levels can reproduce the results and modify the code for their specific problems of interest [[raw/papers/semanticscholar-39decd6e7d9f.md|Wang & Lai (2025)]]. [[raw/papers/arxiv-2507.20990.md|Reeves et al. (2025)]] distribute PyBird-JAX as a differentiable implementation that supports Fisher forecasting, Taylor expansion of model predictions, and gradient-based searches through automatic differentiation, interfacing with a variety of samplers and Boltzmann solvers to provide a high-performance inference pipeline that achieves one-loop galaxy power spectrum predictions in 1.2 ms on CPU and 0.2 ms on GPU—three to four orders of magnitude faster than the original PyBird [[raw/papers/arxiv-2507.20990.md|Reeves et al. (2025)]]. Taken together, these three projects demonstrate that JAX supports differentiable, high-performance computing across cosmology, glaciology, and brain network modeling alike [[raw/papers/arxiv-2507.20990.md|Reeves et al. (2025)]][[raw/papers/semanticscholar-39decd6e7d9f.md|Wang & Lai (2025)]][[raw/papers/semanticscholar-9afbfd2d37be.md|Martin et al. (2025)]].
## Related

- [[brainpy]] — [[brain-dynamics]] simulation framework built on JAX
- [[open-source-brain]] — TVB platform (future JAX integration planned)
- [[machine-learning]] — general ML concepts and tools

## References

1. Alexander Reeves, Pierre Zhang, Henry Zheng. (2025). *PyBird-JAX: Accelerated inference in large-scale structure with model-independent emulation of one-loop galaxy power spectra*. Journal of Cosmology and Astroparticle Physics. [DOI](https://doi.org/10.1088/1475-7516/2026/02/016)
2. Leon Martin, Konstantin Bülau, Marius Pille, Rico Schmitt, Christoph Hüttl, J. Meier, Halgurd Taher, Dionysios Perdikis, M. Schirner, L. Stefanovski, [[petra-ritter]]. (2025). *[[tvb|The Virtual Brain]] Ontology: A Digital Knowledge Framework for Reproducible [[brain-network]] Modeling*. bioRxiv. [DOI](https://doi.org/10.1101/2025.11.19.689211)
3. Yongjian Wang, Ching‐Yao Lai. (2025). *DIFFICE-jax: Differentiable neural-network solver for data assimilation of ice shelves in JAX*. Journal of Open Source Software. [DOI](https://doi.org/10.21105/joss.07254)
4. Eric C. Cyr, Jens Hahne, Nicholas S. Moore, Jacob B. Schroder, Ben S. Southworth, David A. Vargas. (2025). *TorchBraid: High-Performance Layer-Parallel Training of Deep Neural Networks with MPI and GPU Acceleration*. ACM Transactions on Mathematical Software. [DOI](https://doi.org/10.1145/3759244)
5. Deistler, Michael and Kadhim, Kyra L and Pals, Matthijs and Beck, Jonas and Huang, Ziwei and Gloeckler, Manuel and Lappalainen, Janne K and Schröder, Cornelius and Berens, Philipp and Goncalves, Pedro J and Macke, Jakob H. *[[jaxley]]: differentiable simulation enables large-scale training of detailed biophysical models of neural dynamics*. Nature Methods. [DOI](https://doi.org/10.1038/s41592-025-02895-w)