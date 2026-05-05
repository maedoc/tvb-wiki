# Towards Label-Efficient Deep Learning-Based Aging-Related Bug Prediction With Spiking Convolutional Neural Networks

**Source**: semantic-scholar
**ID**: 28d3f5a4c2ab4a5e99e43bbc1aeaf7e4114dc17f
**DOI**: 10.1109/TETC.2025.3531051
**URL**: https://www.semanticscholar.org/paper/28d3f5a4c2ab4a5e99e43bbc1aeaf7e4114dc17f
**Date**: 2025-04-01
**Year**: 2025
**Authors**: Yunzhe Tian, Yike Li, Kang Chen, Zhenguo Zhang, Endong Tong, Jiqiang Liu, Fangyun Qin, Zheng Zheng, Wenjia Niu
**Venue**: IEEE Transactions on Emerging Topics in Computing
**Citations**: 2

## Abstract

Recent advances in Deep Learning (DL) have enhanced Aging-Related Bug (ARB) prediction for mitigating software aging. However, DL-based ARB prediction models face a dual challenge: overcoming overfitting to enhance generalization and managing the high labeling costs associated with extensive data requirements. To address the first issue, we utilize the sparse and binary nature of spiking communication in Spiking Neural Networks (SNNs), which inherently provides brain-inspired regularization to effectively alleviate overfitting. Therefore, we propose a Spiking Convolutional Neural Network (SCNN)-based ARB prediction model along with a training framework that handles the model’s spatial-temporal dynamics and non-differentiable nature. To reduce labeling costs, we introduce a Bio-inspired and Diversity-aware Active Learning framework (BiDAL), which prioritizes highly informative and diverse samples, enabling more efficient usage of the limited labeling budget. This framework incorporates bio-inspired uncertainty to enhance informativeness measurement along with using a diversity-aware selection strategy based on clustering to prevent redundant labeling. Experiments on three ARB datasets show that ARB-SCNN effectively reduces overfitting, improving generalization performance by 6.65% over other DL-based classifiers. Additionally, BiDAL boosts label efficiency for ARB-SCNN training, outperforming four state-of-the-art active learning methods by 4.77% within limited labeling budgets.
