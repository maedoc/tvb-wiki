---
title: Variational Bayes
created: 2022-03-10
updated: 2026-04-24
type: concept
tags: [variational-bayes, parameter-estimation, free-energy-principle, mean-field-theory, stochastic-differential-equations, dynamic-causal-modeling, whole-brain, tvb]
sources: [raw/papers/friston-2007.md, raw/papers/beal-2003.md, raw/papers/blei-kucukelbir-mcauliffe-2017.md]
---

## Opening paragraph
Variational Bayes (VB) is a family of deterministic algorithms that approximate Bayesian posterior distributions by solving an optimisation problem. By replacing intractable integration with the maximisation of a tractable lower bound on the model evidence, VB enables fast approximate inference for high‑dimensional neuro‑computational models.

## Motivation / Context
Exact Bayesian inference rapidly becomes computationally prohibitive when the likelihood couples many latent variables, as is typical for large‑scale brain models such as those implemented in the [[tvb]] simulator or in [[dynamic-causal-modeling]] (DCM). Traditional sampling techniques like Markov chain Monte Carlo (MCMC) can require days of computation for a single subject, limiting their use in population studies and real‑time applications. VB provides a principled alternative: it yields an approximation to the posterior while also delivering a lower bound on the marginal likelihood (the **evidence lower bound**, ELBO), which can be used for model comparison and automatic complexity control. This dual capability aligns with the goals of the [[free-energy-principle]] and underlies many contemporary neuroimaging pipelines.

## Technical content
### Evidence Lower Bound (ELBO)
For a model with latent variables \\(\\theta\\) and observed data \\(y\\), the marginal likelihood can be decomposed as  

\\[
\\log p(y) = \\mathcal{L}(q) + \\mathrm{KL}\\big(q(\\theta) \\| p(\\theta|y)\\big),
\\]

where \\(\\mathcal{L}(q) = \\mathbb{E}_{q}\\big[\\log p(y,\\theta) - \\log q(\\theta)\\big]\\) is the ELBO and \\(\\mathrm{KL}\\) denotes the Kullback‑Leibler divergence. Maximising \\(\\mathcal{L}(q)\\) tightens the bound and drives \\(q(\\theta)\\) toward the true posterior. In practice, the ELBO is expressed as a sum of expected log‑likelihood and a negative entropy term, both of which are analytically tractable under suitable approximations.

### Mean‑field approximation
The most common VB strategy assumes a factorised variational family,  

\\[
q(\\theta) = \\prod_{i} q_i(\\theta_i),
\\]

which decouples the high‑dimensional posterior into a set of lower‑dimensional factors. Coordinate ascent variational inference (CAVI) updates each factor in turn while holding the others fixed, yielding closed‑form updates for conjugate exponential‑family models [[beal-2003]]. This **mean‑field** approach dramatically reduces computational cost but can underestimate posterior correlations.

### Laplace approximation and extensions
When the posterior is approximately Gaussian, the Laplace approximation centres a multivariate normal distribution at the mode of \\(p(\\theta|y)\\) and uses the inverse Hessian as the covariance matrix [[friston-2007]]. The Laplace method is often employed within DCM to obtain analytic expressions for the ELBO, facilitating rapid model inversion. More recent work incorporates **structured** variational families that capture limited dependencies, and **stochastic variational inference** (SVI) that scales to massive datasets by using minibatches of data and noisy gradient estimates [[blei-2017]].

### Black‑box variational inference
Black‑box VI (BBVI) replaces analytic expectations with Monte‑Carlo estimates, allowing arbitrary differentiable models to be fitted with gradients computed by automatic differentiation. BBVI bridges the gap between the flexibility of deep learning frameworks and the principled Bayesian treatment needed for neuro‑computational models, making it feasible to embed VB inside the [[tvb]] multiscale pipeline.

## Relationships to other inference methods
VB sits alongside several alternative approximate inference schemes. Compared with MCMC, VB is orders of magnitude faster but provides only an approximation that can be biased toward under‑dispersion. **Expectation propagation** (EP) offers a different factor‑wise approximation that often yields more accurate marginal moments but at higher computational cost. **Variational message passing** (VMP) extends mean‑field updates to factor graphs, offering a unifying language for many probabilistic programs. In practice, the choice between VB, EP, and MCMC depends on the trade‑off between speed, accuracy, and the need for model evidence for selection.

## Biological grounding and applications
In neuroimaging, VB underlies the estimation of effective connectivity parameters in DCM, where latent neuronal states are modelled by [[neural-mass-model]] equations and linked to observed haemodynamic or electrophysiological signals. The variational free energy computed during inference serves as a proxy for model evidence, enabling principled comparison of competing connectivity architectures (e.g., different hypotheses about cortical hierarchy). Within the [[tvb]] ecosystem, VB is employed for fitting whole‑brain models to resting‑state [[fmri]] or [[meg]] data, allowing subject‑specific structural connectomes derived from diffusion MRI to be combined with neural mass dynamics. The resulting personalised models can predict functional connectivity patterns, simulate disease‑related perturbations, and inform neuromodulation strategies.

## Limitations and open questions
Despite its efficiency, VB’s reliance on factorised approximations can miss important posterior correlations, potentially leading to over‑confident inferences about connectivity strengths. Recent advances such as **hierarchical VAEs** and **normalising‑flow variational families** aim to remedy this but have yet to be fully integrated into large‑scale brain modelling frameworks. Moreover, the interpretation of the ELBO as a biologically meaningful free energy remains an active philosophical debate within the [[free-energy-principle]] community. Ongoing research seeks to quantify the impact of approximation error on downstream neuroscientific conclusions and to develop diagnostic tools for assessing variational quality in high‑dimensional brain models.
