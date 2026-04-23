---
created: 2026-04-23
sources:
- raw/papers/jordan-2018.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/helias-2012.md
- raw/papers/arxiv-2509.02799.md
tags:
- software-brain-modeling
- spiking-neural-networks
- rate-coded-neural-networks
- whole-brain-modeling
title: ANNarchy
type: entity
updated: '2026-04-23'
---

# ANNarchy

## Overview

**ANNarchy** is an open-source Python library for large-scale simulations of rate-coded and spiking neural networks. Developed by Vitay, Dinkelbach, and Hamker, ANNarchy bridges the gap between detailed [[spiking-neural-networks]] and rate-based population models by supporting both paradigms within a unified framework. It compiles high-level Python model descriptions into optimized C++ code with optional CUDA support for GPU acceleration, enabling simulations of millions of neurons.

The framework is designed for computational neuroscientists who need to scale from single-neuron dynamics to large-scale modeling while maintaining performance and biological plausibility.

## Key Features

### Hybrid Neural Network Support
- **Rate-coded networks**: Mean-field approximations for population-level dynamics
- **Spiking networks**: Integrate-and-fire, Hodgkin-Huxley, and custom neuron models
- **Mixed simulations**: Rate and spiking populations can interact in the same model
- **Gap junctions**: Support for electrical synapses between neurons

### High-Performance Backend
- **Code generation**: Python model specification compiles to optimized C++
- **GPU acceleration**: CUDA backend for NVIDIA GPUs
- **Parallel computing**: OpenMP support for multi-core CPUs
- **Scalability**: Simulations of millions of neurons and billions of synapses

### Neural Modeling Capabilities
- **Neuron models**: Leaky integrate-and-fire, Izhikevich, FitzHugh-Nagumo, and user-defined ODEs
- **Synaptic models**: Current-based and conductance-based synapses, STDP, homeostatic plasticity
- **Structural plasticity**: Dynamic rewiring of connections
- **Dopaminergic modulation**: Reward-modulated learning rules

### Data Integration
- **Neuroimaging compatibility**: Built-in tools for generating [[fmri]] and [[eeg]] predictions
- Visualization of synaptic weights and neural activity
- Integration with the NeuralEnsemble ecosystem

## Relationship to TVB

[[TVB]] and ANNarchy occupy complementary positions in the whole-brain modeling landscape:

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
3. **Bridging scales**: Both frameworks can inform each other—TVB provides the large-scale connectivity context while ANNarchy provides detailed cellular mechanisms

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
- [[elephant]] – Analysis toolkit for electrophysiology data from simulations

## References

1. Vitay, J., Dinkelbach, H. Ü., & Hamker, F. H. (2015). ANNarchy: a code generation approach to neural simulations on parallel hardware. *Frontiers in Neuroinformatics*, 9, 19. https://doi.org/10.3389/fninf.2015.00019

2. Dinkelbach, H. Ü., Vitay, J., & Hamker, F. H. (2015). Comparison of GPU- and CPU-implementations of mean-field models of spiking neural networks. *Frontiers in Neuroinformatics*, 9, 17. https://doi.org/10.3389/fninf.2015.00017

3. Hamker, F. H., Zirnsak, M., Ziesche, A., & Lappe, M. (2017). Computational models of spatial attention in the barn owl. In *Computational and Cognitive Neuroscience of Vision* (pp. 69-101). Springer.

4. ANNarchy documentation: [https://annarchy.readthedocs.io](https://annarchy.readthedocs.io)

5. GitHub repository: [https://github.com/annarchy/annarchy](https://github.com/annarchy/annarchy)

---

*Note: ANNarchy is actively maintained and provides a unique capability for hybrid rate/spiking simulations that can validate or extend [[TVB]]'s mean-field approaches through detailed spiking implementations.*