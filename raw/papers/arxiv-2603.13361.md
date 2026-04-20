# BrainCast: A Spatio-Temporal Forecasting Model for Whole-Brain fMRI Time Series Prediction

**arXiv ID**: 2603.13361
**Published**: 2026-03-09
**Updated**: 2026-03-09
**Authors**: Yunlong Gao, Jinbo Yang, Li Xiao, Haiye Huo, Yang Ji, Hao Wang, Aiying Zhang, Yu-Ping Wang
**Categories**: cs.CV, cs.AI, stat.ML
**URL**: https://arxiv.org/abs/2603.13361
**PDF**: https://arxiv.org/pdf/2603.13361
**Source**: arXiv

## Abstract

Functional magnetic resonance imaging (fMRI) enables noninvasive investigation of brain function, while short clinical scan durations, arising from human and non-human factors, usually lead to reduced data quality and limited statistical power for neuroimaging research. In this paper, we propose BrainCast, a novel spatio-temporal forecasting framework specifically tailored for whole-brain fMRI time series forecasting, to extend informative fMRI time series without additional data acquisition. It formulates fMRI time series forecasting as a multivariate time series prediction task and jointly models temporal dynamics within regions of interest (ROIs) and spatial interactions across ROIs. Specifically, BrainCast integrates a Spatial Interaction Awareness module to characterize inter-ROI dependencies via embedding every ROI time series as a token, a Temporal Feature Refinement module to capture intrinsic neural dynamics within each ROI by enhancing both low- and high-energy temporal components of fMRI time series at the ROI level, and a Spatio-temporal Pattern Alignment module to combine spatial and temporal representations for producing informative whole-brain features. Experimental results on resting-state and task fMRI datasets from the Human Connectome Project demonstrate the superiority of BrainCast over state-of-the-art time series forecasting baselines. Moreover, fMRI time series extended by BrainCast improve downstream cognitive ability prediction, highlighting the clinical and neuroscientific impact brought by whole-brain fMRI time series forecasting in scenarios with restricted scan durations.
