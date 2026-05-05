# HeartSimSage: Attention-Enhanced Graph Neural Networks for Accelerating Cardiac Mechanics Modeling

**Source**: semantic-scholar
**ID**: c36d80d056943b2363aef94a9d8543d4e7afa234
**URL**: https://www.semanticscholar.org/paper/c36d80d056943b2363aef94a9d8543d4e7afa234
**Date**: 2025-04-26
**Year**: 2025
**Authors**: Lei Shi, Yurui Chen, Vijay Vedula
**Citations**: 2

## Abstract

Finite element analysis (FEA) forms the cornerstone of modeling cardiac biomechanics but is computationally expensive, limiting its clinical application for digital twin creation, which often requires tens to hundreds of simulations to estimate tissue parameters. We developed an attention-enhanced graph neural network (GNN)-based FEA emulator, HeartSimSage, to rapidly predict passive biventricular myocardial displacements from patient-specific geometries, chamber pressures, and material properties. HeartSimSage addresses the limitations of current emulators by effectively handling diverse three-dimensional (3D) biventricular geometries, mesh topologies, fiber directions, structurally based constitutive models, and physiological boundary conditions. It supports flexible mesh structures with variable node counts, orderings, and element connectivity. To optimize information propagation, we designed a neighboring connection strategy inspired by Graph Sample and Aggregate (GraphSAGE) that prioritizes local interactions while maintaining mid-to-long-range dependencies. We further incorporated Laplace-Dirichlet solutions for enhanced spatial encoding and employed subset-based training for improved efficiency. By integrating an attention mechanism, HeartSimSage adaptively weighs neighbor contributions and filters irrelevant information, enhancing prediction accuracy. HeartSimSage achieves approximately 13,000x speedup on GPU and 190x on CPU compared to traditional FEA, while maintaining a nominal averaged error of 0.13% +- 0.12% in predicting biventricular displacements. We validated our model using a published left ventricle dataset and conducted sensitivity analyses on hyperparameters, neighboring strategies, and the attention mechanism.
