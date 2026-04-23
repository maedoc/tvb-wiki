# BLEG: LLM Functions as Powerful fMRI Graph-Enhancer for Brain Network Analysis

**Source**: arxiv
**ID**: 2604.07361
**URL**: https://arxiv.org/abs/2604.07361
**Date**: 2026-04-01
**Year**: 2026
**Authors**: Rui Dong, Zitong Wang, Jiaxing Li, Weihuang Zheng, Youyong Kong
**Categories**: cs.LG

## Abstract

Graph Neural Networks (GNNs) have been widely used in diverse brain network analysis tasks based on preprocessed functional magnetic resonance imaging (fMRI) data. However, their performances are constrained due to high feature sparsity and inherent limitations of domain knowledge within uni-modal neurographs. Meanwhile, large language models (LLMs) have demonstrated powerful representation capabilities. Combining LLMs with GNNs presents a promising direction for brain network analysis. While LLMs and MLLMs have emerged in neuroscience, integration of LLMs with graph-based data remains unexplored. In this work, we deal with these issues by incorporating LLM's powerful representation and generalization capabilities. Considering great cost for directly tuning LLMs, we instead function LLM as enhancer to boost GNN's performance on downstream tasks. Our method, namely BLEG, can be divided into three stages. We firstly prompt LLM to get augmented texts for fMRI graph data, then we design a LLM-LM instruction tuning method to get enhanced textual representations at a relatively lower cost. GNN is trained together for coarsened alignment. Finally we finetune an adapter after GNN for given downstream tasks. Alignment loss between LM and GNN logits is designed to further enhance GNN's representation. Extensive experiments on different datasets confirmed BLEG's superiority.Code can be available at https://github.com/KamonRiderDR/BLEG.
