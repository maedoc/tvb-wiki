# AAG-NAS-MSCNet: Enhanced Nested Transformer U-Net with Neural Architecture Search and Multi-Scale Classification Network for Brain Tumor Segmentation and Classification

**Source**: semantic-scholar
**ID**: afc9b68e804a695eae1631e44c8123460aeab6ce
**DOI**: 10.1109/ICMNWC66779.2025.11354391
**URL**: https://www.semanticscholar.org/paper/afc9b68e804a695eae1631e44c8123460aeab6ce
**Date**: 2025-12-10
**Year**: 2025
**Authors**: H. R. Prakash Kumar, M. D. Anitha Devi
**Venue**: 2025 5th International Conference on Mobile Networks and Wireless Communications (ICMNWC)
**Citations**: 0

## Abstract

Brain tumors are one of the most life-threatening neurological disorders, and their accurate detection and classification are essential for effective treatment planning. Although Magnetic Resonance Imaging (MRI) offers rich multimodal data, existing Deep Learning frameworks often struggle to suppress irrelevant background features, leading to blurred tumor boundaries and inconsistent inter-scale feature alignment. The existing Nested Transformer U-Net with Neural Architecture Search (NTU-NAS) segmentation framework performs effectively, yet redundant information persists through skip connections, while the MSC-Net classifier lacks feature-level coherence across scales. To overcome this limitation, this research proposes a AAG-NAS-MSCNet model, which is an integrated framework combining Additive Attention Gated NTU-NAS for accurate tumor segmentation and an improved Multi-Scale Classification Network (MSC-Net) enhanced with Cross Feature Correction and Enhancement (CFCE) blocks for robust classification. Additive attention gates selectively highlight tumor-relevant regions, and CFCE modules align hierarchical representations for reliable grading. The proposed AAG-NAS-MSCNet model is trained and validated on the BraTS-2021 dataset and TCGA-GBM dataset, achieving improved Dice scores of $\mathbf{9 5. 0 5 \%, ~} \mathbf{9 4. 4 7 \%}$, and $\mathbf{9 6. 8 5 \%}$ for ET, TC, and WT regions, respectively, and a classification accuracy of 98.95%, outperforming all existing baselines. The results confirm that AAG-NAS-MSCNet effectively balances accuracy, computational efficiency, and generalization across diverse MRI dataset.
