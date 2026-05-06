---
title: Jansen-Rit Model
created: 2026-04-20
updated: 2026-05-06
type: concept
tags: [neural-mass-models, eeg, computational-neuroscience, brain-oscillations, bifurcation-analysis]
sources: [raw/papers/jansen-rit-1995.md, raw/papers/arxiv-2411.16449.md, raw/papers/arxiv-2503.05564.md, raw/papers/gaglioti-2026.md]
---

The Jansen-Rit model is a mathematical model of a cortical column that generates realistic electroencephalogram (EEG) signals and visual evoked potentials (VEPs). Introduced by Benjamin H. Jansen and Vincent G. Rit in their seminal 1995 paper published in Biological Cybernetics [(Jansen & Rit, 1995)](raw/papers/jansen-rit-1995.md), the model has become one of the most widely used [[neural-mass-models]] in computational neuroscience and forms the default forward model for EEG and MEG simulations in [[the-virtual-brain]] [(Sanz-Leon et al., 2015)](raw/papers/tvb-documentation.md). The model represents a cornerstone of [[whole-brain-modeling]] approaches, where multiple cortical columns are coupled via [[structural-connectivity]] to simulate large-scale brain dynamics.

## Motivation and Biological Context

Understanding the electromagnetic signatures of the brain has been a central challenge in [[computational-neuroscience]] since the early days of EEG research. The Jansen-Rit model emerged as a response to the need for biophysically principled models that could link mesoscopic neural population dynamics to macroscopic signals measurable on the scalp. Unlike simplified [[oscillator]] models or [[rate-based-neural-networks]], the Jansen-Rit model captures the interaction between excitatory and inhibitory populations within a cortical column, allowing for realistic simulation of brain rhythms across different frequency bands.

The model's architecture draws on earlier work by Fernando Lopes da Silva [(Lopes da Silva et al., 1974)](raw/papers/lopes-da-silva-1974.md), who developed thalamic models of EEG generation, but extends this framework to explicitly represent cortical processing. This was significant because cortical columns are the fundamental computational unit of the cerebral cortex, and understanding their dynamics is essential for linking microscopic neural mechanisms to whole-brain [[brain-dynamics]] observed in neuroimaging.

## Model Architecture

The Jansen-Rit model consists of three interconnected neural populations representing a single cortical column. The first population comprises pyramidal cells, which are the principal excitatory output neurons of the cortex and the source of the electrical signals measured by EEG. These pyramidal cells receive excitatory input from the second population (excitatory interneurons) and inhibitory input from the third population (inhibitory interneurons), projecting their output to both interneuron populations to complete the feedback loop.

The excitatory interneurons provide fast, glutamatergic feedback to the pyramidal cells, while the inhibitory interneurons mediate GABAergic inhibition with slower dynamics. This asymmetry between fast excitation and slower inhibition is crucial for generating oscillatory behavior. Each population is modeled using a nonlinear function that transforms the total synaptic input into a firing rate, followed by a post-synaptic response function—historically an alpha-shaped function (modeled as a second-order linear filter) that gives the model its characteristic impulse response dynamics [(Jansen & Rit, 1995)](raw/papers/jansen-rit-1995.md).

The mathematical formulation involves ordinary differential equations that govern the dynamics of post-synaptic potentials through second-order linear filters. These filters, with typical time constants on the order of 10-20 milliseconds [(Grimbert & Faugeras, 2006)](raw/papers/grimbert-faugeras-2006.md), determine the oscillatory behavior and allow the model to produce rhythms in the alpha (8-12 Hz), beta (13-30 Hz), and delta (<4 Hz) frequency bands depending on parameter choices.

## Dynamics and Bifurcation Analysis

One of the remarkable properties of the Jansen-Rit model is its ability to produce multiple distinct oscillatory regimes through parameter variation, a phenomenon studied extensively through [[bifurcation-analysis]]. The transition between alpha and delta oscillations has been mathematically characterized as a discontinuity-induced grazing bifurcation, where the minimum of the pyramidal cell output equals the threshold for switching off the excitatory interneuron population, leading to a collapse in excitatory feedback.

Recent work by Mahdi, Sieber, and Tsaneva-Atanasova (2024) [(Mahdi et al., 2024)](raw/papers/arxiv-2411.16449.md) has formalized this transition mechanism, showing that when excitatory activation thresholds are small and slopes are steep—a regime appropriate for neural population dynamics—a singular limit replacing the excitatory activation function with all-or-nothing switches (Heaviside function) allows precise characterization of the bifurcation. This mathematical analysis provides a foundation for understanding how the model generates different brain states and how transitions between them might be induced by external stimulation or pathological changes.

## Applications in Neural Encoding

Beyond traditional EEG simulation, the Jansen-Rit model has found application in studying how neural circuits encode information. Research by Pei (2025) [(Pei, 2025)](raw/papers/arxiv-2503.05564.md) demonstrated that optimized parameter configurations of the Jansen-Rit model can encode different input classes as phase-shifted oscillations. By using genetic algorithms to maximize differences in population responses to particular inputs, phase alignment across neural populations enhanced oscillatory power in ways that could be decoded by downstream circuits. This work highlights the model's utility as a tool for understanding neural coding mechanisms beyond its original purpose of signal generation.

The model has also been extended to study slow wave generation and the effects of cortical lesions on emergent network dynamics [(Gaglioti et al., 2026)](raw/papers/gaglioti-2026.md), demonstrating its relevance for understanding pathological brain states and their relationship to cortical column dysfunction.

## Relationship to Other Models and TVB Integration

The Jansen-Rit model is closely related to other [[neural-mass-models]] including the [[wilson-cowan-model]], which uses a similar population-based approach but with different mathematical formulations and a focus on broader cortical dynamics. Compared to spiking network models like those implementable in [[brian]] or [[nest]], the Jansen-Rit model trades biological realism for computational tractability, making it suitable for simulating large brain networks comprising hundreds of cortical regions.

In [[the-virtual-brain]], the Jansen-Rit model serves as the default neural mass model for generating simulated EEG and MEG signals [(Sanz-Leon et al., 2015)](raw/papers/tvb-documentation.md). The TVB framework couples multiple Jansen-Rit units according to [[structural-connectivity]] matrices derived from diffusion tensor imaging (DTI) data, enabling whole-brain simulations that can be compared against empirical neuroimaging data. This integration makes the model particularly valuable for studying [[personalized-brain-modeling]] applications, where patient-specific connectivity is used to predict individual brain dynamics.

The model's [[forward-model]] formulation also connects to [[dynamic-causal-modeling]] (DCM), where similar population dynamics are inverted using variational methods to estimate effective connectivity from observed data. [[parameter-estimation]] in the Jansen-Rit context involves fitting model outputs to empirical EEG or MEG recordings, typically using optimization or Bayesian approaches to identify the excitatory and inhibitory coupling strengths that best explain observed brain dynamics.