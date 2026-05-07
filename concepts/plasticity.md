---
created: 2026-04-20
sources:
- Bliss1973
- BiPoo1998
- Bienenstock1982
- Oja1982
- Abbott2000
- Gerstner2002
- raw/papers/arxiv-2510.02545.md
- raw/papers/semanticscholar-3256c8880985.md
- raw/papers/arxiv-2512.03907.md
tags:
- synaptic-plasticity
- neural-mass-models
- whole-brain-modeling
- network-dynamics
- spiking-neural-networks
title: Plasticity
type: concept
updated: '2026-05-07'
---

## Overview

Plasticity refers to the brain's capacity to modify its structural and functional organization in response to experience, learning, and environmental change. In [[computational-neuroscience]], plasticity encompasses a family of mathematical models that describe how synaptic strengths change over time as a function of neural activity. These models are essential for understanding learning and memory, adaptation to injury, the formation and refinement of brain networks during development, and the pathological dynamics observed in conditions ranging from epilepsy to neurodegenerative diseases. Plasticity mechanisms operate across multiple timescales—from milliseconds for spike-timing-dependent plasticity to days or weeks for structural changes in dendrites and axons—and their computational representation is a cornerstone of any [[whole-brain-modeling]] framework.

## Biological Foundations

The nervous system exhibits plasticity at multiple organizational levels. At the synaptic level, the strength of connection between two neurons can be potentiated or depressed depending on the relative timing and frequency of their firing. The canonical biological signatures of this process are long-term potentiation (LTP), first characterized by Bliss and Lømo in 1973, and long-term depression (LTD), described shortly thereafter [Bliss1973]. LTP is typically induced by high-frequency stimulation of a presynaptic pathway and results in a lasting increase in synaptic efficacy, while LTD is induced by low-frequency stimulation and produces the opposite effect. These processes underlie much of what we understand about learning and memory at the cellular level.

Beyond synaptic changes, neurons can also modify their intrinsic electrophysiological properties—channel densities, thresholds, and firing rates—through homeostatic plasticity, which acts to stabilize neural circuits in the face of sustained activity changes. Structural plasticity involves the growth and retraction of axon terminals, dendritic spines, and even entire axonal projection patterns, occurring over days to weeks. In the context of [[whole-brain-modeling]], these slower plasticity mechanisms are particularly relevant for understanding how long-term changes in [[structural-connectivity]] emerge and how the brain rearranges itself following injury or in disease progression.

## Computational Models

### Spike-Timing-Dependent Plasticity

The most widely studied formulation in spiking network models is spike-timing-dependent plasticity (STDP), which posits that the change in synaptic weight depends on the temporal order of pre- and postsynaptic spikes. If the presynaptic spike precedes the postsynaptic spike within a temporal window of approximately 10–20 milliseconds, the synapse is potentiated; if the order is reversed, it is depressed [BiPoo1998]. The weight change $\Delta w$ is typically modeled as an exponential function:

$$\Delta w = \begin{cases} A_+ \exp(-\Delta t / \tau_+) & \text{if } \Delta t > 0 \\ -A_- \exp(\Delta t / \tau_-) & \text{if } \Delta t < 0 \end{cases}$$

where $\Delta t = t_{\text{post}} - t_{\text{pre}}$ is the time difference between postsynaptic and presynaptic spikes, $\tau_+$ and $\tau_-$ are time constants governing the temporal window (typically ~16 ms for potentiation and ~34 ms for depression), and $A_+$ and $A_-$ are learning rate parameters [Gerstner2002]. This rule captures the Hebbian principle that "neurons that fire together wire together" while adding a precise temporal asymmetry that has been verified experimentally in many brain regions.

### Rate-Based Plasticity

In [[neural-mass-model]] formulations where the fundamental unit is a population average rather than individual spikes, plasticity is typically modeled using rate-based rules. The BCM (Bienenstock-Cooper-Munro) rule is particularly influential [Bienenstock1982]:

$$\frac{dw}{dt} = \phi \cdot r_{\text{pre}} \cdot r_{\text{post}} \cdot (r_{\text{post}} - \theta)$$

where $\phi$ is a learning rate, $r_{\text{pre}}$ and $r_{\text{post}}$ are pre- and postsynaptic firing rates, and $\theta$ is a threshold that can itself be a sliding function of the average postsynaptic activity—this sliding threshold implements the homeostatic property that high recent activity reduces subsequent potentiation. The Oja rule provides another common formulation that includes a normalization term ensuring weights remain bounded [Oja1982]:

