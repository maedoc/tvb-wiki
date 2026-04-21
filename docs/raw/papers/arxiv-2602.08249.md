# A Unified Framework for Multimodal Image Reconstruction and Synthesis using Denoising Diffusion Models

**arXiv ID**: 2602.08249
**Published**: 2026-02-09
**Updated**: 2026-02-09
**Authors**: Weijie Gan, Xucheng Wang, Tongyao Wang, Wenshang Wang, Chunwei Ying, Yuyang Hu, Yasheng Chen, Hongyu An, Ulugbek S. Kamilov
**Categories**: eess.IV, cs.CV
**URL**: https://arxiv.org/abs/2602.08249
**PDF**: https://arxiv.org/pdf/2602.08249
**Source**: arXiv

## Abstract

Image reconstruction and image synthesis are important for handling incomplete multimodal imaging data, but existing methods require various task-specific models, complicating training and deployment workflows. We introduce Any2all, a unified framework that addresses this limitation by formulating these disparate tasks as a single virtual inpainting problem. We train a single, unconditional diffusion model on the complete multimodal data stack. This model is then adapted at inference time to ``inpaint'' all target modalities from any combination of inputs of available clean images or noisy measurements. We validated Any2all on a PET/MR/CT brain dataset. Our results show that Any2all can achieve excellent performance on both multimodal reconstruction and synthesis tasks, consistently yielding images with competitive distortion-based performance and superior perceptual quality over specialized methods.
