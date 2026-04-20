# Recovering Whole-Brain Causal Connectivity under Indirect Observation with Applications to Human EEG and fMRI

**arXiv ID**: 2602.09034
**Published**: 2026-01-30
**Updated**: 2026-01-30
**Authors**: Sangyoon Bae, Miruna Oprescu, David Keetae Park, Shinjae Yoo, Jiook Cha
**Categories**: q-bio.NC, cs.AI
**URL**: https://arxiv.org/abs/2602.09034
**PDF**: https://arxiv.org/pdf/2602.09034
**Source**: arXiv

## Abstract

Inferring directed connectivity from neuroimaging is an ill-posed inverse problem: recorded signals are distorted by hemodynamic filtering and volume conduction, which can mask true neural interactions. Many existing methods conflate these observation artifacts with genuine neural influence, risking spurious causal graphs driven by the measurement process. We introduce INCAMA (INdirect CAusal MAmba), a latent-space causal discovery framework that explicitly accounts for measurement physics to separate neural dynamics from indirect observations. INCAMA integrates a physics-aware inversion module with a nonstationarity-driven, delay-sensitive causal discovery model based on selective state-space sequences. Leveraging nonstationary mechanism shifts as soft interventions, we establish identifiability of delayed causal structure from indirect measurements and a stability bound that quantifies how inversion error affects graph recovery. We validate INCAMA on large-scale biophysical simulations across EEG and fMRI, where it significantly outperforms standard pipelines. We further demonstrate zero-shot generalization to real-world fMRI from the Human Connectome Project: without domain-specific fine-tuning, INCAMA recovers canonical visuo-motor pathways (e.g., $V1 \to V2$ and $M1 \leftrightarrow S1$) consistent with established neuroanatomy, supporting its use for whole-brain causal inference.
