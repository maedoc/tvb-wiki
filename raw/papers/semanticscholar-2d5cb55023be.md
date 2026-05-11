# A 40nm 0.05-1.4uJ/inference Sample-Wise-Adaptive Spiking Neural Network Processor with Dynamic Neuron-Pruning and Unstructured-Model-Aware Architecture

**Source**: semantic-scholar
**ID**: 2d5cb55023bee7982d12740c9a841b4ba182a7c5
**DOI**: 10.1109/CICC63670.2025.10983259
**URL**: https://www.semanticscholar.org/paper/2d5cb55023bee7982d12740c9a841b4ba182a7c5
**Date**: 2025-04-13
**Year**: 2025
**Authors**: Jinqiao Yang, Zikai Zhu, Longrun Xv, Anqin Xiao, Ziyi Yang, Lirong Zhenq, Zhuo Zou
**Venue**: IEEE Custom Integrated Circuits Conference
**Citations**: 1

## Abstract

The human brain exemplifies a highly adaptive system capable of dynamically recruiting neural resources in response to varying cognitive demands [1]. It recruits a complex network with a large pool of neurons for hard samples, while it recruits a simpler network with fewer neurons for easy samples, achieving sample-wise adaptation, as shown in Fig. 1 (top left). Therefore, it can achieve optimal energy efficiency and processing latency. Recent advances in neuromorphic processors for loT exploit the event-driven feature and temporal-spatial sparsity of Spiking Neural Network (SNN), leading to promising energy efficiency, while achieving task-agnostic processing [2]–[5]. However, these works predominantly focus on task-level adaptation, overlooking the aforementioned capability of the brain for fine-grained sample-wise adaptation, which incurs substantial redundancy in computations, drastically compromising the energy efficiency, especially for frequent presences of easy samples (Fig. 1 (top right)). To deal with this issue, this paper presents a sample-wise adaptive SNN processor with dynamic neuron-pruning to reconstruct an optimized, sample-specific SNN, achieving ultra-low energy consumption and latency. Figure 1 (bottom) illustrates 3 main features of our work: (1) A dynamic pruning scheme utilizing a tiny Perception Network (PN) that identifies inference-relevant (IR) neurons and prunes inference-irrelevant ones In the Inference Network (IN) for each sample to minimize computational costs. (2) An efficient unstructured-model-aware architecture parallelly scheduling active weights for IR neurons into a pipeline-event coupled processing strategy to optimize throughput and energy efficiency. (3) A hierarchical workload monitor, structured across synapse, neuron, and layer levels, enables workload-aware clock gating to mitigate the energy overhead resulting from sample-variant workload imbalances.
