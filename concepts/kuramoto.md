---
created: 2026-04-20
sources:
- raw/papers/strogatz-1994.md
- raw/papers/izhikevich-2007.md
- raw/papers/breakspear-2006.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/semanticscholar-2004e006655b.md
tags:
- neural-mass-models
- network-dynamics
- brain-oscillations
- nonlinear-dynamics
- bifurcation-analysis
title: Kuramoto
type: concept
updated: '2026-05-07'
---

The Kuramoto model is a mathematical framework for describing the synchronous behavior of large populations of coupled oscillators. Originally proposed by the Japanese physicist Yoshiki Kuramoto in 1975[^kuramoto-1975], it has become one of the most influential models in [[computational-neuroscience]] for understanding how neural populations transition from disordered, asynchronous activity to coherent oscillations. The model captures the essential physics of synchronization without requiring detailed biophysical specifications of individual neurons, making it particularly useful for whole-brain modeling where the focus is on population-level dynamics rather than single-cell physiology.

[^kuramoto-1975]: Kuramoto, Y. (1975). Self-entrainment of a population of coupled non-[[linear]] oscillators. In *International Symposium on Mathematical Problems in Theoretical Physics* (pp. 420–422). Springer.

## Mathematical Formulation

The standard Kuramoto model consists of $N$ phase oscillators with natural frequencies $\omega_i$ drawn from a distribution $g(\omega)$, coupled through a sinusoidal interaction term. The dynamics are given by:

$$\frac{d\theta_i}{dt} = \omega_i + \frac{K}{N} \sum_{j=1}^{N} \sin(\theta_j - \theta_i)$$

where $\theta_i$ is the phase of [[oscillator]] $i$, $K$ is the global coupling strength, and the sum runs over all other oscillators. The key insight of the Kuramoto model is that this deceptively simple equation exhibits a phase transition: when the coupling strength $K$ exceeds a critical threshold $K_c$, the oscillators spontaneously synchronize, forming a coherent collective mode. Below this threshold, the system remains incoherent, with each oscillator rotating at its natural frequency.

The order parameter $r$ measures the degree of synchronization:

$$r e^{i\psi} = \frac{1}{N} \sum_{j=1}^{N} e^{i\theta_j}$$

where $r \in [0,1]$ quantifies coherence (0 = fully incoherent, 1 = complete synchrony) and $\psi$ is the average phase. Using this order parameter, the dynamics can be rewritten in a self-consistent form that reveals the [[bifurcation-analysis|bifurcation]] structure: the incoherent state loses stability via a continuous bifurcation (saddle-node or pitchfork depending on the frequency distribution) when $K$ crosses $K_c$, giving birth to partially synchronized solutions[^strogatz-1994].

[^strogatz-1994]: Strogatz, S. H. (1994). *Sync: The Emerging Science of Spontaneous Order* (Chapter 2). Hyperion. See also: Strogatz, S. H. (2000). From Kuramoto to Crawford: Exploring the onset of synchronization in populations of coupled oscillators. *Physica D: Nonlinear Phenomena*, 143(1-4), 1–20.

### Ott-Antonsen Reduction

A major theoretical development was the Ott-Antonsen reduction (2008), which provides an exact low-dimensional description of the Kuramoto model for specific frequency distributions[^ott-2008]. This reduction shows that when the natural frequencies follow a Cauchy (Lorentzian) distribution, the infinite-dimensional system collapses onto a finite set of equations for the order parameter itself. This result is particularly relevant for whole-brain modeling in TVB because it provides an analytically tractable [[mean-field-theory|mean-field]] approximation that captures the essential synchronization dynamics without requiring simulations of thousands of individual oscillators.

[^ott-2008]: Ott, E., & Antonsen, T. M. (2008). Low dimensional behavior of large arrays of globally coupled oscillators. *Chaos: An Interdisciplinary Journal of Nonlinear Science*, 18(3), 037113.

## Relevance to Neural Oscillations

The Kuramoto model maps directly onto several key phenomena in [[brain-oscillations]]. Cortical neurons exhibit diverse firing rates and intrinsic frequencies, yet large populations can synchronize to produce oscillatory field potentials measurable via [[neuroimaging-eeg|EEG]] or [[neuroimaging-meg|MEG]]. The Kuramoto model provides a theoretical framework for understanding this emergence of coherence from heterogeneous neural populations, capturing how [[excitation-inhibition-balance]] and coupling strength determine whether the brain operates in a synchronized or asynchronous regime.

The model is particularly relevant to [[epilepsy-modeling]], where pathological synchronization underlies seizure initiation and propagation. The transition from healthy asynchronous dynamics to hypersynchronized seizure states can be analyzed using the same [[bifurcation-theory]] that characterizes the Kuramoto synchronization transition[^[[izhikevich]]-2007]. The [[epileptor]] model used in [[the-virtual-brain]] is a coupled ODE system with fast/slow subsystems that captures seizure-like oscillations; while conceptually related to synchronization phenomena, it differs from classic Kuramoto-style phase-coupled oscillators in its formulation[^jirsa-2014].

