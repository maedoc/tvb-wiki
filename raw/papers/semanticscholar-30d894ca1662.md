# PyTorchSim: A Comprehensive, Fast, and Accurate NPU Simulation Framework

**Source**: semantic-scholar
**ID**: 30d894ca16621eae26216ccb9f915ec14c6dcd5f
**DOI**: 10.1145/3725843.3756045
**URL**: https://www.semanticscholar.org/paper/30d894ca16621eae26216ccb9f915ec14c6dcd5f
**Date**: 2025-10-18
**Year**: 2025
**Authors**: Wonhyuk Yang, Yunseon Shin, Okkyun Woo, Geonwoo Park, Hyungkyu Ham, Jeehoon Kang, Jongse Park, G. Kim
**Venue**: Micro
**Citations**: 4

## Abstract

Deep Neural Networks (DNNs) have continuously increasing demands for the performance and efficiency of Neural Processing Units (NPUs). While analytical models enable rapid exploration of high-level aspects (e.g., tiling), later stages of NPU design require a cycle-accurate simulator that supports various scenarios. However, existing NPU simulators are limited in several aspects, including support for high-speed, multi-core, multi-model tenancy, generic ISA (with vector operations), compiler, data-dependent timing model, and enabling both inference and training. To address these challenges, we propose PyTorchSim,1 a novel NPU simulation framework integrated with PyTorch 2. PyTorchSim models NPUs with a custom RISC-V-based ISA extended to support various acceleration units (e.g., systolic array). Our custom backend for PyTorch 2 compiles a given DNN using this ISA through lowering passes with MLIR and LLVM. Then, our extended Gem5 and Spike simulators execute the machine code to accurately model the DNN’s timing and functional aspects on the NPU. However, as such a conventional Instruction-Level Simulation (ILS) inevitably runs slowly, we propose Tile-Level Simulation (TLS) to improve speed without sacrificing accuracy. It uses tile-granularity operation latencies from offline ILS runs for high speed while still modeling DRAM and interconnect with cycle-accurate simulators. Furthermore, TLS can also be employed for sparse tensor operations using auxiliary per-tile latency obtained offline. As a result, PyTorchSim provides speedups of up to 139 × compared to Accel-Sim, while achieving high simulation accuracy against Google TPUv3 with an MAE of 11.5%. Additionally, we also demonstrate the effectiveness of PyTorchSim over existing simulators for different scenarios, including heterogeneous dense-sparse NPU, multi-model tenancy, compiler optimization, chiplet-aware NPU scheduling, and impact of DNN training hyperparameter.
