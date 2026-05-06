---
created: 2026-05-06
sources: []
tags:
- neural-simulation
- computational-neuroscience
- spiking-neural-networks
- neural-mass-model
- whole-brain-modeling
title: Neural Simulation
type: concept
updated: '2026-05-06'
---

# Neural Simulation

**Neural simulation** is the computational modeling of brain activity at levels ranging from individual neurons to entire brain networks. It provides a way to formalize theories of brain function, generate testable predictions, and link molecular and cellular mechanisms to behavior and cognition.

## Levels of Simulation

| Scale | Resolution | Examples | Tools |
|-------|-----------|----------|-------|
| Molecular | Ion channels, synapses | Hodgkin–Huxley, Markov models | NEURON, MOOSE |
| Single neuron | Compartmental models | Multi-compartment morphological models | NEURON, Arbor |
| Microcircuit | 10³–10⁵ neurons | Cortical columns, barrel cortex | NEST, Brian2 |
| Mesoscale | 10⁶–10⁸ neurons | Brain regions, area-level dynamics | TVB, ANNarchy |
| Macroscale / Whole brain | 10⁸–10¹¹ neurons | Global brain dynamics, cognition | [[the-virtual-brain|TVB]], TheBrain |

## Relationship to TVB

TVB operates primarily at the **macroscale** level, simulating whole-[[brain-dynamics]] using neural mass and [[mean-field-theory|mean-field]] models:
- TVB can **couple to microscale simulators** ([[nest]], [[nestml]], [[brian2]]) via co-simulation interfaces
- TVB's [[neural-mass-models]] are **derived from** lower-level spiking dynamics using mean-field approximations
- TVB integrates [[structural-connectivity]] data to constrain large-scale network simulations
- TVB generates predictions at the level of [[bold-signal|BOLD]] [[fmri]], EEG, and MEG that can be compared to empirical [[neuroimaging]]

## Related

- [[the-virtual-brain]] — whole-brain simulation platform
- [[spiking-neural-networks]] — neuron-level simulation
- [[neural-mass-model]] — population-level approximation
- [[co-simulation]] — multi-scale simulation coupling
- [[computational-neuroscience]] — broader field