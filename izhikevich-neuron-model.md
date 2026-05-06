---
title: Izhikevich Neuron Model
created: 2026-04-20
updated: 2026-05-06
type: concept
tags: [spiking-neural-networks, neural-mass-models, computational-neuroscience, bifurcation-analysis, nonlinear-dynamics]
sources: []
---

The Izhikevich neuron model is a two-dimensional differential equation model of neural spiking that achieves a remarkable balance between biological realism and computational efficiency. Introduced by Eugene Izhikevich in 2003, the model can reproduce essentially all known types of spiking behavior exhibited by cortical neurons while requiring only simple arithmetic operations, making it particularly suitable for large-scale brain simulations where computational resources are a constraint.

## Mathematical Formulation

The model is defined by the system of equations:

$$\frac{dv}{dt} = 0.04v^2 + 5v + 140 - u + I$$

$$\frac{du}{dt} = a(bv - u)$$

with the reset condition:
$$\text{if } v \geq 30 \text{ mV, then } v \leftarrow c \text{ and } u \leftarrow u + d$$

where **v** represents the membrane potential and **u** is a recovery variable that accounts for the activation of potassium currents and inactivation of sodium currents. The four dimensionless parameters **a**, **b**, **c**, and **d** control the model's dynamic behavior: **a** determines the recovery time constant, **b** controls the sensitivity of the recovery variable to the membrane potential, **c** sets the reset membrane potential after a spike, and **d** governs the reset of the recovery variable. This formulation emerged from the geometric theory of planar polynomial dynamical systems, where Izhikevich identified a quadratic membrane potential term that produces the characteristic spiking and resetting behavior with minimal computational overhead.

## Biological Plasticity and Firing Regimes

One of the model's most powerful features is its ability to capture diverse firing patterns through parameter variation. By adjusting the four parameters, the Izhikevich model can reproduce **tonic spiking** (regular sustained firing), **phasic spiking** (response to onset of stimulus only), **tonic bursting** (rhythmic clusters of spikes), **phasic bursting** (bursting only at stimulus onset), **mixed mode** (initial burst followed by steady spiking), ** Class 1 excitability** (continuous range of firing frequencies from zero), **Class 2 excitability** (abrupt onset of firing), and **spike-frequency adaptation**. This diversity reflects the rich dynamical behavior of real cortical neurons, which exhibit different firing patterns depending on cell type, cortical layer, and behavioral state. The model successfully mimics both excitatory pyramidal cells and inhibitory interneurons, capturing the fundamental distinction between regular-spiking and fast-spiking phenotypes observed in intracellular recordings.

## Relationship to Other Models

The Izhikevich model occupies a distinctive niche in the taxonomy of neuron models, positioned between highly simplified [[integrate-and-fire]] models and biophysically detailed models like the [[Hodgkin-Huxley model]]. Unlike the integrate-and-fire model, which resets artificially after each spike without modeling the recovery dynamics, the Izhikevich model's recovery variable **u** provides a phenomenological description of the ion channel kinetics that govern spike refractoriness. Compared to the [[FitzHugh-Nagumo model]], which was a pioneering planar model of neural excitability, the Izhikevich model uses a quadratic rather than cubic nonlinearity and includes a wider parameter regime that maps more directly to biological observation. The [[adaptive-exponential-integrate-and-fire]] (AdEx) model represents a more recent alternative that shares the philosophy of capturing diverse firing modes with few parameters, but uses exponential rather than quadratic nonlinearity and includes an explicit adaptation variable. These models collectively form the toolkit for researchers building [[spiking neural networks]] who must choose between biological fidelity, mathematical tractability, and computational cost.

## Computational Implementations

The Izhikevich model is implemented in all major [[spiking neural network]] simulators including [[NEST]], [[Brian2]], and NEURON. In [[NEST]], the model is available as `izhikevich_exp` for exponential integrate-and-fire dynamics and `izhikevich` for the canonical quadratic form described above. The model's computational efficiency stems from its avoidance of exponential functions in the core integration step; while the original formulation uses simple Euler integration, more accurate implementations employ adaptive step-size methods. For large-scale [[whole-brain modeling]] applications, the Izhikevich model has been used to populate cortical columns with heterogeneous neural populations that exhibit realistic firing statistics. The [[Virtual Brain]] framework specifically includes Izhikevich neurons as one option for the local network model when simulating brain regions, allowing users to construct multi-scale models that combine [[neural mass model|neural mass approximations]] at the whole-brain level with population-level spiking dynamics at the regional scale.

## Parameter Estimation and Validation

Parameter fitting for the Izhikevich model involves selecting the (a, b, c, d) tuple that produces desired firing characteristics. Analytical relationships exist between parameters and key neural properties: spike amplitude is controlled by c, spike width by d, and the frequency-current relationship by b. In practice, parameter optimization often employs evolutionary algorithms or gradient-based methods to match observed firing patterns from intracellular recordings. Validation typically involves comparing the model's output to experimentally measured spike trains using metrics such as spike timing reliability, frequency-current curves, and phase response curves. The Potjans-Diesmann cortical microcircuit model, which implements four cell types per cortical layer using Izhikevich dynamics, demonstrates how systematic parameterization can reproduce layer-specific firing rates consistent with in vivo measurements.

## Applications in Whole-Brain Modeling

In the context of [[whole-brain modeling]], the Izhikevich model serves as a neural substrate for constructing biologically realistic mean-field approximations. The model's ability to generate [[brain oscillations]] through network interactions makes it valuable for studying alterations in brain dynamics associated with neurological disorders. Research has applied Izhikevich-based networks to model [[epilepsy modeling|epileptic seizures]], where the transition to pathological bursting states emerges from parameter shifts in excitatory-inhibitory balance. The model's relatively low computational cost compared to biophysically detailed models enables simulations of large cortical networks that capture spatial structure while remaining tractable on modern GPU hardware.