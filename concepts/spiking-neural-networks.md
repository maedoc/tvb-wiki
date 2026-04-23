---
created: 2026-04-20
sources:
- raw/papers/gewaltig-diesmann-2007.md
- raw/papers/potjans-diesmann-2014.md
- raw/papers/jordan-2018.md
- raw/papers/hines-carnevale-1997.md
- raw/papers/markram-2015.md
- raw/papers/arxiv-2510.02545.md
- raw/papers/strogatz-1994.md
- raw/papers/semanticscholar-71ffb8153870.md
tags:
- spiking-neural-networks
- software-nest
- software-neuron
- brain-network
- whole-brain-modeling
title: Spiking Neural Networks
type: concept
updated: '2026-04-23'
---

# Spiking Neural Networks

Spiking neural networks (SNNs) are computational models that simulate the dynamics of neurons generating discrete electrical pulses (spikes) in time.

## Definition

Unlike rate-based models that approximate neural activity as continuous firing rates, spiking neural networks explicitly model the generation, propagation, and timing of action potentials (spikes). This provides a more biologically realistic representation of neural communication.

## Model Types

### Point Neuron Models
- **Integrate-and-fire** — Simplified membrane potential integration
- **Adaptive exponential (AdEx)** — Spike frequency adaptation
- **Hodgkin-Huxley** — Detailed ion channel dynamics

Used primarily in [[NEST]] for large-scale networks

### Multi-Compartment Models
- **Cable theory** — Detailed dendritic and axonal morphology
- **Ion channel distributions** — Spatially varying conductances
- **Synaptic integration** — Complex dendritic computation

Used primarily in [[NEURON]] for detailed single-neuron studies

## Simulation Tools

- [[NEST]] — Large networks of point neurons (thousands to billions)
- [[NEURON]] — Multi-compartment detailed neuron models
- [[TVB]] — Can interface with SNNs via mean-field reductions

## Scalability

Jordan et al. (2018) demonstrated NEST scaling to:
- 10^11 synapses (approaching human cortex scale)
- Petascale supercomputers
- Near-perfect weak scaling from laptops to clusters

## Key Publications

- Gewaltig & Diesmann (2007) — NEST simulator introduction gewaltig-diesmann-2007
- Hines & Carnevale (1997) — NEURON simulation environment hines-carnevale-1997
- Potjans & Diesmann (2014) — Cortical microcircuit model potjans-diesmann-2014
- Markram et al. (2015) — Blue Brain cortical reconstruction markram-2015
- Jordan et al. (2018) — Exascale spiking simulations jordan-2018

## Related Concepts

- [[neural mass model]] — Simplified population-level alternative
- [[brain network]] — Network-level organization
- [[whole brain]] — Scaling to brain-wide simulations