---
title: HNN (Human Neocortical Neurosolver)
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software-brain-modeling, neuroimaging-eeg, neuroimaging-meg, neural-mass-models, spiking-neural-networks, brain-oscillations, brain-stimulation, computational-neuroscience]
sources: []
---

# HNN (Human Neocortical Neurosolver)

## Overview

The Human Neocortical Neurosolver (HNN) is an open-source neural modeling software package designed to help researchers and clinicians interpret human electroencephalography (EEG) and magnetoencephalography (MEG) data at the cellular and circuit level. Developed primarily by Stephanie Jones and colleagues at Brown University, HNN bridges the gap between non-invasive human brain recordings and the detailed biophysical mechanisms that generate them. The software provides a biophysically detailed template model of a neocortical cortical column that simulates primary current dipoles—the neural sources of sensor-level EEG/MEG signals—enabling users to formulate and test mechanistic hypotheses about how specific cell types and synaptic connections give rise to observed brain dynamics.

Unlike [[whole-brain-modeling]] approaches such as [[the-virtual-brain]] that typically operate at the [[neural-mass-models]] level of abstraction, HNN simulates detailed single-neuron dynamics using compartment models built on the [[neuron]] simulator. This allows researchers to examine how specific cellular mechanisms—including dendritic currents, synaptic conductances, and gap junction coupling—contribute to macroscopic signals measured at the scalp.

## Key Features

HNN's core innovation lies in its multi-scale simulation capability, which spans from individual neuronal compartments to population-level current dipoles that can be directly compared to source-localized experimental data. The software's template model, originally published in Jones et al. (2007), contains the minimal circuit elements necessary for generating primary current dipoles, including pyramidal neurons in infragranular and supragranular layers, various interneuron subtypes, and layer-specific synaptic connectivity patterns.

The software provides two primary interfaces: a graphical user interface (GUI) designed for researchers without computational modeling experience, and a Python API (hnn-core) allowing scripted simulations and integration with other neuroscience tools. Users can define layer-specific driving inputs through proximal (lemniscal thalamic) and distal (cortico-cortical or non-lemniscal) pathways, enabling hypothesis testing about the origin of specific signal features.

HNN supports several optimization approaches for fitting model parameters to empirical data, including manual parameter tuning and automated optimization using Bayesian methods or COBYLA (Constrained Optimization BY Linear Approximation). The software can simultaneously output multiple modalities: current dipoles for direct comparison with MEG/EEG source estimates, local field potentials (LFP), current-source density (CSD), and single-cell spiking activity. This multi-scale output enables validation of model predictions across different recording scales.

The software includes pre-configured templates for simulating some of the most commonly recorded EEG/MEG signals, including event-related potentials (ERPs) such as the somatosensory N20, and low-frequency rhythms including alpha (7–14 Hz), beta (15–29 Hz), and gamma (30–80 Hz) oscillations.

## Relationship to TVB

HNN and [[the-virtual-brain]] (TVB) share the common goal of connecting brain modeling to empirical neuroimaging data, but they operate at different levels of abstraction and serve complementary research purposes. While HNN focuses on detailed biophysical modeling of cortical microcircuits at the single-neuron and column level, TVB typically operates at the [[neural-mass-models]] level, simulating large-scale brain networks composed of interconnected brain regions.

TVB's strength lies in its ability to model [[whole-brain]] dynamics by coupling multiple brain regions via [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI), making it particularly suitable for studying resting-state networks, [[brain-stimulation]] effects at the network level, and clinical applications such as [[epilepsy-modeling]]. HNN, by contrast, provides mechanistic insight into the cellular and circuit-level generators of specific EEG/MEG features within a single cortical column, making it ideal for understanding the neural basis of event-related potentials and brain oscillations.

There is potential for complementary use cases: TVB could provide the macroscopic [[functional-connectivity]] constraints that inform which cortical regions to model in detail with HNN, while HNN could provide the biophysical parameters that inform mesoscopic dynamics in TVB's [[brain-dynamics]] simulations. Both tools can be used in conjunction with other software in the computational neuroscience ecosystem, including [[brian]], [[nest]], and [[neuroml]]-compatible simulators.

## Key Papers

The foundational HNN template model was published in Jones et al. (2007), which demonstrated that a canonical neocortical circuit containing minimal circuit elements could reproduce primary current dipoles matching human MEG data. Subsequent work established the mechanistic basis of alpha and beta rhythms (Jones et al., 2009; Sherman et al., 2016) and gamma oscillations (Lee & Jones, 2013). The software itself was released in Neymotin et al. (2020), published in eLife, and the current hnn-core Python package was described in Jas et al. (2023), published in the Journal of Open Source Software.

## Related Software

- [[neuron]] — Underlying simulator engine for HNN's detailed single-neuron models
- [[the-virtual-brain]] — Whole-brain modeling at the neural mass level
- [[brian]] — Another Python-based spiking neural network simulator
- [[nest]] — Neural simulation tool for large-scale spiking networks
- [[eeglab]] — EEG/MEG data preprocessing and analysis
- [[fieldtrip]] — MATLAB toolbox for MEG/EEG analysis
- [[mne-python]] — Python toolbox for neurophysiology data analysis