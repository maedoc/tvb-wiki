# Optimizing EEG Graph Structure for Seizure Detection: An Information Bottleneck and Self-Supervised Learning Approach

**arXiv ID**: 2604.01595
**Published**: 2026-04-02
**Updated**: 2026-04-02
**Authors**: Lincan Li, Rikuto Kotoge, Xihao Piao, Zheng Chen, Yushun Dong
**Categories**: cs.LG
**URL**: https://arxiv.org/abs/2604.01595
**PDF**: https://arxiv.org/pdf/2604.01595
**Source**: arXiv

## Abstract

Seizure detection from EEG signals is highly challenging due to complex spatiotemporal dynamics and extreme inter-patient variability. To model them, recent methods construct dynamic graphs via statistical correlations, predefined similarity measures, or implicit learning, yet rarely account for EEG's noisy nature. Consequently, these graphs usually contain redundant or task-irrelevant connections, undermining model performance even with state-of-the-art architectures. In this paper, we present a new perspective for EEG seizure detection: jointly learning denoised dynamic graph structures and informative spatial-temporal representations guided by the Information Bottleneck (IB). Unlike prior approaches, our graph constructor explicitly accounts for the noisy characteristics of EEG data, producing compact and reliable connectivity patterns that better support downstream seizure detection. To further enhance representation learning, we employ a self-supervised Graph Masked AutoEncoder that reconstructs masked EEG signals based on dynamic graph context, promoting structure-aware and compact representations aligned with the IB principle. Bringing things together, we introduce Information Bottleneck-guided EEG SeizuRE DetectioN via SElf-Supervised Learning (IRENE), which explicitly learns dynamic graph structures and interpretable spatial-temporal EEG representations. IRENE addresses three core challenges: (i) Identifying the most informative nodes and edges; (ii) Explaining seizure propagation in the brain network; and (iii) Enhancing robustness against label scarcity and inter-patient variability. Extensive experiments on benchmark EEG datasets demonstrate that our method outperforms state-of-the-art baselines in seizure detection and provides clinically meaningful insights into seizure dynamics. The source code is available at https://github.com/LabRAI/IRENE.
