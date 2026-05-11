# MambaKAN: An Interpretable Framework for Alzheimer’s Disease Diagnosis via Selective State Space Modeling of Dynamic Functional Connectivity

**Source**: semantic-scholar
**ID**: c8c74942dc08f94ada12a3c682f290c2243cfc5b
**DOI**: 10.3390/brainsci16040421
**URL**: https://www.semanticscholar.org/paper/c8c74942dc08f94ada12a3c682f290c2243cfc5b
**Date**: 2026-04-01
**Year**: 2026
**Authors**: Libin Gao, Zhongyi Hu
**Venue**: Brain Science
**Citations**: 0

## Abstract

Background/Objectives: Alzheimer’s disease (AD) is an irreversible neurodegenerative disorder that imposes a profound burden on global public health. While resting-state functional magnetic resonance imaging (rs-fMRI)-based dynamic functional connectivity (dFC) analysis has demonstrated promise in capturing time-varying brain network abnormalities, existing deep learning methods suffer from three fundamental limitations: (1) an inability to model temporal dependencies across dynamic connectivity windows, (2) reliance on post hoc black-box explainability tools, and (3) misalignment between feature learning and classification objectives. Methods: To address these challenges, we propose MambaKAN, an end-to-end interpretable framework integrating a Variational Autoencoder (VAE), a Selective State Space Model (Mamba), and a Kolmogorov–Arnold Network (KAN). The VAE encodes each dFC snapshot into a compact latent representation, preserving nonlinear connectivity patterns. The Mamba encoder captures long-range temporal dynamics across the sequence of latent representations via input-selective state transitions. The KAN classifier provides intrinsic interpretability through learnable B-spline activation functions, enabling direct visualization of how latent features influence diagnostic decisions without post-hoc approximation. The entire pipeline is trained end-to-end with a joint loss function that aligns feature learning with classification. Results: Evaluated on the Alzheimer’s Disease Neuroimaging Initiative (ADNI) dataset across five classification tasks (CN vs. AD, CN vs. EMCI, EMCI vs. LMCI, LMCI vs. AD, and four-class), MambaKAN achieves accuracies of 95.1%, 89.8%, 84.0%, 86.7%, and 70.5%, respectively, outperforming strong baselines including LSTM, Transformer, and MLP-based variants. Conclusions: Comprehensive ablation studies confirm the indispensable contribution of each module, and the three-layer interpretability analysis reveals key temporal patterns and brain regions associated with AD progression.
