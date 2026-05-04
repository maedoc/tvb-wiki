# Latent Thought Models with Variational Bayes Inference-Time Computation

**Source**: semantic-scholar
**ID**: f0a3835950ca893547d3688e50da1dc77326b22c
**URL**: https://www.semanticscholar.org/paper/f0a3835950ca893547d3688e50da1dc77326b22c
**Date**: 2025-02-03
**Year**: 2025
**Authors**: Deqian Kong, Minglu Zhao, Dehong Xu, Bo Pang, Shu Wang, Edouardo Honig, Zhangzhang Si, Chuan Li, Jianwen Xie, Sirui Xie, Y. Wu
**Venue**: International Conference on Machine Learning
**Citations**: 14

## Abstract

We propose a novel class of language models, Latent Thought Models (LTMs), which incorporate explicit latent thought vectors that follow an explicit prior model in latent space. These latent thought vectors guide the autoregressive generation of ground tokens through a Transformer decoder. Training employs a dual-rate optimization process within the classical variational Bayes framework: fast learning of local variational parameters for the posterior distribution of latent vectors (inference-time computation), and slow learning of global decoder parameters. Empirical studies reveal that LTMs possess additional scaling dimensions beyond traditional Large Language Models (LLMs), such as the number of iterations in inference-time computation and number of latent thought vectors. Higher sample efficiency can be achieved by increasing training compute per token, with further gains possible by trading model size for more inference steps. Designed based on these scaling properties, LTMs demonstrate superior sample and parameter efficiency compared to autoregressive models and discrete diffusion models. They significantly outperform these counterparts in validation perplexity and zero-shot language modeling tasks. Additionally, LTMs exhibit emergent few-shot in-context reasoning capabilities that scale with model size, and achieve competitive performance in conditional and unconditional text generation.
