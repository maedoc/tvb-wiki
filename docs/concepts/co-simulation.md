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
updated: '2026-05-07'
---

# Co-Simulation

**Co-simulation** is the practice of coupling multiple simulation engines to model phenomena across scales simultaneously. In [[computational-neuroscience]], it bridges spiking neuron-level dynamics with population-level [[neural-mass-models]].

## Relationship to TVB

TVB implements co-simulation by coupling its macroscale neural mass models with microscale spiking simulators ([[nest]], [[brian2]], [[neuron]]) via TVB-NEST and similar interfaces. This allows whole-brain TVB models to embed detailed cortical microcircuit dynamics in selected regions.

## References

1. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](](https://doi.org/10.1038/s41593-017-0015-4))
3. Ritter et al. (2013). *[[tvb|The Virtual Brain]] integrates computational modeling and multimodal [[neuroimaging]]*. Brain [[connectivity]]. [DOI](](https://doi.org/10.1089/brain.2012.0120))