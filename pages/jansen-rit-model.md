---
title: Jansen-Rit Model
created: 2025-01-15
updated: 2026-05-07
type: concept
tags: [neural-mass-models, computational-neuroscience, neuroimaging-eeg, brain-oscillations, whole-brain-modeling, bifurcation-analysis, parameter-estimation]
sources: [raw/papers/jansen-rit-1995.md, raw/papers/arxiv-2411.16449.md, raw/papers/arxiv-2503.05564.md]
---

The Jansen-Rit model is a seminal [[neural-mass-model]] of a cortical column that generates realistic electroencephalogram (EEG) signals and visual evoked potentials (VEPs). Originally published by Benjamin H. Jansen and Vincent G. Rit in 1995 [1], it represents one of the most influential mathematical formulations in [[computational-neuroscience]] for simulating large-scale brain activity. The model couples three neuronal populations—pyramidal cells, excitatory interneurons, and inhibitory interneurons—through nonlinear dynamics that produce oscillations primarily in the alpha (8–12 Hz) frequency band, with transitions to delta (0.5–4 Hz) under specific parameter regimes [2]. Its analytical tractability and ability to reproduce experimentally observed rhythms have made it the default neural mass implementation in [[The Virtual Brain]] for EEG and magnetoencephalography (MEG) forward simulations.

## Biological Motivation and Context

The development of the Jansen-Rit model addressed a fundamental challenge in neuroscience: how to bridge the gap between microscopic neuronal activity and macroscopic brain signals observable through EEG and MEG. At the time of its publication, individual neuron models (such as the [[hodgkin-huxley-model]]) could capture detailed biophysics but were computationally intractable for simulating whole cortical regions, while simpler phenomenological models lacked biological grounding. The Jansen-Rit model struck a pragmatic balance by treating populations of neurons as aggregate units while retaining key biological mechanisms—excitatory and inhibitory synaptic interactions, membrane time constants, and axonal transmission delays [1].

The model builds directly on earlier work by Fernando Lopes da Silva, who developed thalamic models of EEG generation, but extends this framework to the cortical column level. This shift was significant because it allowed researchers to investigate cortical contributions to brain rhythms independently of thalamic input, while still permitting coupling between multiple cortical columns for larger-scale simulations.

## Mathematical Formulation

The Jansen-Rit model consists of three interconnected populations, each described by second-order ordinary differential equations representing distinct excitatory and inhibitory postsynaptic potential (PSP) kernels. The key innovation is the use of **different** parameters for excitatory and inhibitory synapses:

### Excitatory Postsynaptic Potential Kernel

$$h_e(t) = A a \cdot t \cdot e^{-a t}$$

where $A$ is the excitatory synaptic gain and $a$ is the inverse excitatory time constant.

### Inhibitory Postsynaptic Potential Kernel

$$h_i(t) = B b \cdot t \cdot e^{-b t}$$

where $B$ is the inhibitory synaptic gain and $b$ is the inverse inhibitory time constant.

By default, $A = a$ and $B = b$, giving symmetric kinetics, but the model permits independent variation of these parameters to capture the faster inhibitory GABAergic dynamics relative to slower glutamatergic excitation [1].

The full system equations for population $i$ take the form:

$$\frac{d^2 y_i}{dt^2} + (a+b) \frac{dy_i}{dt} + ab y_i = ab \cdot S\left[\sum_{j} w_{ji} y_j(t - \tau_{ji})\right]$$

where $y_i$ represents the average membrane potential of population $i$, $a$ and $b$ are thePSP kernel time constants (using excitatory $a$ and inhibitory $b$ for excitatory populations, or inverted for inhibitory), $w_{ji}$ is the connection weight from population $j$ to $i$, $\tau_{ji}$ is the axonal transmission delay, and $S[\cdot]$ is a nonlinear sigmoid function that converts membrane potentials to firing rates [1].

The three populations in the model serve distinct computational roles. Pyramidal cells (Population 1) receive excitatory input from both interneuron populations and project to both, establishing recurrent excitation that can support oscillations. Excitatory interneurons (Population 2) receive input from pyramidal cells and provide fast, glutamatergic feedback that modulates the excitatory drive. Inhibitory interneurons (Population 3) receive input from pyramidal cells and provide slower, GABAergic inhibition that modulates the overall excitation-inhibition balance—crucial for generating alpha rhythms and preventing runaway excitation.

The output of the model is typically taken as the mean activity of the pyramidal cell population, which approximates the local field potential and thus the EEG signal measurable at the scalp.

## Relationship to Other Models

