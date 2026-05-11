# PHIVE: A Physics-Informed Variational Encoder Enables Rapid Spectral Fitting of Brain Metabolite Mapping at 7T

**Source**: semantic-scholar
**ID**: b5d64ded87fc48dc1ef8b6f0d79b9bc8e7006cef
**DOI**: 10.1101/2025.01.02.25319930
**URL**: https://www.semanticscholar.org/paper/b5d64ded87fc48dc1ef8b6f0d79b9bc8e7006cef
**Date**: 2025-01-03
**Year**: 2025
**Authors**: A. Shamaei, E. Niess, L. Hingerl, B. Strasser, A. Osburg, K. Eckstein, W. Bogner, S. Motyka
**Venue**: medRxiv
**Citations**: 2

## Abstract

Magnetic Resonance Spectroscopic Imaging (MRSI) enables non-invasive mapping of brain metabolite concentrations but remains computationally intensive and challenging due to a low signal-to-noise ratio (SNR) and overlapping spectral features. Traditional spectral fitting methods, such as LCModel, are time-consuming and often lack comprehensive uncertainty quantification. In this study, we propose Physics-Informed Variational Encoder (PHIVE), a novel deep learning framework that integrates physics- based priors into a variational autoencoder architecture for rapid and accurate metabolite quantification. PHIVE enables simultaneous estimation of metabolite concentrations and uncertainty metrics, including Cramer-Rao Lower Bound (CRLB), aleatoric, and epistemic uncertainties. PHIVE was evaluated on whole-brain MRSI data from 7T acquisitions of healthy controls. The method achieved comparable accuracy to LCModel for key metabolites, such as Total N-acetylaspartate (tNAA), Glutamate-Glutamine complex (Glx), and Myo-inositol (mIns) while demonstrating a six-order magnitude reduction in computational time (6 ms per dataset). Uncertainty quantification highlighted PHIVE's robust- ness in regions with low SNR. Additionally, a conditional baseline modeling approach was introduced, enabling dynamic flexibility in spectral baseline estimation during inference time. These results suggest that PHIVE offers a fast, reliable, and interpretable solution for high-resolution metabolite quantification, paving the way for real-time MRSI applications in clinical and research settings. Future work will focus on expanding its validation across diverse datasets and investigating its utility in longitudinal and multi-center studies.
