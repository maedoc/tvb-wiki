# A Scalable Nonparametric Continuous-Time Survival Model through Numerical Quadrature

**Source**: arxiv
**ID**: 2605.16208
**URL**: https://arxiv.org/abs/2605.16208
**Date**: 2026-05-15
**Year**: 2026
**Authors**: Chaeyeon Lee, Sehwan Kim, Hyungrok Do
**Categories**: stat.ML, cs.LG

## Abstract

Flexible continuous-time survival modeling is critical for capturing complex time-varying hazard dynamics in high-dimensional data; however, training such models remains challenging due to the intractable integral required for likelihood estimation. We introduce QSurv, a scalable deep learning framework that enables nonparametric continuous-time modeling without relying on time discretization or restrictive distributional assumptions. We propose a training objective based on Gauss-Legendre numerical quadrature, which approximates the cumulative hazard with high-order accuracy while facilitating efficient end-to-end training via standard backpropagation. Furthermore, to effectively capture non-stationary hazard dynamics in complex architectures, we introduce time-conditioned low-rank adaptation, a mechanism that conditions general neural backbones on time by dynamically modulating weights via low-rank updates. We provide theoretical analysis establishing approximation error bounds for cumulative-hazard evaluation. Comprehensive experiments across synthetic benchmarks, large-scale real-world tabular datasets, and high-dimensional medical imaging tasks demonstrate that QSurv achieves competitive predictive performance with advantages in instantaneous hazard function estimation, enabling more interpretable characterization of time-varying risk patterns.
