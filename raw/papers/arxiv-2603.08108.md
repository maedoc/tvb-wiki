# Tau-BNO: Brain Neural Operator for Tau Transport Model

**Source**: semantic-scholar
**ID**: 4c0815cf262ed66052b69fe383d20901bc52b16b
**URL**: https://www.semanticscholar.org/paper/4c0815cf262ed66052b69fe383d20901bc52b16b
**Date**: 2026-03-09
**Year**: 2026
**Authors**: Nuutti Barron, Heng Rao, Urmi Saha, Yu Gu, Zhenghao Liu, Ge Yu, Defu Yang, Ashish Raj, Minghan Chen
**Citations**: 0

## Abstract

Mechanistic modeling provides a biophysically grounded framework for studying the spread of pathological tau protein in tauopathies like Alzheimer's disease. Existing approaches typically model tau propagation as a diffusive process on the brain's structural connectome, reproducing macroscopic patterns but neglecting microscale cellular transport and reaction mechanisms. The Network Transport Model (NTM) was introduced to fill this gap, explaining how region-level progression of tau emerges from microscale biophysical processes. However, the NTM faces a common challenge for complex models defined by large systems of partial differential equations: the inability to perform parameter inference and mechanistic discovery due to high computational burden and slow model simulations. To overcome this barrier, we propose Tau-BNO, a Brain Neural Operator surrogate framework for rapidly approximating NTM dynamics that captures both intra-regional reaction kinetics and inter-regional network transport. Tau-BNO combines a function operator that encodes kinetic parameters with a query operator that preserves initial state information, while approximating anisotropic transport through a spectral kernel that retains directionality. Empirical evaluations demonstrate high predictive accuracy ($R^2\approx$ 0.98) across diverse biophysical regimes and an 89\% performance improvement over state-of-the-art sequence models like Transformers and Mamba, which lack inherent structural priors. By reducing simulation time from hours to seconds, we show that the surrogate model is capable of producing new insights and generating new hypotheses. This framework is readily extensible to a broader class of connectome-based biophysical models, showcasing the transformative value of deep learning surrogates to accelerate analysis of large-scale, computationally intensive dynamical systems.
