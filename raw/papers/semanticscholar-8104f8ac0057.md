# A Causal Validation augmented Temporal Convolutional Framework for Brain Effective Connectivity Networks Estimation

**Source**: semantic-scholar
**ID**: 8104f8ac00577b6f9a62f497f3343608c1492ef3
**DOI**: 10.1016/j.neunet.2025.108405
**URL**: https://www.semanticscholar.org/paper/8104f8ac00577b6f9a62f497f3343608c1492ef3
**Date**: 2025-11-29
**Year**: 2025
**Authors**: Aoxiang Dong, Jun Cao, P. Sarrigiannis, Daniel Blackburn, Andrew Starr, Yifan Zhao
**Venue**: Neural Networks
**Citations**: 0

## Abstract

Advancements in neuroimaging have facilitated unprecedented insights into brain connectivity, making the study of brain effective connectivity networks (ECNs) essential for understanding neurological functions and diseases. Recently, neural networks (NNs) have emerged as powerful tools for ECN estimation due to their prominent universal approximation ability and less reliance on prior knowledge. However, most NN-based approaches fail to eliminate redundant temporal information and lack rigorous causal validation mechanisms. This paper introduces a novel end-to-end framework for estimating ECNs utilising Least Absolute Shrinkage and Selection Operator (Lasso) regression of Temporal Convolutional Networks (TCNs), named the Causal Validation augmented Temporal Convolutional Framework (CVTCF). In the CVTCF, a convolutional Hierarchical Group Lasso (cHGL) is proposed to detect Granger Causality (GC) inputs and eliminate redundant temporal information during GC detection. Additionally, the framework incorporates permutation importance validation based on the Wilcoxon signed-rank test to enhance the reliability of GC detection. The proposed CVTCF generally outperformed state-of-the-art methods in a controlled simulation using the chaotic Lorenz-96 model and the publicly available blood-oxygen-level-dependent (BOLD) benchmark dataset. Furthermore, the proposed CVTCF has enabled a detailed analysis of the causal interactions within the cerebral cortex, bringing to light the intricate relationships that underlie neurological functioning and impairment of neurodegenerative conditions like Alzheimer's Disease (AD) and Parkinson's Disease (PD). This study demonstrates the potential of using ECN estimation based on the CVTCF as indicators for neurodegenerative diseases and paves the way for future diagnostic and therapeutic strategies.
