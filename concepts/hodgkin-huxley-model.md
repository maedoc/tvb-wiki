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
updated: '2026-05-07'
---

The Hodgkin-Huxley model is a mathematical framework describing how action-potentials in [[neuron|neurons]] are generated and propagate along axons. Proposed by Alan Hodgkin and Andrew Huxley in 1952, the model provides a biophysically grounded description of [[ion-channel]] dynamics using a system of coupled differential equations that capture the voltage-dependent gating of sodium (Na⁺) and potassium (K⁺) channels, alongside a leak conductance. The Hodgkin-Huxley formalism represents the foundational pillar upon which modern [[neural-mass-models]] and [[spiking-neural-networks]] are built, and it remains essential for understanding the cellular basis of large-scale [[brain-dynamics]] observed in [[neuroimaging-fmri]], [[neuroimaging-eeg]], and [[neuroimaging-meg]] data.

## Historical Context and Motivation

Prior to Hodgkin and Huxley's work, the nature of neuronal excitability was poorly understood. The pioneering experiments of Alan Hodgkin and Andrew Huxley, conducted at the Plymouth Marine Laboratory using the giant squid axon, provided the first quantitative description of the ionic currents underlying the action potential (Hodgkin & Huxley, 1952). Their work established that the action potential results from transient, voltage-dependent increases in membrane conductance to Na⁺ and K⁺ ions, building on the earlier suggestion by Katz and others that ionic currents might underlie excitability. This breakthrough earned Hodgkin and Huxley the 1963 Nobel Prize in Physiology or Medicine and fundamentally shaped the [[trajectory]] of [[computational-neuroscience]].

The motivation for the model was to explain the quantitative relationship between membrane voltage and the ionic currents measured during voltage-clamp experiments (Cole, 1949; Hodgkin et al., 1952). By fitting their equations to experimental data, Hodgkin and Huxley could reproduce the shape, threshold, and refractoriness of the action potential with striking accuracy—a feat that established a new standard for quantitative neuroscience. The model demonstrates that complex neural phenomena can emerge from the interaction of relatively simple molecular-level components, providing a template for multi-scale modeling that resonates with modern [[whole-brain-modeling]] approaches where regional [[neural-mass-model]]s are coupled through [[structural-connectivity]].

## Mathematical formalism

The core of the Hodgkin-Huxley model consists of a system of ordinary differential equations describing the evolution of membrane potential *V* and three gating variables *n*, *m*, and *h*, which represent the probability that the activation gate of the potassium channel is open (*n*), the activation gate of the sodium channel is open (*m*), and the inactivation gate of the sodium channel is open (*h*). The membrane equation takes the form:

$$C_m \frac{dV}{dt} = -g_{\text{Na}} m^3 h (V - E_{\text{Na}}) - g_{\text{K}} n^4 (V - E_{\text{K}}) - g_{\text{L}} (V - E_{\text{L}}) + I_{\text{ext}}$$

where *C*ₘ is the membrane capacitance, *g*ₙₐ, *g*ₖ, and *g*ₗ are the maximum conductances for sodium, potassium, and leak currents respectively, and *E*ₙₐ, *E*ₖ, and *E*ₗ are the corresponding reversal potentials. The gating variables evolve according to equations of the form:

$$\frac{dx}{dt} = \alpha_x(V)(1-x) - beta_x(V) x$$

where *x* ∈ {*n*, *m*, *h*} and *α* and *β* are voltage-dependent rate constants.

The exponents 3 and 4 on the *m* and *n* variables were chosen by Hodgkin and Huxley empirically to provide the best fit to their voltage-clamp data; they do not correspond to literal molecular gate structures that were unknown at the time (Hodgkin & Huxley, 1952). The interpretation of *m*³*h* as "three activation gates and one inactivation gate" reflects the mathematical convenience of the m³h formalism rather than structurally identified components. The actual structural biology of sodium channels (four repeat domains, each contributing a voltage sensor) and potassium channels (four separate subunits) was determined decades later through molecular biology and crystallography.

This system exhibits rich [[nonlinear-dynamics]], including [[bifurcation-theory|bifurcations]] between resting and oscillatory states as parameters are varied, and it serves as a prototype for studying [[brain-oscillations]] and [[excitation-inhibition-balance]] at the single-neuron level. The model can be extended to include [[stochastic-differential-equations]] to capture the random opening and closing of ion channels at small membrane areas, which is particularly relevant for modeling noise in [[neural-mass-model|neural mass]] approximations used in [[whole-brain]] simulations.

## Relationship to Neural Mass Models and Whole-Brain Modeling

In [[whole-brain-modeling]], the Hodgkin-Huxley model serves as the microscopic foundation from which [[neural-mass-model]]s are derived. Neural mass models, such as the [[jansen-rit-model]] and [[wong-wang-model]], simplify the collective dynamics of large neuronal populations by approximating the average membrane potentials and firing rates of excitatory and inhibitory pools. These models inherit key dynamical properties from their single-neuron constituents—including excitability, oscillations, and bistability—while enabling computationally tractable simulations of brain-scale networks coupled via [[connectome|structural connectivity]].

