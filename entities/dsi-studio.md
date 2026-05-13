---
created: 2026-04-23
sources:
- raw/papers/arxiv-2602.09852.md
- raw/papers/semanticscholar-adcab180dcd3.md
- raw/papers/semanticscholar-c393c4c4a671.md
- raw/papers/semanticscholar-fcd025fcc10c.md
- raw/papers/arxiv-2602.18072.md
- raw/papers/semanticscholar-1de06cf619ac.md
- raw/papers/semanticscholar-c8a663464cee.md
- raw/papers/arxiv-2604.18470.md
- raw/papers/arxiv-2603.13598.md
- raw/papers/semanticscholar-2c4128f04843.md
- raw/papers/semanticscholar-548a2d4c8ad1.md
tags:
- software-brain-modeling
- diffusion-imaging
- tractography
- connectomics
- structural-connectivity
- neuroimaging-dti
title: DSI Studio
type: entity
updated: '2026-05-13'
---

# _preamble

DSI Studio is an open-source [[diffusion-mri]] analysis and [[tractography]] platform developed by Fang-Cheng Yeh that implements multiple diffusion reconstruction models—including diffusion tensor imaging (DTI), diffusion spectrum imaging (DSI), and generalized q-sampling imaging (GQI)—to reconstruct white matter fiber pathways and generate [[structural-connectivity]] matrices for neuroimaging research. The software employs q-space diffeomorphic reconstruction (QSDR) to align orientation distribution functions within anatomical spaces, supporting deterministic fiber tracking algorithms that have been used to develop sex-specific structural templates from cohorts exceeding one thousand subjects and revealing significant microstructural differences between males and females across cortical and commissural pathways [[raw/papers/semanticscholar-c8a663464cee.md|Jafari & Memar (2025)]]. In clinical neuroimaging, researchers have utilized DSI Studio 2022 with the HCP842 atlas-based algorithm to automatically model 32 white matter tracts in patients with temporal lobe epilepsy, quantifying morphometric and microstructural tissue changes that inform patient-specific network analyses [[raw/papers/semanticscholar-1de06cf619ac.md|Maximova et al. (2026)]]. The platform's reconstruction pipeline has also been applied to generate high-resolution spin distribution functions and classify 84 distinct fiber bundles spanning association, commissural, projection, and cerebellar pathways through its recognize-and-cluster functionality, enabling systematic tract-level analysis in biomechanical and lesion-mapping studies [[raw/papers/semanticscholar-548a2d4c8ad1.md|Atsumi et al. (2026)]][[raw/papers/semanticscholar-2c4128f04843.md|Sperber et al. (2025)]].

Beyond standalone diffusion analysis, DSI Studio serves as a critical intermediary between raw diffusion-weighted acquisitions and network-based computational neuroscience. Its tractography outputs are used to construct weighted brain connectivity graphs where nodes correspond to atlas-defined regions and edge weights encode fiber counts normalized by mean tract length, parameters that can be directly imported into [[the-virtual-brain]] simulations to define anatomical scaffolds and conduction delays [[raw/papers/arxiv-2604.18470.md|Caon et al. (2026)]]. The platform also functions as an integrated fiber data hub, providing standardized tractography atlases that researchers embed into finite element meshes to model tau propagation and anisotropic diffusion in neurodegenerative disease, bridging structural and functional connectome perspectives [[raw/papers/arxiv-2603.13598.md|Jiang et al. (2026)]][[raw/papers/arxiv-2604.18470.md|Caon et al. (2026)]]. These capabilities position DSI Studio as a versatile tool within the broader ecosystem of whole-brain modeling software alongside packages such as [[mrtrix3]], [[dipy]], and [[brainlife]].

## Overview

DSI Studio is an open-source [[diffusion-mri]] analysis and [[tractography]] software package developed by Fang-Cheng Yeh. It supports multiple diffusion models including diffusion tensor imaging (DTI), diffusion spectrum imaging (DSI), and generalized q-sampling imaging (GQI), and provides tools for fiber tracking, [[connectivity]] matrix generation, and network analysis.

## Key Features

- Multi-model diffusion reconstruction (DTI, DSI, GQI)
- Deterministic and probabilistic fiber tracking
- Connectivity matrix generation from tractography
- ROI-based and seed-based tractography
- Tract density imaging (TDI) and track clustering
- Native support for major diffusion MRI formats (DICOM, [[nifti]], FSL)

## Relationship to TVB

