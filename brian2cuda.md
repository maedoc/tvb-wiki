---
title: Brian2CUDA
created: 2025-01-15
updated: 2026-05-03
type: entity
tags: [software-brian, spiking-neural-networks, computational-neuroscience, gpu-computing]
sources:
  - Alevi et al. (2022). "Brian2CUDA: Flexible and Efficient Simulation of Spiking Neural Network Models on GPUs." Frontiers in Neuroinformatics. doi:10.3389/fninf.2022.883700
  - Stimberg et al. (2014). "Equation-oriented specification of neural models for simulations." Front. Neuroinform. 8:6.
  - Stimberg et al. (2019). "Brian 2, an intuitive and efficient neural simulator." Elife 8:e47314.
  - Yavuz et al. (2016). "GeNN: a code generation framework for accelerated brain simulations." Sci. Rep. 6:18854.
  - Knight & Nowotny (2021). "PyGeNN: a python library for GPU-enhanced neural networks." Front. Neuroinform. 15:659005.
---

# Brian2CUDA

## Overview

Brian2CUDA is a GPU acceleration backend for the [[brian2]] spiking neural network simulator, enabling large-scale neural simulations to run on NVIDIA graphics processing units using CUDA (Compute Unified Device Architecture). Developed primarily by Denis Alevi, Marcel Stimberg, and colleagues at Technical University of Berlin and Sorbonne Université (Alevi et al., 2022), Brian2CUDA extends the Brian2 framework's capabilities beyond CPU-based simulations by leveraging the massive parallelism of modern graphics cards. The package translates Brian2's abstract neural equations into optimized CUDA kernels, allowing researchers to simulate networks with hundreds of thousands to millions of neurons and billions of synapses that would be computationally intractable on traditional CPU architectures. First released in 2020 with its initial public version and formally published in 2022 (Alevi et al., 2022), Brian2CUDA has found adoption among computational neuroscientists working on biologically detailed spiking network simulations at brain-scale.

## Key Features

**Automatic GPU Code Generation**: Brian2CUDA integrates seamlessly with the Brian2 code generation system. Users write neural equations using Brian2's standard syntax—identical to CPU-based simulations—and the backend automatically handles GPU kernel compilation, memory management, and data transfer between host and device. This means existing Brian2 codebases can often be accelerated with only a single line change: switching from the default "numpy" runtime to the "cuda_standalone" runtime (Stimberg et al., 2014).

**Support for Complex Neuron Models**: The CUDA backend supports the full range of Brian2's neuron models, including leaky integrate-and-fire neurons, exponential integrate-and-fire models, and custom models defined through differential equations. It handles conductance-based synapses with arbitrary delay distributions, allowing for biologically realistic synaptic dynamics including excitatory and inhibitory connections with different time constants (Alevi et al., 2022).

**Plasticity and Learning**: Spike-timing-dependent plasticity (STDP) and other learning rules are fully supported through optimized CUDA kernels. The implementation includes both triplet-based and pairwise STDP models, enabling studies of synaptic plasticity, learning, and memory formation in large-scale networks (Alevi et al., 2022).

**Mixed Precision and Performance Tuning**: Brian2CUDA offers configurable precision modes, allowing users to trade off numerical precision for speed when appropriate. The backend includes tools for profiling performance and identifying bottlenecks, helping users optimize their simulations for specific GPU architectures. Benchmarks demonstrate speedups of up to three orders of magnitude compared to Brian's CPU backend for large network simulations (Alevi et al., 2022).

## Relationship to TVB

While [[the-virtual-brain]] (TVB) primarily uses neural mass models operating at the population level, Brian2CUDA represents a complementary approach that operates at the level of individual neurons and synapses. The relationship between TVB and Brian2CUDA reflects a broader division in whole-brain modeling between continuum approximations (neural mass / neural field models) and spiking network models. TVB-NEST is an adapter for the NEST simulator and does not interface with Brian2; there is currently no established TVB-Brian2 adapter. Researchers interested in bridging these scales might use TVB for whole-brain dynamics exploration while using Brian2CUDA for detailed local circuit simulations that inform mesoscopic population models.

## Comparison to Related GPU Accelerators

Brian2CUDA is distinct from [[brian2genn]] (GeNN), another GPU-accelerated spiking neural network simulator. While Brian2CUDA serves as a backend for Brian2, GeNN provides its own independent simulation environment with a different API and code generation approach. Brian2CUDA emphasizes ease of use and tight integration with the Brian2 ecosystem, making it particularly attractive for researchers already familiar with Brian2 syntax. GeNN, developed by Thomas Nowotny and colleagues (Yavuz et al., 2016; Knight & Nowotny, 2021), offers more fine-grained control over GPU kernels and may provide superior performance for specific network architectures.

Compared to other major simulators with GPU support—[[nest]] with its GPUModule, [[neuron]] with its GPU capabilities, and [[bmtk]]—Brian2CUDA distinguishes itself through Python-first design and the ease of model specification. The relationship to [[spiking-neural-networks]] as a whole is thus one of providing an accessible entry point for GPU-accelerated spiking simulations.

## Key Papers

The primary reference for Brian2CUDA is Alevi et al. (2022), "Brian2CUDA: Flexible and Efficient Simulation of Spiking Neural Network Models on GPUs," published in *Frontiers in Neuroinformatics*, which introduces the architecture and demonstrates scaling to large network simulations with up to three orders of magnitude speedup. This work builds on the earlier Brian2 framework paper (Stimberg et al., 2014) and the Brian2 simulator paper (Stimberg et al., 2019) in *Frontiers in Neuroinformatics* and *Elife* respectively.

## Related Software

- [[brian2]]
- [[brian]]
- [[brian2genn]]
- [[spiking-neural-networks]]
- [[computational-neuroscience]]
- [[the-virtual-brain]]
- [[tvb-nest]]
- [[whole-brain-simulators]]