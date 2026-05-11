# Industrial-Grade Sensor Simulation via Gaussian Splatting: A Modular Framework for Scalable Editing and Full-Stack Validation

**Source**: semantic-scholar
**ID**: 3e6ba77ee6a4453b98f7ce93ade1f2d3cbf9200f
**DOI**: 10.1109/IROS60139.2025.11246621
**URL**: https://www.semanticscholar.org/paper/3e6ba77ee6a4453b98f7ce93ade1f2d3cbf9200f
**Date**: 2025-03-14
**Year**: 2025
**Authors**: Xianming Zeng, Sicong Du, Qifeng Chen, Lizhe Liu, Hao Shu, Jiaxuan Gao, Jiarun Liu, Jiulong Xu, Jianyun Xu, Mingxia Chen, Yiru Zhao, Peng Chen, Y. Xue, Chunming Zhao, Sheng Yang, Qiang Li
**Venue**: IEEE/RJS International Conference on Intelligent RObots and Systems
**Citations**: 3

## Abstract

Sensor simulation is pivotal for scalable validation of autonomous driving systems, yet existing Neural Radiance Fields (NeRF) based methods face applicability and efficiency challenges in industrial workflows. This paper introduces a Gaussian Splatting (GS) based system to address these challenges: We first break down sensor simulator components and analyze the possible advantages of GS over NeRF. Then in practice, we refactor three crucial components through GS, to leverage its explicit scene representation and real-time rendering: (1) choosing the 2D neural Gaussian representation for physics-compliant scene and sensor modeling, (2) proposing a scene editing pipeline to leverage Gaussian primitives library for data augmentation, and (3) coupling a controllable diffusion model for scene expansion and harmonization. We implement this framework on a proprietary autonomous driving dataset supporting cameras and LiDAR sensors. We demonstrate through ablation studies that our approach reduces frame-wise simulation latency, achieves better geometric and photometric consistency, and enables interpretable explicit scene editing and expansion. Furthermore, we showcase how integrating such a GS-based sensor simulator with traffic and dynamic simulators enables full-stack testing of end-to-end autonomy algorithms. Our work provides both algorithmic insights and practical validation, establishing GS as a cornerstone for industrial-grade sensor simulation.
