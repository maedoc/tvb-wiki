---
title: Viktor Jirsa
created: 2026-04-20
updated: 2026-05-06
type: entity
tags: [people-researcher, whole-brain-modeling, neural-mass-models, network-dynamics, resting-state, epilepsy-modeling]
sources: [raw/papers/deco-2013.md, raw/papers/deco-jirsa-mcintosh-2012.md, raw/papers/petkoski-jirsa-2019.md, raw/papers/stefanescu-jirsa-2008.md, raw/papers/semanticscholar-7c3337c880fd.md]
---

Viktor Jirsa is a computational neuroscientist whose work has fundamentally shaped the theoretical and practical foundations of whole-brain modeling. His research spans the development of neural mass models, the analysis of brain network dynamics, and the application of these models to understand both healthy resting-state activity and pathological conditions such as epilepsy.

## Scientific Contributions

### Resting-State Dynamics and Metastability

Jirsa's work on resting-state brain dynamics represents one of the most influential theoretical frameworks in contemporary computational neuroscience. In a seminal 2012 review published in Nature Reviews Neuroscience, Deco, Jirsa, and McIntosh introduced the concept of **metastability** to explain how the brain maintains rich, variable spatiotemporal patterns during rest without external input. Their key insight was that the brain operates near a critical point—a **bifurcation**—where stable and unstable dynamics coexist, allowing the system to explore a repertoire of functional states. This work established that resting-state networks are not static but rather attractor states that the brain continuously revisits, providing a unified framework for understanding both spontaneous and task-evoked brain activity.

This theoretical foundation was extended in the 2013 paper "Resting brains never rest," which demonstrated through large-scale computational models how noise-driven fluctuations around a stable fixed point in a structured network—constrained by empirical [[structural connectivity]]—can reproduce empirical resting-state [[functional connectivity]] patterns. The model showed that the brain's intrinsic activity arises from the interaction between the topology of anatomical connections and the local dynamics of neural populations.

### Neural Mass Models and Mean-Field Theory

A significant portion of Jirsa's research has focused on bridging the gap between detailed [[spiking neural networks]] and population-level [[neural mass model]]s. The 2008 paper by Stefanescu and Jirsa demonstrated how high-dimensional networks of heterogeneous spiking neurons can be systematically reduced to low-dimensional neural mass descriptions through [[mean-field theory]]. Their approach used the Ott-Antonsen ansatz and moment closure techniques to derive closed-form equations for population firing rates from networks of quadratic integrate-and-fire neurons with distributed parameters. This work provides the mathematical bridge between detailed simulations (as in [[NEST]]) and fast population-level models (as in TVB), enabling researchers to maintain biological realism while achieving tractable computational costs for whole-brain simulations.

### Time Delays and Epilepsy Modeling

Jirsa's research on seizure dynamics has revealed the critical role of [[time delay]]s in coupled neural mass models. The 2019 study with Petkoski demonstrated that time delays in [[structural connectivity]] pathways can lead to complex dynamics including seizure-like activity, oscillations, and pathological synchronization. This work provides theoretical grounding for [[epilepsy modeling]] in TVB, where the Epileptor model incorporates delayed coupling to capture the emergence and propagation of epileptic seizures across brain regions.

### Network Degeneracy and Connectivity

Recent work by Jirsa and collaborators (2026) on the degeneracy of brain dynamics has further illuminated the relationship between [[structural connectivity]] and functional repertoire. Their research identified a low-dimensional representation of brain states—the Resting State Manifold (RSM)—and showed that the patterns of degeneracy in brain networks regulate how the system responds to perturbations. This work connects to TVB's core premise that personalized brain models can be constructed from individual [[structural connectivity]] data derived from [[diffusion imaging]] and [[tractography]].

## Relationship to The Virtual Brain

Jirsa's research program has directly influenced the development of [[the-virtual-brain]] (TVB), a software platform for whole-brain simulation. The theoretical frameworks developed in his papers—particularly the metastability hypothesis, mean-field reduction techniques, and epilepsy modeling approaches—have been integrated into TVB's architecture:

- **Neural Mass Framework**: The mean-field reduction techniques developed in the Stefanescu-Jirsa 2008 paper enable TVB to simulate large-scale brain dynamics using computationally tractable population models instead of requiring explicit spiking network simulations.

- **Resting-State Simulation**: The noise-driven resting-state model from Deco, Jirsa, and McIntosh's work provides the theoretical basis for TVB's ability to simulate spontaneous brain activity and generate realistic [[functional connectivity]] patterns from [[structural connectivity]] data.

- **Epilepsy Modeling**: The Epileptor model in TVB builds on Jirsa's analysis of seizure dynamics and time-delayed coupling, enabling researchers to simulate seizure onset, propagation, and termination in patient-specific brain networks.

- **Personalized Brain Modeling**: The emphasis on using individual [[structural connectivity]] data to constrain whole-brain models stems from Jirsa's research demonstrating that anatomical connectivity shapes the repertoire of possible functional states.

## Key Publications

| Year | Citation | Venue |
|------|----------|-------|
| 2008 | Stefanescu & Jirsa, "A low dimensional description of globally coupled heterogeneous neural networks" | PLoS Computational Biology |
| 2012 | Deco, Jirsa & McIntosh, "Emerging concepts for the dynamical organization of resting-state activity" | Nature Reviews Neuroscience |
| 2013 | Deco, Jirsa & McIntosh, "Resting brains never rest: computational insights" | Trends in Neurosciences |
| 2019 | Petkoski & Jirsa, "Time-Delayed Coupling Complex Systems and Seizure Dynamics" | Physical Review Letters |
| 2026 | Gudibanda et al., "The role of connectivity for the degeneracy of the brain's resting state dynamics" | Journal of Computational Neuroscience |

## Related Concepts

- [[whole-brain-modeling]]: The field Jirsa helped establish, simulating whole-brain dynamics from anatomical connectivity
- [[neural-mass-models]]: Population-level models his work has advanced and formalized
- [[resting-state]]: The dynamical regime his theoretical work most extensively addresses
- [[epilepsy-modeling]]: Application domain for his seizure dynamics research
- [[structural-connectivity]]: The anatomical substrate his models are constrained by
- [[functional-connectivity]]: The emergent patterns his models reproduce
- [[mean-field-theory]]: The mathematical framework enabling reduction from spiking to population models
- [[bifurcation-analysis]]: The dynamical systems technique used to understand brain state transitions
- [[the-virtual-brain]]: The software platform implementing his theoretical frameworks
- [[epileptor]]: The TVB model for seizures based on his research