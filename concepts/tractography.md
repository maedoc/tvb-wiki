---
created: 2026-04-20
sources:
- raw/papers/mori-1999.md
- raw/papers/jones-2010.md
- raw/papers/tournier-2007.md
- raw/papers/sotiropoulos-zalesky-2019.md
- raw/papers/arxiv-2602.18715.md
- raw/papers/arxiv-2510.20148.md
- raw/papers/semanticscholar-929b90566fc8.md
tags:
- tractography
- neuroimaging-dti
- diffusion-imaging
- structural-connectivity
title: Tractography
type: concept
updated: '2026-04-23'
---

# Tractography

Tractography is a computational method for reconstructing white matter fiber pathways from diffusion MRI data, enabling non-invasive mapping of structural brain connectivity.

## Definition

Introduced by susumu-mori in 1999, tractography algorithms trace virtual "streamlines" through diffusion orientation fields to reconstruct the 3D trajectories of white matter fiber bundles.

## Methods

### Deterministic
- **Streamline tracking**: Follow principal diffusion direction
- **FACT**: Fiber Assignment by Continuous Tracking
- Fast but sensitive to noise and crossing fibers

### Probabilistic
- **Account for uncertainty**: Multiple possible pathways
- **Bootstrap**: Resample data to estimate distributions
- More robust but computationally intensive

### Advanced
- **CSD-based**: Use FOD from constrained spherical deconvolution
- **Global**: Optimize whole-brain tractograms simultaneously
- **Anatomically-constrained**: Use tissue boundaries to constrain tracking

## Challenges and Limitations

- **Crossing fibers**: Single tensor methods fail (constrained-spherical-deconvolution helps)
- **Validation**: Difficult to verify in vivo
- **False positives**: Spurious streamlines
- **False negatives**: Missed connections

## Role in Whole-Brain Modeling

Tractography produces the [[structural-connectivity]] matrices used as model inputs:

1. **Connection weights**: Streamline counts or FA values
2. **Fiber lengths**: For computing transmission delays
3. **Network topology**: Pattern of connections

## Quality Considerations

jones-2010 discusses validation challenges and best practices. Quality affects model reliability.

## Related Concepts
- [[dti]] – Diffusion tensor imaging
- [[diffusion-mri]] – Broader imaging category
- [[structural-connectivity]] – Output of tractography
- constrained-spherical-deconvolution – Advanced fiber resolution
- white-matter – Target tissue