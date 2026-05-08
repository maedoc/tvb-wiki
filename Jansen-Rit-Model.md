---
title: Jansen-Rit Model
created: 2026-04-20
updated: 2026-05-08
type: concept
tags: [neural-mass-models, neuroimaging-eeg, neuroimaging-meg, brain-oscillations, bifurcation-analysis, computational-neuroscience, software-tvb, excitation-inhibition-balance]
sources: [raw/papers/jansen-rit-1995.md, raw/papers/arxiv-2411.16449.md, raw/papers/arxiv-2503.05564.md]
---

The Jansen-Rit model is a neural mass model of a single cortical column that generates realistic electroencephalogram (EEG) signals and visual evoked potentials (VEPs). Originally published by Benjamin H. Jansen and Vincent G. Rit in 1995 [1], the model couples three neural populations—pyramidal cells, excitatory interneurons, and inhibitory interneurons—through post-synaptic impulse response functions. It has become a widely-used neural mass model in [[the-virtual-brain]] (TVB) [2] for simulating macroscopic brain activity including alpha, beta, and gamma rhythms. The model's mathematical simplicity combined with its ability to reproduce physiologically plausible oscillations makes it a cornerstone of whole-brain modeling and a key building block for connectome-based simulations.

## Motivation and Historical Context

The development of the Jansen-Rit model addressed a fundamental challenge in computational neuroscience: how to generate biologically realistic macroscopic brain signals from tractable mathematical descriptions. Prior approaches either focused on detailed spiking neuron networks—which were computationally expensive and difficult to parameterize for large-scale simulations—or relied on overly simplified phenomenological oscillators that lacked neurobiological grounding. Jansen and Rit drew on earlier work by Lopes da Silva and colleagues [1], who developed models of thalamic oscillations, but adapted the framework to cortical columns where the interplay between excitatory pyramidal cells and two distinct interneuron populations could produce the full spectrum of spontaneous EEG rhythms observed in empirical data.

The model's significance extends beyond its original application to VEP generation. It established a template for neural mass modeling that balances mathematical tractability with biological plausibility, influencing subsequent models including the [[wong-wang-model]] and various implementations in [[dynamic-causal-modeling]] (DCM). The Jansen-Rit model's success in reproducing alpha rhythms (~10 Hz) and beta oscillations (~20 Hz) through parameter variation demonstrated that the spectral properties of macroscopic brain activity could emerge from population-level interactions without requiring explicit frequency-setting mechanisms.

## Model Architecture and Mathematics

The Jansen-Rit model describes a cortical column as three coupled populations, each characterized by a static nonlinearity (sigmoid function) followed by a linear temporal filter representing postsynaptic integration. The populations are organized hierarchically: pyramidal cells receive input from interneurons and project back to both excitatory and inhibitory interneurons, while both interneuron types receive input from pyramidal cells and provide feedback inhibition or excitation respectively.

The model equations take the form of a second-order linear system with a sigmoidal nonlinearity applied to the summed inputs. Each population j receives input from other populations i through connection weights C_{ij}, transformed by a sigmoid function S(v) = 2e1 / (1 + e^r(v0 - v)) where e1 controls the maximum firing rate, r determines the slope of the activation function, and v0 sets the threshold. The output of each population passes through a temporal filter h(t) = (αβ / (β - α)) (e^{-αt} - e^{-βt}) representing postsynaptic potentials with characteristic rise time α and decay time β. This filter produces the classic alpha-shaped postsynaptic response that gives the model its name.

The complete system can be expressed as a set of coupled differential equations where the state variables represent the average membrane potentials and their derivatives for each population. The output of the pyramidal population—typically interpreted as the EEG signal recorded at the scalp—emerges from the collective dynamics of these three interacting populations. Parameter estimation typically focuses on the connection weights between populations (C_{12}, C_{21}, C_{13}, C_{31}, C_{23}, C_{32}) and the synaptic time constants, with variations in these parameters producing qualitatively different oscillatory regimes.

