---
title: White Matter
created: 2025-01-15
updated: 2026-05-07
type: concept
tags:
- structural-connectivity
- connectomics
- diffusion-imaging
- neuroimaging-dti
- whole-brain-modeling
- tractography
- fractional-anisotropy
sources:
- raw/papers/semanticscholar-d801ad366cdb.md
- raw/papers/semanticscholar-deecd9987645.md
- raw/papers/semanticscholar-ce89e593c89e.md
---

White matter refers to the bundles of myelinated axons that connect different regions of the brain, forming the structural substrate for information transmission across neural circuits. In the context of [[whole-brain modeling]] and [[computational neuroscience]], white matter serves as the anatomical scaffold upon which [[dynamic-causal-modeling]] and [[neural-mass-models]] simulate signal propagation between brain regions. The white matter network, reconstructed from [[diffusion-imaging]] data via [[tractography]], provides the structural connectivity (SC) matrix that defines the coupling between neural masses in large-scale brain models.

## White Matter Structure and Imaging

The white matter comprises approximately 40% of the human cerebral volume and contains myelinated axons ranging from 0.2 to 20 μm in diameter. Myelin, produced by oligodendrocytes in the central nervous system, increases the speed of action potential propagation from approximately 1 m/s in unmyelinated fibers to over 100 m/s in large-diameter myelinated axons. This speed differential is fundamental to the temporal dynamics observed in [[brain-oscillations]] and the coordination of distributed neural processes across disparate brain regions.

Diffusion-weighted magnetic resonance imaging (DWI) is the primary in vivo modality for probing white matter microstructure. By measuring the Brownian motion of water molecules, DWI enables inference about tissue microstructure, including fiber orientation, axonal density, and myelin content. Advanced reconstruction techniques such as [[dti]] (DTI), Q-ball imaging, and constrained spherical deconvolution allow estimation of fiber orientation distribution functions (fODFs), enabling tractography reconstruction of white matter pathways. The [[human-connectome-project]] (HCP) has established benchmark protocols for high-resolution diffusion imaging, with b-values up to 5000 s/mm² and 1.25 mm isotropic resolution, yielding unprecedented detail in white matter anatomy.

## Structural Connectivity Matrices

In [[whole-brain modeling]], white matter structure is encoded as a structural connectivity (SC) matrix, where elements w_ij represent the strength of anatomical connection between brain regions i and j. These matrices are derived from [[tractography]] streamlines, with connection weights typically computed as either streamline count (probabilistic connectivity) or some microstructural metric such as [[fractional-anisotropy]] (FA) averaged along streamlines. The resulting SC matrix serves as the adjacency matrix governing signal propagation in both [[neural-mass-models]] and [[spiking-neural-networks]] implementations of whole-brain dynamics.

A critical insight from recent work is that purely passive diffusion over the white matter structural network can explain a substantial fraction of observed [[functional-connectivity]] patterns in resting-state fMRI. The higher-order network diffusion (HONeD) model, introduced by Sipes et al. (2026), demonstrates that spatial deconvolution of passive signal spread using the SC matrix reveals an "innovation" signal that better isolates active neural computations from passive signal propagation. This approach highlights the dual role of white matter as both a medium for signal transmission and a confounder in interpreting functional imaging data.

## Quality Assurance and Preprocessing

Rigorous quality assurance of diffusion-weighted images is essential for reliable SC matrix construction. The DWIQC package (Asay et al., 2025) provides automated preprocessing and quality metrics for diffusion data, utilizing tools including FSL, MRtrix3, and Qsiprep to assess data quality through quantitative metrics such as signal-to-noise ratio, motion parameters, and artifact detection. Poor-quality diffusion data propagates errors into SC matrices, compromising the validity of subsequent whole-brain models. Studies using large cohorts such as HCP (770 subjects), [[aomic]], and [[uk-biobank]] (40,000+ subjects) have established expected ranges for diffusion metrics, enabling automated outlier detection.

## Relationship to Whole-Brain Dynamics

Whole-brain computational models incorporate white matter structure in several ways. In [[neural-mass-models]] such as the [[jansen-rit]] or [[wong-wang-model]], coupling between brain regions is implemented via the SC matrix, where regional activity drives input to connected regions. The coupling strength is typically scaled by SC weights, and delay is incorporated based on tract length and assumed conduction velocity (~6-10 m/s for cortico-cortical connections).

Recent work by Myrov et al. (2026) integrates white matter structure into hierarchical [[kuramoto]] models of large-scale brain dynamics, demonstrating that structure-function coupling peaks at criticality for long-range temporal correlations and amplitude cross-correlations. This finding suggests that the white matter SC matrix not only provides anatomical scaffolding but also constrains dynamic regimes in ways that may be optimized for information processing.

## Biological Mechanisms

White matter microstructure reflects developmental and pathological processes. During [[neurodevelopment]], myelination proceeds in a posterior-to-anterior gradient, completing in the third decade of life. Changes in white matter integrity are observed in [[alzheimers-disease]], [[schizophrenia-models]], and following [[brain-stimulation]] interventions. These microstructural changes manifest in diffusion metrics (FA, mean diffusivity, axial/radial diffusivity) and alter SC matrix properties, with downstream consequences for whole-brain dynamics and [[functional-connectivity]].

## Relationship to TVB

[[the-virtual-brain]] (TVB) integrates white matter structural connectivity as a fundamental component of its whole-brain simulation framework. TVB accepts SC matrices derived from [[diffusion-imaging]] and [[tractography]] workflows, typically processed through tools like standard tractography packages or [[connectome-workbench]]. The resulting Connectome data is used to configure coupling functions between brain regions in TVB's neural mass model implementations, including the [[jansen-rit]] model for EEG/MEG simulation and the [[wong-wang-model]] for resting-state dynamics. TVB also supports delay-adjusted coupling that accounts for finite conduction velocity along white matter pathways, making the anatomical white matter geometry a direct determinant of simulated temporal dynamics.