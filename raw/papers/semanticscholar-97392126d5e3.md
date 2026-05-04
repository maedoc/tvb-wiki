# Cooperative Control of Vehicle Platoons with Unknown Dynamics using Neural Network-Enhanced Reinforcement Learning

**Source**: semantic-scholar
**ID**: 97392126d5e3b9bcaba85b5d801fa0a8b79ced13
**DOI**: 10.1109/ICM62621.2025.10934885
**URL**: https://www.semanticscholar.org/paper/97392126d5e3b9bcaba85b5d801fa0a8b79ced13
**Date**: 2025-02-28
**Year**: 2025
**Authors**: Elham Yazdani Bejarbaneh, Haiping Du
**Venue**: International Congress of Mathematicans
**Citations**: 0

## Abstract

This study proposes an optimal cooperative control framework for heterogeneous vehicle platoons using a neural network (NN)-based reinforcement learning (RL) algorithm in an identifier-critic-actor framework. Typically, determining the optimal control policy requires solving the Hamilton-Jacobi-Bellman (HJB) equation, but the presence of nonlinear terms within the HJB equation makes deriving analytical solutions challenging. While RL algorithms can overcome this issue, existing NN-based RL approaches are inherently complex as their update rules are derived from gradient descent optimization of the squared approximation of the HJB equation. This complexity makes their implementation challenging for nonlinear multi-vehicle systems with unknown dynamics. The proposed control strategy for platooning leverages an NN-based RL algorithm, where the update rules are directly derived from the negative gradient of a positive function that is mathematically equivalent to the HJB equation. Additionally, an NN-based identifier is incorporated into the platooning control design to dynamically estimate unknown vehicle dynamics in real time. The methodology is experimentally validated using the high-fidelity Mixed Traffic Simulator (MiTaS) co-simulation platform, which combines the Simulation of Urban Mobility (SUMO) microscopic traffic simulator with MATLAB environment. Simulations results demonstrate the efficacy of the learned strategy in achieving optimal leader-tracking performance.
