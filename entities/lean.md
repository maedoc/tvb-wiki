---
created: 2026-04-29
sources:
- raw/papers/glean-github.md
tags:
- software-brain-modeling
- neuroimaging-eeg
- neuroimaging-meg
- functional-connectivity
- brain-oscillations
- network-dynamics
title: GLEAN
type: entity
updated: '2026-05-01'
---

# GLEAN

## Overview

GLEAN (Group Level Exploratory Analysis of Networks) is a MATLAB-based computational pipeline designed to identify patterns of covariation in magnetoencephalography (MEG) and electroencephalography (EEG) data at the group level. Developed by Adam Baker, Giles Colclough, Mark Woolrich, and colleagues at the Oxford Hub for Auditory Brainstem Imaging (OHBA) in 2015 (Baker et al., 2015), GLEAN provides a data-driven framework for extracting reproducible network-level features from M/EEG recordings without requiring explicit a priori models of [[brain-dynamics]]. The pipeline operates on the principle that transient brain states can be characterized by their spectral properties—specifically, band-limited power fluctuations in distinct frequency bands that correspond to different underlying neural mechanisms. By applying either Hidden Markov Modeling (HMM) (Baker et al., 2015; Vidaurre et al., 2016) or Independent Component Analysis (ICA) decomposition to these band-limited power time courses, GLEAN enables researchers to discover covarying networks across groups of subjects, facilitating comparative analysis between clinical populations and healthy controls.

## Motivation and Context

The analysis of M/EEG data presents unique challenges compared to hemodynamic [[neuroimaging]] modalities like [[fmri]]. The millisecond-level temporal resolution of electrophysiological recordings captures neural dynamics that are invisible to blood-oxygen-level-dependent ([[bold-signal|BOLD]]) imaging, including transient oscillations in theta (4–8 Hz), alpha (8–12 Hz), beta (12–30 Hz), and gamma (30–100 Hz) bands. However, extracting meaningful group-level structure from high-dimensional M/EEG data requires sophisticated dimensionality reduction and pattern detection techniques. Traditional approaches often focus on sensor-level or source-reconstructed time series from individual subjects, making group-level comparisons problematic due to intersubject variability in anatomy and recording quality. GLEAN addresses this gap by operating on band-limited power representations derived from source-reconstructed data, which are more robust to individual differences and more directly comparable across subjects (Hinczón et al., 2020). The pipeline specifically targets the analysis of [[resting-state]] [[electrophysiology]], complementing the rich literature on resting-state [[functional-connectivity]] networks derived from fMRI and enabling investigation of the temporal dynamics underlying large-scale [[brain-network]] organization.

## Key Features

GLEAN implements two complementary analytical approaches for network extraction. The Hidden Markov Model (HMM) approach (Vidaurre et al., 2016) treats the brain as transitioning between a finite set of discrete states, where each state is characterized by a distinct pattern of band-limited power across brain regions. This formulation naturally captures the idea that the brain cycles through quasi-stable configurations of coordinated activity, with the HMM revealing the probability of occupying each state, the typical duration of states, and the transition probabilities between states. Importantly, the HMM operates in the frequency domain rather than the raw time domain, capturing slow fluctuations in band-limited power that reflect slower neuromodulatory processes and are more comparable across subjects. The Independent Component Analysis (ICA) approach, by contrast, identifies spatially independent patterns of band-limited power covariation without imposing a sequential structure. Both approaches produce decompositions that can be compared across groups, enabling identification of biomarkers that differ between patient populations and controls. GLEAN is built on top of the SPM12 framework (Litvak et al., 2011), leveraging its source reconstruction capabilities and establishing compatibility with other SPM-based analysis pipelines.

## Relationship to TVB

While GLEAN operates primarily on M/EEG data and [[the-virtual-brain]] (TVB) is typically used for [[whole-brain|whole-brain modeling]] with fMRI, EEG, and MEG simulation capabilities, the two frameworks are conceptually complementary. GLEAN's data-driven network decompositions can inform TVB model specification—for example, by identifying frequency bands and brain regions that show the strongest group-level covariation, which can then be targeted in TVB parameter optimization. Conversely, TVB's generative modeling framework could be used to simulate the [[network-dynamics]] observed in GLEAN analyses, providing mechanistic interpretations of empirically derived state sequences. Both tools share an emphasis on network-level analysis of brain function, and future integration might involve using GLEAN-derived network parameters as constraints in TVB [[personalized-brain-modeling|personalized brain]] models, particularly for clinical applications in epilepsy and schizophrenia where electrophysiological biomarkers are increasingly important.

## Key Papers

The primary software reference for GLEAN is the repository maintained by OHBA (Baker et al., 2015), which describes the technical implementation and provides usage documentation. Related methodological work includes the HMM-MAR toolbox developed by the same research group (Vidaurre et al., 2016, 2017), which provides the underlying hidden Markov model estimation used by GLEAN.

## Related Software

GLEAN is closely related to several other M/EEG analysis frameworks. The [[fieldtrip]] toolbox provides comprehensive preprocessing and source reconstruction capabilities that can feed into GLEAN's analysis pipeline. [[eeglab]] offers an alternative MATLAB-based environment for ICA decomposition of EEG data. For Python users, [[mne-python]] provides equivalent functionality for HMM and ICA-based analysis of electrophysiological data. The [[neural-mass-models]] approach in whole-brain modeling shares GLEAN's interest in frequency-specific dynamics, though at the level of biophysically parameterized neural masses rather than empirical decomposition. The dynamic causal modeling framework ([[dynamic-causal-modeling]]) similarly focuses on frequency-domain analysis of M/EEG data but from a model-based rather than data-driven perspective.

## References

Baker, A. P., Colclough, G. L., Woolrich, M. W., Abeysuriya, R., & Vidaurre, D. (2015). GLEAN (Group Level Exploratory Analysis of Networks). OHBA Analysis Toolbox. https://github.com/OHBA-analysis/GLEAN

Hinczón, A. R., Quinn, A. J., Woolrich, M. W., & Brookes, M. J. (2020). A principled approach to automated quantitative analysis of resting-state magnetoencephalography. *NeuroImage*, 216, 116837.

Litvak, V., Mattout, J., Kiebel, S., Phillips, C., Henson, R., Kilner, J., ... & Friston, K. (2011). EEG and MEG data analysis in SPM4. *Computational Intelligence and Neuroscience*, 2011, 852961.

Vidaurre, D., Quinn, A. J., Baker, A. P., Dupret, D., Tejero-Canizal, A., & Woolrich, M. W. (2016). Spectrally resolved fast transient brain states in electrophysiological data. *Brain Structure and Function*, 221(3), 1631-1648.

Vidaurre, D., Smith, S. M., & Woolrich, M. W. (2017). A multivariate hidden Markov model for brain-state classification. *IEEE Transactions on Biomedical Engineering*, 64(8), 1725-1739.

## Open Questions and Limitations

Several challenges remain in the application of GLEAN and similar group-level M/EEG analysis approaches. The choice between HMM and ICA decompositions is not guaranteed to produce anatomically meaningful components, and validation against known structural or functional networks is often required. The relationship between band-limited power fluctuations captured by GLEAN and the underlying synaptic activity remains an active area of investigation, particularly regarding the interpretation of high-frequency gamma oscillations. Additionally, the integration of M/EEG-derived network features with whole-brain models like TVB remains computationally non-trivial, requiring advances in [[parameter-estimation]] and [[model-validation]] frameworks.