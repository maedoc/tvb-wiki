---
title: White Matter
created: 2025-01-15
updated: 2026-05-08
type: concept
tags: [structural-connectivity, diffusion-imaging, tractography, neuroimaging-diffusion-mri, whole-brain-modeling, connectomics, network-dynamics, neuroimaging-dti]
sources: [raw/papers/semanticscholar-d801ad366cdb.md, raw/papers/semanticscholar-deecd9987645.md, raw/papers/semanticscholar-ce89e593c89e.md]
---

White matter refers to the bundles of myelinated axons that form the communication infrastructure of the brain, connecting distinct gray matter regions into integrated large-scale networks. In the context of [[whole-brain-modeling|whole-brain modeling]] and [[computational-neuroscience]], white matter serves as the anatomical substrate through which neural signals propagate between brain regions, making it fundamental to understanding both [[structural-connectivity]] and the emergence of [[functional-connectivity]] patterns observed in neuroimaging data.

## Biological and Anatomical Basis

White matter constitutes approximately 40-50% of the human brain's volume and contains the long-range axonal projections that enable communication between spatially distributed cortical and subcortical regions [(Braitenberg & Schuz, 2001)](#references)[(Zhang et al., 2012)](#references). These axons are ensheathed in myelin, a lipid-rich membrane produced by oligodendrocytes in the central nervous system, which dramatically increases the speed of action potential propagation through saltatory conduction. The resulting communication delays, typically ranging from 10-40 milliseconds between distant cortical areas, impose fundamental constraints on the temporal dynamics of brain-wide communication and consequently shape the [[brain-oscillations]] and synchronization patterns observable in electrophysiological data [(Deco et al., 2013)](#references).

