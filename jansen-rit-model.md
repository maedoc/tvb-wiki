---
title: Jansen-Rit Model
created: 2025-01-15
updated: 2026-05-07
type: concept
tags: [neural-mass-models, neuroimaging-eeg, neuroimaging-meg, brain-oscillations, bifurcation-analysis, software-tvb, whole-brain-modeling, dynamic-causal-modeling]
sources: [raw/papers/jansen-rit-1995.md, raw/papers/arxiv-2411.16449.md, raw/papers/arxiv-2503.05564.md, raw/papers/rit-2013.md]
---

The Jansen-Rit model is a neural mass model of a cortical column that generates realistic electroencephalogram (EEG) and visual evoked potential (VEP) signals through the interaction of three neuronal populations. Introduced by Benjamin H. Jansen and Vincent G. Rit in their seminal 1995 paper[^1], the model has become a foundational tool in computational neuroscience for simulating mesoscopic brain activity. It now serves as the default neural mass model in [[the-virtual-brain]] for EEG and magnetoencephalography (MEG) forward simulations[^2], and appears as a key component in many [[whole-brain]] modeling pipelines that couple cortical columns via [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI)[^3].

## Motivation and Context

The development of the Jansen-Rit model addressed a fundamental challenge in computational neuroscience: how to bridge the gap between microscopic single-neuron dynamics and macroscopic electrophysiological signals measurable at the scalp. Earlier approaches, such as those developed by Lopes da Silva and colleagues, focused on thalamic-cortical loops but lacked a principled treatment of cortical column dynamics[^1]. The Jansen-Rit model provided a mathematically tractable yet biologically grounded representation of a cortical column that could reproduce key features of real EEG recordings, including alpha rhythms (8–12 Hz) and beta rhythms (13–30 Hz).

Neural mass models like Jansen-Rit occupy a crucial intermediate position between detailed [[spiking-neural-networks]] that simulate individual neurons and [[mean-field-theory]] approaches that average over large populations. By treating populations of neurons as discrete computational units with lumped parameters, the model achieves a favorable trade-off between computational tractability and biological realism. This makes it particularly suitable for [[whole-brain]] simulations where hundreds of cortical regions must be modeled in coupled formation[^2].

## Model Structure and Equations

The model consists of three interconnected neuronal populations arranged in a cortical column architecture. Population 1 comprises pyramidal cells (the primary output population), Population 2 consists of excitatory interneurons, and Population 3 contains inhibitory interneurons. Each population is characterized by a postsynaptic response function that models the average membrane potential response to incoming synaptic currents.

The dynamics are governed by the following equations, expressed in convolution form:

$$V_i(t) = \int_0^t h_i(t-\tau) \cdot S\left(\sum_{j} w_{ij} V_j(\tau) + \text{input}(t-\tau)\right) d\tau$$

where $V_i(t)$ represents the average membrane potential of population $i$, $h_i(t)$ is the postsynaptic impulse response function (typically modeled as an alpha function $h(t) = \alpha^2 t e^{-\alpha t}$), $w_{ij}$ is the synaptic weight from population $j$ to population $i$, and $S(\cdot)$ is a nonlinear activation function (typically a sigmoid function of the form $S(x) = \frac{1}{1 + e^{-r(x-\theta)}}$ where $r$ controls the slope and $\theta$ the threshold).

The connectivity architecture forms a feedback loop: pyramidal cells receive excitation from excitatory interneurons and project to both interneuron populations. The excitatory interneurons receive input from pyramidal cells and project back, forming a positive feedback loop. The inhibitory interneurons also receive input from pyramidal cells but provide negative feedback through GABAergic inhibition. This architecture generates oscillatory behavior through the interplay of excitation and inhibition, analogous to [[wilson-cowan-model]] formulations but with more biophysically motivated population structure[^1].

## Parameter Regimes and Oscillations

A remarkable feature of the Jansen-Rit model is its ability to generate multiple brain rhythms through parameter variation. The original 1995 paper demonstrated that varying the coupling strengths between populations could produce alpha (8–12 Hz) and beta (13–30 Hz) oscillations characteristic of scalp EEG[^1]. Subsequent research, including work by Mahdi, Sieber, and Tsaneva-Atanasova (2024), has shown that the model also supports delta oscillations (0.5–4 Hz) through a grazing bifurcation mechanism[^4].

