---
created: 2026-04-20
sources:
- raw/papers/fox-raichle-2007.md
- raw/papers/fox-greicius-2004.md
- raw/papers/fox-herman-2012.md
- raw/papers/fox-buckner-2014.md
- raw/papers/raichle-2001.md
- raw/papers/semanticscholar-f05f8cbafb78.md
- raw/papers/smith-2009.md
tags:
- people-researcher
- brain-stimulation
- functional-connectivity
- connectomics
- neuroimaging-fmri
- resting-state
- network-dynamics
- database-hcp
title: Michael D. Fox
type: entity
updated: '2026-05-13'
---

Michael D. Fox, MD, PhD is a physician-scientist and Professor of Neurology at Harvard Medical School who directs the Center for Brain Circuit Therapeutics at Brigham and Women's Hospital in Boston. His research focuses on mapping and modulating human brain circuits to develop new treatments for neurological and psychiatric diseases. Fox is internationally recognized for his work on [[resting-state-fmri]] and its application to understanding brain stimulation therapies.

## Research Background and Training

Fox received his undergraduate degree in Electrical Engineering from Ohio State University, followed by combined MD and PhD training at Washington University in St. Louis. He completed neurology residency and a movement disorders fellowship at Mass General Brigham. This unique training in electrical engineering, neuroimaging, and clinical neurology provides the foundation for his interdisciplinary approach to brain circuit mapping and neuromodulation.

His clinical practice specializes in both invasive brain stimulation ([[parameter-estimation]]) and non‑invasive brain stimulation ([[parameter-estimation]]) for the treatment of movement disorders, epilepsy, and depression. This dual expertise as a clinician and researcher enables him to directly translate circuit‑level insights into therapeutic interventions.

## Key Research Contributions

### Resting State Functional Connectivity MRI

Fox has made fundamental contributions to the development and application of resting state functional connectivity MRI (fcMRI), a neuroimaging technique that uses spontaneous fluctuations in blood oxygenation to map intrinsic brain networks. His early work demonstrated that the human brain is intrinsically organized into dynamic, anticorrelated functional networks, revealing the [[default-mode-network]] and its anti‑correlation with attention networks. This foundational discovery has become one of the most cited findings in modern neuroimaging.

His influential 2007 review article "Spontaneous fluctuations in brain activity observed with functional magnetic resonance imaging" in Nature Reviews Neuroscience remains a landmark paper in the field, describing how spontaneous low‑frequency oscillations in the [[BOLD-signal]] reflect underlying neuronal activity and can be used to delineate functional brain networks without task performance.

### Lesion Network Mapping

A major innovation from Fox's laboratory is the development of [[network-dynamics]], a technique that uses normative maps of human brain connectivity to understand how focal brain lesions produce neurological and psychiatric symptoms. The key insight is that symptoms from brain lesions often arise from connected brain regions rather than the lesion site itself. By combining lesion locations with human connectome data, Fox's team has mapped symptoms ranging from hallucinations and delusions to disorders of consciousness and involuntary movements.

This approach represented a paradigm shift in connecting symptoms to brain anatomy, moving beyond correlational neuroimaging to causal inference based on lesion‑induced changes. The methodology has been applied to diverse conditions including Parkinson's disease, depression, and disorders of consciousness.

### Brain Stimulation Target Identification

Fox has pioneered the use of human brain connectivity to identify optimal targets for both invasive and non‑invasive brain stimulation. His work demonstrated that the efficacy of [[parameter-estimation]] for depression depends on functional connectivity with the subgenual‑cingulate cortex, establishing a network‑based approach to target selection that has since become standard practice.

Similarly, his research on [[parameter-estimation]] for Parkinson's disease revealed that clinical outcomes are determined by the connectivity of the stimulation site to specific brain networks, rather than just the anatomical location of the electrode. This network‑based framework has led to more precise and effective stimulation protocols such as adaptive DBS that responds to pathological beta oscillations in motor circuits.

## Landmark Publications

Fox's research has produced over 50,000 citations according to Google Scholar as of 2024. His body of work spans foundational discoveries in resting state connectivity, translational applications of fcMRI to brain stimulation, and innovative approaches to mapping symptoms to brain circuits. Among his most influential contributions, the 2005 PNAS paper "The human brain is intrinsically organized into dynamic, anticorrelated functional networks" demonstrated the existence of competing brain networks at rest, fundamentally reshaping understanding of intrinsic brain organization. The 2007 Nature Reviews Neuroscience review provided a comprehensive synthesis of spontaneous fluctuation research that became the definitive reference for the field. His 2012 Biological Psychiatry paper established that [[parameter-estimation]] efficacy for depression is related to intrinsic functional connectivity with the subgenual‑cingulate, pioneering network‑based target optimization. The 2014 PNAS paper "Resting‑state networks link invasive and noninvasive brain stimulation across diverse psychiatric and neurological diseases" offered a unified framework connecting diverse brain stimulation approaches through intrinsic network architecture. The 2018 New England Journal of Medicine review "Mapping symptoms to brain networks with the human connectome" synthesize the lesion network mapping methodology for a clinical audience, demonstrating how focal brain lesions produce symptoms through disruption of distributed networks rather than focal damage.

