# Continuous-tone Simple Points: An $\ell_0$-Norm of Cyclic Gradient for Topology-Preserving Data-Driven Image Segmentation

**Source**: arxiv
**ID**: 2604.28159
**URL**: https://arxiv.org/abs/2604.28159
**Date**: 2026-04-30
**Year**: 2026
**Authors**: Wenxiao Li, Faqiang Wang, Yuping Duan, Li Cui, Liqiang Zhang, Jun Liu
**Categories**: cs.CV

## Abstract

Topological features play an essential role in ensuring geometric plausibility and structural consistency in image analysis tasks such as segmentation and skeletonization. However, integrating topology-preserving learning based on simple points into deep learning tasks remains challenging, as existing simple point detection methods are confined to binary images and are non-differentiable, rendering them incompatible with gradient-based optimization in modern deep learning. Moreover, morphological and purely data-driven approaches often fail to guaranty topological consistency. To address these limitations, we propose a novel method that directly computes simple points on continuous-valued images, enabling differentiable topological inference. Building on this theory, we develop an efficient skeleton extraction algorithm that preserves topological structures in binary and continuous-valued images. Furthermore, we design a variational model that enforces topological constraints by preserving topologically non-removable (i.e., non-simple) points, which can be seamlessly integrated into any deep neural network segmentation with softmax or sigmoid outputs. Experimental results demonstrate that the proposed approach effectively improves topological integrity and structural accuracy across multiple benchmarks. The codes are available in https://github.com/levnsio/CSP.
