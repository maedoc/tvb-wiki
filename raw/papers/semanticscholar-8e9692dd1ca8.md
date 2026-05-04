# Deep Learning for fODF Estimation in Infant Brains: Model Comparison, Ground‐Truth Impact, and Domain Shift Mitigation

**Source**: semantic-scholar
**ID**: 8e9692dd1ca84fee545afe51fb5787cb954f6933
**DOI**: 10.1002/hbm.70367
**URL**: https://www.semanticscholar.org/paper/8e9692dd1ca84fee545afe51fb5787cb954f6933
**Date**: 2025-10-01
**Year**: 2025
**Authors**: Rizhong Lin, Hamza Kebiri, A. Gholipour, Yufei Chen, J. Thiran, Davood Karimi, M. Bach Cuadra
**Venue**: Human Brain Mapping
**Citations**: 0

## Abstract

The accurate estimation of fiber orientation distribution functions (fODFs) in diffusion magnetic resonance imaging (MRI) is crucial for understanding early brain development and its potential disruptions. Although supervised deep learning (DL) models have shown promise in fODF estimation from neonatal diffusion MRI (dMRI) data, the out‐of‐domain (OOD) performance of these models remains largely unexplored, especially under diverse domain shift scenarios. This study evaluated the robustness of three state‐of‐the‐art DL architectures: multilayer perceptron (MLP), transformer, and U‐Net/convolutional neural network (CNN) on fODF predictions derived from dMRI data. Using 488 subjects from the developing Human Connectome Project (dHCP) and the Baby Connectome Project (BCP) datasets, we reconstructed reference fODFs from the full dMRI series using single‐shell three‐tissue constrained spherical deconvolution (SS3T‐CSD) and multi‐shell multi‐tissue CSD (MSMT‐CSD) to generate reference fODF reconstructions for model training, and systematically assessed the impact of age, scanner/protocol differences, and input dimensionality on model performance. Our findings reveal that U‐Net consistently outperformed other models when fewer diffusion gradient directions were used, particularly with the SS3T‐CSD‐derived ground truth, which showed superior performance in capturing crossing fibers. However, as the number of input diffusion gradient directions increased, MLP and the transformer‐based model exhibited steady gains in accuracy. Nevertheless, performance nearly plateaued from 28 to 45 input directions in all models. Age‐related domain shifts showed asymmetric patterns, being less pronounced in late developmental stages (late neonates, and babies), with SS3T‐CSD demonstrating greater robustness to variability compared to MSMT‐CSD. To address inter‐site domain shifts, we implemented two adaptation strategies: the Method of Moments (MoM) and fine‐tuning. Both strategies achieved significant improvements ( p<0.05$$ p<0.05 $$ ) in over 95% of tested configurations, with fine‐tuning consistently yielding superior results and U‐Net benefiting the most from increased target subjects. This study represents the first systematic evaluation of OOD settings in DL applications to fODF estimation, providing critical insights into model robustness and adaptation strategies for diverse clinical and research applications.
