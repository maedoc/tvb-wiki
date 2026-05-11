# D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models

**Source**: arxiv
**ID**: 2605.05204
**URL**: https://arxiv.org/abs/2605.05204
**Date**: 2026-05-06
**Year**: 2026
**Authors**: Dengyang Jiang, Xin Jin, Dongyang Liu, Zanyi Wang, Mingzhe Zheng, Ruoyi Du, Xiangpeng Yang, Qilong Wu, Zhen Li, Peng Gao, Harry Yang, Steven Hoi
**Categories**: cs.CV

## Abstract

The landscape of high-performance image generation models is currently shifting from the inefficient multi-step ones to the efficient few-step counterparts (e.g, Z-Image-Turbo and FLUX.2-klein). However, these models present significant challenges for directly continuous supervised fine-tuning. For example, applying the commonly used fine-tuning technique would compromises their inherent few-step inference capability. To address this, we propose D-OPSD, a novel training paradigm for step-distilled diffusion models that enables on-policy learning during supervised fine-tuning. We first find that the modern diffusion model where the LLM/VLM serves as the encoder can inherit its encoder's in-context capabilities. This enables us to make the training as an on-policy self-distillation process. Specifically, during training, we make the model acts as both the teacher and the student with different contexts, where the student is conditioned only on the text feature, while the teacher is conditioned on the multimodal feature of both the text prompt and the target image. Training minimizes the two predicted distributions over the student's own roll-outs. By optimized on the model's own trajectory and under it's own supervision, D-OPSD enables the model to learn new concept, style, etc. without sacrificing the original few-step capacity.
