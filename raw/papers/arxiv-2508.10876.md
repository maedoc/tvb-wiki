# Accelerating cosmological inference of interacting dark energy with neural emulators

**Source**: semantic-scholar
**ID**: 2f13c96447c2e0aacf14afb36b116645e75b5e83
**URL**: https://www.semanticscholar.org/paper/2f13c96447c2e0aacf14afb36b116645e75b5e83
**Date**: 2025-08-14
**Year**: 2025
**Authors**: Karim Carrion
**Citations**: 0

## Abstract

The present thesis aims to tackle two critical aspects of present and future cosmological analysis of Large-Scale Structure (LSS): accurate modelling of the nonlinear matter power spectrum beyond $\Lambda$CDM, and efficient computational techniques for Bayesian parameter estimation. Both are crucial for testing alternative cosmologies and avoiding spurious results. We focus on the Dark Scattering (DS) model, describing pure momentum transfer between dark matter -- dark energy through the parameter $A_{\rm ds}$. To capture DS effects, we adopt the halo model reaction framework within $\tt{ReACT}$, compute the nonlinear DS spectrum, and validate it against $N$-body simulations. We further include baryonic feedback and massive neutrinos, finding degeneracies between DS and baryonic effects but not with neutrinos. We then constrain DS using cosmic shear from KiDS-1000, accelerated by neural emulators from $\tt{CosmoPower}$, which speed up predictions by $\mathcal{O}(10^4)$. Our DS emulator, trained on halo model reaction outputs, preserves percent-level accuracy and incorporates baryonic feedback. Analysing KiDS shear statistics, we obtain $\vert A_{\rm ds}\vert \lesssim 20$ b/GeV at $68 \%$ C.L. Combining KiDS with Planck CMB and BAO data, we find $A_{\rm ds}=10.6^{+4.5}_{-7.3}$ b/GeV at $68 \%$ C.L., suggesting the DS model as a promising resolution to the $S_8$ tension. Finally, we present weak lensing forecasts for Stage IV surveys using an automatically differentiable pipeline with $\tt{jax-cosmo}$ and gradient-based samplers in $\tt{NumPyro}$, reducing computational cost from months on CPUs to days on GPUs. Model evidence is evaluated with $\tt{harmonic}$ under multiple scale cuts. To put things into perspective, the modelling strategies and machine learning accelerations developed here provide powerful tools for the next generation of LSS cosmology.
