# A Scalable Exponential Random Graph Model: Amortised Hierarchical Sequential Neural Posterior Estimation with Applications in Neuroscience

**Source**: semantic-scholar
**ID**: 37e08d0f7dc3a455c62448b2a4a60b7149955ba4
**URL**: https://www.semanticscholar.org/paper/37e08d0f7dc3a455c62448b2a4a60b7149955ba4
**Date**: 2025-06-05
**Year**: 2025
**Authors**: Yefeng Fan, S. White
**Citations**: 0

## Abstract

Exponential Random Graph Models (ERGMs) are an inferential model for analysing statistical networks. Recent development in ERGMs uses hierarchical Bayesian setup to jointly model a group of networks, which is called a multiple-network Exponential Random Graph Model (MN-ERGMs). MN-ERGM has been successfully applied on real-world resting-state fMRI data from the Cam-CAN project to infer the brain connectivity on aging. However, conventional Bayesian ERGM estimation approach is computationally intensive and lacks implementation scalability due to intractable ERGM likelihood. We address this key limitation by using neural posterior estimation (NPE), which trains a neural network-based conditional density estimator to infer the posterior.\\ We proposed an Amortised Hierarchical Sequential Neural Posterior Estimation (AHS-NPE) and various ERGM-specific adjustment schemes to target the Bayesian hierarchical structure of MN-ERGMs. Our proposed method contributes to the ERGM literature as a very scalable solution, and we used AHS-NPE to re-show the fitting results on the Cam-CAN data application and further scaled it up to a larger implementation sample size. More importantly, our AHS-NPE contributes to the general NPE literature as a new hierarchical NPE approach that preserves the amortisation and sequential refinement, which can be applied to a variety of study fields.
