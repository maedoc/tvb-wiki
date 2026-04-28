# NeuroClaw Technical Report

**Source**: arxiv
**ID**: 2604.24696
**URL**: https://arxiv.org/abs/2604.24696
**Date**: 2026-04-27
**Year**: 2026
**Authors**: Cheng Wang, Zhibin He, Zhihao Peng, Shengyuan Liu, Yufan Hu, Lichao Sun, Xiang Li, Yixuan Yuan
**Categories**: cs.CV

## Abstract

Agentic artificial intelligence systems promise to accelerate scientific workflows, but neuroimaging poses unique challenges: heterogeneous modalities (sMRI, fMRI, dMRI, EEG), long multi-stage pipelines, and persistent reproducibility risks. To address this gap, we present NeuroClaw, a domain-specialized multi-agent research assistant for executable and reproducible neuroimaging research. NeuroClaw operates directly on raw neuroimaging data across formats and modalities, grounding decisions in dataset semantics and BIDS metadata so users need not prepare curated inputs or bespoke model code. The platform combines harness engineering with end-to-end environment management, including pinned Python environments, Docker support, automated installers for common neuroimaging tools, and GPU configuration. In practice, this layer emphasizes checkpointing, post-execution verification, structured audit traces, and controlled runtime setup, making toolchains more transparent while improving reproducibility and auditability. A three-tier skill/agent hierarchy separates user-facing interaction, high-level orchestration, and low-level tool skills to decompose complex workflows into safe, reusable units. Alongside the NeuroClaw framework, we introduce NeuroBench, a system-level benchmark for executability, artifact validity, and reproducibility readiness. Across multiple multimodal LLMs, NeuroClaw-enabled runs yield consistent and substantial score improvements compared with direct agent invocation. Project homepage: https://cuhk-aim-group.github.io/NeuroClaw/index.html
