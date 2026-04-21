---
title: "Dynamic causal modelling"
created: 2026-04-20
updated: 2026-04-20
type: source
tags: [paper-methods, dynamic-causal-modeling, effective-connectivity, whole-brain-modeling, neuroimaging-fmri]
sources: []
---

# Dynamic causal modelling

**Authors**: O. David, K.J. Friston  
**Published**: 2003  
**Journal**: NeuroImage  
**DOI**: 10.1016/S1053-8119(03)00202-7

## Summary

Foundational paper introducing Dynamic Causal Modeling (DCM) for neuroimaging data analysis. DCM uses neural mass models as generative models to infer effective connectivity from fMRI, EEG, and MEG data through Bayesian inversion.

## Key Contributions

- DCM framework coupling neural mass models to forward models for neuroimaging
- Bayesian model inversion for connectivity inference
- Separation of neural state dynamics from observation equations
- Application to fMRI effective connectivity analysis

## DCM Structure

- **Neural level**: Jansen-Rit or similar neural mass model describing population dynamics
- **Forward model**: Balloon model (fMRI), electromagnetic forward model (EEG/MEG)
- **Bayesian inversion**: Estimating parameters given neuroimaging observations

## Related Concepts

- [[dynamic causal modeling]]
- [[neural mass model]]
- [[Jansen-Rit]]
- [[effective connectivity]]
- [[functional connectivity]]
