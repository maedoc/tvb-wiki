---
created: 2026-04-27
sources:
- raw/papers/strogatz-1994.md
- raw/papers/semanticscholar-ce89e593c89e.md
- raw/papers/doedel-oldeman-2009.md
- raw/papers/izhikevich-2007.md
- raw/papers/semanticscholar-cc2129666e15.md
tags:
- spiking-neural-networks
- neural-mass-models
- computational-neuroscience
- whole-brain-modeling
- bifurcation-analysis
- nonlinear-dynamics
- brain-oscillations
- dynamical-systems-theory
title: Izhikevich
type: concept
updated: '2026-05-06'
---

The Izhikevich neuron model — a concept in [[whole-brain|whole-brain modeling]] and [[computational-neuroscience]].

The Izhikevich model is a two-dimensional [[nonlinear dynamics|nonlinear]] system that captures the essential spiking and bursting dynamics of cortical neurons while remaining computationally tractable for large-scale simulations [[izhikevich-2007]]. Published by Eugene Izhikevich in 2003, it bridges the gap between biologically realistic but computationally expensive models like the [[Hodgkin-Huxley model]] and simpler [[integrate-and-fire]] approximations, making it particularly valuable for [[neural mass models|whole-brain modeling]] where thousands or millions of neurons must be simulated simultaneously.

## Mathematical Formulation

The canonical Izhikevich model is defined by the system of ordinary differential equations [[izhikevich-2007]]:

$$\frac{dv}{dt} = 0.04v^2 + 5v + 140 - u + I$$

$$\frac{du}{dt} = a(bv - u)$$

where *v* represents the membrane potential and *u* represents the membrane recovery variable, which accounts for the activation of potassium currents and inactivation of sodium currents. The parameter *I* denotes the injected synaptic current. After each spike, when the membrane potential reaches +30 mV, the variables are reset according to:

$$v \leftarrow c$$
$$u \leftarrow u + d$$

The model exhibits a rich diversity of firing patterns determined by the four parameters *a*, *b*, *c*, and *d*: parameter *a* controls the recovery time constant, *b* governs the sensitivity of the recovery variable to the membrane potential, *c* sets the reset value of the membrane potential after a spike, and *d* determines the reset of the recovery variable [[izhikevich-2007]]. This relatively simple reformulation can reproduce the rich repertoire of spiking patterns observed in cortical neurons, including tonic spiking, Class 1 excitability, spike-frequency adaptation, and various forms of bursting.

## Dynamical Systems Perspective

From a [[bifurcation theory|bifurcation]] standpoint, the Izhikevich model generates different firing modes through qualitative changes in phase space structure as parameters vary. The transition between resting and spiking states occurs via a saddle-node on invariant circle (SNIC) bifurcation, while the emergence of bursting involves a more complex interaction between a stable equilibrium and a stable limit cycle [[izhikevich-2007]], [[strogatz-1994]]. This geometric classification of neuronal excitability types—distinguishing between integrator versus resonator neurons, for example—provides a principled framework for understanding how different cortical cell types contribute to network-level dynamics.

The [[dynamical-systems-theory|dynamical systems]] approach also illuminates how the model captures the relationship between neural oscillations and spiking activity. At the single-neuron level, the model exhibits canards—precursor oscillations that precede the explosive onset of firing—and exhibits phase-space structures that parallel those analyzed in simpler models like the [[FitzHugh-Nagumo model]] [[izhikevich-2007]]. Understanding these structures is essential for interpreting the emergence of [[brain oscillations]] in large-scale neural models, where population-level oscillations arise from the collective behavior of many such neurons.

## Role in Whole-Brain Modeling

In [[whole-brain]] simulations, the Izhikevich model serves as a compromise between biophysical realism and computational efficiency. Unlike the Hodgkin-Huxley model, which requires solving four coupled differential equations per channel type with stiff numerical methods, the Izhikevich model integrates rapidly using standard ode solvers. This efficiency enables the construction of large-scale network models that incorporate node heterogeneity—which is critical for reproducing the diverse frequency content observed in empirical neuroimaging data.

