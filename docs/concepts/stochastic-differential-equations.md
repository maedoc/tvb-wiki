---
title: "Stochastic Differential Equations"
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [neural-mass-models, whole-brain-modeling, network-dynamics]
sources: [raw/papers/gardiner-2009.md, raw/papers/tuckwell-1988.md, raw/papers/deco-2008-stochastic.md, raw/papers/deco-2009-stochastic.md]
---

## Definition
Stochastic differential equations (SDEs) extend ordinary differential equations by including random noise terms, modeling systems with intrinsic or extrinsic fluctuations. Essential for capturing the probabilistic nature of neural dynamics.

## Mathematical Form

### Langevin Equation
- dx = f(x)dt + g(x)dW
- Deterministic drift: f(x)
- Stochastic diffusion: g(x)
- Wiener process: dW

### Itô vs Stratonovich
- Different stochastic calculi
- Itô: Non-anticipating
- Stratonovich: Physical interpretation
- Conversion between forms

## In Neuroscience

### Neural Noise Sources
- Synaptic noise
- Channel fluctuations
- Network finite-size effects
- External input variability

### Population Dynamics
- [[neural mass model]] with noise
- Fluctuation-driven dynamics
- deco-2008-stochastic — Stochastic brain dynamics

### Numerical Methods
- Euler-Maruyama scheme
- Milstein method (higher order)
- Stochastic Runge-Kutta
- Multiplicative noise handling

## Applications

### Resting-State
- [[resting state]] fluctuations
- Spontaneous activity patterns
- deco-2009-stochastic — Probabilistic models

### Whole-Brain Modeling
- [[whole brain]] stochastic simulations
- Individual variability
- Noise-induced transitions

## Analysis Methods
- [[fokker-planck equation]] for distributions
- Moment equations
- Linear noise approximation
- Monte Carlo simulation

## Related Concepts
- [[fokker-planck equation]] — Distribution dynamics
- [[mean field theory]] — Population averages
- [[neural mass model]] — Application domain

## References
- gardiner-2009 — Comprehensive handbook
- tuckwell-1988 — Neuroscience applications
- deco-2008-stochastic — Brain dynamics
