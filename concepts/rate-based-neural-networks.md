---
created: 2026-05-06
sources: []
tags:
- rate-based-neural-networks
- firing-rate
- mean-field
- population-dynamics
- neural-mass-model
title: Rate-Based Neural Networks
type: concept
updated: '2026-05-06'
---

# Rate-Based Neural Networks

**Rate-based neural networks** model neural populations by their average **firing rate** rather than tracking individual spikes. They are the theoretical foundation for [[neural-mass-models]] used in [[whole-brain]] simulation frameworks such as [[the-virtual-brain|TVB]].

## Overview

Rate-based models treat a population of neurons (typically 10³–10⁶ cells) as a single dynamical unit whose output is the instantaneous mean firing rate r(t). The core equation is:

$$\tau \frac{dr}{dt} = -r + f(I_{\text{syn}} + I_{\text{ext}})$$

where:
- τ is the membrane time constant
- f(·) is the input–output (activation) function (e.g., sigmoid, rectified [[linear]], or threshold-linear)
- I_syn is the recurrent synaptic input
- I_ext is external input

## Key Variants

| Variant | Dynamics | Application |
|---------|---------|-------------|
| **Wilson–Cowan** | Two-population excitatory/inhibitory | Neural oscillations, visual cortex |
| **Jansen–Rit** | Three-population pyramidal/SP/SS | Epilepsy, ERP generation |
| **Wong–Wang** | Two-population reduced decision making | Working memory, DMN |
| **Dynamic Mean Field (DMF)** | Rate + adaptation variable | Resting-state fMRI predictions |
| **Mean-Field / Neural Mass** | Generic rate equations | Whole-brain TVB simulations |

## Derivation from Spiking Networks

Under assumptions of (1) asynchronous irregular activity, (2) large populations, and (3) Poisson output statistics, the firing rate of a population can be related to its mean synaptic input via the **f–I curve** of the constituent neurons. This is formalised by:

- **Amit & Brunel (1997)** — mean-field theory for integrate-and-fire networks
- **Gerstner (2000)** — rate models from spiking [[neuron]] population dynamics
- **Fourcaud-Trocmé et al. (2003)** — response to fluctuating currents

## Rate vs. Spiking Representation

| Property | Rate-based | Spiking |
|----------|-----------|---------|
| Temporal resolution | ms–s | sub-ms |
| Computational cost | Low (ODEs on ~100 nodes) | High (10⁶+ point neurons) |
| Neural variability | Captured via noise terms | Intrinsic, natural |
| Action potentials | Abstracted | Explicit |
| Synaptic dynamics | Mean synaptic current | Individual post-synaptic potentials |
| Scaling | Entire brain (~10⁸ neurons in 68–1000 nodes) | Limited to local circuits |

## Relationship to TVB

TVB’s entire simulation engine is built on rate-based neural mass models:
- Every TVB **region node** is a rate-based population described by a neural mass model ([[jansen-rit-model]], [[wong-wang-model]], [[wilson-cowan-model]], etc.)
- **Coupling** between regions is rate-based: the firing rate of one node modulates the synaptic input to another
- **Stochastic integration** adds noise terms to capture variability abstracted away by the rate reduction
- TVB **can be extended** with spiking models via the [[co-simulation]] interface, but its default is rate-based

## Software

- **TVB** — neural mass / rate-based whole-brain simulation
- **[[neuroml2]]** — declarative format for neural models including rate-based
- **[[annarchy]]** — hybrid spiking/rate simulator
- **[[rockpool]]** — time-continuous rate and spiking network training

## Related

- [[spiking-neural-networks]] — complementary spiking-level description
- [[neural-mass-model]] — mathematical foundations
- [[mean-field-theory]] — statistical mechanics derivation
- [[co-simulation]] — bridging rate-based TVB with spiking microcircuits
- [[dynamic-causal-modeling]] — [[bayesian]] inversion of rate-based models

## References

- Wilson HR, Cowan JD (1972) — Excitatory and inhibitory interactions in localized populations of model neurons. Biophysical Journal 12(1): 1–24. https://doi.org/10.1016/S0006-3495(72)86068-5
- Jansen BH, Rit VG (1995) — Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. Biological Cybernetics 73(4): 357–366. https://doi.org/10.1007/BF00199471
- Deco G, Jirsa VK (2012) — Ongoing cortical activity at [[rest]]: criticality, multistability, and ghost attractors. Journal of Neuroscience 32(10): 3366–3375. https://doi.org/10.1523/JNEUROSCI.2523-11.2012
- Wong K-F, Wang X-J (2006) — A recurrent network mechanism of time integration in perceptual decisions. Journal of Neuroscience 26(4): 1314–1328. https://doi.org/10.1523/JNEUROSCI.3733-05.2006
- Amit DJ, Brunel N (1997) — Model of global [[spontaneous-activity]] and local structured activity during delay periods in the cerebral cortex. Cerebral Cortex 7(3): 237–252. https://doi.org/10.1093/cercor/7.3.237