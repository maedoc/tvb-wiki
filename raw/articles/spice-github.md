---
title: "Spice GitHub Repository"
created: 2026-05-19
updated: 2026-05-19
type: source
tags: [software-brain-modeling, spiking-neural-networks]
authors:
  - Dennis Bautembach
year: 2020
venue: GitHub
url: "https://github.com/denniskb/spice"
---

# Spice GitHub Repository

**Author**: Dennis Bautembach
**URL**: https://github.com/denniskb/spice
**License**: MIT

## Summary

Spice (/spaɪk/) is a multi-GPU, time-driven (clock-based), general-purpose spiking neural network simulator written in C++ with CUDA acceleration. It was originally developed by Dennis Bautembach during doctoral research at the University of Crete.

## Key Features

- State-of-the-art performance, including sub-second network setup times
- Multi-GPU support with linear scaling up to 8 GPUs
- Custom neuron and synapse models defined directly in native C++
- Modern, user-friendly API
- CPU, single-GPU, and multi-GPU backends (`cpu::snn`, `cuda::snn`, `cuda::multi_snn`)
- No third-party dependencies except CUDA

## Performance Benchmarks

Published benchmarks simulate 10 seconds of biological time. On a single GPU with 1 billion synapses, simulation completes in approximately 1.5 seconds wall-clock time, with setup times under 0.1 seconds.

## Publications

- "Even Faster SNN Simulation with Lazy+Event-driven Plasticity and Shared Atomics" (HPEC 2021)
- "Multi-GPU SNN Simulation with Perfect Static Load Balancing" (IJCNN 2021)
- "Faster and Simpler SNN Simulation with Work Queues" (IJCNN 2020)

## Related Entities

- [[Spice]]
- [[NEST]]
- [[Brian2]]
- [[Arbor]]
