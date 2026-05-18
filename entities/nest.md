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
updated: '2026-05-18'
---

# NEST (NEural Simulation Tool)

NEST (NEural Simulation Tool) is a simulator specifically designed for large networks of point neurons with biologically realistic synaptic dynamics and plasticity rules [[raw/papers/gewaltig-diesmann-2007.md|Gewaltig & Diesmann (2007)]]. Built around an efficient kernel for spike communication and time-stepping, it supports networks ranging from thousands to billions of neurons, making it one of the most widely used platforms for [[spiking-neural-networks|spiking neural network]] research in [[computational-neuroscience]]. Its architecture enables distributed simulation through MPI and OpenMP, allowing researchers to scale models from consumer laptops to high-performance computing clusters. A hallmark of NEST's scientific adoption is the canonical data-driven cortical microcircuit model developed by Potjans and Diesmann, which spans layers 2/3 through 6 with connectivity derived from anatomical and electrophysiological data, reproducing layer- and cell-type-specific firing rates consistent with in vivo recordings and serving as a standard benchmark for spiking network validation [[raw/papers/potjans-diesmann-2014.md|Potjans & Diesmann (2014)]]. More recently, Jordan and colleagues demonstrated near-perfect weak scaling from laptops to petascale supercomputers with hundreds of thousands of cores, achieving simulations of up to 10^11 synapses—approaching the scale of the human cortex—through a five-step communication scheme and memory-efficient data structures that minimize inter-node overhead [[raw/papers/jordan-2018.md|Jordan et al. (2018)]]. These advances establish NEST as a pathway toward biologically realistic [[whole-brain-modeling|whole-brain]] spiking simulations on forthcoming exascale systems, bridging single-circuit dynamics with [[brain-network|brain-scale]] computation.

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
- [[model-validation]] — Repository for sharing NEST and other simulator models

## Related Concepts

- [[spiking neural networks]] — Detailed spiking neuron dynamics
- [[brain network]] — Large-scale network simulations
- [[whole brain]] — Whole-brain modeling approaches
- [[tvb-vs-nest-vs-neuron|Tvb Vs Nest Vs Neuron]]
- [[tvb-multiscale|Tvb Multiscale]]
## Key Researchers
Markus Diesmann has been the central architect and lead researcher behind NEST since its inception, co-authoring the original simulator introduction alongside Marc-Oliver Gewaltig [[raw/papers/gewaltig-diesmann-2007.md|Gewaltig & Diesmann (2007)]] and guiding its evolution toward large-scale [[spiking-neural-networks|spiking network]] simulations. Diesmann's leadership spans the core kernel design, the canonical data-driven cortical microcircuit model developed with Tobias C. Potjans [[raw/papers/potjans-diesmann-2014.md|Potjans & Diesmann (2014)]], and strategic high-performance computing benchmarking alongside Moritz Helias and Susanne Kunkel that established NEST as a discovery tool for [[computational-neuroscience]] [[raw/papers/helias-2012.md|Helias et al. (2012)]]. This sustained, multi-decade involvement across foundational publications makes him the single most consistent scientific voice in NEST's development.

The simulator's technical capabilities reflect parallel advances by researchers who targeted distinct scaling and usability bottlenecks. Jakob Jordan spearheaded the exascale communication architecture, implementing the five-step communication scheme that enabled near-perfect weak scaling from laptops to petascale systems containing up to 10^11 synapses [[raw/papers/jordan-2018.md|Jordan et al. (2018)]]. Jochen Martin Eppler created the [[pynest]] Python interface, lowering the programming barrier and broadening NEST's integration with the broader scientific Python ecosystem [[raw/papers/eppler-2009.md|Eppler (2009)]]. Helias and Kunkel further cemented NEST's high-performance computing credentials by benchmarking the simulator across leadership-class facilities and identifying the hardware requirements necessary for brain-scale [[brain-network]] simulations [[raw/papers/helias-2012.md|Helias et al. (2012)]]. Through these complementary contributions, the NEST team transformed a specialized kernel into a comprehensive platform spanning rapid model prototyping, canonical circuit validation, and exascale whole-brain simulation.
## Use Cases

- Cortical microcircuit simulations
- Large-scale spiking [[network-dynamics]]
- [[synaptic-plasticity]] and learning studies
- Exascale neuroscience computing benchmarks

## References

1. Gewaltig & Diesmann (2007). *NEST ([[neural-simulation]] Tool)*. Scholarpedia. [DOI](https://doi.org/10.4249/scholarpedia.1430)
2. Potjans & Diesmann (2014). *The cell-type specific cortical microcircuit: relating structure and activity*. Cerebral Cortex. [DOI](https://doi.org/10.1093/cercor/bhs358)
3. Jordan et al. (2018). *Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2018.00002)
4. Eppler et al. (2009). *PyNEST: A convenient interface to the NEST simulator*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/neuro.11.012.2008)
5. Helias et al. (2012). *Supercomputers ready for use as discovery machines for neuroscience*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2012.00026)
6. Sanz Leon et al. (2013). *[[the-virtual-brain]]: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)