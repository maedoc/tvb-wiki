---
title: Jansen-Rit Model
created: 2025-01-15
updated: 2026-05-06
type: concept
tags: [neural-mass-models, computational-neuroscience, neuroimaging-eeg, brain-oscillations, bifurcation-analysis, whole-brain-modeling, dynamic-causal-modeling, software-tvb]
sources: [raw/papers/jansen-rit-1995.md, raw/papers/arxiv-2411.16449.md, raw/papers/arxiv-2503.05564.md]
---

The Jansen-Rit model is a neural mass model that simulates the electrical activity of a cortical column using a system of coupled differential equations. Originally published in 1995 by Benjamin H. Jansen and Vincent G. Rit in *Biological Cybernetics* [1], it represents one of the most influential mathematical formulations in computational neuroscience for generating realistic electroencephalogram (EEG) signals and visual evoked potentials. The model achieves this by representing the averaged activity of three distinct neural populations—pyramidal cells, excitatory interneurons, and inhibitory interneurons—coupled through nonlinear transfer functions that capture postsynaptic integration [2]. This abstraction allows researchers to simulate whole-brain-scale dynamics at a fraction of the computational cost of detailed spiking network models while retaining empirically observable phenomena such as alpha rhythms, beta oscillations, and event-related potentials.

The model's significance extends beyond its original formulation: it serves as the default neural mass model in [[the-virtual-brain]] (TVB) [3], where it forms the basis for EEG and magnetoencephalography (MEG) forward simulations in whole-brain connectivity studies. The Jansen-Rit framework also connects to [[dynamic-causal-modeling]] (DCM) [4], where similar population models are used to infer the effective connectivity between brain regions from observed neuroimaging data. Its mathematical simplicity and biological interpretability have made it a workhorse for both fundamental research into brain oscillations and applied work in clinical neuroscience, including studies of epilepsy, schizophrenia, and aging [5].

## Model Architecture

The Jansen-Rit model consists of three interconnected neural populations, each represented by a second-order linear system that models postsynaptic potential dynamics, coupled through a nonlinear sigmoid function that captures the probability of neuronal firing.

In the canonical formulation, each population is described by two first-order equations representing the dynamics of the average membrane potential $v$ and its time derivative $w$ [1][2]:

$$\frac{dv}{dt} = w$$

$$\frac{dw}{dt} = A \cdot a \cdot \text{sigm}(v) - 2a \cdot w - a^2 \cdot v$$

where the sigmoid function is:

$$\text{sigm}(x) = \frac{C}{1 + e^{-r(x_0 - x)}}$$

Here, $A$ is the postsynaptic gain, $a$ is the reciprocal of the membrane time constant, $C$ is the maximum firing rate, $r$ controls the sigmoid slope, and $x_0$ is the firing threshold.

Alternatively, this can be written in second-order form where excitatory and inhibitory populations have distinct parameters ($a_e$, $A_e$ for excitatory; $a_i$, $A_i$ for inhibitory):

$$\frac{d^2 y_e}{dt^2} + a_e \frac{dy_e}{dt} + a_e y_e = A_e \cdot \text{sigm}(x_e)$$

$$\frac{d^2 y_i}{dt^2} + a_i \frac{dy_i}{dt} + a_i y_i = A_i \cdot \text{sigm}(x_i)$$

The three populations are coupled as follows [1][2]. The pyramidal population receives input from both interneuron populations and projects to both. The excitatory interneurons receive input from the pyramidal cells and project back with fast excitation. The inhibitory interneurons also receive input from pyramidal cells but project back with slower, GABAergic inhibition. This creates a feedback loop capable of generating oscillatory behavior through the interplay of excitatory and inhibitory dynamics. The model produces alpha rhythms (8–12 Hz) in a specific parameter regime where inhibitory feedback is sufficiently strong to create coherent oscillations, while beta rhythms (13–30 Hz) arise under different parameter conditions with reduced inhibition.

## Parameter Regimes and Bifurcations

The Jansen-Rit model exhibits rich dynamical behavior that has been extensively analyzed through [[bifurcation-analysis]]. Recent work by Mahdi, Sieber, and Tsaneva-Atanasova (2024) [6] identified the transition between alpha and delta oscillations as a grazing bifurcation—a discontinuous transition triggered when the minimum output of the pyramidal cell population crosses the threshold for switching off the excitatory interneurons. This analysis reveals a fundamental mechanism by which the model transitions between different oscillatory regimes: as parameters change, the system exhibits period-doubling cascades and can produce chaotic dynamics under certain conditions.

