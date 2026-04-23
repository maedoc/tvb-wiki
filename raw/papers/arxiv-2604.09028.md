# Plasticity-Enhanced Multi-Agent Mixture of Experts for Dynamic Objective Adaptation in UAVs-Assisted Emergency Communication Networks

**Source**: arxiv
**ID**: 2604.09028
**URL**: https://arxiv.org/abs/2604.09028
**Date**: 2026-04-10
**Year**: 2026
**Authors**: Wen Qiu, Zhiqiang He, Wei Zhao, Hiroshi Masui
**Categories**: cs.MA, cs.LG, cs.NI

## Abstract

Unmanned aerial vehicles serving as aerial base stations can rapidly restore connectivity after disasters, yet abrupt changes in user mobility and traffic demands shift the quality of service trade-offs and induce strong non-stationarity. Deep reinforcement learning policies suffer from plasticity loss under such shifts, as representation collapse and neuron dormancy impair adaptation. We propose plasticity enhanced multi-agent mixture of experts (PE-MAMoE), a centralized training with decentralized execution framework built on multi-agent proximal policy optimization. PE-MAMoE equips each UAV with a sparsely gated mixture of experts actor whose router selects a single specialist per step. A non-parametric Phase Controller injects brief, expert-only stochastic perturbations after phase switches, resets the action log-standard-deviation, anneals entropy and learning rate, and schedules the router temperature, all to re-plasticize the policy without destabilizing safe behaviors. We derive a dynamic regret bound showing the tracking error scales with both environment variation and cumulative noise energy. In a phase-driven simulator with mobile users and 3GPP-style channels, PE-MAMoE improves normalized interquartile mean return by 26.3\% over the best baseline, increases served-user capacity by 12.8\%, and reduces collisions by approximately 75\%. Diagnostics confirm persistently higher expert feature rank and periodic dormant-neuron recovery at regime switches.
