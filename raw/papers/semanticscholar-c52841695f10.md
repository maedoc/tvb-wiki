# MINDEV: Multi-modal Integrated Diffusion Framework for Video Reconstruction from EEG Signals

**Source**: semantic-scholar
**ID**: c52841695f1020e46b70a3baac4a856fce22a353
**DOI**: 10.1145/3746027.3755054
**URL**: https://www.semanticscholar.org/paper/c52841695f1020e46b70a3baac4a856fce22a353
**Date**: 2025-10-27
**Year**: 2025
**Authors**: Shuai Huang, Yongxionga Wang, Huan Luo, Haodong Jing, Chendong Qin, Jingqun Tang
**Venue**: ACM Multimedia
**Citations**: 10

## Abstract

Despite recent progress in decoding static images from brain activity, reconstructing dynamic visual experiences from EEG signals remains challenging due to the complex temporal dynamics involved. Current approaches primarily rely on pre-trained video generation models while failing to fully leverage the rich temporal-spatial information embedded in EEG signals for video synthesis. This paper proposes MINDEV Multi-modal Integrated Neural DEcoding and Visualization), a framework that places EEG signal processing at the core of video reconstruction. We introduce three key technical contributions: (1) a dual-branch feature extractor that captures both temporal dynamics and spatial relationships in EEG signals, (2) an EEG-driven semantic bridge that uses neural patterns to guide language model interpretation, and (3) a multi-modal video synthesis pipeline where EEG features lead the generation process while semantic guidance provides refinement. Our framework prioritizes the millisecond-level temporal resolution of EEG signals, using them to drive both visual content generation and semantic understanding. Evaluated on the SEED-DV dataset, MINDEV demonstrates superior performance with a semantic classification accuracy of 93.2% and a structural similarity index (SSIM) of 0.4777, establishing a new state-of-the-art for EEG-based video reconstruction. Our code is publicly available at https://github.com/HHarr1son/MINDEV.