The 2026 work by Myrov et al. on hierarchical [[whole-brain]] models demonstrates how local synchronization dynamics, which have roots in the excitability properties described by Hodgkin-Huxley, give rise to long-range temporal correlations and interareal phase synchronization observed in [[meg]] data (Myrov et al., 2026). Similarly, the computational models of human-derived neuronal networks studied by Barabino et al. and the slow wave generation models of Gaglioti et al. build upon principles of neuronal excitability that trace back to the Hodgkin-Huxley formalism, extended to capture population-level bursting and [[brain-stimulation|propagation]] phenomena (Barabino et al., 2026; Gaglioti et al., 2026).

## Reduced Models and Descendants

The Hodgkin-Huxley model has inspired numerous reduced formulations that preserve essential dynamical features while simplifying computational requirements. The [[fitzhugh-nagumo-model]] reduces the four-dimensional HH system to two dimensions by combining the fast sodium dynamics into a single variable while retaining the qualitative behavior of excitation and oscillations. The [[morris-lecar-model]] provides another two-dimensional reduction that captures the essential calcium and potassium dynamics relevant for bursting and plateau potentials. The [[integrate-and-fire]] family of models, including the [[izhikevich-neuron-model]] and the [[adaptive-exponential-integrate-and-fire]] model, offer yet further simplifications that maintain spike generation properties suitable for large-scale network simulations (Izhikevich, 2003).

These reduced models are particularly relevant for the TVB/whole-brain ecosystem, where computational tractability across thousands of brain regions necessitates simplified neuronal dynamics while still preserving the bifurcation structure that gives rise to oscillations, transitions between up and down states, and pathological epileptiform activity.

## Extensions and Software Implementation

The original Hodgkin-Huxley model has been extended in numerous ways to capture diverse neuronal dynamics. The [[izhikevich-neuron-model]] provides a reduced two-dimensional representation that can reproduce the firing patterns of multiple neuronal types with greater computational efficiency. The [[adaptive-exponential-integrate-and-fire]] model offers another simplified approach that captures spike-frequency adaptation and dynamic refractoriness. For detailed biophysical simulations, the [[brian2]] and [[neuron]] simulators provide flexible frameworks for implementing custom Hodgkin-Huxley-style channel dynamics, while [[nest]] offers efficient spiking network simulations at scale.

The [[neuroml]] standard provides a declarative format for specifying Hodgkin-Huxley-type channel models, facilitating model reuse and interoperability across simulators. [[neurodamus]] and [[tvb-nest]] exemplify efforts to bridge the gap between cellular-scale Hodgkin-Huxley models and [[whole-brain]] simulators like [[the-virtual-brain]], enabling multi-scale simulations where microscopic neuronal dynamics give rise to macroscopic brain-wide activity patterns measurable with [[fmri]] and [[eeg]].

## Related Concepts

The Hodgkin-Huxley model connects to several other foundational concepts in computational neuroscience. It provides the dynamical-systems-theoretic foundation for [[bifurcation-analysis]] of neuronal models, where transitions between resting states and repetitive spiking arise through [[andronov-hopf-bifurcation]] as applied to the voltage equation. The model also relates to [[mean-field-theory]], which provides the mathematical apparatus for aggregating millions of Hodgkin-Huxley-style neurons into population-level descriptions. The [[fokker-planck-equation]] provides a framework for describing the probability distribution of membrane states in the presence of stochastic channel noise, bridging the gap between deterministic Hodgkin-Huxley dynamics and the variability observed in real neurons.

## References

- Barabino, V., Callegari, F., Martinoia, S., & Massobrio, P. (2026). Hierarchical afferent [[connectivity]] drives population-wide bursting dynamics in a computational model of human-derived excitatory neuronal networks. *Journal of Neuroscience*. https://doi.org/10.1523/jneurosci.0912-25.2026
- Cole, K. S. (1949). Letter to Alan Hodgkin et al. In: *The Significant Contribution of Kenneth S. Cole to the Development of the Voltage Clamp*. Archives of the Society for the Study of Evolution and of the History of Science.
- Gaglioti, G., Porta, L., Colombo, M., Russo, S., Nieus, T., Deco, G., Corbetta, M., Sarasso, S., & Massimini, M. (2026). Slow wave generation and propagation in a model of brain lesions. *NeuroImage*. https://doi.org/10.1016/j.neuroimage.2026.121817
- Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544.
- [[izhikevich]], E. M. (2003). Simple model of spiking neurons. *IEEE Transactions on Neural Networks*, 14(6), 1569–1572.
- Myrov, V., Suleimanova, A., Knapič, S., Partanen, P., Vesterinen, M., Liu, W., Palva, S., & Palva, J. M. (2026). Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.2505768123