Recent research published in 2026 has extended Izhikevich-style modeling to address whole-brain dynamics near critical synchronization. Myrov et al. demonstrated that hierarchical whole-brain models incorporating oscillator dynamics can reproduce critical-like dynamics marked by emergent long-range temporal correlations and structure-function coupling patterns resembling human MEG data [[semanticscholar-ce89e593c89e]]. These findings underscore the relevance of simplified spiking models for understanding brain-wide coordination.

Similarly, Gaglioti et al. applied neural mass models incorporating transitions between wake-like and sleep-like dynamics—generated through mechanisms analogous to those in the Izhikevich model—to study slow wave generation in brain lesions [[semanticscholar-cc2129666e15]]. Their work demonstrates how bifurcation analysis of simplified neuron models can inform our understanding of pathological states such as post-lesional slow waves, which represent intrusions of sleep-like activity into wakeful brain networks.

## Relationship to Other Neuron Models

The Izhikevich model occupies a middle ground in the spectrum of neural modeling approaches. Compared to the classic [[Hodgkin-Huxley model]], which was derived from the biophysics of ion channels in the squid giant axon and contains separate equations for sodium, potassium, and leak conductances, the Izhikevich model distills these dynamics into a minimal two-dimensional system. Compared to the leaky integrate-and-fire model, which resets instantaneously after each spike without accounting for recovery dynamics, the Izhikevich model captures adaptation and rebound phenomena through its recovery variable.

It is important to distinguish the Izhikevich model from other conductance-based approximations. The exponential integrate-and-fire (AdEx) model, available in simulators such as [[NEST]] and [[Brian2]], is a distinct formulation that uses exponential nonlinearity in the voltage equation rather than the quadratic term employed by Izhikevich [[izhikevich-2007]]. While both models can reproduce similar firing patterns, they arise from different mathematical structures and exhibit different bifurcation sequences.

## Computational Implementation

Major neural simulators support the Izhikevich model as a built-in neuron type. In [[Brian2]], the model is available as `Brian2.Izhikevich()` with parameters for *a*, *b*, *c*, and *d*. [[NEST]] provides the `izhikevich` neuron model as part of its standard library, optimized for spike-driven updates. [[NEURON]] users can implement the model through custom `MOD` files that define the differential equations and reset conditions.

For researchers conducting [[bifurcation analysis]] on the model, software packages such as AUTO-07P enable numerical continuation of equilibria and periodic orbits as parameters vary [[doedel-oldeman-2009]]. This approach has been particularly valuable for mapping the boundaries between different firing regimes and identifying parameter regions relevant to specific neural phenomena.

## Open Questions and Future Directions

Several open questions remain at the intersection of Izhikevich-style modeling and whole-brain dynamics. First, the relationship between single-neuron bifurcation parameters and population-level dynamics remains incompletely characterized—while we know that certain parameter regimes produce specific firing patterns, translating this knowledge into predictions about large-scale [[brain oscillations]] requires further development. Second, the role of parameter heterogeneity across neuronal populations in shaping network-level synchrony and frequency content is an active area of investigation.

Third, there is growing interest in embedding Izhikevich-style neurons within connectome-based models to study how structural topology interacts with intrinsic neuronal dynamics to produce observed patterns of [[brain oscillations]] and [[epilepsy modeling|seizure-like events]]. The simplified dynamics make exhaustive parameter exploration feasible, but bridging the gap between single-neuron bifurcations and emergent whole-brain behavior requires continued theoretical and computational effort.

## Related Concepts
* [[dynamical-systems-theory]]
* [[bifurcation theory]]
* [[nonlinear dynamics]]
* [[brain oscillations]]
* [[neural mass models]]
* [[spiking neural networks]]
* [[whole-brain modeling]]
* [[Hodgkin-Huxley model]]
* [[integrate-and-fire]]
* [[FitzHugh-Nagumo model]]
* [[epilepsy modeling]]
* [[Brian2]]
* [[NEST]]
* [[NEURON]]