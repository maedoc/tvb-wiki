---
created: 2026-04-20
sources:
- raw/papers/hines-carnevale-1997.md
- raw/papers/carnevale-hines-2006.md
- raw/papers/hay-2011.md
- raw/papers/markram-2015.md
- raw/papers/gewaltig-diesmann-2007.md
tags:
- software-neuron
- spiking-neural-networks
- neural-mass-models
title: NEURON
type: entity
updated: '2026-04-23'
---

# NEURON

NEURON is a simulation environment for modeling individual neurons and networks of neurons using multi-compartment cable theory.

## Overview

NEURON provides tools for building and simulating biophysically detailed models of neurons and neural circuits. It uses multi-compartment cable theory and supports arbitrary ion channel kinetics through the NMODL language.

## Key Features

- **Multi-compartment modeling**: Detailed dendritic and axonal morphology
- **NMODL language**: Specify arbitrary ion channel kinetics and mechanisms
- **Implicit numerical methods**: Efficient handling of stiff differential equations
- **hoc and Python interfaces**: Scripting for model construction and control
- **Parallel network simulation**: Large-scale network models
- **ModelDB integration**: Direct sharing and access to published models

## Applications

- Single neuron biophysical modeling
- Complex dendritic computation studies
- Network simulations with realistic cell types
- Educational and research tutorials (The NEURON Book)

## Key Publications

- Hines & Carnevale (1997) — NEURON simulation environment hines-carnevale-1997
- Carnevale & Hines (2006) — The NEURON Book carnevale-hines-2006
- Hay et al. (2011) — Layer 5b pyramidal cell models hay-2011
- Markram et al. (2015) — Blue Brain cortical reconstruction markram-2015

## Related Software

- [[NEST]] — Point neuron network simulator for large-scale networks
- [[TVB]] — Neural mass model whole-brain simulator
- [[ModelDB]] — Model repository for sharing NEURON simulations

## Related Concepts

- [[spiking neural networks]] — Detailed neuron dynamics
- [[neural mass model]] — Simplified population dynamics
- [[brain network]] — Network-level organization

## Key Researchers

- [[Michael Hines]] — NEURON lead developer
- [[Ted Carnevale]] — NEURON co-developer and educator

## Use Cases

- Detailed ion channel studies
- Dendritic integration and computation
- Pathological neuron modeling
- Educational neuroscience simulation