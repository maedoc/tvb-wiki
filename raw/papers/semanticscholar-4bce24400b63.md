# Combining Spatial Wavelets and Sparse Bayesian Learning for Extended Brain Sources Reconstruction.

**Source**: semantic-scholar
**ID**: 4bce24400b635c18509944a6b71e63ee22bb231d
**DOI**: 10.1109/TBME.2025.3629010
**URL**: https://www.semanticscholar.org/paper/4bce24400b635c18509944a6b71e63ee22bb231d
**Date**: 2025-11-04
**Year**: 2025
**Authors**: S. Mokhtari, Jean-Michel Badier, C. Bénar, Bruno Torrésani
**Venue**: IEEE transactions on bio-medical engineering
**Citations**: 0

## Abstract

OBJECTIVE
The accurate reconstruction of extended cortical activity from M/EEG data is a difficult, ill-conditioned problem. This work proposes to model distributed sources through spectral graph wavelets on the cortical surface, and addresses resulting numerical optimization problems. The objective is accurate localization, especially for extended sources, together with quantitatively relevant amplitude and time course.


APPROACH
Unknown sources are expanded on a system of spectral graph wavelets (SGW) defined on the cortical surface. Unknown wavelet coefficients are estimated using either variational or Bayesian formulations, involving priors that favor extended sources through sparsity in the wavelet domain: sparsity-inducing regularization, or sparse Bayesian learning (SBL). These approaches are tested and compared with concurrent approaches on real (open-access) data and numerical simulations. The quality of reconstructions is assessed using complementary metrics.


RESULTS
SGW-based approaches are able to identify accurately extended sources. The combination with SBL is particularly attractive, as it doesn't involve hyperparameter tuning and automatically adapts to the signal to noise ratio (SNR). It yields accurate and robust results with respect to all considered metrics, and performs remarkably well in terms of depth bias.


CONCLUSION
This paper demonstrates the usefulness of spectral graph cortical wavelets for reconstructing cortical activity from M/EEG data, especially when coupling spatial wavelets with SBL.


SIGNIFICANCE
Being able to identify localization, depth, amplitude and time course of brain activity from M/EEG data is important in clinical applications such as epilepsy, as it can improve the detection of potential sources of seizures.
