# pyFAST: A Modular PyTorch Framework for Time Series Modeling with Multi-source and Sparse Data

**Source**: semantic-scholar
**ID**: 47c4ec90cf56ba61c540b618b2569468891de17b
**DOI**: 10.48550/arXiv.2508.18891
**URL**: https://www.semanticscholar.org/paper/47c4ec90cf56ba61c540b618b2569468891de17b
**Date**: 2025-08-26
**Year**: 2025
**Authors**: Zhijin Wang, Senzhen Wu, Yue Hu, X. Liu
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Modern time series analysis demands frameworks that are flexible, efficient, and extensible. However, many existing Python libraries exhibit limitations in modularity and in their native support for irregular, multi-source, or sparse data. We introduce pyFAST, a research-oriented PyTorch framework that explicitly decouples data processing from model computation, fostering a cleaner separation of concerns and facilitating rapid experimentation. Its data engine is engineered for complex scenarios, supporting multi-source loading, protein sequence handling, efficient sequence- and patch-level padding, dynamic normalization, and mask-based modeling for both imputation and forecasting. pyFAST integrates LLM-inspired architectures for the alignment-free fusion of sparse data sources and offers native sparse metrics, specialized loss functions, and flexible exogenous data fusion. Training utilities include batch-based streaming aggregation for evaluation and device synergy to maximize computational efficiency. A comprehensive suite of classical and deep learning models (Linears, CNNs, RNNs, Transformers, and GNNs) is provided within a modular architecture that encourages extension. Released under the MIT license at GitHub, pyFAST provides a compact yet powerful platform for advancing time series research and applications.
