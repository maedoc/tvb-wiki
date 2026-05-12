# SPD Learn: A Geometric Deep Learning Python Library for Neural Decoding Through Trivialization

**Source**: semantic-scholar
**ID**: 90d3e506d395036dbd11db57ad489e2968269bd4
**DOI**: 10.48550/arXiv.2602.22895
**URL**: https://www.semanticscholar.org/paper/90d3e506d395036dbd11db57ad489e2968269bd4
**Date**: 2026-02-26
**Year**: 2026
**Authors**: B. Aristimunha, Ce Ju, A. Collas, Florent Bouchard, A. Mian, Bertrand Thirion, Sylvain Chevallier, Reinmar J. Kobler
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Implementations of symmetric positive definite (SPD) matrix-based neural networks for neural decoding remain fragmented across research codebases and Python packages. Existing implementations often employ ad hoc handling of manifold constraints and non-unified training setups, which hinders reproducibility and integration into modern deep-learning workflows. To address this gap, we introduce SPD Learn, a unified and modular Python package for geometric deep learning with SPD matrices. SPD Learn provides core SPD operators and neural-network layers, including numerically stable spectral operators, and enforces Stiefel/SPD constraints via trivialization-based parameterizations. This design enables standard backpropagation and optimization in unconstrained Euclidean spaces while producing manifold-constrained parameters by construction. The package also offers reference implementations of representative SPDNet-based models and interfaces with widely used brain computer interface/neuroimaging toolkits and modern machine-learning libraries (e.g., MOABB, Braindecode, Nilearn, and SKADA), facilitating reproducible benchmarking and practical deployment.
