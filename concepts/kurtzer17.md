---
created: 2026-05-06
sources:
- raw/papers/kurtzer17.md
tags:
- reproducibility
- containerization
- software-tools
- software-apptainer
- hpc
- singular-containers
title: Kurtzer et al. 2017 (Singularity)
type: concept
updated: '2026-05-07'
---

# Kurtzer et al. 2017 (Singularity)

The paper "Singularity: Scientific containers for mobility of compute" by Kurtzer, Sochat, and Bauer, published in 2017 in PLOS ONE, introduced the Singularity container platform specifically designed for high-performance computing (HPC) environments. Unlike general-purpose container solutions, Singularity was architected from the ground up to address the unique security, privilege, and interoperability requirements of scientific computing on cluster and supercomputer systems. The publication became a foundational reference for containerization in [[computational-neuroscience]], [[neuroimaging]], and broader scientific research, enabling researchers to create portable, reproducible computational environments that could seamlessly execute across diverse computing infrastructure—from individual laptops to national HPC facilities.

## Motivation for Scientific Containerization

Traditional container technologies, particularly Docker, revolutionized software deployment by packaging applications with their dependencies into portable images. However, Docker's design assumed a host where the user has [[root]] privileges and can run a daemon—a model incompatible with multi-user HPC environments where users submit jobs through schedulers like SLURM, PBS, or SGE without elevated privileges. The security model of Docker also created concerns on shared computing resources, as containers running as root could potentially escape their isolation and access the host system. These limitations meant that the reproducibility benefits of containers were largely inaccessible to academic researchers working on institutional clusters, who constituted a significant portion of the computational neuroscience community.

The Singularity project addressed these constraints by implementing a fundamentally different architectural approach. Containers in Singularity run as the invoking user without requiring root access on the host system, and the container runtime is designed to be invoked directly rather than through a daemon. This design preserves the security model of the underlying HPC system while still providing complete isolation of the containerized environment. The containers can be built on any system (where root access may be available) and then transported to and executed on any HPC cluster without modification—a capability that Kurtzer and colleagues termed "mobility of compute."

## Technical Architecture and Key Features

Singularity achieves containers by encapsulating the entire filesystem within a single squashfs or ext3 image file, which is mounted directly by the Singularity runtime rather than using layered filesystem union approaches. This single-file approach offers several advantages for scientific computing: images can be easily transferred between systems using standard file transfer mechanisms, the entire computational environment is self-contained including all libraries and system dependencies, and the immutable image format prevents runtime modifications that could introduce non-determinism. The build process can either start from a Docker image (enabling access to the vast Docker Hub ecosystem) or from a definition file specifying the precise contents of the container.

A defining feature of Singularity is its approach to host system integration. Unlike Docker containers which typically run in isolated network namespaces, Singularity containers by default share the host's network namespace and can bind-mount specific host directories into the container. This design enables natural interaction with HPC job schedulers, where the container can access the scheduler's allocated resources, output files, and existing data stores without special configuration. The container can also access graphics devices for GPU acceleration, making Singularity particularly valuable for [[machine-learning]] workloads common in modern neuroimaging analysis.

The paper demonstrated Singularity's capabilities through several scientific computing case studies, including molecular dynamics simulations, bioinformatics pipelines, and neuroimaging analysis workflows. Each case study illustrated how a container built on a developer's laptop could be deployed unchanged on remote HPC resources, eliminating the common "it works on my machine" problem that plagues scientific software distribution.

## Impact on Computational Neuroscience and Neuroimaging

The publication of the Singularity paper coincided with a critical period in computational neuroscience and neuroimaging, as the field was grappling with widespread reproducibility concerns. Whole-brain modeling workflows using platforms like [[the-virtual-brain]] require complex dependencies spanning neuroscience simulators, neuroimaging toolkits, and statistical analysis packages—each with potentially conflicting version requirements. A simulation built with a specific combination of [[brian2]], [[numpy]], and [[nipype]] versions might produce subtly different dynamics when run with updated packages, making exact reproduction challenging.

