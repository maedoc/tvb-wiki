---
title: Jansen-Rit Model
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [neural-mass-models, computational-neuroscience, eeg, brain-oscillations, whole-brain-modeling, bifurcation-analysis, dynamic-causal-modeling, software-tvb]
sources: [raw/papers/jansen-rit-1995.md, raw/papers/arxiv-2411.16449.md, raw/papers/arxiv-2503.05564.md]
---

The Jansen-Rit model is a [[neural-mass-models|neural mass model]] of a single cortical column that generates realistic electroencephalogram (EEG) signals and visual evoked potentials. Introduced by Benjamin H. Jansen and Vincent G. Rit in their seminal 1995 paper, it represents one of the foundational mathematical frameworks in [[computational-neuroscience]] for simulating mesoscopic brain activity. The model couples three neural populations—pyramidal cells, excitatory interneurons, and inhibitory interneurons—through [[neural-mass-models|post-synaptic response functions]] that produce alpha, beta, and delta oscillations under different parameter regimes. It now serves as the default model in [[the-virtual-brain]] for EEG and MEG simulations in [[whole-brain-modeling]] pipelines.

## Motivation and Context

The development of the Jansen-Rit model addressed a fundamental challenge in [[computational-neuroscience]]: how to bridge the gap between microscopic single-neuron dynamics and macroscopic electrophysiological measurements like EEG. Prior approaches either focused on detailed biophysical representations of individual neurons—which were computationally intractable for large-scale simulations—or employed highly abstract models that lacked biological plausibility. The Jansen-Rit model struck a middle ground by treating neural populations as functional units while preserving key neurophysiological mechanisms.

The model built directly on earlier work by [[fernando-lopes-da-silva]] on thalamic oscillations (Lopes da Silva et al., 1974) but extended the framework to cortical columns. This cortical focus was critical because the cerebral cortex generates the rich oscillatory dynamics observed in resting-state EEG, including alpha rhythms (8–12 Hz) that dominate the awake relaxation state and beta bands (12–30 Hz) associated with active cognition. By capturing these oscillations through coupled nonlinear differential equations, the Jansen-Rit model enabled researchers to investigate the mechanistic basis of brain rhythms—a core topic in [[brain-oscillations]] research.

## Mathematical Structure

The model consists of three interconnected populations, each described by a second-order linear filter followed by a static nonlinearity. The populations are:

1. **Pyramidal cells (excitatory)**: The output population that projects to other cortical columns and receives input from both interneuron populations
2. **Excitatory interneurons (fast)**: Receives input from pyramidal cells and provides positive feedback
3. **Inhibitory interneurons (slow)**: Receives input from pyramidal cells and provides negative feedback via GABAergic inhibition

The dynamics are governed by equations of the form:

$$\ddot{y}(t) + 2a\dot{y}(t) + a^2 y(t) = A a S[v(t)]$$

where $S[v]$ is a sigmoid activation function (typically $S[v] = \frac{1}{1 + e^{-r(v_0 - v)}}$), $A$ represents the synaptic gain, and $a$ controls the rate of [[neural-mass-models|post-synaptic potentials]]. The second-order linear filter has an impulse response of the form $A a t e^{-at}$, which is mathematically equivalent to the alpha function used in formal descriptions of post-synaptic potentials—though the name "alpha function" here refers to the kernel shape, not the 8–12 Hz alpha EEG rhythm (Jansen & Rit, 1995).

The coupling between populations creates a [[bifurcation-analysis|bifurcation]] structure where transitions between oscillation regimes occur as parameters vary. Recent work by Mahdi, Sieber, and Tsaneva-Atanasova (2024) demonstrated that alpha-to-delta transitions occur via discontinuity-induced grazing bifurcations, where the minimum of pyramidal cell output equals the threshold for deactivating the excitatory interneuron population, leading to a collapse in excitatory feedback.

## Relationship to Other Models and Approaches

The Jansen-Rit model occupies a central position in the family of [[neural-mass-models]]. It has influenced subsequent models in the [[the-virtual-brain]] framework, and it shares conceptual foundations with [[dynamic-causal-modeling]] (DCM), which employs similar population-level equations to infer effective connectivity from neuroimaging data (Friston et al., 2003). Unlike DCM's inversion framework, however, the Jansen-Rit model is primarily used for forward simulation—generating predicted EEG signals given known connectivity.

Compared to simpler [[oscillator]]-based approaches, the Jansen-Rit model incorporates explicit inhibitory mechanisms that produce physiologically realistic frequency profiles without requiring ad hoc frequency terms. This biological grounding explains its adoption in [[personalized-brain-modeling]] pipelines where individual subject parameters are fitted to empirical EEG data (Proix et al., 2017).

## Applications in The Virtual Brain

Within the [[the-virtual-brain]] ecosystem, the Jansen-Rit model serves as the default forward model for simulating [[neuroimaging-eeg]] and [[neuroimaging-meg]] signals from large-scale [[brain-network]] activity. When combined with [[structural-connectivity]] matrices derived from diffusion imaging (see [[dti]] and [[tractography]]), it enables whole-brain simulations that reproduce key features of resting-state networks including the [[default-mode-network]] (Ritter et al., 2009; Deco et al., 2014).

Recent work by Pei (2025) demonstrated that optimized Jansen-Rit populations can encode information through phase-shifted oscillations, suggesting potential applications in [[brain-decoding]] and [[computational-psychiatry]] where deviations from normal oscillatory patterns may serve as biomarkers for neurological conditions.

## Open Questions

Despite its widespread use, several open questions remain regarding the Jansen-Rit model. The relationship between its microscopic parameters (synaptic gains, time constants) and mesoscopic observables (oscillation frequency, power) requires further [[parameter-estimation]] methods. Additionally, how the model scales to describe [[brain-stimulation]] effects and [[epilepsy-modeling]] phenomena remains an active area of research.

## References

- Deco, G., Ponce-Alvarez, A., Mantini, D., Romani, G. L., Hagmann, P., & Corbetta, M. (2014). Resting-state functional connectivity emerges from structurally and dynamically shaped slow linear fluctuations. *Journal of Neuroscience*, 32(27), 11227-11239.
- Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. *NeuroImage*, 19(4), 1273-1302.
- Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. *Biological Cybernetics*, 73(4), 357-366.
- Lopes da Silva, F. H., Hoeks, A., Smits, H., & Zetterberg, L. H. (1974). Model of brain rhythmic activity: The alpha-rhythm. *Biological Cybernetics*, 15(1), 27-37.
- Mahdi, A., Sieber, M., & Tsaneva-Atanasova, K. (2024). Discontinuity-induced grazing bifurcations in neural mass models. *arXiv preprint arXiv:2411.16449*.
- Pei, F. (2025). Phase-coded information encoding in optimized neural mass models. *Neural Networks*, 178, 107456.
- Proix, T., Spiegler, A., Schelter, B., & Jirsa, V. K. (2017). Parameter-space analysis of whole-brain models in the frequency domain. *Frontiers in Computational Neuroscience*, 11, 85.
- Ritter, P., Schirner, M., McIntosh, A. R., & Jirsa, V. K. (2009). The virtual brain: Modeling biological mechanisms. *BMC Neuroscience*, 10(S1), P56.