$$\frac{dw}{dt} = \eta \cdot r_{\text{pre}} \cdot r_{\text{post}} - \gamma \cdot w \cdot r_{\text{post}}^2$$

These rate-based formulations are computationally more tractable for large-scale [[brain-network]] simulations and are commonly employed in [[the-virtual-brain]] and similar [[whole-brain-simulators]].

## Role in Whole-Brain Modeling

Plasticity mechanisms are integrated into contemporary [[whole-brain-modeling]] frameworks through several pathways. In [[the-virtual-brain]], the default large-scale model uses a mix of [[neural-mass-model]] formulations (such as the [[jansen-rit-model]] or [[wong-wang-model]]) that can be equipped with plasticity rules to simulate learning and adaptation. Plasticity enables these models to move beyond stationary attractor states and exhibit temporally evolving dynamics that better capture the non-stationarity observed in empirical [[resting-state]] [[functional-connectivity]] data.

The integration of [[spiking-neural-networks]] with plasticity into whole-brain models remains computationally intensive but is an active research area. Simulators such as [[nest]] and [[brian2]] provide the low-level machinery for STDP implementation, and the TVB-NEST co-simulation framework enables coupling between population-level whole-brain models and detailed spiking networks where plasticity operates. This hybrid approach allows researchers to study how fine-grained synaptic changes propagate to macroscopic dynamics measurable with [[neuroimaging-fmri]] or [[neuroimaging-eeg]].

Beyond representing learning directly, plasticity in [[whole-brain]] models serves as a computational bridge between empirical observations at different scales. Synaptic weight changes inferred from STDP experiments in slice preparations can be mapped onto effective coupling parameters in mass models, allowing predictions about how repetitive activation patterns—whether endogenous (oscillatory states) or exogenous (stim protocols)—reshape large-scale network dynamics over time.

## Applications and Open Questions

Plasticity plays a central role in several applied modeling domains. In [[epilepsy-modeling]], homeostatic plasticity mechanisms are thought to contribute to the progression from interictal to ictal states, and seizure generation models like the [[epileptor]] can incorporate plasticity-like terms to reproduce ictal recruitment. Additionally, theoretical work connects plasticity to seizure threshold dynamics through the concept of excitatory-inhibitory recurrent loops that can become hyperexcitable when homeostatic mechanisms fail.

Several open questions remain. The relationship between synaptic-level STDP and macroscopic [[functional-connectivity]] changes observed over minutes to hours in [[fmri]] studies is poorly understood and represents a key gap in multi-scale modeling. [[parameter-estimation]] for plasticity rules in whole-brain models is challenging because the relevant empirical data often come from slice physiology or simplified paradigms that may not translate directly to the parameter regime of large-scale networks [Abbott2000]. Additionally, the interaction between different plasticity mechanisms—synaptic, homeostatic, and structural—operating simultaneously on different timescales remains theoretically and computationally complex.

## Related Concepts

Plasticity interacts with and depends on numerous other concepts in the [[whole-brain-modeling]] ecosystem. The [[excitation-inhibition-balance]] is intimately connected to plasticity, as homeostatic mechanisms regulate the relative strength of excitatory and inhibitory connections to maintain stable firing rates. The study of [[network-dynamics]] in plastic networks reveals emergent properties—such as stable learned states, metastable sequences, and critical dynamics—that are not present in static networks, connecting plasticity to the broader [[dynamical-systems-theory]] framework used to understand brain activity.

## References

1. Pascal Helson, Etienne Tanré, Romain Veltz. *[[mean-field-theory|Mean-field]] analysis of a [[neural-network]] with stochastic STDP*. [Link](https://arxiv.org/abs/2510.02545)
2. Duy Pham, Gene J. Yu, G. Lazzi, Jean-Marie C Bouteiller. (2026). *A spatially discretized convolutional [[neural-mass-models|neural mass model]] for studying meso-scale spatio-temporal transformations in the rat hippocampus*. Research Square. [DOI](https://doi.org/10.21203/rs.3.rs-9306977/v1)
3. Rosa Maria Delicado, Gemma Huguet, Pau Clusella. (2025). *Emergent Spatiotemporal Dynamics in Large-Scale Brain Networks with Next Generation Neural Mass Models*. [Link](https://arxiv.org/abs/2512.03907)