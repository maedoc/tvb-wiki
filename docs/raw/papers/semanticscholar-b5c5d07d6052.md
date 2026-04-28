# Finetuning the Sample Points in Gaussian Filters via Neural Networks

**Source**: semantic-scholar
**ID**: b5c5d07d6052a5b87b2df289d8243d914990bd22
**DOI**: 10.1109/LSP.2025.3645187
**URL**: https://www.semanticscholar.org/paper/b5c5d07d6052a5b87b2df289d8243d914990bd22
**Year**: 2026
**Authors**: Hanyu Liu, Yuran Chen, Xiucong Sun, Yukai Zhu, Xinlong Wang, Haichao Gui
**Venue**: IEEE Signal Processing Letters
**Citations**: 1

## Abstract

Gaussian filters with deterministic sample points, such as the Unscented Kalman Filter (UKF), Cubature Kalman Filter (CKF), Gauss–Hermite Quadrature Filter (GHQF), etc., have been widely employed for nonlinear state estimation. However, these filters utilize a fixed set of sample points irrespective of the system's nonlinearity. While various studies have explored data-driven approaches to optimize the three parameters of the UKF, these methods do not generalize well to other Gaussian filters with a greater number of sample points. In this letter, we propose a novel neural network-based unified framework for finetuning sample points across all Gaussian filters with deterministic sample points. Specifically, we first pretrain a Multi-Layer Perceptron (MLP) to approximate the mapping from the state's mean and covariance to the sample points of the original Gaussian filter. The MLP then replaces the sample points generation strategy in the Gaussian filter and is further refined by maximizing the marginal likelihood of the observed measurement data. Simulation results demonstrate that the Gaussian filters leveraging the well-trained MLP as the sample point generation strategy achieve higher filtering accuracy compared to their original counterparts.
