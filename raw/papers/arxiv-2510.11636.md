# LRQ-Solver: A Transformer-Based Neural Operator for Fast and Accurate Solving of Large-scale 3D PDEs

**Source**: semantic-scholar
**ID**: 2545cd56e192605122eea95d1f28902dce99e77f
**DOI**: 10.48550/arXiv.2510.11636
**URL**: https://www.semanticscholar.org/paper/2545cd56e192605122eea95d1f28902dce99e77f
**Date**: 2025-10-13
**Year**: 2025
**Authors**: Peijian Zeng, Guanzhong Wang, Haohao Gu, Xiaoguang Hu, Tiezhu Gao, Zhuowei Wang, Aimin Yang, Xiaoyu Song
**Venue**: arXiv.org
**Citations**: 1

## Abstract

Solving large-scale Partial Differential Equations (PDEs) on complex three-dimensional geometries represents a central challenge in scientific and engineering computing, often impeded by expensive pre-processing stages and substantial computational overhead. We introduce Low-Rank Query-based PDE Solver (LRQ-Solver), a physics-integrated framework engineered for rapid, accurate, and highly scalable simulations of industrial-grade models. This framework is built upon two primary technical innovations. First, our Parameter Conditioned Lagrangian Modeling (PCLM) approach explicitly couples local physical states with global design parameters, enabling robust predictions across varied simulation configurations. By embedding physical consistency directly into the learning architecture, PCLM ensures that predictions remain physically meaningful even under unseen design conditions, significantly enhancing generalization and reliability. Second, the Low-Rank Query Attention (LR-QA) module leverages the second-order statistics of physical fields to construct a global coherence kernel, reducing the computational complexity of attention from O(N2) to O(NC2 + C3). By replacing point-wise clustering with covariance decomposition, LRQ-Solver achieves exceptional scalability efficiently processing up to 2 million points on a single GPU. Validated on standard benchmarks, LRQ-Solver achieves a 38.9% error reduction on the DrivAerNet++ dataset and 28.76% on the 3D Beam dataset, alongside a training speedup of up to 50 times. Our results establish that LRQ-Solver offers a powerful paradigm for multi-configuration physics simulations, delivering a SOTA combination of accuracy, scalability, and efficiency. Code to reproduce the experiments is available at https://github.com/LilaKen/LRQ-Solver.
