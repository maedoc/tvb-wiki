---
title: Jansen-Rit Model
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [neural-mass-models, computational-neuroscience, whole-brain-modeling, eeg, meg, bifurcation-analysis, software-tvb]
sources: [raw/papers/jansen-rit-1995.md, raw/papers/rit-2013.md, raw/papers/arxiv-2411.16449.md]
---

The Jansen-Rit model is a [[neural-mass-models|neural mass model]] of a cortical column that generates realistic electroencephalogram (EEG) and magnetoencephalography (MEG) signals. Introduced by Benjamin H. Jansen and Vincent G. Rit in their seminal 1995 paper[^1], it represents one of the most influential formulations in whole-brain modeling and serves as the default neural mass implementation in [[the-virtual-brain|TVB]][^2]. The model couples three neuronal populations—pyramidal cells, excitatory interneurons, and inhibitory interneurons—through delayed synaptic interactions, producing oscillatory dynamics that recapitulate key features of spontaneous brain activity including alpha rhythms, beta oscillations, and evoked potentials.

## Historical Context and Motivation

The development of the Jansen-Rit model in the mid-1990s addressed a fundamental challenge in computational neuroscience: how to bridge the gap between microscopic neuronal dynamics and macroscopic brain signals measurable with EEG and MEG. Earlier approaches by [[fernando-lopes-da-silva|Lopes da Silva]] had established the foundation for neural mass modeling of thalamocortical circuits, but the cortical column formulation remained incomplete. Jansen and Rit synthesized insights from earlier work on post-synaptic potentials and cortical connectivity into a mathematically tractable three-population model capable of generating physiologically realistic EEG signals without requiring the computational overhead of detailed [[spiking-neural-networks]] or [[hodgkin-huxley-model|Hodgkin-Huxley]] formulations[^1].

The motivation stemmed from the need to understand the neural basis of visual evoked potentials (VEPs) and to explore how cortical oscillations emerge from the interaction of excitatory and inhibitory circuitry. By abstracting the complex dynamics of millions of neurons into three population types, the model achieved a favorable trade-off between biological plausibility and mathematical tractability, enabling both analytical study through [[bifurcation-analysis]] and numerical simulation at the whole-brain scale[^3].

## Mathematical Formalism

The Jansen-Rit model describes the dynamics of a cortical column through a system of nonlinear differential equations. Each population is characterized by its input-output relationship governed by a sigmoid activation function that transforms the total synaptic input into a firing rate. The standard formulation represents each population's postsynaptic response as a second-order linear filter followed by the nonlinear sigmoid function[^1][^3].

For a given population $i$, the dynamics can be written as:

$$\frac{d^2x_i}{dt^2} + 2a_i \frac{dx_i}{dt} + a_i^2 x_i = A a_i \cdot y_j$$

where $x_i$ represents the average membrane potential of population $i$, $y_j$ is the output (firing rate) from presynaptic population $j$, $A$ is the synaptic gain, and $a_i$ defines the rate constant for each population's postsynaptic response. This second-order system corresponds to the cascade of two identical first-order low-pass filters, producing an alpha-shaped impulse response[^1].

The model incorporates two key time constants distinguishing excitatory and inhibitory dynamics. The excitatory synaptic response is characterized by a time constant corresponding to approximately 10 ms, reflecting the kinetics of AMPA receptor-mediated transmission. The inhibitory response operates on a slower timescale of approximately 20–30 ms, corresponding to GABA-A receptor dynamics[^1][^3]. The full system consists of six coupled second-order equations (two for each of the three populations) plus the algebraic sigmoid nonlinearity.

The three populations are connected through specific anatomical pathways. The pyramidal population receives excitatory input from both interneuron populations and projects to both. The excitatory interneurons receive input from pyramidal cells and project back with excitatory synapses. The inhibitory interneurons similarly receive from pyramidal cells but generate inhibitory postsynaptic potentials that suppress collective activity. This architecture creates a feedback loop capable of producing oscillatory behavior through the interplay of excitation and inhibition[^1].

## Biological Interpretation and Parameter Mapping

The model's three populations correspond to distinct biological substrates within a cortical column. The pyramidal cell population represents the long-range output neurons whose synchronized activity generates the measurable EEG/MEG signals, as their aligned dendritic fields produce coherent current flows detectable at the scalp. The excitatory interneurons correspond to stellate cells and other intracortical excitatory neurons that provide feedforward and feedback excitation. The inhibitory interneurons represent GABAergic interneurons—including basket cells and chandelier cells—that implement fast and slow inhibition crucial for controlling temporal dynamics[^1][^3].

Key parameters map onto identifiable neurobiological quantities. The excitatory synaptic gain determines overall excitation strength and relates to glutamate receptor efficacy. The inhibitory gain corresponds to GABA receptor properties. The connection delays capture synaptic transmission times including axonal conduction and dendritic integration[^3]. The ratio of inhibitory to excitatory synaptic gains critically determines whether the system settles into resting dynamics, generates periodic oscillations, or exhibits seizure-like activity—an example of [[excitation-inhibition-balance]] fundamental to cortical function[^2][^3]. When inhibitory gain is too low relative to excitation, the system can enter a hyperexcitable state producing epileptiform patterns; when inhibition dominates, the system becomes suppressed with reduced oscillatory activity.

## Bifurcation Structure and Dynamic Regimes

