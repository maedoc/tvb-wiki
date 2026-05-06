---
created: 2026-05-06
sources: []
tags:
- neuroimaging-dti
- diffusion-mri
- tractography
- models
- comparison
title: DTI vs HARDI vs NODDI
type: comparison
updated: '2026-05-06'
---

# DTI vs. HARDI vs. NODDI

[[diffusion-mri]] encompasses several modeling approaches that differ in the complexity of tissue microstructure they can resolve. Understanding these differences is essential for selecting appropriate preprocessing for [[whole-brain modeling]] and [[tractography]] pipelines.

## Overview

| Feature | DTI | HARDI/Q-Ball | NODDI |
|---------|-----|--------------|-------|
| **Acquisition** | Single-shell, few b-values | Multi-shell, many directions | Multi-shell (typically 3 shells) |
| **Model complexity** | Single tensor (6 parameters) | Orientation distribution (many parameters) | Multi-compartment (7 parameters) |
| **Crossing fibers** | Cannot resolve | Can resolve 2+ crossing directions | Resolves via compartment separation |
| **Tissue specificity** | No | No | Yes (intra-/extra-cellular, CSF) |
| **Scan time** | Short (~5 min) | Moderate (~10-15 min) | Long (~20-25 min) |
| **Clinical feasibility** | High | Moderate | Low |

## Diffusion Tensor Imaging (DTI)

DTI models water diffusion with a single 3D Gaussian (tensor). It provides three eigenvalues and eigenvectors, from which [[fractional-anisotropy]] (FA), mean diffusivity (MD), and principal diffusion direction are derived.

**Strengths:**
- Fast acquisition and processing
- Robust and well-validated biomarkers (FA, MD) in stroke, [[aging]], neurodegeneration
- Widely available on clinical scanners

**Limitations:**
- Cannot resolve crossing fibers (found in ~90% of [[white-matter]] voxels)
- Single tensor is a gross oversimplification of tissue microstructure
- Biased orientation estimates in crossing-fiber regions

**TVB relevance:** DTI-derived FA maps inform local coupling strengths in [[structural-connectivity]] matrices.

## High Angular Resolution Diffusion Imaging (HARDI / Q-Ball)

HARDI acquires diffusion-weighted images at many gradient directions and uses model-free (Q-Ball) or multi-tensor approaches to resolve complex fiber architectures.

**Strengths:**
- Resolves crossing, kissing, and fanning fiber configurations
- Model-free (Q-Ball / DSI) or constrained spherical deconvolution (CSD)
- Provides orientation distribution functions (ODFs)

**Limitations:**
- Longer scan times
- Requires more directions for accurate ODF reconstruction
- Does not directly quantify tissue compartments

**TVB relevance:** HARDI-derived ODFs enable more accurate [[tractography]], producing structural [[connectivity]] matrices with fewer false positives in crossing-fiber regions.

## Neurite Orientation Dispersion and Density Imaging (NODDI)

NODDI is a multi-compartment model that separates intra-cellular, extra-cellular, and CSF compartments, providing orientation dispersion index (ODI) and neurite density index (NDI).

**Strengths:**
- Quantifies tissue microstructure (not just diffusion shape)
- Separates intra- from extra-cellular diffusion
- ODI maps neurite orientation dispersion
- More specific to biological structure than DTI metrics

**Limitations:**
- Long acquisition and computationally intensive fitting
- Assumes simplified compartment geometries
- Parameter tradeoffs can be sensitive to acquisition design

**TVB relevance:** NODDI-derived density maps provide biologically grounded weights for structural connectivity, potentially improving the accuracy of [[whole-brain]] simulations by incorporating microstructural heterogeneity.

## Which Model for TVB?

| Application | Recommended Model | Rationale |
|-------------|-------------------|-----------|
| Clinical tractography (time-limited) | DTI + deterministic tracking | Fast, sufficient for major tracts |
| Research connectome (quality-limited) | HARDI/CSD + probabilistic tracking | Accurate crossing-fiber resolution |
| Personalized brain modeling | NODDI + CSD | Microstructure-informed connectivity weights |
| Population studies (large N) | DTI | Feasible at scale |

## Relationship to TVB

All three approaches feed into TVB's structural connectivity pipeline:
- **DTI**: Fast, clinical-feasible connectivity for population studies
- **HARDI**: Accurate connectivity for personalized modeling
- **NODDI**: Microstructure-informed weights for biologically realistic simulations

## Software Implementations

These models are implemented across multiple [[neuroimaging]] packages:
- [[mrtrix3]] — CSD, multi-tissue CSD, [[sift]]
- [[dipy]] — DTI, DKI, CSD, NODDI in Python
- [[fsl]] — BedpostX (crossing-fiber model)
- [[qsiprep]] — Automated preprocessing pipeline supporting all three

## References

- Basser et al. (1994) — Original DTI paper
- Tuch et al. (2002) — HARDI / Q-Ball introduction
- Zhang et al. (2012) — NODDI framework