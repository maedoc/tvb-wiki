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
updated: '2026-05-18'
---
# NEURON

NEURON is a simulation environment for building and simulating biophysically detailed models of individual neurons and networks of neurons using multi-compartment cable theory. Introduced by Hines and Carnevale, it provides the NMODL language for specifying arbitrary [[ion-channel]] kinetics and mechanisms, allowing researchers to construct models directly from experimental electrophysiological and anatomical data Hines & Carnevale (1997). The software employs efficient implicit numerical methods to handle the stiff differential equations that arise when complex dendritic morphologies are represented as interconnected compartments, making it computationally tractable to explore realistic neuronal geometries alongside active membrane properties Hines & Carnevale (1997). Over the decades since its release, NEURON has become one of the most widely adopted platforms in [[computational-neuroscience]], hosting thousands of published models that span diverse cell types and brain regions Hines & Carnevale (1997).

The environment offers comprehensive scripting interfaces in both hoc and Python, guiding users from simple single-compartment models to large heterogeneous networks endowed with realistic synaptic dynamics and [[plasticity]] Carnevale & Hines (2006). Carnevale and Hines's monograph has served as the definitive reference and tutorial for generations of researchers adopting NEURON, providing best-practice guidance for validating and sharing simulations Carnevale & Hines (2006). At the single-cell level, Hay and colleagues demonstrated the platform's explanatory power by developing detailed multi-compartment models of neocortical layer 5b pyramidal cells, using a genetic algorithm to optimize ion channel distributions so that the cells reproduced dendritic calcium spikes and backpropagating action potentials against independent experimental data Hay et al. (2011). These rigorously validated models established a methodological benchmark for biophysically detailed neuron construction and are now widely reused in [[spiking-neural-networks]] simulations Hay et al. (2011).

## Overview

NEURON provides tools for building and simulating biophysically detailed models of neurons and neural circuits. It uses multi-compartment cable theory and supports arbitrary [[ion-channel]] kinetics through the NMODL language.

## Key Features

- **Multi-compartment modeling**: Detailed dendritic and axonal morphology
- **NMODL language**: Specify arbitrary ion channel kinetics and mechanisms
- **Implicit numerical methods**: Efficient handling of stiff differential equations
- **hoc and Python interfaces**: Scripting for model construction and control
- **Parallel network simulation**: Large-scale network models
- **[[ModelDB]] integration**: Direct sharing and access to published models

## Applications
At the single-cell level, NEURON has served as the primary environment for constructing biophysically detailed models of individual neurons from experimental data, allowing researchers to examine how realistic dendritic architectures govern neuronal computation [[raw/papers/hines-carnevale-1997.md|Hines & Carnevale (1997)]]. Its multi-compartment cable theory framework and specialized implicit numerical methods handle the stiff differential equations that arise from complex dendritic morphologies with active [[ion-channel]] properties specified via NMODL [[raw/papers/hines-carnevale-1997.md|Hines & Carnevale (1997)]]. [[raw/papers/hay-2011.md|Hay et al. (2011)]] demonstrated the platform's explanatory power by developing detailed models of neocortical layer 5b pyramidal cells, applying a genetic algorithm to optimize ion channel densities across morphological reconstructions so that the models reproduced dendritic calcium spikes and backpropagating action potentials, with predictions validated against independent experimental recordings.

The environment also scales to network-level studies, supporting the assembly of large heterogeneous networks equipped with realistic synaptic dynamics and [[plasticity]] [[raw/papers/carnevale-hines-2006.md|Carnevale & Hines (2006)]]. The NEURON Book provides the standard tutorial progression, guiding users from simple single-compartment prototypes to complex circuits and offering best-practice guidance for validating and sharing simulations within the [[computational-neuroscience]] community [[raw/papers/carnevale-hines-2006.md|Carnevale & Hines (2006)]]. These rigorously validated single-cell models have become reusable components that are widely incorporated into [[spiking-neural-networks]] simulations spanning diverse cell types and brain regions [[raw/papers/hay-2011.md|Hay et al. (2011)]][[raw/papers/hines-carnevale-1997.md|Hines & Carnevale (1997)]].
## Key Publications

- Hines & Carnevale (1997) — NEURON simulation environment hines-carnevale-1997
- Carnevale & Hines (2006) — The NEURON Book carnevale-hines-2006
- Hay et al. (2011) — Layer 5b pyramidal cell models hay-2011
- Markram et al. (2015) — Blue Brain cortical reconstruction markram-2015

## Related Software

- [[NEST]] — Point neuron network simulator for large-scale networks
- [[TVB]] — [[neural-mass-models|Neural mass model]] [[whole-brain]] simulator
- [[model-validation]] — Model repository for sharing NEURON simulations
- Coreneuron — Optimized compute engine for large-scale NEURON simulations

## Related Concepts

- [[spiking neural networks]] — Detailed neuron dynamics
- [[neural mass model]] — Simplified population dynamics
- [[brain network]] — Network-level organization

## Key Researchers

- [[michael-schirner]] — NEURON lead developer
- Ted Carnevale — NEURON co-developer and educator

## Use Cases

- Detailed ion channel studies
- Dendritic integration and computation
- Pathological neuron modeling
- Educational neuroscience simulation
