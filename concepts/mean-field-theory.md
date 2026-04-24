---
created: 2026-04-20
sources:
- raw/papers/amit-brunel-1997.md
- raw/papers/brunel-2000.md
- raw/papers/montbrio-pazo-roxin-2015.md
- raw/papers/schwalger-deger-gerstner-2017.md
- raw/papers/potjans-diesmann-2014.md
- raw/papers/stefanescu-jirsa-2008.md
- raw/papers/arxiv-2603.28931.md
tags:
- neural-mass-models
- spiking-neural-networks
- whole-brain-modeling
title: Mean Field Theory
type: concept
updated: '2026-04-24'
---

## Definition
Mean field theory approximates the behavior of large networks by averaging over microscopic details, deriving macroscopic equations for population-averaged quantities. It bridges single-neuron and population-level descriptions.

## Mathematical Framework

### Population Averaging
- Replace individual neurons with mean rates
- Fluctuations treated as noise
- Self-consistency equations

### Wilson-Cowan Approach
- Population firing rates
- Sigmoid activation functions
- Coupled excitatory-inhibitory dynamics

### Modern Derivations
- montbrio-pazo-roxin-2015 — Exact reduction for QIF
- schwalger-deger-gerstner-2017 — Population density
- Renewal theory approaches

## Network States

### Asynchronous Irregular (AI)
- Low-rate, irregular spiking
- Balanced excitation-inhibition
- brunel-2000 analysis

### Synchronous Regular (SR)
- High-rate, regular spiking
- Strong recurrent excitation

### Oscillatory States
- Fast oscillations from inhibition
- brain oscillations emergence

## Applications

### Neural Mass Models
- [[neural mass model]] foundation
- [[jansen-rit]] and [[wilson-cowan]]
- Mesoscopic brain dynamics

### Whole-Brain Modeling
- [[whole brain]] simulations
- Coupled population dynamics
- [[structural connectivity]] constraints

## Limitations
- Finite-size effects
- Correlation structure
- Spatial heterogeneity
- Strong coupling regimes

## Related Concepts
- [[neural mass model]] — Application
- [[spiking neural networks]] — Microscopic level
- [[stochastic differential equations]] — Noise treatment

## References
- amit-brunel-1997 — Balanced networks
- brunel-2000 — Network states
- montbrio-pazo-roxin-2015 — Exact reduction