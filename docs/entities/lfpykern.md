---
created: 2024-03-15
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/semanticscholar-bceb6bea8311.md
tags:
- software
- lfp
- volume-conduction
- computational-neuroscience
title: LFPykern
type: entity
updated: '2026-05-05'
---

LFPykern is a Python library for computing local field potentials (LFPs) from spiking neural network simulations. The software implements a kernel-based approach to calculating the extracellular electric potential resulting from transmembrane currents in model neurons. Unlike full compartmental models that require detailed morphology, LFPykern works with point neuron simulators such as [[nest]], [[neuron]], and [[brian2cuda]], making it computationally tractable for large-scale network simulations while still providing biophysically grounded LFP predictions.

## Motivation and Context

The [[local-field-potentials|local field potential]] represents the summed electrical activity of thousands to millions of neurons in the vicinity of a recording electrode. In [[computational-neuroscience]], there has long been a gap between detailed biophysical models that can simulate LFPs accurately but are computationally expensive, and simplified firing-rate or neural mass models that run at scale but cannot produce electrophysiological signals that can be directly compared to EEG or intracortical recordings. LFPykern bridges this gap by providing a method to compute LFPs from point-neuron network models using an analytical solution to the [[volume-conduction]] problem.

The approach relies on the principle that the extracellular potential at any point in space can be computed as a weighted sum of the transmembrane currents in all neurons, where the weights depend on the geometry of the neural tissue and the position of the recording electrode. By pre‑computing these "kernels" for a given brain region geometry and electrode configuration, LFPykern enables real‑time or near‑real‑time LFP calculation during network simulations. This makes it particularly valuable for studies that require comparison with empirical EEG or LFP data, such as [[epilepsy-modeling]], [[brain-stimulation]] research, and investigations of [[resting-state]] dynamics.

## Technical Approach

LFPykern implements several volume conduction models of increasing sophistication. The simplest is the point source approximation, where each neuron is treated as a point current source in a homogeneous, isotropic conducting medium. This model provides a first‑order approximation that scales linearly with the number of neurons. More refined models include the line source approximation, which represents dendritic cables as line sources, and the finite‑extent kernel approach that accounts for the spatial distribution of transmembrane currents within individual neurons.

The mathematical foundation rests on the solution to the Poisson equation for quasi‑static [[electrophysiology]], where the extracellular potential φ(r) at position r is given by:

φ(r) = (1/4πσ) ∑ᵢ ∫ Iᵢ(s) / |r - s| ds

where σ is the extracellular conductivity, Iᵢ(s) is the transmembrane current density at position s along neuron i, and the integral is taken over the neuronal morphology. LFPykern approximates this integral using either analytical solutions for simplified geometries or precomputed numerical kernels for arbitrary morphologies.

## Key Features

The library provides several notable capabilities. First, it supports multiple neuron simulators through a standardized interface, allowing users to run simulations in [[nest]], NEURON, or Brian and compute LFPs without modifying their simulation code. Second, LFPykern implements efficient kernel computation using Cython for performance‑critical sections, achieving near-[[linear]] scaling with neuron count for typical electrode configurations. Third, the software includes built‑in support for various electrode geometries including single‑site contacts, linear probes (such as Michigan‑style arrays), and Utah arrays, enabling simulation of common experimental setups. Fourth, LFPykern provides both Python and MATLAB interfaces, facilitating integration with existing analysis pipelines. Finally, the library includes validation tools comparing computed LFPs against analytical solutions and experimental measurements.

## Relationship to TVB

While [[the-virtual-brain]] primarily relies on [[neural-mass-models]] and mean‑field approaches for whole‑brain dynamics, the software has explored integration with detailed neuron‑level simulations for specific applications. The [[tvb-nest]] adapter enables co‑simulation between TVB's mesoscopic population models and NEST‑based microscopic simulations, and LFPykern could in principle be used to compute LFPs from such hybrid simulations to enable direct comparison with intracranial EEG recordings. More broadly, LFPykern represents a complementary approach to TVB's own forward modeling capabilities, which focus on extracting [[bold-signal]] and EEG from large‑scale network dynamics rather than simulating detailed transmembrane currents. For researchers interested in combining whole‑brain connectome‑based modeling with biophysically detailed neuron‑level simulations, LFPykern offers a bridge between these scales of investigation.

## Related Software

LFPykern builds upon and relates to several other tools in the computational neuroscience ecosystem. The [[lfpy]] library provides more detailed LFP computation using full morphological reconstructions but at higher computational cost. The [[nest]] simulator serves as the primary neuron simulation backend for many LFPykern applications. Volume conduction models similar to those in LFPykern are implemented in [[hopfield]] and LFPy2 for different use cases. For forward modeling of EEG rather than LFP, the [[openmeeg]] software provides boundary element method solutions suitable for whole‑head models.

## References

1. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz‑Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi‑Scale Co‑Simulation Framework with a Case Study on Neural‑Level Seizure Generation and [[whole‑brain]] Propagation*. [Link](https://arxiv.org/abs/2505.16861)
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz‑Pier, Thanos Manos. (2026). *Arbor‑TVB: a novel multi‑scale co‑simulation framework with a case study on neural‑level seizure generation and whole‑brain propagation*. Frontiers Comput. Neurosci.. [DOI](https://doi.org/10.3389/fncom.2025.1731161)
3. Max C. W. Engelen, River Betting, Christos Strydis. (2025). *SimHH: A Versatile, Multi‑GPU Simulator for Extended Hodgkin‑Huxley Networks*. IEEE Access. [DOI](https://doi.org/10.1109/ACCESS.2025.3550444)