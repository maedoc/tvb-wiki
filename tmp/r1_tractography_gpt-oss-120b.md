---
title: Tractography
created: 2026-04-20
updated: 2026-04-24
type: concept
tags: [neuroimaging-dti, structural-connectivity, whole-brain-modeling]
sources: [raw/papers/mori-1999.md, raw/papers/jones-2010.md, raw/papers/tournier-2007.md]
---

# Tractography

Tractography is a computational technique that reconstructs the three‑dimensional trajectories of white‑matter fiber bundles from diffusion‑weighted magnetic resonance imaging (dMRI) data. By following the local orientation of water diffusion, tractography yields a structural connectivity matrix that can be used in whole‑brain models such as the [[the-virtual-brain]] and other [[tvb]]‑based simulations.

## Motivation and Context

Understanding how distant cortical and subcortical regions are linked by axonal pathways is fundamental for network neuroscience and for building biophysically realistic brain models. Traditional histological tract tracing is invasive and limited to post‑mortem tissue, whereas diffusion MRI provides a non‑invasive, whole‑brain view of white‑matter architecture in living subjects. The emergence of tractography in the late 1990s (Mori *et al.*, 1999) therefore opened the door to large‑scale, subject‑specific structural connectomes that can be integrated with functional data from [[fMRI]] or electrophysiology.

Beyond merely visualizing fiber bundles, tractography supplies quantitative descriptors—streamline counts, average fractional anisotropy (FA), and estimated fiber lengths—that are essential inputs for multimodal whole‑brain simulators. Projects such as the [[human-connectome-project]] and the UK Biobank increasingly rely on tractography pipelines (e.g., [[mrtrix3]] and [[mrtrix3-connectome]]) to produce reproducible connectome datasets for population‑level modelling.

## Technical Foundations

### Diffusion Modelling

Early tractography used the diffusion tensor model (DTI), which assumes a single dominant fiber orientation per voxel. The tensor’s principal eigenvector defines the local tract direction, but this simplification fails in regions with crossing, kissing, or fanning fibers. The seminal work of Tournier *et al.* (2007) introduced constrained spherical deconvolution (CSD), which estimates a fiber orientation distribution (FOD) that can represent multiple orientations within a voxel, dramatically improving tract reconstruction in complex white‑matter regions.

### Tracking Strategies

| Strategy | Core Idea | Strengths | Limitations |
|----------|-----------|-----------|-------------|
| **Deterministic (e.g., Streamline, FACT)** | Propagate a streamline by following the most likely orientation (principal eigenvector or peak FOD) from seed to termination criteria. | Fast, intuitive visualisation, easy to implement. | Highly sensitive to noise; cannot capture uncertainty; prone to premature termination at crossing zones. |
| **Probabilistic** | Sample from the orientation distribution at each step, generating many possible streamlines per seed; yields a probability map of connectivity. | Accounts for measurement uncertainty; better at detecting tenuous connections. | Computationally intensive; results depend on sampling parameters; may inflate false‑positive rates. |
| **Global / Anatomically‑Constrained** | Optimise an entire tractogram simultaneously (e.g., global tractography) or restrict tracking to biologically plausible tissue masks (GM/WM/CSF) using anatomical priors. | Reduces spurious streamlines; produces more coherent whole‑brain reconstructions. | Requires higher-quality data and more sophisticated pipelines; longer runtimes. |

Deterministic tracking often uses a step size of 0.5–1 mm and stops when FA falls below a threshold (e.g., 0.2) or when curvature exceeds a preset angle (e.g., 45°). Probabilistic methods typically generate 500–5000 samples per seed voxel, and the resulting connectivity matrix reflects the proportion of samples that reach a target region.

### From Streamlines to Connectivity Matrices

Once a tractogram is obtained, it is discretised according to a parcellation (e.g., the [[aal-atlas]] or the [[desikan‑killiany-atlas]]). The number of streamlines intersecting each pair of parcels forms the **structural weight**; mean FA or mean diffusivity can serve as edge attributes. Fiber lengths are computed as the Euclidean or geodesic length of each streamline, providing transmission delay estimates for neural mass models. These matrices are the primary inputs for the [[whole-brain]] simulation framework and for neuroinformatics tools such as the [[brain-connectivity-toolbox]].

## Relationships to Other Methods

Tractography builds on earlier diffusion‑tensor imaging techniques and predates more recent multi‑shell acquisitions that enable higher‑order models (e.g., neurite orientation dispersion and density imaging). While DTI provides a convenient scalar summary of anisotropy, CSD‑based tractography (implemented in tools like [[dipy]] and [[mrtrix3]]) yields more accurate reconstructions, particularly in regions with crossing fibers. Probabilistic frameworks such as those in [[fsl]]’s *PROBTRACKX* complement deterministic pipelines by quantifying confidence in inferred pathways.

In the broader landscape, tractography differs from functional connectivity estimation (e.g., correlations of [[bold-signal]] or electrophysiological signals) and from effective connectivity approaches like [[dynamic-causal-modeling]], which aim to infer directional influences rather than anatomical pathways. Nevertheless, all these modalities converge in whole‑brain models where structural scaffolds constrain the dynamics generated by neural‑mass or spiking models.

## Biological Grounding and Limitations

Although tractography provides an indispensable approximation of axonal architecture, it remains an indirect inference. The method assumes that water diffusion follows the orientation of axonal bundles, yet factors such as edema, partial volume effects, and non‑Gaussian diffusion can bias estimates. Validation against histological tracers or post‑mortem dissections is challenging, and false‑positive streamlines (spurious connections) are a well‑known issue (Jones, 2010). Moreover, streamline counts do not linearly translate to actual axon numbers, and fiber density estimates can be confounded by microstructural heterogeneity.

Despite these caveats, tractography’s ability to generate subject‑specific, whole‑brain structural maps has transformed computational neuroscience. By feeding anatomically plausible connectivity into simulators such as the [[tvb]] and the [[whole-brain-simulators]], researchers can explore how variations in white‑matter topology shape emergent brain rhythms, seizure propagation, and the effects of stimulation.

## Quality Assurance and Best Practices

Jones (2010) outlines several recommendations that are now standard practice:

1. **High angular resolution diffusion imaging (HARDI)** or multi‑shell protocols to support advanced models like CSD.  
2. **Rigorous preprocessing** (eddy current correction, susceptibility distortion correction) using pipelines such as [[qsiprep]] or [[fmriprep]] adapted for diffusion.  
3. **Anatomically constrained tracking** with tissue segmentation from T1‑weighted images (e.g., via [[fsl]] or [[freesurfer]]).  
4. **Cross‑validation** with independent datasets or paired tracer studies when available.  
5. **Transparent reporting** of tracking parameters, seed densities, and threshold settings to facilitate reproducibility.

Adhering to these guidelines improves the reliability of structural matrices and, consequently, the predictive power of whole‑brain models.

---
