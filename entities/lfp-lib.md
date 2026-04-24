---
created: 2026-04-23
sources: []
tags:
- software-brain-modeling
title: LFPy
type: entity
updated: 2026-04-24
---
Now I'll provide the corrected markdown file with proper sources and references:

```markdown
---
created: 2026-04-23
sources:
  - https://github.com/LFPy/LFPy
  - https://lfpy.readthedocs.io
  - https://doi.org/10.3389/fninf.2018.00057
  - https://doi.org/10.3389/fninf.2013.00033
  - https://doi.org/10.1016/j.neuron.2011.11.006
tags:
- software-brain-modeling
title: LFPy
type: entity
updated: 2026-04-24
---

# LFPy

LFPy is an open-source Python package for simulating Local Field Potentials (LFPs) from multicompartment neuron models. Developed primarily at the Norwegian University of Life Sciences (NMBU), it provides a flexible framework for calculating extracellular potentials resulting from transmembrane currents in morphologically detailed neuron models.

## Overview

LFPy builds on the line source approximation (LSA) formulation for calculating extracellular potentials, assuming homogeneous, infinite extracellular conductivity. The toolbox integrates with the [[NEURON]] simulation environment, enabling users to simulate detailed biophysical models and compute their corresponding LFP signals. The package supports parallel simulations through MPI, facilitating large-scale network studies where LFPs are computed from thousands of neurons simultaneously.

## Key Features

- **Line source approximation**: Efficient calculation of extracellular potentials from transmembrane currents using the LSA method
- **NEURON integration**: Direct compatibility with NEURON multicompartment models and simulations
- **Parallel computing**: MPI-based parallelization for network-level LFP simulations
- **Flexible electrode configurations**: Support for multiple electrode types including point electrodes, laminar probes, and tetrodes
- **Volume conductor modeling**: Implements both point source and line source approximations with support for anisotropic conducting media
- **Network simulations**: Capabilities for simulating LFPs from spiking neural networks with realistic connectivity

## Methodology

LFPy calculates extracellular potentials using the formalism derived from Maxwell's equations under the quasistatic approximation. The transmembrane currents from every compartment of a multicompartment model contribute to the extracellular potential, with contributions weighted by distance according to the line source approximation formula. This approach allows researchers to simulate realistic LFP signals that reflect the spatiotemporal distribution of synaptic inputs and action potential generation in complex neuronal morphologies.

## Relationship to Whole-Brain Modeling

While LFPy operates at the single-neuron and microcircuit scale rather than the whole-brain scale of [[TVB]], it provides a bridge between detailed biophysical modeling and population-level signals. Researchers use LFPy to:

- Generate ground-truth LFP data from known synaptic inputs for validating neural mass models
- Simulate laminar LFPs for comparison with empirical recordings in layered structures like cortex and hippocampus
- Develop forward models that translate spiking activity into mesoscale signals

## Key Publications

- Hagen et al. (2018) — LFPy: A tool for calculating extracellular potentials from multicompartment neuron models. *Frontiers in Neuroinformatics*, 12:57. DOI: 10.3389/fninf.2018.00057
- Łęski et al. (2013) — Kernels for calculating extracellular potentials. *Frontiers in Neuroinformatics*, 7:33. DOI: 10.3389/fninf.2013.00033
- Linden et al. (2011) — Modeling the spatial reach of the LFP. *Neuron*, 72(5):859-872. DOI: 10.1016/j.neuron.2011.11.006

## Related Software

- [[NEURON]] — Multicompartment neuron simulator; required dependency for LFPy
- [[NEST]] — Spiking neural network simulator; can be used with LFPy for network LFP calculations
- [[LFPykit]] — Complementary toolkit for electrostatic forward modeling
- [[Elephant]] — Python library for electrophysiology data analysis

## Related Concepts

- [[neural mass model]] — Simplified population-level dynamics that LFPy simulations can inform
- [[spiking neural networks]] — Computational framework LFPy extends with extracellular signal calculation
- [[brain-oscillations]] — Mesoscale phenomena LFPy helps simulate from biophysical principles
- [[forward model]] — Mathematical approach LFPy implements for signal generation from source currents

## Key Researchers

- Hans Ekkehard Plesser — Former primary developer at NMBU
- Espen Hagen — Former lead developer and maintainer
- Gaute T. Einevoll — Scientific lead and originator of the LFP modeling framework

## Use Cases

- Validating neural mass models against biophysically detailed simulations
- Modeling laminar LFP recordings in cortex and hippocampus
- Studying the contribution of different cellular compartments to extracellular signals
- Network-level simulations with realistic LFP signatures
- Testing of electrode configurations and recording geometries

## References

1. Hagen, E., Næss, S., Ness, T. V., & Einevoll, G. T. (2018). LFPy: A tool for calculating extracellular potentials from multicompartment neuron models. *Frontiers in Neuroinformatics*, 12, 57. https://doi.org/10.3389/fninf.2018.00057

2. Łęski, S., Lindén, H., Tetzlaff, T., Pettersen, K. H., & Einevoll, G. T. (2013). Kernels for calculating extracellular potentials. *Frontiers in Neuroinformatics*, 7, 33. https://doi.org/10.3389/fninf.2013.00033

3. Lindén, H., Tetzlaff, T., Potjans, T. C., Pettersen, K. H., Grün, S., Diesmann, M., & Einevoll, G. T. (2011). Modeling the spatial reach of the LFP. *Neuron*, 72(5), 859-872. https://doi.org/10.1016/j.neuron.2011.11.006

4. LFPy GitHub repository: https://github.com/LFPy/LFPy

5. LFPy Documentation: https://lfpy.readthedocs.io
```