# Ada-FCN: Adaptive Frequency-Coupled Network for fMRI-Based Brain Disorder Classification

**Source**: semantic-scholar
**ID**: efb8086381bff10c4a3e02ddc7c37a20abffa394
**DOI**: 10.1007/978-3-032-05162-2_4
**URL**: https://www.semanticscholar.org/paper/efb8086381bff10c4a3e02ddc7c37a20abffa394
**Date**: 2025-11-06
**Year**: 2025
**Authors**: Y. Xun, Jiaxin Xu, Wenbo Gao, Chen Yang, Shujun Wang
**Venue**: International Conference on Medical Image Computing and Computer-Assisted Intervention
**Citations**: 2

## Abstract

Resting-state fMRI has become a valuable tool for classifying brain disorders and constructing brain functional connectivity networks by tracking BOLD signals across brain regions. However, existing mod els largely neglect the multi-frequency nature of neuronal oscillations, treating BOLD signals as monolithic time series. This overlooks the cru cial fact that neurological disorders often manifest as disruptions within specific frequency bands, limiting diagnostic sensitivity and specificity. While some methods have attempted to incorporate frequency informa tion, they often rely on predefined frequency bands, which may not be optimal for capturing individual variability or disease-specific alterations. To address this, we propose a novel framework featuring Adaptive Cas cade Decomposition to learn task-relevant frequency sub-bands for each brain region and Frequency-Coupled Connectivity Learning to capture both intra- and nuanced cross-band interactions in a unified functional network. This unified network informs a novel message-passing mecha nism within our Unified-GCN, generating refined node representations for diagnostic prediction. Experimental results on the ADNI and ABIDE datasets demonstrate superior performance over existing methods. The code is available at https://github.com/XXYY20221234/Ada-FCN.
