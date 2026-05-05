---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-a0cce22e2ffc.md
- raw/papers/semanticscholar-109de470e443.md
- raw/papers/semanticscholar-4d73a30d5c84.md
tags:
- software-brain-modeling
- neuroimaging
- neuroimaging-fmri
- neuroimaging-meg
- neuroimaging-eeg
- reproducibility
- dataset
title: BIDS Apps
type: entity
updated: '2026-05-05'
---

BIDS Apps are containerized [[neuroimaging]] processing pipelines that operate on data organized according to the [[bids]] (Brain Imaging Data Structure) specification. They represent a standardization effort to make neuroimaging analysis workflows portable, reproducible, and interoperable across different computing environments. Each BIDS App is a command-line tool packaged inside a Docker or [[apptainer]] (formerly Singularity) container, accepting BIDS-formatted datasets as input and producing BIDS-compliant derivatives as output. The BIDS Apps framework was introduced by Gorgolewski and colleagues (2017) as a solution to the [[reproducibility]] challenges that have long plagued the neuroimaging community.

## Motivation and Context

Neuroimaging research has long suffered from a reproducibility crisis, wherein analysis pipelines developed at one laboratory often fail to run at another due to differences in software dependencies, operating systems, and data organization. The BIDS Apps framework emerged to address this problem by combining two key innovations: a standardized data format (BIDS) and a containerization approach that bundles all necessary software dependencies into a single portable image. Originally proposed by the Neuroimaging Community through a series of workshops and the OHBM Hackathon, BIDS Apps enable researchers to run identical preprocessing and analysis pipelines regardless of their local computational infrastructure, from laptops to high-performance computing clusters (Gorgolewski et al., 2017).

The BIDS Apps specification defines a common command-line interface that all compliant apps must follow. This includes standardized input arguments for specifying the BIDS dataset path, output directory, and processing options, as well as conventions for handling partial BIDS datasets and generating provenance metadata. By enforcing this interface, the framework allows users to switch between different processing pipelines—say, from [[fmriprep]] for fMRI preprocessing to [[mriqc]] for quality control—without learning different command-line interfaces for each tool. The official BIDS Apps specification is maintained in the `bids-apps` GitHub repository, which serves as the central hub for the specification and the community of developers who build and maintain compliant applications.

## Technical Specification

A BIDS App must adhere to the BIDS Apps specification, which mandates several technical requirements. First, the container must accept a BIDS directory as its primary input and write all outputs to a specified derivatives directory that itself conforms to the [[bids-derivatives]] specification. Second, the app should support common preprocessing options through standardized flags, allowing users to enable or disable specific processing steps without modifying the underlying code. Third, BIDS Apps are expected to generate comprehensive log files and JSON sidecars that document the exact software versions, parameters, and environmental conditions used during execution, thereby enhancing reproducibility (Gorgolewski et al., 2017).

The containerization approach relies on [[datalad-containers]] or raw Docker/Singularity images to ensure bit-level reproducibility. Each BIDS App image is pinned to specific versions of all underlying software dependencies—including operating system libraries, Python packages, and specialized neuroimaging tools like [[fsl-melodic]] or FreeSurfer. This stands in contrast to traditional installation methods where users might pip install or apt-get install packages at different times, leading to the so-called "works on my machine" problem. The BIDS Apps GitHub organization hosts the source code for many popular apps, providing a platform for community contributions and standardized development practices.

## Key BIDS Apps

Several BIDS Apps have become widely adopted in the neuroimaging community. [[fmriprep]] is perhaps the most prominent, providing a complete fMRI preprocessing workflow that includes motion correction, susceptibility distortion correction, registration to standard space, and tissue segmentation (Esteban et al., 2019). [[mriqc]] generates image quality metrics and automated quality control reports for both structural and functional MRI data (Esteban et al., 2017). For diffusion MRI processing, [[smriprep]] has emerged as the community standard, providing robust preprocessing for diffusion‑weighted imaging data including motion correction, eddy current correction, and reconstruction of advanced diffusion models (Cieslak et al., 2021). Other notable tools include [[mrtrix3-connectome]] for advanced diffusion model estimation, [[bids]] for BIDS dataset conversion and curation, and [[heudiconv]] for converting DICOM files directly to BIDS format.

