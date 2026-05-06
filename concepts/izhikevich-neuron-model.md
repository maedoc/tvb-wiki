---
created: 2026-04-20
sources:
- Izhikevich
- 2003; Izhikevich
- 2010; Hodgkin-Huxley; Brunel-Hakim-Richard
- raw/papers/potjans-diesmann-2014.md
- raw/papers/arxiv-2512.22093.md
- raw/papers/arxiv-2507.22146.md
tags:
- spiking-neural-networks
- neural-mass-models
- dynamical-systems-theory
- bifurcation-analysis
- computational-neuroscience
title: Izhikevich Neuron Model
type: concept
updated: '2026-05-06'
---

The Izhikevich neuron model is a reduced two-dimensional dynamical system that reproduces the spike-generating dynamics of cortical neurons with remarkable biological fidelity while maintaining computational tractability. Originally proposed by Eugene Izhikevich in 2003 (see [[izhikevich-2003]]), the model can generate all known types of cortical neuron firing patterns—including regular spiking, fast spiking, intrinsically bursting, and chattering—through variation of just four parameters. Its formulation bridges the gap between simplistic integrate-and-fire models that lack biological realism and biophysically detailed models like the [[hodgkin-huxley-model]] that require expensive numerical integration of dozens of state variables (see [[izhikevich-2010]] for review).

## Motivation and Context

The development of the [[izhikevich]] model addressed a fundamental challenge in [[computational-neuroscience]]: the need for [[neuron]] models that are both biologically realistic and computationally efficient enough to simulate large-scale networks. Traditional conductance-based models such as Hodgkin-Huxley accurately capture [[ion-channel]] dynamics but impose prohibitive computational costs when simulating brain-scale circuits. Conversely, leaky integrate-and-fire models are computationally efficient but cannot capture the diverse firing patterns observed in real neurons—such as adaptation, bursting, and frequency modulation—without ad hoc extensions.

Izhikevich's insight was to formulate a minimal two-variable system that captures the essential dynamics of neuronal spiking through a combination of voltage and recovery variables. The model achieves this by combining the quadratic integrate-and-fire mechanism (which produces realistic spike upstrokes) with a linear recovery variable that accounts for the interplay of ionic currents responsible for spike repolarization and adaptation. This balance between simplicity and biological fidelity has made the model a workhorse in large-scale [[spiking-neural-networks]] simulations, particularly in studies of [[brain-oscillations]] and [[network-dynamics]] (see also [[brunel-hakim-2005]] for Applications to network simulations).

## Mathematical Formulation

The Izhikevich model is governed by the following system of ordinary differential equations:

$$dv/dt = 0.04v^2 + 5v + 140 - u + I_{ext}$$

$$du/dt = a(bv - u)$$

with the reset condition:
$$\text{if } v \geq 30\text{mV, then } v \leftarrow c \text{ and } u \leftarrow u + d$$

In this formulation, $v$ represents the membrane potential and $u$ represents the recovery variable—a combined recovery variable that captures the effects of potassium and sodium currents. The parameter $a$ governs the recovery time constant (larger values produce faster recovery), $b$ controls the sensitivity of the recovery variable to subthreshold fluctuations, $c$ sets the after-spike reset voltage, and $d$ determines the after-spike increase in recovery. The external input current $I_{ext}$ drives the neuron and can be time-varying for more realistic stimulation protocols.

The quadratic term in the voltage equation ($0.04v^2$) generates the exponential rise characteristic of action potentials without requiring explicit threshold crossings, making the model spike-generating rather than spike-driven. This mathematical structure enables the model to undergo [[bifurcation-analysis]]—transitions between resting, spiking, and bursting regimes—similar to real neurons undergoing state transitions in response to changes in input current or neuromodulation.

## Firing Regimes and Biological Mapping

