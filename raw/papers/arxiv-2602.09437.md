# Diffusion-Guided Pretraining for Brain Graph Foundation Models

**arXiv ID**: 2602.09437
**Published**: 2026-02-10
**Updated**: 2026-03-07
**Authors**: Xinxu Wei, Rong Zhou, Lifang He, Yu Zhang
**Categories**: cs.LG, cs.AI
**URL**: https://arxiv.org/abs/2602.09437
**PDF**: https://arxiv.org/pdf/2602.09437
**Source**: arXiv

## Abstract

With the growing interest in foundation models for brain signals, graph-based pretraining has emerged as a promising paradigm for learning transferable representations from connectome data. However, existing contrastive and masked autoencoder methods typically rely on naive random dropping or masking for augmentation, which is ill-suited for brain graphs and hypergraphs as it disrupts semantically meaningful connectivity patterns. Moreover, commonly used graph-level readout and reconstruction schemes fail to capture global structural information, limiting the robustness of learned representations. In this work, we propose a unified diffusion-based pretraining framework that addresses both limitations. First, diffusion is designed to guide structure-aware dropping and masking strategies, preserving brain graph semantics while maintaining effective pretraining diversity. Second, diffusion enables topology-aware graph-level readout and node-level global reconstruction by allowing graph embeddings and masked nodes to aggregate information from globally related regions. Extensive experiments across multiple neuroimaging datasets with over 25,000 subjects and 60,000 scans involving various mental disorders and brain atlases demonstrate consistent performance improvements.
