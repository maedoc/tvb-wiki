---
created: 2026-04-20
sources:
- raw/papers/niedermeyer-silva-2004.md
- raw/papers/nunez-srinivasan-2006.md
- raw/papers/makeig-1996.md
- raw/papers/cohen-2014.md
- raw/papers/arxiv-2511.09243.md
- raw/papers/arxiv-2512.07842.md
- raw/papers/semanticscholar-cc2129666e15.md
- raw/papers/arxiv-2411.16449.md
- raw/papers/arxiv-2603.29903.md
tags:
- neuroimaging-eeg
- brain-oscillations
title: EEG
type: concept
updated: '2026-04-23'
---

# EEG

Electroencephalography (EEG) is a non-invasive method for recording electrical activity of the brain via electrodes placed on the scalp. It provides millisecond-resolution measurements of neural dynamics.

## Definition

EEG measures summed electrical activity from populations of neurons, primarily reflecting synchronous postsynaptic potentials in pyramidal cells oriented perpendicular to the cortical surface. The signal is attenuated and blurred by volume conduction through the brain, CSF, skull, and scalp.

## Characteristics

| Feature | Typical Value |
|---------|---------------|
| Temporal resolution | 1-10 ms |
| Spatial resolution | ~1-10 cm (scalp) |
| Frequency range | 0.1-100 Hz |
| Amplitude | 10-100 μV |

## Frequency Bands

- **Delta (0.5-4 Hz)**: Deep sleep, unconsciousness
- **Theta (4-8 Hz)**: Drowsiness, memory, meditation
- **Alpha (8-13 Hz)**: Relaxed wakefulness, visual cortex
- **Beta (13-30 Hz)**: Active thinking, motor planning
- **Gamma (30-100 Hz)**: Conscious perception, binding

## Role in Whole-Brain Modeling

EEG is a primary output measure for [[neural-mass-model]] validation:

1. **Forward problem**: Model-generated LFPs are transformed to scalp potentials via volume-conduction equations
2. **Frequency content**: Models must reproduce empirical power spectra and oscillatory patterns
3. **Connectivity**: Phase relationships and coherence between regions provide validation targets

[[neural-mass-model]]s like [[jansen-rit]] and [[wilson-cowan]] explicitly generate EEG-like signals from population firing rates.

## Analysis Methods

- **Time-frequency analysis**: Wavelets, Hilbert transform (cohen-2014)
- **Source localization**: Estimating intracranial sources from scalp data
- **Independent Component Analysis (ICA)**: Separating mixed signals (makeig-1996)
- **Connectivity analysis**: Phase locking, coherence, Granger causality

## Comparison with Other Modalities

| Modality | Temporal | Spatial | Signal Source |
|------------|----------|---------|---------------|
| EEG | ~1 ms | ~1 cm | Electrical potentials |
| MEG | ~1 ms | ~0.5 cm | Magnetic fields |
| fMRI | ~1 s | ~3 mm | Hemodynamic response |

## Related Concepts
- [[meg]] – Magnetic counterpart with better spatial resolution
- [[fmri]] – Complementary hemodynamic measure
- [[neural-mass-model]] – Generate EEG-like outputs
- volume-conduction – Physics of signal spread
- source-localization – Estimating brain sources
- brain-oscillations – Rhythmic neural activity