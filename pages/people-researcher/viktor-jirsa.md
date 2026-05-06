---
title: Viktor Jirsa
created: 2026-04-20
updated: 2026-05-06
type: concept
tags: [people-researcher, whole-brain-modeling, neural-mass-models, the-virtual-brain, computational-neuroscience, resting-state, epilepsy-modeling, structural-connectivity, functional-connectivity]
sources: [raw/papers/semanticscholar-7c3337c880fd.md, raw/papers/deco-2013.md]
references:
  - deco-2013
  - jirsa-epileptor-2014
  - gudibanda-rsm-2026
---

Viktor Jirsa is a computational neuroscientist affiliated with Aix-Marseille Université and the Institut de Neurosciences des Systèmes in France, whose work has fundamentally shaped the field of whole-brain modeling, particularly through the development of neural mass models and large-scale brain network simulations that bridge structural connectivity to observed functional dynamics. His research emphasizes how the anatomical scaffold of the brain—measured through diffusion imaging and tractography—constrains and shapes the spontaneous fluctuations observed in resting-state fMRI, EEG, and MEG recordings. Through a combination of dynamical systems theory, mean-field approximations, and parameter estimation techniques, Jirsa's contributions have provided both a theoretical framework and practical software tools for simulating whole-brain activity at the scale of individual brain regions.

## Theoretical Foundations: From Local Dynamics to Global Emergence

The central insight driving much of Jirsa's work is that brain activity at the macroscale emerges from the interaction between local region-level dynamics and the patterns of anatomical connections that link them (Deco et al. 2013). This perspective treats the brain as a networked dynamical system where individual cortical or subcortical areas are modeled as neural mass units—collective representations of millions of neurons whose average activity can be described by reduced equations capturing excitatory and inhibitory interactions. The mathematical framework typically employs delay differential equations or stochastic differential equations to account for finite signal transmission speeds across white matter pathways, with the structural connectivity matrix (derived from diffusion tensor imaging or more advanced tractography methods) providing the coupling architecture.

Jirsa's group has developed several influential neural mass formulations, including models that generate realistic seizure-like dynamics. The Epileptor model, first introduced by Jirsa and colleagues in 2014, captures the essential features of epileptiform activity including interictal spikes, ictal transitions, and post-ictal recovery, making it a valuable tool for studying seizure propagation and the effects of targeted stimulation. These models demonstrate how patient-specific structural connectivity can be incorporated into personalized brain models, enabling predictions of seizure spread patterns that may guide surgical planning or responsive neurostimulation interventions.

## The Resting State Manifold and Network Degeneracy

A major theoretical contribution from Jirsa's group concerns the concept of the resting state manifold (RSM) and its relationship to network degeneracy. In a series of papers, including work with Gudibanda, Fousek, and Petkoski published in the Journal of Computational Neuroscience (2026), the framework identifies a low-dimensional representation of brain states that emerges from the constrained dynamics of whole-brain models. The resting state manifold represents the collection of accessible functional configurations that the brain can occupy given its anatomical structure, and degeneracy refers to the property whereby many different patterns of neural activity can produce similar observable outcomes (Gudibanda et al. 2026).

This work demonstrates that the patterns of degeneracy in whole-brain dynamics are not random but are systematically related to structural properties of the connectome—including modular organization, hub structure, and rich-club connectivity. The productive relationship between emergent network processes and their constituent network entities means that the same anatomical scaffold can support multiple functional repertoires, explaining how the resting brain can flexibly reconfigure between different states while maintaining stability. Noise-driven dynamics naturally explore the manifold, and the contours of degeneracy determine how the system responds to external perturbations or internal variations.

## Relationship to The Virtual Brain

Jirsa's work is fundamentally intertwined with [[the-virtual-brain]] (TVB), the open-source software platform for whole-brain simulation that he helped develop and which serves as a primary tool in the field. TVB implements the neural mass models and large-scale network formulations described above, providing researchers with a graphical interface and programming libraries for constructing personalized brain models from individual structural connectivity data. The software integrates with standard neuroimaging pipelines, accepting connectivity matrices from tools such as [[connectome-workbench]], [[mrtrix3]], or [[dipy]], and can simulate activity across multiple spatial scales from individual regions to the whole brain.

The relationship between Jirsa's theoretical contributions and TVB is bidirectional: his research provides the mathematical foundations that the software implements, while the software enables the community to test and validate the theoretical predictions at scale. TVB's ability to generate simulated fMRI, EEG, and MEG signals from the same underlying model allows direct comparison with empirical data, supporting parameter estimation workflows that fit model parameters to observed brain activity. This integration of theory, computation, and empirical validation has made TVB a cornerstone of the whole-brain modeling ecosystem, with applications ranging from basic neuroscience questions about resting-state dynamics to clinical applications in [[epilepsy-modeling]].

## Key Publications and Impact

The 2013 paper by Deco, Jirsa, and McIntosh in *Trends in Neurosciences*, "Resting brains never rest," articulated an influential computational framework for understanding spontaneous brain activity (Deco et al. 2013). This work demonstrated that noise-driven fluctuations around stable fixed points in structured networks could reproduce empirical resting-state functional connectivity patterns, suggesting that the resting brain continuously explores a repertoire of functional states that overlap with those evoked during tasks. The unified view of resting and task dynamics proposed in this paper has influenced subsequent research on intrinsic brain activity, [[functional-connectivity]], and the relationship between [[structural-connectivity]] and [[functional-connectivity]].

Jirsa's work spans the [[neural-mass-models]] spectrum from detailed biophysical models to reduced formulations suitable for parameter estimation and clinical translation. The emphasis on patient-specific modeling—incorporating individual connectivity data rather than group-averaged templates—has advanced the field toward [[personalized-brain-modeling]] applications, where computational models may eventually guide clinical decision-making in neurology and psychiatry.

## Related Concepts

- [[whole-brain-modeling]] — the broader framework within which Jirsa's work operates
- [[the-virtual-brain]] — the software platform developed in part from Jirsa's research
- [[resting-state]] — the dynamics Jirsa's models specifically address
- [[epilepsy-modeling]] — the application domain of Epileptor-type models
- [[structural-connectivity]] — the anatomical foundation Jirsa's models incorporate
- [[functional-connectivity]] — the emergent patterns his models predict
- [[neural-mass-models]] — the mathematical formulation of regional dynamics
- [[connectome]] — the network-level description of brain wiring
- Yan Wang — researcher contributing to the development of the Epileptor model and whole-brain epilepsy simulations

## References

1. Deco, G., Jirsa, V. K., & McIntosh, A. R. (2013). Resting brains never rest: Computational insights into the brain's resting state. *Trends in Neurosciences*, 36(12), 738-749.

2. Jirsa, V. K., Stacey, W. C., Quilichini, P. P., Ivanov, A. I., & Bernard, C. (2014). On the nature of seizure dynamics. *Brain*, 137(8), 2210-2230.

3. Gudibanda, A., Fousek, J., Petkoski, S., & Jirsa, V. K. (2026). Resting state manifold and degeneracy in whole-brain networks. *Journal of Computational Neuroscience*.