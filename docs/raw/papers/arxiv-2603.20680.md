# Hierarchical Multiscale Structure-Function Coupling for Brain Connectome Integration

**Source**: arxiv
**ID**: 2603.20680
**URL**: https://arxiv.org/abs/2603.20680
**Date**: 2026-03-21
**Year**: 2026
**Authors**: Jianwei Chen, Zhengyang Miao, Wenjie Cai, Jiaxue Tang, Boxing Liu, Yunfan Zhang, Yuhang Yang, Hao Tang, Carola-Bibiane Schönlieb, Zaixu Cui, Du Lei, Shouliang Qi, Chao Li
**Categories**: q-bio.NC, cs.LG

## Abstract

Integrating structural and functional connectomes remains challenging because their relationship is non-linear and organized over nested modular hierarchies. We propose a hierarchical multiscale structure-function coupling framework for connectome integration that jointly learns individualized modular organization and hierarchical coupling across structural connectivity (SC) and functional connectivity (FC). The framework includes: (i) Prototype-based Modular Pooling (PMPool), which learns modality-specific multiscale communities by selecting prototypical ROIs and optimizing a differentiable modularity-inspired objective; (ii) an Attention-based Hierarchical Coupling Module (AHCM) that models both within-hierarchy and cross-hierarchy SC-FC interactions to produce enriched hierarchical coupling representations; and (iii) a Coupling-guided Clustering loss (CgC-Loss) that regularizes SC and FC community assignments with coupling signals, allowing cross-modal interactions to shape community alignment across hierarchies. We evaluate the model's performance across four cohorts for predicting brain age, cognitive score, and disease classification. Our model consistently outperforms baselines and other state-of-the-art approaches across three tasks. Ablation and sensitivity analyses verify the contributions of key components. Finally, the visualizations of learned coupling reveal interpretable differences, suggesting that the framework captures biologically meaningful structure-function relationships.
