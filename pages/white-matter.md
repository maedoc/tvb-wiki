---
title: White Matter
created: 2025-01-15
updated: 2026-05-08
type: concept
tags: [neuroimaging, diffusion-imaging, structural-connectivity, whole-brain-modeling, connectomics, tractography]
sources: [raw/papers/semanticscholar-d801ad366cdb.md, raw/papers/semanticscholar-deecd9987645.md, raw/papers/semanticscholar-ce89e593c89e.md]
---

White matter constitutes the anatomical substrate for signal transmission between distributed brain regions in [[whole-brain|whole-brain modeling]] frameworks, comprising approximately 40% of the human cerebrum by volume [@bassert2022; @mazoyer1986]. Unlike [[functional-connectivity|functional connectivity]], which reflects statistical dependencies in ongoing brain activity measured via [[fmri|fMRI]] or [[meg|MEG]], white matter structure provides the relatively fixed infrastructure upon which neural communication occurs [@bullmore2009]. The term refers specifically to myelinated axonal fiber tracts that appear white due to lipid content, organizing into fascicles that traverse between cortical and subcortical regions. In [[computational-neuroscience]], white matter topology is typically represented as a structural connectivity matrix derived from [[diffusion-imaging]] techniques, forming the backbone of large-scale network models.

## Diffusion Imaging and White Matter Mapping

The primary in vivo method for mapping human white matter anatomy is [[diffusion-imaging|diffusion MRI]], which exploits the anisotropic movement of water molecules along axonal fibers [@basser1994]. The most common reconstruction approach, [[diffusion-tensor-imaging|DTI]], yields the fractional-anisotropy metric widely used to characterize white matter integrity. However, DTI's single-tensor model cannot resolve crossing fibers [@wedeen2008; @tuch2002], leading to the development of more sophisticated models including Q-ball imaging, diffusion spectrum imaging, and constrained spherical deconvolution [@descoteaux2009; @wedeen2005]. These advanced techniques, implemented in software packages such as [[dipy]] and [[mrtrix3|MRtrix3]], enable tractography reconstruction that traces fiber pathways through the white matter volume.

Quality assurance of diffusion-weighted images has become increasingly important as large-scale datasets like the [[human-connectome-project|Human Connectome Project]] and [[aomic|AOMIC]] (Amsterdam Open MRI Collection) make high-resolution DTI data widely available. The DWIQC package provides standardized preprocessing workflows that integrate tools from FSL, MRtrix, and other packages to ensure reproducible white matter tractography across studies.

## Structural Connectivity in Whole-Brain Models

In [[whole-brain-modeling|whole-brain computational models]] such as those implemented in [[the-virtual-brain|The Virtual Brain]], white matter structural connectivity serves as the coupling architecture linking neuralmass models at each brain region. The connectivity matrix is typically derived from tractography, with elements representing the strength or number of streamlines connecting region pairs. This structural scaffold fundamentally constrains the dynamics that can emerge from the model, determining which brain regions can directly influence others and at what latency.

Recent work by Sipes et al. (2026) demonstrates that a surprisingly large proportion of observed [[functional-connectivity]] patterns can be explained by passive signal diffusion along the white matter structural network. Their higher-order network diffusion (HONeD) model calculates closed-form estimates of this passive signal propagation, showing that the resulting "HONeD-innovation" signal reveals aspects of active neural computation that would otherwise be obscured by passive spreading. This finding has important implications for interpreting functional connectivity: apparent coupling between regions may reflect nothing more than shared structural pathways rather than active coordination.

Hierarchical whole-brain models incorporating white matter connectivity have also proven essential for studying brain criticality. The work of Myrov et al. (2026) uses a Hierarchical Kuramoto model where interregional coupling is defined by the structural connectivity matrix, demonstrating that structure-function coupling reaches its maximum at critical dynamics. Their model reveals that while long-range temporal correlations and amplitude cross-correlations peak at criticality, phase synchronization shows different coupling patterns with white matter structure.

## Relationship to Functional and Effective Connectivity

The structure-function relationship in the brain remains one of the most active research areas in computational neuroscience. White matter structural connectivity provides the anatomical constraints within which [[effective-connectivity|effective connectivity]]—the causal influence between regions—must operate. However, the relationship is not simply linear: functional connectivity can be present between regions with no direct structural connection (transitive communication), and strong structural links may manifest as weak functional coupling depending on the dynamical state [@honey2009].

Understanding this relationship is particularly crucial for clinical applications. White matter alterations are implicated in numerous neurological and psychiatric conditions, from [[alzheimers-disease|Alzheimer's disease]] where white matter hyperintensities predict cognitive decline, to [[schizophrenia-models|schizophrenia]] where disrupted structural connectivity correlates with symptom severity. Personalized brain models that incorporate individual white matter topology offer potential for understanding individual differences in brain dynamics and treatment response.

## Software for White Matter Analysis

Beyond DTI reconstruction and tractography, white matter analysis encompasses a rich ecosystem of specialized tools. [[afq]] provides automated tractometry for quantifying white matter properties along major fiber bundles. [[tracktotrack]] and related tools enable tractogram manipulation and filtering. The JHU White Matter Atlas provides region labels for white matter structures, while dedicated software like [[Camino]], [[dsi-studio]], and [[mrtrix3]] offer specialized tractography algorithms. These tools form the preprocessing pipeline from raw diffusion data to the connectivity matrices that drive whole-brain simulations.

## Open Questions

Despite significant methodological advances, fundamental questions about white matter's role in brain dynamics remain unresolved. The appropriate level of detail for structural connectivity in whole-brain models—whether coarse anatomical parcellations suffice or fine-grained tractography is necessary—depends on the question being asked. The temporal dynamics of white matter, typically considered static, may also contribute to brain function; changes in myelination and axonal properties occur on timescales relevant to learning and adaptation. Finally, the relationship between white matter microstructure measured in vivo and the actual communication capacity between regions remains imperfectly characterized, motivating ongoing work to validate diffusion-derived connectivity against ground truth from postmortem studies and invasive measurements.