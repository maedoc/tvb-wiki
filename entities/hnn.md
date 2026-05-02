---
created: 2024-01-15
sources:
- raw/papers/arxiv-2505.16861.md
- raw/papers/semanticscholar-eb704b6f5462.md
- raw/papers/sanz-leon-2013.md
tags:
- software-neuroscience
- neural-mass-models
- whole-brain-modeling
- brain-oscillations
- local-field-potentials
- excitatory-inhibitory-networks
- computational-neuroscience
- laminar-cortex
- forward-model
- eeg
- meg
title: HNN
type: entity
updated: '2026-05-02'
---

# HNN (Human Neocortical Neurosolver)

## Overview

HNN (Human Neocortical Neurosolver) is a biophysically principled modeling software platform designed to simulate neocortical neural circuits and link their activity to macroscopic electrophysiological signals such as electroencephalography (EEG) and magnetoencephalography (MEG). Developed primarily at the State University of New York (SUNY) Buffalo by the research groups of Steven Jones and colleagues, HNN provides a unique bridge between cellular-level neural dynamics and whole-cortex measurements, making it particularly valuable for interpreting evoked and spontaneous brain oscillations observed in human [[neuroimaging]] experiments. The software implements detailed laminar neocortical circuits using [[neural-mass-models]] that incorporate both excitatory (pyramidal) and inhibitory [[neuron]] populations organized by cortical layer, allowing researchers to generate predictions about current flow and field potentials that can be directly compared to empirical EEG/MEG data.

## Key Features

HNN's architecture is distinguished by its focus on **laminar neocortical circuitry**, modeling the six-layered structure of the mammalian cortex with layer-specific populations of excitatory pyramidal cells and inhibitory interneurons. Unlike simpler [[neural-mass-models]] that treat cortical regions as homogeneous units, HNN explicitly represents the vertical (columnar) and horizontal (intralaminar) connections between layers, enabling investigation of how layer-specific activity contributes to surface-recorded signals. The model incorporates biologically realistic parameters including synaptic conductances, time constants, and delay distributions, allowing users to explore how specific cellular mechanisms give rise to observed brain rhythms. The software includes a sophisticated **forward model** that computes the contribution of current dipoles from each laminar population to scalp-recorded EEG and MEG signals, enabling direct simulation-to-data comparison.

A particularly notable feature of HNN is its parameter fitting framework, which allows users to optimize model parameters to match empirical data—a capability essential for [[personalized-brain-modeling]] applications. The software can be run both through a graphical user interface for interactive exploration and via command-line scripts for batch processing and parameter sweeps. HNN has been widely applied to study the neural basis of evoked response potentials (ERPs) such as the auditory N100 and somatosensory N20, as well as spontaneous oscillations in the alpha (8–12 Hz), beta (13–30 Hz), and gamma (30–100 Hz) bands. The ability to manipulate [[excitation-inhibition-balance]] and conduct [[bifurcation-analysis]] on the model equations has made it a valuable tool for understanding the dynamical origins of brain oscillations.

## Relationship to TVB

HNN occupies a complementary niche relative to [[the-virtual-brain]] (TVB), which is a whole-brain simulation platform focused on coupling multiple regional brain models via [[structural-connectivity]] derived from diffusion imaging (DTI). While TVB excels at simulating large-scale brain networks with inter-regional coupling, HNN provides fine-grained, laminar-resolution modeling of individual cortical areas. In practice, the two platforms can be used in concert: HNN can serve as the regional model within a TVB simulation, providing biophysically realistic dynamics for each brain region rather than the simpler [[neural-mass-models]] (such as [[wong-wang-model]] or [[jansen-rit-model]]) typically employed in TVB. This hierarchical approach—using detailed local models like HNN within a macro-scale network framework—represents an important direction in [[whole-brain-modeling]] that bridges the gap between cellular neuroscience and systems-level neuroimaging.

## Key Papers

The foundational HNN methodology was described in several key publications from the Jones laboratory. The core laminar network model was first presented in work characterizing the cellular basis of neocortical oscillations, demonstrating how interactions between excitatory pyramidal cells and diverse inhibitory interneuron subtypes generate rhythmic activity across different frequency bands. Subsequent papers demonstrated HNN's utility in interpreting specific evoked responses, including studies on the auditory N100 which showed that this classic ERP arises from specific laminar currents in primary auditory cortex. More recent work has extended HNN to model auditory oddball paradigms and mismatch negativity, providing insights into how deviance detection emerges from neocortical microcircuit dynamics. The software has also been applied to study alterations in laminar dynamics in clinical populations, including work linking changes in [[excitation-inhibition-balance]] to abnormal oscillations in neuropsychiatric conditions.

## Related Software

HNN is part of a broader ecosystem of computational neuroscience tools focusing on neural mass and [[spiking-neural-networks]] approaches. For detailed biophysical simulations at the single-neuron level, users often turn to NEURON or [[brian2]], while whole-brain simulators like [[the-virtual-brain]] and TVB provide macro-scale network modeling capabilities. For laminar-specific research, HNN shares conceptual territory with the [[jansen-rit-model]] and its derivatives, though these models typically employ simpler mean-field approximations rather than explicit layer-resolved circuits. The [[neural-mass-models]] comparison page provides additional context for understanding HNN's position relative to other approaches in the field.

## Related Concepts

HNN connects to several foundational concepts in computational neuroscience. The platform embodies principles from [[mean-field-theory]], approximating the dynamics of large neuronal populations while retaining biophysical interpretability. Its study of [[brain-oscillations]] connects to the broader field of neural dynamics, linking cellular mechanisms to the rhythmic activity observed in [[eeg]] and [[meg]] recordings. The model's emphasis on laminar organization connects to the concept of [[neural-field-theory]], which describes cortical activity as a continuous medium. Parameter optimization in HNN employs techniques relevant to [[parameter-estimation]] and [[variational-bayes]], reflecting the broader challenge in computational neuroscience of fitting complex models to empirical data. Finally, HNN's focus on linking microcircuit dynamics to macroscope signals embodies the [[forward-model]]ing problem that pervades neuroimaging analysis.

## References

1. Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos. *[[arbor]]-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and [[whole-brain]] Propagation*. [Link](https://arxiv.org/abs/2505.16861)
2. Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos. (2026). *Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation*. Frontiers Comput. Neurosci.. [DOI](https://doi.org/10.3389/fncom.2025.1731161)
3. Sanz Leon et al. (2013). *[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)