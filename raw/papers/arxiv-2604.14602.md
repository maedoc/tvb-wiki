# CausalDetox: Causal Head Selection and Intervention for Language Model Detoxification

**arXiv ID**: 2604.14602
**Published**: 2026-04-16
**Updated**: 2026-04-16
**Authors**: Yian Wang, Yuen Chen, Agam Goyal, Hari Sundaram
**Categories**: cs.CL, cs.AI
**URL**: https://arxiv.org/abs/2604.14602
**PDF**: https://arxiv.org/pdf/2604.14602
**Source**: arXiv

## Abstract

Large language models (LLMs) frequently generate toxic content, posing significant risks for safe deployment. Current mitigation strategies often degrade generation quality or require costly human annotation. We propose CAUSALDETOX, a framework that identifies and intervenes on the specific attention heads causally responsible for toxic generation. Using the Probability of Necessity and Sufficiency (PNS), we isolate a minimal set of heads that are necessary and sufficient for toxicity. We utilize these components via two complementary strategies: (1) Local Inference-Time Intervention, which constructs dynamic, input-specific steering vectors for context-aware detoxification, and (2) PNS-Guided Fine-Tuning, which permanently unlearns toxic representations. We also introduce PARATOX, a novel benchmark of aligned toxic/non-toxic sentence pairs enabling controlled counterfactual evaluation. Experiments on ToxiGen, ImplicitHate, and ParaDetox show that CAUSALDETOX achieves up to 5.34% greater toxicity reduction compared to baselines while preserving linguistic fluency, and offers a 7x speedup in head selection.
