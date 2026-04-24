---
title: Tractography
created: 2026-04-20
updated: 2026-04-24
type: concept
tags: [neuroimaging-dti, diffusion-imaging, tractography, structural-connectivity, paper-methods]
sources: [raw/papers/mori-1999.md, raw/papers/jones-2010.md, raw/papers/tournier-2007.md]
---

Tractography is a computational method for reconstructing white matter fiber pathways from diffusion MRI data, enabling non-invasive mapping of structural brain connectivity. By analyzing the directionality of water diffusion in brain tissue, tractography algorithms trace virtual "streamlines" through diffusion orientation fields to reconstruct the three-dimensional trajectories of white matter fiber bundles. This technique represents one of the few available methods for inferring anatomical connectivity in living humans, making it indispensable for whole-brain modeling and connectomics research.

## Historical Context and Motivation

The development of tractography emerged from the need to map structural brain connectivity without invasive techniques. Prior to diffusion MRI, anatomical connectivity could only be studied through post-mortem dissection or invasive tracing techniques in animal models. The seminal work by [[susumu-mori]] in 1999 introduced the first tractography algorithm, demonstrating three-dimensional fiber tracking in the brain using diffusion tensor imaging (DTI) data. This breakthrough enabled researchers to visualize white matter pathways in vivo and opened the door for quantitative analysis of brain structural networks.

The motivation for tractography in the context of whole-brain modeling is particularly significant. [[whole-brain]] models require structural connectivity matrices that define the anatomical links between brain regions. These matrices serve as the foundational architecture upon which dynamic models of neural activity are built. Without accurate structural connectivity estimates, models cannot reliably predict brain dynamics or simulate neural disorders. The accuracy of tractography directly constrains the predictive power of whole-brain models, making methodological improvements in tractography broadly relevant to computational neuroscience.

## Technical Methods

### Deterministic Tracking

Deterministic tractography follows the principal diffusion direction at each voxel to generate streamlines. The [[fiber-assignment-by-continuous-tracking]] (FACT) algorithm, introduced in the original Mori 1999 paper, represents one of the earliest and most widely used deterministic approaches. In this method, streamlines are propagated by stepping along the primary eigenvector of the diffusion tensor at each location, with termination criteria based on curvature thresholds or fractional anisotropy values. Deterministic methods are computationally efficient and straightforward to implement, making them popular for clinical applications. However, they are particularly sensitive to noise in the diffusion data and struggle in regions where fiber pathways cross, branch, or merge, as the single-tensor model can only represent one fiber orientation per voxel.

### Probabilistic Tracking

Probabilistic tractography addresses some limitations of deterministic methods by accounting for uncertainty in the diffusion orientation estimates. Rather than following a single path, these methods generate thousands of potential streamlines sampled from probability distributions over fiber orientations. Bootstrap-based approaches resample the raw diffusion data to estimate distributions of fiber directions, while Bayesian methods incorporate prior anatomical information. Probabilistic tractography is more robust to noise and can resolve crossing fibers more reliably, though at the cost of significantly increased computational requirements and more complex interpretation of results.

### Advanced Techniques

The introduction of constrained spherical deconvolution (CSD) by [[tournier-2007]] represented a major advance in resolving complex fiber configurations. Unlike DTI, which models diffusion with a single tensor and can only capture one primary fiber orientation, CSD estimates a fiber orientation distribution (FOD) that can represent multiple fiber populations within a single voxel. This innovation dramatically improved tractography accuracy in regions with crossing fibers, such as the centrum semiovale and brainstem. Additional advanced approaches include global tractography methods that optimize entire tractograms simultaneously rather than tracking individual streamlines, and anatomically-constrained tractography (ACT) that uses tissue segmentation to ensure streamlines remain within white matter boundaries.

## Limitations and Challenges

Despite significant methodological advances, tractography remains subject to notable limitations that affect its reliability for whole-brain modeling. The challenge of crossing fibers remains fundamental to diffusion MRI-based approaches, as even CSD can struggle with complex fiber geometries involving more than two or three crossing populations. Validation of tractography results in vivo remains extremely difficult, as ground truth anatomical connectivity is rarely available for human subjects. The [[jones-2010]] paper comprehensively reviews these challenges, emphasizing that tractography provides estimates of anatomical connectivity that must be interpreted cautiously.

False positive and false negative streamlines represent persistent concerns. Spurious streamlines can appear due to noise, partial volume effects, or limitations in the diffusion model, while genuine connections may be missed when fiber orientations are poorly estimated. These errors propagate into structural connectivity matrices used in models, potentially leading to incorrect conclusions about brain network organization. Best practices include quality control of diffusion data, appropriate parameter selection, and careful interpretation of results in the context of known limitations.

## Role in Whole-Brain Modeling

Tractography produces the [[structural-connectivity]] matrices that serve as essential inputs to [[whole-brain]] models. These matrices define which brain regions are anatomically connected, the strength of those connections (typically derived from streamline counts or fractional anisotropy values), and the geometry of the network. Connection weights derived from tractography directly influence model dynamics, affecting synchronization patterns, seizure propagation, and other emergent phenomena.

The quality of tractography-derived connectivity matrices has profound implications for model predictions. In personalized brain modeling, individual tractography data enables patient-specific connectivity estimates that can inform clinical predictions. Software packages such as [[mrtrix3]], [[dipy]], and [[fsl]] provide tractography tools integrated with whole-brain modeling frameworks. The [[human-connectome-project]] has established standardized protocols for acquiring high-quality diffusion MRI data that enable reproducible tractography across research sites. Understanding both the capabilities and limitations of tractography is therefore essential for anyone constructing or interpreting whole-brain models derived from diffusion MRI data.

## Related Concepts

- [[dti]] – Diffusion tensor imaging, the foundational technique for tractography
- [[diffusion-mri]] – Broader imaging category encompassing DTI and advanced methods
- [[structural-connectivity]] – Output of tractography used in whole-brain models
- [[connectomics]] – The study of complete neural wiring diagrams
- [[whole-brain]] – Modeling approaches that incorporate structural connectivity
