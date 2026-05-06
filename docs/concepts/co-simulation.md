---
created: 2026-05-06
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/breakspear-2017.md
- raw/papers/ritter-2013.md
tags:
- co-simulation
- multi-scale-modeling
- spiking-neural-networks
- neural-mass-model
- coupling
title: Co-Simulation
type: concept
updated: '2026-05-06'
---

# Co-Simulation

**Co-simulation** is the practice of coupling multiple simulation engines to model phenomena across scales simultaneously. In [[computational-neuroscience]], it bridges spiking neuron-level dynamics with population-level [[neural-mass-models]].

## Relationship to TVB

TVB implements co-simulation by coupling its macroscale neural mass models with microscale spiking simulators ([[nest]], [[brian2]], [[neuron]]) via TVB-NEST and similar interfaces. This allows whole-brain TVB models to embed detailed cortical microcircuit dynamics in selected regions.