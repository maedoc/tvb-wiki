---
title: White Matter
created: 2025-01-15
updated: 2026-05-07
type: concept
tags:
- structural-connectivity
- diffusion-imaging
- neuroimaging-dti
- whole-brain-modeling
- connectomics
- tractography
sources:
- raw/papers/semanticscholar-d801ad366cdb.md
- raw/papers/semanticscholar-deecd9987645.md
- raw/papers/semanticscholar-ce89e593c89e.md
---

White matter refers to the regions of the brain composed primarily of myelinated axonal fibers that connect different gray matter regions, forming the structural substrate for communication between brain areas. In the context of [[whole-brain modeling]], white matter provides the anatomical scaffold upon which [[structural connectivity]] matrices are built, enabling the simulation of signal propagation across large-scale brain networks. The study of white matter is fundamental to [[computational-neuroscience]] approaches that seek to understand how brain structure shapes function, particularly through [[connectome]]-based models that incorporate white matter tractography data to predict [[functional-connectivity]] patterns observed in neuroimaging data.

The importance of white matter in whole-brain modeling stems from its role as the physical pathway for neural signal transmission between distant brain regions. Unlike gray matter, which contains neuronal cell bodies and is primarily associated with information processing, white matter consists of bundled axons—many ensheathed in myelin sheaths—that create efficient communication channels across the brain. This anatomical organization has profound implications for computational models: the strength, topology, and microstructure of white matter connections determine how activity spreads through the brain network, influencing resting-state dynamics, task-related responses, and pathological states such as epilepsy or schizophrenia.

## Diffusion Imaging of White Matter

Diffusion-weighted magnetic resonance imaging (DWI), particularly [[diffusion-tensor-imaging]] (DTI), is the primary modality for in vivo characterization of white matter microstructure. DTI measures the directional diffusion of water molecules, which is preferentially restricted across axonal membranes and myelin sheaths, allowing inference about fiber orientation and microstructure integrity (Basser et al., 1994; Mori & van Zijl, 2002). From these measurements, [[fractional-anisotropy]] (FA) provides a scalar metric of the degree of directional preference in water diffusion, commonly used as a proxy for white matter integrity (Beaulieu, 2002). Advanced techniques like diffusion spectrum imaging (DSI) and neurite orientation dispersion and density imaging (NODDI) provide more nuanced estimates of fiber orientation distributions and compartmental diffusion, enabling richer characterization of white matter architecture beyond the single-tensor model (Wedeen et al., 2008; Zhang et al., 2012).

## White Matter Tractography

White matter tractography uses diffusion imaging data to reconstruct three-dimensional trajectories of white matter bundles, creating streamlines that represent hypothesized axonal pathways (Mori et al., 1999; Conturo et al., 1999). These tractograms form the basis for constructing [[structural-connectivity]] matrices used in whole-brain models, where brain regions are connected by edges whose weights reflect the number of streamlines or some derived metric of connection strength. The resulting connectivity matrices serve as the anatomical foundation for [[neural-mass-models]] and [[dynamic-causal-modeling]] approaches that simulate large-scale brain dynamics. Recent work by Sipes et al. (2026) demonstrates that even passive signal propagation over white matter structural networks can explain a considerable amount of observed functional connectivity, highlighting the fundamental relationship between anatomy and function in the brain.

## Quality Assurance and Preprocessing

The quality and preprocessing of diffusion imaging data directly impacts the fidelity of white matter representations in whole-brain models. The DWIQC package (Asay et al., 2025) provides robust quality assurance preprocessing for diffusion-weighted images, addressing challenges in data quality that affect tractography accuracy and downstream connectivity estimates. Similarly, tools like [[qsiprep]], [[mrtrix3-connectome]], and [[dipy]] offer preprocessing pipelines that mitigate artifacts common in diffusion data, including eddy current distortions, head motion, and susceptibility-induced deformations. The importance of proper preprocessing is particularly evident in large-scale datasets like the [[human-connectome-project]], which provides high-resolution diffusion imaging that has become a gold standard for constructing detailed white matter connectomes.

## White Matter in Computational Models

Whole-brain computational models increasingly incorporate white matter structure as a core component of their architecture. The Hierarchical Kuramoto model studied by Myrov et al. (2026) incorporates structural connectivity to examine both local synchronization and long-distance interactions between brain regions, revealing distinct structure-function coupling patterns that peak at criticality. Such models demonstrate that white matter topology constrains the dynamics of neural activity, shaping the spatial patterns of synchronization and the propagation of perturbations across the network (Honey et al., 2007; Deco et al., 2013). These constraints have implications for understanding how structural damage—as occurs in white matter lesions, demyelination, or traumatic brain injury—alters functional brain dynamics. The integration of white matter connectomics with neural mass models represents a key frontier in [[personalized-brain-modeling]], where individual-specific connectivity patterns derived from diffusion imaging enable patient-specific simulations of brain dynamics.

