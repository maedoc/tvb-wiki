---
created: 2026-04-23
sources:
- raw/papers/jansen-rit-1995.md
- raw/papers/ritter-2013.md
- raw/papers/sanz-leon-2013.md
tags:
- software-brain-modeling
- neural-mass-models
- whole-brain-modeling
- dynamical-systems
title: XCOS
type: entity
updated: '2026-04-28'
---

# XCOS

**XCOS** (also written as Xcos) is a graphical dynamical system modeler and simulator distributed with the [[scilab|Scilab]] open-source computing environment. Originally developed as a successor to SCICOS, XCOS provides a visual editor for designing and simulating hybrid dynamical systems in discrete and continuous time domains. The platform enables researchers to build block diagrams representing mathematical models, making it valuable for computational neuroscience applications involving neural mass modeling.

## Overview

XCOS serves as a flexible framework for building block diagram models of dynamical systems, with applications spanning control engineering, signal processing, and neuroscience^[scilab-xcos]. The graphical interface allows users to construct models by connecting functional blocks from standard palettes, with the ability to create custom blocks using Scilab's scripting capabilities. This makes XCOS particularly useful for implementing neural mass models such as the [[jansen-rit-model|Jansen-Rit model]], which describes the collective activity of cortical neuronal populations^[jansen-rit-1995].

In the context of [[whole-brain]] modeling, XCOS provides a platform for implementing and simulating [[neural-mass-models]] that describe the average activity of large neuronal populations. These models abstract detailed dynamics of individual neurons into simplified mathematical descriptions, capturing essential features of brain activity visible in [[eeg|electroencephalography (EEG)]] and [[fmri|functional magnetic resonance imaging (fMRI)]] recordings^[sanz-leon-2013].

## Key Features

### Graphical Modeling Environment
- **Block diagram editor**: Visual drag-and-drop interface for constructing dynamical system models
- **Standard palettes**: Pre-built blocks for signal processing, control systems, and mathematical operations
- **Custom block creation**: Users can define custom blocks using Scilab functions
- **Hierarchical modeling**: Support for creating composite blocks and subsystems

### Simulation Capabilities
- **Continuous and discrete time**: Support for hybrid dynamical systems
- **ODE solvers**: Multiple numerical integration methods for solving ordinary differential equations
- **Batch simulation**: Command-line interface for running simulations without the GUI

### Neural Mass Model Implementation
- **Population dynamics**: Blocks representing excitatory and inhibitory neural populations
- **Synaptic blocks**: Alpha-functions for postsynaptic responses
- **Connectivity modeling**: Ability to couple multiple cortical column models
- **Forward modeling**: Generation of simulated EEG signals from neural mass activity

## Relationship to TVB

Within the [[the-virtual-brain|TVB]] ecosystem, XCOS represents an approach to implementing neural mass models for whole-brain simulations. While TVB provides a comprehensive neuroinformatics platform with built-in neural mass model implementations^[ritter-2013], XCOS offers an alternative for researchers preferring explicit block diagram modeling.

Key differences from TVB's built-in models:
- **Explicit structure**: Block diagram representation makes model equations visible
- **Complete customization**: Direct control over block parameters and connections
- **Educational value**: Useful for teaching neural mass modeling concepts

## Related Software

- [[scilab|Scilab]]: Parent environment for numerical computing
- [[TVB]]: Whole-brain modeling platform with built-in neural mass models
- [[brian]]: Spiking neural network simulator with neural mass implementations
- [[NEST]]: Large-scale spiking neural network simulator
- [[annarchy]]: Hybrid rate-coded and spiking network simulator

## References

1. Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. *Biological Cybernetics*, 73(4), 357-366. https://doi.org/10.1007/BF00199471

2. Ritter, P., Schirner, M., McIntosh, A. R., & Jirsa, V. K. (2013). The Virtual Brain integrates computational modeling and multimodal neuroimaging. *Brain Connectivity*, 3(2), 121-145. https://doi.org/10.1089/brain.2012.0120

3. Sanz Leon, P., Jones, S. R., Detorakis, G., Yegen, G., McIntosh, A. R., & Jirsa, V. K. (2013). The Virtual Brain: a simulator of primate brain network dynamics. *Frontiers in Neuroinformatics*, 7, 10. https://doi.org/10.3389/fninf.2013.00010

4. Scilab Xcos documentation: https://www.scilab.org/software/xcos

---

*XCOS provides a valuable platform for computational neuroscience research, enabling researchers to implement neural mass models through an intuitive block diagram interface.*