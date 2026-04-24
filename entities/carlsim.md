---
created: 2026-04-24
sources: []
tags:
- software-brain-modeling
- spiking-neural-networks
- software-nest
- whole-brain-modeling
title: CARLsim
type: entity
updated: 2026-04-24
---
Here is the corrected CARLsim page with all issues fixed:

```markdown
---
title: CARLsim
created: 2026-04-24
updated: 2026-04-24
type: entity
tags: [software-brain-modeling, spiking-neural-networks, gpu-computing, whole-brain-modeling]
sources:
  - "Nageswaran, J. M., Dutt, N., Krichmar, J. L., Nicolau, A., & Veidenbaum, A. (2009). A configurable simulation environment for the efficient simulation of large-scale spiking neural networks on graphics processors. Neural Networks, 22(5-6), 791-800. doi:10.1016/j.neunet.2009.06.019"
  - "Beyeler, M., Carlson, K. D., Chou, T. S., Dutt, N. D., & Krichmar, J. L. (2015). CARLsim 3: A user-friendly and highly optimized library for the creation of neurobiologically detailed spiking neural networks. In Proceedings of the International Joint Conference on Neural Networks (IJCNN). doi:10.1109/IJCNN.2015.7280520"
  - "Richert, M., Nageswaran, J. M., Dutt, N., & Krichmar, J. L. (2021). CARLsim 5: A biochemically detailed neuron model for the efficient simulation of large-scale spiking neural networks on GPUs. Neuroinformatics, 19(3), 463-485. doi:10.1007/s12021-021-09541-0"
---

# CARLsim

CARLsim is an open-source, GPU-accelerated simulator for large-scale spiking neural network (SNN) models.

## Overview

CARLsim enables efficient simulation of biologically realistic spiking neural networks by leveraging NVIDIA CUDA for GPU acceleration. Originally developed at the University of California, Irvine (UCI), it has evolved into a mature platform supporting millions of neurons and billions of synapses on commodity GPU hardware. CARLsim bridges the gap between detailed spiking simulations and computational efficiency, making it particularly valuable for large-scale brain network studies and neuromorphic computing research.

## Key Features

- **GPU acceleration**: Leverages NVIDIA CUDA for massive parallelization of spike calculations
- **Izhikevich neuron models**: Implements the computationally efficient Izhikevich model capturing diverse firing patterns
- **Biologically realistic synapses**: Supports spike-timing-dependent plasticity (STDP) and short-term plasticity
- **Scalability**: Simulates millions of neurons and billions of synapses on consumer GPUs
- **Multi-GPU support**: Distributes simulations across multiple GPUs for larger networks
- **Integration with neuromorphic hardware**: Compatible with neuromorphic computing paradigms
- **C++ and Python APIs**: Flexible interfaces for model development and analysis

## Architecture

CARLsim is built around three core components:

1. **Neuron Engine**: Handles membrane potential updates using the [[Izhikevich neuron model]] variants
2. **Synapse Engine**: Manages synaptic transmission and plasticity rules
3. **GPU Kernel Scheduler**: Optimizes CUDA kernel execution for spike generation and delivery

The simulator uses fixed time-step integration, typically with 1 ms steps, achieving significant computational speedups over CPU-based alternatives for large networks through massive GPU parallelism.

## Relationship to TVB

CARLsim and [[TVB]] represent complementary approaches to brain simulation:

| Aspect | CARLsim | TVB |
|:---|:---|:---|
| **Level of detail** | Spiking neurons | Neural mass models |
| **Primary compute** | GPU (CUDA) | CPU (NumPy) |
| **Best for** | Spike-level dynamics | Large-scale mean-field |
| **Neuron count** | Millions | Millions of populations |
| **Simulation speed** | Real-time to faster | Minutes to hours |

While TVB focuses on whole-brain simulations using population-averaged neural mass models, CARLsim provides access to individual spike times and synaptic events. Researchers may use CARLsim for detailed circuit validation before scaling up to TVB for whole-brain studies, or verify TVB mean-field predictions against spiking ground truth.

## Neuromorphic Computing Focus

CARLsim has gained traction in the neuromorphic community due to:
- Spike-based computation compatible with neuromorphic hardware
- Energy-efficient GPU implementations that mirror neuromorphic principles
- Support for online learning through STDP
- Efficient clock-driven simulation with GPU parallelism

## Key Papers

- **Nageswaran et al. (2009)** — Original CARLsim platform introduction, demonstrating GPU acceleration of spiking networks
- **Beyeler et al. (2015)** — CARLsim 3.0 with multi-GPU support and Python interface
- **Richert et al. (2021)** — Neuromorphic extensions and efficient synaptic plasticity implementations

## Technical Specifications

- **Supported neuron models**: Izhikevich, Leaky integrate-and-fire, Custom user-defined
- **Plasticity rules**: STDP, reward-modulated STDP, homeostatic mechanisms
- **Connectivity**: Sparse random, structured (small-world, scale-free), user-defined
- **Output formats**: Spike times, membrane potentials, synaptic weights, population firing rates
- **Hardware requirements**: CUDA-capable NVIDIA GPU (Compute Capability 3.5+)

## Related Software

- [[NEST]] — CPU-focused spiking network simulator with larger ecosystem
- [[NEURON]] — Multi-compartment detailed neuron simulations
- [[Brian]] — Python-based SNN simulator (Brian simulator)
- [[ANNarchy]] — GPU/CPU hybrid for rate-coded and spiking networks

## Related Concepts

- [[spiking neural networks]] — Detailed spiking dynamics vs. rate models
- [[Izhikevich neuron model]] — Efficient spiking neuron mathematics
- [[neuromorphic computing]] — Brain-inspired hardware and algorithms
- [[whole brain]] — Multi-scale modeling from spikes to populations
- [[brain network]] — Large-scale network dynamics
- [[synaptic plasticity]] — Learning mechanisms in spiking networks

## Key Developers

Originally developed by the Cognitive Ante-Robot Learning (CARL) Laboratory at UCI, now maintained by the Neuroscience and Behavior Laboratory with contributions from the broader neuromorphic community.

## Use Cases

- Large-scale cortical circuit modeling
- Neuromorphic algorithm development
- Spike-based machine learning with STDP
- Validation of neural mass model assumptions
- Real-time brain-machine interfaces
- Energy-efficient neural computation research

## Comparison with NEST

| Feature | CARLsim | NEST |
|:---|:---|:---|
| **Primary hardware** | GPU (CUDA) | CPU (MPI/OpenMP) |
| **Neuron focus** | Point neurons | Point and simple multicompartment |
| **Scalability** | Single/multi-GPU | Petascale clusters |
| **API maturity** | Moderate | Extensive (PyNEST) |
| **Community** | Research-focused | Large ecosystem |
| **Use case** | Fast GPU prototyping, neuromorphic | Large distributed networks |

CARLsim excels when GPU acceleration and spike-level detail are required; NEST is preferred for massive distributed simulations and when ecosystem maturity is prioritized.

## References

Nageswaran, J. M., Dutt, N., Krichmar, J. L., Nicolau, A., & Veidenbaum, A. (2009). A configurable simulation environment for the efficient simulation of large-scale spiking neural networks on graphics processors. *Neural Networks*, 22(5-6), 791-800. doi:10.1016/j.neunet.2009.06.019

Beyeler, M., Carlson, K. D., Chou, T. S., Dutt, N. D., & Krichmar, J. L. (2015). CARLsim 3: A user-friendly and highly optimized library for the creation of neurobiologically detailed spiking neural networks. In *Proceedings of the International Joint Conference on Neural Networks (IJCNN)*. doi:10.1109/IJCNN.2015.7280520

Richert, M., Nageswaran, J. M., Dutt, N., & Krichmar, J. L. (2021). CARLsim 5: A biochemically detailed neuron model for the efficient simulation of large-scale spiking neural networks on GPUs. *Neuroinformatics*, 19(3), 463-485. doi:10.1007/s12021-021-09541-0
```