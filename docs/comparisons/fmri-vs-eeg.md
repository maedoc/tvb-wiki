---
title: fMRI vs EEG for Whole-Brain Modeling
created: 2026-04-20
updated: 2026-04-20
type: comparison
tags: [comparison, neuroimaging-fmri, neuroimaging-eeg]
sources: [raw/papers/ogawa-1990.md, raw/papers/logothetis-2001.md, raw/papers/niedermeyer-silva-2004.md, raw/papers/nunez-srinivasan-2006.md]
---

# fMRI vs EEG for Whole-Brain Modeling

Comparison of functional MRI and electroencephalography as neuroimaging modalities for whole-brain modeling validation and constraint.

## What is Being Compared

fMRI and EEG are complementary neuroimaging modalities that measure different aspects of brain activity. This comparison evaluates their relative strengths for constraining and validating whole-brain network models.

## Dimensions of Comparison

| Dimension | fMRI | EEG |
|-----------|------|-----|
| **Signal source** | Hemodynamic (BOLD) | Electrical potentials |
| **Temporal resolution** | ~1-3 seconds | ~1 ms |
| **Spatial resolution** | ~3 mm | ~1 cm (scalp) |
| **Directness** | Indirect (neurovascular coupling) | Direct (electrical activity) |
| **Coverage** | Whole brain | Cortical surface |
| **Invasiveness** | Non-invasive | Non-invasive |
| **Cost** | High | Low |
| **Portability** | Fixed scanner | Portable systems |
| **Signal-to-noise** | Moderate | Variable |

## Signal Characteristics

### fMRI
- Measures blood oxygenation changes via [[bold-signal]]
- neurovascular-coupling introduces ~6 second hemodynamic delay
- Correlates with local field potentials (LFPs) per [[nikos-logothetis]]
- Excellent for spatial localization of networks

### EEG
- Measures summed postsynaptic potentials
- Direct reflection of neural activity
- Volume conduction blurs spatial source localization
- Excellent for capturing fast dynamics and oscillations

## Whole-Brain Modeling Applications

### fMRI Strengths
- **Network topology**: Resting-state networks clearly spatially resolved
- **Structural-functional correspondence**: Direct comparison with DTI connectivity
- **Clinical translation**: Widely available for patient studies
- **BOLD simulation**: Well-established forward models (Balloon model)

### EEG Strengths
- **Temporal dynamics**: Captures millisecond-scale oscillations
- **Direct validation**: Neural mass models explicitly generate EEG-like signals
- **Frequency analysis**: Clear bands (alpha, beta, gamma) for model targets
- **Source localization**: Can estimate cortical generators

## Complementary Use

Optimal whole-brain modeling uses both modalities:

1. **fMRI**: Constrains spatial network organization
2. **EEG**: Validates temporal dynamics and oscillations
3. **Multimodal integration**: EEG-informed fMRI or joint modeling

## Synthesis

Neither modality alone is sufficient. fMRI provides the spatial organization that EEG lacks, while EEG provides the temporal resolution that fMRI lacks. Whole-brain models should be validated against both, with fMRI targeting network topology and EEG targeting oscillatory dynamics.

## Related Concepts
- [[fmri]] – Functional MRI
- [[eeg]] – Electroencephalography
- [[meg]] – Magnetic counterpart to EEG
- [[bold-signal]] – fMRI contrast mechanism
- neurovascular-coupling – Link between activity and BOLD
- volume-conduction – EEG signal spread
