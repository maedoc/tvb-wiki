# Online Bayesian Calibration under Gradual and Abrupt System Changes

**Source**: arxiv
**ID**: 2605.06612
**URL**: https://arxiv.org/abs/2605.06612
**Date**: 2026-05-07
**Year**: 2026
**Authors**: Yang Xu, Chiwoo Park
**Categories**: cs.LG, cs.ET, stat.ML

## Abstract

Bayesian model calibration is central to digital twins and computer experiments, as it aligns model outputs with field observations by estimating calibration parameters and correcting systematic model bias. Classical Bayesian calibration introduces latent parameters and a discrepancy function to model bias, but suffers from parameter--discrepancy confounding and is typically formulated as an offline procedure under a stationary data-generating assumption. These limitations are restrictive in modern digital twin applications, where systems evolve over time and may exhibit gradual drift and abrupt regime shifts. While data assimilation methods enable sequential updates, they generally do not explicitly model systematic bias and are less effective under abrupt changes. We propose Bayesian Recursive Projected Calibration (BRPC), an online Bayesian calibration framework for streaming data under simulator mismatch and nonstationarity. BRPC extends projected calibration to the online setting by separating a discrepancy-free particle update for calibration parameters from a conditional Gaussian process update for discrepancy, preserving identifiability while enabling bias-aware adaptation under gradual system evolution. To handle abrupt changes, BRPC is integrated with restart mechanisms that detect regime shifts and reset the calibration process. We establish theoretical guarantees for both components, including tracking performance under gradual evolution and false-alarm and detection behavior for restart mechanisms. Empirical studies on synthetic and plant-simulation benchmarks show that BRPC improves calibration accuracy under gradual changes, while restart-augmented BRPC further improves robustness and predictive performance under abrupt regime shifts compared to sliding-window Bayesian calibration and data assimilation baselines.
