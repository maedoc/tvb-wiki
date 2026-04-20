# Awakening Dormant Experts:Counterfactual Routing to Mitigate MoE Hallucinations

**arXiv ID**: 2604.14246
**Published**: 2026-04-15
**Updated**: 2026-04-15
**Authors**: Wentao Hu, Yanbo Zhai, Xiaohui Hu, Mingkuan Zhao, Shanhong yu, Xue Liu, Kaidong Yu, Shuangyong Song, Xuelong Li
**Categories**: cs.LG, cs.AI
**URL**: https://arxiv.org/abs/2604.14246
**PDF**: https://arxiv.org/pdf/2604.14246
**Source**: arXiv

## Abstract

Sparse Mixture-of-Experts (MoE) models have achieved remarkable scalability, yet they remain vulnerable to hallucinations, particularly when processing long-tail knowledge. We identify that this fragility stems from static Top-$k$ routing: routers tend to favor high-frequency patterns over rare factual associations. Consequently, ``specialist experts'' possessing critical long-tail knowledge are often assigned low gating scores and remain ``dormant'' -- under-prioritized for specific tokens despite their proven causal importance on other inputs. To address this, we propose Counterfactual Routing (CoR), a training-free inference framework designed to awaken these dormant experts. CoR integrates layer-wise perturbation analysis with the Counterfactual Expert Impact (CEI) metric to dynamically shift computational resources from syntax-dominant to knowledge-intensive layers while maintaining a constant total activation count, effectively retrieving causally decisive experts via virtual ablation. Extensive experiments on TruthfulQA, FACTOR, and TriviaQA demonstrate that CoR improves factual accuracy by 3.1\% on average without increasing the inference budget, establishing a superior Pareto frontier compared to static scaling strategies.
