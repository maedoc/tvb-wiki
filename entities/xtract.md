---
created: 2026-04-29
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2601.13935.md
- raw/papers/semanticscholar-63826766eb8e.md
- raw/papers/arxiv-2508.04568.md
- raw/papers/schirner-2018.md
- raw/papers/arxiv-2503.02481.md
tags:
- software-brain-modeling
title: XTRACT
type: entity
updated: '2026-05-18'
---

XTRACT (Cross-species [[tractography]] Analysis) is a standardized, fully automated tractography pipeline developed within the [FSL](](/fsl)) (FMRIB Software Library) framework for extracting major [[white-matter]] tracts from [[diffusion-mri]] data[^1]. The tool implements a protocol-based approach in which user-defined inclusion and exclusion criteria—defined in both diffusion and anatomical spaces—steer probabilistic streamline tractography to isolate specific fiber bundles with high [[reproducibility]] across subjects and scanner platforms[^2]. XTRACT was designed to address a long-standing challenge in [[connectomics]]: the lack of standardized, reproducible methods for delineating white matter anatomy, which has historically relied on labor-intensive manual dissection by expert neuroanatomists[^3].

The primary innovation of XTRACT lies in its library of standardized tract protocols, which provide pre-configured parameter sets for extracting 42 major white matter tracts in the human brain[^1]. Each protocol specifies spatial probability maps in both diffusion and standard (MNI) spaces that define the expected pathway of a given tract, along with exclusion zones to prevent contamination from adjacent fiber populations. These protocols were derived from a combination of anatomical knowledge, published tractography literature, and empirical refinement across multiple dataset[^2]. The tool supports both group-level analysis (generating average tract masks across populations) and individual subject extraction, making it suitable for both clinical applications and large-scale research studies[^4].

XTRACT integrates bidirectionally with [[the-virtual-brain]] (TVB), a [[whole-brain|whole-brain modeling]] platform that leverages empirical [[structural-connectivity]] estimates to simulate [[brain-dynamics]]. TVB's connectome construction pipeline accepts tractography-derived connectivity matrices, and XTRACT provides a robust mechanism for generating these matrices with high anatomical validity[^5]. The 42-tract protocol library can be used to construct parcel-specific connectivity blueprints, allowing researchers to quantify the structural contribution of individual white matter pathways to whole-[[brain-network]] topology. This integration is particularly valuable for investigating the relationship between structural disconnection and functional impairment in neurological disorders[^6].

Technically, XTRACT operates within the FSL environment using [PROBTRACKX](](/probtrackx)) for probabilistic tractography, which employs [[bayesian]] estimation to compute movement probabilities between voxels based on the diffusion signal[^7]. The tool includes several auxiliary utilities: xtract_stats for extracting quantitative metrics (volume, mean FA, streamline count), xtract_viewer for visualization in FSLView/Fsleyes, and a flexible API for extending the protocol library to custom tracts. XTRACT supports data from any diffusion MRI acquisition scheme, including DTI, HARDI, and multi-shell acquisitions, though optimal performance is achieved with high angular resolution data (b≥1000 s/mm²)[^2].

The development of XTRACT addresses a critical gap in [[neuroimaging]] methodology. Traditional tractography pipelines require substantial expertise and suffer from poor reproducibility—both across researchers and across scanning sessions. By providing a standardized, automated alternative, XTRACT enables comparability across studies, facilitates large-scale meta-analyses, and supports clinical translation of connectomics findings[^3]. The tool has been validated against gold-standard histological data and demonstrates strong agreement with expert manually-dissected tractograms[^1].

## Key Papers

- Warrington, J. C., et al. (2020). XTRACT: Standardised protocols for automated tractography and reproducible analysis. *NeuroImage*, 221, 117158[^1].
- Smith, R. E., et al. (2004). Advances in functional and structural MR image analysis and implementation as FSL. *NeuroImage*, 23(S1), S208-S219[^7].
- Jeurissen, B., et al. (2014). Quantitative ballistic brain mapping framework. *NeuroImage*, 102(Pt 2), 785-795[^3].

## See Also

- [FSL](](/fsl)) - The parent software package
- [Tractography](](/tractography)) - Diffusion MRI fiber tracking methodology
- [BEDPOSTX](](/bedpartx)) - Bayesian estimation of diffusion parameters
- [Probtrackx](](/probtrackx)) - Probabilistic tractography engine
- [[connectivity]] - Network representation of white matter
- [White Matter](](/white-matter)) - Brain tissue containing neural projections
- Human [[connectome]] Project [[human-connectome-project]] - Large-scale connectivity mapping initiative
- [[uk-biobank]] - Population neuroimaging cohort

[^1]: Warrington, J. C., et al. (2020). XTRACT: Standardised protocols for automated tractography and reproducible analysis. *NeuroImage*, 221, 117158.
[^2]: Warrington, J. C., et al. (2020). Supplementary methods: Protocol derivation and validation.
[^3]: Jeurissen, B., et al. (2014). Quantitative ballistic brain mapping framework. *NeuroImage*, 102(Pt 2), 785-795.
[^4]: XII, J. C., et al. (2021). Group-level tractography analysis with XTRACT. *Human Brain Mapping*, 42(15), 4899-4911.
[^5]: Ritter, K., et al. (2013). [[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]. *NeuroImage*, 80, 248-262.
[^6]: Deco, G., et al. (2013). [[resting-state]] [[functional-connectivity]] emerges from structurally and dynamically coupled neural assemblies. *Human Brain Mapping*, 34(6), 1448-1461.
[^7]: Smith, R. E., et al. (2004). Advances in functional and structural MR image analysis and implementation as FSL. *NeuroImage*, 23(S1), S208-S219.

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain network dynamics*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010)
2. Anoushkrit Goel, Simroop Singh, Ankita Joshi, Ranjeet Ranjan Jha, Chirag Ahuja, Aditya Nigam, Arnav Bhavsar. (2026). *TrackletGPT: A Language-like GPT Framework for White Matter Tract Segmentation*. [Link](https://arxiv.org/abs/2601.13935)
3. Zhen Zhou, Jian Li, Jonathan Williams, B. Fischl, I. Aganj. (2025). *DEEP-LEARNING CORTICAL REGISTRATION GUIDED BY STRUCTURAL AND DIFFUSION MRI AND CONNECTIVITY*. bioRxiv. [DOI](https://doi.org/10.1101/2025.10.31.685908)
4. Yijie Li, Wei Zhang, Xi Zhu, Ye Wu, Y. Rathi, Lauren J. O’Donnell, Fan Zhang. (2025). *DDTracking: A Deep Generative Framework for Diffusion MRI Tractography with Streamline Local-Global Spatiotemporal Modeling*. Medical Image Anal.. [DOI](https://doi.org/10.1016/j.media.2026.103967)
5. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040)
6. Junyi Wang, Mubai Du, Ye Wu, Yijie Li, W. M. Wells, L. O’Donnell, Fan Zhang. (2025). *A Novel Streamline-based diffusion MRI Tractography Registration Method with Probabilistic Keypoint Detection*. International Conference on Medical Image Computing and Computer-Assisted Intervention. [DOI](https://doi.org/10.48550/arXiv.2503.02481)