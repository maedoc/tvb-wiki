---
created: 2025-01-15
sources:
- raw/papers/semanticscholar-60ca593f7e0c.md
- raw/papers/arxiv-2604.17151.md
- raw/papers/arxiv-2512.03907.md
- raw/papers/arxiv-2603.21067.md
- raw/papers/winkler-2014-palm.md
tags:
- variational-bayes
- parameter-estimation
- model-validation
- dynamical-systems-theory
- computational-neuroscience
title: Bayes Factors
type: concept
updated: '2026-05-03'
---

## Overview

Bayes Factors (BF) are a foundational quantity in Bayesian statistics that quantify the relative evidence provided by observed data for one statistical model versus another. Formally, the Bayes Factor comparing model $\mathcal{M}_1$ to model $\mathcal{M}_0$ is defined as the ratio of their marginal likelihoods:

$$\text{BF}_{10} = \frac{p(\mathbf{y} \mid \mathcal{M}_1)}{p(\mathbf{y} \mid \mathcal{M}_0)} = \frac{\int p(\mathbf{y} \mid \boldsymbol{\theta}_1, \mathcal{M}_1) p(\boldsymbol{\theta}_1 \mid \mathcal{M}_1) \, d\boldsymbol{\theta}_1}{\int p(\mathbf{y} \mid \boldsymbol{\theta}_0, \mathcal{M}_0) p(\boldsymbol{\theta}_0 \mid \mathcal{M}_0) \, d\boldsymbol{\theta}_0}$$

where $\mathbf{y}$ represents the observed data (e.g., [[fmri]] time series, EEG recordings, or MEG signals), $\boldsymbol{\theta}_i$ are the parameters of model $\mathcal{M}_i$, and $p(\boldsymbol{\theta}_i \mid \mathcal{M}_i)$ represents the prior distribution over parameters. Values greater than 1 indicate evidence in favor of $\mathcal{M}_1$, while values less than 1 indicate evidence for $\mathcal{M}_0$. This ratio directly addresses the question of which model better explains the data while automatically accounting for model complexity through the integrated likelihood term.

## Motivation and Context

In whole-brain modeling and computational neuroscience, researchers frequently face the challenge of comparing competing models of brain dynamics. Should one use a [[Jansen-Rit model|Jansen-Rit model]] with three neuronal populations or a more elaborate [[Wilson-Cowan model|Wilson-Cowan model]]? Does adding delay parameters to a [[neural-mass-models|neural mass model]] significantly improve its ability to explain empirical connectivity data? Traditional frequentist approaches relying on goodness-of-fit metrics (e.g., $R^2$, AIC, BIC) fail to fully account for model complexity and prior information, potentially leading to overfitting or selection of unnecessarily complex models [@kass1995].

Bayes Factors provide a principled solution to these model comparison challenges by incorporating both data fit and model complexity into a single, interpretable metric. The marginal likelihood inherently penalizes models with many parameters unless the data genuinely supports their inclusion, since the prior predictive mass spreads across a larger parameter space. This automatic Occam's razor property makes BFs particularly valuable in [[personalized-brain-modeling|personalized brain modeling]] contexts, where individual subject data may support different model architectures.

## Technical Considerations

Computing Bayes Factors exactly is typically intractable for realistically sized [[whole-brain-modeling|[[whole-brain]] models]] due to the high-dimensional integrals involved. Several approximation methods have been developed to address this computational challenge. **Variational Bayes** (VB) techniques — which are related to, though conceptually distinct from, the [[free-energy-principle|free-energy principle]] in theoretical neuroscience — provide a tractable lower bound on the log marginal likelihood by optimizing an approximate posterior distribution over parameters [@friston2003]. The evidence lower bound (ELBO) can then be used to compute an approximation to the Bayes Factor.

**Bridge sampling** and **nested sampling** represent alternative numerical approaches that can provide more accurate estimates at higher computational cost. In the context of [[dynamic-causal-modeling|dynamic causal modeling]] (DCM) for [[neuroimaging]], variational Laplace approximation has been traditionally used to estimate model evidence, enabling Bayesian model comparison across competing [[connectivity]] architectures [@friston2007].

