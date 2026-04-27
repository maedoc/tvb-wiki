# Predicting Post-Traumatic Epilepsy from Clinical Records using Large Language Model Embeddings

**Source**: arxiv
**ID**: 2604.14547
**URL**: https://arxiv.org/abs/2604.14547
**Date**: 2026-04-16
**Year**: 2026
**Authors**: Wenhui Cui, Nicholas Swingle, Anand A. Joshi, Dileep Nair, Richard M. Leahy
**Categories**: cs.LG

## Abstract

Objective: Post-traumatic epilepsy (PTE) is a debilitating neurological disorder that develops after traumatic brain injury (TBI). Early prediction of PTE remains challenging due to heterogeneous clinical data, limited positive cases, and reliance on resource-intensive neuroimaging data. We investigate whether routinely collected acute clinical records alone can support early PTE prediction using language model-based approaches. Methods: Using a curated subset of the TRACK-TBI cohort, we developed an automated PTE prediction framework that implements pretrained large language models (LLMs) as fixed feature extractors to encode clinical records. Tabular features, LLM-generated embeddings, and hybrid feature representations were evaluated using gradient-boosted tree classifiers under stratified cross-validation. Results: LLM embeddings achieved performance improvements by capturing contextual clinical information compared to using tabular features alone. The best performance was achieved by a modality-aware feature fusion strategy combining tabular features and LLM embeddings, achieving an AUC-ROC of 0.892 and AUPRC of 0.798. Acute post-traumatic seizures, injury severity, neurosurgical intervention, and ICU stay are key contributors to the predictive performance. Significance: These findings demonstrate that routine acute clinical records contain information suitable for early PTE risk prediction using LLM embeddings in conjunction with gradient-boosted tree classifiers. This approach represents a promising complement to imaging-based prediction.