## Center for Brain Circuit Therapeutics

In 2020, Fox founded the Center for Brain Circuit Therapeutics at Brigham and Women's Hospital, one of the first centers dedicated to translating circuit‑level neuroscience into clinical treatments. The Center integrates expertise from Neurology, Psychiatry, Neurosurgery, and Radiology to comprehensive neuromodulation therapies including [[parameter-estimation]], [[parameter-estimation]], and MRI‑guided focused ultrasound.

The Center represents a unique model for precision neuromodulation, where treatment selection is guided by individual patient symptom profiles mapped onto brain circuits. This approach promises more personalized and effective treatments for patients with refractory neurological and psychiatric conditions.

## Relationship to TVB and Whole‑Brain Modeling

Fox's work is closely related to the mission of The Virtual Brain (TVB) in several important ways. His research on mapping brain symptoms to circuits using the [[human-connectome-project]] data provides essential groundwork for personalized [[whole-brain-modeling]] approaches. The normative connectivity datasets he utilizes, often derived from [[hcp-dataset]], are the same structural connectivity matrices employed in TVB simulations.

The concept of [[functional-connectivity]] emergence from underlying [[structural-connectivity]] is central to both Fox's lesion network mapping and TVB's whole‑brain modeling framework. Fox's demonstrations that stimulation effects propagate through brain networks rather than acting locally align with TVB's network‑based [[neural-mass-model]] approach. Both frameworks recognize that brain dynamics emerge from the interaction between [[connectome]] topology and local [[neural-mass-model]] dynamics—a principle formalized in TVB through the [[jansen-rit]] and [[wong-wang-model]] formulations.

Furthermore, Fox's work on [[brain-stimulation]] target optimization using connectivity profiles parallels TVB's use of [[parameter-estimation]] to identify optimal stimulation sites in personalized brain models. The field of [[epilepsy-modeling]] particularly benefits from this synergy, where TVB's [[epileptor]] model can be combined with Fox's connectivity‑based target selection to optimize responsive neurostimulation.

Fox's conceptual framework intersects with [[dynamic-causal-modeling]] (DCM) through shared interests in inferring effective connectivity from neuroimaging data. While DCM employs variational Bayes for model inversion, Fox's lesion network mapping provides a complementary causal framework for understanding brain‑circuit dysfunction. The integration of his network mapping approaches with TVB's simulation capabilities offers promising avenues for improving neuromodulation therapies.

## Related Concepts

- [[functional-connectivity]] — The correlation patterns in brain activity that Fox maps using fcMRI
- [[structural-connectivity]] — The anatomical wiring that underlies functional networks
- [[connectome]] — The comprehensive map of neural connections that Fox uses for lesion mapping, also central to TVB's [[whole-brain-modeling]] approach
- [[brain-network]] — Intrinsic networks like the [[default-mode-network]] that Fox identified
- [[resting-state]] — The baseline brain activity that Fox's fcMRI methods examine
- [[brain-stimulation]] — The broader field of neuromodulation Fox pioneers, including both [[parameter-estimation]] (invasive) and non‑invasive approaches
- [[human-connectome-project]] — The source of connectivity data that enables Fox's methods
- [[personalized-brain-modeling]] — The approach of tailoring models to individual patients
- [[neural-mass-model]] — Population‑level models used in TVB that align with Fox's network‑based framework
- [[epilepsy-modeling]] — Clinical application domain where Fox's connectivity work complements TVB's simulation approaches
- [[dynamic-causal-modeling]] — Related framework for studying effective connectivity, with complementary causal inference approaches

## References

1. (authors unknown). *Spontaneous fluctuations in brain activity observed with functional magnetic resonance imaging*.
2. (authors unknown). *A Default Mode of Brain Function*.
3. Abdoreza Asadpour, Amin Azimi, Kongfatt Wong-Lin. (2025). *Limitations of Variational Laplace-Based Dynamic Causal Modelling for Multistable Cortical Circuits*. bioRxiv. [DOI](https://doi.org/10.1101/2025.03.10.642327)
4. (authors unknown). *Correspondence of the brain's functional architecture during activation and rest*.