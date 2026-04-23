---
created: 2026-04-20
sources:
- raw/papers/wilson-cowan-1972.md
- raw/papers/wilson-cowan-1973.md
- raw/papers/arxiv-2510.22022.md
- raw/papers/freeman-1975.md
- raw/papers/dayan-abbott-2001.md
- raw/papers/arxiv-2603.13635.md
- raw/papers/gerstner-2014.md
tags:
- people-researcher
- neural-mass-models
- brain-oscillations
title: Hugh R. Wilson
type: entity
updated: '2026-04-23'
---

# Hugh R. Wilson

Canadian computational neuroscientist and mathematician. Co-creator of the Wilson-Cowan model—the canonical firing-rate model of excitatory and inhibitory neural populations. Also known for work on pattern formation and visual cortex modeling.

## Key Contributions

- **Wilson-Cowan model (1972)**: Canonical firing-rate model of coupled excitatory and inhibitory populations
- **Neural field theory (1973)**: Spatial extension to traveling waves and pattern formation
- **Visual hallucination modeling**: With Cowan and Ermentrout, explained form constants through neural field instabilities
- **Pattern formation in neural tissue**: Applications to cortical development and disease

## Major Publications

- Wilson & Cowan (1972) "Excitatory and inhibitory interactions in localized populations of model neurons"
- Wilson & Cowan (1973) "A mathematical theory of the functional dynamics of cortical and thalamic nervous tissue"
- Ermentrout & Cowan (1979) "A mathematical theory of visual hallucinations"
- Wilson (1999) "Spikes, Decisions, and Actions: The Dynamical Foundations of Neuroscience"

## The Wilson-Cowan Model

The model describes the mean firing rate of excitatory and inhibitory populations:
- τ_E dE/dt = -E + S_E(aE - bI + P)
- τ_I dI/dt = -I + S_I(cE - dI + Q)

Where S_E and S_I are sigmoid response functions converting net synaptic input to population firing rate.

## Legacy

The Wilson-Cowan equations are the foundation of neural mass modeling. Virtually all subsequent population models (Jansen-Rit, DCM, TVB implementations) trace their lineage to this formulation. The 1973 spatial extension also founded neural field theory.

## Related Concepts

- [[Wilson-Cowan]]
- [[neural mass model]]
- [[Jack Cowan]]
- brain oscillations