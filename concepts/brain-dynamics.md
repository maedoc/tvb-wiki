---
created: 2026-04-20
sources:
- raw/papers/strogatz-1994.md
- raw/papers/izhikevich-2007.md
- raw/papers/breakspear-2017.md
- raw/papers/kuramoto-1974.md
- raw/papers/coherence-resonance-1998.md
- raw/papers/deco-2012.md
- raw/papers/breakspear-2010.md
- raw/papers/buzsaki-2004.md
- raw/papers/semanticscholar-2004e006655b.md
- raw/papers/arxiv-2512.03907.md
tags:
- neural-mass-models
- whole-brain-modeling
- network-dynamics
- nonlinear-dynamics
- brain-oscillations
title: Brain Dynamics
type: concept
updated: '2026-05-06'
---

Brain dynamics refers to the temporal evolution of neural activity across spatial scales ranging from individual neurons to entire brain regions. In the context of [[whole-brain modeling]], brain dynamics encompasses the mathematical description of how large-scale neural networks generate time-varying patterns of activity that give rise to [[functional connectivity]] observed in [[neuroimaging-fmri]], [[neuroimaging-eeg]], and [[neuroimaging-meg]] recordings. The field sits at the intersection of [[computational-neuroscience]], [[dynamical-systems-theory]], and [[connectomics]], providing a framework for understanding how the brain's fixed [[structural-connectivity]] (derived from [[diffusion-imaging]] tractography) gives rise to flexible [[functional-connectivity]] states.

## Mathematical Framework

The dynamics of large-scale brain activity are typically modeled using systems of coupled differential equations that describe the evolution of neural population activity over time. At the level of neural mass models, each brain region is represented by a set of state variables—typically representing average membrane potentials, firing rates, or synaptic currents—whose dynamics follow [[neural-mass-models]] equations such as the [[jansen-rit-model]], the [[wilson-cowan-model]], or the [[epileptor]] model. The mathematical structure generally takes the form of a system of stochastic differential equations:

$$\frac{d\mathbf{x}_i}{dt} = \mathbf{F}(\mathbf{x}_i) + \mathbf{G}(\mathbf{x}_i, \mathbf{x}_j) + \mathbf{\xi}(t)$$

where $\mathbf{x}_i$ represents the state vector for region $i$, $\mathbf{F}$ captures the local dynamics of that region, $\mathbf{G}$ captures the coupling from other regions determined by the [[structural-connectivity]] matrix, and $\mathbf{\xi}$ represents stochastic noise inputs. Time delays arising from finite conduction velocities are often incorporated, making these systems delay-differential equations that can exhibit rich oscillatory and chaotic behavior.

The theoretical foundation for understanding these dynamics draws heavily from [[nonlinear-dynamics]] and [[bifurcation-analysis]]. As parameters such as coupling strength, excitation-inhibition balance, or external input change, neural mass models can undergo qualitative transitions between dynamical regimes—resting states, oscillations, and pathological states such as seizures—through bifurcation points including saddle-node, [[andronov-hopf-bifurcation]], and pitchfork bifurcations [[strogatz-1994]]. Izhikevich's work provides a geometric classification of these transitions in single neurons that extends to population-level models [[izhikevich-2007]].

## Emergent Network Dynamics

When multiple brain regions are coupled via structural connectivity, novel dynamics emerge that cannot be understood from isolated regions alone. The topology of the connectome—including modular organization, [[rich-club]] hubs, and small-world properties—shapes the patterns of synchronization and propagation that arise [[breakspear-2017]]. Network oscillations emerge through mechanisms including synchronization of nearly identical oscillators (Kuramoto model) [[kuramoto-1974]], frequency-dependent phase locking, and coherence resonance where noise actually enhances oscillatory behavior [[coherence-resonance-1998]].

The study of brain dynamics has revealed several canonical spatiotemporal patterns that recur across individuals and species. These include [[brain-oscillations]] across frequency bands (delta, theta, alpha, beta, gamma) [[buzsaki-2004]], traveling waves that sweep across cortical surfaces [[breakspear-2010]], explosive synchronization transitions similar to phase transitions in physical systems [[kuramoto-1974]], and critical brain dynamics where the system hovers near a critical point, maximizing information processing capacity [[breakspear-2010]]. These patterns provide the mechanistic link between the structural scaffold provided by white matter pathways and the fluid functional connectivity observed in resting-state [[neuroimaging-fmri]].

## Relationship to Whole-Brain Modeling

[[whole-brain modeling]] in the tradition of [[the-virtual-brain]] takes brain dynamics as its core object of study, constructing personalized brain models by combining individual structural connectivity (from [[dti]] or [[hcp-dataset]]) with generic neural mass model dynamics [[deco-2012]]. The fundamental hypothesis is that individual differences in brain dynamics arise from individual differences in structural connectivity, modulated by region-specific parameters that can be fit to empirical data. This approach has been particularly successful in [[epilepsy-modeling]], where the [[epileptor]] model captures seizure onset and propagation through bifurcation dynamics, as well as in studying the effects of [[brain-stimulation]] on network dynamics, including transcranial magnetic stimulation and deep brain stimulation interventions that can induce lasting changes in neural synchrony.

Beyond The Virtual Brain, several other computational neuroscience platforms implement brain dynamics simulations. [[nest]] and [[brian2]] provide spiking neural network simulators that can simulate brain dynamics at finer spatial scales, while [[nengo]] implements neural engineering frameworks. Dynamic causal modeling ([[dcm]]) as implemented in [[spm]] provides a Bayesian framework for inferring the parameters of brain dynamics from neuroimaging data, connecting theoretical models to empirical observations.

## Open Questions and Challenges

Despite significant progress, fundamental questions remain about brain dynamics. The precise relationship between [[structural-connectivity]] and [[functional-connectivity]]—how the fixed anatomical scaffold gives rise to flexible functional states—remains incompletely understood, particularly regarding the relative roles of direct anatomical pathways versus indirect polysynaptic pathways. The appropriate level of abstraction for modeling—whether neural mass models, [[neural-field-theory|neural field]] models, or spiking networks—depends on the questions being asked, and no consensus exists on which framework is optimal for which applications.

Parameter estimation remains a central challenge: whole-brain models contain numerous parameters that cannot be directly measured in vivo, and fitting them to individual subjects requires solving high-dimensional inverse problems. Recent approaches using [[variational-bayes]] and machine learning show promise but require further validation. Additionally, the relationship between brain dynamics in healthy individuals and in clinical populations—such as in [[schizophrenia-models]] or [[alzheimers-modeling]]—offers both a motivation and a testbed for improved models.

## Related Concepts

Brain dynamics connects to several foundational concepts in the wiki. [[bifurcation-analysis]] provides the mathematical toolkit for understanding regime changes. [[neural-mass-models]] are the primary building blocks. [[network-dynamics]] encompasses the study of how network structure shapes temporal evolution. The [[mindboggle]] toolbox provides tools for extracting dynamical features from neuroimaging data. Finally, [[brain-oscillation]]s represent one of the key empirical signatures of brain dynamics observable across neuroimaging modalities.

---

## References

1. (authors unknown). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*.
2. Eugene M. [[izhikevich]]. *Dynamical Systems in Neuroscience: The Geometry of Excitability and Bursting*.
3. Michael Breakspear. *Dynamic models of large-scale brain activity*. Nature Neuroscience (Review). [DOI](](https://doi.org/10.1038/s41593-017-0015-4))