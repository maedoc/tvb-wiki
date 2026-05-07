---
title: White Matter
created: 2025-01-15
updated: 2026-05-08
type: concept
tags: [neuroimaging-dti, structural-connectivity, connectomics, whole-brain-modeling, diffusion-imaging, tractography, neuroimaging]
sources: [raw/papers/semanticscholar-d801ad366cdb.md, raw/papers/semanticscholar-deecd9987645.md, raw/papers/semanticscholar-ce89e593c89e.md]
---

White matter refers to the collections of myelinated axons that form the structural scaffolding of the brain, enabling rapid communication between distant cortical and subcortical regions. Unlike gray matter, which contains neuronal cell bodies and is primarily responsible for information processing, white matter consists predominantly of bundles of axons—termed fibers—that are wrapped in a lipid-rich myelin sheath produced by oligodendrocytes. This myelination dramatically increases the conduction velocity of action potentials, allowing white matter tracts to transmit signals at velocities exceeding 100 m/s in the most heavily myelinated pathways (Hursh, 1929; Rushton, 1951). The anatomical arrangement of white matter forms the physical substrate through which functionally specialized brain regions coordinate their activity, making it indispensable for whole-brain modeling approaches that seek to understand how large-scale network dynamics emerge from the interaction of distributed brain areas.

## Role in Whole-Brain Modeling

In the context of [[whole-brain modeling]], white matter serves as the structural foundation upon which computational models of brain dynamics are built. The field of [[connectomics]] has demonstrated that the pattern of white matter connections—quantified through [[structural-connectivity]] matrices derived from [[diffusion-imaging]] techniques—provides critical constraints for whole-brain simulations (Sporns et al., 2005; Hagmann et al., 2008). These connectivity matrices, typically representing the strength of white matter pathways between brain regions parcellated according to a given [[brain-parcellation|atlas]], serve as the anatomical skeleton for models ranging from simple linear coupling frameworks to sophisticated [[neural-mass-models]] incorporating conductance-based neuronal equations. The importance of white matter anatomy was highlighted in recent work demonstrating that the Hierarchical Kuramoto model, when parameterized with empirical structural connectivity derived from diffusion imaging, produces synchronization dynamics that closely match empirical resting-state [[meg]] measurements (Myrov et al., 2026), with structure-function coupling reaching its maximum at critical points in parameter space where the model exhibits long-range temporal correlations characteristic of healthy brain dynamics.

## Measurement with Diffusion Imaging

The primary method for characterizing white matter non-invasively in vivo is [[diffusion-mri]] and its derivative techniques, particularly [[dti]] and [[diffusion-imaging]] using multiple diffusion gradients. These methods exploit the fact that water molecules diffuse more rapidly along axons than perpendicular to them due to the confining effect of the myelin sheath (Beaulieu, 2002). By modeling this anisotropic diffusion, researchers can infer the orientation of white matter fibers in each voxel and reconstruct the major pathways through [[tractography]] algorithms (Mori et al., 1999; Catani et al., 2002). Quantitative metrics such as [[fractional-anisotropy]] provide measures of white matter microstructure integrity, with higher values indicating more coherent fiber orientation. Recent methodological advances, including tools like DWIQC that provide comprehensive preprocessing and quality assurance for diffusion weighted images (Asay et al., 2025), have improved the reproducibility of white matter tractography across datasets and sites.

## From Structural to Functional Connectivity

A fundamental question in computational neuroscience concerns how [[functional-connectivity]]—the statistical dependencies between regional brain signals—arises from the fixed anatomical substrate of white matter. Research using the HONeD (Higher-Order Network Diffusion) model has demonstrated that a considerable portion of empirical functional connectivity patterns can be explained through purely passive signal diffusion over the white matter structural network, without invoking active neural computation (Sipes et al., 2026). This finding has profound implications for interpreting functional connectivity: it suggests that the white matter scaffold imposes substantial constraints on the space of possible functional interactions, such that even passive propagation through anatomical pathways produces patterns resembling empirically observed resting-state networks. By deconvolving this passive diffusion component from [[fmri]] signals, researchers can isolate the residual "innovation" signal that reflects active neural processing, yielding sparsified functional connectivity matrices that reveal otherwise obscured network organization.

## Relationship to Other Concepts

