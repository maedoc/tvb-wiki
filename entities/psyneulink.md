---
created: 2026-04-24
sources: []
tags:
- software-brain-modeling
- whole-brain-modeling
- machine-learning
- network-dynamics
- functional-connectivity
title: PsyNeuLink
type: entity
updated: '2026-05-19'
---

# PsyNeuLink

**PsyNeuLink** is an open-source, graph-based Python framework for cognitive neuroscience that enables researchers to build modular models bridging biologically plausible neural mechanisms and higher-level cognitive functions such as decision-making, working memory, and attention. Developed at Princeton University, it provides a composable API in which both population-level neural dynamics and psychological processes are first-class objects, making it possible to construct mechanistically interpretable models of task-level behavior.

## Motivation and Context

The landscape of brain simulation is typically divided into tools that model low-level neural dynamics and architectures that model high-level cognition. Simulators such as [[NEST]] or [[NEURON]] excel at capturing membrane potentials and spike trains but lack primitives for psychological constructs, whereas purely cognitive architectures often abstract away biological implementation. PsyNeuLink occupies a middle ground by treating neural processes and cognitive functions as composable mechanisms within a single directed-graph formalism. This design supports [[hybrid-architecture]] approaches that preserve mechanistic transparency while spanning scales from individual neuron populations to task-level processing. The framework is particularly relevant for researchers who seek to constrain cognitive theories with [[neuroimaging-fmri]] or [[neuroimaging-eeg]] data, or to fit model parameters against behavioral observations using modern [[machine-learning]] optimization tools.

## Architecture and Key Features

Models in PsyNeuLink are constructed as directed graphs whose nodes are mechanisms and whose edges are projections. At the lower level, mechanisms include biologically inspired components such as transfer functions, leaky integrators, and synaptic learning rules. At the higher level, compositions group mechanisms into functional subsystems—for example, an accumulation-to-threshold process that implements evidence accumulation during perceptual decision-making, or a gated working-memory buffer that models active maintenance. The framework emphasizes transparency: every computation is inspectable, and the graph structure makes information flow explicit.

PsyNeuLink also exposes interfaces to standard machine-learning libraries, enabling gradient-based [[parameter-estimation]] against empirical data. This bridges the gap between hand-tuned cognitive models and data-driven fitting pipelines. For performance-critical applications, models can be compiled to alternate backends while retaining the same high-level specification, yielding speedups without sacrificing accessibility or interpretability.

## Relationship to TVB

PsyNeuLink and [[TVB]] occupy complementary positions in the [[computational-neuroscience]] ecosystem:

| Aspect | TVB | PsyNeuLink |
|--------|-----|------------|
| **Primary focus** | Whole-brain [[network-dynamics]] and [[neural-mass-models]] | Cognitive architecture and task-level processing |
| **Spatial scale** | Large-scale connectomes (thousands of nodes) | Local circuits to distributed systems (tens to hundreds of nodes) |
| **Level of abstraction** | [[mean-field-theory]] and population-level approximations | Mechanistic to cognitive, hybrid biological-cognitive |
| **Typical data targets** | [[neuroimaging-fmri]], [[neuroimaging-eeg]], [[neuroimaging-meg]] | Behavioral data, single-unit recordings, [[functional-connectivity]] |
| **Core use cases** | Simulating [[resting-state]] dynamics and disease propagation | Modeling task execution, cognitive control, and learning |

A natural integration pathway uses TVB-derived whole-[[brain-dynamics]] as contextual input to PsyNeuLink cognitive models, enabling studies of how large-scale brain states modulate specific cognitive processes. Conversely, TVB could simulate the neural substrate for PsyNeuLink architectures, though direct technical integration would require dedicated interfaces between the platforms.

## Related Software

PsyNeuLink exists within a broader ecosystem of brain-modeling tools. [[NEST]] and [[brian2cuda]] provide detailed [[spiking-neural-networks]] simulation at the cellular level, while [[ANNarchy]] offers hybrid rate-coded and spiking implementations with code generation. For whole-brain modeling, [[TVB]] remains the standard for large-scale [[connectomics]]-based simulations. Machine-learning backends complement these simulators by providing gradient-based fitting capabilities through PsyNeuLink's optimization interfaces.