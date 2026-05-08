# A Sparse-Integrated Filtering Residual Spiking Neural Network for High-Accuracy Spike Sorting and Co-Optimization on Memristor Platforms

**Source**: semantic-scholar
**ID**: 5ce5c3686a0547918f639850feb6a641ce4e2865
**DOI**: 10.1109/TBCAS.2025.3601403
**URL**: https://www.semanticscholar.org/paper/5ce5c3686a0547918f639850feb6a641ce4e2865
**Date**: 2025-08-22
**Year**: 2025
**Authors**: Yiwen Zhu, Jingyi Chen, Lingli Cheng, Fangduo Zhu, Xumeng Zhang, Qi Liu
**Venue**: IEEE Transactions on Biomedical Circuits and Systems
**Citations**: 0

## Abstract

Brain-computer interfaces rely on precise decoding of neural signals, where spike sorting is a critical step to extract individual neuronal activities from complex neural data. This work presents a spiking neural network (SNN) framework for efficient spike sorting, named SIFT-RSNN. In the SIFT-RSNN, raw neural signals are encoded into spike trains using a threshold-based temporal encoding strategy, then a sparse-integrated filtering module refines misfiring spikes, enhancing data sparsity for pattern learning. The RSNN module with a membrane shortcut structure ensures efficient feature transfer and improves generalization performance of the overall system. The SIFT-RSNN achieves an accuracy of 96.2% and 99.6% on the Difficult1 and Difficult2 subsets of Leicester dataset, surpassing state-of-the-art methods. We also implement it on a compute-in-memory platform with 8k memristor cells utilizing quantization-free mapping method and propose two algorithm-hardware co-optimization strategies to mitigate non-ideal hardware effects: weight outlier pre-constraint (WOP) and noise adaptation training (NAT). After optimization, our algorithm continues to outperform existing spike sorting methods, achieving accuracies of 94.2% and 99.7%, while also demonstrating improved robustness. The memristor platform only exhibits a 2% and 1.5% accuracy drop compared to software results on the two difficult subsets. Additionally, it achieves 3.52 $ \boldsymbol{\mu}$J energy consumption and 0.5 ms latency per inference. This work offers promising solutions for brain-computer interface systems and neural prosthesis applications in the future.
