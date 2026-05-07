---
title: "Anticevic 2012"
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [schizophrenia-models, neural-mass-models, excitation-inhibition-balance, computational-psychiatry, whole-brain-modeling, brain-oscillations, brain-dynamics, structural-connectivity, functional-connectivity, personalized-brain-modeling]
sources: [raw/papers/anticevic-2012.md]
---

Anticevic et al. (2012) introduced a computational framework that integrated biophysically realistic [[neural-mass-models]] with empirically derived [[structural-connectivity]] data from [[diffusion-imaging]] to study [[whole-brain-modeling|whole-brain dynamics]] in [[schizophrenia-models]]. This landmark paper demonstrated how combined deficits in glutamatergic (NMDA receptor-mediated) signaling and GABAergic inhibition produce dysfunction spanning multiple scales—from local neural population [[brain-oscillations]] to large-scale [[functional-connectivity]] patterns observable in [[resting-state-fmri]]. The work established a bridge between cellular-level neurotransmitter abnormalities and macroscopic network-level disturbances, providing a foundational framework for [[personalized-brain-modeling]] in psychiatric research.

## Background and Motivation

Schizophrenia is characterized by disturbances in perception, cognition, and reality testing that affect approximately 1% of the global population. Prior to this work, researchers had established that schizophrenia involves both glutamatergic dysfunction (evidenced by the psychotomimetic effects of ketamine, an NMDA receptor antagonist) and GABAergic deficits (evidenced by reduced parvalbumin-positive interneurons and impaired gamma-band oscillations). However, the mechanistic link between these cellular-level abnormalities and the large-scale brain network disruptions observed in neuroimaging studies remained poorly understood.

Empirical resting-state fMRI studies had demonstrated that schizophrenia patients exhibit altered [[functional-connectivity]] patterns, including reduced anticorrelation between the [[default-mode-network]] and task-positive systems, but the underlying synaptic mechanisms generating these network-level changes were unknown. Addressing this gap required a computational framework capable of bridging scales from neurotransmitter function to whole-brain dynamics.

## Technical Framework

The computational model combines a neural mass formulation—specifically a variant of the [[wong-wang-model]] or related excitatory-inhibitory population model—with anatomically realistic white matter tracts derived from diffusion imaging and [[tractography]]. The neural mass equations capture the dynamic interaction between excitatory (glutamatergic) pyramidal cells and inhibitory interneurons, where NMDA receptor dysfunction is modeled as reduced excitatory drive while GABAergic deficits manifest as reduced [[excitation-inhibition-balance]].

The model employs coupled differential equations describing neural population dynamics. The excitatory population evolves according to:

$$\frac{dE}{dt} = -\frac{E}{\tau_E} + (1-E)S(E,V) - W_{EE} \cdot E + W_{IE} \cdot I$$

Similarly, the inhibitory population follows:

$$\frac{dI}{dt} = -\frac{I}{\tau_I} + S(E,V) - W_{II} \cdot I + W_{EI} \cdot E$$

In these equations, E and I represent the average firing rates of excitatory and inhibitory populations respectively, τ_E and τ_I are the respective time constants determining neural response dynamics, and S(E,V) represents a sigmoid input-output function that converts mean neural activity into activation levels. The coupling weights W_{XY} encode the strength of connections from population Y to population X, capturing the interactions between excitatory and inhibitory neuronal populations.

By varying the NMDA-mediated excitation strength and GABAergic inhibition strength, the authors explored how different combinations of neurotransmitter dysfunction affect: (1) local gamma-band oscillations (30-100 Hz)—a core deficit in schizophrenia; (2) regional mean activity levels across cortical and subcortical regions; and (3) large-scale [[functional-connectivity]] patterns observable in resting-state fMRI. The key insight was that moderate combined deficits—rather than extreme loss in either system—produced the most schizophrenia-like pattern of results, a prediction later validated against empirical data.

## Key Findings

The computational framework produced several important predictions. First, combined moderate deficits in NMDA-mediated excitation and GABAergic inhibition reproduced the pattern of reduced gamma-band oscillations consistently observed in schizophrenia patients. Second, the model predicted that these local deficits would propagate through the [[structural-connectivity]] backbone to produce altered [[functional-connectivity]] patterns at the network level, including reduced interhemispheric synchronization and disrupted modular organization. Third, the framework demonstrated that different combinations of neurotransmitter deficits produced distinct phenotypic patterns, providing a mechanistic basis for the heterogeneity observed clinically.

The work established what has become a foundational principle in [[computational-psychiatry]]: that psychiatric disorders like schizophrenia involve dysregulation of [[excitation-inhibition-balance]] that can be understood through the lens of [[dynamical-systems-theory]]. The model showed that the brain's intrinsic [[brain-dynamics]] naturally settle into stable activity patterns, and perturbing the excitation-inhibition balance shifts these dynamics into pathological attractor states.

## Relationship to Subsequent Work

This paper directly influenced subsequent developments in [[computational-psychiatry]] and [[whole-brain-modeling]] for psychiatric applications. The framework was extended in later work to examine [[brain-oscillations]] abnormalities in first-episode psychosis, the effects of [[brain-stimulation]] interventions, and the development of [[personalized-brain-modeling]] approaches that incorporate individual patient [[structural-connectivity]] data. The modeling approach also informed subsequent comparisons between different [[neural-mass-models]] and their suitability for psychiatric applications.

The work connects to the [[wong-wang-model]] framework for understanding excitation-inhibition balance in cortical microcircuits, extending it from local circuit modeling to the whole-brain scale by embedding neural masses in anatomically realistic connectivity matrices. This approach parallels the methodology used in [[the-virtual-brain]] for simulating [[brain-dynamics]] on a whole-brain scale. The [[epileptor]] model, originally developed for seizure modeling, similarly employs neural mass approaches connected through structural connectivity matrices to study pathological brain dynamics.

## Implications for Treatment

The computational model suggests that successful pharmacological interventions must restore excitation-inhibition balance rather than broadly stimulating or depressing neural activity. This principle has guided subsequent development of treatments targeting GABAergic function or specific NMDA receptor subtypes in schizophrenia. The framework enables in silico testing of pharmaceutical interventions before clinical trials, representing a step toward [[personalized-brain-modeling]] in psychiatry.

## Open Questions

Several questions remain active areas of research: how chronic illness differs from the acute pharmacological challenge model, whether these mechanisms generalize to other psychiatric disorders beyond schizophrenia, and how to translate individual patient data into model parameters for personalized predictions. The framework also raises methodological questions about the appropriate level of biological detail in [[computational-psychiatry]] models—adding more molecular specificity may not improve predictive power if the relevant [[brain-dynamics]] emerge at the network level.