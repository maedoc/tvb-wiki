---
created: 2024-01-15
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/semanticscholar-bceb6bea8311.md
tags:
- software-brian
- software-neuron
- spiking-neural-networks
- gpu-computing
- computational-neuroscience
- neural-mass-models
- neural-network
- software-modeling
- code-generation
title: Brian2GeNN
type: entity
updated: '2026-05-06'
---

Brian2GeNN is a software bridge that connects the Brian2 spiking [[neural-network]] simulator with the GeNN (GPU-enhanced Neuronal Networks) code generation framework, enabling high-performance GPU-accelerated simulations of spiking neural networks. The tool was developed to address the computational bottleneck inherent in large-scale [[spiking-neural-networks]] simulations, which often require millions of neurons and synapses to achieve biologically realistic [[network-dynamics]]. By automatically converting Brian2 model definitions into optimized CUDA code via GeNN, Brian2GeNN allows neuroscientists to write network models in Brian2's intuitive Python-based syntax while transparently benefiting from the massive parallelism of graphics processing units.

## History and Development

Brian2GeNN was developed by Marcel Stimberg, Dan F. M. Goodman, and Thomas Nowotny, with the initial public release in 2019. The project emerged from the intersection of two established software efforts in computational neuroscience: [[brian2]], a Python-based spiking neural network simulator developed by Romain Brette and Goodman at the École Normale Supérieure in Paris, and GeNN, a GPU code generation framework originally created by Nowotny and colleagues at the University of Sussex. The motivation for Brian2GeNN was to enable neuroscientists to access the performance benefits of GPU acceleration without abandoning Brian2's accessible Python modeling paradigm.

The first major version (Brian2GeNN 1.0) was released alongside the publication of the primary reference paper in Frontiers in Neuroinformatics, demonstrating the tool's capability to accelerate Brian2 simulations by orders of magnitude [[brian2genn]]. Subsequent releases have expanded model compatibility and improved integration with newer versions of both Brian2 and GeNN.

## Motivation and Context

The field of [[computational-neuroscience]] has increasingly relied on detailed [[spiking-neural-networks]] (SNNs) to understand brain dynamics at multiple scales. However, simulating large neural circuits with biologically plausible connectivity and dynamics poses a significant computational challenge. Traditional CPU-based simulators such as Brian, [[neuron|NEURON]], and [[nest]] can handle networks of tens of thousands of neurons, but scaling to brain-scale simulations—requiring millions of neurons and billions of synapses—remains prohibitively slow on conventional hardware.

GPU computing emerged as a promising solution because modern graphics processors can execute thousands of threads in parallel, making them well-suited for the inherently parallel nature of neural network simulations. However, writing GPU code directly requires expertise in CUDA or OpenCL and significantly increased development time. Brian2GeNN addresses this gap by providing an automatic code generation pipeline: users write models in Brian2's domain-specific language, and Brian2GeNN generates optimized CUDA code that runs on GPUs without requiring the user to write any GPU-specific code.

## Technical Overview

Brian2GeNN operates as a backend for Brian2's extensible code generation system. When a user defines a neural network model using Brian2's Python API—which includes neuron equations, synaptic dynamics, and stimulation protocols—the tool intercepts the code generation process and produces C++/CUDA code compatible with the GeNN framework rather than standard C++.

The generated code exploits several GPU optimization strategies. First, neuron updates are performed in parallel across thousands of GPU threads, each thread handling one neuron or one small group of neurons. Second, synaptic operations use optimized sparse matrix techniques since biological neural networks exhibit strong structural [[connectivity]] patterns with many zero connections. Third, spike communication uses efficient GPU kernels that minimize data transfer between GPU memory and host memory.

A key technical challenge addressed by Brian2GeNN is maintaining feature compatibility between the CPU and GPU backends. The tool maps Brian2's abstract neuron and synapse objects onto GeNN's GPU-optimized data structures while preserving the mathematical semantics of the original model equations. This includes handling [[stochastic-differential-equations]] for noise-driven dynamics, complex synaptic weight plasticity rules, and various neuron models including [[izhikevich|Izhikevich]] neurons and [[hodgkin-huxley-model|Hodgkin-Huxley]] formulations.

## Key Features

Brian2GeNN provides several notable capabilities that make it valuable for computational neuroscience research. The primary feature is transparent GPU acceleration: users need only add a single line of code to switch from CPU to GPU execution, with no changes required to the model definition itself. This design philosophy lowers the barrier to entry for GPU-accelerated simulations and encourages adoption by researchers without specialized GPU programming knowledge.

