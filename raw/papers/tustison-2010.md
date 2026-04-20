---
title: "N4ITK: improved N3 bias correction"
created: 2026-04-20
updated: 2026-04-20
type: source
tags: [paper-methods, software-ants, neuroimaging-processing, neuroimaging-mri]
sources: []
---

# N4ITK: improved N3 bias correction

**Authors**: Tustison et al. (2010)
**Journal**: IEEE Transactions on Medical Imaging
**DOI**: https://doi.org/10.1109/TMI.2010.2046908
**Full text**: https://doi.org/10.1109/TMI.2010.2046908

## Summary

This paper presents N4ITK, a substantially improved reimplementation of the widely used N3 MRI bias field correction algorithm within the ITK framework. N4ITK replaces the original histogram sharpening approach with an iterative B-spline fitting procedure that offers faster convergence, greater robustness to noise, and improved accuracy across diverse field strengths and coil configurations. The open-source implementation integrates naturally into ITK- and ANTs-based pipelines. N4ITK has become the de facto standard preprocessing step for MRI intensity non-uniformity correction in neuroimaging workflows worldwide.

## Key Contributions

- Improved N3 bias field correction algorithm
- B-spline fitting for faster convergence
- Greater robustness to noise
- Improved accuracy across field strengths
- De facto standard for MRI preprocessing

## Related Entities

- [[ANTs]]
- [[Nick Tustison]]
