# SpiNeRF: direct-trained spiking neural networks for efficient neural radiance field rendering

**Source**: semantic-scholar
**ID**: 05fde5c6d8e37b1a5ce1e4d60f0a52e59d896411
**DOI**: 10.3389/fnins.2025.1593580
**URL**: https://www.semanticscholar.org/paper/05fde5c6d8e37b1a5ce1e4d60f0a52e59d896411
**Date**: 2025-07-23
**Year**: 2025
**Authors**: Xingting Yao, Qinghao Hu, Fei Zhou, Tielong Liu, Zitao Mo, Zeyu Zhu, Zhengyang Zhuge, Jian Cheng
**Venue**: Frontiers in Neuroscience
**Citations**: 4

## Abstract

Spiking neural networks (SNNs) have recently demonstrated significant progress across various computational tasks, due to their potential for energy efficiency. Neural radiance fields (NeRFs) excel at rendering high-quality 3D scenes but require substantial energy consumption, with limited exploration of energy-saving solutions from a neuromorphic approach. In this paper, we present SpiNeRF, a novel method that integrates the sequential processing capabilities of SNNs with the ray-casting mechanism of NeRFs, aiming to enhance compatibility and unlock new prospects for energy-efficient 3D scene synthesis. Unlike conventional SNN encoding schemes, our method considers the spatial continuity inherent in NeRF, achieving superior rendering quality. To further improve training and inference efficiency, we adopt a hybrid volumetric representation that allows the predefinition and masking of invalid sampled points along pixel-rendering rays. However, this masking introduces irregular temporal lengths, making it intractable for hardware processors, such as graphics processing units (GPUs), to conduct effective parallel training. To address this issue, we present two methods: Temporal padding (TP) and temporal condensing-and-padding (TCP). Experiments on multiple datasets demonstrate that our method outperforms previous SNN encoding schemes and artificial neural network (ANN) quantization methods in both rendering quality and energy efficiency. Compared to the full-precision ANN baseline, our method reduces energy consumption by up to 72.95% while maintaining comparable synthesis quality. Further verification using a neuromorphic hardware simulator shows that TCP-based SpiNeRF achieves additional energy efficiency gains over the ANN-based approaches by leveraging the advantages of neuromorphic computing. Codes are in https://github.com/Ikarosy/SpikingNeRF-of-CASIA.
