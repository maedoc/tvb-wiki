---
title: Tractography
created: 2026-04-20
updated: 2026-04-24
type: concept
tags:
- tractography
- neuroimaging-dti
- diffusion-imaging
- structural-connectivity
- connectomics
- whole-brain-modeling
- paper-methods
- paper-review
sources:
- raw/papers/mori-1999.md
- raw/papers/jones-2010.md
- raw/papers/tournier-2007.md
- raw/papers/sotiropoulos-zalesky-2019.md
---

Tractography is a family of computational techniques that reconstruct three-dimensional white matter fiber pathways from diffusion-weighted magnetic resonance imaging data. By tracing virtual streamlines through local estimates of water diffusion orientation, tractography provides the only non-invasive method for mapping the structural wiring of the human brain in vivo. These reconstructed pathways form the basis of connectome construction and directly constrain computational models of large-scale brain dynamics.

## Motivation and Context

Before the advent of diffusion MRI, knowledge of long-range anatomical connectivity in the human brain relied almost exclusively on invasive tracer studies in non-human primates or post-mortem dissection. The development of diffusion tensor imaging (DTI) in the mid-1990s made it possible to infer fiber orientation from the anisotropic diffusion of water molecules along axonal bundles, but it was Mori et al.'s introduction of tractography algorithms in 1999 that transformed static orientation maps into coherent, three-dimensional trajectories. This breakthrough bridged the gap between voxel-level diffusion measurements and systems-level network analysis, enabling researchers to ask how the physical architecture of white matter shapes functional communication. For whole-brain modeling, tractography is not merely a visualization tool: it produces the quantitative structural connectivity matrices that define which brain regions are anatomically linked, how strongly they are coupled, and the temporal delays imposed by axonal transmission distances.

## Methods and Evolution

Early deterministic tractography algorithms, such as Fiber Assignment by Continuous Tracking (FACT), propagate streamlines by following the principal diffusion direction estimated by the single tensor model at each voxel. While computationally efficient, these methods are notoriously sensitive to noise and physiologically naïve in regions where multiple fiber populations cross, kiss, or fan within a single voxel. Probabilistic approaches partially address this limitation by generating distributions of possible pathways and quantifying uncertainty through bootstrap resampling or Bayesian modeling, yielding more robust connectivity estimates at the cost of increased computation.

A more principled solution to the crossing-fiber problem came with constrained spherical deconvolution (CSD), introduced by Tournier et al. in 2007. Rather than assuming a single dominant orientation per voxel, CSD estimates the full fiber orientation distribution (FOD), resolving multiple intra-voxel fiber populations and dramatically improving tracking accuracy in complex regions such as the centrum semiovale and crossing pathways of the brainstem. Modern pipelines have since expanded beyond local streamline propagation to include global energy-minimization strategies that optimize whole-brain tractograms simultaneously, as well as anatomically constrained tractography that uses tissue segmentation maps to prevent streamlines from penetrating gray matter or cerebrospinal fluid boundaries. These advances are implemented in widely used software libraries including MRtrix3, DIPY, and FSL, which support end-to-end connectome reconstruction from raw diffusion data through parcellation and matrix generation.

## Role in Whole-Brain Modeling

In connectome-based modeling, tractography outputs are converted into structural connectivity matrices that serve as the anatomical scaffold for neural dynamics. Streamline count, fractional anisotropy, or mean diffusivity between pairs of gray matter regions are typically used to define connection weights, while fiber lengths determine signal transmission delays. These matrices feed directly into platforms such as [[tvb]] and [[nest]], where the pattern of long-range projections constrains synchronization, information flow, and the emergence of collective oscillations. Network topological features derived from tractography—including [[network-hubs]], [[rich-club]] organization, and modular architecture—have been shown to predict empirical [[functional-connectivity]] patterns and to shape the spread of activity in [[epilepsy-modeling]] and neurodegeneration simulations. The quality of these matrices therefore places an upper bound on the biological realism that a model can achieve.

## Challenges and Limitations

Despite decades of methodological refinement, tractography remains an ill-posed inverse problem. Jones (2010) provided a critical survey of its validation challenges, emphasizing that the presence of a streamline between two regions does not guarantee a true anatomical synapse, while the absence of a streamline does not prove disconnection. Distance-related biases, gyral bias in seed placement, and the tractography-specific problem of false positives and false negatives all complicate the interpretation of connectivity strength. Sotiropoulos and Zalesky (2019) argued that connectome construction is not a solved problem: choices in acquisition scheme, preprocessing, tracking algorithm, and parcellation interact in nonlinear ways that propagate into downstream network statistics. For whole-brain modelers, these uncertainties translate into sensitivity analyses that must bracket structural connectivity parameters to assess whether observed dynamical phenomena are robust to anatomical noise or artifacts of the specific tractography pipeline employed.

## Related Concepts

Tractography sits at the intersection of several overlapping domains in computational neuroscience. It is the primary computational engine that transforms raw [[diffusion-mri]] data into the [[structural-connectivity]] matrices used in [[connectome]] analysis, distinguishing itself from [[dti]]—the broader tensor-based modeling framework from which early tractography emerged. In the context of [[whole-brain]] simulation, tractography-derived connectivity is often compared against [[effective-connectivity]] estimates from [[dynamic-causal-modeling]] or [[functional-connectivity]] derived from [[fmri]] and [[eeg]], with mismatches between structural and functional connectivity providing clues about unmeasured polysynaptic pathways or state-dependent modulation of connection strengths.
