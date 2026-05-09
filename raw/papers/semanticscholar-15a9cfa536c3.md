# PHIVE: A physics-informed variational encoder enables rapid spectral fitting of brain metabolite mapping at 7T.

**Source**: semantic-scholar
**ID**: 15a9cfa536c3f9ab5ec70edf5a7c455f72ae1ca4
**DOI**: 10.1016/j.media.2026.104014
**URL**: https://www.semanticscholar.org/paper/15a9cfa536c3f9ab5ec70edf5a7c455f72ae1ca4
**Date**: 2026-03-01
**Year**: 2026
**Authors**: A. Shamaei, Amir Buchali, E. Niess, Lukas Hingerl, Bernhard Strasser, A. Osburg, Korbinian Eckstein, W. Bogner, S. Motyka
**Venue**: Medical Image Analysis
**Citations**: 0

## Abstract

Magnetic Resonance Spectroscopic Imaging (MRSI) enables non-invasive mapping of brain metabolite concentrations but remains computationally intensive and challenging due to a low signal-to-noise ratio (SNR) and overlapping spectral features. Traditional spectral fitting methods, such as LCModel, are time-consuming and often lack comprehensive uncertainty quantification. In this study, we propose Physics-Informed Variational Encoder (PHIVE), a novel deep learning framework that integrates physics-based priors into a variational autoencoder architecture for rapid and accurate metabolite quantification. PHIVE enables simultaneous estimation of metabolite concentrations and uncertainty metrics, including Cramér-Rao Lower Bound (CRLB), aleatoric, and epistemic uncertainties. PHIVE is evaluated on whole-brain MRSI data from 7T acquisitions of healthy controls and multiple sclerosis (MS) patients. The method achieved comparable accuracy to LCModel for key metabolites, such as Total N-acetylaspartate (tNAA), Glutamate-Glutamine complex (Glx), and Myo-inositol (mIns) while demonstrating a six-order-of-magnitude reduction in computational time (6 ms per dataset). Uncertainty quantification highlighted PHIVE's robustness in regions with low SNR. Additionally, a conditional baseline modeling approach is introduced, enabling dynamic flexibility in spectral baseline estimation during inference time. These results suggest that PHIVE offers a fast, reliable, and interpretable solution for high-resolution metabolite quantification, paving the way for real-time MRSI applications in clinical and research settings. Future work will focus on expanding its validation across diverse datasets and investigating its utility in longitudinal and multi-center studies. Our code is available at https://github.com/amirshamaei/PHIVE.
