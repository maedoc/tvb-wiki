# NeuroRing: Scaling Spiking Neural Networks via Multi-FPGA Bidirectional Ring Topologies and Stream-Dataflow Architectures

**Source**: semantic-scholar
**ID**: 86a2739d89da8cd2adacae2c9f4becb3707472f9
**URL**: https://www.semanticscholar.org/paper/86a2739d89da8cd2adacae2c9f4becb3707472f9
**Date**: 2026-04-30
**Year**: 2026
**Authors**: Muhammad Ihsan Al Hafiz, Artur Podobas
**Citations**: 0

## Abstract

Spiking neural networks (SNNs) are a promising paradigm for energy-efficient event-driven computation, but large-scale SNN execution remains challenging because sparse spike communication and synchronization can dominate runtime. Existing solutions across CPU, GPU, ASIC, and FPGA platforms offer different trade-offs between programmability, efficiency, and scalability. To address this gap, we present NeuroRing, a modular and scalable SNN accelerator based on a stream-dataflow architecture and a bidirectional ring topology, implemented in High-Level Synthesis (HLS) on programmable FPGAs. NeuroRing supports modular single- and multi-FPGA deployment and is compatible with existing SNN workflows through integration with the NEST simulator. We evaluate NeuroRing on the cortical microcircuit benchmark and a Sudoku constraint-satisfaction workload. Results show that NeuroRing preserves the key activity statistics of the NEST reference model, achieves faster-than-real-time execution of the full-scale cortical microcircuit with a real-time factor (RTF) of 0.83, exhibits meaningful strong and weak scaling, and provides competitive energy efficiency on two programmable FPGAs. These results position NeuroRing as a flexible and scalable platform for both neuroscience simulation and broader event-driven applications.
