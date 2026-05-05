# AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion

**Source**: arxiv
**ID**: 2605.02892
**URL**: https://arxiv.org/abs/2605.02892
**Date**: 2026-05-04
**Year**: 2026
**Authors**: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
**Categories**: cs.CV, cs.IR

## Abstract

Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
