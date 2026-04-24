Done. Updated `dynamic-causal-modeling.md` with a condensed, schema-compliant rewrite (~790 words).

**What changed:**
- **Restructured** from ~1150 words to the 500–800 target while retaining all technical depth
- **Opening paragraph** now gives a plain definition of DCM and its scope (fMRI/EEG/MEG) before any equations
- **Motivation & Context** contrasts DCM with [[functional-connectivity]] and [[structural-connectivity]], situates it within the [[free-energy-principle]], and cites the three key source papers
- **Mathematical formulation** explains the bilinear state equation (A/B/C matrices) and the modality-specific observation models (Balloon/[[bold-signal]] for fMRI, lead-field for EEG/MEG) with prose around each equation
- **Bayesian inference** covers variational Laplace, free-energy bounds, and fixed-effects vs. random-effects model selection
- **DCM Variants** merged into a single dense section covering deterministic fMRI, stochastic, EEG/MEG ([[jansen-rit]], [[wilson-cowan]]), and spectral [[resting-state]] DCM
- **Relationships & Biological Grounding** contrasts DCM with Granger causality, notes identifiability limits, and maps parameters to physiology (synaptic efficacy, neuromodulation, vascular reactivity) with clinical links to [[epilepsy-modeling]] and TVB
- **Wikilinks:** 20 outbound links to existing pages
- **Tags:** all 15 tags validated against the taxonomy
- **Log:** appended to `log.md` under `## 2026-04-24`

File: `dynamic-causal-modeling.md`
