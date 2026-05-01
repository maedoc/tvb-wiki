---
title: HNN
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software, neural-mass-models, brain-oscillations, computational-neuroscience, neuroimaging-eeg, neuroimaging-meg, whole-brain-modeling]
sources: [10.7554/eLife.51214, 10.1523/JNEUROSCI.1485-06.2007, 10.1523/JNEUROSCI.1084-09.2009, 10.1073/pnas.1604135113, 10.3389/fnhum.2013.00869, 10.1093/brain/awv043]
---

# HNN

## Overview

HNN (Human Neocortical Neurosolver) is an open-source computational modeling package developed primarily by [[stephanie-jones]] and collaborators at Brown University and the MGH Martinos Center for Biomedical Imaging, with Samuel Neymotin as lead developer. The software provides a unified framework for simulating and analyzing neocortical microcircuits, bridging the gap between microscale cellular mechanisms and macroscale electromagnetic measurements captured by electroencephalography (EEG) and magnetoencephalography (MEG) [1][2]. HNN combines biophysically realistic neural mass models with data-driven optimization to enable researchers to perform inverse modeling—inferring the underlying neural dynamics that generate observed brain signals.

## Motivation and Context

The fundamental challenge in neuroimaging lies in the inverse problem: given measurements of brain activity from EEG or MEG, what underlying neural events produced those signals? Traditional approaches often treat this as a purely mathematical source localization problem, ignoring the biophysical constraints that make certain configurations more plausible than others. HNN addresses this limitation by embedding the inverse problem within a forward modeling framework built on established neuroscience—specifically, the detailed laminar structure of the neocortex and the known synaptic connections between excitatory and inhibitory neuronal populations [1][2].

The software emerged from the recognition that brain oscillations in different frequency bands (alpha, beta, gamma) arise from distinct cellular and network mechanisms, and that understanding which mechanisms generate abnormal oscillations in conditions like schizophrenia or epilepsy is essential for developing targeted therapies [1][4][6]. By providing a tool that can both generate predictions about brain dynamics and fit those predictions to empirical data, HNN enables a hypothesis-testing approach to circuit neuroscience that would otherwise require invasive electrophysiology in humans.

## Technical Description

### Canonical Neocortical Microcircuit Model

At the core of HNN lies the canonical layered neocortical circuit model developed by Jones and colleagues, which represents the six-layer structure of the neocortex with biophysically realistic populations [1][2][3]. The model includes excitatory pyramidal cells organized in layers 2/3 and 5, as well as inhibitory interneurons that mediate feedforward and feedback inhibition. Each population is modeled using a version of the Hodgkin-Huxley formalism that captures the essential dynamics of action potential generation while remaining computationally efficient [1][2].

The model simulates coordinated activity using a mean-field approach, where the collective activity is characterized by average membrane potential and firing rates. Synaptic connections between populations use biologically realistic time courses for excitatory postsynaptic potentials (mediated by AMPA receptors) and inhibitory postsynaptic potentials (mediated by GABA-A receptors) [2][3]. The model captures the excitation-inhibition balance fundamental to cortical dynamics—through proper tuning of excitatory and inhibitory synaptic conductances, the model can reproduce the full spectrum of neocortical oscillations from slow delta rhythms to fast gamma oscillations [3][4][5].

The output includes simulated local field potentials that approximate what would be measured by EEG or MEG sensors, along with the firing rates of individual populations. Critically, the model includes dendritic filtering properties that relate postsynaptic currents to the measured electromagnetic fields, enabling direct comparison with empirical recordings [1][2].

### Parameter Estimation and Data Fitting

HNN implements optimization routines that adjust model parameters to minimize the mismatch between simulated and observed brain signals [1][4]. The fitting process can target various features of the data, including power spectral density, evoked response potentials, or connectivity metrics. This makes HNN particularly valuable for clinical applications where individual patient data can be used to infer personalized brain models—a concept closely related to [[personalized-brain-modeling]].

### Forward Dipole Calculation

The software includes tools for computing forward dipole projections from the simulated laminar pyramidal cell activity, allowing researchers to compare model-generated electromagnetic fields directly with empirical EEG/MEG measurements [1][2]. This forward calculation—rather than inverse source localization—enables hypothesis testing about which cellular mechanisms generate observed macroscopic signals.

## Relationship to TVB