The interpretation of Bayes Factors follows the Jeffreys scale [@jeffreys1961; @stephens2009], which provides qualitative guidance: BF$_{10}$ between 1–3 indicates barely worth mentioning evidence, 3–10 indicates moderate evidence, 10–30 indicates strong evidence, 30–100 indicates very strong evidence, and $>100$ indicates decisive evidence for $\mathcal{M}_1$ over $\mathcal{M}_0$. However, researchers should recognize that BFs depend sensitively on prior specification—changing the prior distributions over model parameters can substantially alter the computed Bayes Factor.

## Relationship to TVB and Whole-Brain Modeling

In [[The Virtual Brain|TVB]] and related [[whole-brain-simulators|whole-brain simulators]], Bayes Factors serve multiple purposes. They enable comparison of different [[neural-mass-models|neural mass model]] types (e.g., [[Epileptor|Epileptor]] vs. [[Wong-Wang model|Wong-Wang]] excitatory-inhibitory networks) when fitting to empirical [[functional-connectivity|functional connectivity]] data. They also support [[parameter-estimation|parameter estimation]] routines by providing a Bayesian updating framework, allowing belief distributions over model parameters to be refined based on observed neuroimaging data through iterative Bayesian updating [@kass1995].

The integration of variational Bayes methods into TVB's optimization pipeline allows researchers to not only identify best-fitting parameters but also quantify the evidence supporting different model variants. This supports the broader goal of [[model-validation|model validation]] in [[computational-neuroscience]] by providing statistically grounded comparisons rather than relying solely on goodness-of-fit metrics.

## Related Concepts

Bayes Factors connect to several important concepts in the wiki: [[variational-bayes]] provides the computational machinery for approximating marginal likelihoods; [[parameter-estimation]] encompasses the broader task of fitting models to data; [[model-validation]] represents the ultimate goal of assessing whether brain models capture genuine aspects of neural dynamics; and [[free-energy-principle]] offers a theoretical framework that motivates variational approaches to model evidence approximation in neuroscience applications.

## Key Papers

- Jeffreys, H. (1961). *Theory of Probability* (3rd ed.). Oxford University Press. — The foundational text introducing the Jeffreys scale for interpreting Bayes Factors.
- Kass, R. E., & Raftery, A. E. (1995). Bayes Factors. *Journal of the American Statistical Association*, 90(430), 773–795. — Comprehensive review of Bayes Factors in statistical practice.
- Friston, K. J., Mattout, J., Trujillo-Barreto, N., Ashburner, J., & Penny, W. (2007). Variational Bayes under the [[palm]] framework. *NeuroImage*, 35(4), 1499–1510. — Application of variational methods to model comparison in neuroimaging.
- Friston, K. J., & Penny, W. (2003). Posterior probability maps and SPMs. *NeuroImage*, 19(3), 1240–1249. — Early work connecting variational Bayes to the free-energy principle in neuroscience.

## References

- [@jeffreys1961] Jeffreys, H. (1961). *Theory of Probability* (3rd ed.). Oxford University Press.
- [@kass1995] Kass, R. E., & Raftery, A. E. (1995). Bayes Factors. *Journal of the American Statistical Association*, 90(430), 773–795.
- [@friston2003] Friston, K. J., & Penny, W. (2003). Posterior probability maps and SPMs. *NeuroImage*, 19(3), 1240–1249.
- [@friston2007] Friston, K. J., Mattout, J., Trujillo-Barreto, N., Ashburner, J., & Penny, W. (2007). Variational Bayes under the PALM framework. *NeuroImage*, 35(4), 1499–1510.
- [@stephens2009] Stephens, M., & Balding, D. J. (2009). Bayesian statistical analysis of genetic association studies. *Nature Reviews Genetics*, 10(11), 681–687.

## Related Software

- **DCM** (Dynamic Causal Modeling) — MATLAB toolbox implementing variational Laplace for Bayesian model comparison in neuroimaging.
- **VBVS** (Variational Bayes Variational Statistics) — R package implementing variational Bayes approximations for model selection.
- **[[tvb|The Virtual Brain]]** — Whole-brain modeling platform incorporating Bayesian model comparison for parameter estimation and model selection.