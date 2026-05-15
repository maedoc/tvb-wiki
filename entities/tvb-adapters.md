---
created: 2026-04-27
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/ritter-2013.md
- raw/papers/semanticscholar-97e6ff441097.md
- raw/papers/schirner-2018.md
- raw/papers/semanticscholar-9afbfd2d37be.md
- raw/papers/semanticscholar-eb4197c24bf2.md
tags:
- software-tvb-adapters
title: TVB Adapters
type: entity
updated: '2026-05-15'
---

TVB Adapters (tvb-adapters) is the interoperability layer of [[the-virtual-brain]] (TVB) that connects the platform's core simulation engine to external neuroimaging data streams, analysis toolchains, and complementary simulation backends. As an open-source neuroinformatics platform, TVB enables researchers to construct personalized whole-brain models by combining empirical [[structural-connectivity]]—typically derived from [[diffusion-imaging]] [[tractography]]—with biologically realistic [[neural-mass-models]], and to generate synthetic signals corresponding to [[neuroimaging-eeg]], [[neuroimaging-meg]], and [[neuroimaging-fmri]] modalities Sanz Leon et al. (2013). The adapters layer operationalizes this multimodal integration by ingesting subject-specific connectivity matrices and neuroimaging timeseries, feeding them into TVB's simulation pipeline, and exposing the outputs for direct comparison against empirical recordings Ritter et al. (2013). This bidirectional coupling between data and model is essential for [[personalized-brain-modeling]], where individual variations in anatomical structure parameterize virtual brain simulations capable of reproducing subject-specific functional connectivity patterns Ritter et al. (2013).

A concrete instantiation of this pipeline is the automated construction of personalized virtual brains from individual structural MRI and diffusion-weighted imaging data, which integrates [[parcellation]], tractography, and connectivity estimation to produce TVB-ready model inputs with minimal manual intervention Schirner et al. (2018). Beyond single-platform execution, recent efforts to standardize brain network simulation metadata have produced software that generates executable code for multiple simulation platforms and programming languages—including TVB, JAX, and Julia—thereby enhancing [[reproducibility]], comparability, and portability across the broader computational neuroscience ecosystem Leon Martin et al. (2025). Through these ingestion, translation, and export capabilities, TVB Adapters functions as the connective tissue between TVB's simulation core and the wider neuroinformatics landscape, lowering technical barriers for researchers who wish to move from raw neuroimaging data to mechanistic [[whole-brain]] simulations Schirner et al. (2018).

## Key Features

* Core functionality for [[neuroimaging]] and [[computational-neuroscience]] workflows
* Integration with Python ecosystem and neuroimaging toolchains
* Open-source with active community maintenance

## Relationship to Whole-Brain Modeling

TVB Adapters is often used alongside [[tvb]] and other simulation platforms in pre-processing or post-processing pipelines for [[connectome]]-based brain modeling.

## Related Software
* Antspy
* [[arbor]]
* [[bids]] Validator
* Bidscoin
* [[brainstorm]]
[[ Allen SDK]]

## References

1. Sanz Leon et al. (2013). *The Virtual Brain: a simulator of primate brain [[network-dynamics]]*. Frontiers in Neuroinformatics. [DOI](https://doi.org/10.3389/fninf.2013.00010))
2. Ritter et al. (2013). *The Virtual Brain integrates computational modeling and multimodal neuroimaging*. Brain [[connectivity]]. [DOI](https://doi.org/10.1089/brain.2012.0120))
3. R. A. Benn, Ting Xu, R. Mars, Magdalena Boch, Léa Roumazeilles, K. Heuer, Roberto Toro, D. Margulies, J. Manzano-Patrón, Paula Montesinos, C. Galán-Arriola, G. López-Martín, J. Sanchez-González, E. P. Duff, Borja Ibáñez. (2025). *Precon_all: A species-agnostic automated pipeline for non-human cortical surface reconstruction*. bioRxiv. [DOI](https://doi.org/10.1101/2025.04.16.649072))
4. Schirner et al. (2018). *An automated pipeline for constructing personalized virtual brains*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2018.05.040))
5. Leon Martin, Konstantin Bülau, Marius Pille, Rico Schmitt, Christoph Hüttl, J. Meier, Halgurd Taher, Dionysios Perdikis, M. Schirner, L. Stefanovski, [[petra-ritter]]. (2025). *The Virtual Brain Ontology: A Digital Knowledge Framework for Reproducible [[brain-network]] Modeling*. bioRxiv. [DOI](https://doi.org/10.1101/2025.11.19.689211))
6. Amirreza Movahedin, Lennart P. L. Landsmeer, Christos Strydis. (2025). *HUMA: Heterogeneous, Ultra Low-Latency Model Accelerator for The Virtual Brain on a Versal Adaptive SoC*. Symposium on Field Programmable Gate Arrays. [DOI](https://doi.org/10.1145/3706628.3708875))

## ORPHAN PAGE CONTEXT ( Allen SDK)
---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-028f7c6ac41d.md
- raw/papers/ritter-2013.md
tags:
- software
- [[connectomics]]
- [[structural-connectivity]]
- [[diffusion-imaging]]
- neuroimaging-dti
title: Allen SDK
type: entity
updated: '2026-05-05'
---

The [[allen-sdk]] is a software development kit produced by the Allen Institute for Brain Science that provides programmatic access to the institute's brain mapping datasets, particularly the Allen Mouse Brain