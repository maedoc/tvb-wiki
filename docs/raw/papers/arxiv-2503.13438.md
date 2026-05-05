# Deep Belief Markov Models for POMDP Inference

**Source**: semantic-scholar
**ID**: 31fac6c7b77a918db4e8d35cc553267bde5ffdd6
**DOI**: 10.48550/arXiv.2503.13438
**URL**: https://www.semanticscholar.org/paper/31fac6c7b77a918db4e8d35cc553267bde5ffdd6
**Date**: 2025-03-17
**Year**: 2025
**Authors**: Giacomo Arcieri, K. G. Papakonstantinou, Daniel Straub, Eleni Chatzi
**Venue**: Neural Networks
**Citations**: 0

## Abstract

This work introduces a novel deep learning-based architecture, termed the Deep Belief Markov Model (DBMM), which provides efficient, model-formulation agnostic inference in Partially Observable Markov Decision Process (POMDP) problems. The POMDP framework allows for modeling and solving sequential decision-making problems under observation uncertainty. In complex, high-dimensional, partially observable environments, existing methods for inference based on exact computations (e.g., via Bayes' theorem) or sampling algorithms do not always scale well. Furthermore, ground truth states may not be available for learning the exact transition dynamics. DBMMs extend deep Markov models into the partially observable decision-making framework and allow efficient belief inference entirely based on available observation data via variational inference methods. By leveraging the potency of neural networks, DBMMs can infer and simulate non-linear relationships in the system dynamics and naturally scale to problems with high dimensionality and discrete or continuous variables. In addition, neural network parameters can be dynamically updated efficiently based on data availability. DBMMs can thus be used to infer a belief variable, thus enabling the derivation of POMDP solutions over the belief space. We evaluate the efficacy of the proposed methodology by evaluating the capability of model-formulation agnostic inference of DBMMs in benchmark problems that include discrete and continuous variables. Finally, we demonstrate the practical utility of the inferred beliefs in a downstream decision-making task, showing that an RL agent guided by DBMMs beliefs significantly outperforms powerful model-free baselines and achieves near-optimal performance.1.
