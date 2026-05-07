---
created: 2025-01-15
sources:
- wong-wang-2006
- deco-et-al-2013
- deco-et-al-2014
- tvb-documentation
- breakspear-2004
- jansen-rit-1995
- raw/papers/wilson-cowan-1972.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/semanticscholar-ce89e593c89e.md
tags:
- neural-mass-model
- whole-brain-modeling
- rate-based-neural-networks
- excitation-inhibition-balance
- computational-neuroscience
- brain-oscillations
- network-dynamical-systems-theory
title: Wong-Wang Model
type: concept
updated: '2026-05-07'
---

The [[wong-wang|Wong-Wang model]] is a [[neural-mass-models|neural mass model]] that describes the dynamics of excitatory and inhibitory neural populations through coupled firing-rate equations. Originally developed by Kong-Feng Wong and Xiao-Jing Wang in 2006, this model provides a computationally tractable framework for simulating large-scale [[brain-dynamics]] while retaining sufficient biological detail to capture key phenomena such as oscillations, multistability, and state transitions[^wong-wang-2006]. The model has become one of the most widely adopted canonical models in [[whole-brain|whole-brain modeling]] frameworks, particularly within [[the-virtual-brain]] (TVB), where it serves as a default option for simulating regional cortical dynamics[^deco-et-al-2014][^tvb-documentation].

## Motivation and Context

The development of the Wong-Wang model addressed a fundamental challenge in [[computational-neuroscience]]: bridging the gap between detailed single-[[neuron]] models and macroscopic brain dynamics observable through [[neuroimaging]]. Biologically realistic neuron-by-neuron simulations of whole-brain-scale networks remain computationally prohibitive, while earlier abstract models lacked the capacity to capture important features of real neural circuitry. The Wong-Wang model strikes a balance by representing populations of excitatory pyramidal cells and inhibitory interneurons as unified units, capturing the essential dynamics of recurrent excitation and inhibition without the overhead of simulating individual spiking neurons[^wong-wang-2006].

This modeling approach fits within a broader tradition of neural mass models including the [[jansen-rit-model]][^jansen-rit-1995], [[wilson-cowan-model]], and [[larter-breakspear]][^breakspear-2004] model. However, the Wong-Wang model distinguishes itself through its relative mathematical tractability and its explicit formulation of excitatory-inhibitory interactions that give rise to asynchronous and oscillatory regimes. The model enables researchers to investigate how changes in the balance between excitation and inhibition—a key factor in numerous brain disorders—impact large-scale network dynamics observable in fMRI and EEG[^wong-wang-2006].

It is important to distinguish between the original two-population Wong-Wang model (2006) and the reduced single-population variant that is commonly used in whole-brain simulations. The reduced model, developed by Deco and colleagues in 2013, simplifies the excitatory population while preserving the essential NMDA-mediated dynamics that give rise to the model's characteristic slow oscillatory behavior[^deco-et-al-2013]. TVB's default implementation uses this reduced formulation for computational efficiency, as discussed in the following sections.

## Mathematical Formulation

### Original Two-Population Model

The original Wong-Wang model describes the evolution of synaptic activity variables for excitatory and inhibitory populations. For a single brain region, the equations take the form of a system of ordinary differential equations[^wong-wang-2006]:

$$\tau_E \frac{dS_E}{dt} = -S_E + \phi\left(J_{EE} S_E - J_{EI} S_I + I_{\text{external}}\right)$$

$$\tau_I \frac{dS_I}{dt} = -S_I + \phi\left(J_{IE} S_E - J_{II} S_I + I_{\text{external}}\right)$$

