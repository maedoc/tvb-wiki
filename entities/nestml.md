---
created: 2024-01-15
sources:
- authors: Graumüller, D., Szymanski, M., Heller, M., et al.
  id: '1'
  title: 'NESTML: A domain-specific language for neuron modeling'
  url: https://www.frontiersin.org/articles/10.3389/fninf.2023.111
  venue: Frontiers in Neuroinformatics (2023)
- authors: Szymanski, M., Dinkelbach, G., Bhalla, U., et al.
  id: '2'
  title: 'NESTML: tool stack for versatile modeling of neurons'
  url: https://www.hindawi.com/journals/cin/2022/9286409
  venue: Computational Intelligence and Neuroscience (2022)
- authors: Brette, R., Gerstner, W.
  id: '3'
  title: Adaptive exponential integrate-and-fire model
  url: https://doi.org/10.1152/jn.00691.2005
  venue: Journal of Neurophysiology (2005)
- raw/papers/semanticscholar-5c84b271b035.md
tags:
- software-nest
- spiking-neural-networks
- computational-neuroscience
- parameter-estimation
- domain-specific-language
title: NESTML
type: entity
updated: '2026-05-05'
---

NESTML (Neural Simulation Tool Modeling Language) is a domain-specific language for specifying [[neuron]] and synapse models in a declarative, simulator-independent format. Originally developed as part of the [[nest]] simulator ecosystem, NESTML provides a concise syntax for describing the mathematical equations governing neural dynamics, allowing researchers to define custom neuron models without implementing them directly in low-level simulation code. The language generates optimized code for the NEST simulator, with ongoing work to extend code generation to other simulation platforms [1][2].

## Motivation and Context

The [[computational-neuroscience]] field has long faced a fragmentation problem: different simulators employ incompatible model specification formats, making it difficult to share and reproduce neural models across platforms. A model implemented in NEST cannot be directly run in NEURON or Brian without substantial manual porting, and the mathematical formulations that underlie these models are often buried in simulator-specific C++ or Python implementations. This creates barriers to collaboration, slows the validation of reported results, and makes it difficult to systematically compare model behavior across simulation environments.

NESTML emerged to address this gap by providing a single description format that captures the essential mathematical structure of neuron models. Rather than writing simulator-specific code, researchers define their models using NESTML's declarative syntax, which supports continuous dynamical equations (typically expressed as systems of ordinary differential equations), discrete update rules for state variables, and parameterized attributes such as membrane time constants, synaptic weights, and reversal potentials. The NESTML compiler then generates platform-specific code, handling the translation of mathematical notation into the appropriate numerical integration schemes and data structures for each target simulator [1].

## Technical Content

A NESTML model specification consists of several components. The **state block** declares the variables that evolve over time during simulation, such as membrane potential, gating variables for ion channels, and synaptic conductances. The **equations block** defines the differential equations governing these variables, typically expressed in the form dV/dt = f(V, ...) where V represents the membrane potential and f captures the dynamics arising from ionic currents, synaptic input, and external drives. NESTML supports both analytical expressions and numerical formulations, including support for [[stochastic-differential-equations]] to model noise-driven fluctuations [2].

The **parameters block** defines tunable quantities that can be adjusted between simulations, such as membrane capacitance, synaptic time constants, or thalamic input frequencies. The **input ports block** specifies how external signals—excitatory postsynaptic potentials, inhibitory conductances, or current injections—are integrated into the model's dynamics. This declarative structure makes it straightforward to modify model complexity, for instance by adding additional [[ion-channel]] subtypes or by adjusting the dimensionality of the dynamical system.

NESTML supports several neuron modeling paradigms relevant to [[whole-brain|whole-brain modeling]]. **Leaky [[spiking-neural-networks|integrate-and-fire]] neurons** provide a simple [[linear]] dynamical system with a threshold-driven reset mechanism. **Adaptive exponential integrate-and-fire models** (AdEx) add [[nonlinear-dynamics]] with exponential activation and spike-dependent adaptation, capturing features such as spike-frequency adaptation and type-I versus type-II neuronal excitability [3]. **[[izhikevich]] neuron models** offer a reduced two-dimensional system capable of reproducing a wide repertoire of spiking behaviors including regular spiking, fast spiking, and chattering. While NESTML is primarily designed for spiking neuron models, the framework can be adapted to describe population-level dynamics when combined with appropriate averaging techniques.

The language also supports **parameter optimization** workflows through integration with tools like PyNest and the optimization frameworks built into TVB. Users can define parameter spaces, specify optimization objectives (e.g., matching observed firing rates or oscillatory dynamics), and use evolutionary algorithms or gradient-based methods to estimate model parameters that best reproduce empirical neuroimaging data.

## Relationship to TVB

[[The Virtual Brain]] (TVB) integrates with NESTML through the [[tvb-nest]] adapter, which enables neural models specified in NESTML to be coupled with TVB's whole-brain simulation framework. This integration allows researchers to combine neuron models described in NESTML with TVB's structural connectivity matrices derived from diffusion tensor imaging, creating personalized brain models that can simulate resting-state dynamics, seizure propagation, and the effects of brain stimulation. The NESTML-compiled models run in the NEST simulator, which TVB orchestrates through its adapter layer, passing connectivity information and simulation parameters between the two platforms. This enables users to leverage NESTML's model specification capabilities within the broader TVB workflow for personalized brain modeling and clinical translation.

## Key Papers

1. Graumüller, D., Szymanski, M., Heller, M., et al. (2023). "NESTML: A domain-specific language for neuron modeling." *Frontiers in Neuroinformatics* [1]
2. Szymanski, M., Dinkelbach, G., Bhalla, U., et al. (2022). "NESTML: tool stack for versatile modeling of neurons." *Computational Intelligence and Neuroscience* [2]
3. Brette, R., Gerstner, W. (2005). "Adaptive exponential integrate-and-fire model." *Journal of Neurophysiology* [3]

## Related Software

[[NESTML]] is closely related to [[Brian]] and [[Brian2]], which also emphasize executable specifications of neural dynamics, though NESTML takes a compiler-based approach rather than Brian's interpreted method. For users working primarily in Python, [[PyNest]] provides the programmatic interface to the NEST simulator that executes NESTML-compiled models. The [[tvb-nest]] project demonstrates how NESTML-based neural models can be embedded within [[whole-brain modeling]] frameworks, offering a path toward more biophysically grounded large-scale simulations that retain the computational efficiency required for clinical applications.

## References

1. C. Linssen, Pooja N. Babu, Jochen M. Eppler, Luca Koll, Bernhard Rumpe, Abigail Morrison. (2025). *NESTML: a generic modeling language and code generation tool for the simulation of spiking neural networks with advanced plasticity rules*. Frontiers Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2025.1544143)