# The Enduring Dominance of Deep Neural Networks: A Critical Analysis of the Fundamental Limitations of Quantum Machine Learning and Spiking Neural Networks

**Source**: semantic-scholar
**ID**: be9d135c0c4694bf16739253d475304039e7746f
**DOI**: 10.48550/arXiv.2510.08591
**URL**: https://www.semanticscholar.org/paper/be9d135c0c4694bf16739253d475304039e7746f
**Date**: 2025-10-04
**Year**: 2025
**Authors**: Takehiro Ishikawa
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Recent advancements in QML and SNNs have generated considerable excitement, promising exponential speedups and brain-like energy efficiency to revolutionize AI. However, this paper argues that they are unlikely to displace DNNs in the near term. QML struggles with adapting backpropagation due to unitary constraints, measurement-induced state collapse, barren plateaus, and high measurement overheads, exacerbated by the limitations of current noisy intermediate-scale quantum hardware, overfitting risks due to underdeveloped regularization techniques, and a fundamental misalignment with machine learning's generalization. SNNs face restricted representational bandwidth, struggling with long-range dependencies and semantic encoding in language tasks due to their discrete, spike-based processing. Furthermore, the goal of faithfully emulating the brain might impose inherent inefficiencies like cognitive biases, limited working memory, and slow learning speeds. Even their touted energy-efficient advantages are overstated; optimized DNNs with quantization can outperform SNNs in energy costs under realistic conditions. Finally, SNN training incurs high computational overhead from temporal unfolding. In contrast, DNNs leverage efficient backpropagation, robust regularization, and innovations in LRMs that shift scaling to inference-time compute, enabling self-improvement via RL and search algorithms like MCTS while mitigating data scarcity. This superiority is evidenced by recent models such as xAI's Grok-4 Heavy, which advances SOTA performance, and gpt-oss-120b, which surpasses or approaches the performance of leading industry models despite its modest 120-billion-parameter size deployable on a single 80GB GPU. Furthermore, specialized ASICs amplify these efficiency gains. Ultimately, QML and SNNs may serve niche hybrid roles, but DNNs remain the dominant, practical paradigm for AI advancement.
