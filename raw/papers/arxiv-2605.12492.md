# Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation

**Source**: arxiv
**ID**: 2605.12492
**URL**: https://arxiv.org/abs/2605.12492
**Date**: 2026-05-12
**Year**: 2026
**Authors**: Kexuan Shi, Hanxuan Li, Zeju Qiu, Yandong Wen, Simon Buchholz, Weiyang Liu
**Categories**: cs.LG, stat.ML

## Abstract

We introduce Pion, a spectrum-preserving optimizer for large language model (LLM) training based on orthogonal equivalence transformation. Unlike additive optimizers such as Adam and Muon, Pion updates each weight matrix through left and right orthogonal transformations, preserving its singular values throughout training. This yields an optimization mechanism that modulates the geometry of weight matrices while keeping their spectral norm fixed. We derive the Pion update rule, systematically examine its design choices, and analyze its convergence behavior along with several key properties. Empirical results show that Pion offers a stable and competitive alternative to standard optimizers for both LLM pretraining and finetuning.
