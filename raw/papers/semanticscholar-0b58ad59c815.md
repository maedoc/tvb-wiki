# MPTorch-FPGA: A Custom Mixed-Precision Framework for FPGA-Based DNN Training

**Source**: semantic-scholar
**ID**: 0b58ad59c815dfdace0d93b101f5c40bc92278ff
**DOI**: 10.23919/DATE64628.2025.10993010
**URL**: https://www.semanticscholar.org/paper/0b58ad59c815dfdace0d93b101f5c40bc92278ff
**Date**: 2025-03-31
**Year**: 2025
**Authors**: Sami Ben Ali, Silviu-Ioan Filip, Olivier Sentieys, Guy Lemieux
**Venue**: Design, Automation and Test in Europe
**Citations**: 1

## Abstract

Training Deep Neural Networks (DNNs) is computationally demanding, leading to a growing interest in reduced precision formats to enhance hardware efficiency. Several frame-works explore custom number formats with parameterizable precision through software emulation on CPUs or GPUs. However, they lack comprehensive support for different rounding modes and struggle to accurately evaluate the impact of custom precision for FPGA-based targets. This paper introduces MPTorch-FPGA, an extension of the MPTorch framework for performing custom, multi-precision inference and training computations in CPU, GPU, and FPGA environments in PyTorch. MPTorch-FPGA can generate a model-specific accelerator for DNN training, with customizable sizes and arithmetic implementations, providing bit-level accuracy with respect to emulated low precision DNN training on GPUs or CPUs. An offline matching algorithm selects one of several pre-generated (static) FPGA configurations using a custom performance model to estimate latency. To showcase the versatility of MPTorch-FPGA, we present a series of training benchmarks using diverse DNN models, exploring a range of number format configurations and rounding modes. We report both accuracy and hardware performance metrics, verifying the precision of our performance model by comparing estimated and measured latencies across multiple benchmarks. These results highlight the flexibility and practical value of our framework.