The power of the Izhikevich model lies in its ability to reproduce diverse cortical firing patterns through systematic parameter variation. Regular spiking pyramidal neurons are obtained with parameters $(a = 0.02, b = 0.2, c = -65, d = 8)$, where moderate values of $a$ and $d$ produce spike-frequency adaptation. Fast-spiking interneurons, characterized by high firing rates without adaptation, correspond to $(a = 0.1, b = 0.2, c = -65, d = 2)$—larger $a$ produces faster recovery. Intrinsically bursting neurons, which emit bursts of 2–4 spikes at resting potential before transitioning to tonic spiking, use parameters $(a = 0.02, b = 0.2, c = -55, d = 4)$ where the lower reset voltage $c$ initiates subsequent burst cycles. Chattering or rhythmic bursting neurons exhibit high-frequency burst onset and are captured by $(a = 0.02, b = 0.2, c = -50, d = 2)$.

These parameter regimes map onto biophysical mechanisms in real neurons: the $b$ parameter influences the coupling between $u$ and $v$, capturing the balance between depolarizing sodium and hyperpolarizing potassium currents; $d$ controls after-hyperpolarization depth, relating to calcium-activated potassium currents that produce accommodation; $c$ determines the voltage [[trajectory]] following spike termination, reflecting sodium channel inactivation dynamics.

## Relationship to Other Models

The Izhikevich model occupies a unique position in the taxonomy of [[neural-mass-models]] and spiking neuron models. Compared to the [[hodgkin-huxley-model]], it reduces the dimensionality from four state variables (m, h, n, plus membrane potential) to just two while capturing most qualitative firing patterns—this reduction makes simulations of networks with thousands of neurons tractable. Compared to leaky integrate-and-fire models, it exhibits genuine spike-generating dynamics rather than artificial threshold resets, enabling natural representation of spike timing and refractoriness.

The model shares conceptual ground with the [[adaptive-exponential-integrate-and-fire]] (AdEx) model, which also combines voltage integration with a recovery variable but uses exponential rather than quadratic coupling. Both models can be cast into a common framework of two-dimensional integrate-and-fire models, though they differ in their bifurcation structures and parameter sensitivity (see [[izhikevich-2010]]). In the context of [[whole-brain-modeling]], the Izhikevich model serves as a building block for mesoscale simulations, though simpler [[neural-mass-models]] like [[jansen-rit-model]] or [[wong-wang-model]] are more commonly used at the whole-brain scale due to their direct mapping to neuroimaging signals.

## Implementation and Software

The Izhikevich model is implemented in major [[spiking-neural-networks]] simulators including [[nest]] and [[brian2]]. In NEST, the model is available as `izhikevich` with parameters passed through the `a`, `b`, `c`, and `d` status dictionaries. The model supports both current-based and conductance-based synaptic input, enabling realistic network simulations with arbitrary connectivity structures. Implementation in Brian2 uses the ` equations` framework, allowing transparent extension to include additional currents or plasticity mechanisms.

## Relationship to TVB

Within [[the-virtual-brain]] framework, the Izhikevich model is not directly used as the primary neural mass model, which instead employs reduced models like the [[epileptor]] or [[jansen-rit-model]] that map more directly to [[neuroimaging-fmri]] signals. However, TVB's integration with NEST through [[tvb-nest]] enables hybrid simulations where Izhikevich neurons can be embedded within whole-brain connectome frameworks. This approach is particularly valuable for studying [[epilepsy-modeling]] at the mesoscale, where detailed single-neuron dynamics inform population-level seizures, and for investigating how [[brain-stimulation]] interventions modulate network dynamics at the cellular level. The model's computational efficiency makes it suitable for exploring [[parameter-estimation]] in large-scale networks where biologically constrained parameters need to be fitted to empirical functional connectivity data.

## Limitations

Despite its versatility, the Izhikevich model has several known limitations. First, the four parameters ($a$, $b$, $c$, $d$) lack direct biophysical interpretability—unlike conductance-based models where parameters correspond to specific ion channel properties, the Izhikevich parameters are phenomenological and must be fitted empirically to match desired firing patterns. Second, the standard model cannot reproduce subthreshold oscillations without explicit extensions or additional variables; real neurons often exhibit graded subthreshold responses that require modifications to the vanilla formulation. Third, the hard voltage reset (the instantaneous jump to $c$ when $v$ reaches 30 mV) is a mathematical artifact that discards information about the exact spike shape and timing, limiting the model's utility for studying spike-timing-dependent [[plasticity]] or precise spike coordination. These limitations should be considered when selecting the Izhikevich model for applications requiring biophysical detail or subthreshold dynamics.