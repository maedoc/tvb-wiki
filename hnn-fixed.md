---
title: HNN
created: 2025-01-15
updated: 2026-05-01
type: entity
tags: [software, neural-mass-models, spiking-neural-networks, eeg, meg, local-field-potentials, brain-oscillations, excitation-inhibition-balance, parameter-estimation]
sources: [10.7554/eLife.51214, 10.1523/JNEUROSCI.1485-06.2007, 10.1523/JNEUROSCI.1084-09.2009, 10.1073/pnas.1604135113, 10.3389/fnhum.2013.00869, 10.1093/brain/awv043]
---

# HNN

## Overview

HNN (Human Neocortical Neurosolver) is an open-source computational modeling software package designed to simulate and analyze neocortical microcircuits, with particular emphasis on interpreting electroencephalography (EEG) and magnetoencephalography (MEG) data. Developed primarily by [[stephanie-jones]] and collaborators at Brown University and the National Institute of Mental Health (NIMH), with Samuel Neymotin as lead developer, HNN provides a unified framework for building data-constrained cortical models that can be directly fitted to empirical electrophysiological recordings [1][2]. The software implements detailed biophysically-realistic neuron models based on conductance-based dynamics, allowing researchers to investigate the cellular and circuit-level mechanisms underlying macroscopic brain signals observed in non-invasive neuroimaging modalities.

## Key Features

HNN distinguishes itself from other [[neural mass models]] by its multi-scale approach, bridging the gap between single-neuron dynamics and population-level oscillations visible in [[EEG]] and [[MEG]] recordings [3]. The software employs a hybrid modeling architecture that combines compartmental neuron models with synaptic connectivity schemes derived from experimental anatomical data. Each neuron model includes multiple voltage-gated ion channels, allowing for realistic action potential generation and subthreshold dynamics that give rise to features like spike-frequency adaptation and dendritic integration.

The parameter-estimation capabilities of HNN represent one of its most powerful features. Researchers can fit model parameters—including synaptic conductances, intrinsic membrane properties, and connectivity strengths—to empirical data using optimization algorithms [4]. This enables hypothesis testing about the underlying circuit mechanisms generating observed brain rhythms. The software includes pre-configured templates for modeling specific cortical layers and cell types, as well as tools for simulating sensory evoked responses and spontaneous [[brain-oscillations]]. HNN also provides visualization utilities for comparing model output directly with empirical recordings, facilitating rapid iteration between model refinement and data comparison.

## Relationship to TVB

While [[the-virtual-brain]] (TVB) focuses on whole-brain modeling at the network level, simulating large-scale brain regions connected through [[structural connectivity]] derived from diffusion tensor imaging, HNN operates at a finer spatial scale, concentrating on cortical column or microcircuit dynamics. TVB typically employs reduced [[neural mass models]] that capture population-level activity without detailed single-neuron biophysics, whereas HNN prioritizes mechanistic realism at the cellular level [5]. The complementary nature of these tools has led some researchers to propose hierarchical modeling approaches where HNN-derived local circuit parameters inform TVB's mesoscopic population models. Both software packages share the goal of connecting computational models to empirical neuroimaging data, and both are widely used in the computational neuroscience community for studying brain dynamics.

## Technical Details

HNN implements conductance-based neuron models following the formalism pioneered by [[hodgkin-huxley-model]], extended with additional ion channels to capture the diversity of cortical cell types. The neural simulations are based on compartmental models where each compartment is described by a system of ordinary differential equations governing membrane potential dynamics:

$$C_m \frac{dV}{dt} = -g_L(V - E_L) - g_{Na}m^3h(V - E_{Na}) - g_K n^4(V - E_K) + I_{syn}$$

where $C_m$ represents membrane capacitance, $g_L$, $g_{Na}$, and $g_K$ are leak, sodium, and potassium conductances respectively, and $m$, $h$, and $n$ are voltage-dependent gating variables. Synaptic inputs are modeled as conductance changes following synaptic activation, allowing for realistic temporal integration and frequency-dependent plasticity.

The software simulates neural networks composed of excitatory and inhibitory neurons connected via biologically-realistic synaptic contacts. Network connectivity can be specified either through statistical rules or through data-driven connectivity matrices. This flexibility allows researchers to investigate how specific connectivity patterns—particularly the balance between excitation and inhibition, known as [[excitation-inhibition-balance]]—gives rise to emergent network dynamics including oscillations in different frequency bands.

## Key Papers