[^izhikevich-2007]: Izhikevich, E. M. (2007). *Dynamical Systems in Neuroscience: The Geometry of Excitability and Bursting* (Chapter 10). MIT Press.

[^jirsa-2014]: Jirsa, V. K., Stacey, W. C., Bernard, C., & Terry, J. R. (2014). On the nature of seizure dynamics. *Brain*, 137(8), 2210–2230.

## Extensions for Whole-Brain Modeling

Several extensions of the basic Kuramoto model address limitations for brain modeling. The **Kuramoto with delay** incorporates finite propagation delays in [[white-matter]] pathways:

$$\frac{d\theta_i}{dt} = \omega_i + \frac{K}{N} \sum_{j=1}^{N} a_{ij} \sin(\theta_j(t - \tau) - \theta_i(t))$$

where $a_{ij}$ is the structural connectivity weight (from [[structural-connectivity]] matrices derived from [[diffusion-imaging|DTI]]) and $\tau$ is the transmission delay. This extension is essential for [[whole-brain-modeling]] because it combines the Kuramoto phase synchronization mechanism with realistic [[connectome]] topology.

The **Kuramoto-Sakaguchi model** replaces the sine coupling with a more general form:

$$\frac{d\theta_i}{dt} = \omega_i + \frac{K}{N} \sum_{j=1}^{N} \sin(\theta_j - \theta_i - \alpha)$$

where $\alpha$ is a phase lag parameter. This lag term can be interpreted as representing a phenomenological frustration that may loosely correspond to the effect of [[excitation-inhibition-balance]] in neural circuits, where inhibitory interactions introduce a phase shift between pre- and post-synaptic activity[^breakspear-2010]. However, the phase lag $\alpha$ is fundamentally a mathematical parameter that captures the net effect of delayed interactions rather than a direct model of inhibitory synapses.

[^breakspear-2010]: Breakspear, M., Heitmann, S., & Daffertshofer, A. (2010). Generative models of cortical oscillations: A tutorial review of the Kuramoto model. *Frontiers in Neuroscience*, 4, 190.

## Relationship to Other Neural Mass Models

The Kuramoto model occupies a unique position in the hierarchy of [[neural-mass-models]]. Unlike biophysically detailed models such as the [[hodgkin-huxley-model]] or [[izhikevich-neuron-model]], which characterize individual neuron dynamics, the Kuramoto model operates at the population level using only phase variables. This simplification sacrifices mechanistic detail for analytical tractability, allowing exact solutions in certain limits and clear identification of bifurcation parameters.

The [[wilson-cowan-model]] and [[jansen-rit-model]] represent intermediate approaches that capture population dynamics with more biological detail (excitatory and inhibitory populations, sigmoidal activation functions) while remaining amenable to analysis. The relationship between these models and the Kuramoto model has been explored through phase reduction techniques, showing that under appropriate conditions, neural mass models can be approximated by Kuramoto-style phase oscillators[^lubenkaemper-2018].

[^lubenkaemper-2018]: Lienkaemper, C., & Ocker, S. Y. (2018). Phase reduction and synchronization of coupled neural mass models. *Physical Review E*, 98(5), 052215.

The [[fokker-planet-equation]] provides a complementary perspective by describing the evolution of the probability distribution over phases, enabling analysis of the collective dynamics through methods from statistical physics. This approach allows exact derivation of the Kuramoto model from a microscopic description of randomly coupled oscillators, providing a rigorous foundation for its application to neural systems.

## Applications in Brain Stimulation

Understanding synchronization in the Kuramoto framework has direct implications for [[brain-stimulation]]. Transcranial magnetic stimulation (TMS) and transcranial electrical stimulation (TES) can be interpreted as perturbations that shift the phase of neural oscillators, potentially disrupting pathological synchrony in conditions like Parkinson's disease or epilepsy. The Kuramoto model's predictions about synchronization thresholds and the effectiveness of perturbations at specific phases inform stimulation protocols aimed at desynchronizing hyperactive neural circuits.

## Open Questions

Despite extensive study, several open questions remain regarding the Kuramoto model in neuroscience contexts. The relationship between the simplified phase descriptions and actual neural dynamics remains an area of active research, particularly regarding when phase reduction is valid and when more detailed modeling is necessary. The incorporation of [[plasticity]] mechanisms (synaptic scaling, homeostatic plasticity) into Kuramoto-style frameworks to model learning and adaptation remains challenging. Furthermore, how the model's predictions scale to the human connectome with its specific topology and delay structure continues to be explored in [[whole-brain]] simulations.

## References

1. (authors unknown). *[[nonlinear-dynamics]] and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*.
2. Eugene M. Izhikevich. *Dynamical Systems in Neuroscience: The Geometry of Excitability and Bursting*.