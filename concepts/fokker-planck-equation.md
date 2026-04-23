---
created: 2026-04-20
sources:
- raw/papers/risken-1989.md
- raw/papers/gardiner-2009.md
- raw/papers/tuckwell-1988.md
- raw/papers/semanticscholar-0c97a15133c9.md
- raw/papers/semanticscholar-9afbfd2d37be.md
- raw/papers/arxiv-2508.19134.md
tags:
- neural-mass-models
- mean-field-theory
- parameter-estimation
title: Fokker-Planck Equation
type: concept
updated: '2026-04-24'
---

## Definition
The Fokker-Planck equation (also called forward Kolmogorov equation) describes the time evolution of the probability density function for the state of a system governed by stochastic differential equations. It provides an alternative to simulating individual trajectories.

## Mathematical Form

### General Form
- ∂p/∂t = -∂/∂x[μ(x)p] + ∂²/∂x²[D(x)p]
- Drift term: μ(x) (mean velocity)
- Diffusion term: D(x) (spreading rate)

### For Neural Systems
- Population density approach
- Membrane potential distribution
- Firing rate from boundary conditions

## Solution Methods

### Analytical Techniques
- Eigenfunction expansions
- Fourier transforms
- Path integrals
- risken-1989 methods

### Numerical Methods
- Finite difference schemes
- Finite element methods
- Spectral methods
- Matrix continued fractions

## Applications in Neuroscience

### Population Density
- Distribution of membrane potentials
- schwalger-deger-gerstner-2017 — Population equations
- Exact macroscopic dynamics

### First Passage Times
- Time to threshold crossing
- Interspike interval distributions
- Escape rate theory

### Neural Mass Models
- Stochastic [[neural mass model]] analysis
- Noise-induced transitions
- Stationary distributions

## Relationship to SDEs
- Equivalent descriptions
- SDE: Trajectory level
- Fokker-Planck: Distribution level
- Monte Carlo vs. PDE solution

## Related Concepts
- [[stochastic differential equations]] — Equivalent formulation
- [[mean field theory]] — Population-level analysis
- [[neural mass model]] — Application domain

## References
- risken-1989 — Definitive reference
- gardiner-2009 — Solution methods
- tuckwell-1988 — Neural applications