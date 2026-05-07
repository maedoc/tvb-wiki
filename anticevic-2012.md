---
title: Anticevic 2012
created: 2025-01-15
updated: 2026-05-07
type: concept
tags: [whole-brain-modeling, computational-neuroscience, neural-mass-models, brain-dynamics, glutamate, gaba, excitation-inhibition-balance, computational-psychiatry]
sources:
  - "[Anticevic A, Gancsos M, Murray JD, Repovs G, Driesen NR, Ennis DJ, et al. NMDA receptor function in large-scale anticorrelated neural systems with implications for cognition and schizophrenia. Proc Natl Acad Sci USA. 2012;109(41):16720-16725. doi:10.1073/pnas.1208494109](https://doi.org/10.1073/pnas.1208494109)"
  - "[Deco G, Ponce-Alvarez A, Mantini D, Romani GL, Hagmann P, Corbetta M. Resting-state functional connectivity emerges from structurally and dynamically shaped slow linear fluctuations. J Neurosci. 2013;33(27):11239-11252.](https://doi.org/10.1523/JNEUROSCI.1091-13.2013)"
  - "[Murray JD, Anticevic A, Gancsos M, Ichinose M, Corlett PR, Krystal JH, Wang X-J. Linking microcircuit dysfunction to cognitive impairment: effects of disinhibition associated with schizophrenia in a cortical working memory model. Cereb Cortex. 2014;24(3):859-872.](https://doi.org/10.1093/cercor/bhs370)"
  - "[Yizhar O, Fenno LE, Prigge M, Schneider F, Davidson TJ, O'Shea DJ, et al. Neocortical excitation/inhibition balance in information processing and social dysfunction. Nature. 2011;477:171-178.](https://doi.org/10.1038/nature10360)"
---

Anticevic 2012 refers to a specific influential paper by Anticevic and colleagues: **"NMDA receptor function in large-scale anticorrelated neural systems with implications for cognition and schizophrenia"** published in *Proceedings of the National Academy of Sciences* in 2012 (PNAS 109(41):16720-16725, DOI: 10.1073/pnas.1208494109) [[1]]. This work combined pharmacological fMRI in healthy volunteers with biophysically constrained computational modeling to investigate how NMDA receptor antagonism affects large-scale brain network interactions relevant to schizophrenia [[2]].

## Overview and Definition

The Anticevic 2012 study addressed a fundamental question in schizophrenia research: how do molecular-level perturbations to glutamate signaling scale up to produce the systems-level disruptions in brain dynamics observed in the disorder? The authors administered subanesthetic ketamine (an NMDA receptor antagonist) to healthy volunteers while they performed a working memory task, then used computational modeling to interpret the observed brain activity changes [[1]].

A central hypothesis in schizophrenia research proposes that reduced NMDA receptor function on GABAergic interneurons produces cortical disinhibition—a breakdown in the balance between excitatory glutamatergic signaling and inhibitory GABAergic signaling [[4]]. The Anticevic 2012 paper provided empirical and computational evidence linking this synaptic-level mechanism to alterations in large-scale functional connectivity between the task-positive fronto-parietal network and the default mode network.

## Biological and Computational Context

The human brain's cortex contains approximately 10¹¹ neurons, with excitatory pyramidal cells and inhibitory GABAergic interneurons engaged in continuous mutual interaction. The excitation/inhibition (E/I) balance is increasingly recognized as a fundamental parameter governing cortical computation—perturbations to this balance have been implicated in schizophrenia, autism, and other neuropsychiatric conditions [[4]].

Anticevic and colleagues extended prior work by modeling the functional antagonism between the task-activated (frontoparietal) network and the task-deactivated default mode network as two reciprocally inhibitory modules. Their computational model implemented disinhibition via selective reduction of NMDA conductance onto inhibitory interneurons, demonstrating that this manipulation reproduced the pattern of brain activity observed under ketamine administration [[3]].

When coupled across brain regions via [[structural-connectivity]] matrices derived from [[dti]] tractography, biophysically realistic neural mass models can reproduce empirical resting-state functional connectivity patterns. This approach has been further developed to understand how the excitation/inhibition balance parameter influences large-scale network dynamics [[2]].

## Mathematical Framework

The neural mass formulation captures population-level dynamics through differential equations describing the evolution of excitatory and inhibitory pool mean membrane potentials. Drawing on the framework developed by Compte et al. (2000) for working memory, the basic equations take the form:

