---
title: SimBrain
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software-brain-modeling, computational-neuroscience, neural-network, spiking-neural-networks, network-dynamics]
sources:
  - Yoshimi et al. (2012). Simbrain. Neural Networks
  - https://simbrain.net
  - https://github.com/simbrain/simbrain
---

# SimBrain

## Overview

SimBrain is a free, open-source neural network simulator designed for building, running, and analyzing computer simulations of brain circuitry[^1]. Developed primarily by Jeff Yoshimi and collaborators at the University of Texas at Austin, SimBrain aims to be as visual and easy-to-use as possible while maintaining sufficient flexibility for computational neuroscience research[^2]. The software provides an interactive graphical environment where researchers can construct neural networks by placing neurons and synapses, connect them in arbitrary configurations, and observe their dynamics in real time through various visualization tools.

The simulator supports a wide range of neural network architectures, from simple feedforward networks to complex recurrent structures including Hopfield networks, Boltzmann machines, and adaptive resonance theory (ART) networks. SimBrain distinguishes itself through its integrated "world components" — simulated environments that neural networks can inhabit and interact with — and its ability to represent a network's state space through projection plots and other visualization methods[^1]. This combination of visual interactivity and environmental embedding makes SimBrain particularly well-suited for educational purposes and for exploring embodied cognition scenarios.

## Key Features

SimBrain provides several features that make it valuable for computational neuroscience research and education. The software is written primarily in Kotlin (with legacy Java components) and runs cross-platform on Windows, macOS, and Linux[^3]. Its graphical user interface allows researchers to construct networks through point-and-click interactions, with keyboard shortcuts enabling rapid prototyping of network architectures.

The neuron models available in SimBrain encompass both rate-based and spiking formulations. Users can choose from standard activation functions, Leaky Integrate-and-Fire (LIF) neurons for spiking dynamics, and custom neuron types. The synaptic plasticity mechanisms include Hebbian learning, its variants, and other learning rules that can be applied to individual synapses or entire weight matrices[^1]. This flexibility enables investigation of network-level learning phenomena such as pattern recognition, memory formation, and competitive learning.

The visualization capabilities in SimBrain are particularly extensive. Time series plots display neuron activation evolution over time, bar charts show instantaneous network state, and projection plots map high-dimensional network state into two or three dimensions for intuitive visualization. The coupling system allows different components — networks, plots, and world environments — to be linked together, creating integrated simulation workspaces where network activity drives visualizations in real time[^4].

SimBrain also includes subnetworks, which are customized collections of network objects that can be trained as a unit. Pre-built subnetworks include backpropagation networks, restricted Boltzmann machines (RBMs), and various competitive learning architectures. These can be combined with free-form network components to create hybrid architectures that leverage both traditional connectionist approaches and more biologically inspired dynamics.

## Relationship to TVB and Whole-Brain Modeling

While [[entities/tvb]] (The Virtual Brain) specializes in whole-brain modeling using [[concepts/neural-mass-model]] at the mesoscopic level, SimBrain operates at a different scale focusing on detailed circuit-level dynamics and learning mechanisms. The two simulators serve complementary but distinct purposes in the computational neuroscience ecosystem. TVB excels at reproducing brain-wide dynamics derived from structural connectivity matrices derived from diffusion imaging data, enabling clinical applications and large-scale connectome modeling that can be validated against empirical neuroimaging recordings[^5].

SimBrain, in contrast, provides the fine-grained mechanistic detail needed to investigate microcircuit-level learning rules, synaptic plasticity mechanisms, and network dynamics that emerge from particular circuit motifs. Researchers can use SimBrain to explore how specific neural architectures compute particular functions, then abstract those mechanisms into reduced models suitable for TVB's whole-brain framework. This multi-scale integration is an important frontier in computational neuroscience, where detailed circuit models inform mesoscopic population models.

For researchers interested in bridging these scales, SimBrain can serve as a detailed circuit model whose activity patterns inform the parameters of reduced neural mass models used in TVB. Conversely, TVB's empirical connectivity data — particularly structural connectivity matrices — can provide biologically realistic constraints when constructing SimBrain network models of specific brain regions.

## Comparisons to Other Simulators

Among computational neuroscience simulators, SimBrain occupies a unique position by prioritizing visual interactivity and educational accessibility. [[entities/brian]] and [[entities/brian2]] provide more established platforms with extensive validation in the computational neuroscience community, offering sophisticated neuron and synapse models with detailed biological realism[^6]. [[entities/nest]] specializes in large-scale spiking neural network simulations suitable for brain-scale modeling, while [[entities/neuron]] provides specialized capabilities for detailed single-neuron and morphologically realistic simulations.

What distinguishes SimBrain is its emphasis on visualization, interactivity, and the ability to embed neural networks in virtual environments. This design philosophy makes it particularly suitable for exploring network dynamics from a qualitative, intuitive perspective, and for educational contexts where students benefit from real-time visual feedback. However, for large-scale simulations or simulations requiring detailed biophysical realism, specialized simulators like NEST or NEURON may be more appropriate.

## Key Papers

The original SimBrain paper (Yoshimi et al., 2012) introduced the software and demonstrated its application to various neural network phenomena including pattern recognition, dynamical systems, and embodied cognition scenarios. The accompanying textbook "Neural Networks in Cognitive Science" provides a comprehensive introduction to neural network theory with hands-on tutorials based on SimBrain simulations. Subsequent work has applied SimBrain to studying the dynamics of recurrent networks, exploring learning rules in competitive architectures, and investigating the relationship between neural activity and phenomenological consciousness.

## Related Software

- [[entities/brian2]] — Advanced spiking neural network simulator with biological realism
- [[entities/nest]] — Large-scale neural network simulator for brain-scale modeling
- [[entities/neuron]] — Simulator for detailed single-neuron and morphologically realistic models
- [[entities/tvb]] — Whole-brain simulation platform for clinical and connectomic applications
- [[bindsnet]] — Spiking neural network library with PyTorch integration
- [[entities/annarchy]] — Python-based simulator with good support for rate-coded and spiking networks

## References

[^1]: Yoshimi, J., et al. (2012). Simbrain. *Neural Networks*, 34, 1-3. https://doi.org/10.1016/j.neunet.2012.04.001

[^2]: SimBrain Official Website. https://simbrain.net

[^3]: SimBrain GitHub Repository. https://github.com/simbrain/simbrain

[^4]: SimBrain Documentation. https://docs.simbrain.net

[^5]: The Virtual Brain. https://www.thevirtualbrain.org

[^6]: Stimberg, M., et al. (2019). Brian 2: an intuitive and efficient neural simulator. *eLife*, 8, e47314.