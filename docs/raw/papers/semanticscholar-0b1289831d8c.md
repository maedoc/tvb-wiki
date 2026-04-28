# Topology-Aware Deep Reinforcement Learning for Renewable Dispatch: A Case Study on the Peshawar Grid

**Source**: semantic-scholar
**ID**: 0b1289831d8ccf5d8efd1621ba20f90d694b68ea
**DOI**: 10.1109/HONET67928.2025.11318493
**URL**: https://www.semanticscholar.org/paper/0b1289831d8ccf5d8efd1621ba20f90d694b68ea
**Date**: 2025-12-02
**Year**: 2025
**Authors**: Muhammad Arslan Khurshid, Gull Muhammad Khan
**Venue**: International Symposium on High-capacity Optical Networks and Enabling Technologies
**Citations**: 0

## Abstract

The transition toward renewable-dominant power systems introduces significant challenges in real-time dispatch, topology-aware control, and operational stability. While Deep Reinforcement Learning (DRL) enables adaptive decision-making, its conventional formulations often disregard power grid topology, limiting physical feasibility. This paper presents a novel Hybrid Deep Graph Processing (HDGP) framework that integrates Graph Neural Networks (GNNs) with Proximal Policy Optimization (PPO) for topology-informed solar dispatch in utility-scale networks.HDGP jointly learns structural encodings and control policies through a closed-loop interaction with the Python for Power System Analysis (PyPSA) simulator, enabling real-time decisions that respect operational constraints. Unlike prior DRL or GNN-based models that treat grid dynamics in isolation, HDGP employs a graph-in-the-loop architecture to enhance convergence stability, voltage regulation, and constraint adherence.We evaluate the framework on the 132 kV Peshawar Grid Station in Pakistan, characterized by high solar intermittency and aging infrastructure. The results demonstrate 100 percent satisfaction of operational constraints—including voltage limits and line flow thresholds—and full daytime PV utilization. When benchmarked against Optimal Power Flow (OPF), the HDGP controller achieves a mean absolute error of 0.0210 MW, with a mean relative error of 0.39 percent, confirming its ability to approximate OPF-level performance in real-time.Additionally, HDGP achieves a 14 percent reduction in greenhouse gas emissions compared to conventional dispatch strategies. These results validate HDGP as a scalable and reliable approach for clean energy integration in real-world, resource-constrained grids, contributing toward the realization of UN Sustainable Development Goal 7.
