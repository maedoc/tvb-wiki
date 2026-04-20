# PRISM: Differentiable Analysis-by-Synthesis for Fixel Recovery in Diffusion MRI

**arXiv ID**: 2604.00250
**Published**: 2026-03-31
**Updated**: 2026-03-31
**Authors**: Mohamed Abouagour, Atharva Shah, Eleftherios Garyfallidis
**Categories**: cs.CV
**URL**: https://arxiv.org/abs/2604.00250
**PDF**: https://arxiv.org/pdf/2604.00250
**Source**: arXiv

## Abstract

Diffusion MRI microstructure fitting is nonconvex and often performed voxelwise, which limits fiber peak recovery in narrow crossings. This work introduces PRISM, a differentiable analysis-by-synthesis framework that fits an explicit multi-compartment forward model end-to-end over spatial patches. The model combines cerebrospinal fluid (CSF), gray matter, up to K white-matter fiber compartments (stick-and-zeppelin), and a restricted compartment, with explicit fiber directions and soft model selection via repulsion and sparsity priors. PRISM supports a fast MSE objective and a Rician negative log-likelihood (NLL) that jointly learns sigma without oracle information. A lightweight nuisance calibration module (smooth bias field and per-measurement scale/offset) is included for robustness and regularized to identity in clean-data tests. On synthetic crossing-fiber data (SNR=30; five methods, 16 crossing angles), PRISM achieves 3.5 degrees best-match angular error with 95% recall, which is 1.9x lower than the best baseline (MSMT-CSD, 6.8 degrees, 83% recall); in NLL mode with learned sigma, error drops to 2.3 degrees with 99% recall, resolving crossings down to 20 degrees. On the DiSCo1 phantom (NLL mode), PRISM improves connectivity correlation over CSD baselines at all four tracking angles (best r=.934 at 25 degrees vs. .920 for MSMT-CSD). Whole-brain HCP fitting (~741k voxels, MSE mode) completes in ~12 min on a single GPU with near-identical results across random seeds.
