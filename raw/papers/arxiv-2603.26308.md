# D-GATNet: Interpretable Temporal Graph Attention Learning for ADHD Identification Using Dynamic Functional Connectivity

**Source**: arxiv
**ID**: 2603.26308
**URL**: https://arxiv.org/abs/2603.26308
**Date**: 2026-03-27
**Year**: 2026
**Authors**: Qurat Ul Ain, Alptekin Temizel, Soyiba Jawed
**Categories**: cs.LG

## Abstract

Attention Deficit Hyperactivity Disorder (ADHD) is a prevalent neurodevelopmental disorder whose neuroimaging-based diagnosis remains challenging due to complex time-varying disruptions in brain connectivity. Functional MRI (fMRI) provides a powerful non-invasive modality for identifying functional alterations. Existing deep learning (DL) studies employ diverse neuroimaging features; however, static functional connectivity remains widely used, whereas dynamic connectivity modeling is comparatively underexplored. Moreover, many DL models lack interpretability. In this work, we propose D-GATNet, an interpretable temporal graph-based framework for automated ADHD classification using dynamic functional connectivity (dFC). Sliding-window Pearson correlation constructs sequences of functional brain graphs with regions of interest as nodes and connectivity strengths as edges. Spatial dependencies are learned via a multi-layer Graph Attention Network, while temporal dynamics are modeled using 1D convolution followed by temporal attention. Interpretability is achieved through graph attention weights revealing dominant ROI interactions, ROI importance scores identifying influential regions, and temporal attention emphasizing informative connectivity segments. Experiments on the Peking University site of the ADHD-200 dataset using stratified 10-fold cross-validation with a 5-seed ensemble achieved 85.18% +_5.64 balanced accuracy and 0.881 AUC, outperforming state-of-the-art methods. Attention analysis reveals cerebellar and default mode network disruptions, indicating potential neuroimaging biomarkers.