In the delta regime, the excitatory activation thresholds are small and slopes are steep, making the model sensitive to small inputs. The transition between alpha and delta oscillations occurs when the minimum of the pyramidal cell output equals the threshold for switching off the excitatory interneuron population, leading to a collapse in excitatory feedback. This bifurcation analysis connects the model's dynamics to [[bifurcation-theory]] and provides a mathematical framework for understanding regime transitions in cortical oscillations[^4].

Beyond alpha and delta, the model exhibits beta rhythms (12–30 Hz), gamma oscillations (>30 Hz), and pathological dynamics resembling epileptiform activity when the ratio of inhibitory to excitatory gains falls outside physiological ranges[^2][^3]. The parameter space organized by bifurcation boundaries enables systematic exploration of transitions between health and disease states, a capability extensively exploited in clinical applications targeting epilepsy and other neurological disorders[^2].

## Implementation in The Virtual Brain

The Jansen-Rit model forms the default neural mass implementation in [[the-virtual-brain|TVB]], selected as the primary model for EEG and MEG simulation due to its proven ability to generate physiologically realistic signals and its favorable computational properties for large-scale simulations[^2]. TVB's implementation allows users to specify region-specific parameters, coupling functions, and connectivity matrices, enabling personalized brain modeling campaigns.

The computational efficiency of the model makes it suitable for whole-brain simulations where hundreds of cortical columns are coupled through structural connectivity matrices derived from diffusion tensor imaging. This pipeline—constructing whole-brain models by coupling multiple Jansen-Rit columns through empirically measured connectivity—has become a standard approach in the field[^2][^3]. The model's bifurcation structure has been characterized within TVB, providing users with guidance on parameter regimes that produce specific dynamical behaviors[^4].

## Relationship to Other Models

The Jansen-Rit model is closely related to several other neural mass formulations. It extends the earlier [[wilson-cowan-model]] by incorporating distinct population types and more detailed synaptic dynamics. Compared to the [[wong-wang-model]], another popular neural mass approach used in [[whole-brain]] modeling, Jansen-Rit emphasizes cortical column architecture and EEG generation more directly.

In the [[whole-brain-modeling]] ecosystem, Jansen-Rit competes with models such as [[epileptor]] (for seizure modeling) and the [[zerlaut]] model (for mean-field approximations). The TVB platform implements Jansen-Rit as a default option for [[forward-model]] computation of electrophysiological signals, enabling users to simulate source activity and compute [[volume-conduction]]-influenced scalp potentials[^2].

## Applications and Open Questions

Applications of the model span clinical and basic research domains. It serves as a forward model in [[dynamic-causal-modeling]] analyses of EEG and MEG data, supports [[epilepsy-modeling]] through extension to seizure-like dynamics, and provides the basis for [[effective-connectivity]] inference in studies of brain disorders[^2]. The model's relative computational efficiency makes it suitable for parameter sweep studies and [[bifurcation-analysis]] of brain dynamics.

Recent work by Pei (2025) has explored using genetic algorithms to optimize Jansen-Rit parameters for information encoding, demonstrating that phase-shifted oscillations across different parameter regimes can carry information about distinct inputs[^5]. This work opens new avenues for understanding how neural circuits can represent and process information through oscillatory dynamics.

Parameter estimation remains an open challenge, as the model's many free parameters (coupling strengths, time constants, thresholds) must be fitted to individual empirical data. Advances in optimization algorithms and increased computational power continue to improve the feasibility of patient-specific modeling approaches[^2][^5].

## References

[^1]: Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. *Biological Cybernetics*, 73(4), 357–366. https://doi.org/10.1007/bf00199471

[^2]: Ritter, P., & Schirner, M. (2013). The virtual brain: modeling biological brains. In *Critical Reviews in Biomedical Engineering*. (Discussion of TVB implementation and default model status).

[^3]: Weigenand, A., Schellenberger Costa, M., Ngo, H.-V. V., Claussen, J. C., & Martinetz, T. (2014). Characterization of the Takens-Bogdanov bifurcations in a model of cortical activity. *PLoS Computational Biology*, 10(9), e1003923. https://doi.org/10.1371/journal.pcbi.1003923

[^4]: Mahdi, H., Sieber, J., & Tsaneva-Atanasova, K. (2024). Alpha-delta transitions in cortical rhythms as grazing bifurcations. *arXiv preprint* arXiv:2411.16449. https://arxiv.org/abs/2411.16449

[^5]: Pei, A. (2025). Phase alignment enhances oscillatory power in neural mass models optimized for class encoding. *arXiv preprint* arXiv:2503.05564. https://arxiv.org/abs/2503.05564