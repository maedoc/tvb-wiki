---
title: Neural Network
created: 2026-04-20
updated: 2026-05-07
type: concept
tags: [neural-mass-models, network-dynamics, dynamical-systems-theory, nonlinear-dynamics, bifurcation-theory]
sources: [raw/papers/strogatz-1994.md, raw/papers/breakspear-2017.md, raw/papers/hagmann-2008.md, raw/papers/wilson-cowan-1972.md, raw/papers/wong-wang-2006.md, raw/papers/hodgkin-huxley-1952.md, raw/papers/izhikevich-2003.md, raw/papers/kuramoto-1975.md, raw/papers/jansen-rit-1995.md]
---

A **neural network** in the context of whole-brain modeling refers to a mathematical framework composed of interacting units that represent neural populations or individual neurons. Unlike machine learning neural networks—which are black-box function approximators trained via gradient descent—neural networks in computational neuroscience are explicitly designed to capture biologically motivated dynamics, often derived from conductance-based equations or mean-field approximations of spiking populations. These models form the dynamical core of [[whole-brain modeling]] platforms such as [[the-virtual-brain]], where they generate simulated brain activity that can be compared to empirical [[neuroimaging-fmri]], [[neuroimaging-eeg]], or [[neuroimaging-meg]] data.

## Theoretical Foundations and Historical Context

The mathematical study of neural dynamics traces its origins to the early work of nonlinear dynamics and [[bifurcation-theory]]. Steven Strogatz's seminal textbook on [[nonlinear-dynamics]] and chaos theory established the foundational tools—phase plane analysis, nullclines, bifurcation types (saddle-node, Hopf, pitchfork)—that remain essential for understanding how neural populations transition between activity states [1]. Michael Breakspear's 2017 review on [[dynamic-causal-modeling|dynamic models of large-scale brain activity]] synthesizes this tradition, providing a taxonomy of brain models that includes neural mass models, network models, and neural field models [2]. A neural mass model typically represents a cortical column or region as a set of coupled differential equations describing the mean activity of excitatory and inhibitory populations, capturing phenomena such as [[brain-oscillations]] and seizures.

The network perspective emerges from [[connectomics]] research, notably Hagmann et al.'s 2008 mapping of the [[structural-core]] of the human cerebral cortex using diffusion MRI [3]. This work demonstrated that brain regions are not uniformly connected but organized into a **rich-club** of highly interconnected hub regions. In computational models, the [[structural-connectivity]] matrix derived from diffusion imaging serves as the skeleton onto which neural mass models are coupled, yielding [[functional-connectivity]] patterns that emerge from the interplay between anatomy and dynamics.

## Mathematical Formulation

Neural network models in whole-brain modeling take several forms, each with different levels of biological detail. The simplest are **rate-based models**, where the activity of a population $i$ evolves according to:

$$\frac{dx_i}{dt} = -x_i + S\left(\sum_j w_{ij} x_j + I_i\right)$$

where $x_i$ is the mean firing rate of population $i$, $w_{ij}$ is the connection weight from $j$ to $i$, $I_i$ is external input, and $S(\cdot)$ is a sigmoidal activation function. The [[wilson-cowan-model]] [4] and [[wong-wang-model]] [5] are paradigmatic examples that have been used to study resting-state dynamics and transitions between brain states.

More biophysically detailed are conductance-based models such as the [[hodgkin-huxley-model]] [6], which describes membrane potential $V$ through coupled differential equations for sodium, potassium, and leakage currents. These give rise to realistic spiking behavior but are computationally expensive when scaled to whole-brain simulations. The [[izhikevich-neuron-model]] [7] offers a reduced two-dimensional formulation that captures the essential phenomenology of various spiking modes (tonic, phasic, bursting) with minimal computational cost.

For oscillatory dynamics, the [[kuramoto]] model [8] provides a powerful framework:

$$\frac{d\theta_i}{dt} = \omega_i + \frac{K}{N}\sum_{j=1}^{N} \sin(\theta_j - \theta_i)$$

where $\theta_i$ is the phase of oscillator $i$, $\omega_i$ its natural frequency, and $K$ the coupling strength. This model has been used to study synchronization phenomena in large-scale brain networks, particularly in the context of [[brain-oscillations]] across frequency bands.

## Whole-Brain Modeling with Neural Networks

In [[whole-brain modeling]], neural networks are instantiated at each brain region defined by a [[brain-parcellation]] (e.g., [[aal-atlas]], [[desikan-killiany-atlas]], or [[schaefer-atlas]]). The regional dynamics are then coupled via the empirical [[structural-connectivity]] matrix derived from [[diffusion-imaging]] tractography. This **connectome-based modeling** approach, exemplified by [[the-virtual-brain]], allows researchers to investigate how the anatomical scaffold constrains functional dynamics—a question central to the field of [[netneuroscience]].

The choice of neural mass model significantly affects the simulated dynamics. The [[jansen-rit-model]] [9]—a three-population model (pyramidal, excitatory, inhibitory)—has been extensively used for EEG/MEG simulation and can generate realistic alpha oscillations. The [[epileptor]] model specializes in seizure dynamics, employing a fast-slow subsystem architecture to capture the transition from interictal to ictal states relevant for [[epilepsy-modeling]]. The [[wong-wang-exc-inh]] model captures excitation-inhibition balance and has been used to simulate resting-state fMRI signals.

Parameter estimation in these models involves fitting simulated functional connectivity to empirical data, typically using optimization routines or Bayesian approaches. This yields personalized brain models that can predict individual responses to [[brain-stimulation]] or disease progression, a core goal of [[personalized-brain-modeling]].

## Relationship to Machine Learning Architectures

While neural networks in computational neuroscience share the name with deep learning architectures, their purposes and training paradigms differ fundamentally. Neuroscience-inspired neural networks aim to explain mechanisms—how does excitation-inhibition balance give rise to oscillations? How do [[network-dynamics]] emerge from [[structural-connectivity]]? Deep learning networks, by contrast, are typically treated as black boxes optimized for prediction performance. However, advances in [[machine-learning]] for neuroscience, particularly in encoding models that predict neural responses from stimuli, have created productive bridges between these traditions.

## Open Questions and Future Directions

The field faces several open challenges. **Neural mass models remain phenomenological**—while they capture population dynamics effectively, their parameters do not always map cleanly to biological quantities. Bridging the gap between microscopic spiking neural networks (see [[spiking-neural-networks]]) and macroscopic mean-field models remains an active research area. Additionally, the relationship between structural connectivity reconstructed via [[tractography]] and true anatomical pathways remains contested, directly affecting the validity of whole-brain simulations. Future directions include integrating [[variational-bayes]] and [[free-energy-principle]] frameworks for robust parameter estimation, and using [[neuroml]] standards to ensure interoperability between simulators.
