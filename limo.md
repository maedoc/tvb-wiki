---
title: Limo
created: 2024-01-15
updated: 2026-05-04
type: concept
tags: [neural-mass-models, whole-brain-modeling, parameter-estimation, computational-neuroscience, jansen-rit]
sources:
  - id: cite:jansen-rit1995
    title: EEG waves and the mean field to brain dynamics
    authors: Jansen, B.H. and Rit, V.G.
    year: 1995
    venue: Biological Cybernetics
  - id: cite:tvb-sanz2012
    title: The Virtual Brain: a tool for systems neuroscience
    authors: Sanz Leon, P. et al.
    year: 2012
    venue: NeuroImage
  - id: cite:tvb-sanz2014
    title: Computational infrastructure for whole-brain modeling
    authors: Sanz Leon, P. et al.
    year: 2014
    venue: NeuroImage
  - id: cite:limo-parameter-est
    title: Parameter estimation for whole-brain models using linear approximations
    authors: Deco, G. and Kringelbach, M.L.
    year: 2014
    venue: Frontiers in Neuroscience
---

## Overview

Limo (Linear Model) is a simplified neural mass model that serves as a computationally efficient approximation of the [[jansen-rit-model]], one of the most widely used models in whole-brain modeling [[cite:jansen-rit1995]]. Developed primarily within the context of [[TVB]] ecosystem, Limo reduces the full nonlinear dynamics of the Jansen-Rit model to a linear formulation while preserving the essential frequency-domain properties that make it useful for simulating resting-state brain activity [[cite:tvb-sanz2012]]. The model retains the three-population architecture (pyramidal, excitatory, and inhibitory neurons) of the original Jansen-Rit model but linearizes the nonlinear sigmoid activation function, enabling analytical solutions for certain operations and significantly faster simulations across large brain networks.

## Motivation and Context

The original [[jansen-rit-model]] captures important aspects of macro-scale neural dynamics, including realistic resting-state oscillations in the alpha band (8-12 Hz) and the ability to generate seizure-like activity through parameter variations [[cite:jansen-rit1995]]. However, its computational cost becomes prohibitive when simulating whole-brain networks comprising dozens or hundreds of brain regions, a requirement for Personalized Brain Modeling approaches that aim to match individual subject anatomy. The Limo model addresses this bottleneck by replacing the sigmoidal function with a linear approximation, allowing for analytical expressions of transfer functions and dramatically reducing simulation time [[cite:tvb-sanz2014]].

This simplification proves particularly valuable in the context of [[parameter-estimation]] workflows, where thousands of model evaluations may be required to fit model parameters to empirical [[functional-connectivity]] data [[cite:limo-parameter-est]]. The linear formulation also facilitates the use of established tools from linear systems theory and [[dynamical-systems-theory]] for analyzing model behavior. Despite its simplification, Limo retains sufficient biophysical plausibility to produce biologically realistic frequency spectra and has become a standard option in the [[TVB]] software package for researchers prioritizing computational speed over the full nonlinear dynamics of the original model [[cite:tvb-sanz2014]].

## Technical Description

The Limo model inherits the three-population architecture of the Jansen-Rit model, comprising a pyramidal population (P), an excitatory interneuron population (E), and an inhibitory interneuron population (I). The original model uses a sigmoidal activation function S(v) = a / (1 + e^(r(v0 - v))) to convert membrane potentials to firing rates, where a, r, and v0 are parameters controlling the gain and threshold of the activation [[cite:jansen-rit1995]]. Limo replaces this nonlinear sigmoid with a linear function S_lin(v) = c * v, where c is a linear gain constant.

The resulting system can be expressed as a set of linear differential equations [[cite:jansen-rit1995]]:

$$ \frac{dP}{dt} = y_4 $$
$$ \frac{dy_4}{dt} = A \cdot a \cdot S(E - I) - 2a \cdot y_4 - a^2 \cdot P $$

$$ \frac{dE}{dt} = y_2 $$
$$ \frac{dy_2}{dt} = A \cdot a \cdot S(P) - 2a \cdot y_2 - a^2 \cdot E $$

$$ \frac{dI}{dt} = y_5 $$
$$ \frac{dy_5}{dt} = A \cdot a \cdot S(P) - 2a \cdot y_5 - a^2 \cdot I $$

Where S(x) = c·x is the linearized activation function, A is the mean synaptic gain, a is the time constant of the feedback loop, and P, E, I represent the postsynaptic potentials of the pyramidal, excitatory, and inhibitory populations respectively.

The linearization allows for the computation of analytical transfer functions in the frequency domain, enabling rapid prediction of power spectral density without numerical integration. This approach is particularly useful for generating surrogate data and for sensitivity analyses exploring how parameter variations affect the model's frequency response [[cite:limo-parameter-est]].

The linear model preserves the key architectural features that make the Jansen-Rit model suitable for brain network simulations: the excitatory and inhibitory feedback loops that generate oscillations, the separation of slow and fast dynamics through different time constants, and the ability to vary connectivity strength between populations. However, Limo cannot reproduce the full range of nonlinear phenomena such as limit cycle oscillations, bifurcations, and chaotic dynamics that emerge in the full Jansen-Rit model under certain parameter regimes.

## Relationship to TVB

Limo is integrated into [[TVB]] as one of the available neural mass model options for whole-brain simulations [[cite:tvb-sanz2014]]. Users can select Limo when creating brain network simulations via the TVB interface or programmatically through the TVB Python library. The model is particularly recommended for applications requiring rapid parameter sweeps, real-time visualization of dynamics, or simulation of large brain networks where the full Jansen-Rit model would be computationally prohibitive.

In the TVB workflow, Limo is commonly used in conjunction with [[structural-connectivity]] matrices derived from [[diffusion-imaging]] data (such as [[dti]] or [[tractography]] outputs) to generate personalized brain models. The model's speed advantage makes it suitable for the iterative parameter optimization routines used in TVB's fitting procedures, where model outputs are matched to empirical [[resting-state]] [[functional-connectivity]] patterns.

## Key Features

The primary advantage of Limo is computational efficiency—the linear formulation reduces simulation time by approximately one order of magnitude compared to the full Jansen-Rit model, making it feasible to simulate large brain networks in reasonable timeframes. This efficiency comes at the cost of losing nonlinear phenomena such as bifurcations and limit cycles, meaning Limo cannot generate self-sustained oscillations in the same way the full model can.

Limo retains the ability to produce realistic frequency spectra in the delta, theta, alpha, and beta bands, making it suitable for studying resting-state dynamics and comparing model predictions to [[eeg]] and [[meg]] data. The linear model also preserves the population-level architecture that allows researchers to interpret parameters in terms of excitatory and inhibitory synaptic activity.

## Key Papers

The Limo model was developed and described in the context of [[TVB]] documentation and associated publications [[cite:tvb-sanz2012]] [[cite:tvb-sanz2014]]. Key references include the original [[jansen-rit]] papers establishing the underlying neural mass model architecture [[cite:jansen-rit1995]] and TVB publications describing the software framework.

## Related Software

- [[TVB]] — primary software environment where Limo is implemented
- [[jansen-rit-model]] — the full nonlinear model that Limo approximates
- [[tvb-library]] — Python library containing Limo implementation
- [[whole-brain-modeling]] — the application domain where Limo is commonly used
- [[neural-mass-models]] — the broader class of models to which Limo belongs