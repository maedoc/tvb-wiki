---
created: 2025-01-01
sources:
- raw/papers/semanticscholar-60ca593f7e0c.md
tags:
- whole-brain-modeling
- neural-mass-models
- connectomics
- structural-connectivity
- functional-connectivity
- network-dynamics
- dynamical-systems-theory
- mean-field-theory
- parameter-estimation
- personalized-brain-modeling
title: Whole-Brain Modeling
type: concept
updated: '2026-05-15'
---

# Whole-Brain Modeling

Whole-brain modeling is a computational neuroscience approach that simulates neural dynamics across the entire brain using empirically derived [[structural-connectivity]] data. Unlike region-specific or cell-type-specific models, whole-brain models integrate large-scale anatomical connectivity — typically from [[diffusion-imaging]] and [[tractography]] — to constrain the dynamics of coupled neural populations spanning dozens to hundreds of brain regions. The goal is to reproduce and predict macroscopic phenomena observed in [[neuroimaging-fmri]], [[neuroimaging-eeg]], and [[neuroimaging-meg]], providing a mechanistic bridge between brain structure and function.

## Motivation

The brain is fundamentally a network: local circuits process information within specialised regions, but those regions communicate over long-range white-matter pathways to produce coordinated cognition and behaviour. Studying regions in isolation fails to capture emergent properties that arise only from large-scale coupling — such as [[resting-state]] [[functional-connectivity]] networks, oscillatory synchronisation, and state transitions. Whole-brain modeling addresses this gap by treating the brain as a single dynamical system whose behaviour emerges from the interplay of local node dynamics and the global [[structural-connectivity]] scaffold.

This approach gained traction as advances in [[diffusion-imaging]] made subject-specific connectomes available at scale, and as computational power reached a threshold where simulating networks of tens to hundreds of coupled neural populations became tractable. Whole-brain models now serve as virtual laboratories for testing hypotheses about brain organisation, predicting the effects of lesions or stimulation, and generating candidate biomarkers for neurological and psychiatric conditions including [[epilepsy-modeling]], [[schizophrenia-models]], and [[alzheimers-modeling]].

## Technical Foundations

At their core, [[whole-brain]] models couple local dynamical models — typically [[neural-mass-models]] or [[mean-field-theory]] reductions of spiking networks — through a structural [[connectivity]] matrix _W_, where each entry _Wᵢⱼ_ encodes the anatomical connection strength from region _j_ to region _i_. The generic form for a network of _N_ regions is:

\[
\dot{x}_i = f(x_i, \theta_{\text{local}}) + G \sum_{j=1}^{N} W_{ij} \, g(x_i, x_j)
\]

Here _xᵢ_ is the state vector of region _i_, _f_ captures the local dynamics with parameters _θ_local_, _G_ is a global coupling parameter that scales the influence of long-range inputs, and _g_ is a coupling function — typically diffusive (depending on _xⱼ_ − _xᵢ_) or directed (depending on _xⱼ_ alone). The structural connectivity matrix _W_ is commonly normalised row-wise or by the maximum eigenvalue to ensure [[network-dynamics]] remain bounded as _G_ varies.

The choice of local node model depends on the phenomenon of interest. For simulating [[resting-state]] [[functional-connectivity]], the reduced Wong–Wang model and dynamic mean-field formulations are widely used because they generate realistic BOLD-like time series at low computational cost. For investigating oscillatory dynamics, rhythm-generating models such as the Jansen–Rit model capture alpha-band activity and seizure-like transitions. Biologically richer formulations — including [[mean-field-theory]] reductions of [[spiking-neural-networks]] such as the [[adaptive-exponential-integrate-and-fire]] neuron — bridge the gap between mesoscopic population models and cellular-level biophysics.

## Model Fitting and Validation

Whole-brain models contain free parameters — including the global coupling _G_ and parameters of the local node dynamics — that must be tuned so the model output matches empirical data. The most common validation target is the empirical [[functional-connectivity]] (FC) matrix, computed as the Pearson correlation between [[bold-signal|BOLD]] time series of all region pairs. Model FC is computed by simulating the system, convolving the resulting neural activity with a haemodynamic response function to produce synthetic BOLD signals, and then correlating. The fit between model FC and empirical FC, quantified by the Pearson correlation between the upper triangles of the two matrices, serves as an objective function for [[parameter-estimation]] via grid search, [[bayesian]] optimisation, or gradient-based methods.

Fitting to [[functional-connectivity]] alone can produce models that reproduce static FC well but fail to capture dynamic features such as metastability or time-varying FC states. More recent validation frameworks incorporate additional constraints, including the switching rate between functional connectivity configurations, spectral content of regional time series, and the fit to [[effective-connectivity]] measures derived from [[dynamic-causal-modeling]].

## Relationship to The Virtual Brain

[[the-virtual-brain|The Virtual Brain (TVB)]] is the most comprehensive software platform for constructing, simulating, and analysing whole-brain models. TVB integrates subject-specific [[structural-connectivity]] matrices, a library of built-in [[neural-mass-models]] — including the generic 2D oscillator, reduced Wong–Wang, Jansen–Rit, Stefanescu–Jirsa 3D, and reduced epileptor models — configurable coupling functions, and forward solutions for generating synthetic [[neuroimaging-fmri]], [[neuroimaging-eeg]], and [[neuroimaging-meg]] signals. The platform encapsulates the entire whole-brain modeling workflow from importing connectivity data through parameter exploration to model fitting and visualisation, making the approach accessible to researchers without requiring them to implement numerical solvers or coupling schemes from scratch.

## Open Questions

Several challenges remain active areas of investigation. The inference of [[structural-connectivity]] from [[tractography]] introduces biases — including a tendency to over-represent short-range connections and under-represent inter-hemispheric projections — that propagate into model predictions. The appropriate level of biophysical detail in the local node model is debated: simpler models often fit [[functional-connectivity]] comparably to more complex ones, raising questions of model identifiability. Finally, standard whole-brain models are deterministic, yet empirical brain dynamics exhibit substantial variability across time and individuals, motivating the development of stochastic and [[personalized-brain-modeling]] approaches that incorporate subject-specific parameter estimates and noise models.