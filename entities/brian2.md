---
title: "Brian2"
created: 2026-05-06
updated: 2026-05-06
type: entity
tags: [software-brian, spiking-neural-networks, python, simulation]
sources: []
---

# Brian2

**Brian2** is a Python-based simulator for spiking neural networks. It is the successor to the original Brian simulator and is designed for rapid prototyping of neural models with high performance.

## Overview

Brian2 provides:
- Equation-oriented model specification using a custom syntax that resembles mathematical notation
- Automatic code generation for multiple backends (C++, Cython, NumPy)
- Support for heterogeneous synaptic delays, multiple synapse types, and complex connectivity patterns
- Detailed documentation and active community support

## Relationship to TVB

Brian2 and TVB operate at different scales but share theoretical foundations:
- Brian2 models individual spiking neurons (microscale)
- TVB models population-level neural mass dynamics (macroscale)
- Both frameworks use mathematical models for neural dynamics
- Brian2 is used to generate spiking data that can inform TVB parameter choices
- [[pynn]] provides a common API for Brian2, NEST, and NEURON
- TVB-PyNN integration allows hybrid modeling across scales

## References

- Brian2 website: https://briansimulator.org/
- Stimberg et al. (2019) — Brian 2, an intuitive and efficient neural simulator
