# NESTML: a generic modeling language and code generation tool for the simulation of spiking neural networks with advanced plasticity rules

**Source**: semantic-scholar
**ID**: 5c84b271b035473f4f6e33fffef9b3c6737bc247
**DOI**: 10.3389/fninf.2025.1544143
**URL**: https://www.semanticscholar.org/paper/5c84b271b035473f4f6e33fffef9b3c6737bc247
**Date**: 2025-06-04
**Year**: 2025
**Authors**: C. Linssen, Pooja N. Babu, Jochen M. Eppler, Luca Koll, Bernhard Rumpe, Abigail Morrison
**Venue**: Frontiers Neuroinformatics
**Citations**: 8

## Abstract

With increasing model complexity, models are typically re-used and evolved rather than starting from scratch. There is also a growing challenge in ensuring that these models can seamlessly work across various simulation backends and hardware platforms. This underscores the need to ensure that models are easily findable, accessible, interoperable, and reusable—adhering to the FAIR principles. NESTML addresses these requirements by providing a domain-specific language for describing neuron and synapse models that covers a wide range of neuroscientific use cases. The language is supported by a code generation toolchain that automatically generates low-level simulation code for a given target platform (for example, C++ code targeting NEST Simulator). Code generation allows an accessible and easy-to-use language syntax to be combined with good runtime simulation performance and scalability. With an intuitive and highly generic language, combined with the generation of efficient, optimized simulation code supporting large-scale simulations, it opens up neuronal network model development and simulation as a research tool to a much wider community. While originally developed in the context of NEST Simulator, NESTML has been extended to target other simulation platforms, such as the SpiNNaker neuromorphic hardware platform. The processing toolchain is written in Python and is lightweight and easily customizable, making it easy to add support for new simulation platforms.
