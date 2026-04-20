---
title: "Dynamic Causal Modeling"
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [dynamic-causal-modeling, effective-connectivity, neuroimaging-fmri]
sources: [raw/papers/friston-2003-dcm.md, raw/papers/stephan-2010.md, raw/papers/daunizeau-david-stephan-2011.md, raw/papers/friston-2014-spectral-dcm.md]
---

## Definition
Dynamic Causal Modeling (DCM) is a Bayesian framework for inferring effective connectivity (directed causal influences) between brain regions from neuroimaging data using biologically informed neural mass models.

## Core Components

### Neural Mass Model
- State equations describe neural population dynamics
- Endogenous connectivity (A matrix)
- Modulatory inputs (B matrix)
- Driving inputs (C matrix)

### Observation Model
- Links neural states to measured signals
- fMRI: Balloon model of hemodynamics
- EEG/MEG: Electromagnetic forward model

### Bayesian Inference
- [[variational bayes]] for posterior estimation
- Model comparison using evidence
- Parameter priors from physiology

## Types of DCM

### fMRI DCM
- Deterministic or stochastic dynamics
- Nonlinear state equations
- Balloon hemodynamic model

### EEG/MEG DCM
- [[jansen-rit]] or [[wilson-cowan]] neural masses
- Electromagnetic forward model
- Frequency domain analysis

### Spectral DCM
- friston-2014-spectral-dcm for resting-state
- Stationary assumptions
- Cross-spectral density fitting

## Applications
- [[effective connectivity]] estimation
- Experimental modulation effects
- Clinical connectivity changes
- Model-based group comparisons

## Related Concepts
- [[effective connectivity]] — What DCM estimates
- [[variational bayes]] — Inference method
- [[neural mass model]] — Biological basis
- [[free energy principle]] — Theoretical foundation

## References
- friston-2003-dcm — Original DCM paper
- stephan-2010 — Practical guide
- daunizeau-david-stephan-2011 — Critical review
