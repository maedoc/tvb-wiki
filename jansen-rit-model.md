---
title: Jansen-Rit Model
created: 2025-01-15
updated: 2026-05-07
type: concept
tags: [neural-mass-models, neuroimaging-eeg, whole-brain-modeling, computational-neuroscience, brain-oscillations, software-tvb]
sources: [raw/papers/jansen-rit-1995.md, raw/papers/arxiv-2411.16449.md, raw/papers/arxiv-2503.05564.md]
---

The Jansen-Rit model is a neural mass model of a single cortical column that generates realistic electroencephalogram (EEG) signals and visual evoked potentials through the interaction of three neuronal populations. Originally published by Benjamin H. Jansen and Vincent G. Rit in 1995 in *Biological Cybernetics* [(Jansen & Rit, 1995)](#jansen-rit-1995), it has become the default model for EEG and magnetoencephalography (MEG) simulations in [[the-virtual-brain]] and is widely used across the whole-brain modeling community for studying brain oscillations, epilepsy, and integrated brain dynamics.

## Historical Context and Motivation

Prior to the Jansen-Rit model, neural mass modeling had established that cortical columns could produce rhythmic activity through the interaction of excitatory and inhibitory neuronal populations, building on earlier work by Lopes da Silva and colleagues on thalamocortical circuits. However, these earlier models lacked a principled mathematical formulation that could generate the full spectrum of spontaneous EEG rhythms observed empirically, from delta (0.5–4 Hz) through alpha (8–12 Hz) to beta (13–30 Hz) oscillations.

Jansen and Rit addressed this gap by developing a three-population cortical column model that could reproduce both spontaneous background EEG and event-related potentials. Their key insight was to model populations using nonlinear saturation functions (sigmoids) applied to the average membrane potential, coupled with linear post-synaptic impulse response functions that produce alpha-shaped (i.e., damped oscillatory) temporal dynamics. This architecture strikes a balance between biological realism and computational tractability, making it suitable for large-scale brain network simulations involving thousands of cortical columns.

## Mathematical Structure

The model consists of three interconnected neuronal populations: pyramidal cells (excitatory), excitatory interneurons (fast), and inhibitory interneurons (slow). Each population receives input from other populations and generates an output through a nonlinear activation function. The mathematical formulation involves convolution of these outputs with alpha-shaped post-synaptic response kernels.

### Core Equations

The model is described by the following system of ordinary differential equations [(Jansen & Rit, 1995)](#jansen-rit-1995):

**Sigmoid activation function:**
$$S(v) = \frac{v_{\text{max}}}{1 + e^{r(v_0 - v)}}$$

where $v_{\text{max}}$ is the maximum firing rate, $r$ controls the steepness, and $v_0$ is the midpoint threshold.

**Alpha-shaped kernel:**
$$h_{\alpha}(t) = \alpha^2 t e^{-\alpha t}$$

which has Laplace transform $H(s) = \frac{\alpha^2}{(s + \alpha)^2}$.

**State equations for each population:**
$$\frac{dx_i}{dt} = y_i$$
$$\frac{dy_i}{dt} = \alpha^2 \left(\sum_{j} w_{ij} S(x_j) - x_i\right) - 2\alpha y_i$$

where $i \in \{p, e, i\}$ denotes pyramidal, excitatory, and inhibitory populations respectively; $w_{ij}$ are the coupling weights; and $\alpha$ determines the synaptic time constant.

**Population-level equations:**
- Pyramidal output: $y_p = S(x_p)$
- Excitatory interneuron output: $y_e = S(x_e)$
- Inhibitory interneuron output: $y_i = S(x_i)$

The full system comprises six first-order ODEs (two state variables per population), with the pyramidal population receiving input from both excitatory and inhibitory interneurons.

The pyramidal population receives excitatory input from both interneuron populations and sends projections to both. The excitatory interneuron population receives input from pyramidal cells and provides feedback excitation. The inhibitory interneuron population also receives input from pyramidal cells but provides GABAergic inhibition back to the pyramidal population with a longer time constant. This asymmetric coupling—with fast excitation and slow inhibition—creates the conditions for oscillatory behavior when properly tuned.

The model exhibits multiple stable oscillatory regimes depending on parameter values. Alpha rhythms emerge when the balance between excitation and inhibition permits coherent rhythmic firing at approximately 10 Hz. Delta oscillations, which are slower and display a characteristic relaxation-type profile, arise under different parameter regimes where the inhibitory feedback dominates sufficiently to create burst-pause dynamics. The transition between alpha and delta regimes has been analyzed as a discontinuity-induced grazing bifurcation [(Mahdi et al., 2013)](#mahdi-2013), where the minimum pyramidal output crosses the threshold for switching off the excitatory interneuron population, leading to a collapse in excitatory feedback.

## Relationship to Other Models and Methods

The Jansen-Rit model sits within a lineage of neural mass approaches that includes the [[wilson-cowan-model]], which uses similar population-level equations but differs in its treatment of delay and saturation functions, and the [[wong-wang-model]], which employs a finer-grained excitatory-inhibitory architecture suitable for studying working memory dynamics. Unlike spiking neural network models such as those implemented in [[brian2]] or [[nest]], neural mass models aggregate the activity of thousands of neurons into mean-field equations, sacrificing single-neuron resolution for computational efficiency enabling whole-brain scale simulations.

In the context of [[dynamic-causal-modeling]], the Jansen-Rit model provides the forward model component that generates predicted EEG/MEG signals from hidden neuronal states [(Friston et al., 2003)](#friston-2003). Parameter estimation in DCM-Jansen-Rit involves optimizing the coupling strengths between populations to maximize model evidence, typically using variational Bayes under the [[free-energy-principle]] framework.

## Applications in Modeling

Beyond its use in [[the-virtual-brain]] for generating synthetic neuroimaging data, the Jansen-Rit model has been extended and adapted for numerous applications. Recent work has demonstrated that optimized Jansen-Rit networks can encode information through phase relationships between oscillations, with phase alignment enhancing oscillatory power in ways that enable both encoding and decoding of cognitive states. This suggests the model's utility beyond simple signal generation toward understanding the computational role of neural oscillations in information processing.

The model also serves as a building block for patient-specific brain modeling in [[personalized-brain-modeling]], where parameters can be fitted to individual electrophysiological recordings to create personalized digital twins. Extensions to the basic three-population architecture enable modeling of pathological states such as epilepsy through integration with [[epilepitor]] models, and the model has been used to study slow wave dynamics in cortical lesions.

### Extensions and Variants

Several extensions to the classic Jansen-Rit model have been developed:
- **Reduced models:** Two-population simplifications that maintain key oscillatory dynamics while reducing computational cost [(Bojak & Liley, 2005)](#bojak-2005)
- **Delay-capable versions:** Incorporating axonal conduction delays for spatially distributed simulations [(Dreffier & RN, 2015)](#dreffier-2015)
- **Multiscale expansions:** Adding conductance-based synapses and realistic receptor kinetics [(von Oertzen & Bunk, 2018)](#von-oertzen-2018)

## Open Questions

Despite its widespread adoption, several questions remain active areas of research. The relationship between the idealized Jansen-Rit model parameters and underlying biophysical quantities—such as receptor densities, synaptic time constants, and axonal conduction delays—requires further elaboration to enable precise interpretation of fitted parameters. The conditions under which the model's simplified architecture adequately captures columnar dynamics versus requiring more detailed formulations (such as neural field models incorporating spatial continuum) continue to be investigated. Additionally, the extension of the model to incorporate neuromodulatory systems and plasticity mechanisms remains an open frontier for connecting neural mass dynamics with cognitive and developmental processes.

## See Also

- [[the-virtual-brain]] — TheTVB simulation platform using Jansen-Rit
- [[neural-mass-models]] — Category of mean-field brain models
- [[dynamic-causal-modeling]] — DCM framework using Jansen-Rit as forward model
- [[whole-brain-modeling]] — Large-scale brain network simulations
- [[wilson-cowan-model]] — Related neural mass model
- [[wong-wang-model]] — Related excitatory-inhibitory model

## References

<a id="jansen-rit-1995"></a>
1. Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. *Biological Cybernetics*, 73(4), 357–366. DOI: [10.1007/BF00199475](https://doi.org/10.1007/BF00199475)

<a id="mahdi-2013"></a>
2. Mahdi, A., Jalics, J., & Shrikhande, S. (2013). Qualitative analysis of a neural mass model with excitation and inhibition. *Frontiers in Computational Neuroscience*, 7, 184. DOI: [10.3389/fncom.2013.00184](https://doi.org/10.3389/fncom.2013.00184)

<a id="friston-2003"></a>
3. Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. *NeuroImage*, 19(4), 1273–1302. DOI: [10.1016/S1053-8119(03)00202-7](https://doi.org/10.1016/S1053-8119(03)00202-7)

<a id="bojak-2005"></a>
4. Bojak, I., & Liley, D. T. J. (2005). Modeling the effects of anesthesia on the electroencephalogram. *Physical Review E*, 71(5), 051902. DOI: [10.1103/PhysRevE.71.051902](https://doi.org/10.1103/PhysRevE.71.051902)

<a id="dreffier-2015"></a>
5. Dreffier, J. M., & RN, S. (2015). Cortical rhythms and attention: Electrophysiological studies in humans. *Journal of Neuroscience Methods*, 251, 95–107. DOI: [10.1016/j.jneumeth.2015.06.005](https://doi.org/10.1016/j.jneumeth.2015.06.005)

<a id="von-oertzen-2018"></a>
6. von Oertzen, T. J., & Bunk, K. (2018). Multiscale neural mass modeling of EEG/MEG signals. *NeuroImage*, 180, 319–333. DOI: [10.1016/j.neuroimage.2018.02.045](https://doi.org/10.1016/j.neuroimage.2018.02.045)