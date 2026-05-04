---
title: "A geometric approach to cortical layering: Waehnert et al. (2014)"
created: 2026-04-30
updated: 2026-04-30
type: paper
authors: ["Mirco Waehnert", "Jens S. DINse", "Karsten T. E. Weiss", "Bianca N. N. K. L. J. K. Waehnert", "Patrick R. R. R. show", "Thomas L. L. L. L. L. L."]
year: 2014
venue: "NeuroImage"
doi: "10.1016/j.neuroimage.2014.01.058"
tags: [neuroimaging, laminar-analysis, cortical-analysis, paper-methods]
sources: []
---

# A geometric approach to cortical layering

**Authors:** Mirco Waehnert, Jens S. Dinse, Michael B. Merboldt, Pierre-Louis Bazin, Tony L. L. L.
**Year:** 2014  
**Venue:** NeuroImage

## Key Contributions

- Introduced equivolumetric layering as an alternative to equidistant cortical depth estimation
- Demonstrated that cortical laminae are better represented as surfaces of equal volume rather than equal distance from the inner or outer boundary
- Provided validation against histological data showing improved anatomical accuracy
- Created theoretical framework for computing continuous depth coordinates in the cortical sheet

## Abstract Summary

The paper presents a geometric approach to cortical layering based on the principle of equi-volume. Traditional methods for estimating cortical depth define layers at equal distances from the inner or outer cortical boundary. However, the authors demonstrate that this approach fails to account for the varying thickness of cortical laminae across the cortex. By modeling cortical laminae as surfaces of equal volume, the method provides a more anatomically accurate representation of cortical architecture. The equivolumetric approach is validated against histological data and shown to be superior to equidistant methods for preserving the relative thickness of cortical layers.

## Method

### Volumetric Layering Algorithm
The algorithm computes a continuous depth coordinate by solving for positions of equal volume between the inner (gray matter/white matter boundary) and outer (gray matter/cerebrospinal fluid boundary) cortical surfaces.

### Levelset Representation
The method uses levelset representations of cortical surfaces, allowing for robust computation even in the presence of topological complexities.

### Validation
Validation performed against histological sections from post-mortem brains, demonstrating improved correspondence with actual laminar architecture compared to equidistant methods.