The Jansen-Rit model occupies a central position in the ecosystem of [[neural-mass-models]], serving as a foundation upon which numerous extensions and variations have been built. The [[wilson-cowan-model]] precedes it and provides a simpler two-population (excitatory-inhibitory) framework that captures similar dynamics but with less anatomical specificity. The [[wong-wang-model]] emerged later, incorporating more detailed mean-field theory and enabling investigations of decision-making and working memory. The [[epileptor]] model, used extensively in [[epilepsy-modeling]] within TVB, builds on Jansen-Rit-style dynamics but adds fast-slow subsystem coupling to reproduce seizure-like bursts [3].

The model's architecture is closely related to the concept of [[excitation-inhibition-balance]], a fundamental principle in neuroscience explaining how cortical circuits maintain stable firing rates despite massive excitatory drive. By tuning the relative gains of excitatory and inhibitory populations, the Jansen-Rit model can transition between different dynamical regimes—stable fixed points, limit cycles (oscillations), and chaotic behavior—much like the [[van-der-pol-oscillator]] or [[kuramoto]] models in other domains. The 2024 analysis by Mahdi, Sieber, and Tsaneva-Atanasova identified these transitions as discontinuity-induced grazing bifurcations, where the minimum of the pyramidal cell output reaches the threshold for switching off the excitatory interneuron population [2].

## Applications in Whole-Brain Modeling

In the context of [[whole-brain-modeling]], the Jansen-Rit model serves as the default columnar model in [[The Virtual Brain]] (TVB). When combined with [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI) or probabilistic tractography, multiple Jansen-Rit columns can be coupled to form large-scale brain networks capable of reproducing resting-state dynamics, including [[default-mode-network]] activity and [[brain-oscillations]] in the alpha band [3].

The TVB implementation treats each brain region (as defined by a [[brain-parcellation]] such as the [[desikan-killiany-atlas]] or [[schaefer-atlas]]) as a Jansen-Rit column, with connection weights and delays specified by empirical [[connectivity]] data. This framework has been used extensively for personalized brain modeling, where individual structural connectivity is combined with parameter estimation techniques to fit models to individual subject's EEG or fMRI data. Such personalization is crucial for clinical applications in [[epilepsy-modeling]], [[alzheimers-modeling]], and [[brain-stimulation]] targeting [3].

Recent work has explored bifurcation analysis of the Jansen-Rit model, identifying how transitions between brain states (such as alpha to delta oscillations) correspond to qualitative changes in the system's dynamics. This analysis connects the model to the broader framework of [[bifurcation-theory]] and [[dynamical-systems-theory]], enabling principled investigation of brain state transitions [2].

## Parameter Estimation and Optimization

A significant challenge in using the Jansen-Rit model for personalized applications is the estimation of its free parameters—synaptic gains, time constants, and connection weights—from empirical data. Various approaches have been employed, including variational Bayes, evolutionary algorithms, and more recently, machine learning optimization. The 2025 work by Pei demonstrated that genetic algorithms could optimize Jansen-Rit parameters to maximize phase differences between responses to different input classes, enabling the model to function as an information encoder where oscillatory phase carries semantic content [4]. This work suggests the model's relevance extends beyond passive signal generation to active computational roles in [[neural-network]] information processing.

The default parameters in TVB's implementation produce alpha oscillations around 10 Hz with realistic waveform morphology, but the model is highly sensitive to parameter changes—a small variation in excitation-inhibition balance can shift the system from alpha dominance to delta dominance or even to pathological states relevant for [[epilepsy-modeling]] [1][2].

## Open Questions and Future Directions

Despite its widespread adoption, the Jansen-Rit model faces several limitations that motivate ongoing research. The assumption of homogeneous populations within each column ignores the substantial diversity of cortical neuron types. The use of simple sigmoidal activation functions neglects the detailed channel kinetics captured in models like [[izhikevich]] or [[adaptive-exponential-integrate-and-fire]]. The lack of explicit dendrites, spines, or synaptic plasticity mechanisms limits its utility for studying learning and development.

Future directions include integration with [[spiking-neural-networks]] for multi-scale modeling, incorporation of neuromodulatory effects (dopamine, acetylcholine) that modulate gain parameters, and extension to include slow oscillations and up-down states relevant for sleep and [[consciousness-models]]. The model's analytical tractability continues to make it a valuable tool for understanding fundamental principles of brain dynamics even as more biophysically detailed alternatives emerge.

---

## References

1. Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a stochastic neural network model. *Biological Cybernetics*, 73(4), 357–365. https://doi.org/10.1007/BF00199472

2. Mahdi, A., Sieber, M., & Tsaneva-Atanasova, K. (2024). Discontinuity-induced bifurcations in a neural mass model. *arXiv preprint* arXiv:2411.16449.

3. The Virtual Brain. (n.d.). Neural mass model documentation. Retrieved from https://www.thevirtualbrain.org

4. Pei, A. (2025). Genetic algorithm optimization of Jansen-Rit parameters for phase-based information encoding. *arXiv preprint* arXiv:2503.05564.