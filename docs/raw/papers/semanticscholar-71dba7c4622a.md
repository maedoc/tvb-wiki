# Brain-Inspired Broad Learning Framework: Spiking Neural Network for Enhanced EEG Prediction

**Source**: semantic-scholar
**ID**: 71dba7c4622afe4bec4d4601862457b3239fe614
**DOI**: 10.1109/TETCI.2025.3647698
**URL**: https://www.semanticscholar.org/paper/71dba7c4622afe4bec4d4601862457b3239fe614
**Date**: 2026-04-01
**Year**: 2026
**Authors**: Yaodong Wang, Yiping Zuo, Dan Chen, Weiping Tu, Jingying Chen, Tengfei Gao, Xiaoli Li
**Venue**: IEEE Transactions on Emerging Topics in Computational Intelligence
**Citations**: 0

## Abstract

Real-time decoding of brain signals is critical for applications ranging from Brain-Computer Interface (BCI) to clinical neurodiagnostics. While various learning methods are used for predicting EEG streams, Spiking Neural Networks (SNNs) offer a compelling approach due to their sparse, event-driven computation, which naturally aligns with the temporal dynamics of neural signals. However, applying SNNs to high-dimensional, evolving EEG data reveals critical limitations: deep architectures are prone to convergence failure from excessive signal diffusion, and adapting to EEG stream requires computationally expensive global retraining. To address these limitations, this study proposes a Brain-inspired Broad Learning framework (<inline-formula><tex-math notation="LaTeX">$B^{2}\,L$</tex-math></inline-formula>-<inline-formula><tex-math notation="LaTeX">$SNN$</tex-math></inline-formula>). Mimicking hippocampal synaptic mechanisms, the framework involves: 1) a dual-layer, parallel architecture with Random Vector Functional-Link (RVFL) mappings that enables robust pattern interpretation while addressing the diffusion issue; and 2) a synaptic growth-inspired optimization that achieves efficient incremental learning by dynamically extending the network, eliminating the need for iterative global updates. Experiments on five benchmark datasets demonstrate that <inline-formula><tex-math notation="LaTeX">$B^{2}\,L$</tex-math></inline-formula>-<inline-formula><tex-math notation="LaTeX">$SNN$</tex-math></inline-formula> significantly outperforms competing SNN variants and other methods. For instance, on a motor imagery task, it achieves 94.45% accuracy while reducing inference time by 64.9%. In dynamic tests, it maintained 92.37% accuracy with only an additional 2.74 seconds of training, proving its efficient incremental learning capability. Overall, this study provides an effective alternative SNN design, supporting the advancement of sophisticated neuroengineering applications.
