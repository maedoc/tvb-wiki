# Mizar: Boosting Secure Three-Party Deep Learning with Co-Designed Sign-Bit Extraction and GPU Acceleration

**Source**: semantic-scholar
**ID**: 7c807a732622acd30917122aad6b8ff15e6c8431
**DOI**: 10.1109/ACSAC67867.2025.00076
**URL**: https://www.semanticscholar.org/paper/7c807a732622acd30917122aad6b8ff15e6c8431
**Date**: 2025-12-08
**Year**: 2025
**Authors**: Ye Dong, Xudong Chen, Xiangfu Song, Yaxi Yang, Tianwei Zhang, Jin-Song Dong
**Venue**: Asia-Pacific Computer Systems Architecture Conference
**Citations**: 1

## Abstract

Three-party secret sharing-based computation has emerged as a promising approach for secure deep learning, benefiting from its high throughput. However, it still faces persistent challenges in computing complex operations such as secure Sign-Bit Extraction, particularly in high-latency and low-bandwidth networks. A recent work, Aegis (Lu et al., Cryptology ePrint'2023), made significant strides by proposing a constant-round DGK-style Sign-Bit Extraction protocol with GPU acceleration on Piranha (Watson et. al., USENIX Security'2022). However, Aegis exhibits two critical limitations: it i) overlooks the use of bit-wise prefix-sum, and ii) inherits non-optimized modular arithmetic over prime fields and excessive memory overhead from the underlying GPU-based MPC framework. This results in suboptimal performance in terms of communication, computation, and GPU memory usage. Driven by the limitations of Aegis, we propose an optimized constant-round secure Sign-Bit Extraction protocol with communication and GPU-specific optimizations. Concretely, we construct a new masked randomized list by exploiting the upper bound of bit-wise prefix-sum to reduce online communication by up to 50%, and integrate fast modular-reduction and kernel fusion techniques to enhance GPU utilization in MPC protocols. Besides, we propose specific optimizations for secure piecewise polynomial approximations and Maxpool computation in neural network evaluations. Finally, we instantiate these protocols as a framework Mizar and report their improved performance over state-of-the-art GPU-based solutions: i) For secure Sign-Bit Extraction, we achieve a speedup of 2-2.5 × and reduce communication by 2-3.5 ×. ii) Furthermore, we improve the performance of secure evaluation of nonlinear functions and neural networks by 1.5-3.5 ×. iii) Lastly, our framework achieves 10%-50% GPU memory savings.
