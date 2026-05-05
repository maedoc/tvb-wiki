# Variational Bayesian Adaptive Learning of Deep Latent Variables for Acoustic Knowledge Transfer

**Source**: semantic-scholar
**ID**: 3d5f3705f9422501c737b13bdabd705681dfead7
**DOI**: 10.1109/TASLPRO.2025.3530321
**URL**: https://www.semanticscholar.org/paper/3d5f3705f9422501c737b13bdabd705681dfead7
**Date**: 2025-01-26
**Year**: 2025
**Authors**: Huiyong Hu, Sabato Marco Siniscalchi, Chao-Han Huck Yang, Chin-Hui Lee
**Venue**: IEEE Transactions on Audio, Speech, and Language Processing
**Citations**: 0

## Abstract

In this work, we propose a novel variational Bayesian adaptive learning approach for cross-domain knowledge transfer to address acoustic mismatches between training and testing conditions, such as recording devices and environmental noise. Different from the traditional Bayesian approaches that impose uncertainties on model parameters risking the curse of dimensionality due to the huge number of parameters, we focus on estimating a manageable number of latent variables in deep neural models. Knowledge learned from a source domain is thus encoded in prior distributions of deep latent variables and optimally combined, in a Bayesian sense, with a small set of adaptation data from a target domain to approximate the corresponding posterior distributions. Two different strategies are proposed and investigated to estimate the posterior distributions: Gaussian mean-field variational inference, and empirical Bayes. These strategies address the presence or absence of parallel data in the source and target domains. Furthermore, structural relationship modeling is investigated to enhance the approximation. We evaluated our proposed approaches on two acoustic adaptation tasks: 1) device adaptation for acoustic scene classification, and 2) noise adaptation for spoken command recognition. Experimental results show that the proposed variational Bayesian adaptive learning approach can obtain good improvements on target domain data, and consistently outperforms state-of-the-art knowledge transfer methods.
