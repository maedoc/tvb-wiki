---
created: 2026-04-20
sources:
- raw/papers/gewaltig-diesmann-2007.md
- raw/papers/potjans-diesmann-2014.md
- raw/papers/jordan-2018.md
- raw/papers/eppler-2009.md
- raw/papers/helias-2012.md
- raw/papers/sanz-leon-2013.md
tags:
- software-nest
- spiking-neural-networks
- brain-network
title: NEST
type: entity
updated: '2026-05-04'
---

# NEST (NEural Simulation Tool)

NEST is a simulator for spiking [[neural-network]] models, widely used in [[computational-neuroscience]].
[[fooof]]

## Overview

NEST is specifically designed for large networks of point neurons with biologically realistic synaptic dynamics and [[plasticity]] rules. Built around an efficient kernel for spike communication and time-stepping, NEST supports networks ranging from thousands to billions of neurons.

## Key Features

- **Point neuron models**: Efficient simulation of integrate-and-fire and Hodgkin-Huxley type neurons
- **Biologically realistic synapses**: Detailed synaptic dynamics and plasticity rules
- **Massive scalability**: From laptops to petascale supercomputers (10^11+ synapses)
- **Parallel computing**: MPI and OpenMP support for distributed simulation
- **[[pynest]] interface**: Python API for rapid prototyping and scientific workflow integration
- **Canonical microcircuits**: Reference implementations like the Potjans-Diesmann cortical model

## Scalability

Jordan et al. (2018) demonstrated NEST's near-perfect weak scaling:
- Consumer laptops to petascale supercomputers
- Hundreds of thousands of cores
- Up to 10^11 synapses (approaching human cortex scale)
- Five-step communication scheme for efficiency

## Key Publications

- Gewaltig & Diesmann (2007) — NEST introduction gewaltig-diesmann-2007
- Potjans & Diesmann (2014) — Cortical microcircuit model potjans-diesmann-2014
- Jordan et al. (2018) — Exascale scalability jordan-2018
- Eppler et al. (2009) — PyNEST Python interface eppler-2009
- Helias et al. (2012) — HPC benchmarking helias-2012

## Related Software

- [[TVB]] — [[neural-mass-models|Neural mass model]] simulator for whole-[[brain-dynamics]]
- [[NEURON]] — Multi-compartment detailed neuron simulations
- [[ModelDB]] — Repository for sharing NEST and other simulator models

## Related Concepts

- [[spiking neural networks]] — Detailed spiking neuron dynamics
- [[brain network]] — Large-scale network simulations
- [[whole brain]] — Whole-brain modeling approaches
- [[tvb-vs-nest-vs-neuron|Tvb Vs Nest Vs Neuron]]
- [[tvb-multiscale|Tvb Multiscale]]
## Key Researchers

- [[Markus Diesmann]] — Core NEST developer and lead researcher

## Use Cases

- Cortical microcircuit simulations
- Large-scale spiking [[network-dynamics]]
- [[synaptic-plasticity]] and learning studies
- Exascale neuroscience computing benchmarks

## References

1. Gewaltig & Diesmann (2007). *NEST (NEural Simulation Tool)*. Scholarpedia. [DOI](https://doi.org/10.4249/scholarpedia.1430)
2. Potjans & Diesmann (2014). *The cell-type specific cortical microcircuit: relating structure and activity*. Cerebral Cortex. [DOI](https://doi.org/10.1093/cercor/bhs358)
3. Jordan et al. (2018). *Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2018.00002)
4. Eppler et al. (2009). *PyNEST: A convenient interface to the NEST simulator*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/neuro.11.012.2008)
5. Helias et al. (2012). *Supercomputers ready for use as discovery machines for neuroscience*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2012.00026)
6. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)