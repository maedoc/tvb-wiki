---
title: MUSIC
created: 2024-01-15
updated: 2026-04-28
type: entity
tags: [software-neurons, software-modeling, spiking-neural-networks, neural-mass-models, software-brian, software-nest, software-neuron]
sources:
  - "[Ekeberg & Djurfeldt, 2008](https://doi.org/10.1038/npre.2008.1830.1)"
  - "[Djurfeldt et al., 2010](https://doi.org/10.1007/s12021-010-9064-z)"
---

# MUSIC

## Overview

**MUSIC** (MUlti-SImulator Coordinator) is a C++ library with Python bindings designed for co-simulation of spiking neural networks across multiple neuronal simulators running in parallel. Originally developed by researchers at the Royal Institute of Technology (KTH) Stockholm and initiated by the International Neuroinformatics Coordinating Facility (INCF), MUSIC provides a standardized API that allows different simulators—such as [[nest]], [[neuron]], [[brian2]], and other [[spiking-neural-networks]] engines—to communicate in real-time during a unified simulation. This orchestration capability enables researchers to build hybrid models that leverage the strengths of multiple simulation environments, combining, for example, the detailed biophysics of NEURON with the large-scale population dynamics supported by NEST.

The framework operates by establishing a communication bus through which simulators exchange spike events and continuous signals during each simulation timestep. Rather than requiring all components of a model to be implemented within a single simulator, MUSIC empowers researchers to partition biologically realistic brain networks across heterogeneous computational resources, allocating specific brain regions or cell types to whichever simulator best handles their computational demands.

## Motivation and Context

Computational neuroscience has long grappled with the fundamental trade-off between biological realism and simulation scale. Detailed [[hodgkin-huxley-model]] formulations can capture the nuanced dynamics of individual neurons and synapses, but their computational cost becomes prohibitive when modeling the millions of neurons and billions of synapses comprising realistic brain circuits. Conversely, [[neural-mass-model]] approaches and simplified point neuron representations—such as the [[izhikevich-neuron-model]] or [[adaptive-exponential-integrate-and-fire]] formulations—enable simulations at brain-scale, but often sacrifice the biophysical fidelity necessary for certain research questions.

Prior to MUSIC, researchers seeking to combine these approaches faced substantial engineering challenges. Simulations had to be conducted sequentially, with output from one simulator serving as input to another—a process that introduced temporal artifacts and eliminated the possibility of true bidirectional interaction. MUSIC emerged as a solution to this fragmentation problem, providing a unified temporal framework in which multiple simulators advance in lockstep while continuously exchanging data. This capability proved particularly valuable for modeling brain systems where microcircuit-level details (such as specific ion channel configurations or dendritic morphologies) interact with macrocircuit-level dynamics (such as [[brain-oscillations]] or [[resting-state]] network activity).

The development of MUSIC also aligned with the broader push toward [[reproducibility]] in computational neuroscience. By providing a standard interface for multi-simulator workflows, MUSIC enables researchers to document and share complex hybrid models with greater transparency, facilitating collaboration across labs that may prefer different underlying simulation engines.

## Technical Description

MUSIC implements a publisher-subscriber messaging pattern built atop the Message Passing Interface (MPI), allowing distributed simulations to synchronize and communicate with minimal overhead [@sources[0]]. Each participating simulator registers output mappings—specifying which neuronal populations will transmit spikes or analog signals—and input mappings—that define which signals the simulator expects to receive from other participants. During simulation initialization, MUSIC constructs a routing table that directs these communications across the computational cluster.

The framework supports three port types: continuous ports for multi-dimensional time-series such as membrane voltages; event ports for time-stamped integer identifiers such as neuronal spikes; and message ports for string-based communication [@sources[1]]. This flexibility allows MUSIC to accommodate diverse model architectures, from pure [[spiking-neural-networks]] implementations to hybrid schemes that combine rate-based [[neural-mass-model]] approximations with detailed spiking neurons.

