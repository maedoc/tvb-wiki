# Toward Variational Structural Learning of Bayesian Networks

**Source**: semantic-scholar
**ID**: 235ad241600027b3a59edcafef9a92c8f52da13f
**DOI**: 10.1109/ACCESS.2025.3533878
**URL**: https://www.semanticscholar.org/paper/235ad241600027b3a59edcafef9a92c8f52da13f
**Year**: 2025
**Authors**: A. Masegosa, Manuel Gómez-Olmedo
**Venue**: IEEE Access
**Citations**: 1

## Abstract

This study presents a novel variational framework for structural learning in Bayesian networks (BNs), addressing the key limitation of existing Bayesian methods: their lack of scalability to large graphs with many variables. Traditional approaches, such as MCMC and stochastic search, often encounter computational barriers due to the super-exponential growth of the Directed Acyclic Graph (DAG) space. Our method introduces a scalable alternative by leveraging a factorized variational family to approximate the posterior distribution over DAG structures, enabling efficient computation of Bayesian scores and predictive posterior inference. Unlike previous methods, which are constrained by high computational costs or domain-specific limitations, this approach achieves tractability through mean-field variational inference and tractable updating equations, allowing application to significantly larger datasets. Empirical results on benchmark datasets demonstrate that the proposed framework consistently outperforms state-of-the-art methods in terms of scalability and predictive accuracy while maintaining robustness across diverse scenarios. This work represents a key step towards scalable Bayesian structural learning and opens avenues for future research to refine the variational approximation and incorporate advanced parallelization techniques.
