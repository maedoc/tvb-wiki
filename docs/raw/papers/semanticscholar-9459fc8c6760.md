# A Hybrid Stochastic-Binary Computing Batch Normalization Engine for Low-Power On-Chip Learning Spiking Neural Networks

**Source**: semantic-scholar
**ID**: 9459fc8c6760beff5c7aef90c6450e30567a7315
**DOI**: 10.1109/TVLSI.2025.3602991
**URL**: https://www.semanticscholar.org/paper/9459fc8c6760beff5c7aef90c6450e30567a7315
**Date**: 2025-12-01
**Year**: 2025
**Authors**: Wei Liu, Yue Liu, Zhiyi Yu, Shanlin Xiao
**Venue**: IEEE Transactions on Very Large Scale Integration (VLSI) Systems
**Citations**: 0

## Abstract

Batch normalization (BN) has proven to be a critical component in speeding up the training of deep spiking neural networks in deep learning. However, conventional BN implementations face significant challenges in terms of excessive off-chip memory bandwidth requirements and complex circuit designs, hindering their applicability for on-chip training in spiking neural networks (SNNs). This article introduces a novel hybrid stochastic-binary computing BN engine (HBN) that strikes an optimal balance between computational efficiency and hardware resource utilization, enabling efficient on-chip learning for SNNs. While conventional binary-mode BN engines offer temporal efficiency, they demand substantial hardware resources. In contrast, stochastic computing (SC)-based BN approaches reduce hardware overhead but introduce latency penalties and necessitate additional random number generation (RNG) circuits. To overcome these limitations, we propose a hybrid architecture that seamlessly integrates binary and stochastic computing (SC) paradigms. Our co-designed methodology effectively balances computational latency and hardware footprint. This is achieved by a rounding-free SC multiplier unified with binary-circuit map ping, which eliminates latency and RNG overheads. Extensive validation across both static image datasets and neuromorphic datasets demonstrates that HBN maintains algorithmic fidelity while achieving unprecedented computational efficiency. Simulation results reveal 98.7% reduction in floating-point operations (FLOPs), 98.5% latency improvement, and 98.2% energy consumption reduction compared with conventional BN implementations. FPGA implementation on the ZCU102 platform demonstrates practical hardware advantages, including 74.9% reduction in look-up table (LUT) utilization, 83.6% decrease in flip-flop (FF) count, and 13.7% reduction in block RAM (BRAM) allocation. Notably, the design achieves 63.7% power reduction compared with state-of-the-art implementations while maintaining complete DSP-free operation.
