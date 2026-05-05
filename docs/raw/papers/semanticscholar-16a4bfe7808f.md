# Iterative Optimization of GraphSAGE for Knowledge Graph Assembly: A Dynamic Indexing and GPU Acceleration Approach

**Source**: semantic-scholar
**ID**: 16a4bfe7808f137900a635b404bf91d0be78802d
**DOI**: 10.31449/inf.v49i20.10433
**URL**: https://www.semanticscholar.org/paper/16a4bfe7808f137900a635b404bf91d0be78802d
**Date**: 2025-12-14
**Year**: 2025
**Authors**: Jinghua Wang, Zheng Zhu, Zihan Xu, Yue Wang, Yinxiao Kong
**Venue**: Informatica
**Citations**: 0

## Abstract

In large-scale knowledge graph data assembly, the traditional GraphSAGE model faces bottlenecks such as low neighborhood sampling efficiency, insufficient negative sample mining, and low computing resource utilization. Targeted optimization methods are urgently needed to improve data processing performance and embedding quality. As a mainstream graph neural network framework, GraphSAGE shows strong scalability and adaptability in graph structure representation learning. When its original implementation faces large-scale knowledge graph data assembly tasks, there are problems such as low neighborhood sampling efficiency, insufficient GPU resource utilization, and weak model training stability. Several key technology optimization methods are proposed, including multi-level neighborhood-aware sampling based on dynamic hybrid indexing, Hard Negative sample online mining strategy based on GPU acceleration, deep binding of non-blocking asynchronous I/O and GPU pipeline, and distributed node partitioning and multi-GPU work stealing load balancing model. Deep binding of asynchronous I/O and GPU pipelines, reducing data loading latency by 47%; Distributed node partitioning with multi-GPU work-stealing, boosting GPU utilization by 15 percentage points. Experiments on standard datasets show the optimized toolchain shortens assembly time from 34.7s to 9.2s, increases throughput by 63.9%, and improves inference accuracy by 89% compared to baseline.
