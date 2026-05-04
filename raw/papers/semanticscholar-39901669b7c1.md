# Federated learning meets Bayesian neural network: Robust and uncertainty-aware distributed variational inference

**Source**: semantic-scholar
**ID**: 39901669b7c1cb318e4db390beff521b83c7600e
**DOI**: 10.1016/j.neunet.2025.107135
**URL**: https://www.semanticscholar.org/paper/39901669b7c1cb318e4db390beff521b83c7600e
**Date**: 2025-01-01
**Year**: 2025
**Authors**: Pengfei Li, Qinghua Hu, Xiaofei Wang
**Venue**: Neural Networks
**Citations**: 5

## Abstract

Federated Learning (FL) is a popular framework for data privacy protection in distributed machine learning. However, current FL faces some several problems and challenges, including the limited amount of client data and data heterogeneity. These lead to models trained on clients prone to drifting and overfitting, such that we just obtain suboptimal performance of the aggregated model. To tackle the aforementioned problems, we introduce a novel approach explicitly integrating Bayesian neural networks (BNNs) into the FL framework. The proposed approach is able to enhance the robustness. We refer to this approach as FedUAB, standing for FL with uncertainty-aware BNNs. In the FedUAB algorithm, each FL client independently trains a BNN using the Bayes by backprop algorithm. The weights of approximating model are modeled as Gaussian distributions, which mitigates the overfitting issue and also ensures better data privacy. Besides, we apply novel methods to overcome other key challenges in the fusion of BNNs and FL, such as selecting an optimal prior distribution, aggregating weights characterized by Gaussian forms across multiple clients, and rigorously managing weights variances. In the simulation of a FL environment, FedUAB demonstrated superior performance with both its server-side global model and client-side personalized models, outperforming traditional FL and other Bayesian FL methods. Moreover, it possesses the capability to quantify and decompose uncertainties. We have open-sourced our project at https://github.com/lpf111222/FedUAB/.
