---
created: 2026-05-06
sources:
- raw/papers/eppler-2009.md
- raw/papers/arxiv-2602.18072.md
- raw/papers/semanticscholar-6adce6f156d9.md
tags:
- software-pynn
- spiking-neural-networks
- python
- simulation
- interoperability
title: PyNN
type: entity
updated: '2026-05-18'
---

# PyNN

**PyNN** (Python Neural Networks) is a Python API for simulator-independent specification of neuronal network models. It provides a common interface to multiple [[spiking-neural-networks|spiking neural network]] simulators, enabling model portability and interoperability.

## Overview

PyNN provides:
- Unified Python API for spiking [[neural-network]] specification
- Backends for [[nest]], [[neuron]], [[brian2]], and other simulators
- Standardized neuron and synapse models
- Network topology and [[connectivity]] specification
- Recording and data analysis tools
- Facilitation of model sharing and [[reproducibility]]

## Simulators Supported
The backends available to PyNN span conventional distributed simulators and emerging neuromorphic hardware, reflecting a broader trend in which Python serves as the lingua franca for spiking network specification. For large-scale simulation, the NEST ecosystem was an early adopter of comprehensive Python interoperability: Eppler et al. introduced PyNEST, a scripting interface that exposes the simulator's full functionality for defining neuron populations, synaptic connections, and simulation parameters, while integrating with NumPy, Matplotlib, and SciPy to support reproducible workflows [[raw/papers/eppler-2009.md|Eppler et al. (2008)]]. At the neuromorphic extreme, Frank et al. describe HiAER-Spike, a reconfigurable event-driven platform capable of executing 160 million neurons and 40 billion synapses via a Python interface that remains agnostic to hardware-level detail and tolerates arbitrary network topologies [[raw/papers/arxiv-2602.18072.md|Frank et al. (2026)]]. Johari et al. further demonstrate a Python-to-hardware compilation framework that translates high-level SNN descriptions into SPICE-level hybrid CMOS-memristor circuits, confirming that a single Python frontend can drive heterogeneous physical substrates [[raw/papers/semanticscholar-6adce6f156d9.md|Johari et al. (2025)]]. These examples illustrate the breadth of targets—from [[nest]]-class distributed simulators through custom [[neuromorphic-computing|neuromorphic]] chips—that a common Python API for [[spiking-neural-networks|spiking neural networks]] must bridge.
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
- [[brian2]] — Python-native, rapid prototyping backend
- [[neuroml2]] — model exchange format compatible with both PyNN and TVB
- [[sonata]] — network description format used by both ecosystems

## References

1. Eppler et al. (2009). *PyNEST: A convenient interface to the NEST simulator*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/neuro.11.012.2008)
2. Gwenevere Frank, Gopabandhu Hota, Keli Wang, C. Deng, Krish Arora, Diana Vins, Abhinav Uppal, Omowuyi Olajide, Kenneth Yoshimoto, Qingbo Wang, Mariko Yamaoka, Johannes Leugering, S. Deiss, Leif Gibb, Gert Cauwenberghs. (2026). *HiAER-Spike Software-Hardware Reconfigurable Platform for Event-Driven Neuromorphic Computing at Scale*. arXiv.org. [DOI](https://doi.org/10.48550/arXiv.2602.18072)
3. Sarah Johari, Arghavan Mohammadhassani, Anup Das. (2025). *A Framework for Automatic Synthesis of Neuromorphic Architectures with Heterogeneous Integration of CMOS and Memristors*. International Symposium on Circuits and Systems. [DOI](https://doi.org/10.1109/ISCAS56072.2025.11043873)