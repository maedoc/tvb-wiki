---
created: 2026-04-20
sources:
- raw/papers/strogatz-1994.md
- raw/papers/guckenheimer-holmes-1983.md
- raw/papers/kuznetsov-2004.md
- raw/papers/seydel-2010.md
- raw/papers/touboul-2011.md
tags:
- bifurcation-analysis
- neural-mass-models
- epilepsy-modeling
title: Bifurcation Theory
type: concept
updated: '2026-04-24'
---

## Definition
Bifurcation theory studies how the qualitative behavior of dynamical systems changes as parameters are varied. It identifies critical parameter values where system behavior undergoes sudden transitions.

## Types of Bifurcations

### Local Bifurcations (Codimension 1)
- **Saddle-node**: Creation/annihilation of fixed points
- **Transcritical**: Exchange of stability between fixed points
- **Pitchfork**: Symmetry-breaking bifurcations
- **Hopf**: Birth of limit cycles from fixed points

### Global Bifurcations
- **Homoclinic**: Orbit connects to saddle equilibrium
- **Heteroclinic**: Connections between different saddles
- **Infinite period**: Cycle period diverges

### Codimension 2 Bifurcations
- Bogdanov-Takens (double zero eigenvalue)
- Cusp bifurcations
- Takens-Bogdanov points

## Applications in Neuroscience

### Epilepsy Modeling
- Seizure onset as bifurcation
- [[epilepsy modeling]] uses bifurcation analysis
- Parameter changes trigger pathological states
- Critical slowing before transitions

### Neural Mass Models
- [[neural mass model]] parameter exploration
- Identifying operating regimes
- Transitions between oscillatory states
- [[bifurcation analysis]] for model calibration

## Numerical Methods
- Continuation methods (AUTO, MATCONT)
- Branch tracing algorithms
- Stability computation
- Test function detection

## Related Concepts
- [[dynamical systems theory]] — Mathematical foundation
- [[nonlinear dynamics]] — System behavior
- [[neural mass model]] — Application domain
- [[epilepsy modeling]] — Clinical application

## References
- kuznetsov-2004 — Applied bifurcation methods
- seydel-2010 — Practical numerical techniques
- strogatz-1994 — Introduction to bifurcations