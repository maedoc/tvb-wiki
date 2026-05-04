# Let ViT Speak: Generative Language-Image Pre-training

**Source**: arxiv
**ID**: 2605.00809
**URL**: https://arxiv.org/abs/2605.00809
**Date**: 2026-05-01
**Year**: 2026
**Authors**: Yan Fang, Mengcheng Lan, Zilong Huang, Weixian Lei, Yunqing Zhao, Yujie Zhong, Yingchen Yu, Qi She, Yao Zhao, Yunchao Wei
**Categories**: cs.CV

## Abstract

In this paper, we present \textbf{Gen}erative \textbf{L}anguage-\textbf{I}mage \textbf{P}re-training (GenLIP), a minimalist generative pretraining framework for Vision Transformers (ViTs) designed for multimodal large language models (MLLMs). To better align vision encoders with the autoregressive nature of LLMs, GenLIP trains a ViT to predict language tokens directly from visual tokens using a standard language modeling objective, without contrastive batch construction or an additional text decoder. This design offers three key advantages: (1) \textbf{Simplicity}: a single transformer jointly models visual and textual tokens; (2) \textbf{Scalability}: it scales effectively with both data and model size; and (3) \textbf{Performance}: it achieves competitive or superior results across diverse multimodal benchmarks. Trained on 8B samples from Recap-DataComp-1B, GenLIP matches or surpasses strong baselines despite using substantially less pretraining data. After continued pretraining on multi-resolution images at native aspect ratios, GenLIP further improves on detail-sensitive tasks such as OCR and chart understanding, making it a strong foundation for vision encoders in MLLMs.