The tool supports most standard Brian2 neuron and synapse models, including leaky integrate-and-fire neurons, [[adaptive-exponential-integrate-and-fire]] neurons, and conductance-based models. It also handles synaptic models with exponential or alpha-shaped postsynaptic potentials, spike-timing-dependent [[plasticity]], and various forms of short-term plasticity.

Performance benchmarking has demonstrated significant speedups compared to CPU-based Brian2 execution. For typical network simulations with tens of thousands of neurons and hundreds of thousands of synapses, Brian2GeNN can achieve speedups of 10-100x depending on network size and model complexity. The relative performance gain increases with network size, making the tool particularly useful for brain-scale simulations relevant to [[whole-brain-modeling]] research.

## Relationship to TVB and Related Software

While [[the-virtual-brain|TVB]] focuses on [[whole-brain-modeling]] using [[neural-mass-models]] at the macroscale, Brian2GeNN operates at the microscale of individual spiking neurons. These approaches are complementary: TVB simulates large-scale brain dynamics using simplified population models, while Brian2GeNN enables detailed investigations of cellular-level mechanisms that can inform the development of more accurate mass models.

Brian2GeNN fits within a broader ecosystem of [[spiking-neural-networks]] simulators that also includes [[nest]] (which has its own GPU extension via the NEST GPU project) [[nest]], [[brian2cuda]] (another GPU backend for Brian2 using CUDA directly), and Auryn (a simulator optimized for asynchronous spiking networks). The distinction is that Brian2GeNN uses GeNN as an intermediate layer, which provides additional flexibility for custom GPU kernel definitions.

## Relationship to GeNN

GeNN (GPU-enhanced Neuronal Networks) is a C++/CUDA library that generates optimized GPU code for neural network simulations. Originally developed for spiking neural networks with support for detailed neuron models nowotny-2014-genn, GeNN has evolved to support a wide range of model types. Brian2GeNN serves as the bridge between Brian2's Python interface and GeNN's code generation backend, translating the declarative Brian2 model specification into the imperative C++/CUDA code that GeNN compiles and execute.

The relationship is asymmetric: while GeNN can be used independently with manually written C++ models, Brian2GeNN provides the reverse mapping—enabling Brian2 users to leverage GeNN without learning C++. This follows a similar pattern to [[tvb-nest|TVB-NEST]], which connects [[tvb|The Virtual Brain]] with NEST for [[co-simulation]] of mass models and spiking networks.

## Limitations

Brian2GeNN, while powerful, has important limitations that users should consider. Not all Brian2 features are supported on the GeNN backend; some advanced features such as arbitrary Python code in neuron equations, certain state update mechanisms, and complex network topologies that require dynamic connectivity may not translate correctly to GPU execution. Users should consult the compatibility documentation before migrating complex models.

GPU memory constraints represent a practical limitation for very large simulations. While GPUs offer massive parallelism, the amount of available GPU memory (typically 4-16 GB on consumer hardware) can limit network size, particularly when storing detailed state variables for each neuron and synapse. Simulations exceeding GPU memory capacity will fail or require manual partitioning.

Additionally, Brian2GeNN currently supports single-GPU execution only. Multi-GPU parallelization across multiple devices is not supported, which can limit scalability for simulations requiring more neurons than a single GPU can accommodate. Users with very large-scale simulation needs may need to consider alternative approaches such as distributed CPU clusters or the Spinnaker neuromorphic hardware platform.

## Related Software

Brian2GeNN is part of a rich ecosystem of neural simulation tools, each with different strengths. Brian2 is the Python-based spiking neural network simulator that serves as the frontend for Brian2GeNN, providing the modeling interface that users interact with directly stimberg-2019-brian2. The [[brian2cuda]] project offers an alternative GPU backend for Brian2 that uses CUDA directly rather than through GeNN, potentially offering different performance characteristics. Genn itself is the underlying code generation framework that transforms model specifications into optimized CUDA executables nowotny-2014-genn. [[nest]] is a widely-used simulator for spiking networks that has its own GPU acceleration effort through the NEST GPU project [[nest]]. The [[neuron]] simulator provides another established option for neuron and network simulations. Spinnaker represents a fundamentally different approach using custom neuromorphic hardware rather than GPU acceleration. Finally, [[tvb-nest]] provides integration between TVB and NEST, analogous to how Brian2GeNN connects Brian2 with GeNN.

## References

1. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and [[whole-brain]] Propagation*. [Link](](https://arxiv.org/abs/2505.16861))
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](](https://doi.org/10.3389/fncom.2025.1731161))
3. Max C. W. Engelen, River Betting, Christos Strydis. (2025). *SimHH: A Versatile, Multi-GPU Simulator for Extended Hodgkin-Huxley Networks*. IEEE Access. [DOI](](https://doi.org/10.1109/ACCESS.2025.3550444))