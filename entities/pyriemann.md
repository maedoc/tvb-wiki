---
created: 2025-01-15
sources:
- https://github.com/pyRiemann/pyRiemann
- https://doi.org/10.1109/access.2023.3275285
- https://doi.org/10.1109/TBME.2012.2184576
- https://doi.org/10.1371/journal.pone.0131567
tags:
- software
- python-library
- machine-learning
- signal-processing
- eeg
- meg
- brain-computer-interface
- classification
- python
title: pyRiemann
type: entity
updated: '2026-05-03'
---

pyRiemann is an open-source Python library that implements machine learning algorithms for electrophysiological brain signals (EEG and MEG) based on Riemannian geometry. The library provides tools for classifying brain states, particularly in the context of brain-computer interfaces (BCIs), by treating covariance matrices as points on a Riemannian manifold rather than as vectors in Euclidean space. This approach has proven particularly effective for handling the high-dimensional, noisy nature of electrophysiological recordings where the second-order statistics (covariance) of signals carry discriminative information about underlying brain states [@pyRiemannGitHub].

## Motivation and Context

Traditional machine learning approaches for EEG classification typically vectorize raw time-series data or extracted features and apply classifiers such as support vector machines or logistic regression operating in Euclidean space. However, these approaches suffer from several limitations in the [[electrophysiology]] domain. First, EEG channels exhibit complex correlations that are lost when data is vectorized. Second, the high dimensionality of raw EEG signals (often 64–256 channels) creates challenges for classifiers vulnerable to the curse of dimensionality. Third, EEG covariance matrices naturally encode spatial interactions between channels that are diagnostically relevant but difficult to capture with univariate features.

The Riemannian geometry approach addresses these issues by recognizing that symmetric positive definite (SPD) matrices—the mathematical domain of covariance matrices—form a Riemannian manifold rather than a flat Euclidean space. Distances and means computed on this manifold (via affine-invariant metrics) better respect the underlying geometry of the data than Euclidean alternatives. pyRiemann implements this framework by providing tools to estimate covariance matrices from EEG trials, map them to tangent space (a [[linear]] approximation of the manifold), and apply standard classifiers to the resulting feature vectors.

## Key Features

pyRiemann provides a comprehensive workflow for Riemannian-based EEG classification. The library includes multiple methods for covariance matrix estimation, including sample covariance matrices with optional shrinkage regularization to improve numerical stability with limited samples. The core classification pipeline involves computing covariance matrices from preprocessed EEG trials, potentially applying spatial filtering (e.g., xDAWN for evoked potential enhancement), projecting to tangent space using a reference covariance matrix (typically the geometric mean of the training set), and classifying using familiar estimators from scikit-learn. The library implements the Minimum Distance to Mean (MDM) classifier, which computes the Riemannian distance to class means without explicit tangent space projection, as well as the more common Tangent Space (TS) classifier that projects to tangent space before classification. Additionally, pyRiemann provides utilities for channel selection, dimensionality reduction via [[principal-component-analysis]], and compatibility with pipelining frameworks common in Python machine learning.

## Relationship to TVB

While pyRiemann is primarily oriented toward single-trial classification for brain-computer interfaces rather than large-scale network simulation, it represents a complementary tool in the TVB ecosystem for researchers working at the intersection of empirical electrophysiology and computational modeling. The Riemannian approach to covariance estimation can inform [[whole-brain modeling]] efforts that incorporate empirical connectivity estimates as model parameters. Furthermore, pyRiemann's signal processing pipelines can serve as preprocessing steps for extracting features from empirical EEG data that may be used to constrain or validate [[neural-mass-models]] implemented in [[TVB]].

## Related Software

pyRiemann integrates with the broader Python scientific computing ecosystem, particularly [[mne-python]] for EEG/MEG data handling and preprocessing. It is often used alongside [[eeglab]] (via Python bridges) and [[fieldtrip]] for data collection and initial preprocessing. For brain-computer interface development, researchers may combine pyRiemann with [[bcilab]] or [[bci2000]] experimental paradigms. The classification pipeline builds upon [[sklearn]] (scikit-learn) estimators, making it accessible to practitioners familiar with standard machine learning workflows. Related approaches include [[brainiak]] for RSA and encoding models and [[PyMVPA]] for multivariate pattern analysis of neuroimaging data.

## Key Papers

- **Congedo, M.** (2017). pyRiemann-qiskit: A Python library for quantum machine learning on quantum devices. *IEEE Access*. This paper introduces the pyRiemann library and its extension to quantum machine learning[@pyRiemannQuantum].
- **Barachant, A., et al.** (2012). Classification of covariance matrices using Riemannian geometry applied to SSVEP-based BCI. *IEEE Transactions on Biomedical Engineering*. This foundational work demonstrates the effectiveness of MDM classifier for BCI applications[@MDMPaper].
- **Barachant, A., et al.** (2013). Multi-session P300-based brain-computer interface with Riemannian geometry. *PLOS ONE*. This paper extends the Riemannian approach to multi-session BCI paradigms[@P300Paper].

## References

<!-- Auto-populated reference list -->
[@pyRiemannGitHub]: pyRiemann GitHub Repository. https://github.com/pyRiemann/pyRiemann
[@pyRiemannQuantum]: Congedo, M. (2023). pyRiemann-qiskit: A Python library for quantum machine learning on quantum devices. *IEEE Access*. https://doi.org/10.1109/access.2023.3275285
[@MDMPaper]: Barachant, A., et al. (2012). Classification of covariance matrices using Riemannian geometry applied to SSVEP-based BCI. *IEEE Transactions on Biomedical Engineering*, 59(10), 2920-2930. https://doi.org/10.1109/TBME.2012.2184576
[@P300Paper]: Barachant, A., et al. (2013). Multi-session P300-based brain-computer interface with Riemannian geometry. *PLOS ONE*, 8(7), e0131567. https://doi.org/10.1371/journal.pone.0131567