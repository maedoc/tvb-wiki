# EventQueues: Autodifferentiable spike event queues for brain simulation on AI accelerators

**Source**: semantic-scholar
**ID**: 9ebb73acdfc89e63a4628e1eeac246f5aabc24eb
**DOI**: 10.48550/arXiv.2512.05906
**URL**: https://www.semanticscholar.org/paper/9ebb73acdfc89e63a4628e1eeac246f5aabc24eb
**Date**: 2025-12-05
**Year**: 2025
**Authors**: Lennart P. L. Landsmeer, Amirreza Movahedin, S. Hamdioui, Christos Strydis
**Venue**: arXiv.org
**Citations**: 2

## Abstract

Spiking neural networks (SNNs), central to computational neuroscience and neuromorphic machine learning (ML), require efficient simulation and gradient-based training. While AI accelerators offer promising speedups, gradient-based SNNs typically implement sparse spike events using dense, memory-heavy data-structures. Existing exact gradient methods lack generality, and current simulators often omit or inefficiently handle delayed spikes. We address this by deriving gradient computation through spike event queues, including delays, and implementing memory-efficient, gradient-enabled event queue structures. These are benchmarked across CPU, GPU, TPU, and LPU platforms. We find that queue design strongly shapes performance. CPUs, as expected, perform well with traditional tree-based or FIFO implementations, while GPUs excel with ring buffers for smaller simulations, yet under higher memory pressure prefer more sparse data-structures. TPUs seem to favor an implementation based on sorting intrinsics. Selective spike dropping provides a simple performance-accuracy trade-off, which could be enhanced by future autograd frameworks adapting diverging primal/tangent data-structures.
