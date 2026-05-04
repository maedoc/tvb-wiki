# Predicting Price Movements in High-Frequency Financial Data with Spiking Neural Networks

**Source**: semantic-scholar
**ID**: a05004c1ab4f62bf0b30c0a361eeeca13e0c382e
**DOI**: 10.48550/arXiv.2512.05868
**URL**: https://www.semanticscholar.org/paper/a05004c1ab4f62bf0b30c0a361eeeca13e0c382e
**Date**: 2025-12-05
**Year**: 2025
**Authors**: Brian Ezinwoke, O. Rhodes
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Modern high-frequency trading (HFT) environments are characterized by sudden price spikes that present both risk and opportunity, but conventional financial models often fail to capture the required fine temporal structure. Spiking Neural Networks (SNNs) offer a biologically inspired framework well-suited to these challenges due to their natural ability to process discrete events and preserve millisecond-scale timing. This work investigates the application of SNNs to high-frequency price-spike forecasting, enhancing performance via robust hyperparameter tuning with Bayesian Optimization (BO). This work converts high-frequency stock data into spike trains and evaluates three architectures: an established unsupervised STDP-trained SNN, a novel SNN with explicit inhibitory competition, and a supervised backpropagation network. BO was driven by a novel objective, Penalized Spike Accuracy (PSA), designed to ensure a network's predicted price spike rate aligns with the empirical rate of price events. Simulated trading demonstrated that models optimized with PSA consistently outperformed their Spike Accuracy (SA)-tuned counterparts and baselines. Specifically, the extended SNN model with PSA achieved the highest cumulative return (76.8%) in simple backtesting, significantly surpassing the supervised alternative (42.54% return). These results validate the potential of spiking networks, when robustly tuned with task-specific objectives, for effective price spike forecasting in HFT.
