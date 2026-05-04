# Empowering Heterogeneous Graph Foundation Models via Decoupled Relation Alignment

**Source**: arxiv
**ID**: 2605.00731
**URL**: https://arxiv.org/abs/2605.00731
**Date**: 2026-05-01
**Year**: 2026
**Authors**: Ziyu Zheng, Yaming Yang, Zhe Wang, Ziyu Guan, Wei Zhao
**Categories**: cs.SI, cs.AI

## Abstract

While Graph Foundation Models (GFMs) have achieved remarkable success in homogeneous graphs, extending them to multi-domain heterogeneous graphs (MDHGs) remains a formidable challenge due to cross-type feature shifts and intra-domain relation gaps. Existing global feature alignment methods (PCA or SVD) enforce a shared feature space blindly, which distorts type-specific semantics and disrupts original topologies, inevitably leading to "Type Collapse" and "Relation Confusion". To address these fundamental limitations, we propose Decoupled relation Subspace Alignment (DRSA), a novel, plug-and-play relation-driven alignment framework. DRSA fundamentally shifts the paradigm by decoupling feature semantics from relation structures. Specifically, it introduces a dual-relation subspace projection mechanism to coordinate cross-type interactions within a shared low-rank relation subspace explicitly. Furthermore, a feature-structure decoupled representation is designed to decompose aligned features into a semantic projection component and a structural residual term, adaptively absorbing intra-domain variations. Optimized via a stable alternating minimization strategy based on Block Coordinate Descent, DRSA constructs a well-calibrated, structure-aware latent space. Extensive experiments on multiple real-world benchmark datasets demonstrate that DRSA can be seamlessly integrated as a universal preprocessing module, significantly and consistently enhancing the cross-domain and few-shot knowledge transfer capabilities of state-of-the-art GFMs. The code is available at: https://github.com/zhengziyu77/DSRA.
