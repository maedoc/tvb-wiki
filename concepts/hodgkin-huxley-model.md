---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-ce89e593c89e.md
- raw/papers/semanticscholar-71ffb8153870.md
- raw/papers/semanticscholar-cc2129666e15.md
tags:
- neural-mass-models
- computational-neuroscience
- ion-channel
- spiking-neural-networks
- dynamical-systems-theory
- bifurcation-theory
- stochastic-differential-equations
- whole-brain-modeling
- brain-oscillations
title: Hodgkin-Huxley Model
type: concept
updated: '2026-05-06'
---

The Hodgkin-Huxley model is a mathematical framework describing how [[action-potential]]s in [[neuron|neurons]] are generated and propagate along [[axon|axons]]. Proposed by Alan Hodgkin and Andrew Huxley in 1952, the model provides a biophysically grounded description of [[ion-channel]] dynamics using a system of coupled differential equations that capture the voltage-dependent gating of sodium (Na⁺) and potassium (K⁺) channels, alongside a leak conductance. The Hodgkin-Huxley formalism represents the foundational pillar upon which modern [[neural-mass-models]] and [[spiking-neural-networks]] are built, and it remains essential for understanding the cellular basis of large-scale [[brain-dynamics]] observed in [[neuroimaging-fmri]], [[neuroimaging-eeg]], and [[neuroimaging-meg]] data.

## Historical Context and Motivation

Prior to Hodgkin and Huxley's work, the nature of neuronal excitability was poorly understood. The pioneering experiments of Alan Hodgkin and Andrew Huxley, conducted at the Plymouth Marine Laboratory using the giant squid axon, provided the first quantitative description of the ionic currents underlying the action potential. Their 1952 papers established that the action potential results from transient, voltage-dependent increases in membrane conductance to Na⁺ and K⁺ ions, challenging the prevailing "calcium hypothesis" that attributed the spike to calcium influx. This work earned Huxley and Hodgkin the 1963 Nobel Prize in Physiology or Medicine and fundamentally shaped the [[trajectory]] of [[computational-neuroscience]].

The motivation for the model was to explain the quantitative relationship between membrane voltage and the ionic currents measured during voltage-clamp experiments. By fitting their equations to experimental data, Hodgkin and Huxley could reproduce the shape, threshold, and refractoriness of the action potential with striking accuracy—a feat that established a new standard for quantitative neuroscience. The model demonstrates that complex neural phenomena can emerge from the interaction of relatively simple molecular-level components, providing a template for multi-scale modeling that resonates with modern [[whole-brain-modeling]] approaches where regional [[neural-mass-model]]s are coupled through [[structural-connectivity]].

## Mathematical formalism

The core of the Hodgkin-Huxley model consists of a system of ordinary differential equations describing the evolution of membrane potential *V* and three gating variables *n*, *m*, and *h*, which represent the probability that the activation gate of the potassium channel is open (*n*), the activation gate of the sodium channel is open (*m*), and the inactivation gate of the sodium channel is open (*h*). The membrane equation takes the form:

$$C_m \frac{dV}{dt} = -g_{\text{Na}} m^3 h (V - E_{\text{Na}}) - g_{\text{K}} n^4 (V - E_{\text{K}}) - g_{\text{L}} (V - E_{\text{L}}) + I_{\text{ext}}$$

where *C*ₘ is the membrane capacitance, *g*ₙₐ, *g*ₖ, and *g*ₗ are the maximum conductances for sodium, potassium, and leak currents respectively, and *E*ₙₐ, *E*ₖ, and *E*ₗ are the corresponding reversal potentials. The gating variables evolve according to equations of the form:

$$\frac{dx}{dt} = \alpha_x(V)(1-x) - beta_x(V) x$$

where *x* ∈ {*n*, *m*, *h*} and *α* and *β* are voltage-dependent rate constants. The exponents 3 and 4 on the *m* and *n* variables reflect the cooperative gating of sodium and potassium channels—sodium channels require three activation gates to open simultaneously before conducting, while potassium channels require four.

This system exhibits rich [[nonlinear-dynamics]], including [[bifurcation-theory|bifurcations]] between resting and oscillatory states as parameters are varied, and it serves as a prototype for studying [[brain-oscillations]] and [[excitation-inhibition-balance]] at the single-neuron level. The model can be extended to include [[stochastic-differential-equations]] to capture the random opening and closing of ion channels at small membrane areas, which is particularly relevant for modeling [[noise]] in [[neural-mass-model|neural mass]] approximations used in [[whole-brain]] simulations.

