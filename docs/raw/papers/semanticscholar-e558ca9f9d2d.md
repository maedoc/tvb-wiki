# A Scalable Data-Driven Surrogate Model for 3D Dynamic Wind Farm Wake Prediction Using Physics-Inspired Neural Networks and Wind Box Decomposition

**Source**: semantic-scholar
**ID**: e558ca9f9d2de0343a6b1444bb89ced5f7ae285c
**DOI**: 10.3390/en18133356
**URL**: https://www.semanticscholar.org/paper/e558ca9f9d2de0343a6b1444bb89ced5f7ae285c
**Date**: 2025-06-26
**Year**: 2025
**Authors**: Qiuyu Lu, Yuqi Cao, Pingping Xie, Ying Chen, Yingming Lin
**Venue**: Energies
**Citations**: 3

## Abstract

Wake effects significantly reduce efficiency and increase structural loads in wind farms. Therefore, accurate and computationally efficient models are crucial for wind farm layout optimization and operational control. High-fidelity computational fluid dynamics (CFD) simulations, while accurate, are too slow for these tasks, whereas faster analytical models often lack dynamic fidelity and 3D detail, particularly under complex conditions. Existing data-driven surrogate models based on neural networks often struggle with the high dimensionality of the flow field and scalability to large wind farms. This paper proposes a novel data-driven surrogate modeling framework to bridge this gap, leveraging Neural Networks (NNs) trained on data from the high-fidelity SOWFA (simulator for wind farm applications) tool. A physics-inspired NN architecture featuring an autoencoder for spatial feature extraction and latent space dynamics for temporal evolution is introduced, motivated by the time–space decoupling structure observed in the Navier–Stokes equations. To address scalability for large wind farms, a “wind box” decomposition strategy is employed. This involves training separate NN models on smaller, canonical domains (with and without turbines) that can be stitched together to represent larger farm layouts, significantly reducing training data requirements compared to monolithic farm simulations. The development of a batch simulation interface for SOWFA to generate the required training data efficiently is detailed. Results demonstrate that the proposed surrogate model accurately predicts the 3D dynamic wake evolution for single-turbine and multi-turbine configurations. Specifically, average velocity errors (quantified as RMSE) are typically below 0.2 m/s (relative error < 2–5%) compared to SOWFA, while achieving computational accelerations of several orders of magnitude (simulation times reduced from hours to seconds). This work presents a promising pathway towards enabling advanced, model-based optimization and control of large wind farms.
