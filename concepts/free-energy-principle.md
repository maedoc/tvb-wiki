---
created: 2026-04-20
sources:
- raw/papers/friston-2010-fep.md
- raw/papers/friston-2007.md
- raw/papers/deco-2013.md
- raw/papers/breakspear-2017.md
tags:
- dynamic-causal-modeling
- whole-brain-modeling
- effective-connectivity
title: Free Energy Principle
type: concept
updated: '2026-04-24'
---

## Definition
The Free Energy Principle (FEP) proposes that self-organizing biological systems minimize variational free energy, which bounds surprise (negative log evidence). This provides a unifying account of perception, action, and learning.

## Core Concepts

### Variational Free Energy
- F = Expected energy - Entropy
- Bounds surprise: F ≥ -ln p(y)
- Minimization equivalent to Bayesian inference

### Perception as Inference
- Brain as inference machine
- Generative models predict sensory input
- Prediction errors drive belief updating

### Active Inference
- Action minimizes expected free energy
- Perception and action jointly optimize
- Exploration-exploitation tradeoff

### Self-Evidence
- Biological systems maintain states
- Resist dispersion (entropy)
- Self-organizing to characteristic states

## Connection to DCM
- friston-2010-fep — Unifying framework
- [[dynamic causal modeling]] implements FEP
- Model inversion minimizes free energy
- [[neural mass model]] as generative model

## Applications
- Computational psychiatry
- [[whole brain]] model optimization
- Behavior and perception
- Learning and memory

## Related Concepts
- [[dynamic causal modeling]] — Implementation
- [[variational bayes]] — Mathematical method
- bayesian brain — Related hypothesis

## Criticisms and Debates
- Scope and testability
- Relationship to other frameworks
- Computational complexity
- Empirical validation

## References
- friston-2010-fep — Foundational review
- friston-2007 — Variational methods