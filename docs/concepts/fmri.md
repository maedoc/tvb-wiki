---
title: fMRI
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [neuroimaging-fmri, resting-state, task-based]
sources: [raw/papers/ogawa-1990.md, raw/papers/logothetis-2001.md, raw/papers/friston-1994.md, raw/papers/huettel-2009.md]
---

# fMRI

Functional magnetic resonance imaging (fMRI) is a non-invasive neuroimaging technique that measures brain activity by detecting changes in blood oxygenation and flow associated with neural activity.

## Definition

fMRI relies on the Blood Oxygenation Level Dependent (BOLD) contrast mechanism discovered by [[seiji-ogawa]] in 1990. When neural activity increases, local blood flow increases disproportionately to oxygen consumption, changing the ratio of oxygenated to deoxygenated hemoglobin, which affects local magnetic field properties.

## Types of fMRI

### Task-Based fMRI
- Measures brain activity during specific cognitive or motor tasks
- Uses experimental designs (block or event-related)
- Statistical analysis via General Linear Model (statistical-parametric-mapping)

### Resting-State fMRI
- Measures spontaneous activity during task-free conditions
- Discovered by [[bharat-biswal]] in 1995
- Reveals intrinsic-connectivity-networks via temporal correlations

## Role in Whole-Brain Modeling

fMRI serves as the primary empirical target for validating whole-brain models:

1. **Resting-state connectivity**: Models generate synthetic BOLD time series and compute functional connectivity matrices to compare with empirical data
2. **Task responses**: Models simulate task-evoked activations for comparison with experimental results
3. **Network organization**: Model-generated networks are validated against resting-state network topologies

The neurovascular-coupling between neural activity and BOLD is critical for model-data comparison. [[nikos-logothetis]] showed that BOLD correlates most strongly with local field potentials (LFPs) rather than spiking activity, informing how neural mass model outputs should be converted to BOLD signals.

## Key Challenges

- **Motion artifacts**: Head motion creates spurious connectivity (power-2012)
- **Hemodynamic response**: Delayed and dispersed (~6 second peak)
- **Spatial resolution**: Limited by vascular architecture (~3mm typical)
- **Temporal resolution**: Limited by TR (typically 1-3 seconds)

## Related Concepts
- [[eeg]] – Complementary electrophysiological measure
- [[meg]] – Magnetic counterpart to EEG
- [[bold-signal]] – Underlying contrast mechanism
- [[resting-state]] – Task-free functional connectivity
- [[functional-connectivity]] – Statistical dependencies between regions
- neurovascular-coupling – Link between neural activity and hemodynamics
