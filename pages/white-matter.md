---
title: White Matter
created: 2025-01-15
updated: 2026-05-06
type: concept
tags: [neuroimaging-dti, structural-connectivity, connectomics, whole-brain-modeling, diffusion-imaging, tractography]
sources: [raw/papers/semanticscholar-d801ad366cdb.md, raw/papers/semanticscholar-deecd9987645.md, raw/papers/semanticscholar-ce89e593c89e.md]
---

White matter refers to the bundles of myelinated axons that connect different regions of the brain, forming the structural substrate for communication between cortical and subcortical areas. Unlike gray matter, which contains neuronal cell bodies and is primarily responsible for information processing, white matter consists largely of densely packed axonal fibers surrounded by myelin sheaths produced by oligodendrocytes. This fatty insulation gives white matter its characteristic appearance and enables rapid, faithful transmission of action potentials across long distances. In the context of [[whole-brain modeling]], white matter serves as the anatomical scaffold upon which computational models simulate signal propagation, and its structural topology is fundamental to understanding how functional brain dynamics emerge from anatomical constraints.

The importance of white matter in computational neuroscience has grown substantially with the advent of [[diffusion imaging]] techniques, particularly [[dti|Diffusion Tensor Imaging (DTI)]] and more advanced methods such as diffusion spectrum imaging (DSI) (Wedeen et al., 2008) and neurite orientation dispersion and density imaging (NODDI) (Zhang et al., 2012). These [[neuroimaging]] modalities allow researchers to probe the microstructural properties of white matter tracts in vivo, providing metrics such as [[fractional-anisotropy]] (FA), mean diffusivity (MD), and axonal orientation distributions. The resulting [[structural-connectivity]] matrices—typically derived from [[tractography]] algorithms (Jeurissen et al., 2014)—serve as the foundational connectivity matrices in [[whole-brain]] computational models implemented in software such as [[the-virtual-brain]].

## Signal Propagation and Structural-Functional Coupling

A central question in whole-brain modeling is how [[functional-connectivity]] patterns emerge from the underlying [[structural-connectivity]] architecture. Recent work by Sipes et al. (2026) demonstrates that a considerable amount of observed functional connectivity can be explained by purely passive diffusion processes propagating through the white matter network. Their Higher-Order Network Diffusion (HONeD) model calculates, in closed-form, an estimate of active signal components by spatially deconvolving the effects of passive signal spread over the brain's structural connectivity. This approach, applied across 770 [[human-connectome-project]] subjects, revealed that the resulting "HONeD-innovation" signal sparsifies functional connectivity while retaining a well-connected network, remodels resting-state networks, and deblurs task-activation maps. The finding that passive diffusion accounts for such a large proportion of functional connectivity highlights both the strong structural constraints on brain dynamics and the need for models that can isolate active neural computation from passive signal spread.

The relationship between white matter structure and function—often termed structure-function coupling—exhibits distinct patterns depending on the brain state and the dynamical regime of the system. The work of Myrov et al. (2026) on hierarchical whole-brain modeling of critical synchronization dynamics provides important insights into this relationship. Their Hierarchical Kuramoto model, which incorporates two levels of hierarchy and allows examination of both local synchronization and long-distance interactions between brain regions, produces critical-like dynamics marked by emergent long-range temporal correlations (LRTCs) and interareal phase synchronization. Notably, structure-function coupling shows that correlations with [[structural-connectivity]] peak at criticality for LRTCs and cross-correlations but decay for local and interareal phase synchronization. Comparison with human resting-state [[meg]] data revealed that the model's behavior most closely resembles MEG phase synchronization and multipeak power spectra on the subcritical side of an extended critical regime.

## White Matter in Whole-Brain Modeling Pipelines

The preprocessing and quality assurance of diffusion-weighted images is crucial for reliable structural connectivity estimation. Asay et al. (2025) developed DWIQC, a Python package that serves as a robust quality assurance preprocessing tool for diffusion weighted images while facilitating data management and sharing via the XNAT platform. DWIQC integrates analysis tools from FSL, Prequal, Qsiprep, and [[mrtrix3]] to perform first-level preprocessing and assess data quality through quantitative metrics. The importance of such preprocessing pipelines cannot be overstated, as artifacts in diffusion data can propagate through tractography algorithms and result in spurious white matter tracks that fundamentally distort the structural connectivity matrix used in whole-brain models (Cieslak et al., 2021). This highlights the critical need for rigorous quality control at every stage of the diffusion imaging pipeline, from acquisition through tractography-based connectivity reconstruction.

