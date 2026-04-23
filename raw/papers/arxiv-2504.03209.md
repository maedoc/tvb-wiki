# PIONM: A Generalized Approach to Solving Density-Constrained Mean-Field Games Equilibrium under Modified Boundary Conditions

**Source**: semantic-scholar
**ID**: 720e2a5a583b08c3e7370081b54d265dc4b8da5a
**DOI**: 10.1109/IJCNN64981.2025.11227714
**URL**: https://www.semanticscholar.org/paper/720e2a5a583b08c3e7370081b54d265dc4b8da5a
**Date**: 2025-04-04
**Year**: 2025
**Authors**: Jinwei Liu, Wang Yao, Xiao Zhang
**Venue**: IEEE International Joint Conference on Neural Network
**Citations**: 0

## Abstract

Neural network-based methods are effective for solving equilibria in Mean-Field Games (MFGs), particularly in high-dimensional settings. However, solving the coupled partial differential equations (PDEs) in MFGs limits their applicability since solving coupled PDEs is computationally expensive. Additionally, modifying boundary conditions, such as the initial state distribution or terminal value function, necessitates extensive retraining, reducing scalability. To address these challenges, we propose a generalized framework, PIONM (Physics-Informed Neural Operator NF-MKV Net), which leverages physics-informed neural operators to solve MFGs equations. PIONM utilizes neural operators to compute MFGs equilibria for arbitrary boundary conditions. The method encodes boundary conditions as input features and trains the model to align them with density evolution, modeled using discrete-time normalizing flows. Once trained, the algorithm efficiently computes the density distribution at any time step for modified boundary condition, ensuring efficient adaptation to different boundary conditions in MFGs equilibria. Unlike traditional MFGs methods constrained by fixed coefficients, PIONM efficiently computes equilibria under varying boundary conditions, including obstacles, diffusion coefficients, initial densities, and terminal functions. PIONM can adapt to modified conditions while preserving density distribution constraints, demonstrating superior scalability and generalization capabilities compared to existing methods.
