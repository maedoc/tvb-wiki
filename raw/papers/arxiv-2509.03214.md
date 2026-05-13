# RTGMFF: Enhanced fMRI-Based Brain Disorder Diagnosis via ROI-Driven Text Generation and Multimodal Feature Fusion

**Source**: semantic-scholar
**ID**: d1213aeb4ab310458a649b02e477233d85442878
**DOI**: 10.1109/BIBM66473.2025.11356807
**URL**: https://www.semanticscholar.org/paper/d1213aeb4ab310458a649b02e477233d85442878
**Date**: 2025-09-03
**Year**: 2025
**Authors**: Junhao Jia, Yifei Sun, Yunyou Liu, Cheng Yang, Changmiao Wang, Feiwei Qin, Yong Peng, Wenwen Min
**Venue**: IEEE International Conference on Bioinformatics and Biomedicine
**Citations**: 3

## Abstract

Functional magnetic resonance imaging (fMRI) is a powerful tool for probing brain function, yet reliable clinical diagnosis is hampered by low signal-to-noise ratios, inter-subject variability, and the limited frequency awareness of prevailing CNN- and Transformer-based models. Moreover, most fMRI datasets lack textual annotations that could contextualize regional activation and connectivity patterns. We introduce RTGMFF, a framework that unifies automatic ROI-level text generation with multimodal feature fusion for brain-disorder diagnosis. RTGMFF consists of three components: (i) ROI-driven fMRI text generation deterministically condenses each subject's activation, connectivity, age, and sex into reproducible text tokens; (ii) Hybrid frequency-spatial encoder fuses a hierarchical waveletmamba branch with a cross-scale Transformer encoder to capture frequency-domain structure alongside long-range spatial dependencies; and (iii) Adaptive semantic alignment module embeds the ROI token sequence and visual features in a shared space, using a regularized cosine-similarity loss to narrow the modality gap. Extensive experiments on the ADHD-200 and ABIDE benchmarks show that RTGMFF surpasses current methods in diagnostic accuracy, achieving notable gains in sensitivity, specificity, and area under the ROC curve. Code is available at https://github.com/BeistMedAI/RTGMFF.
