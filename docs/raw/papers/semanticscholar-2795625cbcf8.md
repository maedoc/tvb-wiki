# Improving Data-Driven Inferential Sensor Modeling by Industrial Knowledge: A Bayesian Perspective

**Source**: semantic-scholar
**ID**: 2795625cbcf88edd86e2dc04afac4fef4c32e60f
**DOI**: 10.1109/TSMC.2024.3493071
**URL**: https://www.semanticscholar.org/paper/2795625cbcf88edd86e2dc04afac4fef4c32e60f
**Date**: 2025-02-01
**Year**: 2025
**Authors**: Zhichao Chen, Hao Wang, Zhihuan Song, Zhiqiang Ge
**Venue**: IEEE Transactions on Systems, Man, and Cybernetics: Systems
**Citations**: 11

## Abstract

Accurate quality variable inference by process variables is the core of industrial inferential sensor modeling, where recent advancements have seen deep learning (DL) models achieving remarkable success. However, integrating knowledge of unit operations is critical for improving inferential sensor performance, yet it has received little attention. The main challenge lies in the incompleteness and correctness of industrial knowledge due to its semi-empirical nature and inevitable engineering errors. Addressing this, this article introduces the gradient knowledge network based on the graph neural network’s message-passing mechanism within the variational Bayesian inference framework, which naturally copes with the abovementioned issues by fusing observational data. Initially, the prior knowledge about the process variables, which mirrors the graph in graph neural network, is parameterized as Dirichlet distribution based on the analysis of message-passing mechanism. However, the divergence computation and normalization constraints are challenging for model implementation. To navigate these challenges, the Bayesian inference problem is transformed into an optimization problem, subsequently recast as a simulation problem induced by the gradient field, ensuring compatibility with DL backends. Furthermore, a theoretical iteration equation is derived to maintain the normalization constraint. The architecture of the proposed model and its learning algorithm are then detailed. Finally, various experiments are conducted on two real industrial processes to demonstrate the model’s efficacy from the perspective of prediction accuracy, sensitivity analysis, and ablation study.
