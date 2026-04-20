---
title: Resting-State fMRI
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [resting-state, neuroimaging-fmri, functional-connectivity]
sources: [raw/papers/biswal-1995.md, raw/papers/fox-raichle-2007.md, raw/papers/smith-2009.md, raw/papers/zuo-2010.md, raw/papers/buckner-2013.md]
---

# Resting-State fMRI

Resting-state fMRI (rs-fMRI) measures spontaneous brain activity during task-free conditions to reveal intrinsic functional organization through temporal correlations between regions.

## Definition

Discovered by [[bharat-biswal]] in 1995, resting-state functional connectivity refers to the observation that spontaneous low-frequency (<0.1 Hz) fluctuations in BOLD signal are correlated between functionally related brain regions even in the absence of explicit tasks.

## Intrinsic Connectivity Networks (ICNs)

Major resting-state networks include:

| Network | Key Regions | Function |
|---------|-------------|----------|
| Default Mode | PCC, mPFC, angular gyrus | Self-referential processing |
| Sensorimotor | Pre/postcentral gyri | Motor/sensory function |
| Visual | Occipital cortex | Visual processing |
| Frontoparietal | dlPFC, IPL | Cognitive control |
| Salience | AI, ACC | Attention/salience |
| Dorsal Attention | FEF, IPS | Spatial attention |

## Role in Whole-Brain Modeling

Resting-state connectivity is the primary empirical target for whole-brain models:

1. **Validation target**: Models generate synthetic BOLD time series and compute functional connectivity for comparison with empirical data
2. **Network topology**: The pattern of correlations constrains model parameters
3. **Spontaneous dynamics**: Models must reproduce empirically observed fluctuations without external stimulation

## Reliability and Reproducibility

zuo-2010 demonstrated that ICNs are reliable across scanning sessions, supporting their use as stable model targets. smith-2009 showed correspondence between task activation and resting-state patterns, suggesting shared underlying architecture.

## Confounds and Preprocessing

- **Motion artifacts**: Systematic effects on connectivity (power-2012)
- **Physiological noise**: Cardiac and respiratory fluctuations
- **Global signal**: Controversial correction method

## Related Concepts
- [[fmri]] – Parent imaging modality
- [[functional-connectivity]] – Statistical dependencies
- intrinsic-connectivity-networks – Spontaneous networks
- [[default-mode-network]] – Most studied ICN
- spontaneous-activity – Ongoing neural dynamics
