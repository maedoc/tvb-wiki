---
created: 2026-04-27
sources:
- raw/papers/friston-1993.md
- raw/papers/arxiv-2603.13361.md
- raw/papers/sporns-tononi-kotter-2005.md
- raw/papers/arxiv-2604.03619.md
- raw/papers/arxiv-2603.28931.md
- raw/papers/arxiv-2603.29903.md
- raw/papers/semanticscholar-ff8218c1e55e.md
- raw/papers/glean-github.md
tags:
- cifti
title: Cifti
type: concept
updated: '2026-05-18'
---

CIFTI ([[connectivity]] Informatics Technology Initiative) is a specialized [[neuroimaging]] data format developed by the [[human-connectome-project]] (HCP) for storing dense whole-brain connectivity data. It addresses fundamental limitations of older neuroimaging formats such as [[nifti]] by unifying surface-based cortical representations with volumetric subcortical data into a single coherent structure known as "grayordinates" — a portmanteau combining "gray matter" with "coordinates" that encompasses both cortical surface vertices and subcortical voxels.

The format was developed to handle the challenges of modern multi-modal connectivity analyses where researchers combine [[functional-connectivity]] matrices from [[fmri]] with [[structural-connectivity]] estimates from diffusion imaging. Traditional formats like NIfTI were designed primarily for volumetric data, creating significant file management challenges when working with both surface-based cortical representations and volumetric subcortical structures. CIFTI resolves this by enabling storage of complete connectivity matrices between all grayordinates rather than just parcel-based summaries, preserving the full information content of [[resting-state]] analyses.

CIFTI files use extensions such as `.dtseries.nii` for time series data and `.dscalar.nii` for scalar data, both built on the NIfTI-2 header structure for improved metadata handling. The format is maintained as CIFTI-2 and has become a standard for HCP data releases. It is particularly well-suited for [[whole-brain]] connectivity analyses central to [[whole-brain-modeling]] approaches, and serves as the primary data format for [[the-virtual-brain]] workflows that combine multiple neuroimaging modalities to construct personalized [[connectome]]-based models. See also: [[connectome-workbench]], [[ciftify]], [[hcp-pipelines]], and [[hcp-dataset]]. Related tool: [[cifti-tools]].

## Related Concepts
The design of CIFTI reflects the dual need to represent both [[functional-connectivity]] and [[structural-connectivity]] within a single anatomical frame. Early neuroimaging work defined functional connectivity as the temporal correlation between spatially remote neurophysiological events, a concept first formalized through principal component analysis of PET and [[fmri]] data sets [[raw/papers/friston-1993.md|Friston et al. (1993)]]. The subsequent introduction of the [[connectome]] as a comprehensive structural description of the human brain established the theoretical requirement for formats capable of storing dense, whole-brain relational data rather than isolated volumetric images [[raw/papers/sporns-tononi-kotter-2005.md|Sporns, Tononi & Kötter (2005)]]. More recent fMRI studies demonstrate that functional graphs decode category-specific network states, confirming that the connectivity matrices CIFTI was designed to archive carry meaningful representational information [[raw/papers/arxiv-2603.28931.md|Karmi et al. (2026)]]. By combining surface-based cortical vertices with subcortical voxels into a unified grayordinates space, CIFTI resolves the file-management limitations of earlier formats such as [[nifti]] and provides a coherent substrate for [[whole-brain-modeling]] pipelines that bridge anatomical structure and functional dynamics.

The multimodal integration that CIFTI enables is increasingly central to advanced computational models. A topological signal-processing framework that integrates diffusion MRI-derived structural scaffolds with resting-state fMRI to infer higher-order functional interactions was demonstrated across large cohorts from the [[human-connectome-project]] [[raw/papers/arxiv-2603.29903.md|Bispo et al. (2026)]]. Such analyses require unified representations of surface and volumetric data, a design goal that CIFTI shares. Whole-brain fMRI time-series forecasting methods such as BrainCast preserve dense temporal content to extend informative time series and improve downstream cognitive prediction, reflecting the analytical value of grayordinate-level signal storage [[raw/papers/arxiv-2603.13361.md|Gao et al. (2026)]]. Similarly, techniques that compress fMRI volumes into compact latent tokens for long-range dynamics modeling draw on large-scale benchmarks including the HCP and UK Biobank, highlighting the continuing challenge of efficiently representing high-dimensional brain data that CIFTI was created to address [[raw/papers/arxiv-2604.03619.md|Kim et al. (2026)]]. Collectively, these lines of work situate CIFTI within the broader landscape of [[connectomics]] infrastructure, where [[resting-state]] functional imaging and anatomical connectivity must coexist in formats that natively accommodate hybrid voxel-vertex geometries.

## References

1. (authors unknown). *[[functional-connectivity]]: The Principal-Component Analysis of Large (PET and [[fmri]]) Data Sets*.
2. Yunlong Gao, Jinbo Yang, Li Xiao, Haiye Huo, Yang Ji, Hao Wang, Aiying Zhang, Yu-Ping Wang. *BrainCast: A Spatio-Temporal Forecasting Model for Whole-Brain fMRI Time Series Prediction*. [Link](](https://arxiv.org/abs/2603.13361))
3. (authors unknown). *The Human [[connectome]]: A Structural Description of the Human Brain*.
4. Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, Taesup Moon. (2026). *Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?*. [Link](](https://arxiv.org/abs/2604.03619))
5. Shira Karmi, Galia Avidan, Tammy Riklin Raviv. *Decoding Functional Networks for Visual Categories via GNNs*. [Link](](https://arxiv.org/abs/2603.28931))
6. Breno C. Bispo, Stefania Sardellitti, Juliano B. Lima, Fernando A. N. Santos. (2026). *Multimodal Higher-Order Brain Networks: A Topological Signal Processing Perspective*. [Link](](https://arxiv.org/abs/2603.29903))
7. Yunman Xia, S. Peng, J. Dukart, C. Xie, Shitong Xiang, S. Petkoski, Zilin Li, Joerg F. Hipp, S. Muthukumaraswamy, A. Forsyth, Tianye Jia, N. Vaidya, T. Lett, Liyi Qian, Xiao Chang, Yuxiang Dai, T. Banaschewski, G. Barker, A. Bokde, R. Brühl, S. Desrivières, Herta Flor, P. Gowland, A. Grigis, Andreas Heinz, H. Lemaître, F. Nees, D. Orfanos, Luise Poustka, M. Smolka, Sarah Hohmann, H. Walter, R. Whelan, Paul Wirsching, Zuo Zhang, Lauren Robinson, J. Winterer, Yuning Zhang, H. Kebir, Ulrike Schmidt, Julia Sinclair, Yuchen Liu, Jiexiang Wang, Fei Dai, Longbin Zeng, Yubo Hou, Huarui Wang, Leijun Ye, Chunhe Li, Qibao Zheng, Andre F Marquand, Changsong Zhou, V. Jirsa, Jianfeng Feng, Wenlian Lu, Gunter Schumann. (2026). *Digital Twin Brain simulation and manipulation of a functional [[brain-network]] underlying mental illness*. bioRxiv. [DOI](](https://doi.org/10.64898/2026.03.06.710030))
8. (authors unknown). *[[lean|GLEAN]]: Group Level Exploratory Analysis of Networks*.