# Illuminati: A Simulation Framework for Modeling and Evaluating Photonic Neural Networks

**Source**: semantic-scholar
**ID**: 45063e481a65803dd10d7dded3d7adb61c7e9551
**DOI**: 10.1109/ISQED65160.2025.11014410
**URL**: https://www.semanticscholar.org/paper/45063e481a65803dd10d7dded3d7adb61c7e9551
**Date**: 2025-04-23
**Year**: 2025
**Authors**: Andy Wolff, Avinash Karanth
**Venue**: IEEE International Symposium on Quality Electronic Design
**Citations**: 0

## Abstract

As the size of the neural network model increases along with complexity, the design of energy-efficient and highly accurate hardware accelerators for implementing complex neural network is becoming a major challenge. Emerging technology such as silicon photonics is an attractive solution for designing hardware accelerators because of its support for parallelism, increased performance per Watt, and higher bandwidth density compared to traditional electronics. While tools exist that can model photonic circuits used in neural networks, there are few that allow for larger scale architectures to be modeled rapidly while maintaining high fidelity. In this paper, we propose Illuminati, a tool designed for rapid design-space exploration of photonic neural network architectures by considering the design challenges of photonic architectures at large scale with inherent parallelism. The simulator implements multiple methods to increase performance and possesses additional optimizations that, in exchange for reduced accuracy, allow large architectures to be modeled without being prohibitively computationally expensive. The C++ implementation allows for the class structure that makes abstraction more practical for users, a PyTorch integration accelerates the linear algebra on which the simulation depends, and DSENT models the power consumption of both photonic components and electrical bac-kend circuits. We validate Illuminati with a photonic simulator and provide a case study with two proposed neural network architectures.
