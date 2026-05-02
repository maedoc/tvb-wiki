---
title: NeuSIGHT
created: 2024-01-15
updated: 2026-05-03
type: entity
tags: [software-tvb, gpu-performance, deep-learning, machine-learning, ml-for-systems, performance-modeling, performance-prediction, training-optimization, inference-optimization]
sources:
  - https://dl.acm.org/doi/10.1145/3669940.3707265
  - https://github.com/sitar-lab/NeuSight
  - https://arxiv.org/abs/2407.13853
---

## Overview

NeuSIGHT (Neural Unified System for GPU Performance Forecasting) is an open-source framework designed to predict the performance of deep learning training and inference workloads on various graphics processing units (GPUs) without requiring actual execution on the target hardware [#lee2025forecasting]. Developed by researchers at Georgia Institute of Technology and Meta, NeuSIGHT was introduced in 2025 as a solution to the growing challenge of estimating deep learning model performance across rapidly evolving model architectures and GPU hardware generations. The framework addresses a critical pain point in machine learning systems: the inability to benchmark new models on unavailable or prohibitively expensive GPUs, such as the NVIDIA H100 which experienced lead times of up to 52 weeks [#forbes2024].

## Motivation

The deep learning community faces a perpetual challenge: new model architectures emerge continuously, but access to the latest GPU hardware remains constrained by long procurement lead times and high costs [#forbes2024]. This creates significant uncertainty about whether a given model architecture can meet performance requirements on available or upcoming hardware. Traditional approaches to performance prediction—cycle-accurate GPU simulators—require extensive modeling effort for each new GPU architecture and can take hours to simulate even relatively small models like ResNet-50 [#li2023path].

Prior works in GPU performance prediction suffered from high error rates when forecasting performance on unseen models and new GPUs [#yu2021habitat]. Methods like Habitat, which uses multi-layer perceptrons to predict kernel latency directly, showed percentage errors exceeding 120% on out-of-distribution hardware like the NVIDIA A100. Similarly, linear regression-based approaches [#li2023path] failed to capture the non-linear relationship between kernel characteristics and actual GPU performance, particularly for small matrix dimensions where GPU utilization remains low.

## Technical Approach

NeuSIGHT introduces a novel decomposition approach that breaks the complex problem of latency prediction into smaller, more manageable sub-problems. Rather than predicting the latency of an entire deep learning kernel directly using machine learning, NeuSIGHT exploits the tile-based execution strategy employed by modern GPU libraries.

### Tiled Execution Model

Modern GPU libraries for deep learning, such as cuDNN and CUTLASS, execute General Matrix Multiplication (GEMM) operations by partitioning output matrices into smaller working sets called tiles. Each tile represents a segment of the output matrix, loads the corresponding input operands, and computes the associated output elements. These tiles are then dispatched to individual Streaming Multiprocessors (SMs) on the GPU and executed concurrently. The number of tiles that can execute concurrently is limited by the number of SMs, and the entire kernel executes in multiple waves of tile groups.

This tiling strategy enables scalable execution of matrix operations by decomposing them into multiple smaller, independent workloads. NeuSIGHT leverages this observation to make predictions at tile granularity, where the problem is more tractable for machine learning models to solve accurately.

### Performance Bounding with Fundamental Laws

NeuSIGHT constrains its predictions using fundamental GPU performance laws, most notably the Roofline model [#williams2009roofline]. The Roofline bandwidth represents the maximum achievable throughput of a kernel on a GPU, computed as the minimum of the kernel's arithmetic intensity multiplied by peak memory bandwidth and the GPU's peak FLOPs. This provides a physical lower bound on tile latency that cannot be exceeded.

The framework employs multi-layer perceptrons (MLPs) to predict the utilization coefficient for each kernel type. Specifically, NeuSIGHT uses five specialized MLPs tailored for different operator categories: batched matrix multiplication, fully-connected layers, element-wise operators, softmax, and layer normalization. Each MLP has 8 fully connected layers with 512 hidden units and uses ReLU activations. The input features include GPU hardware specifications normalized per SM, such as memory size, bandwidth, peak FLOPs, and L2 cache size, expressed as resource utilization ratios.

### Distributed Execution Support

Beyond single-GPU prediction, NeuSIGHT extends its forecasting to distributed training scenarios across multiple GPUs within a server. The framework augments the deep learning computation graph with communication operators based on the specified parallelism strategy: pipeline parallelism, tensor parallelism, or data parallelism. For pipeline parallelism, NeuSIGHT estimates bubble overheads based on microbatch size and send/receive operation latency. For tensor model and data parallelism, it inserts all-reduce operators to synchronize activations or gradients across GPUs, combining communication and compute latencies to forecast end-to-end performance.

## Key Results

NeuSIGHT demonstrates significantly improved prediction accuracy compared to prior approaches. Across diverse GPUs (NVIDIA P4, P100, V100, T4, A100, L4, H100, and AMD MI100, MI210, MI250) and deep learning workloads (BERT, GPT-2, GPT-3, OPT, Switch Transformer), NeuSIGHT achieves a mean absolute percentage error of 8.9% for inference and 7.3% for training, compared to 140% for the MLP-based Habitat approach and 60.8% for linear regression-based methods.

Particularly notable is NeuSIGHT's performance on out-of-distribution hardware. When predicting latency on the NVIDIA H100—a GPU not included in the training set—the framework achieves a prediction error of just 2.3% for GPT-3 training and inference, compared to 121.4% and 30.8% respectively for prior state-of-the-art methods.

## Implementation

NeuSIGHT is implemented in Python and integrates with PyTorch for model graph extraction using the Torch.fx library. The framework requires two input files: a device configuration file specifying GPU architectural parameters (memory size, memory bandwidth, number of SMs, cores per SM, compute frequency, peak FLOPs, and L2 cache size), and a deep learning model configuration file describing the model architecture in Hugging Face format.

The software includes pre-trained MLP predictors for common operator types and provides scripts for both prediction and retraining with custom datasets. Installation is available via pip from the GitHub repository, with tested support for Python 3.9 and PyTorch 2.1.0.

## Relationship to TVB

While NeuSIGHT bears no direct relationship to The Virtual Brain, it represents a complementary category of computational neuroscience infrastructure tools: both address challenges in model validation when empirical measurement is impractical. TVB enables simulation of brain dynamics when direct neural measurement is infeasible, while NeuSIGHT enables performance forecasting when hardware execution is impractical. Users building computational pipelines that involve both brain simulation and machine learning inference may find NeuSIGHT valuable for resource planning in hybrid workflows.

## Related Software

NeuSIGHT operates within the machine learning systems ecosystem and relates to several established tools. For deep learning framework compilation and optimization, it can be used alongside TVM and PyTorch. For performance modeling and simulation, it complements analytical tools like Roofline analysis utilities and cycle-accurate GPU simulators such as Accel-Sim. The framework's prediction workflow integrates with profiling tools including PyTorch Profiler for extracting kernel metadata and nvprof for performance analysis. Additionally, NeuSIGHT's distributed training predictions can be combined with network simulation tools like ASTRA-Sim for multi-node forecasting.

## References

1. Lee, S., Phanishayee, A., & Mahajan, D. (2025). Forecasting GPU Performance for Deep Learning Training and Inference. *Proceedings of the 30th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS '25)*, 493-508. https://doi.org/10.1145/3669940.3707265

2. NeuSight GitHub Repository. (2024). SCAI-Tech/NeuSight. https://github.com/sitar-lab/NeuSight

3. Williams, S., Waterman, A., & Patterson, D. (2009). Roofline: An insightful visual performance model for multicore architectures. *Communications of the ACM*, 52(4), 65-76.

4. Yu, G. X., Gao, Y., Golikov, P., & Pekhimenko, G. (2021). Habitat: A Runtime-Based Computational Performance Predictor for Deep Neural Network Training. *USENIX Annual Technical Conference (ATC '21)*.

5. Li, Y., Sun, Y., & Jog, A. (2023). Path Forward Beyond Simulators: Fast and Accurate GPU Execution Time Prediction for DNN Workloads. *International Symposium on Microarchitecture (MICRO '23)*.

[#lee2025forecasting]: https://dl.acm.org/doi/10.1145/3669940.3707265
[#forbes2024]: https://www.forbes.com/sites/jasonblewis/2024/02/05/nvidia-face-52-week-lead-time-for-h100-gpus-as-demand-skyrockets/
[#li2023path]: https://doi.org/10.1145/3617238.3620129
[#yu2021habitat]: https://www.usenix.org/system/files/atc21_yu.pdf
[#williams2009roofline]: https://doi.org/10.1145/1498765.1498785