---
title: STEPS
created: 2024-01-15
updated: 2026-04-23
type: entity
tags: [software-brain-modeling, spiking-neural-networks, stochastic-differential-equations, molecular-simulation]
sources: [https://steps.sourceforge.net/, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3418487/, https://www.frontiersin.org/articles/10.3389/fninf.2014.00041/full]
---

# STEPS

## Overview

**STEPS** (STochastic Engine for Pathway Simulation) is a software package for simulating stochastic reaction-diffusion systems in complex three-dimensional geometries. Originally developed at the University of Antwerp and continuing development at the Okinawa Institute of Science and Technology (OIST), STEPS enables detailed molecular-level modeling of neuronal signaling pathways, including calcium dynamics, synaptic transmission, and second-messenger cascades. The software bridges the gap between molecular kinetics and cellular physiology by treating stochasticity and spatial organization as first-class modeling concerns.

STEPS is implemented in C++ with a Python interface, combining computational performance with accessibility. It employs the spatial stochastic simulation algorithm to track individual molecules diffusing and reacting within detailed cellular morphologies represented as tetrahedral meshes.

## Key Features

**Spatial Stochastic Simulation.** Unlike deterministic solvers such as [[NEURON]] or compartmental models in [[Brian]], STEPS uses exact or approximate stochastic algorithms to simulate individual molecular copy numbers. This captures intrinsic noise in biochemical pathways, which can be functionally significant at small molecule counts.

**Tetrahedral Mesh Geometry.** STEPS represents cellular volumes using unstructured tetrahedral meshes, enabling accurate modeling of complex morphologies like dendritic spines, the endoplasmic reticulum, and synaptic clefts. This goes beyond simple compartmental approximations common in neural simulators.

**Hybrid Solver Architecture.** The software supports multiple simulation approaches through a unified interface: the spatial Gillespie exact method, multinomial diffusion approximation, and operator-splitting methods for larger systems. Users can select appropriate trade-offs between accuracy and computational cost.

**Parallelization.** STEPS implements parallel solvers using MPI and GPU acceleration to handle large-scale spatial simulations that would otherwise be computationally prohibitive.

**SBML Import and Mesh Tools.** STEPS supports import of models in the Systems Biology Markup Language (SBML) format and provides tetrahedral mesh generation capabilities for importing and processing realistic cellular morphologies.

## Relationship to TVB

STEPS and [[The Virtual Brain]] operate at complementary scales in the multi-scale brain modeling pipeline:

| Aspect | STEPS | TVB |
|--------|-------|-----|
| **Scale** | Molecular/cellular (nm to µm) | Whole-brain network (mm to cm) |
| **Granularity** | Single molecules | Neural masses / mean-field populations |
| **Stochasticity** | Intrinsic molecular noise | Statistical/phenomenological |
| **Spatial** | 3D cellular ultrastructure | Large-scale connectivity |

While STEPS models the detailed biophysics of synaptic and subcellular processes, [[The Virtual Brain]] abstracts these into population-level dynamics. A complete multi-scale workflow could potentially use STEPS simulations to parameterize synaptic transmission models that feed into TVB's connectome-based simulations. Similarly, [[NEST]] serves as an intermediate layer for spiking network simulations between these extremes.

## Key Papers

- Hepburn et al. (2012). *STEPS: Efficient Simulation of Stochastic Reaction-Diffusion Models in Realistic Morphologies.* BMC Systems Biology. Introduces the core spatial stochastic simulation framework and demonstrates tetrahedral mesh representation of cellular geometries.

- Chen & De Schutter (2014). *STEPS: Modeling and Simulating Complex Reaction-Diffusion Systems with Python.* Frontiers in Neuroinformatics. Details the Python interface and hybrid solver architecture.

- Chen, W., Hepburn, I., & De Schutter, E. (2020). *Parallel STEPS: Large Scale Stochastic Spatial Reaction-Diffusion Simulation with High Performance Computers.* Frontiers in Neuroinformatics. Describes MPI parallelization enabling large-scale simulations of realistic neuronal morphologies.

## Related Software

- [[NEURON]] — Compartmental modeling with deterministic reaction-diffusion, operates at similar scales but with different approaches to spatial and stochastic modeling
- [[Brian]] — Python-based spiking neural network simulator; includes stochastic elements at the network level but uses compartmental approximations
- [[The Virtual Brain]] — Whole-brain network modeling, potential downstream consumer of STEPS-derived synaptic parameters
- [[MOOSE]] — Multiscale Object-Oriented Simulation Environment; supports reaction-diffusion simulations and stochastic methods including Gillespie algorithms

## References

1. Hepburn, I., Chen, W., Wils, S., & De Schutter, E. (2012). STEPS: Efficient simulation of stochastic reaction-diffusion models in realistic morphologies. *BMC Systems Biology*, 6(1), 36.

2. Chen, W., & De Schutter, E. (2014). STEPS—Modeling and simulating complex reaction-diffusion systems with Python. *Frontiers in Neuroinformatics*, 8, 41.

3. Chen, W., Hepburn, I., & De Schutter, E. (2020). Parallel STEPS: Large scale stochastic spatial reaction-diffusion simulation with high performance computers. *Frontiers in Neuroinformatics*, 14, 11.
