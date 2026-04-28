# An Automatic Pipeline for Simultaneous EEG-FMRI Artifact-removal (SEFA)

**Source**: semantic-scholar
**ID**: a31e278722813aa600c34a0c2b0fdbc803540b5e
**DOI**: 10.1109/ICBME68496.2025.11392189
**URL**: https://www.semanticscholar.org/paper/a31e278722813aa600c34a0c2b0fdbc803540b5e
**Date**: 2025-11-19
**Year**: 2025
**Authors**: Farid Hosseinzadeh, A. M. Mohammadi, Mehrdad Anvarifard, Sasan Keshavarz, E. Ebrahimzadeh, H. Soltanian-Zadeh
**Venue**: Iranian Conference on Biomedical Engineering
**Citations**: 0

## Abstract

Simultaneous EEG-fMRI provides complementary temporal and spatial information about brain function, but its utility is hindered by severe scanner-induced artifacts such as gradient and ballistocardiographic (BCG) noise. Manual artifact correction is effective but laborintensive, inconsistent, and difficult to scale. We introduce SEFA, a fully automated two-stage preprocessing pipeline for simultaneous EEG-fMRI that integrates MRI-specific artifact correction (average artifact subtraction, optimal basis set, and PCA/OBS modeling) with state-of-the-art EEG cleaning techniques adapted from a previous popular standard EEG preprocessing pipeline, HAPPE, including automated independent component classification (MARA and ICLabel), bad-channel detection, multitaper regression for line noise, and segment-level quality control. Validation against manually corrected datasets from a reward-based decision-making task demonstrated that SEFA achieves near-perfect equivalence with expert preprocessing. Event-related potentials (ERPs) from both approaches exhibited indistinguishable morphology, latency, and amplitude, with mean channel-wise correlations of $\mathrm{r}=0.91 \pm 0.14$, and 72 % of electrodes exceeding $\mathrm{r}>0.90$. Signal-to-noise ratio (SNR) improved from $\sim 0.8 \text{dB}$ in raw data to 6.7 dB with SEFA, matching manual performance (6.9 dB). Statistical testing confirmed no significant differences in ERP amplitude or latency between automated and manual methods (all $\mathrm{p} > \text{0.1}$). By reducing operator bias and cutting processing time from hours to minutes, SEFA enables reproducible, scalable, and clinically feasible preprocessing of simultaneous EEG-fMRI data.
