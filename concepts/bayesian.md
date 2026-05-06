---
created: 2026-05-06
sources:
- raw/papers/david-friston-2003.md
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/semanticscholar-b9acfa0a7c80.md
tags:
- bayesian
- statistics
- computational-neuroscience
- inference
- modeling
title: Bayesian Inference
type: concept
updated: '2026-05-06'
---

# Bayesian Inference

**Bayesian inference** is a statistical framework for updating beliefs about parameters or hypotheses based on observed evidence. In [[computational-neuroscience]], Bayesian methods are used for [[parameter-estimation]], model comparison, and uncertainty quantification in brain models.

## Overview

Bayesian inference treats parameters as random variables with prior distributions that are updated by likelihood functions derived from data:

$$P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)}$$

Key applications in neuroscience include:
- Dynamic Causal Modeling (DCM) for [[effective-connectivity]]
- Bayesian model selection and averaging
- Parameter estimation in [[neural-mass-models]]
- Source reconstruction in EEG/MEG
- [[connectivity]] estimation from [[neuroimaging]] data

## Relationship to TVB

Bayesian methods are central to TVB [[model-validation]] and personalization:
- **Parameter estimation**: Bayesian approaches estimate neural mass model parameters from empirical data
- **Model comparison**: Bayesian model evidence compares competing TVB configurations (different connectivity, different models)
- **Uncertainty quantification**: Bayesian posterior distributions capture parameter uncertainty in [[whole-brain]] models
- [[dynamic-causal-modeling]] in SPM uses Bayesian inference, and DCM connectivity estimates inform TVB simulations
- The [[variational-bayes]] algorithm enables scalable Bayesian inference for large-scale [[connectome]] models

## Related Concepts

- [[variational-bayes]] — approximate Bayesian inference for large models
- [[dynamic-causal-modeling]] — Bayesian framework for effective connectivity
- [[modeldb]] — comparing alternative brain models
- [[connectomedb]] — inferring connectivity from data

## References

1. O. David, K.J. Friston. *Dynamic causal modelling*. NeuroImage. [DOI](https://doi.org/10.1016/S1053-8119(03)00202-7)
2. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI): A flexible and integrative toolkit for efficient probabilistic inference on virtual brain models*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.01.21.633922))
3. Abolfazl Ziaeemehr, M. Woodman, Lia Domide, S. Petkoski, V. Jirsa, Meysam Hashemi. (2025). *Virtual Brain Inference (VBI), a flexible and integrative toolkit for efficient probabilistic inference on whole-brain models*. eLife. [DOI](](https://doi.org/10.7554/eLife.106194))