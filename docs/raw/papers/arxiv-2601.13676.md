# Autoregressive deep learning for real-time simulation of soft tissue dynamics during virtual neurosurgery

**arXiv ID**: 2601.13676
**Published**: 2026-01-20
**Updated**: 2026-01-20
**Authors**: Fabian Greifeneder, Wolfgang Fenz, Benedikt Alkin, Johannes Brandstetter, Michael Giretzlehner, Philipp Moser
**Categories**: cs.LG
**URL**: https://arxiv.org/abs/2601.13676
**PDF**: https://arxiv.org/pdf/2601.13676
**Source**: arXiv

## Abstract

Accurate simulation of brain deformation is a key component for developing realistic, interactive neurosurgical simulators, as complex nonlinear deformations must be captured to ensure realistic tool-tissue interactions. However, traditional numerical solvers often fall short in meeting real-time performance requirements. To overcome this, we introduce a deep learning-based surrogate model that efficiently simulates transient brain deformation caused by continuous interactions between surgical instruments and the virtual brain geometry. Building on Universal Physics Transformers, our approach operates directly on large-scale mesh data and is trained on an extensive dataset generated from nonlinear finite element simulations, covering a broad spectrum of temporal instrument-tissue interaction scenarios. To reduce the accumulation of errors in autoregressive inference, we propose a stochastic teacher forcing strategy applied during model training. Specifically, training consists of short stochastic rollouts in which the proportion of ground truth inputs is gradually decreased in favor of model-generated predictions. Our results show that the proposed surrogate model achieves accurate and efficient predictions across a range of transient brain deformation scenarios, scaling to meshes with up to 150,000 nodes. The introduced stochastic teacher forcing technique substantially improves long-term rollout stability, reducing the maximum prediction error from 6.7 mm to 3.5 mm. We further integrate the trained surrogate model into an interactive neurosurgical simulation environment, achieving runtimes below 10 ms per simulation step on consumer-grade inference hardware. Our proposed deep learning framework enables rapid, smooth and accurate biomechanical simulations of dynamic brain tissue deformation, laying the foundation for realistic surgical training environments.
