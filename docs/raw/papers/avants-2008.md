---
title: "Symmetric diffeomorphic image registration with cross-correlation"
created: 2026-04-20
updated: 2026-04-20
type: source
tags: [paper-methods, software-ants, neuroimaging-processing, brain-network, structural-connectivity]
sources: []
---

# Symmetric diffeomorphic image registration with cross-correlation

**Authors**: Avants et al. (2008)
**Journal**: Medical Image Analysis
**DOI**: https://doi.org/10.1016/j.media.2007.06.004
**Full text**: https://doi.org/10.1016/j.media.2007.06.004

## Summary

Avants and colleagues introduce SyN (Symmetric Normalization), a diffeomorphic deformable image registration algorithm that optimizes a symmetric energy function to produce unbiased, invertible mappings between image pairs. By using cross-correlation as the similarity metric, SyN achieves robust performance on intra-modal brain MRI registration tasks including atlas construction and longitudinal change detection. The symmetric formulation eliminates the template-bias inherent in asymmetric registration approaches. SyN, as implemented in the ANTs toolkit, consistently ranks among the top-performing algorithms in independent evaluations and has become a standard method for brain MRI normalization.

## Key Contributions

- SyN (Symmetric Normalization) algorithm
- Diffeomorphic deformable image registration
- Unbiased, invertible mappings
- Cross-correlation similarity metric
- Template-bias elimination

## Related Entities

- [[ANTs]]
- [[Brian Avants]]
