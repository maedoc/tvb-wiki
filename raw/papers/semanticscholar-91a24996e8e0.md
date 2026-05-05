# Bayesian Source Identification With Dual Hierarchical Neural Networks for Urban Air Pollution

**Source**: semantic-scholar
**ID**: 91a24996e8e0cb737fad6a476eddf34b399241ec
**DOI**: 10.1029/2024MS004790
**URL**: https://www.semanticscholar.org/paper/91a24996e8e0cb737fad6a476eddf34b399241ec
**Date**: 2025-04-01
**Year**: 2025
**Authors**: Elissar Al Aawar, Sofien Resifi, Hatem Jebari, I. Hoteit
**Venue**: Journal of Advances in Modeling Earth Systems
**Citations**: 1

## Abstract

Identifying urban air pollution sources is essential for public health and environmental sustainability. In this study, we propose a novel hierarchical method for urban air pollution source identification, leveraging deep learning (DL) within an efficient Bayesian inference framework. We rely on observations in the form of two‐dimensional (2D) pollutant concentration distributions, and adopt the Wasserstein W2 $\left({W}_{2}\right)$ distance to model the likelihood probability distribution. The hierarchical nature of the framework stems from the integration of two neural networks (NNs). The first one acts as an emulator that replicates the physical dispersion model to predict future pollution observations recursively over a defined timeframe. These predictions are then used as inputs for the second NN that approximates the W2 ${W}_{2}$ distance between predicted and observed pollutant concentration distributions to rapidly compute the likelihood probability. The approach adopts a multi‐model strategy to mitigate the accumulation of errors, particularly those arising from the recursive prediction steps across multiple time intervals, ensuring the reliability of predictions over extended periods. The proposed framework is implemented on graphics processing units (GPUs), enabling scalable computations for real‐world applications and rapid decision making. Through extensive numerical experiments, we demonstrate the suggested method's effectiveness in accurately estimating pollution source parameters, including location, emission rate, and duration, using synthetic observational data. Sensitivity analyses further explore the impact of observational horizons and sampling on solution convergence and accuracy. Numerical results demonstrate robust performances and computational efficiency compared to the conventional approach, particularly in scenarios with limited computational resources and observations availability.
