---
created: 2026-05-06
sources: []
tags:
- software-pynn
- spiking-neural-networks
- python
- simulation
- interoperability
title: PyNN
type: entity
updated: '2026-05-06'
---

# PyNN

**PyNN** (Python Neural Networks) is a Python API for simulator-independent specification of neuronal network models. It provides a common interface to multiple [[spiking-neural-networks|spiking neural network]] simulators, enabling model portability and interoperability.

## Overview

PyNN provides:
- Unified Python API for spiking [[neural-network]] specification
- Backends for [[nest]], [[neuron]], [[brian]], and other simulators
- Standardized neuron and synapse models
- Network topology and [[connectivity]] specification
- Recording and data analysis tools
- Facilitation of model sharing and [[reproducibility]]

## Simulators Supported

| Simulator | Backend | Scale |
|-----------|---------|-------|
| **NEST** | `pyNN.nest` | Large-scale distributed |
| **NEURON** | `pyNN.neuron` | Detailed multicompartment |
| **Brian** | `pyNN.brian` | Flexible, Python-native |
| **BrainScaleS** | `pyNN.brainscales` | Neuromorphic hardware |
| **SpiNNaker** | `pyNN.spiNNaker` | Massively parallel |

## Relationship to TVB

PyNN and TVB operate at different scales but are complementary:
- **PyNN** focuses on spiking neuron-level simulation (microscale)
- **TVB** focuses on neural mass/field models at the [[whole-brain]] scale (macroscale)
- PyNN-generated spiking data can inform TVB [[neural-mass-models|neural mass model]] parameterization
- TVB [[mean-field-theory|mean-field]] outputs can seed PyNN network states
- Both use Python and share ecosystem tools ([[neo]], [[nibabel]])
- The [[neuroml]] and [[lems]] standards bridge PyNN and TVB model descriptions
- Future integration: TVB-PyNN hybrid models combining regional mean-field with local spiking detail

## Software Ecosystem

- [[nest]] — primary large-scale backend for PyNN
- [[neuron]] — detailed morphological backend
- [[brian]] — Python-native, rapid prototyping backend
- [[neuroml2]] — model exchange format compatible with both PyNN and TVB
- [[sonata]] — network description format used by both ecosystems

## References

- PyNN website: http://neuralensemble.org/PyNN/
- Davison et al. (2009) — PyNN: a common interface for neuronal network simulators
- Davison et al. (2008) — Coordination of neuronal network simulators