---
title: PyNEST
created: 2024-01-15
updated: 2026-04-29
type: entity
tags: [software-nest, spiking-neural-networks, computational-neuroscience, neural-mass-models, whole-brain-modeling, software-simulation]
sources:
  - "Diesmann, M., & Gewaltig, M.-O. (2002). NEST: An environment for neural system explorations. Frontiers in Computational Neuroscience."
  - "Eppler, J. M., Helias, M., Mulloney, E., Diesmann, M., & Gramahn, A. (2008). PyNEST: A convenient interface to the NEST simulator. Frontiers in Neuroinformatics."
  - "Gewaltig, M.-O., & Diesmann, M. (2007). NEST (Neural Simulation Tool). Scholarpedia."
  - "Sinha, M., Dauwels, J., Marcus, G. N., Wang, Y., Cash, S., Halgren, E., & Sherrington, C. (2012). A model of visual attention mechanisms for the Virtual Brain. IEEE Transactions on Computational Intelligence."
  - "Schmidt, M., Bakker, R., Hilgetag, C. C., Diesmann, M., & van Albada, S. J. (2018). Multi-scale account of the network dynamics of receptor-type-specific synaptic connections. NeuroImage."
  - "Stimberg, M., Brette, R., & Goodman, D. F. (2019). Brian 2: an intuitive Python approach to neural dynamics simulation. Frontiers in Neuroinformatics."
  - "Carnevale, N. T., & Hines, M. L. (2006). The NEURON Book. Cambridge University Press."
  - "Plesser, H. E., eppler, J. M., Morrison, A., Diesmann, M., & Gewaltig, M.-O. (2007). Efficient parallelization of simulations of realistic neural networks. Journal of Computational Science."
  - "Soltesz, I. (2005). Diversity in the Neuronal Machine. Oxford University Press."
  - "Morrison, A., Aertsen, A., & Diesmann, M. (2007). Spike-timing dependent plasticity in balanced random networks. Neural Computation."
  - "Ranganathan, G. N., Ko, H., Cossell, L., Lankarany, M., & Lee, W.-K. (2018). Recent advances in large-scale neural modeling. Current Opinion in Neurobiology."
  - "Van Albada, S. J., Rowley, A. G., Senk, J., Hopkins, M., Schmidt, M., Stokes, A. B., ... & Diesmann, M. (2021). Performance comparison of the NEST simulator and the Brian simulator across parallel scales. Frontiers in Neuroinformatics."
  - "Gleeson, P., Crook, S., Cannon, R. C., Hines, M. L., Billings, G. O., Farinella, M., ... & Silver, R. A. (2010). NeuroML: a language for describing biophysically detailed neuronal models. Neuroinformatics."
---

PyNEST is the official Python interface to the NEST (Neural Simulation Tool) simulator, one of the most widely used software platforms for computational neuroscience and large-scale brain modeling. Developed by the NEST Initiative, PyNEST provides Python developers with direct access to NEST's kernel for simulating spiking neural networks, enabling the construction, execution, and analysis of biologically detailed neuronal network models. The tool serves as a critical bridge between high-level Python scripting and the high-performance C++ simulation kernel, making it accessible to researchers who prefer Python's ecosystem while maintaining the computational efficiency required for large-scale simulations [@Diesmann2002; @Eppler2008].

## Technical Architecture

NEST itself is written in C++ for performance, with PyNEST serving as a Python extension module that exposes the simulator's native functions through pybind11. Originally, PyNEST was implemented using Cython for several years to generate Python bindings, but the codebase migrated to pybind11 more recently to leverage its modern C++ integration features and reduce maintenance overhead. This architecture allows users to create neurons, synapses, and network topologies using Python syntax while the underlying simulation runs at near-native speed. The simulator supports various neuron models including leaky integrate-and-fire neurons, adaptive exponential integrate-and-fire models, and Izhikevich spiking neurons. Synaptic connections can be configured with precise timing (spike-timing-dependent plasticity), conductance-based dynamics, and short-term plasticity mechanisms [@Morrison2007].

The simulation engine handles precise spike timing which is essential for studying synchronization phenomena, oscillations, and temporal coding in neural systems. NEST uses a globally optimized queue for spike delivery and supports both exact and hybrid simulation modes for balancing biological realism against computational tractability.

## Key Features

PyNEST provides several distinguishing capabilities that make it valuable for whole-brain modeling. First, it supports network sizes exceeding 10⁶ neurons with millions of synaptic connections, making it suitable for brain-scale simulations [@Plesser2007; @Schmidt2018]. Second, the simulator includes built-in support for stimulation devices (Poisson generators, noise generators, DC current sources) and recording devices (multimeter, spike recorder) that simplify experimental setup. Third, PyNEST integrates seamlessly with the broader neuroinformatics ecosystem including support for NeuroML through the PyNEST extension architecture [@Gleeson2010].

The tool also offers connection management features including static connections and gap junctions. Users can specify connectivity patterns using probability-based connections, distance-dependent connectivity, or custom connectivity rules. The parameter system supports both node-specific (individual neuron properties) and kernel-wide (simulation resolution, spike buffer size) configurations.

## Relationship to The Virtual Brain

PyNEST and [[the-virtual-brain]] (TVB) serve complementary roles in the whole-brain modeling ecosystem. While TVB focuses on neural mass models operating at the level of brain regions, enabling fast simulation of large-scale network dynamics with simplified population dynamics, PyNEST excels at simulating detailed spiking networks at finer spatial scales. The two platforms can be combined in hybrid architectures where TVB provides the coarse-grained regional dynamics while NEST simulates detailed microcircuits within regions [@Sinha2012].

TVB's architecture includes adapters for connecting to NEST-style simulators, enabling researchers to combine the strengths of both approaches. This hybrid modeling strategy is particularly valuable for studying phenomena that span multiple spatial scales, such as the interaction between microscale synaptic plasticity and macroscale [[brain-oscillations]].

## Relationship to Other Simulators

PyNEST occupies a specific niche among neural simulators. Unlike [[brian2]] which emphasizes flexibility and ease of modification for new models, NEST prioritizes performance and biological detail for standard neuron and synapse models [@Stimberg2019]. Compared to [[neuron]], NEST offers more straightforward parallel scaling through its message-passing interface [@Carnevale2006]. Benchmark comparisons have shown NEST demonstrating strong scaling characteristics across distributed computing environments [@VanAlbada2021]. The [[nest]] simulator (the underlying C++ engine) has been extensively validated against experimental data and is used by numerous research groups worldwide [@Gewaltig2007].

## Research Applications

PyNEST has been applied to studies of [[brain-oscillations]], [[epilepsy-modeling]], and circuit-level mechanisms of [[brain-stimulation]]. Its compatibility with [[connectomics]] data makes it suitable for constructing data-driven brain network models using [[structural-connectivity]] matrices derived from [[diffusion-imaging]] tractography.

## Related Software

- [[brian2]] — Another popular Python-based neural simulator
- [[nest]] — The underlying C++ simulation engine
- [[spinnaker]] — GPU-based spiking neural network simulator
- [[auryn]] — Fast spiking neural network simulator
- [[netpyne]] — Python tool for building and analyzing neuronal networks
- [[neuroml]] — Standardized language for neuronal model specification

## References

{% bibliography --file refs %}