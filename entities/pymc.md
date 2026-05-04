---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/semanticscholar-b9acfa0a7c80.md
- raw/papers/sanz-leon-2013.md
tags:
- software-brian
- software-neuron
- parameter-estimation
- variational-bayes
- computational-neuroscience
- bayes-factors
title: PyMC
type: entity
updated: '2026-05-04'
---

# PyMC

## Overview

PyMC (formerly PyMC3) is an open-source Python library for probabilistic programming that provides tools for Bayesian statistical modeling and inference. It enables researchers to specify complex probabilistic models using Python code and perform inference using Markov Chain Monte Carlo (MCMC) methods, variational inference, and other approximation techniques. Originally developed by John Salvatier, Thomas Wiecki, and Christopher Fonnesbeck in 2012 [@pymc-docs], PyMC has become one of the most widely used frameworks for Bayesian analysis in Python, with applications spanning [[neuroimaging]], epidemiology, and [[computational-neuroscience]].

## Key Features

PyMC provides several core capabilities that make it valuable for [[whole-brain|whole-brain modeling]] applications. The library implements current MCMC samplers including the No-U-Turn Sampler (NUTS), which automatically tunes its integration parameters and provides efficient sampling from high-dimensional posterior distributions. NUTS, developed by Matthew Hoffman and Andrew Gelman, is particularly valuable for fitting the large parameter sets characteristic of whole-brain models, where computational efficiency can dramatically impact research throughput [@hoffman-gelman-nuts].

Beyond MCMC sampling, PyMC supports variational Bayesian inference through the ADVI (Automatic Differentiation Variational Inference) algorithm. This allows for fast approximation of posterior distributions when exact inference is intractable, which is often the case with biologically realistic [[neural-mass-models]] containing nonlinearities and delays. The variational inference approach is especially useful for initial exploration of parameter spaces and for models where MCMC sampling proves computationally prohibitive [@advi-paper].

The library integrates tightly with NumPy and SciPy, using Theano (and now PyTensor) for automatic differentiation. This enables gradient-based inference methods that scale to large models. PyMC also provides built-in tools for model diagnosis, including trace plots, divergent transitions detection, and posterior predictive checks—all essential for validating that inference has proceeded correctly when fitting brain models to empirical data.

## Relationship to TVB

PyMC plays an important role in the [[the-virtual-brain]] ecosystem as a tool for [[parameter-estimation]] and model fitting. Whole-brain models constructed in TVB typically contain numerous free parameters—including conduction delays, coupling strengths, and neural mass model constants—that must be estimated from empirical neuroimaging data. Bayesian inference provides a principled framework for this estimation, naturally handling the uncertainty inherent in fitting complex models to noisy measurements of brain activity.

Researchers have explored integrating PyMC with TVB for performing Bayesian parameter estimation on whole-brain [[connectivity]] models. This integration allows researchers to not only find point estimates of model parameters but also obtain full posterior distributions quantifying uncertainty in each parameter estimate. Such uncertainty quantification is essential for [[personalized-brain-modeling]], where understanding the reliability of individual parameter estimates informs confidence in downstream clinical applications.

Furthermore, PyMC enables comparison of competing [[whole-brain-modeling|whole-brain model]] architectures using Bayesian model comparison. By computing Bayes factors (see [[bayes-factors]]) between models with different structural assumptions—such as differences in neural mass model formulation or connectivity scaling—researchers can rigorously evaluate which model architecture better explains empirical data while accounting for model complexity.

## Technical Considerations

While PyMC provides powerful inference machinery, applying it to whole-brain modeling contexts presents specific challenges. The high dimensionality of whole-brain models—involving 80+ brain regions each with potentially multiple state variables—can lead to slow sampling and difficulties in achieving convergence. Researchers often employ dimensionality reduction strategies, such as using [[mean-field-theory|mean-field]] approximations that treat regions as independent conditionally on global coupling parameters, to render inference tractable.

The relationship between PyMC and the [[free-energy-principle]] framework warrants note. Both emphasize variational methods for approximate inference, and the ADVI implementation in PyMC can be viewed as a practical tool for implementing variational free energy minimization. This connection has motivated work applying PyMC-based inference to models framed within the predictive processing paradigm popular in theoretical neuroscience.

## Related Software

PyMC occupies a similar niche to other probabilistic programming frameworks including Stan, which offers a domain-specific language for model specification, and TensorFlow Probability, which provides probabilistic modeling primitives within the TensorFlow ecosystem. Within computational neuroscience specifically, PyMC complements the simulation-oriented approaches of [[brian]] and [[neuron]] by providing the inference machinery needed to fit such simulation models to data. The library also interfaces with [[nilearn]] for preprocessing neuroimaging data prior to model fitting.

## Key Papers

- Salvatier, J., Wiecki, T. V., & Fonnesbeck, C. (2016). Probabilistic programming in Python using PyMC3. *PeerJ Computer Science* [@pymc-docs]
- Hoffman, M. D., & Gelman, A. (2014). The No-U-Turn Sampler: adaptively setting path lengths in Hamiltonian Monte Carlo. *Journal of Machine Learning Research* [@hoffman-gelman-nuts]
- Kucukelbir, A., Ranganath, R., Gelman, A., & Blei, D. M. (2015). Automatic differentiation variational inference. *arXiv preprint* [@advi-paper]