The foundational paper describing HNN is "Human Neocortical Neurosolver (HNN): A software platform for interpreting MEG/EEG data" by Neymotin et al. (2020), published in eLife, which established the software's architecture and demonstrated its utility for analyzing sensory-evoked responses [1]. Earlier work by Jones et al. (2007) established the theoretical foundations for the underlying neocortical model, demonstrating how conductance-based modeling could reproduce human MEG data [2]. Subsequent work established the mechanistic basis of alpha and beta rhythms (Jones et al., 2009; Sherman et al., 2016) [3][4] and gamma oscillations (Lee & Jones, 2013) [5]. The development of HNN was motivated by the need to bridge the gap between detailed [[spiking neural network]] simulations and the macroscopic signals measured by non-invasive [[neuroimaging]] modalities, a challenge shared by other [[computational neuroscience]] packages like [[brian]], [[nest]], and [[neuron]].

## Related Software

- [[the-virtual-brain]]
- [[brian]]
- [[brian2]]
- [[nest]]
- [[neuron]]
- [[pynest]]
- [[netpyne]]
- [[lfpy]]
- [[brain-dynamics-toolbox]]
- [[mne-python]]
- [[eeglab]]
- [[fieldtrip]]

## Research Applications

HNN has been applied to investigate multiple research questions in cognitive and clinical neuroscience. Studies have used HNN to model the neural basis of [[brain-oscillations]] across different frequency bands, from slow oscillations to gamma rhythms, demonstrating how specific combinations of synaptic and intrinsic properties give rise to different oscillation patterns [3][4][5]. The software has also been employed in clinical research contexts, including investigations of [[epilepsy modeling]] where abnormal [[excitation-inhibition-balance]] leads to pathological synchrony and seizure dynamics. Additionally, HNN has been applied to study circuit deficits in autism spectrum disorder, demonstrating how alterations in intracortical connectivity can manifest in atypical MEG signatures [6]. HNN also serves as an educational tool for training graduate students in [[computational neuroscience]], providing a platform for learning about [[dynamical-systems-theory]] concepts through hands-on simulation exercises.

## References

[1] Neymotin, S. A., Daniels, D. S., Caldwell, B., McDougal, R. A., Carnevale, N. T., Jas, M., Moore, C. I., Hines, M. L., Hämäläinen, M., & Jones, S. R. (2020). Human Neocortical Neurosolver (HNN), a new software tool for interpreting the cellular and network origin of human MEG/EEG data. *eLife*, 9:e51214. https://doi.org/10.7554/eLife.51214

[2] Jones, S. R., Pritchett, D. L., Stufflebeam, S. M., Hämäläinen, M., & Moore, C. I. (2007). Neural correlates of tactile detection: A combined magnetoencephalography and biophysically based computational modeling study. *Journal of Neuroscience*, 27(2), 415-430. https://doi.org/10.1523/JNEUROSCI.1485-06.2007

[3] Jones, S. R., Pritchett, D. L., Sikora, M. A., Stufflebeam, S. M., Hämäläinen, M., & Moore, C. I. (2009). Quantitative analysis and biophysically realistic neural modeling of the MEG mu rhythm: Rhythmogenesis and modulation of sensory-evoked responses. *Journal of Neurophysiology*, 102(6), 3554-3572. https://doi.org/10.1523/JNEUROSCI.1084-09.2009

[4] Sherman, M. A., Lee, S., Law, R., Haegens, S., Moore, C. I., Hämäläinen, M. S., & Jones, S. R. (2016). Neural mechanisms of transient neocortical beta rhythms: Converging evidence from humans, computational modeling, monkeys, and mice. *Proceedings of the National Academy of Sciences*, 113(33), E4885-E4894. https://doi.org/10.1073/pnas.1604135113

[5] Lee, S., & Jones, S. R. (2013). Distinguishing mechanisms of gamma frequency oscillations in human current source signals using a computational model of a laminar neocortical network. *Frontiers in Human Neuroscience*, 7, 869. https://doi.org/10.3389/fnhum.2013.00869

[6] Khan, S., Michmizos, K., Tommerdahl, M., Ganesan, S., Kitzbichler, M. G., Zetino, M., Garel, K. L. A., Herbert, M. R., Hämäläinen, M. S., & Kenet, T. (2015). Somatosensory cortex functional connectivity abnormalities in autism show opposite trends, depending on direction and spatial scale. *Brain*, 138(5), 1394-1409. https://doi.org/10.1093/brain/awv043