# GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs

**Source**: arxiv
**ID**: 2605.08074
**URL**: https://arxiv.org/abs/2605.08074
**Date**: 2026-05-08
**Year**: 2026
**Authors**: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
**Categories**: cs.LG

## Abstract

Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
