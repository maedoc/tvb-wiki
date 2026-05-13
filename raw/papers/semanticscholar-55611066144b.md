# DFMG: Delay-Flush Multi-Group Algorithm for Spiking Neural Network Simulation

**Source**: semantic-scholar
**ID**: 55611066144b7794a6bbf5cb8eb10d1ae93f80e4
**DOI**: 10.1145/3730436.3730516
**URL**: https://www.semanticscholar.org/paper/55611066144b7794a6bbf5cb8eb10d1ae93f80e4
**Date**: 2025-02-14
**Year**: 2025
**Authors**: Hong Liang, Zhiguang Chen, Yangle Zeng, Guangnan Feng, Yutong Lu
**Venue**: Proceedings of the 2025 International Conference on Artificial Intelligence and Computational Intelligence
**Citations**: 0

## Abstract

Spiking Neural Network (SNN) has been known as an effective tool for advancing comprehension of the brain. Recent efforts aim to simulate human-scale SNNs, encompassing 86 billion neurons and hundreds of trillion synapses. However, network communication emerges as a bottleneck in SNN simulation. In this paper, we propose DFMG, a Delay-Flush Multi-Group algorithm which utilizes the synaptic delay in multi-area models to alleviate the communication bottleneck. Firstly, DFMG adopts a delay-flush communication pattern to reduce the network packet counts. Then, DFMG utilizes several smaller communication groups instead of a large one to improve communication locality. DFMG also includes a hierarchical clustering algorithm and a greedy patching algorithm which partition the groups. We evaluate the performance with a model of 116 areas using 232 compute nodes on the Tianhe-Xingyi Supercomputing System. The results show that our DFMG improves communication performance and achieves up to 26% speedup.
