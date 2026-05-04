# The IQ-Motion Confound in Multi-Site Autism fMRI May Be Inflated by Site-Correlated Measurement Uncertainty

**Source**: semantic-scholar
**ID**: f8f4fac8055cb89250a31b4b5722f7a9e8447de0
**URL**: https://www.semanticscholar.org/paper/f8f4fac8055cb89250a31b4b5722f7a9e8447de0
**Date**: 2026-04-14
**Year**: 2026
**Authors**: K. Soliman
**Citations**: 0

## Abstract

Multi-site autism neuroimaging studies routinely control for the confound between full-scale IQ and head motion by regressing framewise displacement against IQ scores and removing shared variance. This procedure assumes that ordinary least squares (OLS) provides an unbiased estimate of the confound magnitude. We tested this assumption on the ABIDE-I phenotypic dataset (n=935 subjects across 19 international scanning sites) using Probability Cloud Regression, an errors-in-variables (EIV) estimator that models per-observation measurement uncertainty in both variables. IQ measurement error was derived from published Wechsler test-retest reliability coefficients; response-side uncertainty was represented by a site-level proxy equal to the within-site standard deviation of mean framewise displacement. Three findings emerged. First, OLS overestimates the IQ-motion slope by a factor of 4.67 relative to the EIV-corrected estimate when the bias factor is computed from the full-precision fitted coefficients (OLS -0.00125, EIV -0.00027 mm per IQ point after rounding for display). Second, under leave-site-out cross-validation a single pooled predictor of raw FD produces negative out-of-sample R^2 at all 19 sites (overall R^2 = -0.074), indicating that the pooled predictor does not transport cleanly across sites once site information is removed. Third, the direction of the EIV-corrected slope is robust across all 64 configurations of an 8x8 sensitivity grid spanning 12-fold ranges of each noise parameter. These results suggest that pooled OLS may overstate the IQ-motion association in ABIDE-I, but direct downstream consequences for motion-correction pipelines remain to be quantified using raw motion traces and connectivity-level re-analysis. Formal EIV methods appear to remain uncommon in multi-site neuroimaging confound estimation.
