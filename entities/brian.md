---
title: Brian
created: 2024-01-15
updated: 2026-05-06
type: entity
tags: [software-brian, spiking-neural-networks, computational-neuroscience, neural-simulation, python, software]
sources:
  - id: goodman-brette-2009
    citation: Goodman, C. F. M., & Brette, R. (2009). Brian: a simulator for spiking neural networks in Python. Frontiers in Neuroinformatics, 3, 16.
    url: https://doi.org/10.3389/neuro.11.016.2009
  - id: stimberg-2019
    citation: Stimberg, M., Brette, R., & Goodman, D. F. (2019). Brian 2: an intuitive and efficient neural simulator. eLife, 8, e47314.
    url: https://doi.org/10.7554/eLife.47314
---

Brian is a Python-based spiking neural network simulator designed for computational neuroscience research. Originally developed by Dan Goodman and Romain Brette, Brian provides an intuitive syntax for defining neuron models, synapses, and plasticity mechanisms without requiring deep programming expertise. The simulator emphasizes readability and flexibility, allowing researchers to rapidly prototype and experiment with single-neuron and network models (Goodman & Brette, 2009). Brian executes simulations through direct numerical integration in Python, making it suitable for simulations ranging from individual neurons to large-scale networks (Goodman & Brette, 2009).

The development of Brian emerged from a need in the computational neuroscience community for simulator software that bridges the gap between mathematical model descriptions and working code. Traditional simulators like [[neuron]] and GENESIS often require significant setup time and specialized knowledge, while Brian's Python-based approach allows models to be specified in a syntax that closely resembles the mathematical equations found in neuroscience literature. This correspondence between mathematical notation and implementation code is the core philosophical innovation of Brian—equations written for academic papers can often be directly transcribed into working simulations with minimal modification (Goodman & Brette, 2009).

Technically, Brian operates through a straightforward process: the user defines the model using differential equations, synaptic connections, and simulation parameters in Python, and then Brian's runtime system executes the numerical integration directly using SciPy and NumPy backends. The original Brian (1.x) executed simulations at the Python level without code generation. The simulator supports exact integration for linear systems, Runge-Kutta methods for general cases, and (in Brian2) adaptive timestep methods for stiff systems (Stimberg et al., 2019). Brian's neuron framework includes standard models such as [[hodgkin-huxley-model]], [[izhikevich-neuron-model]], and [[adaptive-exponential-integrate-and-fire]] neurons, while also allowing arbitrary custom equations. Synaptic interactions can be specified with arbitrary temporal dynamics, and the software includes built-in support for spike-timing dependent plasticity through its learning frameworks (Goodman & Brette, 2009).

The relationship between Brian and [[brian2]] is one of predecessor to successor—Brian2 represents a complete reimplementation that introduced C++ code generation, Cython optimization, and later GPU support for improved performance (Stimberg et most recent9). Most new projects should use Brian2, though the original Brian remains available for backward compatibility with legacy codebases. Brian occupies a similar niche to [[brian2genn]] (which generates code for GPUs) and [[nest]] (which focuses on large-scale network simulations), but distinguishes itself through its emphasis on model flexibility and educational accessibility. The simulator integrates with the broader Python scientific ecosystem, working alongside libraries like [[numpy]], [[scipy]], and [[matplotlib]] for data analysis and visualization.

In the context of whole-brain modeling and [[the-virtual-brain]], Brian represents a more fine-grained alternative to the neural mass approaches typically employed in connectome-based simulations. While TVB operates at the level of brain regions connected by empirical [[structural-connectivity]] matrices, Brian enables simulation at the level of individual neurons and small motifs. This makes Brian particularly useful for studying microcircuit dynamics that could inform meso-scale or macro-scale [[neural-mass-model]] implementations. Researchers using TVB to investigate the relationship between [[structural-connectivity]] and [[functional-connectivity]] might use Brian to simulate small network motifs and validate simplified population dynamics before embedding them in larger whole-brain frameworks.
