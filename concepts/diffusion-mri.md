---
created: 2026-04-20
sources:
- raw/papers/basser-1994.md
- raw/papers/jones-2010.md
- raw/papers/sotiropoulos-zalesky-2019.md
- raw/papers/semanticscholar-deecd9987645.md
- raw/papers/arxiv-2602.09852.md
- raw/papers/arxiv-2602.18715.md
- raw/papers/arxiv-2603.29903.md
- raw/papers/arxiv-2510.20148.md
tags:
- diffusion-imaging
- structural-connectivity
- neuroimaging-dti
title: Diffusion MRI
type: concept
updated: '2026-04-23'
---

# Diffusion MRI

Diffusion MRI (dMRI) encompasses MRI techniques that measure the diffusion of water molecules to probe tissue microstructure. It is the primary method for non-invasive mapping of white matter architecture in vivo.

## Definition

Diffusion MRI applies diffusion-sensitizing gradients to measure how water molecules move within tissue. The rate and direction of diffusion reveal tissue properties, particularly in white matter where water diffusion is constrained by axonal membranes and myelin sheaths.

## Methods

### DTI (Diffusion Tensor Imaging)
- Single tensor model per voxel
- Limited to one fiber orientation
- Fast acquisition and processing

### Advanced Methods
- **CSD** (constrained-spherical-deconvolution): Multiple fiber orientations
- **DSI** (Diffusion Spectrum Imaging): Full diffusion probability distribution
- **NODDI**: Neurite orientation dispersion and density imaging

## Connectome Construction

Diffusion MRI enables [[connectome]] mapping through:

1. **Preprocessing**: Denoising, distortion correction, registration
2. **Fiber orientation estimation**: Tensor or spherical deconvolution models
3. **Tractography**: Streamline tracking through orientation fields
4. **Connectivity matrix**: Counting streamlines between regions

## Role in Whole-Brain Modeling

Diffusion-derived structural connectivity is a primary input to whole-brain models:

- **Connection weights**: Number of streamlines or fractional anisotropy
- **Connection lengths**: Tractography-derived distances
- **Network topology**: Small-world, rich-club properties

## Challenges

- **Validation**: Difficult to verify in vivo
- **Crossing fibers**: Complex architectures challenge simple models
- **Partial volume**: Multiple tissue types in single voxels
- **Biological interpretation**: Relationship to axonal properties

## Related Concepts
- [[dti]] – Basic diffusion tensor method
- [[tractography]] – Fiber tracking algorithms
- [[structural-connectivity]] – Anatomical connections
- [[connectome]] – Complete connectivity map
- white-matter – Myelinated fiber tracts