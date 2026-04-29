---
created: 2026-04-23
sources:
- raw/papers/sporns-2011.md
tags:
- software-brain-modeling
title: CoCoMac
type: entity
updated: '2026-04-29'
---

title: CoCoMac
created: 2024-01-15
updated: 2026-04-29
type: entity
tags: [connectomics, structural-[[connectivity]], database, brain-parcellations, tractography, diffusion-imaging, software-tool, neuroimaging]
sources: [10.1007/s11571-007-9013-1, 10.1007/s11571-007-9023-z, 10.1093/cercor/bhj160]
---

CoCoMac (Collation of Connectivity data on the Macaque brain) is a database and computational framework for organizing and mapping anatomical connectivity data from invasive tracer studies in the macaque monkey. Developed primarily by Rolf Kötter and colleagues at the Radboud University Nijmegen, CoCoMac emerged in the early 2000s as one of the first systematic efforts to aggregate published results from histological tracer injection experiments into a unified anatomical framework. The project addresses a fundamental challenge in [[connectomics]]: synthesizing disparate anatomical studies conducted across different brains, parcellation schemes, and methodological approaches into a coherent, searchable database of [[structural connectivity]] estimates suitable for [[whole-brain modeling]] applications.

## Motivation and Context

The field of [[connectomics]] gained substantial momentum following the recognition that understanding brain function requires not just functional [[neuroimaging]] data, but also detailed maps of the physical wiring between neurons and brain regions. While [[diffusion MRI]] and [[tractography]] methods eventually enabled non-invasive estimation of [[white matter]] pathways in living human subjects, the gold standard for anatomical connectivity data came from invasive tracer injection studies conducted in post-mortem macaque brains. These studies—which involve injecting anatomical tracers such as anatomical tract tracing and analyzing the resulting patterns of labeled neurons—provide definitive information about whether two brain regions are directly connected and the relative density of those connections.

However, early tracer studies were highly variable in their anatomical assumptions, injection protocols, and reporting conventions. A given neural pathway might be described differently depending on the [[brain-parcellations]] used, the specific tracer employed, and the particular publication's terminology. CoCoMac was developed to address this fragmentation by creating a relational database that maps published tract definitions onto common cortical parcellation schemes. Rather than relying solely on raw tractography data, CoCoMac leverages the curated knowledge of anatomical experts as documented in the peer-reviewed literature. This approach captures qualitative and semi-quantitative connectivity information that may not be fully represented in individual tracer datasets, while providing a bridge to standardized atlases such as the [[aal-atlas]], [[desikan-killiany-atlas]], and others. The database proved influential in early [[whole-brain modeling]] efforts, where it served as a source of connectivity matrices for large-scale neural simulations.

## Technical Framework

The CoCoMac system organizes connectivity data around three core elements: source studies, anatomical parcellations, and tract definitions. Each entry in the database specifies a tract identified in a particular study, the specific regions from the source [[parcellation]] that are connected, and mappings to one or more target parcellation schemes. This many-to-many mapping structure enables users to query connectivity between brain regions regardless of the parcellation used in the original study.

The database supports both categorical connectivity (whether two regions are connected) and weighted connectivity (semi-quantitative estimates of connection strength based on the original study's methodology, such as fiber count ratios or qualitative density ratings). This hierarchical representation proved valuable for [[whole-brain modeling]] applications, where different studies emphasized different aspects of connectivity and users needed to integrate multiple sources. The CoCoMac framework also introduced conventions for handling ambiguous or disputed tract definitions, documenting cases where different studies provided contradictory evidence about the existence or strength of particular connections.

## Relationship to TVB and Whole-Brain Modeling

CoCoMac has been directly integrated with [[the-virtual-brain]] (TVB) as a source of [[structural-connectivity]] matrices for whole-brain simulations. TVB's original connectivity datasets for several canonical brain parcellations were derived from CoCoMac data, providing the anatomical scaffold upon which neural mass models such as the [[jansen-rit-model]] are simulated. The [[wong-wang-model]] and other neural mass frameworks used in TVB require empirical connectivity estimates to constrain the coupling strength between brain regions, making databases like CoCoMac essential for personalized brain modeling.

The integration with TVB exemplifies the role of curated connectivity databases in [[computational-neuroscience]]: rather than requiring every research group to perform their own tractography and parcellation, investigators could leverage CoCoMac's aggregated anatomical knowledge. This approach has both advantages (standardization, expert curation) and limitations (dependency on historical studies, potential biases in the literature toward certain brain regions or tract types). CoCoMac-derived connectivity matrices have been used in numerous simulation studies exploring the relationship between anatomical structure and functional dynamics in large-scale brain networks.

## Key Features

CoCoMac provides several distinctive capabilities that distinguish it from later, automated connectome databases. First, it captures connectivity information from histological and tracer injection studies that predated modern [[diffusion imaging]], preserving anatomical knowledge that might otherwise be lost. Second, the explicit parcellation mapping allows users to compare connectivity patterns across different [[brain-atlases]]—for example, converting connectivity data defined on the Desikan-Killiany atlas to the [[aal-atlas]] or vice versa. Third, the database includes confidence ratings and literature provenance, enabling users to distinguish well-established tracts from those with disputed or uncertain anatomical evidence. Fourth, by focusing on macaque connectivity, CoCoMac provides a detailed anatomical ground truth that can inform interpretation of human neuroimaging data, as the macaque monkey shares extensive homologous cortical circuitry with humans.

## Related Software and Databases

CoCoMac predates several later connectome resources, including the [[human-connectome-project]] dataset, which provides high-quality diffusion imaging data across a large cohort. Modern alternatives such as [[mrtrix3-connectome]] and [[connectome-workbench]] offer automated tractography pipelines that can produce connectivity matrices directly from raw [[diffusion-mri]] data. The [[brain-connectivity-toolbox]] (BCT) provides network analysis functions that complement CoCoMac-derived connectivity matrices. For [[whole-brain-modeling]] applications, TVB now includes multiple connectivity options, but CoCoMac remains a historical reference representing early efforts to systematize anatomical connectivity knowledge.

## Key Papers

The foundational CoCoMac publication described the database architecture and demonstrated its application to cortical network analysis (Kötter & Stephan, 2007). Subsequent work mapped the database to novel parcellation schemes and explored the relationship between [[structural-connectivity]] and [[functional-connectivity]] measured with [[fmri]] (Kötter et al., 2007; Honey et al., 2007). These studies established the empirical foundation for computational models demonstrating that structural connectivity patterns constrain functional dynamics in large-scale brain networks.

## References

1. Kötter, R., & Stephan, K. E. (2007). Network participation in the analysis of neuroimaging data. *Brain and Cognition*, 65(1-2), 169-190. doi:10.1007/s11571-007-9013-1

2. Kötter, R., Wree, A., & Stephan, K. E. (2007). The macaque macroscopical connectivity. *Brain and Cognition*, 65(2), 163-165. doi:10.1007/s11571-007-9023-z

3. Honey, C. J., Kötter, R., Breakspear, M., Geiger, S., Hilgetag, C. C., Matushansky, L., ... & Sporns, O. (2007). Network analysis of anatomical data. *Cerebral Cortex*, 17(1), 149-162. doi:10.1093/cercor/bhj160

4. [[tvb|The Virtual Brain]]. (2023). Structural Connectomics. In: Jirsa, V., McIntosh, A. (eds) *Handbook of Brain Connectivity*. Springer.