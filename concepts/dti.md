---
title: DTI
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [neuroimaging-dti, diffusion-imaging, structural-connectivity]
sources: [raw/papers/basser-1994.md, raw/papers/mori-1999.md, raw/papers/jones-2010.md]
---

# DTI

Diffusion Tensor Imaging (DTI) is an MRI technique that measures the diffusion of water molecules to characterize tissue microstructure, particularly white matter fiber orientation.

## Definition

DTI models water diffusion using a 3x3 tensor that describes diffusion rates in all directions. In white matter, water diffuses more freely along axons than perpendicular to them (anisotropic diffusion), revealing fiber orientations.

## Key Metrics

| Metric | Description |
|--------|-------------|
| FA (Fractional Anisotropy) | 0 (isotropic) to 1 (fully anisotropic) |
| MD (Mean Diffusivity) | Average diffusion rate |
| AD (Axial Diffusivity) | Diffusion along principal axis |
| RD (Radial Diffusivity) | Diffusion perpendicular to axis |

## Role in Whole-Brain Modeling

DTI is the primary source of [[structural-connectivity]] data for whole-brain models:

1. **Connectivity matrices**: [[tractography]] algorithms trace white matter pathways to create region-to-region connectivity weights
2. **Network topology**: The pattern of connections constrains model dynamics
3. **Individual variability**: Subject-specific DTI enables personalized models

## Limitations

- **Crossing fibers**: Single tensor cannot resolve multiple fiber orientations per voxel
- **Validation**: Tractography accuracy varies by region
- **Resolution**: Limited by voxel size (typically 2-3 mm)

## Advanced Methods

- **CSD** (constrained-spherical-deconvolution): Resolves crossing fibers (tournier-2007)
- **HARDI**: High angular resolution diffusion imaging
- **Multi-shell**: Multiple b-values for better tissue modeling

## Related Concepts
- [[diffusion-mri]] – Broader category including DTI
- [[tractography]] – Fiber tracking from DTI data
- [[structural-connectivity]] – Anatomical connections
- white-matter – Myelinated axon tracts
