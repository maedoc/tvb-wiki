# ToxDL 2.0: Protein toxicity prediction using a pretrained language model and graph neural networks

**Source**: semantic-scholar
**ID**: 5938b84158e570b628fd4fe075f5472372debfaa
**DOI**: 10.1016/j.csbj.2025.04.002
**URL**: https://www.semanticscholar.org/paper/5938b84158e570b628fd4fe075f5472372debfaa
**Date**: 2025-04-01
**Year**: 2025
**Authors**: Lin Zhu, Yi Fang, Shuting Liu, Hongbin Shen, Wim De Neve, Xiaoyong Pan
**Venue**: Computational and Structural Biotechnology Journal
**Citations**: 15

## Abstract

Motivation Assessing the potential toxicity of proteins is crucial for both therapeutic and agricultural applications. Traditional experimental methods for protein toxicity evaluation are time-consuming, expensive, and labor-intensive, highlighting the requirement for efficient computational approaches. Recent advancements in language models and deep learning have significantly improved protein toxicity prediction, yet current models often lack the ability to integrate evolutionary and structural information, which is crucial for accurate toxicity assessment of proteins. Results In this study, we present ToxDL 2.0, a novel multimodal deep learning model for protein toxicity prediction that integrates both evolutionary and structural information derived from a pretrained language model and AlphaFold2. ToxDL 2.0 consists of three key modules: (1) a Graph Convolutional Network (GCN) module for generating protein graph embeddings based on AlphaFold2-predicted structures, (2) a domain embedding module for capturing protein domain representations, and (3) a dense module that combines these embeddings to predict the toxicity. After constructing a comprehensive toxicity benchmark dataset, we obtained experimental results on both an original non-redundant test set (comprising pre-2022 protein sequences) and an independent non-redundant test set (a holdout set of post-2022 protein sequences), demonstrating that ToxDL 2.0 outperforms existing state-of-the-art methods. Additionally, we utilized Integrated Gradients to discover known toxic motifs associated with protein toxicity. A web server for ToxDL 2.0 is publicly available at www.csbio.sjtu.edu.cn/bioinf/ToxDL2/.
