# Exact closed-form Gaussian moments of residual layers

**Source**: semantic-scholar
**ID**: f1697b92c508c61c0cf950ae3333fee0f231fa0e
**DOI**: 10.48550/arXiv.2601.22307
**URL**: https://www.semanticscholar.org/paper/f1697b92c508c61c0cf950ae3333fee0f231fa0e
**Date**: 2026-01-29
**Year**: 2026
**Authors**: Simon Kuang, Xinfan Lin
**Venue**: arXiv.org
**Citations**: 0

## Abstract

We study the problem of propagating the mean and covariance of a general multivariate Gaussian distribution through a deep (residual) neural network using layer-by-layer moment matching. We close a longstanding gap by deriving exact moment matching for the probit, GeLU, ReLU (as a limit of GeLU), Heaviside (as a limit of probit), and sine activation functions; for both feedforward and generalized residual layers. On random networks, we find orders-of-magnitude improvements in the KL divergence error metric, up to a millionfold, over popular alternatives. On real data, we find competitive statistical calibration for inference under epistemic uncertainty in the input. On a variational Bayes network, we show that our method attains hundredfold improvements in KL divergence from Monte Carlo ground truth over a state-of-the-art deterministic inference method. We also give an a priori error bound and a preliminary analysis of stochastic feedforward neurons, which have recently attracted general interest.
