# Functional Connectivity-Guided Band Selection for Motor Imagery Brain-Computer Interfaces

**Source**: arxiv
**ID**: 2605.00746
**URL**: https://arxiv.org/abs/2605.00746
**Date**: 2026-05-01
**Year**: 2026
**Authors**: Natália Araújo do Carmo, Aarthy Nagarajan
**Categories**: q-bio.NC, eess.SP, physics.optics

## Abstract

Reliable control in motor imagery brain-computer interfaces (MI-BCIs) requires the precise decoding of user-specific neural rhythms, which vary significantly across individuals. The Common Spatial Pattern (CSP) algorithm is a cornerstone of MI-BCI decoding, yet its performance depends strongly on the spectral range of the input EEG data. Although Filter Bank CSP (FBCSP) extends this as a data-driven decoding framework, its frequency sub-bands are predefined rather than selected using subject-specific physiological criteria. This paper presents a proof-of-concept study of static functional connectivity (FC)-guided band selection for MI-BCI, demonstrated using a conventional FBCSP-based pipeline. The proposed method identifies the most discriminative spectral bands by calculating phase-based connectivity across four sensorimotor channels using wPLI, PLV, and PLI. Nine bands in a 4-40 Hz filter bank are ranked by the effect size of their hemispheric coupling differences and pruned to the top K bands for feature extraction and classification via FBCSP and a Support Vector Regressor. This framework was tested for K values ranging from 1 to 8 across the BCI Competition IV-2a (n = 9) and OpenBMI (n = 54) datasets. Performance was benchmarked against standard nine-band FBCSP and random ablation to determine the minimum number of bands (K*) required to maintain accuracy within a 2% baseline equivalence zone. Results show FC-guided selection can outperform random ablation and achieve near-baseline performance while reducing required CSP fits by 22.2% to 77.8%. PLV enables the most aggressive dimensionality reduction by prioritizing the μ and low-\b{eta} ranges, while wPLI demonstrates superior inter-session robustness by mitigating volume conduction. These findings establish FC-guided selection as a principled and interpretable alternative to heuristic filter bank designs.