A typical MUSIC workflow begins with model decomposition: the researcher identifies which brain regions or cell populations will be simulated in which engine, then configures output and input proxies for each partition. These configurations are specified in a MUSIC configuration file that defines the ports, their widths (number of data elements), and the connections between them. The simulation launcher then spawns multiple MPI processes, each running a distinct simulator with its MUSIC proxy active, and coordinates their execution through a shared timeline. During the runtime phase, each simulator calls the MUSIC tick() function at regular intervals, allowing data transfer to occur while maintaining synchronization across all participating applications.

## Relationship to TVB and Whole-Brain Modeling

While [[the-virtual-brain]] (TVB) primarily operates at the level of [[neural-mass-model]] and [[whole-brain-modeling]]—simulating large-scale brain regions as coupled oscillators or mean-field units—MUSIC operates at the finer granularity of spiking neuron networks. However, the two frameworks are complementary in the broader ecosystem of brain modeling. TVB can serve as a mean-field wrapper around MUSIC-based spiking networks, using output from detailed microcircuit simulations to inform the parameters of its reduced models. Conversely, MUSIC-based simulators can receive slow-varying control signals from TVB, implementing closed-loop architectures where large-scale network states modulate fine-grained neuronal dynamics.

## Relationship to Other Software

MUSIC occupies a unique niche as an orchestration layer rather than a standalone simulator. It builds upon the MPI standard widely used in high-performance computing and draws inspiration from earlier multi-process coordination efforts in computational neuroscience. Unlike [[nest]] or [[brian2]], which provide complete simulation environments, MUSIC provides only the communication fabric—the actual neuronal dynamics must be supplied by the partnered simulators. The framework shares conceptual ground with [[netpyne]] and [[annarchy]] in enabling hybrid model architectures, though those tools focus on code generation and optimization within single simulators rather than true cross-simulator coordination.

## Key Features

- **Parallel execution**: Multiple simulators run simultaneously with clock synchronization
- **MPI-based communication**: Efficient message passing across distributed compute nodes
- **Spike and analog signal support**: Accommodates both discrete and continuous data types
- **Flexible routing**: Configurable output/input mappings enable arbitrary network topologies
- **Simulator independence**: Partners can be NEST, NEURON, Brian, or custom implementations

## Key Papers

- Ekeberg, Ö., & Djurfeldt, M. (2008). MUSIC - Multisimulation Coordinator: Request For Comments. Nature Precedings. https://doi.org/10.1038/npre.2008.1830.1
- Djurfeldt, M., Hjorth, J., Eppler, J. M., Dudani, N., Helias, M., Potjans, T. C., ... & Ekeberg, Ö. (2010). Run-Time Interoperability Between Neuronal Network Simulators Based on the MUSIC Framework. Neuroinformatics, 8(1), 43-60. https://doi.org/10.1007/s12021-010-9064-z

## Open Questions

The primary challenge facing MUSIC lies in ensuring temporal accuracy when simulators with different intrinsic timesteps must coordinate. While the framework provides mechanisms for interpolation and event buffering, mismatches in simulation resolution can introduce artifacts that are only beginning to be systematically characterized. Additionally, the user base remains relatively small compared to standalone simulators, limiting the availability of community resources, tutorials, and third-party integrations. Future development may benefit from tighter integration with [[neuroml]] standardization efforts, which seek to define common model description formats that could further reduce friction in multi-simulator workflows.

## References

1. Ekeberg, Ö., & Djurfeldt, M. (2008). MUSIC - Multisimulation Coordinator: Request For Comments. Nature Precedings. https://doi.org/10.1038/npre.2008.1830.1
2. Djurfeldt, M., Hjorth, J., Eppler, J. M., Dudani, N., Helias, M., Potjans, T. C., Bhalla, U. S., Diesmann, M., Hellgren Kotaleski, J., & Ekeberg, Ö. (2010). Run-Time Interoperability Between Neuronal Network Simulators Based on the MUSIC Framework. Neuroinformatics, 8(1), 43-60. https://doi.org/10.1007/s12021-010-9064-z