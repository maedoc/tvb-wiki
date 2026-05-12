# MoCoTalk: Multi-Conditional Diffusion with Adaptive Router for Controllable Talking Head Generation

**Source**: arxiv
**ID**: 2605.08050
**URL**: https://arxiv.org/abs/2605.08050
**Date**: 2026-05-08
**Year**: 2026
**Authors**: Xinyan Ye, Jiankang Deng, Abbas Edalat
**Categories**: cs.CV

## Abstract

Talking-head generation requires joint modeling of identity, head pose, facial expression, and mouth dynamics. Existing methods typically address only a subset of these factors, and rely on fixed-weight or heuristic fusion when multiple conditions are involved. We present MoCoTalk, a multi-conditional video diffusion framework that unifies four complementary control signals: a reference image, facial keypoints, 3DMM-rendered shading meshes, and the corresponding speech audio. To resolve destructive interference among heterogeneous conditions, we introduce an Adaptive Multi-Condition Router that computes channel-wise, timestep-aware gating over the four condition streams, allowing the fusion strategy to vary with both feature subspace and noise level. To better capture speech-related facial dynamics, we design a Mouth-Augmented Shading Mesh, a 3DMM-based representation that decouples head motion, mouth motion, expression, and lighting. This design provides a temporally consistent geometric prior and allows flexible recombination of these attributes at inference. We further introduce a lip consistency loss to tighten audio-visual alignment. Extensive experiments show that MoCoTalk achieves state-of-the-art performance on the majority of structural, motion, and perceptual metrics, while offering attribute-level controllability that single-condition methods do not provide.
