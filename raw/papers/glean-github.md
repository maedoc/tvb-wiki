---
title: "GLEAN: Group Level Exploratory Analysis of Networks"
created: 2026-04-30
updated: 2026-04-30
type: paper
authors: ["Adam Baker", "Giles Colclough", "Mark Woolrich", "Romesh Abeysuriya", "Vidaurre"]
year: 2015
venue: "Software"
doi: ""
tags: [software-eeg, software-meg, neuroimaging-eeg, neuroimaging-meg, functional-connectivity, paper-methods]
sources: []
---

# GLEAN: Group Level Exploratory Analysis of Networks

**Authors:** Adam Baker, Giles Colclough, Mark Woolrich, Romesh Abeysuriya, Vidaurre  
**Year:** 2015  
**Venue:** Software (OHBA Analysis Toolbox)  
**Repository:** https://github.com/OHBA-analysis/GLEAN

## Key Contributions

GLEAN is a MATLAB toolbox for identifying patterns of covariation from M/EEG band-limited power using Hidden Markov Models (HMM) or Independent Component Analysis (ICA). The pipeline is designed for group-level analysis of resting-state electrophysiology data, enabling comparative analysis between clinical populations and healthy controls.

## Technical Overview

GLEAN operates on source-reconstructed M/EEG data, extracting band-limited power time courses in distinct frequency bands (theta, alpha, beta, gamma). The HMM approach models the brain as transitioning between discrete states characterized by distinct patterns of band-limited power across brain regions. The ICA approach identifies spatially independent patterns of covariation without imposing sequential structure.

### Dependencies

- **SPM12**: GLEAN is built on top of the SPM12 framework (Statistical Parametric Mapping) for source reconstruction and preprocessing. The software leverages SPM's beamforming capabilities for MEG/EEG source localization and its established pipeline for data preprocessing (filtering, artifact rejection, etc.). See Litvak et al. (2011) for SPM4/12 EEG-MEG analysis capabilities. SPM12 is available at: https://www.fil.ion.ucl.ac.uk/spm/software/spm12/

- **HMM-MAR Toolbox**: The Hidden Markov Model - Multivariate Autoregressive (HMM-MAR) toolbox developed by OHBA provides the underlying estimation routines for the HMM functionality in GLEAN. This toolbox implements the spectrally resolved HMM approach described in Vidaurre et al. (2016), which operates on band-limited power time courses rather than raw amplitude data. The HMM-MAR toolbox is available at: https://github.com/OHBA-analysis/HMM-MAR

### Band-Limited Power Methodology

The band-limited power approach in GLEAN involves:
1. Source reconstruction using beamforming or minimum norm estimation
2. Band-pass filtering in user-specified frequency bands (theta: 4-8 Hz, alpha: 8-12 Hz, beta: 12-30 Hz, gamma: 30-100 Hz)
3. Hilbert transformation to extract analytic amplitude
4. Downsampling to create band-limited power time courses
5. Group-level decomposition using HMM or ICA

This methodology is grounded in the interpretation that band-limited power reflects the amplitude of underlying neural oscillations, which correlate with synaptic activity and are modulated by neuromodulatory systems.

## Relationship to TVB

GLEAN's data-driven network decompositions can inform whole-brain modeling approaches in [[the-virtual-brain]] by identifying frequency bands and brain regions showing strong group-level covariation. The extracted network parameters can be used to constrain TVB models or validate simulated electrophysiological dynamics against empirically observed states.

## Key References

- Baker, A. P., Colclough, G. L., Woolrich, M. W., Abeysuriya, R., & Vidaurre, D. (2015). GLEAN (Group Level Exploratory Analysis of Networks). OHBA Analysis Toolbox.

- Litvak, V., Mattout, J., Kiebel, S., Phillips, C., Henson, R., Kilner, J., ... & Friston, K. (2011). EEG and MEG data analysis in SPM4. Computational Intelligence and Neuroscience, 2011, 852961.

- Vidaurre, D., Quinn, A. J., Baker, A. P., Dupret, D., Tejero-Canizal, A., & Woolrich, M. W. (2016). Spectrally resolved fast transient brain states in electrophysiological data. Brain Structure and Function, 221(3), 1631-1648.

- Vidaurre, D., Smith, S. M., & Woolrich, M. W. (2017). A multivariate hidden Markov model for brain-state classification. IEEE Transactions on Biomedical Engineering, 64(8), 1725-1739.

- Hinczón, A. R., Quinn, A. J., Woolrich, M. W., & Brookes, M. J. (2020). A principled approach to automated quantitative analysis of resting-state magnetoencephalography. NeuroImage, 216, 116837.