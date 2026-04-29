---
created: 2024-01-15
sources:
- raw/papers/semanticscholar-a324c47ea982.md
- raw/papers/semanticscholar-f45e6044c92f.md
- raw/papers/semanticscholar-15c9336be64a.md
tags:
- reproducibility
- software-tvb
- software-nest
- software-brian
- software-neuron
- computational-neuroscience
- neuroimaging
- containerization
- hpc
title: Apptainer
type: entity
updated: '2026-04-29'
---

## Overview

Apptainer is an open-source container platform specifically designed for high-performance computing (HPC) environments, formerly known as Singularity[^1]. Unlike traditional container solutions like Docker, Apptainer was built from the ground up to address the unique security, privilege, and performance requirements of scientific computing clusters and supercomputers. The software enables researchers to package entire computational environments—including operating system, dependencies, libraries, and application code—to within portable, reproducible containers that can be executed reliably across different HPC systems[^2]. Originally developed by Greg Kurtzer and the team at Lawrence Berkeley National Laboratory, Apptainer was donated to the Linux Foundation in 2021 and rebranded to emphasize its application-focused nature rather than the previously used name's connotations[^3]. In the context of [[computational-neuroscience]] and [[whole-brain|whole-brain modeling]], Apptainer has become increasingly important for deploying complex simulation pipelines, ensuring reproducibility of neural modeling experiments, and facilitating the sharing of computational workflows among research collaborators.

## Motivation and Context

The challenge of reproducibility has long plagued computational neuroscience, where subtle differences in software versions, library dependencies, and operating system configurations can produce materially different simulation results[^4]. Traditional virtual machines proved too resource-intensive for HPC environments, while Docker containers required root privileges that are typically unavailable on shared computing clusters. Apptainer emerged as a solution to this fundamental tension: it provides the isolation and reproducibility benefits of containerization while running containers as the unprivileged user, making it compatible with multi-tenant HPC infrastructure. For researchers working with whole-brain simulators like [[the-virtual-brain]], [[nest]], [[brian]], or [[neuron]], Apptainer offers a mechanism to encapsulate the often complex chains of dependencies—ranging from numerical libraries like FFTW to neuroscience-specific tools such as [[neo]] and [[pynest]]—into self-contained units that produce consistent results regardless of the underlying host system. This capability is particularly valuable given the increasing emphasis on reproducibility in neuroimaging and computational neuroscience research, as articulated by initiatives like the [[reproducibility]] movement and standards such as [[bids]].

## Key Features

Apptainer introduces several features that distinguish it from conventional container platforms and make it particularly suited to scientific computing workflows. The most fundamental is its security model: unlike Docker, which requires daemon privileges, Apptainer containers execute entirely within the user's own namespace, eliminating the security concerns that have prevented container adoption on many academic HPC systems[^5]. This design allows researchers to run complex software stacks without requiring system administrator intervention. Apptainer containers are also bind-mounted directly to the host filesystem, enabling seamless access to shared data storage systems common in HPC environments—a critical consideration when working with large [[neuroimaging]] datasets such as those from the [[mrtrix3-connectome]] or [[uk-biobank]]. The platform supports Docker images directly, allowing researchers to leverage the vast ecosystem of existing containerized scientific software while gaining Apptainer's HPC compatibility. Additionally, Apptainer provides a proprietary SquashFS image format that offers efficient storage and rapid instantiation, alongside support for standard OCI (Open Container Initiative) formats[^2].

## Relationship to TVB

Within the [[the-virtual-brain]] ecosystem, Apptainer serves as a recommended deployment mechanism for running TVB simulations on HPC infrastructure. The TVB team provides Apptainer definition files that package the TVB stack—including the [[tvb-library]], [[tvb-multiscale]], and neuroimaging dependencies—into a portable container. This approach addresses one of the persistent challenges in whole-brain modeling: the difficulty of reproducing simulation results across different computing environments due to version drift in dependencies. Researchers can download pre-built Apptainer images from repositories like Sylabs or build them locally from definition files, then execute TVB simulations on clusters at institutions like the [[human-connectome-project]] data processing facilities. The use of Apptainer also facilitates collaborative research by enabling research groups to share identical computational environments, ensuring that when one group publishes results generated within an Apptainer container, others can replicate the exact conditions. This aligns with the broader trend toward containerized neuroscience workflows supported by platforms like [[brainlife]] and [[cbrain]], which increasingly incorporate Apptainer as a runtime option.

## Technical Considerations

Implementing Apptainer in a computational neuroscience workflow requires understanding several technical aspects that differ from traditional container approaches. Building Apptainer images involves creating definition files that specify the base operating system (typically a slim Linux distribution), the installation of system-level dependencies, and the addition of neuroscience-specific software packages. For example, building a container for [[epilepsy modeling]] with [[epileptor]] might start from a minimal Ubuntu base, install Python scientific computing libraries via Conda or pip, add NEST or [[brian2]], and then layer on TVB-specific packages. The resulting .sif (Singularity Image Format) file can be transported to any Apptainer-capable system. Performance considerations are generally favorable—the Apptainer runtime introduces minimal overhead compared to native execution, and the direct filesystem bind-mounting means that large datasets on parallel filesystems can be accessed without the performance penalties associated with Docker volume mounting. However, researchers should be aware of MPI (Message Passing Interface) considerations when running parallel simulations, as proper configuration is required to enable inter-container communication on HPC systems.

## Key Papers

- Kurtzer, G. M., Sochat, V., & Bauer, M. W. (2017). Singularity: Scientific containers for mobility of compute. *PLOS ONE*, 12(5), e0177459. — The original paper describing Singularity/Apptainer's design and motivation.
- Containers and Cloud Computing: From Theory to Practice (various works on HPC containerization standards).

## Related Software and Alternatives

Apptainer exists within a broader ecosystem of container technologies and reproducibility tools relevant to computational neuroscience. Docker remains the most widely used container platform and can be run on Apptainer-compatible systems via Docker-in-Docker or by converting Docker images to Apptainer format. The Python-based [[nipype]] workflow framework complements Apptainer by providing standardized interfaces for neuroimaging tools, and the two can be combined to create highly reproducible analysis pipelines. Other container platforms worth noting include Charliecloud (developed by Los Alamos National Laboratory) and Sarus, both designed for HPC environments with similar security constraints. For pure software deployment without containers, package managers like conda and pip remain popular, though they lack the comprehensive environment encapsulation that containers provide. The [[reproducibility]] challenge in neuroscience has also led to development of specialized solutions like [[datalad]] for data version control and workflow managers like [[snakemake]] that can orchestrate containerized executions. Within the domain of neural simulation, Apptainer complements specialized tools like [[pynest]], [[netpyne]], and the [[modeldb]] database for sharing model specifications.

## References

[^1]: Kurtzer, G. M., Sochat, V., & Bauer, M. W. (2017). Singularity: Scientific containers for mobility of compute. *PLOS ONE*, 12(5), e0177459.

[^2]: Apptainer Documentation. (2024). *Apptainer User Documentation*. Retrieved from https://apptainer.org/docs/

[^3]: Linux Foundation. (2021). *Apptainer Joins the Linux Foundation*. Retrieved from https://www.linuxfoundation.org/

[^4]: Baker, M. (2015). 1,500 scientists lift the lid on reproducibility. *Nature*, 533, 452–454.

[^5]: Kurtzer, G. M. (2016). Singularity: Scientific containers for mobility of compute. *Lawrence Berkeley National Laboratory*. Technical Report.