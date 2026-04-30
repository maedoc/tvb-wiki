# Meta-learning-enhanced implicit full waveform inversion

**Source**: arxiv
**ID**: 2604.26938
**URL**: https://arxiv.org/abs/2604.26938
**Date**: 2026-04-29
**Year**: 2026
**Authors**: Huan Song, Shijun Cheng, Huanhuan Tang, Wei Ouyang, Weijian Mao
**Categories**: physics.geo-ph

## Abstract

Implicit full waveform inversion (IFWI) introduces implicit neural representations to parameterize the subsurface velocity model as a continuous function of spatial coordinates, which alleviates the dependence on the initial model and improves inversion flexibility. However, IFWI still requires a large number of iterative updates for each new exploration area, leading to slow convergence, high computational cost, and a lack of mechanisms to share prior knowledge across different geological settings, thereby limiting its efficiency and generalization capability. To further accelerate convergence and enhance cross-area generalization, we propose a meta-learning-based implicit full waveform inversion method, referred to as Meta-learning-enhanced implicit full waveform inversion (Meta-IFWI). In this framework, the subsurface velocity model is represented using an implicit neural network with periodic activation functions (SIREN), while a meta-learning strategy is employed to pretrain a single network on multiple velocity inversion tasks. Through this process, the network learns shared inversion priors and rapid adaptation strategies across different geological scenarios. For a new inversion task, the pretrained Meta-IFWI model can be efficiently adapted to the observed seismic data with only a few gradient updates, significantly reducing the number of iterations required for inversion. Numerical experiments conducted on in-distribution models, including layered synthetic models and the Overthrust model, as well as out-of-distribution complex models such as Marmousi 2, demonstrate that, compared with conventional IFWI, the proposed Meta-IFWI achieves improved inversion accuracy while substantially accelerating convergence and reducing computational cost. Moreover, Meta-IFWI exhibits enhanced robustness and stronger cross-area generalization capability.
