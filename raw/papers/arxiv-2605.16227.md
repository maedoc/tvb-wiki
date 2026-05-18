# LymphNode: A Plug-and-Play Access Control Method for Deep Neural Networks

**Source**: arxiv
**ID**: 2605.16227
**URL**: https://arxiv.org/abs/2605.16227
**Date**: 2026-05-15
**Year**: 2026
**Authors**: Hanyu Pei, Shang Liu, Zeyan Liu
**Categories**: cs.CR

## Abstract

Deep Neural Networks (DNNs) are high-value intellectual property (IP), yet deploying them to edge environments exposes them to \textbf{unrestricted oracle access}, rendering them vulnerable to model extraction and inversion attacks. Existing defenses fail to address this practically: passive watermarking only offers post-hoc provenance, while active defenses impose prohibitive latency or require persistent access to sensitive training data. To bridge this gap, we propose \textit{LymphNode}, a novel post-hoc defense framework that acts as an intrinsic ``immune system" within the model. \textit{LymphNode} enforces a strict ``default-deny'' policy: it actively neutralizes model utility for unauthorized queries via \textbf{Generalized Sparse Universal Adversarial Perturbations (GSUAP)} injected into the feature space, effectively blocking gradient estimation and data inference. Utility is selectively restored only for authorized inputs carrying a stealthy feature-domain credential. Our framework is highly practical: it is \textbf{data-efficient}, establishing robust protection with fewer than 100 samples ($<1\%$ of training data), and \textbf{cross-dataset adaptable}, enabling protection using public surrogate datasets. \textit{LymphNode} thus provides a lightweight, immediately deployable defense for high-stakes scenarios where original training data is restricted or unavailable.