Singularity provided the missing infrastructure for addressing these challenges. Research groups could now containerize their entire analysis pipeline—from raw [[dti]] or [[fmri]] data through connectivity matrix construction to final simulation—and share the container image alongside their published results. This capability proved particularly valuable for large consortium efforts like the [[human-connectome-project]] and [[uk-biobank]], where data processed by multiple sites needed to yield comparable results regardless of the local computing environment. The container approach also facilitated [[bids]]-compliant preprocessing pipelines like [[fmriprep]] and [[qsiprep]], which distributed their software as Singularity images to ensure consistent results across the neuroimaging community.

## Relationship to TVB and Whole-Brain Modeling

In the context of [[the-virtual-brain]] and [[whole-brain-modeling]], Singularity containers enable several critical workflows. First, they provide a mechanism for sharing complete simulation environments—the container can include not just the TVB libraries but also the exact versions of supporting packages like [[tvb-library]], [[numpy]], [[scipy]], and [[matplotlib]] that collectively determine simulation behavior. Researchers can thus share not just their connectivity matrices and parameter settings but the complete computational environment needed to reproduce their findings.

Second, containerization supports the personalized brain modeling paradigm that TVB enables. A researcher developing a personalized model for a specific clinical application—say, [[epilepsy-modeling]] or [[alzheimers-modeling]]—can containerize the entire processing pipeline: from [[dicom]] or [[bids]] data ingestion, through tractography and connectivity estimation using [[mrtrix3]] or [[dipy]], to TVB simulation with disease-specific parameter configurations. This container can then be shared with clinical collaborators who lack the technical expertise to install the complex dependencies, or executed on computing clusters with different software configurations.

Third, Singularity containers facilitate large-scale parameter sweeps and validation studies that require running many simulations under controlled conditions. By ensuring every simulation uses identical software versions, containers eliminate one potential source of variability in these computationally intensive studies. The ability to run on GPU-equipped HPC nodes through Singularity's NVIDIA Docker compatibility also enables acceleration of computationally demanding simulations.

## Relationship to Related Concepts

The Singularity platform connects to several other concepts in this wiki. It represents a core technology under [[reproducibility]], providing the technical foundation for portable computational environments. The development of Singularity catalyzed the broader [[containerization]] movement in scientific computing, which also includes alternatives like [[apptainer]] (the renamed open-source project after Singularity's commercial bifurcation) and Docker for local development. The container approach complements [[datalad]] and [[datalad-containers]] for integrated data and environment management, and integrates with workflow tools like [[snakemake]] and [[pydra]] for pipeline orchestration.

Singularity containers are used extensively in the [[neurodesk]] ecosystem for ready-to-use neuroimaging analysis environments and in platforms like [[brainlife]] for cloud-based processing. The technology also underlies the growing availability of containerized neuroscience simulators including [[nest]], [[brian2]], and [[the-virtual-brain]], enabling researchers to run these simulations without manual dependency management.

## Limitations and Evolution

While Singularity represented a significant advance for scientific computing, it has limitations worth noting. The single-image approach means that unlike Docker's layered filesystem, containers cannot share common base layers efficiently when many images are stored on a system. The build process, while straightforward, still requires some familiarity with Linux system administration and the Singularity definition file format. These factors created barriers for researchers seeking the lowest-possible entry barrier to reproducible computing.

The technology landscape has also evolved since the 2017 publication. The Singularity project was later rebranded as Apptainer under the Linux Foundation, maintaining the core architecture while improving governance and community support. Docker has implemented rootless mode options that partially address the HPC compatibility concerns. Alternative approaches like Nix and Guix provide purely declarative environments without container encapsulation. Despite these developments, Singularity remains widely deployed on HPC systems worldwide and continues to serve as a foundational reference for containerization in scientific computing.