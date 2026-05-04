# GPU Acceleration for Faster Evolutionary Spatial Cyclic Game Systems

**Source**: semantic-scholar
**ID**: 753617f088df28eeeef83f508240dcd8fde926c9
**DOI**: 10.2139/ssrn.5238901
**URL**: https://www.semanticscholar.org/paper/753617f088df28eeeef83f508240dcd8fde926c9
**Date**: 2025-08-17
**Year**: 2025
**Authors**: Louie Sinadjan
**Venue**: Social Science Research Network
**Citations**: 0

## Abstract

This dissertation presents the design, implementation and evaluation of GPU-accelerated simulation frameworks for Evolutionary Spatial Cyclic Games (ESCGs), a class of agent-based models used to study ecological and evolutionary dynamics. Traditional single-threaded ESCG simulations are computationally expensive and scale poorly. To address this, high-performance implementations were developed using Apple's Metal and Nvidia's CUDA, with a validated single-threaded C++ version serving as a baseline comparison point. Benchmarking results show that GPU acceleration delivers significant speedups, with the CUDA maxStep implementation achieving up to a 28x improvement. Larger system sizes, up to 3200x3200, became tractable, while Metal faced scalability limits. The GPU frameworks also enabled replication and critical extension of recent ESCG studies, revealing sensitivities to system size and runtime not fully explored in prior work. Overall, this project provides a configurable ESCG simulation platform that advances the computational toolkit for this field of research. This dissertation forms the basis for a paper accepted for publication and presentation at the European Modelling and Simulation Symposium.