## Bifurcation Dynamics and Transitions

A key feature of the Jansen-Rit model is its rich dynamical repertoire, which includes multiple oscillatory regimes accessible through parameter variation. Recent theoretical work [3] has analyzed the transitions between alpha (8-12 Hz) and delta (0.5-4 Hz) oscillations as discontinuity-induced grazing bifurcations. In this regime, the excitatory activation thresholds in the model are small and slopes are steep, making a singular limit where the sigmoid function is replaced by a Heaviside step function appropriate for analysis. At the grazing bifurcation, the minimum of the pyramidal cell output equals the threshold for switching off the excitatory interneuron population, leading to a collapse in excitatory feedback and a qualitative shift in oscillation frequency and waveform morphology.

This bifurcation analysis connects the Jansen-Rit model to the broader framework of [[bifurcation-theory]] in dynamical systems, revealing why the model produces such realistic-looking EEG-like oscillations: the underlying mechanism involves threshold-induced switching dynamics that mirror the all-or-none firing of real neurons. The model thus provides a bridge between microscopic neural dynamics and macroscopic brain rhythms, capturing the functional consequences of excitation-inhibition balance in cortical circuits.

## Relationship to Whole-Brain Modeling

In the context of [[whole-brain modeling]], the Jansen-Rit model serves as the fundamental unit of cortex in TVB's simulation engine. TVB implements the Jansen-Rit model at each region of a cortical parcellation, coupling them through empirical [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI) tractography. The resulting large-scale model can generate resting-state networks, simulate the propagation of seizure-like activity, and predict the effects of brain stimulation interventions.

The model's computational efficiency—requiring only a handful of differential equations per brain region—makes it feasible to simulate hundreds of regions at millisecond resolution across tens of seconds of simulated time. This tractability comes with trade-offs: the model averages over millions of neurons in each population, losing details of single-neuron dynamics that more detailed approaches like [[spiking-neural-networks]] (implemented in [[nest]] or [[brian2]]) can capture. For many whole-brain applications requiring only the spectral properties of brain activity, this trade-off is acceptable, and the Jansen-Rit model remains the workhorse of TVB-based research.

## Extensions and Related Models

The success of the Jansen-Rit model inspired numerous extensions. The [[wong-wang-model]] introduced a finer distinction between excitatory and inhibitory subpopulations for modeling resting-state networks. The Epileptor model, used for seizure modeling in TVB, extends the Jansen-Rit framework with additional populations capable of producing ictal (seizure) and interictal (between-seizure) dynamics. In [[dynamic-causal-modeling]], the Jansen-Rit model underlies the neural mass model (NMM) option for inverting models of task-related brain activity using variational Bayes inference.

Recent work [4] has explored optimizing Jansen-Rit parameters for information encoding, demonstrating that phase-shifted oscillations across population inputs can be decoded from oscillatory power. This suggests potential applications in brain-computer interfaces and neuromorphic computing, where the model's dynamical properties could be exploited for temporal pattern recognition. The model also serves as a testbed for parameter estimation algorithms, including adaptive MCMC methods and evolutionary strategies, given its relatively low dimensional parameter space and well-characterized output space.

## References

[1] Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. *Biological Cybernetics*, 73(1), 35-45. https://doi.org/10.1007/bf00199471

[2] The Virtual Brain. (2024). TVB Documentation - Neural Mass Models. https://www.thevirtualbrain.org/

[3] Mahdi, H., Sieber, J., & Tsaneva-Atanasova, K. (2024). Alpha-delta transitions in cortical rhythms as grazing bifurcations. *arXiv preprint* arXiv:2411.16449. https://arxiv.org/abs/2411.16449

[4] Pei, A. (2025). Phase alignment enhances oscillatory power in neural mass models optimized for class encoding. *arXiv preprint* arXiv:2503.05564. https://arxiv.org/abs/2503.05564