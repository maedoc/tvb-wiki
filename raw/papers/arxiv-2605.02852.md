# Inferring Active Neural Circuits Using Diffusion Scores

**Source**: arxiv
**ID**: 2605.02852
**URL**: https://arxiv.org/abs/2605.02852
**Date**: 2026-05-04
**Year**: 2026
**Authors**: Savik Kinger, Johannes Bertram, Luciano Dyballa, Eviatar Yemini, Steven W. Zucker
**Categories**: q-bio.NC

## Abstract

In biological systems, neural circuits compute through directed, short-latency interactions whose effects unfold across multiple time scales and behavioral contexts. We address the problem of inferring these local, lag-specific interactions from sampled neural population activity under varying stimuli, without assuming a parametric form for the underlying dynamics. Our approach leverages denoising score models by estimating joint-window scores over consecutive activity snapshots (i.e., brain states) and converting these scores into calibrated, directed edge tests via cross-block score products. The key insight is that these products recover the Jacobian of the transition map between brain states under nonlinear dynamics. To cleanly separate lag-specific effects, we introduce minimal multi-block windows that condition on intermediate time points, avoiding the omitted-lag bias inherent in pairwise analyses. The resulting method, Score--Block Time Graphs (SBTG), identifies lag-specific directed interactions in sampled neuronal population data. We specifically apply SBTG to whole-brain C. elegans calcium imaging data to recover lag-specific circuit structure not resolved by current methods, including improved alignment with independent connectomes, cell-type-specific temporal organization, and neuromodulatory profiles consistent with known receptor kinetics. These findings highlight the potential for SBTG to serve as a practical ``AI for science'' tool by turning high-dimensional neural population recordings into statistically testable circuit hypotheses.
