# BACE: Behavior-Adaptive Connectivity Estimation for Interpretable Graphs of Neural Dynamics

**Source**: semantic-scholar
**ID**: 84b6e5ab7026dc8deb35259115c04125abcd85a0
**DOI**: 10.1101/2025.10.21.683776
**URL**: https://www.semanticscholar.org/paper/84b6e5ab7026dc8deb35259115c04125abcd85a0
**Date**: 2025-10-11
**Year**: 2025
**Authors**: Mehrnaz Asadi, Sina Javadzadeh, Rahil Soroushmojdehi, S. Alireza, S. Mousavi, T. Sanger
**Venue**: bioRxiv
**Citations**: 4

## Abstract

Understanding how distributed brain regions coordinate to produce behavior requires models that are both predictive and interpretable. We introduce Behavior-Adaptive Connectivity Estimation (BACE), an end-to-end framework that learns phase-specific, directed inter-regional connectivity directly from multi-region intracranial local field potentials (LFP). BACE aggregates many micro-contacts within each anatomical region via per-region temporal encoders, applies a learnable adjacency specific to each behavioral phase, and is trained on a forecasting objective. On synthetic multivariate time series with known graphs, BACE accurately recovers ground-truth directed interactions while achieving forecasting performance comparable to state-of-the-art baselines. Applied to human subcortical LFP recorded simultaneously from eight regions during a cued reaching task, BACE yields an explicit 8×8 connectivity matrix for each within-trial behavioral phase. The resulting behavioral phase-specific graphs reveal behavioraligned reconfiguration of inter-regional influence and provide compact, interpretable adjacency matrices for comparing network organization across behavioral phases. By linking predictive success to explicit connectivity estimates, BACE offers a practical tool for generating data-driven hypotheses about the dynamic coordination of subcortical regions during behavior.
