# End-to-end Cortical Surface Reconstruction from Clinical Magnetic Resonance Images

**Source**: semantic-scholar
**ID**: 0d1e37498294df066cbb4c3c8294581611d655d6
**DOI**: 10.48550/arXiv.2505.14017
**URL**: https://www.semanticscholar.org/paper/0d1e37498294df066cbb4c3c8294581611d655d6
**Date**: 2025-05-20
**Year**: 2025
**Authors**: J. D. Nielsen, Karthik Gopinath, Andrew Hoopes, A. Dalca, C. Magdamo, Steve Arnold, Sudeshna Das, A. Thielscher, J. E. Iglesias, O. Puonti
**Venue**: MLMI@MICCAI
**Citations**: 0

## Abstract

Surface-based cortical analysis is valuable for a variety of neuroimaging tasks, such as spatial normalization, parcellation, and gray matter (GM) thickness estimation. However, most tools for estimating cortical surfaces work exclusively on scans with at least 1 mm isotropic resolution and are tuned to a specific magnetic resonance (MR) contrast, often T1-weighted (T1w). This precludes application using most clinical MR scans, which are very heterogeneous in terms of contrast and resolution. Here, we use synthetic domain-randomized data to train the first neural network for explicit estimation of cortical surfaces from scans of any contrast and resolution, without retraining. Our method deforms a template mesh to the white matter (WM) surface, which guarantees topological correctness. This mesh is further deformed to estimate the GM surface. We compare our method to recon-all-clinical (RAC), an implicit surface reconstruction method which is currently the only other tool capable of processing heterogeneous clinical MR scans, on ADNI and a large clinical dataset (n=1,332). We show a approximately 50 % reduction in cortical thickness error (from 0.50 to 0.24 mm) with respect to RAC and better recovery of the aging-related cortical thinning patterns detected by FreeSurfer on high-resolution T1w scans. Our method enables fast and accurate surface reconstruction of clinical scans, allowing studies (1) with sample sizes far beyond what is feasible in a research setting, and (2) of clinical populations that are difficult to enroll in research studies. The code is publicly available at https://github.com/simnibs/brainnet.
