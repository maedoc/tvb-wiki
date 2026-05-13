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
updated: '2026-05-13'
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

PyNN backends span a continuum from conventional software simulators to custom neuromorphic hardware, enabling the same network specification to execute on platforms that differ by orders of magnitude in scale, energy efficiency, and architectural approach. The [[nest]] backend traces its lineage to Python interfacing work that exposes the simulator's full functionality through a high-level scripting API, integrating with NumPy and Matplotlib to enable rapid prototyping and reproducible sharing of simulation scripts [[raw/papers/eppler-2009.md|Eppler et al. (2008)]]. Event-driven neuromorphic platforms move computation onto dedicated hardware optimized for sparse connectivity and sparse activity. Frank et al. demonstrated a reconfigurable system capable of supporting 160 million neurons and 40 billion synapses—roughly twice the scale of a mouse brain—at faster-than-real-time speeds, shielding users from hardware complexity through hardware-agnostic Python programming interfaces [[raw/papers/arxiv-2602.18072.md|Frank et al. (2026)]]. Complementing this, Johari et al. introduced frameworks for automatically synthesizing hybrid CMOS-memristor neuromorphic architectures from high-level Python descriptions, compiling spiking network models down to SPICE-level circuit designs that significantly enhance energy efficiency over conventional CMOS implementations [[raw/papers/semanticscholar-6adce6f156d9.md|Johari et al. (2025)]]. Between these extremes, the [[neuron]] backend targets detailed multicompartment morphological modeling, while [[brian2|Brian]] provides a flexible, Python-native environment suited to rapid prototyping.

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
- [[brian2]] — Python-native, rapid prototyping backend
- [[neuroml2]] — model exchange format compatible with both PyNN and TVB
- [[sonata]] — network description format used by both ecosystems

## References

1. Eppler et al. (2009). *[[pynest]]: A convenient interface to the NEST simulator*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/neuro.11.012.2008))
2. Gwenevere Frank, Gopabandhu Hota, Keli Wang, C. Deng, Krish Arora, Diana Vins, Abhinav Uppal, Omowuyi Olajide, Kenneth Yoshimoto, Qingbo Wang, Mariko Yamaoka, Johannes Leugering, S. Deiss, Leif Gibb, Gert Cauwenberghs. (2026). *HiAER-Spike Software-Hardware Reconfigurable Platform for Event-Driven [[neuromorphic-computing]] at Scale*. arXiv.org. [DOI](](https://doi.org/10.48550/arXiv.2602.18072))
3. Sarah Johari, Arghavan Mohammadhassani, Anup Das. (2025). *A Framework for Automatic Synthesis of Neuromorphic Architectures with Heterogeneous Integration of CMOS and Memristors*. International Symposium on Circuits and Systems. [DOI](](https://doi.org/10.1109/ISCAS56072.2025.11043873))