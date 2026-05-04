# Optimization of Weak Lensing Lightcone Simulations for Higher-Order Statistics in the LSST era

**Source**: arxiv
**ID**: 2605.00821
**URL**: https://arxiv.org/abs/2605.00821
**Date**: 2026-05-01
**Year**: 2026
**Authors**: J. Mena-Fernández, C. Doux, J. Harnois-Déraps, K. Heitmann, C. Combet, P. Larsen, N. Frontiere, A. Bera, S. Samario-Nava, L. Castiblanco, C. Uhlemann, the LSST Dark Energy Science Collaboration
**Categories**: astro-ph.CO

## Abstract

We present a framework for generating lightcone simulations tailored to the analysis of Stage-IV cosmic shear data using Higher-Order Statistics (HOS). We revisit key design choices from previous simulation campaigns and re-optimize several internal parameters, benchmarking accuracy through changes in $χ^2$ of cosmic shear statistics under survey conditions mimicking 10 years of observations from the Legacy Survey of Space and Time (LSST). We find that discretizing the lightcone uniformly in scale factor yields higher accuracy than commonly adopted schemes such as uniform spacing in redshift or comoving distance. While $N_{\rm part} = 1024^3$ simulation particles (corresponding to a mass resolution of $m_{\rm part} = 2.08\times10^{10}M_\odot$) is sufficient to model two-point statistics up to $\ell = 5000$, we observed significant instabilities on our full suite of HOS as the number of mass shells used in the lightcone construction, $N_{\rm shells}$, is varied. In contrast, simulations with $N_{\rm part} = 2048^3$ particles ($m_{\rm part} = 2.60\times10^{9}M_\odot$) robustly reproduce all statistics considered. In this higher-resolution configuration, $N_{\rm shells}$ can be reduced to $\sim50$ with only minor deviations, no larger than $0.1-0.3σ$ relative to our highest-resolution case ($N_{\rm shells}\sim100$). This has been explicitly verified through a comparison between our fiducial lightcone production mode based on slicing particle snapshots and an exact lightcone mode where individual particle trajectories are solved for at runtime. We further show that the particle density per pixel can be downsampled by a significant amount for $z>1.5$, saving large computational resources with no impact on the resulting statistics. These results guide the design of upcoming simulation campaigns geared towards forward-modeling and emulation-based analyses of Stage-IV data.
