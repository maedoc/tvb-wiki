---
title: Anticevic 2012
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [whole-brain-modeling, computational-neuroscience, excitation-inhibition-balance, resting-state, functional-connectivity, computational-psychiatry, brain-dynamics]
sources: []
---

Anticevic 2012 refers to a influential line of research by Aleksi Anticevic and colleagues on whole-brain computational modeling of excitatory-inhibitory dynamics and their relationship to resting-state functional connectivity. This work established foundational connections between neurobiologically realistic neural mass models and empirically observed patterns of spontaneous brain activity, particularly within the [[default-mode-network]] and other [[intrinsic-connectivity-networks]].

## Background and Motivation

The central challenge addressed by this research concerns how large-scale patterns of spontaneous brain activity—observed via [[resting-state]] [[functional-connectivity]] [[fmri]]—emerge from the interplay between excitatory and inhibitory neural populations constrained by [[structural-connectivity]] derived from [[dti]] and tractography. Prior to 2012, much of the resting-state literature treated functional connectivity as a static or slowly varying property, without mechanistic account of how these networks arise dynamically from neural circuitry. Anticevic's work bridged this gap by demonstrating that [[excitation-inhibition-balance]] is a critical determinant of whole-brain dynamic states.

## Technical Contributions

The computational framework developed in this work employs [[neural-mass-models]] that represent local cortical populations as interacting excitatory and inhibitory neural pools. These models are embedded within a [[structural-connectivity]] matrix derived from empirical diffusion imaging data, creating a whole-brain network where each node represents a brain region with its own local dynamics. The key analytical insight was demonstrating that the Balance between excitatory glutamatergic signaling and inhibitory GABAergic signaling determines both the stability of resting-state dynamics and the ability of the system to transition between different functional configurations.

The mathematical formulation captures neural population dynamics through differential equations describing the evolution of mean firing rates for excitatory ($E$) and inhibitory ($I$) populations:

$$\frac{dE}{dt} = -E + S(W_E \cdot E - W_I \cdot I + \alpha \xi(t))$$

$$\frac{dI}{dt} = -I + S(W_E \cdot E - W_I \cdot I + \beta \xi(t))$$

where $S(\cdot)$ is a sigmoidal activation function, $W_E$ and $W_I$ represent recurrent excitatory and inhibitory synaptic weights, and $\xi(t)$ represents noise-driven fluctuations that probe the system's dynamic repertoire.

## Relationship to Resting-State Dynamics

A crucial finding from Anticevic 2012 and subsequent work is that noise-driven fluctuations in a balanced excitatory-inhibitory system naturally give rise to functional connectivity patterns that mirror empirically observed [[resting-state-fmri]] networks. This emergence occurs without task-evoked inputs, suggesting that the resting brain's spontaneous dynamics are not merely idle states but rather reflect continuous exploration of the state's dynamical repertoire constrained by the [[structural-connectivity]] scaffold. The [[default-mode-network]] emerges as a particularly robust pattern due to specific properties of the structural connectivity between regions supporting internally-directed versus externally-directed processing.

## Computational Psychiatry Implications

This work has had substantial impact on [[computational-psychiatry]], demonstrating that alterations in excitation-inhibition balance—hypothesized to underlie conditions such as [[schizophrenia-models]] and [[epilepsy-modeling]]—can be modeled mechanistically and their whole-brain consequences evaluated against empirical neuroimaging data. By fitting model parameters to patient populations, researchers can infer which specific circuit-level alterations drive observed changes in functional connectivity. This approaches bridges the gap between cellular-level neurochemistry and systems-level neuroimaging observables.

## Relationship to TVB

[[the-virtual-brain]] (TVB) implements related neural mass modeling frameworks that build upon the theoretical foundations established by Anticevic and colleagues. The [[wong-wang-model]] and related excitatory-inhibitory neural mass models available in TVB's model library enable direct application to studying the relationship between whole-brain excitation-inhibition balance and functional connectivity. TVB's ability to simulate large-scale brain networks with configurable neural mass models enables researchers to extend the original Anticevic framework with patient-specific connectivity data and to predict the effects of pharmacological interventions on whole-brain dynamics.

## Related Concepts

The theoretical framework connects to several foundational concepts in whole-brain modeling: [[whole-brain-modeling]] generally, [[excitation-inhibition-balance]] as a fundamental regulatory mechanism, [[resting-state]] dynamics as an emergent property, [[functional-connectivity]] as an observable outcome of underlying neural dynamics, and [[computational-psychiatry]] as an applied domain. Methodologically, it relates to [[dynamic-causal-modeling]] and [[neural-mass-models]] as specific computational implementations.