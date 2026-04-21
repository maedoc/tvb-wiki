# IoT-Brain: Grounding LLMs for Semantic-Spatial Sensor Scheduling

**arXiv ID**: 2604.08033
**Published**: 2026-04-09
**Updated**: 2026-04-09
**Authors**: Zhaomeng Zhou, Lan Zhang, Junyang Wang, Mu Yuan, Junda Lin, Jinke Song
**Categories**: cs.AI, cs.MA, cs.NI
**URL**: https://arxiv.org/abs/2604.08033
**PDF**: https://arxiv.org/pdf/2604.08033
**Source**: arXiv

## Abstract

Intelligent systems powered by large-scale sensor networks are shifting from predefined monitoring to intent-driven operation, revealing a critical Semantic-to-Physical Mapping Gap. While large language models (LLMs) excel at semantic understanding, existing perception-centric pipelines operate retrospectively, overlooking the fundamental decision of what to sense and when. We formalize this proactive decision as Semantic-Spatial Sensor Scheduling (S3) and demonstrate that direct LLM planning is unreliable due to inherent gaps in representation, reasoning, and optimization. To bridge these gaps, we introduce the Spatial Trajectory Graph (STG), a neuro-symbolic paradigm governed by a verify-before-commit discipline that transforms open-ended planning into a verifiable graph optimization problem. Based on STG, we implement IoT-Brain, a concrete system embodiment, and construct TopoSense-Bench, a campus-scale benchmark with 5,250 natural-language queries across 2,510 cameras. Evaluations show that IoT-Brain boosts task success rate by 37.6% over the strongest search-intensive methods while running nearly 2 times faster and using 6.6 times fewer prompt tokens. In real-world deployment, it approaches the reliability upper bound while reducing 4.1 times network bandwidth, providing a foundational framework for LLMs to interact with the physical world with unprecedented reliability and efficiency.