## Relationship to TVB

The [[the-virtual-brain]] (TVB) ecosystem leverages BIDS Apps as part of its data preprocessing pipeline for whole‑brain modeling. When constructing personalized brain models from empirical neuroimaging data, TVB requires structural connectivity matrices derived from diffusion tensor imaging (DTI) or more advanced diffusion models, as well as functional connectivity matrices from resting‑state [[fmri]] or [[meg]] recordings. The preprocessing of raw neuroimaging data to produce these inputs can be facilitated by BIDS‑compliant preprocessing chains, including [[smriprep]] for diffusion data and [[fmriprep]] for functional data.

Moreover, TVB's integration with tools like [[datalad]] enables version‑controlled storage and retrieval of large neuroimaging datasets, complementing the BIDS organizational structure. Researchers building [[personalized-brain-modeling|personalized brain]] models increasingly adopt BIDS as the foundation for data management, allowing them to feed preprocessed [[connectivity]] estimates directly into TVB's simulation framework. The combination of BIDS data organization, BIDS Apps for preprocessing, and TVB for dynamical modeling creates an end‑to‑end reproducible workflow from raw MRI scans to [[whole‑brain]] simulations. This integration is particularly valuable for studies that require both high‑quality preprocessing (ensured by validated BIDS Apps) and sophisticated dynamical analysis (provided by TVB), enabling researchers to maintain reproducibility across the entire analysis pipeline while focusing their efforts on the scientific questions at hand.

## Key Papers

- Gorgolewski, K., Alfaro‑Almagro, F., Auer, T., et al. (2017). BIDS Apps: Improving reproducibility in neuroimaging. Neuroimage.
- Esteban, O., Markiewicz, C.J., Blair, R.W., et al. (2019). fMRIPrep: A robust preprocessing pipeline for functional MRI. Nature Methods.
- Esteban, O., Birman, D., Schaer, M., et al. (2017). MRIQC: Advancing the automatic prediction of MRI quality. PeerJ.
- Cieslak, M., Cook, P.A., He, X., et al. (2021). QSIPrep: An integrative pipeline for preprocessing and reconstruction of [[diffusion‑mri]] data.

## Related Software

- [[bids]] — BIDS dataset conversion and curation tool
- [[heudiconv]] — DICOM to BIDS converter
- [[smriprep]] — [[diffusion-mri]] preprocessing
- [[mrtrix3-connectome]] — Advanced [[diffusion‑imaging]] toolkit
- [[datalad]] — Version‑controlled data management

## References

1. L. Fisch, N. Winter, J. Goltermann, Carlotta B. C. Barkhau, D. Emden, J. Ernsting, M. Konowski, R. Leenings, T. Borgers, K. Flinkenflügel, D. Grotegerd, Anna Kraus, E. Leehr, S. Meinert, F. Stein, L. Teutenberg, F. Thomas‑Odenthal, P. Usemann, M. Hermesdorf, H. Jamalabadi, Andreas Jansen, I. Nenadić, Benjamin Straube, T. Kircher, Klaus Berger, Benjamin Risse, U. Dannlowski, T. Hahn. (2026). *deepmriprep: voxel‑based morphometry preprocessing via deep neural networks*. Nature Computational Science. [DOI](https://doi.org/10.1038/s43588-026-00953-7)
2. Sima Soltanpour, Md Taufiq Nasseef, Rachel Utama, Arnold Chang, D. Madularu, Praveen Kulkarni, Craig F. Ferris, Chris Joslin. (2025). *Robust automated preclinical fMRI preprocessing via a multi‑stage dilated convolutional Swin Transformer affine registration*. Frontiers in Neuroscience. [DOI](https://doi.org/10.3389/fnins.2025.1621244)
3. Zhishun Wang, Feng Liu, Rachel Marsh, Gaurav H. Patel, J. Grinband. (2026). *MEPrep: A robust pipeline for multi‑echo fMRI denoising and preprocessing*. Imaging Neuroscience. [DOI](https://doi.org/10.1162/IMAG.a.1198)