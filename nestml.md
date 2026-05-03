---
title: NESTML
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software-nest, neuromorphic-computing, neural-network, spiking-neural-networks, software-brian, software-neuron, neural-mass-models, neuroconstruct, lems, software-modeling]
sources: []
---

NESTML (Neural Simulation Tool Markup Language) is a domain-specific modeling language designed to specificationaily describe neuron and synapse models for simulation in the NEST simulator. Developed primarily at the Institute of Neuroscience and Medicine (INM-6) at Forschungszentrum Jülich, NESTML provides a declarative approach to neuron modeling that separates the mathematical description of neuronal dynamics from the implementation details of particular simulation engines, enabling automatic code generation for multiple target platforms.

## Overview

NESTML extends the concepts pioneered by NeuroML and related efforts by providing a dedicated language for describing point neuron models with arbitrary complexity. At its core, NESTML allows researchers to define neuronal dynamics through differential equations describing the evolution of membrane potential, gating variables for ion channel states, and synaptic conductance updates. The language supports both integrate-and-fire type models as well as more detailed conductance-based models derived from the [[hodgkin-huxley-model]] formalism.

The language was developed in response to a perennial challenge in computational neuroscience: the difficulty of implementing complex neuron models in multiple simulation environments. When a researcher develops a novel neuron model described in a research paper, implementing it in NEST, NEURON, or Brian often requires substantial manual effort and introduces the possibility of implementation errors. NESTML addresses this by allowing researchers to write a single model specification that can be automatically translated into optimized simulation code for different targets.

## Key Features

**Declarative Model Specification**: NESTML employs a declarative syntax where researchers specify the differential equations governing neuronal dynamics, initial conditions for state variables, and parameter constraints. The language uses a block-based structure with separate sections for state variables, parameters, equations, input ports (for synaptic currents), and output definitions.

**Automatic Code Generation**: One of NESTML'sprimary strengths is its ability to generate optimized C++ code for the NEST simulator directly from the declarative model specification. This eliminates the need for researchers to write low-level simulation code and ensures consistency between the mathematical description and the implementation.

**Ion Channel Support**: NESTML includes built-in support for arbitrary numbers of gating variables following the Hodgkin-Huxley formalism. Users can define custom ion channel models with any number of gate types and voltage-dependent transition rates expressed as alpha-beta functions or generic expressions.

**Synaptic Modeling**: The language supports both spike-triggered and continuous synaptic conductances. Users can define synaptic models with arbitrary temporal dynamics including exponential rise and decay, alpha functions, or more complex kinetic schemes derived from double-exponential synapse formulations.

**Unit System**: NESTML incorporates a physical unit system that enables dimensional analysis during model specification. This catches parameter errors early in the modeling process—for example, preventing the user from accidentally specifying a membrane time constant in seconds when milliseconds are required.

**ODE Solving**: The language supports both exact solutions for simple differential equations (as used in [[adaptive-exponential-integrate-and-fire]] models) and numerical integration using forward Euler or RK2/RK4 methods for more complex dynamics.

## Relationship to NEST and the Ecosystem

NESTML is tightly integrated with the [[nest]] simulator, which provides the primary simulation backend. When a NESTML model is compiled, it produces a native NEST extension module that can be loaded at runtime. This allows users to create custom neuron types that integrate seamlessly with NEST's connection management and recording facilities.

Beyond NEST, NESTML shares conceptual territory with other neuronal modeling tools. Unlike the general-purpose [[brian]] language which uses interpreted Python, NESTML generates compiled simulation code optimized for large-scale network simulations. Compared to NeuroML, which provides a broader but less simulation-specific format, NESTML offers deeper integration with NEST at the cost of narrower target support.

The language builds upon concepts from LEMS (Low Entropy Model Specification), sharing a philosophical approach to declarative model definition, though NESTML is specifically optimized for point neuron models rather than the more general morphological neuron descriptions supported by NeuroML.

## Relationship to TVB

While NESTML is primarily used with the NEST simulator for detailed spiking network simulations, it connects to [[the-virtual-brain]] through complementary modeling scales. TVB often employs reduced [[neural-mass-models]] such as the [[jansen-rit-model]] or [[wong-wang-model]] to simulate large-scale brain dynamics at the population level. In contrast, NESTML-based models in NEST can simulate the microscopic activity of individual neurons that give rise to these mass-model dynamics. 

Integration between TVB and NEST is possible through projects like [[tvb-nest]], which couples the two simulators to enable multi-scale brain modeling where mass-model dynamics in TVB are constrained by or coupled to detailed spiking network simulations in NEST specified via NESTML.

## Key Papers

The NESTML language was formally introduced by Plotnikov et al. (2016) in "NESTML: a modeling language for spiking neurons" with subsequent extensions and improvements documented in later publications. The language has been applied to implement various neuron models including variations of the [[adaptive-exponential-integrate-and-fire]] model and conductance-based neurons with detailed ion channel dynamics.

## Related Software

- [[nest]] — Neural simulation tool, primary target for NESTML code generation
- [[brian]] — Alternative spiking neural network simulator with interpreted Python interface
- [[neuroml]] — Broader neural modeling format with multiple simulation targets
- [[neuroconstruct]] — GUI tool for managing neuronal models
- [[pynest]] — Python interface to NEST
- [[neuron]] — NEURON simulator for detailed neuronal simulations

## Technical Considerations

Users adopting NESTML should be aware that the language focuses specifically on point neuron models and does not currently support full morphological neuron reconstructions with compartmental modeling. For detailed morphological simulations, the [[neuron]] simulator with its built-in specification language remains more appropriate. Additionally, NESTML models require compilation—in contrast to interpreted frameworks like Brian—but this compilation step produces highly optimized simulation code suitable for large-scale networks containing millions of neurons.