# Clinically-Informed Modeling for Pediatric Brain Tumor Classification from Whole-Slide Histopathology Images

**Source**: semantic-scholar
**ID**: 3369b57c314b921ee25acb3c5214202b11e3712c
**URL**: https://www.semanticscholar.org/paper/3369b57c314b921ee25acb3c5214202b11e3712c
**Date**: 2026-04-22
**Year**: 2026
**Authors**: Joakim Nguyen, Jian Yu, Jinrui Fang, N. Konz, Tianlong Chen, Sanjay Krishnan, C. Krishnan, Ying Ding, Hairong Wang, A. Shukla
**Citations**: 0

## Abstract

Accurate diagnosis of pediatric brain tumors, starting with histopathology, presents unique challenges for deep learning, including severe data scarcity, class imbalance, and fine-grained morphologic overlap across diagnostically distinct subtypes. While pathology foundation models have advanced patch-level representation learning, their effective adaptation to weakly supervised pediatric brain tumor classification under limited data remains underexplored. In this work, we introduce an expert-guided contrastive fine-tuning framework for pediatric brain tumor diagnosis from whole-slide images (WSI). Our approach integrates contrastive learning into slide-level multiple instance learning (MIL) to explicitly regularize the geometry of slide-level representations during downstream fine-tuning. We propose both a general supervised contrastive setting and an expert-guided variant that incorporates clinically informed hard negatives targeting diagnostically confusable subtypes. Through comprehensive experiments on pediatric brain tumor WSI classification under realistic low-sample and class-imbalanced conditions, we demonstrate that contrastive fine-tuning yields measurable improvements in fine-grained diagnostic distinctions. Our experimental analyses reveal complementary strengths across different contrastive strategies, with expert-guided hard negatives promoting more compact intra-class representations and improved inter-class separation. This work highlights the importance of explicitly shaping slide-level representations for robust fine-grained classification in data-scarce pediatric pathology settings.
