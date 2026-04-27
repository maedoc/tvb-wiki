# BrainSegNet: A Novel Framework for Whole-Brain MRI Parcellation Enhanced by Large Models

**Source**: semantic-scholar
**ID**: 1422c5af77e8e6cb32bf781d12bcf09d7ef8ab41
**DOI**: 10.48550/arXiv.2601.09263
**URL**: https://www.semanticscholar.org/paper/1422c5af77e8e6cb32bf781d12bcf09d7ef8ab41
**Date**: 2026-01-14
**Year**: 2026
**Authors**: Yucheng Li, Xiaofan Wang, Junyi Wang, Yijie Li, Xi Zhu, Mubai Du, Dian Sheng, Wei Zhang, Fan Zhang
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Whole-brain parcellation from MRI is a critical yet challenging task due to the complexity of subdividing the brain into numerous small, irregular shaped regions. Traditionally, template-registration methods were used, but recent advances have shifted to deep learning for faster workflows. While large models like the Segment Anything Model (SAM) offer transferable feature representations, they are not tailored for the high precision required in brain parcellation. To address this, we propose BrainSegNet, a novel framework that adapts SAM for accurate whole-brain parcellation into 95 regions. We enhance SAM by integrating U-Net skip connections and specialized modules into its encoder and decoder, enabling fine-grained anatomical precision. Key components include a hybrid encoder combining U-Net skip connections with SAM's transformer blocks, a multi-scale attention decoder with pyramid pooling for varying-sized structures, and a boundary refinement module to sharpen edges. Experimental results on the Human Connectome Project (HCP) dataset demonstrate that BrainSegNet outperforms several state-of-the-art methods, achieving higher accuracy and robustness in complex, multi-label parcellation.
