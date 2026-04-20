# Multimodal Connectome Fusion via Cross-Attention for Autism Spectrum Disorder Classification Using Graph Learning

**arXiv ID**: 2603.15168
**Published**: 2026-03-16
**Updated**: 2026-03-16
**Authors**: Ansar Rahman, Hassan Shojaee-Mend, Sepideh Hatamikia
**Categories**: cs.CV, cs.AI
**URL**: https://arxiv.org/abs/2603.15168
**PDF**: https://arxiv.org/pdf/2603.15168
**Source**: arXiv

## Abstract

Autism spectrum disorder (ASD) is a complex neurodevelopmental condition characterized by atypical functional brain connectivity and subtle structural alterations. rs-fMRI has been widely used to identify disruptions in large-scale brain networks, while structural MRI provides complementary information about morphological organization. Despite their complementary nature, effectively integrating these heterogeneous imaging modalities within a unified framework remains challenging. This study proposes a multimodal graph learning framework that preserves the dominant role of functional connectivity while integrating structural imaging and phenotypic information for ASD classification. The proposed framework is evaluated on ABIDE-I dataset. Each subject is represented as a node within a population graph. Functional and structural features are extracted as modality-specific node attributes, while inter-subject relationships are modeled using a pairwise association encoder (PAE) based on phenotypic information. Two Edge Variational GCNs are trained to learn subject-level embeddings. To enable effective multimodal integration, we introduce a novel asymmetric transformer-based cross-attention mechanism that allows functional embeddings to selectively incorporate complementary structural information while preserving functional dominance. The fused embeddings are then passed to a MLP for ASD classification. Using stratified 10-fold cross-validation, the framework achieved an AUC of 87.3% and an accuracy of 84.4%. Under leave-one-site-out cross-validation (LOSO-CV), the model achieved an average cross-site accuracy of 82.0%, outperforming existing methods by approximately 3% under 10-fold cross-validation and 7% under LOSO-CV. The proposed framework effectively integrates heterogeneous multimodal data from the multi-site ABIDE-I dataset, improving automated ASD classification across imaging sites.
