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
updated: '2026-04-23'
---

# NEST (NEural Simulation Tool)

NEST is a simulator for spiking neural network models, widely used in computational neuroscience.

## Overview

NEST is specifically designed for large networks of point neurons with biologically realistic synaptic dynamics and plasticity rules. Built around an efficient kernel for spike communication and time-stepping, NEST supports networks ranging from thousands to billions of neurons.

## Key Features

- **Point neuron models**: Efficient simulation of integrate-and-fire and Hodgkin-Huxley type neurons
- **Biologically realistic synapses**: Detailed synaptic dynamics and plasticity rules
- **Massive scalability**: From laptops to petascale supercomputers (10^11+ synapses)
- **Parallel computing**: MPI and OpenMP support for distributed simulation
- **PyNEST interface**: Python API for rapid prototyping and scientific workflow integration
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

- [[TVB]] — Neural mass model simulator for whole-brain dynamics
- [[NEURON]] — Multi-compartment detailed neuron simulations
- [[ModelDB]] — Repository for sharing NEST and other simulator models

## Related Concepts

- [[spiking neural networks]] — Detailed spiking neuron dynamics
- [[brain network]] — Large-scale network simulations
- [[whole brain]] — Whole-brain modeling approaches

## Key Researchers

- [[Markus Diesmann]] — Core NEST developer and lead researcher

## Use Cases

- Cortical microcircuit simulations
- Large-scale spiking network dynamics
- Synaptic plasticity and learning studies
- Exascale neuroscience computing benchmarks