White matter occupies a central position in the hierarchy of brain connectivity research, serving as the physical substrate that connects [[brain-network|brain networks]] measured at the systems level to the cellular and molecular mechanisms of neural signaling. The [[human-connectome-project]] has pioneered high-quality diffusion imaging protocols that have become standard references for white matter microstructure characterization (Van Essen et al., 2013). In clinical applications, white matter alterations are implicated in numerous neurological and psychiatric conditions, from [[alzheimers-modeling|Alzheimer's disease]] where white matter hyperintensities predict cognitive decline to [[epilepsy-modeling|epilepsy]] where altered structural connectivity patterns may contribute to seizure spread (Filippi et al., 2020). Whole-brain modeling frameworks like [[the-virtual-brain]] integrate white matter structural connectivity data to generate personalized brain models that can be used to study disease mechanisms and optimize brain stimulation interventions (Sanz-Leon et al., 2015).

## Conclusion

The relationship between white matter structure and brain function remains an active area of research. While the passive diffusion model demonstrates that functional connectivity partially reflects anatomy (Sipes et al., 2026), the emergence of complex dynamics—such as those exhibiting critical behavior with long-range temporal correlations—requires models that go beyond simple anatomical coupling (Myrov et al., 2026). Future directions include incorporating white matter temporal dynamics, including activity-dependent myelination and plasticity, into whole-brain frameworks to capture the adaptive remodeling of structural connectivity that occurs throughout the lifespan. As diffusion imaging techniques continue to improve (Asay et al., 2025) and computational models become increasingly sophisticated, white matter will remain a cornerstone of whole-brain neuroscience, bridging the gap between anatomical structure and emergent functional dynamics.

## References

1. Asay, D. J., O'Keefe, T. M., Buckner, R. L., & Mair, R. W. (2025). DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images. *Journal of Open Source Software*, 10(69), 6974. https://doi.org/10.21105/joss.06974

2. Beaulieu, C. (2002). The basis of anisotropic water diffusion in the nervous system—a technical review. *NMR in Biomedicine*, 15(7-8), 435-455. https://doi.org/10.1002/nbm.782

3. Catani, M., Howard, R. J., Pajevic, S., & Jones, D. K. (2002). Virtual in vivo interactive dissection of white matter fasciculi in the human brain. *NeuroImage*, 17(1), 77-94. https://doi.org/10.1006/nimg.2002.1136

4. Filippi, M., Basaia, S., Canu, E., Imperiale, F., Meani, A., Caso, F., ... & Agosta, F. (2020). White matter damage predicts disease progression in Alzheimer's disease: A diffusion-tensor imaging study. *Radiology*, 295(2), 366-376. https://doi.org/10.1148/radiol.2020191420

5. Hagmann, P., Cammoun, L., Gigandet, X., Meuli, R., Honey, C. J., Wedeen, V. J., & Sporns, O. (2008). Mapping the structural core of human cerebral cortex. *PLoS Biology*, 6(7), e159. https://doi.org/10.1371/journal.pbio.0060159

6. Hursh, J. B. (1929). The conduction velocity and diameter of nerve fibers. *American Journal of Physiology*, 89(2), 486-507. https://doi.org/10.1152/ajplegacy.1929.89.2.486

7. Mori, S., Crain, B. J., Chacko, V. P., & van Zijl, P. C. (1999). Three-dimensional tracking of axonal projections in the brain by magnetic resonance imaging. *Annals of Neurology*, 45(2), 265-269. https://doi.org/10.1002/1531-8249(199902)45:2<265::AID-ANA21>3.0.CO;2-3

8. Myrov, V., Suleimanova, A., Knapič, S., Partanen, P., Vesterinen, M., Liu, W., ... & Palva, J. M. (2026). Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain. *Proceedings of the National Academy of Sciences*, 123(12), e2505768123. https://doi.org/10.1073/pnas.2505768123

9. Rushton, W. A. H. (1951). A theory of the effects of myelin sheath thickness on conduction velocity in mammalian nerve fibers. *Journal of Physiology*, 115(1), 101-122. https://doi.org/10.1113/jphysiol.1951.sp004624

10. Sanz-Leon, P., Knock, S. A., Spiegler, A., & Jirsa, V. K. (2015). Mathematical framework for large-scale brain network modeling in The Virtual Brain. *NeuroImage*, 111, 385-407. https://doi.org/10.1016/j.neuroimage.2015.01.002

11. Sipes, B. S., Arab, F., Nagarajan, S., & Raj, A. (2026). HONeD-in on Brain Activity: Deconvolving Passive Diffusion on the Structural Network from Functional Brain Signals. *bioRxiv*. https://doi.org/10.64898/2026.01.05.697753

12. Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the brain. *Cerebral Cortex*, 15(7), 1034-1044. https://doi.org/10.1093/cercor/bhh005

13. Van Essen, D. C., Smith, S. M., Barch, D. M., Behrens, T. E., Yacoub, E., & Ugurbil, K. (2013). The WU-Minn Human Connectome Project: An overview. *NeuroImage*, 80, 62-79. https://doi.org/10.1016/j.neuroimage.2013.05.041