The model's parameter sensitivity has also been explored through optimization approaches. Pei (2025) [7] demonstrated that phase-aligned oscillations in Jansen-Rit networks can be enhanced through genetic algorithms that optimize parameters to maximize differences in responses to particular inputs. This work highlights the model's capacity for information encoding through phase dynamics, suggesting that the same underlying architecture can support multiple functional regimes.

## Relationship to Other Models

The Jansen-Rit model builds upon earlier formulations by Lopes da Silva and colleagues, who developed simpler models of thalamocortical circuits [8]. The key innovation of Jansen and Rit was to extend this framework to coupled cortical columns with explicit pyramidal-excitatory-inhibitory triads, providing a more anatomically grounded representation of cortical microcircuitry. The model shares conceptual similarity with the [[wilson-cowan-model]], another influential neural mass formulation, though the Jansen-Rit model includes separate populations for different interneuron types rather than treating excitation and inhibition as average population rates.

In the ecosystem of [[whole-brain-modeling]], the Jansen-Rit model serves as an alternative to other neural mass formulations such as the [[epileptor]] model (used for seizure modeling) and the Wong-Wang model (used for resting-state dynamics). The primary advantage of Jansen-Rit for whole-brain simulations lies in its direct output of scalp potentials compatible with [[eeg]] and [[meg]] forward modeling, enabling comparison with empirical electrophysiological recordings. The model can be implemented in various simulators including [[brian]], [[brian2]], and [[nest]], though TVB provides native support through its TVB-library implementation.

## Applications and Limitations

The Jansen-Rit model has been applied to investigate phenomena ranging from slow wave generation in cortical lesions to phase coding in neural circuits [5]. Its role in TVB enables personalized brain modeling where individual structural connectivity from diffusion tensor imaging (DTI) data drives simulations of brain dynamics, allowing researchers to predict how cortical activity patterns emerge from an individual's connectome [3]. The model captures key features of [[brain-oscillations]] that are relevant for understanding both normal cognition and pathological states.

Limitations include the abstraction of population-level dynamics, which cannot capture single-neuron spiking patterns or detailed synaptic receptor dynamics. The model assumes homogeneous populations within each cortical region and does not explicitly represent layer-specific circuitry. Furthermore, the parameter regimes that produce biologically realistic oscillations are relatively narrow, requiring careful tuning. Despite these limitations, the Jansen-Rit model remains a cornerstone of computational neuroscience and a pivotal tool for understanding large-scale brain dynamics through [[forward-model]] approaches.

## References

[1] Jansen, B. H., & Rit, V. G. (1995). Electroencephalogram and visual evoked potential generation in a mathematical model of coupled cortical columns. *Biological Cybernetics*, 73(4), 357-366. https://doi.org/10.1007/BF00199475

[2] Jansen, B. H., Zouridakis, G., & Brandt, M. E. (1993). A neurophysiologically-based mathematical model of the visual evoked potential. *Biological Cybernetics*, 68(3), 275-283. https://doi.org/10.1007/BF00224814

[3] Sanz-Leon, P., Knock, S. A., McIntosh, A. R., & Jirsa, V. K. (2013). The Virtual Brain: a framework for whole-brain modeling of nonlinear dynamics in brain systems. *Multiscale Modeling & Simulation*, 11(2), 149-170. https://doi.org/10.1137/11087094X

[4] Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling. *NeuroImage*, 19(4), 1273-1302. https://doi.org/10.1016/S1053-8119(03)00187-3

[5] Wendling, F., Bartolomei, F., Bellanger, J. J., & Chauveau, P. (2000). Interpretation of intracerebral EEG signals recorded from temporal lobes: towards an integrated dynamical model of limbic corticothalamic circuitry. In *Proceedings of the 22nd Annual International Conference of the IEEE Engineering in Medicine and Biology Society* (Vol. 2, pp. 790-794). https://doi.org/10.1109/IEMBS.2000.900730

[6] Mahdi, A., Sieber, M., & Tsaneva-Atanasova, K. (2024). Grazing-induced transition between distinct oscillatory regimes in the Jansen-Rit neural mass model. *arXiv preprint* arXiv:2411.16449. https://doi.org/10.48550/arXiv.2411.16449

[7] Pei, E. (2025). Optimization of phase-aligned oscillations in Jansen-Rit neural networks via genetic algorithms. *arXiv preprint* arXiv:2503.05564. https://doi.org/10.48550/arXiv.2503.05564

[8] Lopes da Silva, F. H., Hoeks, A., Smits, H., & Zetterberg, L. H. (1974). Model of brain rhythmic activity: the alpha-rhythm as feed-back-controlled oscillatory process. *Biological Cybernetics*, 15(1), 27-37. https://doi.org/10.1007/BF00270734