DSI Studio generates [[structural-connectivity]] matrices that can be directly imported into TVB as the anatomical scaffold for [[whole-brain]] simulations. The fiber count or tract density between regions serves as the weights in TVB's connectivity matrix, while mean tract length estimates inform conduction velocity and delay parameters. This pipeline is commonly used in [[epilepsy-modeling]], where patient-specific diffusion MRI tractography defines the structural backbone of [[the-virtual-brain]].

## Key Papers

- Yeh, F. C., Wedeen, V. J., & Tseng, W. Y. I. (2010). Generalized q-sampling imaging. *IEEE Transactions on Medical Imaging*, 29(9), 1626–1635.
- Yeh, F. C., & Tseng, W. Y. I. (2011). NTU-90: a high angular resolution brain atlas constructed by q-space diffeomorphic reconstruction. *NeuroImage*, 58(1), 91–99.
- Yeh, F. C. (2020). Shape analysis of the human [[connectome]] in [[alzheimers-disease|Alzheimer's disease]]. *NeuroImage*, 225, 117527.

## Related Software

* [[mrtrix3]]
* Fsl
* [[ants]]
* [[tvb]]
* [[dipy]]
* [[brainlife]]

## References

1. Peter N. Taylor, Gerard Hall, Jonathan Horsley, Yujiang Wang, Sjoerd B. Vos, Gavin P Winston, Andrew W McEvoy, Anna Miserocchi, Jane de Tisi, John S Duncan. (2026). *Open diffusion MRI and connectivity data for epilepsy and surgery: The IDEAS II release*. [Link](](https://arxiv.org/abs/2602.09852))
2. J. Meier, P. Triebkorn, M. Schirner, [[petra-ritter]]. (2025). *Connectomes, simultaneous EEG-[[fmri]] [[resting-state]] data and brain simulation results from 50 healthy subjects*. bioRxiv. [DOI](](https://doi.org/10.1101/2024.04.17.589718))
3. Jorge Barrios, Evan Porter, D. Capaldi, T. Upadhaya, William C. Chen, Julian R. Perks, Aditya Apte, M. Aristophanous, Eve LoCastro, Dylan Hsu, Payton H Stone, J. Villanueva-Meyer, Gilmer Valdes, Fei Jiang, Michael Maddalena, A. Ballangrud, K. Prezelski, Hui Lin, Jinger Y. Sun, M. K. Aldin, O. Chau, B. Ziemer, M. Seaberg, P. Sneed, J. Nakamura, L. Boreta, S. Fogh, D. Raleigh, J. Chew, H. Vasudevan, S. Cha, Christopher Hess, Ruben Fragoso, David B. Shultz, L. Pike, S. Hervey-Jumper, Derek S. Tsang, P. Theodosopoulos, Daniel Cooke, Stanley H Benedict, Ke Sheng, Jan Seuntjens, Catherine Coolens, J. Deasy, S. Braunstein, Olivier Morin. (2025). *Multi-institutional atlas of brain metastases informs spatial modeling for precision imaging and personalized therapy*. Nature Communications. [DOI](](https://doi.org/10.1038/s41467-025-59584-7))
4. Mathias Goncalves, Julia Moser, Thomas J. Madison, rae McCollum, Jacob T. Lundquist, Begim Fayzullobekova, Lidia Hadera, Han H. N. Pham, Lucille A. Moore, Audrey Houghton, Greg Conan, M. Styner, Dimitrios Alexopoulos, C. Smyser, Sally M Stoyell, Sanju Koirala, Steven M. Nelson, Kimberly B. Weldon, Erik G. Lee, R. Hermosillo, L. Vizioli, E. Yacoub, G. H. Patel, Juan Sanchez, K. Wengler, T. Salo, T. Satterthwaite, J. Elison, C. Markiewicz, R. Poldrack, E. Feczko, Oscar Esteban, D. Fair. (2025). *[[fmriprep]] Lifespan: Extending A Robust Pipeline for [[neuroimaging-fmri|Functional MRI]] Preprocessing to Developmental [[neuroimaging]]*. bioRxiv. [DOI](](https://doi.org/10.1101/2025.05.14.654069))
5. Gwenevere Frank, Gopabandhu Hota, Keli Wang, C. Deng, Krish Arora, Diana Vins, Abhinav Uppal, Omowuyi Olajide, Kenneth Yoshimoto, Qingbo Wang, Mariko Yamaoka, Johannes Leugering, S. Deiss, Leif Gibb, Gert Cauwenberghs. (2026). *HiAER-Spike Software-Hardware Reconfigurable Platform for Event-Driven [[neuromorphic-computing]] at Scale*. arXiv.org. [DOI](](https://doi.org/10.48550/arXiv.2602.18072))