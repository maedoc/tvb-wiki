# Effective, Efficient, and General Information Abstraction for Imperfect-Information Extensive-Form Games

**Source**: arxiv
**ID**: 2605.10900
**URL**: https://arxiv.org/abs/2605.10900
**Date**: 2026-05-11
**Year**: 2026
**Authors**: Boning Li, Longbo Huang
**Categories**: cs.GT

## Abstract

Information abstraction reduces the computational cost of solving imperfect-information games by clustering information sets into a smaller number of \emph{buckets}. Existing methods either rely on domain-specific features such as rank or equity, which are inapplicable to games with non-standard payoff structures, or require expensive offline neural-network training on billions of samples. We propose \textbf{Warm-up Expected Value-based Abstraction (WEVA)}, a simple yet effective alternative: run a small number of Counterfactual Regret Minimization (CFR) iterations on the full game as a \emph{warm-up} phase, extract per-hand expected value features at every decision node, form a depth-weighted multi-node feature vector, and apply $k$-means++ clustering to obtain the abstraction mapping. WEVA requires no domain knowledge, no pre-training, and incurs only a small overhead on top of the abstract-game solve. Experiments on three structurally diverse games, with different bucket numbers and CFR variants, show that WEVA consistently outperforms equity-based and rank-based abstractions, reducing exploitability by up to over $80\%$. Surprisingly, as few as $W{=}10$ warm-up iterations already produce abstractions that outperform existing information abstraction methods in most settings. These results establish WEVA as an \emph{effective, efficient, and general} approach to information abstraction in imperfect-information extensive-form games.
