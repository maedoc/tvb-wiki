# RopeDreamer: A Kinematic Recurrent State Space Model for Dynamics of Flexible Deformable Linear Objects

**Source**: arxiv
**ID**: 2604.28161
**URL**: https://arxiv.org/abs/2604.28161
**Date**: 2026-04-30
**Year**: 2026
**Authors**: Tim Missal, Lucas Domingues, Berk Guler, Simon Manschitz, Jan Peters, Paula Dornhofer Paro Costa
**Categories**: cs.RO

## Abstract

The robotic manipulation of Deformable Linear Objects (DLOs) is a fundamental challenge due to the high-dimensional, non-linear dynamics of flexible structures and the complexity of maintaining topological integrity during contact-rich tasks. While recent data-driven methods have utilized Recurrent and Graph Neural Networks for dynamics modeling, they often struggle with self-intersections and non-physical deformations, such as tangling and link stretching. In this paper, we propose a latent dynamics framework that combines a Recurrent State Space Model with a Quaternionic Kinematic Chain representation to enable robust, long-term forecasting of DLO states. By encoding the DLO as a sequence of relative rotations (quaternions) rather than independent Cartesian positions, we inherently constrain the model to a physically valid manifold that preserves link-length constancy. Furthermore, we introduce a dual-decoder architecture that decouples state reconstruction from future-state prediction, forcing the latent space to capture the underlying physics of deformation. We evaluate our approach on a large-scale simulated dataset of complex pick-and-place trajectories involving self-intersections. Our results demonstrate that the proposed model achieves a 40.52% reduction in open-loop prediction error over 50-step horizons compared to the state-of-the-art baseline, while reducing inference time by 31.17%. Our model further maintains superior topological consistency in scenarios with multiple crossings, proving its efficacy as a compositional primitive for long-horizon manipulation planning.
