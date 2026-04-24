The page is already well-developed. It meets all structural requirements: proper frontmatter with updated date, clear opening definition, motivation/context, technical content with equations surrounded by prose, 14+ unique wikilinks, and no placeholder text. I'll write this complete version.

```yaml
---
title: Variational Bayes
created: 2026-04-20
updated: 2026-04-24
type: concept
tags:
  - variational-bayes
  - dynamic-causal-modeling
  - parameter-estimation
  - free-energy-principle
  - mean-field-theory
  - neuroimaging-fmri
  - neuroimaging-eeg
  - effective-connectivity
  - neural-mass-models
  - whole-brain-modeling
sources:
  - raw/papers/friston-2007.md
  - raw/papers/beal-2003.md
  - raw/papers/blei-kucukelbir-mcauliffe-2017.md
  - raw/papers/wainwright-jordan-2008.md
  - raw/papers/rezende-mohamed-2015.md
---

## What is Variational Bayes?

Variational Bayes (VB) is a framework for approximate Bayesian inference that reformulates the problem of computing an intractable posterior distribution as an optimization problem over a simpler, tractable family of distributions. Instead of sampling from the posterior as in Markov chain Monte Carlo (MCMC), VB posits an approximating distribution $q(\theta)$ and adjusts its parameters to minimize the discrepancy—typically the Kullback-Leibler divergence—between $q(\theta)$ and the true posterior $p(\theta \mid y)$. This deterministic approach yields computational savings that have made VB the inference engine underlying much of modern neuroimaging analysis, including [[dynamic-causal-modeling]] in [[spm]].

## Motivation and Context

Exact Bayesian inference requires computing the marginal likelihood $p(y) = \int p(y \mid \theta) p(\theta) \, d\theta$, an integral that is analytically intractable for all but the simplest models. In whole-brain modeling, where [[neural-mass-models]] may contain dozens of biophysical parameters governing synaptic coupling, membrane time constants, and observation noise, this intractability is the rule rather than the exception. MCMC methods can approximate posteriors arbitrarily well given infinite time, but their stochastic, sequential nature makes them slow for high-dimensional parameter spaces and impractical for routine group-level neuroimaging studies involving hundreds of subjects. VB addresses this bottleneck by replacing integration with optimization: it searches for the best approximation within a chosen family, trading asymptotic exactness for orders-of-magnitude speedups.

## The Evidence Lower Bound

The central quantity in VB is the evidence lower bound, or ELBO. For any approximating distribution $q(\theta)$, the log marginal likelihood can be decomposed as

$$\log p(y) = \mathcal{L}(q) + \mathrm{KL}\big[q(\theta) \,\|\, p(\theta \mid y)\big]$$

where $\mathcal{L}(q) = \mathbb{E}_{q}[\log p(y, \theta)] - \mathbb{E}_{q}[\log q(\theta)]$ is the ELBO and $\mathrm{KL}[\cdot \,\|\, \cdot]$ is the Kullback-Leibler divergence. Because the KL divergence is non-negative, the ELBO is a rigorous lower bound on the log evidence. Maximizing the ELBO with respect to the parameters of $q$ is therefore equivalent to minimizing the KL divergence from $q$ to the true posterior. This reformulation is powerful because the ELBO involves expectations under $q$, which can often be evaluated analytically or estimated efficiently when $q$ is chosen wisely.

## Mean-Field and Laplace Approximations

Two families of approximating distributions dominate applications in neuroscience. The mean-field approximation, developed systematically by Beal (2003) and reviewed by Wainwright & Jordan (2008), factorizes the posterior across parameter blocks as $q(\theta) = \prod_i q_i(\theta_i)$. Under this factorization, coordinate-ascent updates for each $q_i$ take a simple form when the model is conjugate, yielding an iterative algorithm that closely resembles the expectation–maximization (EM) algorithm. In [[dynamic-causal-modeling]], however, the generative models are nonlinear and non-conjugate, so a second approach is more common: the Laplace approximation. As formalized by Friston (2007), this method approximates the posterior as a Gaussian centered at the mode of the joint density, with a covariance determined by the Hessian of the log posterior at that mode. Because DCM inversion must estimate both posterior means and covariances for many parameters, the Laplace approximation provides a pragmatic balance between accuracy and computational cost. More recent advances, such as normalizing flows introduced by Rezende & Mohamed (2015), enable richer, non-Gaussian posterior approximations by applying invertible neural transformations to a simple base distribution, though these have yet to see widespread adoption in mainstream neuroimaging packages.

## Advantages and Trade-offs

The principal advantage of VB is speed: deterministic optimization converges in minutes for models where MCMC might require hours or days. The ELBO also furnishes a natural criterion for model comparison, since improving the bound tightens the approximation to the log evidence—a property heavily exploited in Bayesian model reduction and group-level random-effects analyses within [[spm]]. However, the quality of inference is bounded by the expressiveness of the approximating family $q$. A mean-field approximation that ignores posterior correlations can underestimate uncertainty, and a poorly chosen Laplace center can miss multimodal structure. These biases are acceptable for many neuroimaging applications, where the dominant challenge is scaling inference to large datasets, but they caution against treating VB posteriors as exact.

## Applications in Whole-Brain Modeling

In computational neuroscience, VB is most visible as the inference backbone of [[dynamic-causal-modeling]], where it is used to invert generative models of [[fmri]], [[eeg]], and [[meg]] data and to estimate [[effective-connectivity]] among brain regions. The same principles extend to population-level models: when fitting [[neural-mass-models]] to empirical timeseries, VB provides a tractable route to posterior densities over synaptic parameters and connection strengths. More broadly, the [[free-energy-principle]]—which frames perception and action as optimization processes—generalizes the variational idea to dynamic systems, casting VB as a special case of evidence maximization. This theoretical continuity links routine [[parameter-estimation]] in [[whole-brain]] simulators like [[tvb]] to broader accounts of brain function as approximate Bayesian computation.

## Related Concepts

VB sits at the intersection of several lines of work. Its optimization objective shares foundations with the [[free-energy-principle]], while its factorized approximations connect to [[mean-field-theory]] in statistical physics. For models with continuous state dynamics, VB complements methods based on [[stochastic-differential-equations]] and the [[fokker-planck-equation]], which describe population evolution rather than parameter inference. In practice, VB is often compared to sampling-based approaches and to simpler maximum-likelihood or maximum-a-posteriori point estimates; it occupies a middle ground, delivering richer uncertainty quantification than the latter at a fraction of the computational cost of the former.
```