In [[the-virtual-brain]] workflows, white matter tractography-derived connectivity matrices form the anatomical backbone of the Connectome import module. The software supports various connectivity file formats and provides tools for computing tract length matrices, fiber count matrices, and conductivity matrices—each of which can modulate model dynamics in different ways (Ritter et al., 2013). The [[brian2]] and [[nest]] simulators used in TVB's co-simulation capabilities also interact with white matter representations when modeling detailed white matter microcircuits.

## Open Questions and Future Directions

Despite significant advances, several open questions remain regarding the role of white matter in whole-brain dynamics. The appropriate level of detail for white matter representation in large-scale models remains contested—whether detailed tractography-derived connectomes or simplified graph-theoretic representations better capture essential dynamics depends on the scientific question at hand. Additionally, the temporal dynamics of white matter microstructure, including activity-dependent changes in myelination and axonal properties, are not typically incorporated in standard whole-brain models but may prove crucial for understanding learning and development. Finally, the relationship between structural disconnection and computational deficits in neurological and psychiatric conditions—such as [[schizophrenia-models]] and [[alzheimers-modeling]]—remains an important frontier where white matter modeling and clinical translation intersect.

## References

Asay, D. J., O'Keefe, T. M., Buckner, R. L., & Mair, R. W. (2025). DWIQC: A Python package for preprocessing and quality assurance of diffusion weighted images. *Journal of Open Source Software*, 10(69), 6974. https://doi.org/10.21105/joss.06974

Cieslak, M., Cook, P. A., He, X., Yeh, F. C., Dhollander, T., Adebimpe, A., Haufe, S., Eickhoff, S. B., Frank, M. J., & Gee, J. C. (2021). QSIPrep: An integrative pipeline for quality assessment and individualized preprocessing of diffusion MRI data. *bioRxiv*. https://doi.org/10.1101/2021.03.17.435698

Jeurissen, B., Descoteaux, M., Mori, S., & Leemans, A. (2014). Diffusion MRI fiber tracking: A comparison and evaluation of current methods and artifacts. *AJNR American Journal of Neuroradiology*, 35(3), 512-524. https://doi.org/10.3174/ajnr.A3891

Mori, S., Crain, B. J., Chacko, V. P., & van Zijl, P. C. (1999). Three-dimensional tracking of axonal projections in the brain by magnetic resonance imaging. *Annals of Neurology*, 45(2), 265-269.

Myrov, V., Suleimanova, A., Knapič, S., Partanen, P., Vesterinen, M., Liu, W., Palva, S., & Palva, J. M. (2026). Hierarchical whole-brain modeling of critical synchronization dynamics in the human brain. *Proceedings of the National Academy of Sciences*, 123(12), e2505768123. https://doi.org/10.1073/pnas.2505768123

Ritter, P., Schirner, M., McIntosh, A. R., Jirsa, V. K., & Deco, G. (2013). The virtual brain integrates computational modeling and multimodal neuroimaging. *Brain Connectivity*, 3(2), 121-145. https://doi.org/10.1089/brain.2012.0120

Sipes, B. S., Arab, F., Nagarajan, S., & Raj, A. (2026). HONeD-in on brain activity: Deconvolving passive diffusion on the structural network from functional brain signals. *bioRxiv*. https://doi.org/10.64898/2026.01.05.697753

Wedeen, V. J., Wang, R. P., Schmahmann, J. D., Benner, T., Tseng, W. Y. I., Dai, G., Pandya, D. N., Hagmann, P., D'Arceuil, H., & de Crespigny, A. J. (2008). Diffusion spectrum magnetic resonance imaging (DSI) of tractography within the human brain. *Magnetic Resonance in Medicine*, 59(5), 1125-1133. https://doi.org/10.1002/mrm.21291

Zhang, H., Schneider, T., Wheeler-Kingshott, C. A., & Alexander, D. C. (2012). NODDI: Practical in vivo neurite orientation dispersion and density imaging of the human brain. *NeuroImage*, 61(4), 1000-1016. https://doi.org/10.1016/j.neuroimage.2012.03.072