where $S_E$ and $S_I$ represent the average synaptic activity of excitatory and inhibitory populations respectively, $\tau_E$ and $\tau_I$ are their respective time constants, and $J_{EE}$, $J_{EI}$, $J_{IE}$, and $J_{II}$ represent the coupling strengths between populations (the first subscript denotes the receiving population, the second the sending population). The nonlinearity $\phi(x) = (1 + \tanh(x))/2$ or alternatively a sigmoid function transforms the total input into a firing rate. The external input $I_{\text{external}}$ can represent sensory drive, neuromodulation, or noise[^wong-wang-2006].

### Reduced Single-Population Model (Used in TVB)

The reduced Wong-Wang model, which serves as TVB's default implementation, simplifies the dynamics to a single excitatory population with NMDA-mediated recurrent excitation[^deco-et-al-2013][^deco-et-al-2014]:

$$\tau_E \frac{dS_E}{dt} = -S_E + \phi\left(J_{EE} S_E + I_{\text{external}}\right)$$

In this formulation, the inhibitory dynamics are not explicitly modeled but can be effectively incorporated through the choice of the $J_{EE}$ parameter or through a separate inhibitory time constant. This reduction preserves the essential slow dynamics of the original model while significantly reducing computational cost for whole-brain simulations[^deco-et-al-2013].

The model exhibits rich dynamics including stable fixed points corresponding to asynchronous states, limit cycles corresponding to oscillations, and bistability between these regimes depending on the parameters. The ratio of excitatory to inhibitory coupling strength proves particularly critical: when recurrent excitation dominates, the system settles into a high-activity state, while strong inhibition can suppress activity or generate rhythmic oscillations reminiscent of gamma or beta bands observed in electrophysiological recordings[^wong-wang-2006][^deco-et-al-2013].

## Relationship to Other Models and TVB

The Wong-Wang model represents one of several neural mass implementations available in TVB. In the TVB framework, regional Wong-Wang dynamics are coupled through a [[structural-connectivity]] matrix derived from diffusion tensor imaging, allowing researchers to simulate how local excitatory-inhibitory balance interacts with the anatomical connectivity structure to produce [[functional-connectivity]] patterns resembling those observed in empirical [[resting-state]] fMRI[^deco-et-al-2014].

The model connects to broader concepts in [[dynamical-systems-theory]], where the transition between qualitatively different dynamical regimes—fixed points, oscillations, and chaotic attractors—provides a mathematical framework for understanding brain state transitions. The [[excitation-inhibition-balance]] is also central to many clinical applications: altered E/I balance has been implicated in [[schizophrenia-models]] and [[epilepsy-modeling]], and the Wong-Wang model provides a tool for exploring how pathological changes in synaptic parameters propagate through large-scale networks[^wong-wang-2006].

For comparison, the [[epileptor]] model in TVB represents a specialized extension designed specifically to capture seizure dynamics, while the Wong-Wang model serves as a more general-purpose option for modeling healthy dynamics and a wider range of brain states[^tvb-documentation]. The [[wong-wang-exc-inh]] variant provides an even simpler formulation focusing exclusively on excitatory dynamics, useful when the computational simplicity outweighs the need for explicit inhibitory dynamics.

## Parameter Estimation and Applications

A critical aspect of applying the Wong-Wang model to empirical data involves fitting its parameters—particularly the coupling strengths $J_{EE}$, $J_{EI}$, $J_{IE}$, and $J_{II}$—to match observed [[functional-connectivity]] patterns. This falls within the broader framework of [[parameter-estimation]] methods used throughout whole-brain modeling. Typical approaches include gradient-based optimization, evolutionary algorithms, and more recently, approaches based on [[variational-bayes]] and machine-learning surrogate models[^deco-et-al-2014].

The model has been employed to study [[brain-oscillations]] at [[rest]], working memory processes, and the effects of [[brain-stimulation]] on [[network-dynamics]]. Its relatively low computational cost makes it suitable for parameter sweeps and sensitivity analyses across large cohorts, enabling investigations of individual differences in dynamical parameters and their relationship to behavioral measures or clinical outcomes[^deco-et-al-2013][^deco-et-al-2014].

---