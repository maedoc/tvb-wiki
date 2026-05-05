---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-a6b8919e7fe8.md
- raw/papers/huntenburg-2018.md
- raw/papers/semanticscholar-518ee560ec89.md
tags:
- software
title: Spinal Cord Toolbox
type: entity
updated: '2026-05-05'
---

The Spinal Cord Toolbox (SCT) is a specialized open-source software platform for automated processing and quantitative analysis of spinal cord magnetic resonance imaging (MRI) data. Developed primarily by the [NeuroPoly laboratory](https://neuropoly.github.io/) at the University of Montreal, SCT addresses the unique challenges posed by spinal cord [[neuroimaging]]—particularly the small cross-sectional area of the cord (~10mm diameter), its curved geometry within the vertebral canal, and the susceptibility artifacts that plague conventional MRI processing pipelines designed for the brain [@de-leener-2017]. The toolkit provides a comprehensive suite of command-line tools that enable preprocessing, segmentation, registration, and metric extraction across multiple MRI modalities including T1-weighted, T2-weighted, diffusion tensor imaging (DTI), and functional MRI of the spinal cord.

## Motivation and Context

The spinal cord has historically received less attention than the brain in neuroimaging research, largely due to technical challenges in imaging and processing. Unlike the cerebral cortex, which benefits from standardized preprocessing workflows developed over decades (see Freesurfer, Fsl, and Nilearn), spinal cord MRI requires specialized algorithms that account for the cord's elongated geometry, surrounding cerebrospinal fluid, and vertebrae that introduce distortion. Researchers studying spinal cord injury, demyelinating diseases such as multiple sclerosis, or neurodegenerative conditions affecting descending motor pathways previously had to develop custom processing scripts for each study, leading to poor [[reproducibility]] and methodological heterogeneity. SCT emerged to fill this gap by providing a validated, automated, and open-source pipeline that brings spinal cord neuroimaging to the same level of methodological rigor as brain imaging [@de-leener-2020].

## Technical Content

SCT implements several core algorithms specifically designed for spinal cord processing. The spinal cord segmentation relies on a deep learning architecture (based on convolutional neural networks) trained on manually annotated datasets, achieving robust and accurate detection of the cord boundary across healthy subjects and patients with pathology. For registration, SCT employs a chain of affine and deformable transformations that align spinal cord images to a template space—the [[mni-space]]-derived PAM50 template—which enables group-level analysis and comparison across subjects. The toolkit additionally provides tools for vertebral labeling, gray matter segmentation, and extraction of quantitative metrics including cross-sectional area, spinal cord diameter, and magnetization transfer ratios.

For [[diffusion-imaging]] analysis, SCT integrates with established [[diffusion-mri]] processing tools including Mrtrix3 and Dipy to perform [[tractography]] of [[white-matter]] pathways in the spinal cord. The pipeline includes automatic detection of the spinal levels (C1-C5, T1-T12) and orientation-specific analysis of diffusion metrics such as [[fractional-anisotropy]] and mean diffusivity along the cord's central axis. These capabilities make SCT particularly valuable for studying the structural integrity of descending corticospinal tracts and ascending sensory pathways in clinical populations [@levy-2025].

## Key Features

The toolkit offers over 100 command-line functions organized into modular scripts that can be combined into processing pipelines. Key features include the `sct_deepseg` command for automated spinal cord segmentation, `sct_register_multimodal` for registration across MRI contrasts, and `sct_extract_metric` for quantitative analysis of cord morphology and diffusion properties. Tractography in SCT is performed through integration with Mrtrix3 rather than a native SCT command, enabling detailed reconstruction of spinal white matter pathways. SCT supports batch processing and integration with workflow managers such as [[snakemake]], enabling reproducible analysis of large datasets. The software is distributed as a Python package and as Docker/Singularity containers through [[apptainer]] for easy installation and deployment in high-performance computing environments.

## Relationship to TVB

The Spinal Cord Toolbox occupies a niche somewhat peripheral to [[the-virtual-brain]]'s [[TVB]] core [[whole-brain|whole-brain modeling]] mission. While TVB focuses on large-scale brain network dynamics and simulates cortical and subcortical activity at the systems level, SCT specializes in the spinal cord—a structure typically outside the scope of whole-brain connectivity models. However, the two software platforms share philosophical commitments to open-source development, reproducible neuroimaging pipelines, and standardized preprocessing. Researchers interested in modeling the full neuraxis from cortex to spinal cord could potentially use SCT to preprocess spinal cord MRI data, extract [[structural-connectivity]] information, and incorporate these findings into extended whole-brain models that include descending motor pathways. The integration remains uncommon in the literature, but SCT's outputs in the form of spinal cord segmentations and templates could theoretically serve as anatomical constraints for extensions of [[whole-brain-modeling]] frameworks.

## Key Papers

- **De Leener et al. 2017** - "SCT: a toolbox for automated segmentation and tractography of the spinal cord" (NeuroImage) - Original publication describing SCT's core functionality
- **De Leener et al. 2020** - "SCT: Spinal Cord Toolbox, version 5.0" (Nature Communications) - Major update with deep learning segmentation
- **Levy et al. 2025** - "SCT: Spinal Cord Toolbox, version 6.0" (NeuroImage) - Current version with enhanced diffusion imaging capabilities

## Related Software

SCT intersects with several other neuroimaging software packages in the broader ecosystem. For general MRI preprocessing, it complements tools like [[ants]] for registration and Fsl for statistical analysis. For diffusion MRI processing, SCT can be used alongside Mrtrix3 and Dipy for tractography and connectivity analysis. The template-based approach used by SCT shares methodology with brain parcellation tools such as Nilearn and [[templateflow]]. For quality control and visualization, SCT integrates with Freesurfer's freeview and general-purpose medical imaging viewers. Researchers building comprehensive neuroimaging pipelines may combine SCT with brain-focused tools like [[mne-bids]] for combined spinal cord and cortical analysis.

## References

1. Quynh Lê, Arichena Manmatharayan, Mashaal Syed, Ki-Sang Kang, Tsao‐Wei Liang, Mahdi Alizadeh, Chengyuan Wu. (2026). *Structural and [[functional-connectivity]] in Parkinson's Disease Patients With Freezing of Gait and Other Gait Disturbances*. Clinical Neuroimaging. [DOI](https://doi.org/10.1002/neo2.70042)
2. (authors unknown). *[[nighres]]: processing tools for high-resolution neuroimaging*.
3. Rohan Banerjee, M. Kaptan, Alexandra Tinnermann, Ali Khatibi, Alice Dabbagh, C. Büchel, Christian W Kündig, C. S. Law, Dario Pfyffer, D. Lythgoe, Dimitra Tsivaka, D. Van de Ville, Falk Eippert, Fauziyya Muhammad, Gary H. Glover, Gergely Dávid, Grace Haynes, Jan Haaker, Jonathan C. W. Brooks, J. Finsterbusch, K. Martucci, K. Hemmerling, Mahdi Mobarak-Abadi, M. Hoggarth, M. Howard, Molly G. Bright, Nawal Kinany, O. Kowalczyk, Patrick Freund, Robert L. Barry, S. Mackey, Shahabeddin Vahdat, Simon Schading, Stephen B McMahon, Todd Parish, Véronique Marchand-Pauvert, Yufen Chen, Z. A. Smith, K. Weber, B. De Leener, Julien Cohen-Adad. (2025). *EPISeg: Automated segmentation of the spinal cord on echo planar images using open-access multi-center data*. bioRxiv. [DOI](https://doi.org/10.1101/2025.01.07.631402)