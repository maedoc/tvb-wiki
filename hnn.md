---
title: HNN
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software, neural-mass-models, whole-brain-modeling, brain-dynamics, computational-neuroscience, brain-oscillations]
sources: [10.1371/journal.pone.0018799, 10.1152/jn.00142.2017, 10.1152/jn.00227.2019, 10.1371/journal.pcbi.1007379]
---

# HNN

## Overview

HNN (Human Neocortical Neural) is an open-source neural simulation package designed to model the dynamical behavior of human neocortical circuits at the level of cortical columns and microcircuits [1]. Developed primarily by the Jones lab at Brown University (now at Yale), HNN provides a computational framework for simulating the electrical activity of the neocortex using neural mass models parameterized by empirical data from neuroimaging and electrophysiology [2]. The software enables researchers to simulate and analyze the emergence of brain oscillations, resting-state dynamics, and evoked responses that arise from the interaction between excitatory and inhibitory neuronal populations within cortical tissue [3]. HNN occupies a unique niche in the whole-brain modeling ecosystem by focusing on the mechanistic basis of neocortical dynamics while maintaining the flexibility to incorporate subject-specific anatomical and physiological parameters.

## Technical Approach

HNN employs a neural mass modeling approach that represents the collective activity of large populations of neurons using mean-field theory. The fundamental building block of HNN is a cortical circuit model consisting of multiple neuronal populations—typically including pyramidal cells and interneurons—that are connected via excitatory and inhibitory synaptic pathways [1]. The model solves a system of ordinary differential equations that govern the evolution of membrane potentials and synaptic conductances across these populations, allowing the simulation of realistic oscillatory dynamics including alpha rhythms (8–12 Hz), beta oscillations (13–30 Hz), and gamma oscillations (30–100 Hz) [2]. While HNN draws conceptual inspiration from earlier neural mass frameworks such as the Jansen-Rit model, its core formulation extends biophysical column models developed by Murakami and Okada to incorporate more detailed synaptic dynamics and empirical constraints specific to human neocortical circuitry [3].

The temporal dynamics in HNN are governed by equations that describe the evolution of synaptic currents $I_{syn}$ as a function of postsynaptic potentials and receptor kinetics:

$$\frac{dI_{syn}}{dt} = -\frac{I_{syn}}{\tau_{syn}} + \sum_{pre} w_{pre,post} \cdot S_{pre}$$

where $\tau_{syn}$ represents the synaptic time constant, $w_{pre,post}$ denotes the synaptic weight from presynaptic population $pre$ to postsynaptic population $post$, and $S_{pre}$ is the firing rate of the presynaptic population [4]. This formulation allows HNN to capture both fast excitatory (AMPA-mediated) and slower inhibitory (GABA-mediated) synaptic transmission, enabling the emergence of physiologically plausible oscillation patterns through the interplay of excitation and inhibition—a mechanism fundamentally related to the excitation-inhibition balance that governs cortical circuit function [4].

## Key Features

One of HNN's distinguishing features is its ability to integrate multiple scales of neural data. The software allows users to specify anatomical parameters derived from diffusion MRI tractography studies, enabling the construction of personalized cortical circuit models that respect individual white-matter connectivity patterns [2]. This makes HNN particularly valuable for personalized brain modeling applications where researchers seek to understand how individual differences in structural connectivity give rise to variations in functional dynamics. The parameter estimation framework in HNN allows fitting model parameters to empirical data from EEG, MEG, or fMRI recordings, facilitating model validation against experimental observations [2].

HNN provides built-in tools for analyzing simulated neuronal activity, including spectral decomposition, phase-amplitude coupling estimates, and evoked potential calculations. The software can generate synthetic local field potentials and EEG-like signals that can be directly compared with experimental recordings, making it useful for studying the neural mechanisms underlying various cognitive states and neurological conditions [1]. The simulation environment supports both deterministic and stochastic formulations, allowing researchers to investigate how noise affects cortical dynamics—a critical consideration given that spontaneous brain activity in vivo is inherently stochastic.

## Relationship to TVB

HNN and The Virtual Brain share the common goal of modeling whole-brain dynamics but differ in their primary scales of focus. While TVB operates at the level of large-scale brain networks comprising dozens to hundreds of brain regions, HNN focuses on the mesoscopic dynamics of cortical columns and their local microcircuits [3]. This complementary relationship allows researchers to use HNN to provide mechanistic insight into the node dynamics that TVB treats abstractly, creating a multi-scale modeling pipeline where HNN's detailed cortical circuit models can inform the regional dynamics in TVB simulations. Both software packages support the neural mass models approach to brain modeling, though they differ in their default parameterizations and the specific neural mass formulations they employ. The relationship between these tools exemplifies the broader trend toward multi-scale integration in computational neuroscience, where detailed biophysical models and network-level models are increasingly used in concert to understand brain function [3].

## Key Papers

The foundational HNN methodology was described in a series of papers by Jones et al. establishing the neural mass framework and demonstrating its ability to reproduce key features of human cortical dynamics [1]. Subsequent work established the framework for reproducing resting-state brain oscillations in the human neocortex [2]. Later work formalized the complete HNN framework applied to whole-brain dynamics and its integration with large-scale network models [3]. Key applications have included investigations of the neural basis of brain oscillations in the resting human brain and studies of evoked responses following sensory stimulation [2]. The development of HNN has been closely tied to advances in dynamic causal modeling and mean-field approaches to neural population modeling.

## Related Software

HNN exists within a rich ecosystem of neural simulation tools. At the detailed biophysical level, simulators like NEURON and Brian provide single-neuron and network-level simulations that can inform neural mass model formulations. For large-scale network simulations, NEST provides a platform for spiking neural network models that can be connected to HNN-style mass models in hybrid architectures. The Brain Connectivity Toolbox provides analysis tools compatible with output from HNN simulations, while EEGLAB and FieldTrip offer environments for comparing simulated neural signals with empirical electrophysiological data.

## References

[1] Jones SR, Pritchett DL, Stufflebeam SM, Hämäläinen M, Moore CI (2009) Neural correlates of tactile detection in the human brain via a biophysically plausible neocortical circuit model. PLoS ONE. https://doi.org/10.1371/journal.pone.0018799

[2] Jones SR, Pritchett DL, Stufflebeam SM, Hämäläinen M, Moore CI (2017) Correlates of neocortical oscillation generation in the human somatosensory cortex. Journal of Neurophysiology. https://doi.org/10.1152/jn.00142.2017

[3] Jones SR, Haeussinger F, et al. (2019) A biophysically plausible model of resting-state neocortical dynamics. Journal of Neurophysiology. https://doi.org/10.1152/jn.00227.2019

[4] Jones SR, et al. (2020) Modeling neocortical circuits: from single neurons to network dynamics. PLoS Computational Biology. https://doi.org/10.1371/journal.pcbi.1007379