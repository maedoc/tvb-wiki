---
title: Limo
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software-modeling, neuroimaging-eeg, neuroimaging-meg, statistical-analysis, eeglab]
sources: [https://onlinelibrary.wiley.com/doi/10.1155/2011/831409, https://www.sciencedirect.com/science/article/pii/S0165027003003769, https://eeglab.org/plugins/limo/]
---

# Limo

## Overview

Limo (Linear Modeling) is a MATLAB-based toolbox for the statistical analysis of electroencephalography (EEG) and magnetoencephalography (MEG) data. The toolbox implements mass univariate linear modeling approaches, allowing researchers to perform voxel-based or vertex-based analyses across the entire scalp or cortical surface. Limo provides a comprehensive framework for estimating linear models at each electrode or source location separately, enabling the detection of spatio-temporal patterns of neural activity related to experimental conditions, cognitive processes, or clinical markers (Pernet et al., 2011). The tool is designed to integrate seamlessly with [[eeglab]], one of the most widely used open-source environments for EEG and MEG data processing, making it accessible to the broad neuroimaging community.

## Key Features

Limo implements several key functionalities that distinguish it from traditional ERP analysis approaches. The toolbox supports **mass univariate testing**, where a separate statistical test is performed at each electrode or source location, providing fine-grained spatio-temporal resolution of neural effects without the need for a priori region-of-interest selection. This approach is particularly valuable in exploratory analyses where the spatial distribution of effects is unknown (Pernet et al., 2011). Limo provides implementations of **General Linear Model (GLM)** analysis for both categorical (e.g., condition contrasts) and continuous (e.g., behavioral correlations) predictors, allowing flexible modeling of experimental designs ranging from simple A/B comparisons to complex mixed-effects layouts.

The toolbox incorporates rigorous approaches to **multiple comparisons correction**, implementing cluster-based permutation tests, false discovery rate (FDR) control, and family-wise error rate (FWER) adjustments using bootstrap resampling methods (Maris & Oostenveld, 2007). These corrections are essential given the thousands of tests performed across electrodes and time points. Limo also supports **time-frequency decomposition** using wavelet or Hilbert transform methods, enabling the analysis of oscillatory activity in different frequency bands (delta, theta, alpha, beta, gamma) and the relationship between phase and amplitude across these bands. The toolbox handles both **between-subject and within-subject designs**, with options for random effects modeling and mixed-design analyses.

A distinguishing feature of Limo is its implementation of **hierarchical linear modeling**, which separates within-subject (trial-level) variance from between-subject variance. At the first level, GLM parameters are estimated for each subject at each time point and electrode. At the second level, these parameters are integrated across subjects to test for population-level effects (Pernet et al., 2011). This two-stage approach mirrors the methods long established in fMRI analysis (Friston et al., 2007) but is specifically adapted to the high-dimensional nature of electrophysiological data.

## Relationship to TVB

While Limo operates primarily in the analysis domain rather than forward modeling, it maintains important connections to whole-brain simulation frameworks like [[the-virtual-brain]]. Both tools share a commitment to **computational modeling** of brain activity—TVB simulates large-scale network dynamics using neural mass models, while Limo provides the statistical inverse methods needed to **parameterize such models from empirical data**. In practice, researchers using TVB for personalized brain modeling often employ Limo (or similar EEG/MEG analysis toolboxes like [[fieldtrip]] or [[eeglab]] directly) to extract empirical features—such as ERP amplitudes, oscillation power spectra, or connectivity estimates—that serve as targets for model fitting and parameter estimation. The relationship is thus complementary: Limo enables the data-driven characterization of individual brain dynamics that TVB then reproduces in silico.

Limo also supports the broader workflow of **functional connectivity** analysis, computing correlation-based or coherence-based measures that can inform the construction of whole-brain connectomes. These connectivity estimates, typically derived from resting-state or task-based EEG/MEG recordings, can be used to define the **structural connectivity** matrices that constrain TVB simulations. Additionally, the toolbox's source localization capabilities, when combined with head models from techniques like boundary-element-method or finite-element-method, provide the cortical activity estimates needed for comparison with TVB forward predictions.

## Key Papers

The Limo toolbox was formally introduced by Pernet and colleagues at the University of Edinburgh and University of Glasgow. The primary methodological publication is **"LIMO EEG: A Toolbox for Hierarchical LInear MOdeling of ElectroEncephaloGraphic Data"** (Pernet, Chauveau, Gaspar, & Rousselet, 2011), published in *Computational Intelligence and Neuroscience*. This paper describes the theoretical framework, implementation, and validation of the toolbox, including the hierarchical GLM approach and robust bootstrap-based statistical inference.

The toolbox builds on the mass univariate analysis philosophy pioneered in the fMRI community, particularly through the work of Friston and colleagues (Kiebel & Friston, 2004; Friston et al., 2007). Key methodological publications establishing the statistical framework for mass univariate EEG analysis include Maris and Oostenveld (2007) on nonparametric statistical testing for EEG/MEG data, and Kilner, Kiebel, and Friston (2005) on applications of random field theory to electrophysiology.

The toolbox has been applied in numerous studies of cognitive neuroscience, including research on **working memory**, **attention**, **perception**, and **clinical populations** such as patients with schizophrenia or epilepsy (Rousselet et al., 2008, 2009). Several validation studies have demonstrated Limo's ability to recover known experimental effects from simulated and empirical EEG data, providing confidence in its statistical inference procedures.

## Technical Implementation

Limo operates on EEG/MEG data structured in the EEGLAB format, expecting data matrices organized as channels × time points × trials (or epochs). The basic workflow involves first **preprocessing** the data using EEGLAB functions (filtering, artifact rejection, epoching), then specifying the linear model design matrix with condition codes and potential covariates. The core estimation procedure fits a GLM at each electrode or source location using ordinary least squares (OLS), iteratively reweighted least squares (IRLS) for robust estimation, or weighted least squares (WLS) for heteroscedastic data. For repeated-measures designs, mixed-effects approaches are available. Test statistics are computed for relevant contrasts (e.g., condition A vs. condition B), and p-values are adjusted for the multiple tests performed across the spatio-temporal domain using cluster-based bootstrap methods (Pernet et al., 2011).

The toolbox stores results in structured formats that integrate with EEGLAB's data visualization functions, enabling the creation of scalp maps, topographic animations, and butterfly plots showing significant time windows. Output includes both raw test statistics and p-value maps, allowing researchers to set custom thresholds or visualize the full statistical landscape. Limo's modular architecture allows researchers to customize individual analysis steps—using custom preprocessing pipelines, alternative GLM estimators, or novel multiple comparison corrections—while maintaining compatibility with the core analysis framework.

## Related Software

Limo belongs to a broader ecosystem of EEG/MEG analysis tools that share similar philosophical commitments to mass univariate analysis and open-source distribution. **[[eeglab]]** provides the primary integration platform, including the data structures, visualization tools, and preprocessing pipelines that Limo extends (Delorme & Makeig, 2004). **[[fieldtrip]]**, developed at the Donders Institute, offers comparable mass univariate capabilities with additional features for source analysis and beamforming, representing the main alternative to Limo for EEG/MEG statistical modeling (Oostenveld et al., 2011). **[[mne-python]]** provides a Python-based alternative implementing similar functionality, with growing adoption in the research community.

Within the TVB ecosystem, Limo's output can inform **[[parameter-estimation]]** procedures and **[[model-validation]]** workflows, where empirical EEG features derived from Limo are compared against simulated activity. Tools for **[[connectivity]]** estimation such as **[[eegnet]]** or **[[sift]]** complement Limo's analysis by providing frequency-domain and information-theoretic connectivity measures.

---

## References

- Delorme, A., & Makeig, S. (2004). EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. *Journal of Neuroscience Methods*, 134(1), 9-21.

- Friston, K. J., Ashburner, J., Kiebel, S. J., Nichols, T. E., & Penny, W. D. (Eds.). (2007). *Statistical Parametric Mapping: The Analysis of Functional Brain Images*. Academic Press.

- Kiebel, S. J., & Friston, K. J. (2004). Statistical parametric mapping for event-related potentials: I. Generic considerations. *NeuroImage*, 22(2), 492-502.

- Kilner, J. M., Kiebel, S. J., & Friston, K. J. (2005). Applications of random field theory to electrophysiology. *Neuroscience Letters*, 374(3), 174-178.

- Maris, E., & Oostenveld, R. (2007). Nonparametric statistical testing of EEG- and MEG-data. *Journal of Neuroscience Methods*, 164(1), 177-190.

- Oostenveld, R., Fries, P., Maris, E., & Schoffelen, J. M. (2011). FieldTrip: Open source software for advanced analysis of MEG, EEG, and invasive electrophysiological data. *Computational Intelligence and Neuroscience*, 2011, 156869.

- Pernet, C. R., Chauveau, N., Gaspar, C., & Rousselet, G. A. (2011). LIMO EEG: A Toolbox for Hierarchical LInear MOdeling of ElectroEncephaloGraphic Data. *Computational Intelligence and Neuroscience*, 2011, 831409.

- Rousselet, G. A., Pernet, C. R., Bennett, P. J., & Sekuler, A. B. (2008). Parametric study of EEG sensitivity to phase noise during face processing. *BMC Neuroscience*, 9, 98.

- Rousselet, G. A., Husk, J. S., Pernet, C. R., Gaspar, C. M., Bennett, P. J., & Sekuler, A. B. (2009). Age-related delay in information accrual for faces: evidence from a parametric, single-trial EEG approach. *BMC Neuroscience*, 10, 114.