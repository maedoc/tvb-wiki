# Brain Effective Connectivity Estimation via Fourier Spatiotemporal Attention

**Source**: semantic-scholar
**ID**: 68566d1846ff1eb60c2d15f5ad1d96c2bb4a6fb1
**DOI**: 10.1145/3690624.3709226
**URL**: https://www.semanticscholar.org/paper/68566d1846ff1eb60c2d15f5ad1d96c2bb4a6fb1
**Date**: 2025-03-14
**Year**: 2025
**Authors**: Wenrui Xiong, Jinduo Liu, Junzhong Ji, Fenglong Ma
**Venue**: Knowledge Discovery and Data Mining
**Citations**: 2

## Abstract

Estimating brain effective connectivity (EC) from functional magnetic resonance imaging (fMRI) data can aid in comprehending the neural mechanisms underlying human behavior and cognition, providing a foundation for disease diagnosis. However, current spatiotemporal attention modules handle temporal and spatial attention separately, extracting temporal and spatial features either sequentially or in parallel. These approach overlooks the inherent spatiotemporal correlations present in real world fMRI data. Additionally, the presence of noise in fMRI data further limits the performance of existing methods. In this paper, we propose a novel brain effective connectivity estimation method based on Fourier spatiotemporal attention (FSTA-EC), which combines Fourier attention and spatiotemporal attention to simultaneously capture inter-series (spatial) dynamics and intra-series (temporal) dependencies from high-noise fMRI data. Specifically, Fourier attention is designed to convert the high-noise fMRI data to frequency domain, and map the denoised fMRI data back to physical domain, and spatiotemporal attention is crafted to simultaneously learn spatiotemporal dynamics. Furthermore, through a series of proofs, we demonstrate that incorporating learnable filters into fast Fourier transform and inverse fast Fourier transform processes is mathematically equivalent to performing cyclic convolution. The experimental results on simulated and real-resting-state fMRI datasets demonstrate that the proposed method exhibits superior performance when compared to state-of-the-art methods. The code is available at https://github.com/XiongWenXww/FSTA.
