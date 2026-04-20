# Stochastic Attention: Connectome-Inspired Randomized Routing for Expressive Linear-Time Attention

**arXiv ID**: 2604.00754
**Published**: 2026-04-01
**Updated**: 2026-04-01
**Authors**: Zehao Jin, Yanan Sui
**Categories**: cs.CL, cs.LG
**URL**: https://arxiv.org/abs/2604.00754
**PDF**: https://arxiv.org/pdf/2604.00754
**Source**: arXiv

## Abstract

The whole-brain connectome of a fruit fly comprises over 130K neurons connected with a probability of merely 0.02%, yet achieves an average shortest path of only 4.4 hops. Despite being highly structured at the circuit level, the network's long-range connections are broadly distributed across brain regions, functioning as stochastic shortcuts that enable efficient global communication. Inspired by this observation, we propose Stochastic Attention (SA), a drop-in enhancement for sliding-window attention (SWA) that applies a random permutation to the token sequence before windowed attention and restores the original order afterward. This transforms the fixed local window into a stochastic global one within the same $O(nw)$ per-layer budget. Through depth, independently sampled permutations yield exponentially growing receptive fields, achieving full sequence coverage in $O(\log_w n)$ layers versus $O(n/w)$ for SWA. We validate SA in two settings: pre-training language models from scratch, where a gated SA + SWA combination achieves the best average zero-shot accuracy, and training-free inference on Qwen3-8B and Qwen3-30B-A3B, where SA consistently outperforms SWA and matches or exceeds Mixture of Block Attention at comparable compute budgets. These results suggest that connectome-inspired stochastic routing is a practical primitive for improving the expressivity of efficient attention, complementary to existing linear and sparse approaches.