$$\tau_e \frac{dV_e}{dt} = -V_e + J_e S_e + \text{external\_input}$$

$$\tau_i \frac{dV_i}{dt} = -V_i + J_i S_i + J_{ie} S_e$$

where $V_e$ and $V_i$ represent mean membrane potentials of excitatory and inhibitory pools, $\tau_e$ and $\tau_i$ are respective time constants, $J_e$ and $J_i$ are synaptic coupling strengths, and $S_e$, $S_i$ are sigmoid functions mapping membrane potentials to firing rates. The parameter $J_{ie}$ captures the strength of feedback inhibition from excitatory to inhibitory populations—a key control parameter for excitation/inhibition balance.

A key insight from Anticevic 2012 was that perturbing the E/I balance preferentially by reducing NMDA conductance onto inhibitory interneurons caused the two large-scale networks (task-positive and default mode) to lose their normal anticorrelation, producing a pattern consistent with failure to suppress internal thoughts during cognitive tasks [[1]][[3]].

## Relationship to Clinical Translation

The Anticevic 2012 framework demonstrated a computational approach for relating synaptic-level hypotheses (specifically NMDA receptor hypofunction) to systems-level observations measurable with fMRI. This work established important methodological foundations for whole-brain modeling in [[computational-psychiatry]], showing how biophysically realistic models can bridge molecular mechanisms and brain-wide dynamics [[1]][[3]].

By integrating pharmacological challenge studies with computational modeling, this approach enables hypothesis testing about the mechanistic basis of psychiatric symptoms—testing whether specific synaptic perturbations produce patterns consistent with patient data. While the original paper focused on ketamine as a pharmacological model rather than claiming to establish the field of personalized brain modeling, subsequent work hasbuilt on these methods to advance [[personalized-brain-modeling]] approaches.

## Relationship to Other Models and Software

The computational approach developed in Anticevic 2012 shares conceptual territory with several other [[neural-mass-models]]: the Wilson-Cowan model, which captures population-level excitation and inhibition through simpler analytic forms; the [[wong-wang-model]], which adds detailed representations of NMDA and GABA-A receptor dynamics; and the Epileptor model, which specifically addresses seizure dynamics as a pathological limit cycle emerging from excitatory-inhibitory interactions.

In terms of software implementation, this work is conceptually related to [[the-virtual-brain]] simulator, which incorporates neural mass models within a whole-brain connectivity framework. Both approaches couple population-level models across brain regions using empirical structural connectivity to generate large-scale dynamics. The Anticevic framework's focus on glutamate/GABA mechanisms also connects to [[dynamic-causal-modeling]], which uses similar mathematical machinery to infer effective connectivity from neuroimaging data.

## Open Questions and Current Directions

Several open questions remain active research areas. The parameter estimation problem for biophysical models remains challenging—constraining the many parameters from empirical data requires sophisticated variational Bayes or optimization approaches. Furthermore, the relationship between these mesoscopic models and [[spiking-neural-networks]] that resolve individual neuron dynamics remains an active research area, with efforts such as NEST simulation code approaching human-scale cortical simulations.

Contemporary extensions increasingly integrate machine learning approaches. Recent work applying deep learning models to fMRI data for long-range brain dynamics modeling suggests new hybrid architectures that combine the interpretability of biophysical models with the pattern recognition capabilities of neural networks.

## References

1. Anticevic A, Gancsos M, Murray JD, Repovs G, Driesen NR, Ennis DJ, et al. NMDA receptor function in large-scale anticorrelated neural systems with implications for cognition and schizophrenia. Proc Natl Acad Sci USA. 2012;109(41):16720-16725. doi:10.1073/pnas.1208494109

2. Deco G, Ponce-Alvarez A, Mantini D, Romani GL, Hagmann P, Corbetta M. Resting-state functional connectivity emerges from structurally and dynamically shaped slow linear fluctuations. J Neurosci. 2013;33(27):11239-11252.

3. Murray JD, Anticevic A, Gancsos M, Ichinose M, Corlett PR, Krystal JH, Wang X-J. Linking microcircuit dysfunction to cognitive impairment: effects of disinhibition associated with schizophrenia in a cortical working memory model. Cereb Cortex. 2014;24(3):859-872.

4. Yizhar O, Fenno LE, Prigge M, Schneider F, Davidson TJ, O'Shea DJ, et al. Neocortical excitation/inhibition balance in information processing and social dysfunction. Nature. 2011;477:171-178.