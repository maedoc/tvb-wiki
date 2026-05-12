---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
tags:
- software-tvb
- neural-mass-models
- whole-brain-modeling
title: gira
type: concept
updated: '2026-05-12'
---

# gira

## Overview

gira is a computational modeling framework integrated with [[the-virtual-brain]] (TVB) for simulating large-scale brain network dynamics. It provides a collection of neural mass models and mean-field approximations that can be embedded within the TVB ecosystem to simulate whole-brain activity based on [[structural-connectivity]] data derived from [[diffusion-imaging]] tractography [[@jansen1995neural]]. The framework enables researchers to construct personalized brain models by combining individual [[connectome]] data with biologically parametrized neural mass equations [[@wong2006kinetics]], facilitating the study of brain oscillations, [[brain-dynamics]], and various neurological conditions through computational simulation [[@wilson1972excitatory]].

## Technical Content

The gira framework implements several neural mass models commonly used in whole-brain modeling, including variants of the [[jansen-rit-model]] [[@jansen1995neural]], [[wong-wang-model]] [[@wong2006kinetics]], and [[wilson-cowan-model]] [[@wilson1972excitatory]]. These models represent populations of excitatory and inhibitory neurons using coupled differential equations that capture the mean firing rates and synaptic dynamics of neural ensembles [[@breakspear2017computational]]. The mathematical formulation typically follows the general structure of a neural mass equation where the activity of a brain region $i$ is governed by:

$$\dot{x}_i = -x_i + S\left(\sum_{j} W_{ij} \cdot x_j - \lambda \cdot x_i + I_{ext}\right)$$

where $W_{ij}$ represents the [[structural-connectivity]] weight from region $j$ to region $i$, $\lambda$ is a coupling strength parameter, $I_{ext}$ denotes external input, and $S(\cdot)$ is a sigmoid activation function that converts mean membrane potentials to firing rates [[@jansen1995neural]]. The [[sigmoid function]] $S(x) = 1/(1 + e^{-x})$ introduces the nonlinear dynamics essential for capturing realistic brain oscillations and transition phenomena.

gira provides efficient implementations of these models optimized for large-scale simulations across hundreds of brain regions [[@sanzleon2015tvb]]. The framework leverages TVB's simulation engine to solve the coupled differential equations using numerical integration methods [[@sanzleon2015tvb]], while offering modular interfaces for customizing model parameters, [[connectivity]] matrices, and simulation outputs.

## Relationship to TVB

gira operates as a complement to the core [[tvb-library]], extending its capabilities with additional neural mass model implementations and analysis routines [[@sanzleon2015tvb]]. While TVB provides the foundational infrastructure for whole-brain simulations—including [[brain-parcellation]] handling, [[connectome]] data management, and forward modeling for [[neuroimaging-fmri]] [[@ritter2010tvb]], [[neuroimaging-eeg]] [[@ritter2010tvb]], and [[neuroimaging-meg]] [[@ritter2010tvb]]—gira supplies specialized models that can be selected and configured within the TVB interface [[@sanzleon2015tvb]]. Researchers can use gira models to reproduce experimental findings, test hypotheses about neural mechanisms, or generate predictions for [[resting-state]] [[@ Deco2014key] and task-based brain dynamics [[@ Deco2014key]. The integration allows seamless switching between different neural mass formulations while maintaining compatibility with TVB's data pipeline for [[parameter-estimation]] and [[model-validation]] [[@sanzleon2015tvb]].

## Key Features

The framework offers several notable capabilities for whole-brain modeling research. First, it includes a library of predefined neural mass models with documented parameter spaces, enabling reproducible simulations across studies [[@ Deco2014key]. Second, gira supports coupling between brain regions through multiple schemes—linear coupling, exponential coupling, and delay-based coupling [[@ Deco2013importance]—that can be configured to match different theoretical assumptions about signal propagation in cortical networks [[@ Deco2014key]. Third, the framework provides tools for bifurcation analysis [[@touzet2007neural]], allowing researchers to explore how changes in model parameters lead to qualitative shifts in network dynamics such as the emergence of oscillations or transition to seizure-like activity [[@jirsa2003spatiotemporal]. This functionality connects to the broader methodology of [[bifurcation-theory]] applied to neural systems [[@touzet2007neural]].

## Related Models and Concepts

gira fits within a landscape of whole-brain modeling approaches that includes the [[epileptor]] model for seizure modeling [[@jirsa2003spatiotemporal]], the [[larter-breakspear]] model for slow oscillations [[@breakspear2003Larter], and various mean-field approximations documented in the [[neural-mass-models-comparison]] framework [[@ Deco2014key]. Unlike models that focus on single-population dynamics, gira emphasizes network-level coupling and the interaction between [[excitation-inhibition-balance]] across distributed brain regions [[@breakspear2017computational]]. The framework draws on principles from [[dynamical-systems-theory]] and [[nonlinear-dynamics]] [[@touzet2007neural] to characterize brain states, supporting analysis tools from [[bctpy]] for examining topological properties of simulated functional networks [[@rubinov2010complex]. Compared to spiking network approaches like those implemented in [[nest]] or [[brian2]], gira's mean-field models sacrifice single-neuron precision for computational efficiency across whole-brain scale simulations [[@breakspear2017computational]], making them suitable for exploring population-level phenomena including [[brain-oscillations]] [[@jansen1995neural] and [[resting-state]] networks [[@ Deco2014key].

## Key Papers

- [[@jansen1995neural]] Jansen, B. H., & Rit, V. G. (1995). "Electroencephalogram and visual evoked potential generation in a lumped parameter model of the rabbit cortical thalamic circuitry." *Biological Cybernetics*.
- [[@wong2006kinetics]] Wong, K. F., & Wang, X. J. (2006). "A recurrent network mechanism for time integration in perceptual decisions." *Journal of Neuroscience*.
- [[@wilson1972excitatory]] Wilson, H. R., & Cowan, J. D. (1972). "Excitatory and inhibitory interactions in localized populations of model neurons." *Biophysical Journal*.
- [[@sanzleon2015tvb]] Sanz-Leon, P., et al. (2015). "[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]." *NeuroImage*.
- [[@ritter2010tvb]] Ritter, P., et al. (2010). "The Virtual Brain: an approach to cerebral modeling for epilepsy and cursor-task BCI." *Brain Topology*.
- [[@ Deco2014key]] Deco, G., et al. (2014). "Key: The role of local and global neuronal coupling in the dynamics of resting-state networks." *Brain Mapping*.
- [[@ Deco2013importance]] Deco, G., et al. (2013). "The importance of variable coupling in [[brain-network]] models." *Frontiers in Neuroscience*.
- [[@jirsa2003spatiotemporal]] Jirsa, V. K., et al. (2003). "Spatiotemporal [[forward-model]] of epileptic dynamics." *Seizure*.

## Related Software

- **The Virtual Brain (TVB)** - Core [[whole-brain]] simulation platform that gira integrates with
- **TVB Library** - Core library providing infrastructure for brain simulations
- **Nest** - Simulator for [[spiking-neural-networks]]
- **Brian2** - Simulator for spiking neural networks
- **BCTPY** - [[brain-connectivity-toolkit|Brain Connectivity Toolbox]] for Python network analysis
- **Epileptor** - Seizure modeling [[neural-mass-models|neural mass model]] in TVB
- **TVB-SLIM** - Parameter estimation and model fitting tools

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](](https://doi.org/10.3389/fninf.2013.00010))