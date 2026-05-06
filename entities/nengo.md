---
created: 2024-01-15
sources:
- Eliasmith C, Stewart TC (2012) A large-scale model of the functioning brain. Science
  338(6111):1202-1205.
- 'Bekolay T, Bergstra J, Hunsberger E, et al. (2014) Nengo: a Python tool for building
  neural models. Front Neuroinform 8:39.'
- 'Eliasmith C, Anderson CH (2003) Neural Engineering: Computation, Representation,
  and Dynamics in Neurobiological Systems. MIT Press.'
- Stewart TC, Bekolay T, Eliasmith C (2012) Learning to select actions with spiking
  neurons in a recurrent network. J Neural Eng 9(2):026005.
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/sanz-leon-2013.md
tags:
- software
- neural-network
- spiking-neural-networks
- computational-neuroscience
- neural-mass-models
title: Nengo
type: entity
updated: '2026-05-06'
---

Nengo is a Python library for building, simulating, and deploying neural models at various scales, from individual [[neuron]] circuits to brain-scale networks implementing cognitive architectures. It implements the Neural Engineering Framework (NEF), a principled approach to constructing large-scale neural systems that enables precise control over representation, transformation, and temporal dynamics in biological neural tissue (Eliasmith & Anderson, 2003). The library emphasizes biologically realistic spiking neuron models while providing abstractions that make it accessible for both [[computational-neuroscience]] research and engineering applications.

The development of Nengo addressed a fundamental challenge in computational neuroscience: the difficulty of building neural models that scale from cellular-level detail to [[whole-brain]] simulations while maintaining both biological plausibility and computational tractability. Traditional approaches often required choosing between detail and scale, resulting in either detailed single-region models or abstracted whole-brain simulations lacking cellular resolution. Nengo introduced the concept of semantic pointers—a neural representation mechanism inspired by pointer-based data structures in computer science that combines pointer-like discrete addressing with continuous vector operations—enabling manipulation of high-dimensional information in ways that more closely mirror neural coding in biological brains (Bekolay et al., 2014).

The mathematical foundation of Nengo rests on three core principles. First, representation involves encoding continuous-valued vectors into neural activity patterns through populations of neurons whose tuning properties (preferred directions, gains, and biases) collectively determine what information the ensemble represents. Second, transformation specifies how neural connections compute functions of represented vectors, typically through learning rules that optimize connection weights to approximate desired transformations via [[linear]] regression on neural firing rates. Third, dynamics extends the framework to time-varying signals, where neural ensembles implement differential equations that govern the temporal evolution of represented variables, enabling modeling of neural oscillators, memory systems, and adaptive filters (Eliasmith & Anderson, 2003).

Nengo supports diverse neuron models including leaky [[spiking-neural-networks|integrate-and-fire]] neurons, [[adaptive-exponential-integrate-and-fire]] neurons, and [[izhikevich]] neuron models, allowing researchers to match the biophysical properties of their target neural systems. The software provides multiple backend simulators: Nengo DL integrates with [[tensorflow]] for deep learning acceleration and GPU computation via CUDA, while Nengo OCL offers OpenCL support for GPU acceleration (Bekolay et al., 2014). The architecture supports both fixed-timestep and variable-timestep integration methods, with adaptive solvers that automatically adjust simulation precision based on neural activity dynamics.

Key models built with Nengo include SPAUN (Semantic Pointer Architecture Unified Network), which demonstrated flexible cognitive behavior—including reasoning, learning, and decision-making—using approximately 2.5 million simulated neurons organized into functional modules corresponding to different brain regions (Eliasmith & Stewart, 2012). This landmark project illustrated the potential for building brain-scale neural systems capable of complex, variable behaviors rather than isolated computational tasks.

Compared to other neural simulators like [[brian|Brian]] or [[nest|NEST]], Nengo occupies a unique position by explicitly implementing the NEF abstraction layer, which provides high-level tools for constructing neural systems that perform arbitrary nonlinear transformations on represented vectors. While Brian offers extremely flexible neuron and synapse definitions for detailed biophysical modeling, and NEST provides optimized spike-based simulation for large networks, Nengo prioritizes the Neural Engineering Framework's emphasis on functional computation in neural tissue. The software can interoperate with [[nest]] through the nengo-nest project, enabling hybrid simulations that combine NEF-style constructions with NEST's optimized spiking network capabilities.

Nengo relates to [[the-virtual-brain|TVB]] through their complementary but distinct approaches to neural modeling. While [[the-virtual-brain]] (TVB) specializes in whole-brain modeling using neural mass models—averaging the activity of large neuronal populations to simulate regional dynamics on the connectome—Nengo typically operates at the level of spiking neural networks with explicit cellular resolution. Researchers investigating the relationship between microscale neural circuitry and macroscale brain dynamics might employ Nengo to construct detailed spiking models of specific brain regions while using TVB for connectome-based whole-brain simulations. Both frameworks can be parameterized using structural connectivity data derived from diffusion imaging, though they represent different points on the resolution-scalability spectrum and serve different research objectives within the broader scope of [[whole-brain-modeling]]. Notably, some researchers have explored coupling Nengo's spiking network models with TVB's mass model framework to bridge these different levels of analysis, enabling investigations that combine fine-grained neural circuitry with whole-brain dynamics.