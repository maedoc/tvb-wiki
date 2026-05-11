# Research on Modeling and Optimization Algorithm of Soft Robot Perceptual Control System Based on Octopus Neural Structure Simulation

**Source**: semantic-scholar
**ID**: 4308c593f07430b1d0868a7edc65e30f0c85c297
**DOI**: 10.1109/AECSPE66597.2025.00140
**URL**: https://www.semanticscholar.org/paper/4308c593f07430b1d0868a7edc65e30f0c85c297
**Date**: 2025-09-04
**Year**: 2025
**Authors**: Bin Zhao
**Venue**: 2025 Asia Conference on Energy Conversion Systems and Power Electronics (AECSPE)
**Citations**: 0

## Abstract

Based on octopus distributed nervous system and multi-modal sensing mechanism, this paper constructs a hierarchical soft robot sensing control system, and designs a collaborative optimization algorithm to improve its control performance and environmental adaptability. In the aspect of system modeling, the bionic architecture of "central layer-local ganglion-executive layer" is adopted: the central layer (CNS) processes environmental information and task objectives through the LSTM network to generate global posture instructions; Local ganglion (STS) fuses tactile pressure matrix and chemical sensor array data based on Bayesian filter, and outputs local compensation instruction in real time. The final control signal is formed after weighted fusion and dead-time function processing. Kinematic modeling adopts the assumption of segmented constant curvature to describe the bending behavior of flexible segments, and introduces NARX (Nonlinear Autoregressive with eXogenous inputs) neural network to compensate for deformation errors caused by driving line tension, achieving high-dimensional dynamic mapping. In terms of optimization algorithms, a hybrid strategy combining genetic algorithm (GA) and proximal policy optimization (PPO) with reinforcement learning (RL) is proposed: GA offline optimizes the core parameters of the controller to provide the initial strategy, PPO online dynamically adjusts to cope with unknown disturbances, and achieves comprehensive performance optimization through a multi-objective cost function (minimizing trajectory tracking error, energy consumption, and collision risk). Experimental verification shows that the system performs excellently in static object grasping (geometric shape recognition rate of 95.7%, surface material recognition rate of 91.3%), S-shaped trajectory tracking (RMSE as low as 2.05 mm at curvature 1.0 cm–1, an improvement of 48.4% compared to RL control), and chemical leakage response (NH3 detection accuracy of 97.1%, delay of 62 ± 8 ms), and maintains a grasping success rate of over 92% in scenarios such as sensor failure and external force interference, significantly better than traditional PID control. It provides an effective solution for high-precision and robust control of soft robots in complex environments.