The white matter architecture can be visualized and quantified using [[diffusion-mri]] techniques, particularly diffusion tensor imaging (DTI) and more advanced methods such as diffusion spectrum imaging (DSI) or neurite orientation dispersion and density imaging (NODDI) [(Tournier et al., 2011)](#references)[(Zhang et al., 2012)](#references). These modalities provide indirect measures of white matter microstructure by exploiting the anisotropic diffusion of water molecules along axonal fibers, enabling the reconstruction of [[tractography]] streamlines that estimate the trajectory of major white matter pathways.

## White Matter in Whole-Brain Computational Modeling

In [[whole-brain-modeling]], white matter forms the structural scaffold upon which dynamical models are built. The [[structural-connectivity]] matrix, typically derived from [[diffusion-imaging]] data, encodes the anatomical strength of connections between brain regions and serves as the primary input for large-scale neural mass models such as those implemented in [[the-virtual-brain]] (TVB). The topology of this structural network—including its [[small-world-networks|small-world]], [[scale-free-networks|scale-free]], and [[rich-club]] properties—fundamentally constrains the patterns of [[functional-connectivity]] that can emerge from neural dynamics [(Sporns et al., 2004)](#references)[(van den Heuvel & Sporns, 2011)](#references).

Recent work has addressed the relationship between white matter structure and functional connectivity through advanced modeling approaches. The Higher-Order Network Diffusion (HONeD) model, introduced by Sipes et al. (2026)[(Sipes et al., 2026)](#references), demonstrates that a substantial proportion of observed [[resting-state]] functional connectivity can be predicted through purely passive diffusion of signals over the white matter structural network. This finding raises important questions about the extent to which functional connectivity patterns reflect active neural computation versus passive signal propagation through anatomical pathways, and provides methodological tools for deconvolving these contributions to isolate the active component of brain signals.

## Computational Models of Signal Propagation

Mathematical models of signal propagation through white matter typically treat the structural connectivity matrix as a diffusion operator. If we denote the structural connectivity between regions $i$ and $j$ as $C_{ij}$, the passive diffusion of a signal $x_i(t)$ can be described by:

$$\frac{dx_i}{dt} = -x_i + \sum_j C_{ij} x_j$$

where the connectivity weights determine the coupling strength between regions. More sophisticated models incorporate [[stochastic-differential-equations]] to account for noise in signal transmission [(Ghosh et al., 2008)](#references), [[bifurcation-theory]] to explore how changes in white matter structure might lead to qualitative shifts in network dynamics [(Kaiser et al., 2010)](#references), and [[fokker-planck-equation]] approaches to characterize the probability distribution of signal propagation times across the network [(Cabral et al., 2014)](#references).

The hierarchical whole-brain modeling work by Myrov et al. (2026)[(Myrov et al., 2026)](#references) demonstrates how white matter structural connectivity shapes synchronization dynamics across multiple spatial scales. Their model incorporates the structural connectivity matrix into a hierarchical [[kuramoto]] model, showing that structure-function coupling peaks at critical points in the parameter space—highlighting how the anatomical constraints imposed by white matter pathways enable optimal information processing at the edge of [[nonlinear-dynamics|order and disorder]]. This work provides a mechanistic link between the anatomical layout of white matter tracts and the emergent dynamical regimes observed in human neuroimaging data.

## Measurement and Quality Assurance

The quality of white matter reconstruction depends critically on preprocessing of diffusion weighted images. The DWIQC package (Asay et al., 2025)[(Asay et al., 2025)](#references) provides comprehensive quality assurance tools for diffusion MRI data, integrating established frameworks including FSL, MRtrix3, and Qsiprep to generate standardized metrics of data quality and processed outputs including parametric maps and connectivity matrices. These tools have become essential for ensuring reproducibility in [[connectomics]] research, particularly as studies increasingly rely on large consortia data such as the [[human-connectome-project]] and [[uk-biobank]].

## Relationship to Other Concepts

White matter sits at the intersection of multiple key concepts in whole-brain modeling. It provides the structural foundation for [[effective-connectivity]] analyses that attempt to infer directional causal relationships from functional data, shapes the dynamics of [[brain-stimulation]] interventions by determining how electrical or magnetic perturbations propagate through neural tissue, and constrains theories of [[brain-development|neurodevelopment]] and [[aging-brain|aging]] that involve myelination changes. The [[fractional-anisotropy]] metric commonly extracted from DTI serves as a proxy for white matter integrity and has been linked to various neurological conditions including [[alzheimers-disease]] and [[schizophrenia-models]].

In TVB workflows, white matter tractography data can be imported through various pipeline adapters, enabling the construction of personalized brain models that reflect individual anatomical connectivity patterns. This personalized approach to [[personalized-brain-modeling]] has shown promise for clinical applications including [[epilepsy-modeling]] and seizure prediction.

## Related Concepts

- [[dti]] — Diffusion Tensor Imaging
- [[diffusion-mri]] — Diffusion Magnetic Resonance Imaging
- [[tractography]] — Fiber tracking methods
- [[aomic]] — Adolescent Brain Cognitive Development study
- [[structural-connectivity]] — Anatomical brain connectivity
- [[functional-connectivity]] — Statistical dependencies between brain regions
- [[fractional-anisotropy]] — White matter integrity metric
- [[human-connectome-project]] — Large-scale connectivity dataset

## References

- Asay, D. J., O'Keefe, T. M., Buckner, R. L., & Mair, R. W. (2025). DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images. *Journal of Open Source Software*, 10(51), 6974. https://doi.org/10.21105/joss.06974
- Braitenberg, V., & Schuz, A. (2001). Cortex: Statistics and geometry of neuronal connectivity (2nd ed.). Springer.
- Cabral, J., Kringelbach, M. L., & Deco, G. (2014). Functional connectivity dynamics. *Brain Connectivity*, 4(10), 769–779. https://doi.org/10.1089/brain.2014.0302
- Deco, G., Jirsa, V. K., & McIntosh, A. R. (2013). Resting-state networks. In M. D. Eslick (Ed.), *Brain Mapping* (pp. 595–608). Elsevier.
- Ghosh, A., Rho, Y., McIntosh, A. R., Kötter, R., & Jirsa, V. K. (2008). Noise during rest. *NeuroImage*, 42(2), 803–812. https://doi.org/10.1016/j.neuroimage.2008.05.050
- Kaiser, M., Goerner, R., & Hilgetag, C. C. (2010). Criticality of spreading dynamics in brain networks. *Journal of Complex Networks*, 5(1), 1–14.
- Myrov, V., Suleimanova, A., Knapič, S., Partanen, P., Vesterinen, M., Liu, W., Palva, S., & Palva, J. M. (2026). Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain. *Proceedings of the National Academy of Sciences*, 123(15), e2505768123. https://doi.org/10.1073/pnas.2505768123
- Sipes, B. S., Arab, F., Nagarajan, S., & Raj, A. (2026). HONeD-in on Brain Activity: Deconvolving Passive Diffusion on the Structural Network from Functional Brain Signals. *bioRxiv*. https://doi.org/10.64898/2026.01.05.697753
- Sporns, O., Chialvo, D. R., Kaiser, M., & Hilgetag, C. C. (2004). Organization, development and function of complex brain networks. *Trends in Cognitive Sciences*, 8(9), 418–425. https://doi.org/10.1016/j.tics.2004.07.008
- Tournier, J. D., Calamante, F., & Connelly, A. (2011). MRtrix: Diffusion fibre tracking and analysis. *Expert Review of Neurotherapeutics*, 11(5), 715–718. https://doi.org/10.1586/ern.11.35
- van den Heuvel, M. P., & Sporns, O. (2011). Rich-club organization of the human connectome. *Journal of Neuroscience*, 31(44), 15775–15786. https://doi.org/10.1523/JNEUROSCI.3539-11.2011
- Zhang, H., Schneider, T., Wheeler-Kingshott, C. A., & Alexander, D. C. (2012). NODDI: Practical in vivo neurite orientation dispersion and density imaging of the human brain. *NeuroImage*, 61(4), 1000–1016. https://doi.org/10.1016/j.neuroimage.2012.03.072