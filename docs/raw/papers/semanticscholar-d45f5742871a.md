# ER-detect: a pipeline for robust detection of early evoked responses in BIDS-iEEG electrical stimulation data.

**Source**: semantic-scholar
**ID**: d45f5742871acf3189e5a2e1cfd894fffd716e36
**DOI**: 10.1016/j.jneumeth.2025.110389
**URL**: https://www.semanticscholar.org/paper/d45f5742871acf3189e5a2e1cfd894fffd716e36
**Date**: 2025-02-01
**Year**: 2025
**Authors**: M. A. van den Boom, Nicholas M. Gregg, G. Valencia, B. Lundstrom, K. J. Miller, D. van Blooijs, G. Huiskamp, F. Leijten, G. Worrell, Dora Hermes
**Venue**: Journal of Neuroscience Methods
**Citations**: 1

## Abstract

BACKGROUND
Human brain connectivity can be measured in different ways. Intracranial EEG (iEEG) measurements during single pulse electrical stimulation provide a unique way to assess the spread of electrical information with millisecond precision. However, the methods used for the detection of responses in cortico-cortical evoked potential (CCEP) data vary across studies, from visual inspection with manual annotation to a variety of automated methods.


NEW METHOD
To provide a robust workflow to process CCEP data and detect early evoked responses in a fully automated and reproducible fashion, we developed the Early Response (ER)-detect toolbox. ER-detect is an open-source Python package and Docker application to preprocess BIDS structured iEEG data and detect early evoked CCEP responses. ER-detect can use three early response detection methods, which were validated against 14 manually annotated CCEP datasets from two different clinical sites by four independent raters.


RESULTS
and comparison with existing methods: ER-detect's automated detection performed on par with the inter-rater reliability (Cohen's Kappa of ~0.6). Moreover, ER-detect was optimized for processing large CCEP datasets, to be used in conjunction with other connectomic investigations.


CONCLUSION
ER-detect provides a highly efficient standardized workflow such that iEEG-BIDS data can be processed in a consistent manner and enhance the reproducibility of CCEP based connectivity results for both research and clinical purposes.
