# Amortized Simulation-Based Inference in Generalized Bayes via Neural Posterior Estimation

**Source**: semantic-scholar
**ID**: 6831479732d91a40bb1ecf57f93277649a188f9e
**DOI**: 10.48550/arXiv.2601.22367
**URL**: https://www.semanticscholar.org/paper/6831479732d91a40bb1ecf57f93277649a188f9e
**Date**: 2026-01-29
**Year**: 2026
**Authors**: Shiyi Sun, Geoff K. Nicholls, Jeong Eun Lee
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Generalized Bayesian Inference (GBI) tempers a loss with a temperature $\beta>0$ to mitigate overconfidence and improve robustness under model misspecification, but existing GBI methods typically rely on costly MCMC or SDE-based samplers and must be re-run for each new dataset and each $\beta$ value. We give the first fully amortized variational approximation to the tempered posterior family $p_\beta(\theta \mid x) \propto \pi(\theta)\,p(x \mid \theta)^\beta$ by training a single $(x,\beta)$-conditioned neural posterior estimator $q_\phi(\theta \mid x,\beta)$ that enables sampling in a single forward pass, without simulator calls or inference-time MCMC. We introduce two complementary training routes: (i) synthesize off-manifold samples $(\theta,x) \sim \pi(\theta)\,p(x \mid \theta)^\beta$ and (ii) reweight a fixed base dataset $\pi(\theta)\,p(x \mid \theta)$ using self-normalized importance sampling (SNIS). We show that the SNIS-weighted objective provides a consistent forward-KL fit to the tempered posterior with finite weight variance. Across four standard simulation-based inference (SBI) benchmarks, including the chaotic Lorenz-96 system, our $\beta$-amortized estimator achieves competitive posterior approximations in standard two-sample metrics, matching non-amortized MCMC-based power-posterior samplers over a wide range of temperatures.