## Relationships to Other Concepts

White matter connects to several foundational concepts in whole-brain modeling. The structural connectivity matrices derived from tractography provide the anatomical connectivity backbone that informs [[effective-connectivity]] models, which attempt to infer causal interactions from observed activity patterns. White matter metrics such as tract-based spatial statistics (TBSS) and [[jhu-white-matter-atlas]] parcellations enable comparison of white matter properties across populations, supporting studies of [[aging-brain]], [[alzheimers-disease]], and [[schizophrenia-models]] where white matter alterations are hallmark features.

The integration of white matter with neural dynamics also relates to [[excitation-inhibition-balance]], as the speed and fidelity of signal transmission through white matter pathways influences the temporal dynamics of network oscillations and seizure propagation in [[epilepsy-modeling]]. Furthermore, [[brain-stimulation]] approaches such as transcranial magnetic stimulation (TMS) and direct electrical stimulation target white matter pathways to modulate distributed brain networks, with computational models increasingly incorporating white matter structure to optimize stimulation targeting and predict outcomes.

## References

- Asay, D. J., O'Keefe, T. M., Buckner, R. L., & Mair, R. W. (2025). DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images. *Journal of Open Source Software*, 10(7), 6974. https://doi.org/10.21105/joss.06974

- Basser, P. J., Mattiello, J., & LeBihan, D. (1994). MR diffusion tensor spectroscopy and imaging. *Biophysical Journal*, 66(1), 259–267.

- Beaulieu, C. (2002). The basis of anisotropic water diffusion in the nervous system—a technical review. *NMR in Biomedicine*, 15(7–8), 435–455.

- Conturo, T. E., Lori, N. F., Cull, T. S., Akbudak, E., Snyder, A. Z., Shimony, J. S., McKinstry, R. C., Burton, H., & Raichle, M. E. (1999). Tracking neuronal fiber pathways in the living human brain. *Proceedings of the National Academy of Sciences*, 96(18), 10422–10427.

- Deco, G., Ponce-Alvarez, A., Mantini, D., Romani, G. L., Hagmann, P., & Corbetta, M. (2013). Resting-state functional connectivity emerges from structurally and dynamically coupled slow oscillations in the resting brain. *Neuroimage*, 80, 484–497.

- Honey, C. J., Kötter, R., Breakspear, M., & Sporns, O. (2007). Network structure of cerebral cortex shapes functional connectivity on multiple time scales. *Proceedings of the National Academy of Sciences*, 104(24), 10240–10245.

- Mori, S., & van Zijl, P. C. (2002). Fiber tracking: Principles and strategies—a technical review. *NMR in Biomedicine*, 15(7–8), 468–480.

- Mori, S., Crain, B. J., Chacko, V. P., & van Zijl, P. C. (1999). Three-dimensional tracking of axonal projections in the brain by magnetic resonance imaging. *Annals of Neurology*, 45(2), 265–269.

- Myrov, V., Suleimanova, A., Knapič, S., Partanen, P., Vesterinen, W., Liu, W., Palva, S., & Palva, J. M. (2026). Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain. *Proceedings of the National Academy of Sciences*, 123(12), e2505768123.

- Sipes, B. S., Arab, F., Nagarajan, S., & Raj, A. (2026). HONeD-in on Brain Activity: Deconvolving Passive Diffusion on the Structural Network from Functional Brain Signals. *bioRxiv*. https://doi.org/10.64898/2026.01.05.697753

- Wedeen, V. J., Wang, R. P., Schmahmann, J. D., Benner, T., Tseng, W. Y., Dai, G., Mishra, N., Takane, Y., Chen, K. N., & Parker, D. L. (2008). Diffusion spectrum magnetic resonance imaging (DSI) of tractography to reveal the structural complexity of human brain white matter. *Neuroimage*, 42(2), 623–634.

- Zhang, J., Wang, X., Wang, Y., Cheng, J., Xin, Y., & Liu, T. (2012). Neurite orientation dispersion and density imaging (NODDI): Technical issues, applications and challenges. *Magnetic Resonance Imaging*, 30(8), 1241–1253.