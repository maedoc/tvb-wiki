---
created: 2026-04-20
sources:
- raw/papers/biswal-1995.md
- raw/papers/fox-raichle-2007.md
- raw/papers/smith-2009.md
- raw/papers/friston-1993.md
- raw/papers/honey-2009.md
- raw/papers/power-2011.md
- raw/papers/smith-2013-connectomics.md
- raw/papers/zuo-2010.md
- raw/papers/arxiv-2512.00063.md
- raw/papers/semanticscholar-44da8d4ab79e.md
tags:
- functional-connectivity
- resting-state
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
title: Functional Connectivity
type: concept
updated: '2026-04-23'
---

# Functional Connectivity

Functional connectivity refers to statistical dependencies between neurophysiological signals measured from different brain regions, revealing communication and coordination between areas.

## Definition

Unlike [[structural-connectivity]] (anatomical connections), functional connectivity is a statistical concept describing temporal correlations between regional time series. It can exist between regions without direct anatomical connections via polysynaptic or indirect pathways.

## Measures

### fMRI-Based
- **Pearson correlation**: Linear correlation of BOLD time series
- **Partial correlation**: Controlling for other regions
- **Mutual information**: Non-linear dependencies

### EEG/MEG-Based
- **Coherence**: Frequency-specific correlation
- **Phase locking value**: Consistency of phase differences
- **Granger causality**: Directional influence
- **Transfer entropy**: Information flow

## Resting-State Networks

Functional connectivity at rest reveals intrinsic-connectivity-networks including:
- Default mode network
- Sensorimotor network
- Visual network
- Attention networks

## Role in Whole-Brain Modeling

Functional connectivity is the primary validation target for whole-brain models:

1. **Static FC**: Correlation matrix of regional time series
2. **Dynamic FC**: Time-varying connectivity patterns
3. **Network topology**: Small-world, modular structure

Models generate synthetic time series from which FC is computed and compared to empirical data.

## Comparison with Other Connectivity Types

| Type | Definition | Measurement |
|------|------------|-------------|
| Structural | Anatomical connections | [[dti]], tracing |
| Functional | Statistical dependencies | [[fmri]], [[eeg]], [[meg]] correlations |
| Effective | Causal/directed influence | Modeling, perturbation |

## Related Concepts
- [[structural-connectivity]] – Anatomical connections
- [[effective-connectivity]] – Causal interactions
- [[resting-state]] – Task-free functional connectivity
- intrinsic-connectivity-networks – Spontaneous networks
- [[connectivity-types]] – Comparison of connectivity types
- sc-fc-relationship – Structure-function relationship
- [[connectomics]] – Field of connectivity research
- [[connectome]] – Complete connectivity

## Historical Development

### Early Definition (1993)
karl friston|Friston et al. defined functional connectivity as "the temporal correlation between spatially remote neurophysiological events."

### Resting-State Discovery (1995)
bharat biswal|Biswal et al. discovered that resting-state correlations could be reliably measured with fMRI.

### Network Era (2000s-present)
- Large-scale network mapping
- Multimodal connectivity analysis
- Individual differences research

## Structure-Function Relationship

Functional connectivity can exist without direct structural connections due to:
- Polysynaptic pathways
- Common input from shared sources
- Dynamic synchronization

See honey-2009 for empirical evidence of the SC-FC relationship.