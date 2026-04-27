# Estimating H I Mass Fraction in Galaxies with Bayesian Neural Networks

**Source**: semantic-scholar
**ID**: e2968a3d8266d2a3c99a08eb5e369cb85c8af0f5
**DOI**: 10.3390/galaxies14010010
**URL**: https://www.semanticscholar.org/paper/e2968a3d8266d2a3c99a08eb5e369cb85c8af0f5
**Date**: 2026-02-02
**Year**: 2026
**Authors**: Joelson Sartori, Cristian G. Bernal, C. Frajuca
**Venue**: Galaxies
**Citations**: 0

## Abstract

Neutral atomic hydrogen (H I) regulates galaxy growth and quenching, but direct 21 cm measurements remain observationally expensive and affected by selection biases. We develop Bayesian neural networks (BNNs)—a type of neural model that returns both a prediction and an associated uncertainty—to infer the H I mass, log10(MHI), from widely available optical properties (e.g., stellar mass, apparent magnitudes, and diagnostic colors) and simple structural parameters. For continuity with the photometric gas fraction (PGF) literature, we also report the gas-to-stellar-mass ratio, log10(G/S), where explicitly noted. Our dataset is a reproducible cross-match of SDSS DR12, the MPA–JHU value-added catalogs, and the 100% ALFALFA release, resulting in 31,501 galaxies after quality controls. To ensure fair evaluation, we adopt fixed train/validation/test partitions and an additional sky-holdout region to probe domain shift, i.e., how well the model extrapolates to sky regions that were not used for training. We also audit features to avoid information leakage and benchmark the BNNs against deterministic models, including a feed-forward neural network baseline and gradient-boosted trees (GBTs, a standard tree-based ensemble method in machine learning). Performance is assessed using mean absolute error (MAE), root-mean-square error (RMSE), and probabilistic diagnostics such as the negative log-likelihood (NLL, a loss that rewards models that assign high probability to the observed H I masses), reliability diagrams (plots comparing predicted probabilities to observed frequencies), and empirical 68%/95% coverage. The Bayesian models achieve point accuracy comparable to the deterministic baselines while additionally providing calibrated prediction intervals that adapt to stellar mass, surface density, and color. This enables galaxy-by-galaxy uncertainty estimation and prioritization for 21 cm follow-up that explicitly accounts for predicted uncertainties (“risk-aware” target selection). Overall, the results demonstrate that uncertainty-aware machine-learning methods offer a scalable and reproducible route to inferring galactic H I content from widely available optical data.
