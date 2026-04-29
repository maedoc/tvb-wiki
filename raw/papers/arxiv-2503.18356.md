# GRiNS: a python library for simulating gene regulatory network dynamics

**Source**: semantic-scholar
**ID**: d665abf8d2579de981596841072f052c3d201fa9
**DOI**: 10.1186/s12859-025-06268-0
**URL**: https://www.semanticscholar.org/paper/d665abf8d2579de981596841072f052c3d201fa9
**Date**: 2025-03-24
**Year**: 2025
**Authors**: Pradyumna Harlapur, Harshavardhan Bv, M. Jolly
**Venue**: BMC Bioinformatics
**Citations**: 0

## Abstract

The emergent dynamics of complex gene regulatory networks govern various cellular processes. However, understanding these dynamics is challenging due to the difficulty of parameterizing the computational models for these networks, especially as the network size increases. Here, we introduce a simulation library, Gene Regulatory Interaction Network Simulator (GRiNS), to address these challenges. GRiNS integrates popular parameter-agnostic simulation frameworks, RACIPE and Boolean Ising formalism, into a single Python library capable of leveraging GPU acceleration for efficient and scalable simulations. GRiNS extends the ordinary differential equations (ODE) based RACIPE framework with a more modular design, allowing users to choose parameters, initial conditions, and time-series outputs for greater customisability and accuracy in simulations. For large networks, where ODE-based simulation formalisms do not scale well, GRiNS implements Boolean Ising formalism, providing a simplified, coarse-grained alternative, significantly reducing the computational cost while capturing key dynamical behaviours of large regulatory networks. GRiNS enables parameter-agnostic modeling of gene regulatory networks to study their dynamic and steady-state behaviors in a scalable and efficient manner. The documentation and installation instructions for GRiNS can be found at https://moltenecdysone09.github.io/GRiNS/.
