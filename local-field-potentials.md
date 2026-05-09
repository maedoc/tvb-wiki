---
title: Local Field Potentials
created: 2025-01-15
updated: 2026-05-09
type: concept
tags: [electrophysiology, neuroimaging-eeg, neuroimaging-meg, neural-mass-models, neural-field-theory, brain-oscillations, functional-connectivity, forward-model, parameter-estimation]
sources: [raw/papers/arxiv-2512.07842.md, raw/papers/arxiv-2510.22022.md, raw/papers/arxiv-2603.07524.md]
---

Local Field Potentials (LFPs) represent extracellular voltage fluctuations measured at the scale of millimeters within cortical tissue, reflecting the summed synaptic activity of local neuronal populations rather than individual action potentials. Unlike single-unit recordings that capture the firing of specific neurons, LFPs provide a mesoscopic signal that integrates postsynaptic potentials across thousands of neurons in the vicinity of the recording electrode, making them particularly suitable for studying population-level dynamics in both experimental and computational neuroscience contexts.

## Motivation and Context

The study of cortical dynamics during different behavioral states—such as decision making, sleep, and movement—requires understanding the neural rhythms that emerge from coordinated population activity. LFPs serve as a crucial bridge between microscopic single-neuron activity and macroscopic neuroimaging signals such as [[fmri]] and [[eeg]], offering millisecond temporal resolution while retaining spatial specificity that [[meg]] and EEG often lose due to volume conduction effects. In the context of [[whole-brain modeling]], LFPs provide validation data for [[neural-mass-models]] and [[neural-field-theory]] approaches, enabling researchers to compare simulated population dynamics against empirical recordings from intracranial electrodes or microelectrode arrays.

The capability to accurately model and estimate LFPs has become increasingly important for [[personalized-brain-modeling]] applications, where patient-specific parameters derived from electrophysiological recordings can inform clinical interventions for conditions ranging from [[epilepsy-modeling]] to [[brain-stimulation]] therapies. Recent work by Avitabile, Lord, and Meddouni (2025) demonstrates how [[parameter-estimation]] techniques combined with data assimilation can reconstruct both the hidden neural states and model parameters that generate observed LFP signals, enabling characterization of cortical dynamics during natural sleep in mouse models.

## Theoretical Framework

LFPs are commonly modeled using [[neural-mass-models]] such as the [[jansen-rit-model]] or [[wilson-cowan-model]], which describe the collective activity of excitatory and inhibitory neural populations through coupled differential equations. In the Wilson-Cowan formalism, the activity of a neural population at position $\mathbf{x}$ and time $t$ evolves according to:

$$\frac{\partial u(\mathbf{x}, t)}{\partial t} = -u(\mathbf{x}, t) + \int_{\Omega} w(\mathbf{x} - \mathbf{y}) S(u(\mathbf{y}, t)) d\mathbf{y} + I(\mathbf{x}, t)$$

where $S(u) = 1/(1 + e^{-u})$ is the sigmoid activation function, $w(\mathbf{x} - \mathbf{y})$ represents the synaptic connectivity kernel describing interactions between populations at different spatial positions, and $I(\mathbf{x}, t)$ denotes external inputs (Tamekue & Ching, 2025). The integral term captures the spatial convolution that gives rise to wave-like propagation and pattern formation in cortical tissue.

For modeling LFPs specifically, the relation between the population activity variable $u$ and the measured extracellular potential involves a [[forward-model]] that accounts for volume conduction effects—the passive spread of current through the extracellular medium (Buzsáki et al., 2012). This forward problem is inherently ill-posed because the same LFP measurement could theoretically arise from multiple spatial configurations of neural activity, necessitating regularization approaches or Bayesian inference frameworks for meaningful inversion (Jiang et al., 2026).

## Relationship to Other Electrophysiological Signals

LFPs occupy an intermediate position in the hierarchy of neurophysiological signals, carrying information that complements both spiking activity and macroscopic neuroimaging. While single-unit recordings provide precise timing information about individual neuron firing, LFPs capture synchronized synaptic events that reflect [[functional-connectivity]] patterns at the local circuit level. The relationship between LFP and spiking activity is bidirectional: LFPs can both predict spike timing through phase-precession relationships and be modulated by feedback from actively firing neurons (Buzsáki et al., 2012).

In the context of [[dynamic-causal-modeling]], LFPs serve as empirical data for estimating effective connectivity—the directed causal influences between brain regions—using variants of the [[jansen-rit-model]] or more abstract neural mass formulations. The spectral content of LFPs, particularly brain oscillations in the delta (1–4 Hz), theta (4–8 Hz), alpha (8–12 Hz), beta (12–30 Hz), and gamma (30–100 Hz) bands, provides a fingerprint of the underlying network states and can reveal pathological dynamics such as those observed in [[epileptor-rs]] models of seizure-like activity (Jirsa et al., 2014).

## Parameter Estimation and Data Assimilation

A key challenge in using LFPs for [[whole-brain modeling]] lies in estimating both the hidden neural states and the parameters of the governing equations from noisy measurements. Bayesian [[parameter-estimation]] approaches, combined with data assimilation techniques, offer a principled framework for this inverse problem. The method demonstrated by Avitabile et al. (2025) employs a discretized Wilson-Cowan model and performs joint estimation of state variables and parameters—including connectivity kernel width and synaptic time constants—using synthetic measurements before applying to real cortical LFP data from sleep experiments.

Control-theoretic approaches to neural field equations, such as those developed by Tamekue and Ching (2025), provide additional tools for understanding how external inputs shape LFP dynamics. Their framework for synthesizing piecewise-constant inputs to achieve prescribed target states in Amari-type neural fields has implications for understanding paradoxical neural representations and developing closed-loop stimulation protocols that manipulate population dynamics in precisely controlled ways.

## Open Questions and Future Directions

Despite significant progress, several open questions remain in LFP research. The relationship between LFPs measured at different spatial scales—from single-electrode recordings to large-scale arrays—requires further theoretical characterization. Additionally, the integration of LFP-based parameter estimation with [[structural-connectivity]] estimates derived from [[diffusion-imaging]] remains technically challenging due to the different spatial scales and temporal resolutions of these modalities.

Future directions include the development of more biophysically realistic forward models that account for the detailed morphology of neuronal dendrites, improved regularization techniques for solving the inverse problem, and hybrid approaches that combine LFPs with [[fmri]] signals through [[bold-model]] frameworks for integrated analysis of brain dynamics across spatiotemporal scales.

