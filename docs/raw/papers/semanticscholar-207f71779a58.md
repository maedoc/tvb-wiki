# Integrating Cortical Source Reconstruction and Adversarial Learning for EEG Classification

**Source**: semantic-scholar
**ID**: 207f71779a58d11020ba561eed336f4e0fe18b8b
**DOI**: 10.3390/s25164989
**URL**: https://www.semanticscholar.org/paper/207f71779a58d11020ba561eed336f4e0fe18b8b
**Date**: 2025-08-01
**Year**: 2025
**Authors**: Yue Guo, Yan Pei, Rong Yao, Yueming Yan, Meirong Song, Haifang Li
**Venue**: Italian National Conference on Sensors
**Citations**: 1

## Abstract

Existing methods for diagnosing depression rely heavily on subjective evaluations, whereas electroencephalography (EEG) emerges as a promising approach for objective diagnosis due to its non-invasiveness, low cost, and high temporal resolution. However, current EEG analysis methods are constrained by volume conduction effect and class imbalance, both of which adversely affect classification performance. To address these issues, this paper proposes a multi-stage deep learning model for EEG-based depression classification, integrating a cortical feature extraction strategy (CFE), a feature attention module (FA), a graph convolutional network (GCN), and a focal adversarial domain adaptation module (FADA). Specifically, the CFE strategy reconstructs brain cortical signals using the standardized low-resolution brain electromagnetic tomography (sLORETA) algorithm and extracts both linear and nonlinear features that capture cortical activity variations. The FA module enhances feature representation through a multi-head self-attention mechanism, effectively capturing spatiotemporal relationships across distinct brain regions. Subsequently, the GCN further extracts spatiotemporal EEG features by modeling functional connectivity between brain regions. The FADA module employs Focal Loss and Gradient Reversal Layer (GRL) mechanisms to suppress domain-specific information, alleviate class imbalance, and enhance intra-class sample aggregation. Experimental validation on the publicly available PRED+CT dataset demonstrates that the proposed model achieves a classification accuracy of 85.33%, outperforming current state-of-the-art methods by 2.16%. These results suggest that the proposed model holds strong potential for improving the accuracy and reliability of EEG-based depression classification.
