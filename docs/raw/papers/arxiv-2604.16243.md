# Find, Fix, Reason: Context Repair for Video Reasoning

**arXiv ID**: 2604.16243
**Published**: 2026-04-17
**Updated**: 2026-04-17
**Authors**: Haojian Huang, Chuanyu Qin, Yinchuan Li, Yingcong Chen
**Categories**: cs.CV
**URL**: https://arxiv.org/abs/2604.16243
**PDF**: https://arxiv.org/pdf/2604.16243
**Source**: arXiv

## Abstract

Reinforcement learning has advanced video reasoning in large multi-modal models, yet dominant pipelines either rely on on-policy self-exploration, which plateaus at the model's knowledge boundary, or hybrid replay that mixes policies and demands careful regularization. Dynamic context methods zoom into focused evidence but often require curated pretraining and two-stage tuning, and their context remains bounded by a small model's capability. In contrast, larger models excel at instruction following and multi-modal understanding, can supply richer context to smaller models, and rapidly zoom in on target regions via simple tools. Building on this capability, we introduce an observation-level intervention: a frozen, tool-integrated teacher identifies the missing spatiotemporal dependency and provides a minimal evidence patch (e.g., timestamps, regions etc.) from the original video while the question remains unchanged. The student answers again with the added context, and training updates with a chosen-rollout scheme integrated into Group Relative Policy Optimization (GRPO). We further propose a Robust Improvement Reward (RIR) that aligns optimization with two goals: outcome validity through correct answers and dependency alignment through rationales that reflect the cited evidence. Advantages are group-normalized across the batch, preserving on-policy exploration while directing it along causally meaningful directions with minimal changes to the training stack. Experiments on various related benchmarks show consistent accuracy gains and strong generalization. Web page and source code will be available at https://github.com/JethroJames/FFR.git.
