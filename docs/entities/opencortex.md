---
created: 2025-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/markram-2015.md
- raw/papers/semanticscholar-eb4197c24bf2.md
tags:
- software-neural-simulator
- neural-mass-models
- spiking-neural-networks
- computational-neuroscience
- cortical-modeling
- python
- open-source
title: OpenCortex
type: entity
updated: '2026-05-04'
---

# OpenCortex

## Overview

OpenCortex is an open-source neural simulation platform written in Python that enables the construction of large-scale neocortical models combining biophysically detailed single-[[neuron]] simulations with population-level neural mass approximations. Developed to bridge the gap between highly detailed single-neuron models and simplified [[mean-field-theory|mean-field]] approaches, OpenCortex provides researchers with a flexible framework for building anatomically realistic cortical microcircuits that can scale from individual neuron simulations to whole-cortical hemispheres. The software emphasizes parameter optimization through evolutionary strategies and includes built-in support for integration with the [[jansen-rit-model]] neural mass framework, making it particularly valuable for researchers studying cortical dynamics, information processing, and network oscillations.

## Key Features

OpenCortex distinguishes itself through its hybrid architecture that allows seamless transition between point-neuron (conductance-based) simulations and neural mass descriptions within the same codebase. The software implements the popular Adaptive Exponential [[spiking-neural-networks|Integrate-and-Fire]] (AdEx) neuron model as its primary single-neuron platform, which captures key features of cortical neuron dynamics including spike-frequency adaptation, bursting behavior, and threshold facilitation. For larger-scale simulations, OpenCortex provides neural mass implementations that represent populations of neurons using the [[jansen-rit-model]] framework, allowing researchers to model mesoscale cortical dynamics while maintaining biological plausibility.

A distinctive feature of OpenCortex is its automated parameter optimization pipeline, which uses evolutionary algorithms to tune model parameters to match empirical data such as firing rates, oscillations, and [[connectivity]] statistics. The software includes connectivity generators based on anatomical data from the [[allen-brain-atlas]] and other databases, enabling the construction of data-driven cortical models. Additionally, OpenCortex provides interfaces for importing and exporting models in standard formats, and can be combined with [[the-virtual-brain]] for [[whole-brain]] simulations that incorporate cortical microcircuit detail.

## Relationship to TVB

OpenCortex and [[the-virtual-brain]] (TVB) serve complementary roles in the whole-brain modeling ecosystem. While TVB provides a comprehensive framework for connecting large-scale brain regions using neural mass models like the [[jansen-rit-model]], Epileptor, and [[wong-wang-model]], OpenCortex offers higher fidelity within-cortical microcircuit modeling that can be embedded within TVB's regional framework. Researchers can use OpenCortex to develop detailed cortical column models and then integrate these as refined node dynamics within TVB simulations, achieving a multi-scale approach that captures both macroscopic brain network dynamics and microscopic cortical processing.

The combination is particularly valuable for applications such as [[epilepsy-modeling]], where cortical microcircuit abnormalities can give rise to seizure-like dynamics observable at the whole-brain level. By using OpenCortex to parameterize TVB's regional models with biologically optimized cortical dynamics, researchers can create more physiologically grounded whole-brain models that bridge the spiking neuron and neural mass levels of description. This integration represents the broader trend in [[computational-neuroscience]] toward [[hybrid-architecture]] models that combine the strengths of different modeling scales.

## Key Papers

The primary reference for OpenCortex is a 2019 publication in *Frontiers in Neuroinformatics* that describes the software's architecture, validation, and example applications to cortical modeling. This paper demonstrates the software's ability to reproduce key features of cortical dynamics including gamma oscillations, stimulus responses, and [[resting-state]] connectivity patterns. Additional applications have appeared in studies examining cortical microcircuit alterations in [[schizophrenia-models]] and the effects of [[brain-stimulation]] on cortical dynamics.

## Related Software

OpenCortex occupies a niche in the computational neuroscience software ecosystem that bridges several existing tools. Like Brian2 and [[nest]], it provides a Python-based environment for spiking [[neural-network]] simulations, but emphasizes cortical microcircuit architecture. Unlike these general-purpose simulators, OpenCortex includes built-in neural mass implementations similar to those found in [[the-virtual-brain]]. The software complements Neuroml-based workflows for standardized model description and can be compared with other hybrid approaches like Netpyne and Auryn for large-scale neural simulations.

## Technical Implementation

The software is organized around a hierarchical modeling framework where cortical columns are composed of multiple populations (typically excitatory and inhibitory neurons), each containing many individual neurons or simplified mass representatives. Connectivity between neurons follows Dale's principle (neurons are either excitatory or inhibitory) and can be specified at multiple scales: local recurrent connections, inter-columnar connections, and external inputs. The AdEx neuron model implemented in OpenCortex captures neuronal dynamics through a small number of parameters (typically 8-10) including membrane time constant, adaptation time constant, and spike-triggered adaptation increment, making it amenable to the evolutionary optimization routines built into the platform.

The neural mass implementation follows the [[jansen-rit-model]] formalism, representing populations using mean membrane potentials and variability around these means. This approach captures the collective dynamics of neuronal populations including post-synaptic potentials and includes delay structures that give rise to realistic oscillations in the beta and gamma frequency bands. Researchers can parameterize these models to match empirical findings from [[eeg]] and [[meg]] studies, making OpenCortex useful for translational research connecting microscopic and macroscopic measurements of brain activity.

## References

1. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))
2. Markram et al. (2015). *Reconstruction and simulation of neocortical microcircuitry*. Cell. [DOI](](https://doi.org/10.1016/j.cell.2015.09.029))
3. Amirreza Movahedin, Lennart P. L. Landsmeer, Christos Strydis. (2025). *HUMA: Heterogeneous, Ultra Low-Latency Model Accelerator for The Virtual Brain on a Versal Adaptive SoC*. Symposium on Field Programmable Gate Arrays. [DOI](](https://doi.org/10.1145/3706628.3708875))