# M3D-BFS: a Multi-stage Dynamic Fusion Strategy for Sample-Adaptive Multi-Modal Brain Network Analysis

**arXiv ID**: 2604.01667
**Published**: 2026-04-02
**Updated**: 2026-04-02
**Authors**: Rui Dong, Xiaotong Zhang, Jiaxing Li, Yueying Li, Jiayin Wei, Youyong Kong
**Categories**: cs.AI, cs.CV
**URL**: https://arxiv.org/abs/2604.01667
**PDF**: https://arxiv.org/pdf/2604.01667
**Source**: arXiv

## Abstract

Multi-modal fusion is of great significance in neuroscience which integrates information from different modalities and can achieve better performance than uni-modal methods in downstream tasks. Current multi-modal fusion methods in brain networks, which mainly focus on structural connectivity (SC) and functional connectivity (FC) modalities, are static in nature. They feed different samples into the same model with identical computation, ignoring inherent difference between input samples. This lack of sample adaptation hinders model's further performance. To this end, we innovatively propose a multi-stage dynamic fusion strategy (M3D-BFS) for sample-adaptive multi-modal brain network analysis. Unlike other static fusion methods, we design different mixture-of-experts (MoEs) for uni- and multi-modal representations where modules can adaptively change as input sample changes during inference. To alleviate issue of MoE where training of experts may be collapsed, we divide our method into 3 stages. We first train uni-modal encoders respectively, then pretrain single experts of MoEs before finally finetuning the whole model. A multi-modal disentanglement loss is designed to enhance the final representations. To the best of our knowledge, this is the first work for dynamic fusion for multi-modal brain network analysis. Extensive experiments on different real-world datasets demonstrates the superiority of M3D-BFS.
