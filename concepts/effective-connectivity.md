---
title: Effective Connectivity
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [effective-connectivity, dynamic-causal-modeling, network-dynamics]
sources: [raw/papers/friston-1994.md]
---

# Effective Connectivity

Effective connectivity refers to the causal or directed influence that one neural system exerts over another, capturing the mechanism by which activity in one region affects activity in another.

## Definition

Unlike [[functional-connectivity]] (statistical dependencies) or [[structural-connectivity]] (anatomical connections), effective connectivity is a mechanistic concept describing the causal effect of one region on another given the network context.

## Estimation Methods

### Model-Based
- **Dynamic Causal Modeling (DCM)**: Bayesian framework for inferring effective connectivity from neuroimaging data
- **Structural Equation Modeling**: Path analysis for connectivity
- **Granger Causality**: Temporal precedence as proxy for causality

### Model-Free
- **Transfer Entropy**: Information-theoretic directed measure
- **Directed Transfer Function**: Frequency-domain causality

## Role in Whole-Brain Modeling

Effective connectivity is what whole-brain models aim to capture:

1. **Model output**: Models generate directed interactions between regions
2. **Validation**: Compare model EC to empirical estimates from DCM
3. **Mechanism**: EC reflects the actual flow of influence in the network

In [[dynamic-causal-modeling]], effective connectivity parameters (A, B, C matrices) describe:
- **A**: Endogenous connectivity
- **B**: Modulation by experimental conditions
- **C**: Driving inputs

## Comparison with Other Connectivity Types

| Type | What It Captures | Directional? |
|------|------------------|--------------|
| Structural | Anatomy | No |
| Functional | Correlation | No |
| Effective | Causal influence | Yes |

## Related Concepts
- [[functional-connectivity]] – Statistical dependencies
- [[structural-connectivity]] – Anatomical connections
- [[dynamic-causal-modeling]] – Primary estimation method
- granger-causality – Temporal causality
- [[connectivity-types]] – Comparison of connectivity types
