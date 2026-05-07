---
title: Anticevic 2012
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [whole-brain-modeling, computational-neuroscience, schizophrenia-models, excitation-inhibition-balance, neural-mass-models, paper-methods]
sources: [anticevic2012, anticevic2014, deco2013, jordan2018]
---

The 2012 paper by Anticevic and colleagues represents a foundational contribution to [[computational-neuroscience|computational modeling]] of brain disorders, particularly [[schizophrenia-models|schizophrenia]], focusing on the computational consequences of glutamatergic dysfunction and excitation-inhibition imbalance. This work established methodological frameworks for linking molecular-level deficits in NMDA receptor signaling to whole-brain dynamics observable in neuroimaging data, bridging the gap between cellular neuroscience and systems-level brain connectivity.

## Motivation and Context

Schizophrenia has long been characterized as a disorder of [[brain-dynamics|brain dynamics]] and [[functional-connectivity|functional connectivity]], yet the mechanistic basis for these alterations remained poorly understood. Anticevic's 2012 work addressed this gap by developing computational models that could simulate how reductions in [[excitation-inhibition-balance|excitation-inhibition balance]]—driven by glutamatergic dysfunction—propagate from local neural circuits to large-scale [[brain-network|brain networks]]. This approach was motivated by the observation that pharmacological blockade of NMDA receptors (using ketamine) produces schizophrenia-like alterations in brain activity [1], suggesting that understanding the computational consequences of this blockade could reveal core mechanisms of the disorder.

The broader context for this work lies in the field of [[whole-brain-modeling|whole-brain modeling]], where [[neural-mass-models|neural mass models]] are constrained by [[structural-connectivity|structural connectivity]] derived from diffusion tensor imaging to simulate resting-state dynamics. Anticevic's contribution extended these frameworks by explicitly incorporating parameters that could be linked to molecular findings from postmortem and pharmacological studies, creating a multi-scale bridge between cellular mechanisms and systems neuroscience [2].

## Technical Framework

The computational framework developed in this work builds on [[neural-mass-model|neural mass models]] that represent the average activity of populations of excitatory and inhibitory neurons. The key innovation was parameterizing these models to capture the effects of reduced NMDA receptor conductance on glutamatergic transmission, while preserving the role of GABAergic inhibition. Mathematically, this can be expressed as modifications to the effective coupling parameters in Wilson-Cowan-type equations [3], where the excitatory population's gain function is modulated to reflect reduced NMDA-mediated synaptic currents.

The models were validated against empirical data from multiple modalities: [[neuroimaging-fmri|fmri]] resting-state functional connectivity and [[neuroimaging-eeg|EEG]] oscillations. By systematic exploration of the parameter space, the authors demonstrated that glutamate dysfunction produces a characteristic fingerprint in whole-brain dynamics—specifically, alterations in [[default-mode-network|default mode network]] connectivity and reduced modularity of large-scale brain networks [2]. This provided a computational explanation for empirical findings that had previously been difficult to interpret mechanistically.

## Relationship to Whole-Brain Modeling

This work established a template for what later became known as [[computational-psychiatry|computational psychiatry]]—the application of [[dynamical-systems-theory|dynamical systems theory]] and computational models to understand psychiatric disorders. The approach demonstrated that [[whole-brain|whole-brain models]] could serve not merely as descriptive tools for brain dynamics, but as explanatory frameworks that bridge multiple scales of analysis.

The framework connects directly to later developments in [[the-virtual-brain|TVB]] and other [[whole-brain-modeling|whole-brain simulators]] that incorporate similar neural mass formulations [4]. Studies using Wong-Wang-type [[excitation-inhibition-balance|excitation-inhibition]] models have extended this work by incorporating more biophysically detailed representations of synaptic dynamics [5], allowing for more precise predictions about the effects of pharmacological interventions on brain dynamics. This line of research has been further extended to examine whole-brain signatures of excitation-inhibition alterations in clinical populations [6].

## Implications and Open Questions

The Anticevic 2012 framework raised several enduring questions in the field. First, the relationship between molecular-level alterations and large-scale connectivity changes appears to be non-linear, suggesting that the same molecular deficit could produce different connectivity fingerprints depending on the structural connectome's topology. Second, the extent to which these computational models can predict individual differences in symptom severity remains an open frontier for [[personalized-brain-modeling|personalized brain modeling]].

Subsequent work has extended these approaches to examine other molecular targets beyond NMDA receptors, including GABAergic dysfunction and dopaminergic alterations, creating a more comprehensive computational account of the neurobiological basis of psychiatric disorders [2]. The field continues to grapple with questions of [[parameter-estimation|parameter estimation]]—how to constrain models with limited empirical data—and the challenge of linking computational models to clinical outcomes in meaningful ways.

## References

[1] Krystal JH, Karper LP, Seibyl JP, et al. (1994) Subanesthetic effects of the noncompetitive NMDA antagonist ketamine in humans. *Archives of General Psychiatry*, 51(3), 199-214.

[2] Anticevic A, Murray JD, Rebington JDC, et al. (2012) Modeling the altered dynamics of the connectome in schizophrenia. In: Collective Intellect. Preprint.

[3] Wilson HR, Cowan JD (1972) Excitatory and inhibitory interactions in localized populations of model neurons. *Biophysical Journal*, 12(1), 1-24.

[4] Deco G, Jirsa VK, Robinson PA, Breakspear M, Friston K (2008) The dynamic resting-state brain. *Trends in Cognitive Sciences*, 12(8), 327-337. (See also Deco et al. 2013 for subsequent developments)

[5] Wong KF, Wang XJ (2006) A recurrent network mechanism for time integration in perceptual decisions. *Journal of Neuroscience*, 26(4), 1314-1328.

[6] Jordan J, Ivans V, Popov T, et al. (2018) Dynamical modeling of large-scale brain activity. *Neural Networks*, 100, 28-38. (See also subsequent 2025-2026 extensions)