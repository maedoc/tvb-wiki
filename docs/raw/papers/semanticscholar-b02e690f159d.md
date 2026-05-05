# Fast EEG/MEG BEM-based forward problem solution for high-resolution head models

**Source**: semantic-scholar
**ID**: b02e690f159df03162b33f16c340118b15d15bca
**DOI**: 10.1016/j.neuroimage.2024.120998
**URL**: https://www.semanticscholar.org/paper/b02e690f159df03162b33f16c340118b15d15bca
**Date**: 2025-01-01
**Year**: 2025
**Authors**: W. Wartman, Guillermo Nuñez Ponasso, Z. Qi, J. Haueisen, B. Maess, T. Knösche, K. Weise, G. Noetscher, T. Raij, S. Makaroff
**Venue**: NeuroImage
**Citations**: 9

## Abstract

A fast BEM (boundary element method) based approach is developed to solve an EEG/MEG forward problem for a modern high-resolution head model. The method utilizes a charge-based BEM accelerated by the fast multipole method (BEM-FMM) with an adaptive mesh pre-refinement method (called b-refinement) close to the singular dipole source(s). No costly matrix-filling or direct solution steps typical for the standard BEM are required; the method generates on-skin voltages as well as MEG magnetic fields for high-resolution head models within 90 s after initial model assembly using a regular workstation. The forward method is validated by comparison against an analytical solution on a spherical shell model as well as comparison against a full h-refinement method on realistic 1M facet human head models, both of which yield agreement to within 5 % for the EEG skin potential and MEG magnetic fields. The method is further applied to an EEG source localization (inverse) problem for real human data, and a reasonable source dipole distribution is found.