While both HNN and [[TVB]] (The Virtual Brain) are whole-brain modeling frameworks, they operate at different scales of neural organization. HNN focuses on detailed laminar microcircuits within individual cortical regions, treating each brain area as a multi-compartment neural mass model [3]. TVB, by contrast, typically uses simpler neural mass formulations (such as the [[jansen-rit-model]] or [[wong-wang-model]]) but connects brain regions at the macroscale using [[structural-connectivity]] matrices derived from diffusion imaging [3]. The two approaches are complementary: HNN provides mechanistic detail at the local circuit level, while TVB captures whole-brain network dynamics arising from long-range connectivity [3]. Combining these frameworks—by using HNN to parameterize local circuit dynamics within TVB's network architecture—represents an active frontier in multiscale brain modeling.

## Key Papers

The foundational description of HNN appeared in **Neymotin et al. (2020)** "Human Neocortical Neurosolver (HNN): A software platform for interpreting MEG/EEG data," published in *eLife*, which established the software architecture and demonstrated its utility for analyzing sensory-evoked responses [1]. Earlier theoretical work establishing the neocortical model foundations was published in **Jones et al. (2007)** "Neural correlates of tactile detection: A combined magnetoencephalography and biophysically based computational modeling study," in *Journal of Neuroscience* [2]. Subsequent work established the mechanistic basis of alpha and beta rhythms in **Jones et al. (2009)** "Quantitative analysis and biophysically realistic neural modeling of the MEG mu rhythm" ( *Journal of Neurophysiology*) and **Sherman et al. (2016)** "Neural mechanisms of transient neocortical beta rhythms" in *Proceedings of the National Academy of Sciences* [3][4]. Research on gamma frequency oscillations in **Lee & Jones (2013)** "Distinguishing mechanisms of gamma frequency oscillations in human current source signals" (*Frontiers in Human Neuroscience*) demonstrated the model's capability to capture fast rhythmic activity [5]. Clinical applications to autism were explored in **Khan et al. (2015)** "Somatosensory cortex functional connectivity abnormalities in autism" in *Brain* [6].

## Related Software

- [[TVB]] — whole-brain simulator using neural mass models
- [[brian2]] — spiking neural network simulator  
- [[nest]] — neural simulation tool
- [[wong-wang-model]] — competing neural mass formulation for whole-brain modeling
- [[jansen-rit-model]] — classic neural mass model for EEG generation
- [[brain-dynamics-toolbox]] — related tool for simulating brain dynamics
- [[mne-python]] — EEG/MEG data analysis suite
- [[neural-mass-models]] — broader category of models that includes HNN

## References

[1] Neymotin, S. A., Daniels, D. S., Caldwell, B., McDougal, R. A., Carnevale, N. T., Jas, M., Moore, C. I., Hines, M. L., Hämäläinen, M., & Jones, S. R. (2020). Human Neocortical Neurosolver (HNN): A software platform for interpreting the cellular and network origin of human MEG/EEG data. *eLife*, 9:e51214. https://doi.org/10.7554/eLife.51214

[2] Jones, S. R., Pritchett, D. L., Stufflebeam, S. M., Hämäläinen, M., & Moore, C. I. (2007). Neural correlates of tactile detection: A combined magnetoencephalography and biophysically based computational modeling study. *Journal of Neuroscience*, 27(2), 415-430. https://doi.org/10.1523/JNEUROSCI.1485-06.2007

[3] Jones, S. R., Pritchett, D. L., Sikora, M. A., Stufflebeam, S. M., Hämäläinen, M., & Moore, C. I. (2009). Quantitative analysis and biophysically realistic neural modeling of the MEG mu rhythm: Rhythmogenesis and modulation of sensory-evoked responses. *Journal of Neurophysiology*, 102(6), 3554-3572. https://doi.org/10.1523/JNEUROSCI.1084-09.2009

[4] Sherman, M. A., Lee, S., Law, R., Haegens, S., Moore, C. I., Hämäläinen, M. S., & Jones, S. R. (2016). Neural mechanisms of transient neocortical beta rhythms: Converging evidence from humans, computational modeling, monkeys, and mice. *Proceedings of the National Academy of Sciences*, 113(33), E4885-E4894. https://doi.org/10.1073/pnas.1604135113

[5] Lee, S., & Jones, S. R. (2013). Distinguishing mechanisms of gamma frequency oscillations in human current source signals using a computational model of a laminar neocortical network. *Frontiers in Human Neuroscience*, 7, 869. https://doi.org/10.3389/fnhum.2013.00869

[6] Khan, S., Michmizos, K., Tommerdahl, M., Ganesan, S., Kitzbichler, M. G., Zetino, M., Garel, K. L. A., Herbert, M. R., Hämäläinen, M. S., & Kenet, T. (2015). Somatosensory cortex functional connectivity abnormalities in autism show opposite trends, depending on direction and spatial scale. *Brain*, 138(5), 1394-1409. https://doi.org/10.1093/brain/awv043