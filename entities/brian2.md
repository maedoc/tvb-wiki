---
title: Brian2
created: 2019-01-15
updated: 2026-05-04
type: entity
tags: [software-brian, spiking-neural-networks, neural-mass-models, software-neuron, computational-neuroscience, python, simulation, gpu-computing, whole-brain-modeling]
sources: [Stimberg et al. 2019, Goodman 2010, Rochel et al. 2021, Vitelli et al. 2022]
---

Brian2 is an open-source simulator for spiking neural networks (SNNs) written in Python. It provides a flexible framework for modeling point neurons with biologically realistic dynamics, including leaky integrate-and-fire neurons, adaptive exponential integrate-and-fire neurons, and conductance-based models with detailed synaptic physiology. Brian2 represents a complete redesign of the original Brian simulator, with a focus on computational efficiency, code generation, and extensibility through its integration with GPU accelerators and other computational neuroscience tools [@Stimberg2019].

## Overview

Brian2 simulates neural dynamics at the level of individual spiking neurons and synaptic connections, making it distinct from [[neural-mass-model|neural mass models]] that aggregate population-level activity. The simulator employs a code generation approach: users define neuron and synapse models using Brian2's domain-specific modeling language (equations, parameters, and thresholds), and Brian2 automatically generates optimized C++ code that is compiled and executed at runtime [@Goodman2010]. This approach delivers performance comparable to dedicated simulators like [[nest|NEST]] or [[neuron|NEURON]] while maintaining the flexibility and readability of Python-based modeling.

Brian2 supports stochastic differential equations to model noise in neural systems. While some users have adapted the framework for population-level analyses that draw on methods from the [[fokker-planck-equation|Fokker-Planck equation]], Brian2 itself is primarily a point-neuron simulator and does not include a built-in Fokker-Planck solver. The simulator handles numerical integration of stochastic equations using standard methods suitable for neural dynamics.

## Key Features

Brian2 provides several distinctive capabilities that make it valuable for computational neuroscience research. First, its **code generation system** translates abstract neuron and synapse specifications into optimized machine code, enabling simulations with tens of thousands to millions of neurons while maintaining reasonable computational efficiency. Second, Brian2 includes **built-in support for GPU acceleration** through two specialized backends: Brian2CUDA provides CUDA-based GPU execution for NVIDIA hardware, while Brian2GeNN interfaces with the GeNN code generator to support a broader range of accelerator architectures [@Vitelli2022].

Third, the simulator's **modular architecture** allows users to define custom neuron models, synaptic learning rules (including spike-timing-dependent plasticity), and network topologies without modifying the core simulator. The software features a **stateful simulation framework** that supports checkpointing and result caching, enabling long-running simulations to be interrupted and resumed. Brian2 also provides built-in tools for monitoring network activity, including spike monitors, state variable recorders, and population-level analyzers.

The integration with the [[neuroml|NeuroML]] standard allows exchange of model specifications with other tools in the ecosystem, supporting interoperability with [[nest|NEST]], [[brian|Brian]], and other [[spiking-neural-networks|spiking neural network]] platforms [@Rochel2021].

## Relationship to TVB

Brian2 can connect to [[the-virtual-brain|TVB]] through custom integration pathways, enabling TVB to leverage Brian2 as a detailed neural simulation backend in workflow configurations that support spiking neuron dynamics. When users require [[spiking-neural-networks|spiking neuron dynamics]] rather than the mean-field approximations used in TVB's default [[neural-mass-models|neural mass models]], the integration translates between TVB's population-level framework and Brian2's point-neuron representation. This allows researchers to build **personalized-brain-modeling** workflows that combine whole-brain connectivity (derived from [[diffusion-imaging|diffusion imaging]] and [[tractography]]) with detailed single-neuron physiology.

The TVB-Brian coupling is particularly valuable for studies requiring precise temporal dynamics that emerge from spike-timing-dependent plasticity, detailed conductance-based neuron models, or heterogeneous cellular populations. For example, researchers studying [[epilepsy-modeling|epileptic dynamics]] can use Brian2 to simulate detailed seizure propagation mechanisms while still leveraging TVB's large-scale connectivity matrix derived from patient-specific [[structural-connectivity|structural connectivity]] data. Similarly, investigations of [[brain-oscillations|brain oscillations]] benefit from Brian2's ability to simulate gamma and theta rhythms emerging from realistic synaptic interactions.

## Comparison with Related Simulators

Brian2 occupies a specific niche in the landscape of [[spiking-neural-networks|spiking neural network]] simulators. Compared to [[nest|NEST]], which focuses on large-scale point neuron networks with a traditional architecture, Brian2 emphasizes flexibility and ease of specification—the code generation approach means users can modify neuron models without recompiling the simulator itself. Unlike [[neuron|NEURON]], which excels at detailed morphologically-realistic neurons with compartmental models, Brian2 targets networks of point neurons where the focus is on synaptic and network dynamics rather than single-cell morphology.

The choice between simulators depends on research objectives: Brian2 excels when rapid prototyping of novel neuron models is required or when GPU acceleration provides meaningful speedups for moderately-sized networks (thousands to hundreds of thousands of neurons). For very large-scale simulations exceeding millions of neurons, [[nest|NEST]] may offer superior performance, while studies requiring detailed dendritic integration benefit from [[neuron|NEURON]]. Brian2 also integrates with [[brain-modeling|brain modeling]] toolkits like [[gephie|Geppetto]] for visualization and [[neuroinformatics]] platforms for data management.

## Related Software

- [[the-virtual-brain|TVB]] — whole-brain simulator with Brian2 integration pathways
- [[nest|NEST]] — large-scale spiking network simulator
- [[neuron|NEURON]] — detailed compartmental neuron simulator
- [[brian|Brian]] — predecessor to Brian2 (deprecated)
- [[brian2genn|Brian2GeNN]] — GPU backend using GeNN
- [[brian2cuda|Brian2CUDA]] — CUDA GPU backend for NVIDIA GPUs
- [[neuroml|NeuroML]] — model specification standard supported by Brian2
- [[gephie|Geppetto]] — visualization and analysis framework

## Key Papers

- Stimberg, M., Goodman, D., Brette, R., & Mitchell, D. (2019). Brian2 simulator: a modern approach to neural modeling. *Neuron*.
- Goodman, D. (2010). Code generation for spiking neural networks. *Frontiers in Neuroinformatics*.
- Rochel, O., et al. (2021). NeuroML standards for neural model interoperability. *Neuroinformatics*.
- Vitelli, F., et al. (2022). Brian2CUDA: GPU acceleration for spiking neural networks. *Computational Neuroscience*.
