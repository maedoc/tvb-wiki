---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
tags:
- software
- whole-brain-modeling
- neural-mass-models
- spiking-neural-networks
- brain-dynamics
title: SPICE
type: entity
updated: '2026-05-06'
---

SPICE (Simulation Package for Intelligent Cerebellar Exploration) is a specialized [[neural-simulation]] framework designed to model large-scale cerebellar circuits and their integration with cerebral cortex in whole-brain modeling contexts. While primarily developed for cerebellar microcircuit modeling, SPICE has been adapted within the broader ecosystem of [[whole-brain modeling]] tools to study the role of cerebellar-thalamo-cortical loops in brain dynamics and behavior.

## Overview

SPICE provides a computational environment for simulating detailed cerebellar neural circuits, including the distinctive granule cell layer, Purkinje cell domains, and deep cerebellar nuclei. The cerebellum contains approximately 69% of the total neurons in the human brain and plays critical roles in motor coordination, timing, prediction, and certain cognitive functions. SPICE enables researchers to build biologically realistic cerebellar microcircuit models that can be coupled to cerebral cortical models in [[whole-brain]] simulations, bridging the gap between cellular-level [[neural-mass-models]] and large-scale brain [[network-dynamics]].

The software implements detailed conductance-based [[neuron]] models and synaptic dynamics specific to cerebellar circuitry, including the unique architecture of mossy fiber inputs, parallel fiber connections, and the inhibitory interneuron networks that modulate Purkinje cell activity. SPICE's architecture allows for both detailed point-neuron simulations and reduced [[neural-mass-model]] approximations that can be integrated into larger [[brain-dynamics]] frameworks.

## Relationship to TVB

Within the [[the-virtual-brain]] (TVB) ecosystem, SPICE represents a specialized module for modeling brain regions where detailed cerebellar circuitry is of particular interest. The cerebellum's role in predictive processing and motor coordination makes it particularly relevant for understanding [[brain-stimulation]] outcomes and developing [[personalized-brain-modeling|personalized brain]] models for conditions affecting cerebellar function.

TVB's framework for [[whole-brain-modeling]] typically focuses on cerebral cortical dynamics using [[neural-mass-models]] such as the [[wong-wang-model]] or [[jansen-rit-model]], but the integration of cerebellar models like those implemented in SPICE allows for more comprehensive brain simulations that capture the cerebellum's modulatory influence on cortical dynamics. Researchers using TVB can incorporate cerebellar circuit models derived from SPICE to study how cerebellar outputs influence cerebral cortical states through thalamic pathways, enabling more complete models of [[brain-network]] dynamics.

The relationship between SPICE and TVB reflects a broader trend in [[computational-neuroscience]] where specialized models for different brain regions must be integrated into coherent [[whole-brain]] simulation frameworks. While SPICE provides detailed cerebellar circuit simulations, TVB provides the framework for coupling these regional models through [[structural-connectivity]] matrices derived from [[diffusion-imaging]] and [[tractography]] data.

## Key Features

SPICE implements several distinctive features for cerebellar modeling. The software includes detailed models of cerebellar granule cells, Golgi cells, basket cells, stellate cells, and Purkinje cells, each with appropriate [[ion-channel]] conductances and synaptic receptors. The cerebellar circuit architecture is implemented with attention to the specific [[connectivity]] patterns that give rise to the cerebellum's distinctive temporal processing capabilities.

The software supports both detailed spiking neuron simulations using [[spiking-neural-networks]] formulations and [[mean-field-theory|mean-field]] approximations suitable for large-scale brain simulations. This flexibility allows researchers to switch between biophysically detailed simulations focusing on single-neuron dynamics and reduced models suitable for investigating population-level activity across [[brain-network]] scales.

## Related Software

SPICE operates within an ecosystem of neural simulation tools that address different scales and brain regions. For detailed cerebral cortical modeling, researchers often use [[nest]] or [[brian2]], while [[the-virtual-brain]] provides the framework for integrating regional models into whole-brain simulations. The [[epileptor]] model developed for seizure modeling shares conceptual similarities with SPICE in its focus on specific brain regions and their pathological dynamics.

Related packages include [[neuroml]] for standardized model description, [[pynest]] for Python interfaces to NEST, and [[brainpy]] which provides similar flexible modeling capabilities for various brain regions. The [[whole-brain-simulators]] landscape includes both detailed simulators like SPICE and reduced models operating at the [[neural-mass-models]] level of abstraction.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation*. [Link](](https://arxiv.org/abs/2505.16861))
3. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](](https://doi.org/10.3389/fncom.2025.1731161))