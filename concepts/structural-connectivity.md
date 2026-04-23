---
created: 2026-04-20
sources:
- raw/papers/basser-1994.md
- raw/papers/mori-1999.md
- raw/papers/jones-2010.md
- raw/papers/sotiropoulos-zalesky-2019.md
- raw/papers/arxiv-2603.21032.md
- raw/papers/honey-2009.md
- raw/papers/arxiv-2603.21067.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-27108cae3f6e.md
tags:
- structural-connectivity
- neuroimaging-dti
- diffusion-imaging
- connectomics
title: Structural Connectivity
type: concept
updated: '2026-04-23'
---

# Structural Connectivity

Structural connectivity refers to the anatomical connections between brain regions, typically represented as white matter fiber tracts that enable communication between neuronal populations.

## Definition

Structural connectivity is the physical "wiring diagram" of the brain, comprising axonal fiber bundles that connect gray matter regions. Unlike [[functional-connectivity]] (statistical dependencies), structural connectivity reflects actual anatomical pathways.

## Measurement Methods

### In Vivo (Human)
- **DTI** (diffusion-tensor-imaging): Most common method
- **Tractography**: Algorithmic reconstruction of fiber pathways
- **Limitations**: Indirect measurement, crossing fiber challenges

### Ex Vivo (Animal)
- **Tracer injections**: Gold standard for directionality
- **Histology**: Myelin staining, axonal tracing
- **Limitations**: Invasive, not applicable to humans

## Connectome Construction

From diffusion MRI to connectivity matrix:

1. **Parcellation**: Divide brain into regions (e.g., Desikan-Killiany, AAL)
2. **Tractography**: Track fibers between regions
3. **Weighting**: Count streamlines, FA, or other metrics
4. **Matrix**: N×N matrix of connection weights

## Role in Whole-Brain Modeling

Structural connectivity is a primary input to whole-brain models:

1. **Connection weights**: Determine coupling strength between regions
2. **Network topology**: Small-world, rich-club organization affects dynamics
3. **Delays**: Fiber lengths determine signal transmission delays
4. **Individual variability**: Subject-specific SC enables personalized models

## Key Properties

- **Sparsity**: ~20-30% of possible connections exist
- **Small-world**: High clustering, short path lengths
- **Rich-club**: Hubs densely interconnected
- **Modularity**: Community structure

## Related Concepts
- [[functional-connectivity]] – Statistical dependencies
- [[effective-connectivity]] – Causal interactions
- [[connectome]] – Complete connectivity map
- [[tractography]] – Fiber tracking methods
- [[dti]] – Primary measurement method
- white-matter – Myelinated fiber tracts