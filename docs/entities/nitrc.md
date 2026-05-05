---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
tags:
- software
- neuroimaging
- neuroimaging-fmri
- neuroimaging-eeg
- neuroimaging-meg
- neuroimaging-dti
- reproducibility
- software-bct
- software-fsl
- software-spm
title: NITRC-CE
type: entity
updated: '2026-05-05'
---

# NITRC-CE

## Overview

[[nitrc-ce]] ([[neuroimaging]] Informatics Technology Initiative – Computational Environment) is a containerized computing platform designed to provide researchers with ready-to-use, reproducible neuroimaging analysis environments. Developed as part of the NITRC family of resources, NITRC-CE delivers pre-configured Docker containers bundled with widely-used neuroimaging software packages, enabling practitioners to launch computational workflows without the typically cumbersome process of manual software installation and dependency management. The platform is maintained by the Neuroimaging Informatics Technology Initiative, a community resource originally funded by the NIH Blueprint for Enhancing the Development of Neuroimaging Technologies [1].

## Technical Implementation

NITRC-CE leverages container virtualization through Docker to package complete software stacks that include core neuroimaging toolkits such as [[pysurfer]], [[fsl-melodic]], [[SPM]], [[mrtrix3-connectome]], [[mne-bids-pipeline]], [[eeglab]], dipy, and numerous additional specialized packages. Each container image is built following best practices for neuroimaging workflows, ensuring that software versions are pinned and compatible with each other. This approach addresses one of the most persistent challenges in computational neuroscience: the "dependency hell" that arises when trying to coordinate the diverse software packages required for a typical neuroimaging analysis pipeline, particularly those involving multimodal data integration [2].

The computational environment supports full neuroimaging workflows spanning [[structural connectivity|diffusion tensor imaging (DTI)]] tractography, [[functional connectivity|fMRI resting-state analysis]], [[EEG]] and [[MEG]] source reconstruction, and voxel-based morphometry. Researchers can instantiate pre-built containers that include complete software ecosystems—for example, a container containing both [[fsl-melodic]] and [[mrtrix3-connectome]] for integrated diffusion analysis, or another bundling [[mne-bids-pipeline]] with [[eeglab]] for electrophysiology preprocessing. This modular design allows users to select precisely the software combination needed for their specific analysis pipeline.

## Relationship to TVB

NITRC-CE provides a valuable infrastructure for whole-brain modeling workflows using [[The Virtual Brain]] (TVB). When researchers need to prepare empirical brain connectomes for TVB simulations—such as generating structural connectivity matrices from [[diffusion MRI]] tractography or processing [[fMRI]] time series for model calibration—NITRC-CE containers can provide the necessary software environment without conflicts [3]. The platform's reproducibility guarantees are particularly relevant for TVB users who need to document and share exact software versions used to generate connectivity data that feeds into whole-brain simulations. This integration path has been utilized in several studies combining empirical connectivity analysis with computational modeling.

## Key Features

What distinguishes NITRC-CE from general-purpose container platforms is its curated, domain-specific software curation. Unlike generic Docker Hub images that may lack neuroimaging-specific configuration, NITRC-CE containers are built with neuroimaging workflows in mind, including proper environment variables, working configurations for common software interactions, and tested interoperability between co-installed packages. The platform also provides documentation and community support through the broader NITRC ecosystem, helping researchers—particularly those less experienced with command-line tools—successfully launch complex neuroimaging analyses. The community-driven nature of the platform ensures that new software packages are periodically added as the neuroimaging field evolves.

## Relationship to Other Resources

NITRC-CE occupies a niche distinct from both general container registries and integrated neuroimaging platforms. Compared to [[brainlife]]—which offers a fully-managed cloud computing service with graphical interface—NITRC-CE provides more granular control suitable for users comfortable with command-line execution. Unlike [[neuromorpho-toolkit]], which similarly provides containerized neuroimaging software environments, NITRC-CE emphasizes accessibility for the broader research community and maintains close integration with the original NITRC software repository [2]. The platform complements resources like [[BIDS]] and [[datalad]] by providing the computational environment in which these data standards can be operationalized. NITRC-CE also relates to [[NITRC]] proper (the original software repository), which serves as the distribution mechanism for the container images.

## Related Software

- [[NITRC]]
- [[brainlife]]
- [[neuromorpho-toolkit]]
- [[datalad]]
- [[BIDS]]
- [[pysurfer]]
- [[fsl-melodic]]
- [[SPM]]
- [[the-virtual-brain]]

## Key Papers

- Neuroimaging Informatics Technology Initiative. "NITRC: Neuroimaging informatics tools repository." Frontiers in Neuroinformatics (2012).
- Gorgolewski, G., et al. "NITRC-CE: A containerized computational environment for neuroimaging." Neuroinformatics (2017).
- Sanz Leon, P., et al. "[[tvb|The Virtual Brain]]: a simulator of primate brain [[network-dynamics]]." Neuroinformatics (2013).

## References

[1] Neuroimaging Informatics Technology Initiative. "NITRC: Neuroimaging informatics tools repository." *Frontiers in Neuroinformatics* 6 (2012): 7.

[2] Gorgolewski, G., et al. "NITRC-CE: A containerized computational environment for neuroimaging." *Neuroinformatics* 15, no. 1 (2017): 51-58.

[3] Sanz Leon, P., et al. "The Virtual Brain: a simulator of primate [[brain-network]] dynamics." *Neuroinformatics* 11, no. 1 (2013): 49-64.