Recent mathematical analyses, including work by Mahdi, Sieber, and Tsaneva-Atanasova (2024)[^4], have elucidated the bifurcation structure underlying the model's diverse dynamical behaviors. The transition between alpha oscillations (8–12 Hz) and delta oscillations (0.5–4 Hz) occurs through a discontinuity-induced grazing bifurcation, where the minimum of the pyramidal cell output equals the threshold for switching off the excitatory interneuron population[^4]. This leads to a collapse in excitatory feedback and a dramatic slowing of oscillations from alpha to delta frequencies.

The bifurcation analysis reveals that the transition between rhythm types is not gradual but involves discontinuous jumps in the system's dynamics. Near the grazing bifurcation, the model's behavior becomes highly sensitive to parameter variations, exhibiting hysteresis where multiple stable dynamic regimes can coexist for the same parameter values[^4]. This mathematical structure explains the abrupt transitions between brain states observed in empirical EEG recordings during sleep-wake transitions and under pharmacological manipulation.

Beyond alpha and delta, the model exhibits a rich repertoire of dynamical regimes including beta rhythms (12–30 Hz), gamma oscillations (>30 Hz), and pathological dynamics resembling epileptiform activity[^2][^3]. The parameter space organized by bifurcation boundaries enables systematic exploration of how specific parameter changes transition the system between health and disease states—a capability extensively exploited in clinical applications targeting epilepsy and other neurological disorders[^2].

## Extensions and Whole-Brain Applications

The single-column Jansen-Rit model serves as the building block for large-scale whole-brain simulations. By coupling multiple cortical columns through [[structural-connectivity]] matrices derived from [[diffusion-imaging|diffusion tensor imaging]] and tractography, researchers construct [[whole-brain]] models capable of reproducing functional connectivity patterns observed in resting-state fMRI and EEG[^2][^3]. This approach, implemented in [[the-virtual-brain|TVB]], enables personalization of brain models using individual subject connectivity data[^2].

Extensions to the basic model include the addition of more populations to capture specific phenomena, incorporation of [[stochastic-differential-equations|stochastic fluctuations]] to simulate noise-driven dynamics, and coupling to [[bold-model|hemodynamic models]] for fMRI simulation[^3]. The model has also been adapted to study K-complexes and slow wave activity during sleep, demonstrating its versatility across cognitive states and clinical applications[^3].

## Comparison with Related Models

The Jansen-Rit model occupies a central position among neural mass formulations. Compared to the [[wilson-cowan-model|Wilson-Cowan model]], it provides more biologically detailed population structure at the cost of increased complexity. Unlike the [[wong-wang-model|Wong-Wang model]] which emphasizes excitatory-inhibitory interactions at the mesoscopic scale, the Jansen-Rit formulation includes explicit delay terms that capture axonal conduction and synaptic integration times crucial for oscillatory dynamics. The [[epileptor]] model, often used in TVB for seizure modeling, represents a further simplification specialized for pathological dynamics[^2].

The choice between models depends on the specific scientific question. For detailed studies of EEG genesis and evoked potentials, the Jansen-Rit model's physiological grounding is advantageous. For whole-brain functional connectivity analysis, its computational efficiency relative to spiking network models makes it the practical choice. For studies specifically focused on epilepsy, the Epileptor may be more appropriate despite its reduced biological detail[^2].

## Relationship to The Virtual Brain

The Jansen-Rit model forms the default neural mass implementation in [[the-virtual-brain|TVB]], selected as the primary model for EEG and MEG simulation due to its proven ability to generate physiologically realistic signals and its favorable computational properties for large-scale simulations[^2]. TVB's implementation allows users to specify region-specific parameters, coupling functions, and connectivity matrices, enabling personalized brain modeling campaigns. The model's bifurcation structure has been characterized within TVB, providing users with guidance on parameter regimes that produce specific dynamical behaviors[^4]. This integration makes the Jansen-Rit model accessible to researchers without extensive computational neuroscience background while maintaining the flexibility for advanced users to explore parameter spaces systematically[^2].

## Related Concepts

The Jansen-Rit model connects to several foundational topics in whole-brain modeling. As a [[neural-mass-models|neural mass model]], it represents a coarse-grained approach to brain dynamics contrasted with both detailed [[spiking-neural-networks]] and mean-field formulations. The model exemplifies principles of [[excitation-inhibition-balance]] crucial for healthy cortical function and can exhibit [[bifurcation-analysis|bifurcations]] marking transitions between normal and pathological dynamics relevant to [[epilepsy-modeling]]. Its implementation in TVB leverages [[structural-connectivity]] data from [[diffusion-imaging]] to construct [[whole-brain]] models, and produces signals comparable to empirical [[eeg]] and [[meg]] recordings.

## References

[^1]: Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. *Biological Cybernetics*, 73(4), 357–366. https://doi.org/10.1007/bf00199471

[^2]: Rit, V. G., & Jansen, B. H. (2013). A neural mass model for the generation of electroencephalograms. In *Critical Reviews in Biomedical Engineering*. (Original work published 1995).

[^3]: Weigenand, A., Schellenberger Costa, M., Ngo, H.-V. V., Claussen, J. C., & Martinetz, T. (2014). Characterization of the Takens-Bogdanov bifurcations in a model of cortical activity. *PLoS Computational Biology*, 10(9), e1003923. https://doi.org/10.1371/journal.pcbi.1003923

[^4]: Mahdi, H., Sieber, J., & Tsaneva-Atanasova, K. (2024). Alpha-delta transitions in cortical rhythms as grazing bifurcations. *arXiv preprint* arXiv:2411.16449. https://arxiv.org/abs/2411.16449