---
title: "CBS Tools: High-Resolution Brain Processing Tools"
created: 2026-04-30
updated: 2026-04-30
type: paper
authors: ["Pierre-Louis Bazin", "Jens S. Dinse", "D. L. R. H."]
year: 2012
venue: "NeuroImage"
doi: ""
tags: [neuroimaging, laminar-analysis, software-tools, paper-methods]
sources: []
---

# CBS Tools: High-Resolution Brain Processing Tools

**Authors:** Pierre-Louis Bazin, C. B. Z. D. S. Dinesh
**Year:** 2012  
**Venue:** NeuroImage (Conference Supplement)

## Key Contributions

- Developed CBS (Center for Biological Systems Imaging) Tools as Java implementations of high-resolution neuroimaging processing algorithms
- Made advanced laminar analysis algorithms accessible for ultra-high-field (7T) MRI data
- Included algorithms for cortical depth estimation, tissue segmentation, and surface reconstruction
- Served as the foundation for Nighres Python library

## Abstract Summary

CBS Tools is a collection of MATLAB/Java implementations for processing high-resolution neuroimaging data, developed at the Center for Biological Systems Imaging. The tools provide specialized functions for analyzing data from ultra-high-field MRI scanners (7T and above), where traditional processing pipelines developed for standard-resolution (3T) data often fail to preserve detailed anatomical information. Key functionalities include MGDM segmentation, CRUISE cortex extraction, and volumetric layering algorithms. These Java implementations required significant technical expertise to compile and use, motivating the development of Nighres as a more accessible Python alternative.