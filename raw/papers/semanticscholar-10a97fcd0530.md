# Data-driven emulation of modal aerosol microphysics via neural operator-based modeling

**Source**: semantic-scholar
**ID**: 10a97fcd0530da65d1a73d7fb95751c5b2ac0fc1
**DOI**: 10.1038/s41598-025-33209-x
**URL**: https://www.semanticscholar.org/paper/10a97fcd0530da65d1a73d7fb95751c5b2ac0fc1
**Date**: 2025-12-26
**Year**: 2025
**Authors**: Z. Bai, Damian W. I. Rouson
**Venue**: Scientific Reports
**Citations**: 1

## Abstract

The complexity and the small characteristic scales of aerosol microphysical processes pose a big challenge for accurate and efficient Earth system simulations at regional and global scales. In this work, we construct and evaluate a surrogate model: the aerosol deep operator network (ADON), a physics-inspired dual-net architecture for emulating the aerosol microphysics parameterization suite in the version 2 of the Energy Earth System Model (E3SMv2). The current version of the surrogate model is trained on a dataset comprising 9.8 million samples obtained from a global E3SMv2 simulation with the horizontal resolution of about one degree under cloud-free conditions. Incorporating domain spatial and temporal coordinates, as well as principle components extracted from training data, the dual-net surrogate model effectively captures the intricate representations of aerosol and the relationship with atmospheric state variables, achieving an R-squared score over \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$95.7\%$$\end{document} for all the lognormal aerosol modes in the extrapolated regime. The validated model provides feature importance of input variables and their impact on the predictive capacity of the surrogate model in relation to the E3SM. The computational cost of online inference time deployed on CPUs and GPUs with lower precisions highlights ADON’s efficiency and potential in robust predictive modeling for large-scale Earth system computations.