## Relationship to Neural Mass Models and Whole-Brain Modeling

In [[whole-brain-modeling]], the Hodgkin-Huxley model serves as the microscopic foundation from which [[neural-mass-model]]s are derived. Neural mass models, such as the [[jansen-rit-model]] and the [[wong-wang-model]], simplify the collective dynamics of large neuronal populations by approximating the average membrane potentials and firing rates of excitatory and inhibitory pools. These models inherit key dynamical properties from their single-neuron constituents—including excitability, oscillations, and bistability—while enabling computationally tractable simulations of brain-scale networks coupled via [[connectome|structural connectivity]].

The 2026 work by Myrov et al. on [[hierarchical]] [[whole-brain]] models demonstrates how local synchronization dynamics, which have roots in the excitability properties described by Hodgkin-Huxley, give rise to long-range temporal correlations and interareal phase synchronization observed in [[meg]] data. Similarly, the computational models of human-derived neuronal networks studied by Barabino et al. and the slow wave generation models of Gaglioti et al. both build upon principles of neuronal excitability that trace back to the Hodgkin-Huxley formalism, extended to capture population-level bursting and [[brain-stimulation|propagation]] phenomena.

## Extensions and Software Implementation

The original Hodgkin-Huxley model has been extended in numerous ways to capture diverse neuronal dynamics. The [[izhikevich-neuron-model]] provides a reduced two-dimensional representation that can reproduce the firing patterns of multiple neuronal types with greater computational efficiency. The [[adaptive-exponential-integrate-and-fire]] model offers another simplified approach that captures spike-frequency adaptation and dynamic refractoriness. For detailed biophysical simulations, the [[brian2]] and [[neuron]] simulators provide flexible frameworks for implementing custom Hodgkin-Huxley-style channel dynamics, while [[nest]] offers efficient spiking network simulations at scale.

The [[neuroml]] standard provides a declarative format for specifying Hodgkin-Huxley-type channel models, facilitating model reuse and interoperability across simulators. [[neurodamus]] and [[tvb-nest]] exemplify efforts to bridge the gap between cellular-scale Hodgkin-Huxley models and [[whole-brain]] simulators like [[the-virtual-brain]], enabling multi-scale simulations where microscopic neuronal dynamics give rise to macroscopic brain-wide activity patterns measurable with [[fmri]] and [[eeg]].

## Related Concepts

The Hodgkin-Huxley model connects to several other foundational concepts in computational neuroscience. It provides the dynamical-systems-theoretic foundation for [[bifurcation-analysis]] of neuronal models, where transitions between resting states and repetitive spiking arise through [[andronov-hopf-bifurcation]] as applied to the voltage equation. The model also relates to [[mean-field-theory]], which provides the mathematical apparatus for aggregating millions of Hodgkin-Huxley-style neurons into population-level descriptions. The [[fokker-planck-equation]] provides a framework for describing the probability distribution of membrane states in the presence of stochastic channel noise, bridging the gap between deterministic Hodgkin-Huxley dynamics and the variability observed in real neurons.

## References

1. V. Myrov, A. Suleimanova, Samanta Knapič, P. Partanen, M. Vesterinen, Wenya Liu, S. Palva, J. M. Palva. (2026). *Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain.*. Proceedings of the National Academy of Sciences of the United States of America. [DOI](](https://doi.org/10.1073/pnas.2505768123))
2. Valerio Barabino, F. Callegari, Sérgio Martinoia, P. Massobrio. (2026). *Hierarchical afferent [[connectivity]] drives population-wide bursting dynamics in a computational model of human-derived excitatory neuronal networks*. Journal of Neuroscience. [DOI](](https://doi.org/10.1523/jneurosci.0912-25.2026))
3. Gianluca Gaglioti, L. Porta, M. Colombo, Simone Russo, Thierry Nieus, G. Deco, M. Corbetta, S. Sarasso, M. V. Sanchez-Vives, M. Massimini. (2026). *Slow wave generation and propagation in a model of brain lesions*. NeuroImage. [DOI](](https://doi.org/10.1016/j.neuroimage.2026.121817))