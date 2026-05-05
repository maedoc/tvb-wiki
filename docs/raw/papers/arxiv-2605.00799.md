# GMGaze: MoE-Based Context-Aware Gaze Estimation with CLIP and Multiscale Transformer

**Source**: arxiv
**ID**: 2605.00799
**URL**: https://arxiv.org/abs/2605.00799
**Date**: 2026-05-01
**Year**: 2026
**Authors**: Xinyuan Zhao, Yihang Wu, Ahmad Chaddad, Sarah A. Alkhodair, Reem Kateb
**Categories**: cs.CV

## Abstract

Gaze estimation methods commonly use facial appearances to predict the direction of a person gaze. However, previous studies show three major challenges with convolutional neural network (CNN)-based, transformer-based, and contrastive language-image pre-training (CLIP)-based methods, including late fusion of image features, lack of factor-aware conditioning, and impractical capacity scaling. To address these challenges, we propose Globally-conditioned Multi-scale Gaze estimation (GMGaze), which leverages a multi-scale transformer architecture. Specifically, the model first introduces semantic prototype conditioning, which modulates the CLIP global image embedding using four learned prototype banks (i.e., illumination, background, head pose and appearance) to generate two complementary context-biased global tokens. These tokens, along with the CLIP patch and CNN tokens, are fused at the first layer. This early unified fusion prevents information loss common in late-stage merging. Finally, each token passes through sparse Mixture-of-Experts modules, providing conditional computational capacity without uniformly increasing dense parameters. For cross-domain adaptation, we incorporate an adversarial domain adaptation technique with a feature separation loss that encourages the two global tokens to remain de-correlated. Experiments using four public benchmarks (MPIIFaceGaze, EYEDIAP, Gaze360, and ETH-XGaze) show that GMGaze achieves mean angular errors of 2.49$^\circ$, 3.22$^\circ$, 10.16$^\circ$, and 1.44$^\circ$, respectively, outperforming previous baselines in all within-domain settings. In cross-domain evaluations, it provides state-of-the-art (SOTA) results on two standard transfer routes.
