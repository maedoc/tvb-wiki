# Brain-MGF: Multimodal Graph Fusion Network for EEG-fMRI Brain Connectivity Analysis Under Psilocybin

**Source**: semantic-scholar
**ID**: 9c6b33e398d8160e30442711c3597fd1dcd27a66
**DOI**: 10.48550/arXiv.2511.18325
**URL**: https://www.semanticscholar.org/paper/9c6b33e398d8160e30442711c3597fd1dcd27a66
**Date**: 2025-11-23
**Year**: 2025
**Authors**: S. Yap, Fuad M. Noman, J. Loo, D. Stoliker, Moein Khajehnejad, R. Phan, D. Dowe, Adeel Razi, Chee-Ming Ting
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Psychedelics, such as psilocybin, reorganise large-scale brain connectivity, yet how these changes are reflected across electrophysiological (electroencephalogram, EEG) and haemodynamic (functional magnetic resonance imaging, fMRI) networks remains unclear. We present Brain-MGF, a multimodal graph fusion network for joint EEG-fMRI connectivity analysis. For each modality, we construct graphs with partial-correlation edges and Pearson-profile node features, and learn subject-level embeddings via graph convolution. An adaptive softmax gate then fuses modalities with sample-specific weights to capture context-dependent contributions. Using the world's largest single-site psilocybin dataset, PsiConnect, Brain-MGF distinguishes psilocybin from no-psilocybin conditions in meditation and rest. Fusion improves over unimodal and non-adaptive variants, achieving 74.0% accuracy and 76.5% F1 score on meditation, and 76.0% accuracy with 85.8% ROC-AUC on rest. UMAP visualisations reveal clearer class separation for fused embeddings. These results indicate that adaptive graph fusion effectively integrates complementary EEG-fMRI information, providing an interpretable framework for characterising psilocybin-induced alterations in large-scale neural organisation.
