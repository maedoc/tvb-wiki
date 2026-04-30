---
created: 2026-04-23
sources:
- raw/papers/jordan-2018.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/helias-2012.md
- raw/papers/arxiv-2509.02799.md
- raw/papers/arxiv-2507.22146.md
- raw/papers/semanticscholar-5c84b271b035.md
tags:
- software-brain-modeling
- spiking-neural-networks
- rate-coded-neural-networks
- whole-brain-modeling
title: ANNarchy
type: entity
updated: '2026-04-30'
---

# ANNarchy

## Overview

**ANNarchy** is an open-source Python library for large-scale simulations of rate-coded and spiking neural networks. Developed by Vitay, Dinkelbach, and Hamker, ANNarchy bridges the gap between detailed [[spiking-neural-networks]] and rate-based population models by supporting both paradigms within a unified framework. It compiles high-level Python model descriptions into optimized C++ code with optional CUDA support for GPU acceleration, enabling simulations of millions of neurons.

The framework is designed for computational neuroscientists who need to scale from single-neuron dynamics to large-scale modeling while maintaining performance and biological plausibility.

## Key Features

### Hybrid Neural Network Support
- **Rate-coded networks**: [[mean-field-theory|Mean-field]] approximations for population-level dynamics
- **Spiking networks**: Integrate-and-fire, Hodgkin-Huxley, and custom neuron models
- **Mixed simulations**: Rate and spiking populations can interact in the same model
- **Gap junctions**: Support for electrical synapses between neurons

### High-Performance Backend
- **Code generation**: Python model specification compiles to optimized C++
- **GPU acceleration**: CUDA backend for NVIDIA GPUs
- **Parallel computing**: OpenMP support for multi-core CPUs
- **Scalability**: Simulations of millions of neurons and billions of synapses

### Neural Modeling Capabilities
- **Neuron models**: Leaky integrate-and-fire, [[izhikevich]], FitzHugh-Nagumo, and user-defined ODEs
- **Synaptic models**: Current-based and conductance-based synapses, STDP, homeostatic [[plasticity]]
- **Structural plasticity**: Dynamic rewiring of connections
- **Dopaminergic modulation**: Reward-modulated learning rules

### Data Integration
- **[[neuroimaging]] compatibility**: Built-in tools for generating [[fmri]] and [[eeg]] predictions
- Visualization of synaptic weights and neural activity
- Integration with the NeuralEnsemble ecosystem

## Relationship to TVB

[[TVB]] and ANNarchy occupy complementary positions in the [[whole-brain]] modeling landscape:

| Aspect | TVB | ANNarchy |
|--------|-----|----------|
| **Level of detail** | Neural mass and mean-field | Single neuron to population |
| **Default dynamics** | Continuum, rate-based | Spiking and rate-coded |
| **Structural connectivity** | Uses [[structural-connectivity]] from DTI | User-defined or imported |
| **Performance optimization** | NumPy/OpenMP | C++/CUDA code generation |
| **Typical scale** | Whole-brain networks | Flexible (local to brain-scale) |

**Complementary use cases:**

1. **Hybrid modeling**: TVB's mean-field models can be compared against ANNarchy's spiking implementations of equivalent dynamics
2. **Validation**: ANNarchy's detailed spiking simulations can validate TVB's population-level approximations
3. **Bridging scales**: Both frameworks can inform each other—TVB provides the large-scale [[connectivity]] context while ANNarchy provides detailed cellular mechanisms

ANNarchy is particularly valuable when researchers need to verify that mean-field approximations accurately reflect the underlying spiking dynamics, or when GPU acceleration is required for rate-coded simulations.

## Key Papers

- **Vitay et al., 2015** – Original ANNarchy publication introducing the code generation approach for rate-coded and spiking networks
- **Dinkelbach et al., 2015** – Performance benchmarking demonstrating CUDA acceleration capabilities
- **Hamker et al., 2017** – Applications to large-scale cortical modeling and attention networks

## Related Software

- [[TVB]] – Whole-brain neural mass modeling with focus on connectivity
- [[NEST]] – Event-driven simulation of large-scale spiking networks
- [[brian]] – Flexible Python spiking network simulator with code generation
- [[neuron]] – Detailed compartmental modeling of individual neurons
- [[elephant]] – Analysis toolkit for [[electrophysiology]] data from simulations

## References

1. Jordan et al. (2018). *Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2018.00002)
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *[[arbor]]-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](https://doi.org/10.3389/fncom.2025.1731161)
3. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *Arbor-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](https://arxiv.org/abs/2505.16861)
4. Helias et al. (2012). *Supercomputers ready for use as discovery machines for neuroscience*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2012.00026)
5. Martin Breyton, Viktor Sip, M. Woodman, Meysam Hashemi, S. Petkoski, V. Jirsa. (2025). *Data-driven mean-field within whole-brain models*. [Link](https://www.semanticscholar.org/paper/144ae1f1dabec42c14493d0083d36f168508f886)
6. J. Bose. (2025). *Pendulum Model of Spiking Neurons*. arXiv.org. [DOI](https://doi.org/10.48550/arXiv.2507.22146)
7. C. Linssen, Pooja N. Babu, Jochen M. Eppler, Luca Koll, Bernhard Rumpe, Abigail Morrison. (2025). *NESTML: a generic modeling language and code generation tool for the simulation of spiking neural networks with advanced plasticity rules*. Frontiers Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2025.1544143)