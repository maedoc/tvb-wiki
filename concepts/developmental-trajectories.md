---
created: 2026-04-20
sources:
- raw/papers/gogtay-2004.md
- raw/papers/fair-2009.md
- raw/papers/power-2010.md
- raw/papers/tau-peterson-2010.md
- raw/papers/semanticscholar-34ef3bcd7c8b.md
tags:
- neurodevelopment
- personalized-brain-modeling
- plasticity
- critical-periods
- aging
- whole-brain-modeling
- neuroimaging-fmri
- neuroimaging-dti
- neural-mass-models
- network-dynamics
title: Developmental Trajectories
type: concept
updated: '2026-05-04'
---

Developmental trajectories describe the patterns of change in brain structure and function across the lifespan, from prenatal development through aging. These trajectories are often non-[[linear]], with different brain regions following distinct developmental curves that reflect the complex interplay between genetic programs and experience-dependent plasticity. Understanding these trajectories is essential for building biologically realistic [[whole-brain-modeling|[[whole-brain]] models]] that can accurately represent age-specific neural dynamics, predict individual outcomes, and identify deviations that may indicate developmental disorders.

## Definition and Theoretical Foundations

A developmental [[trajectory]] is the path of change in a brain measure over time, characterizing how structure, function, or [[connectivity]] evolve across age. Trajectories can be linear or non-linear, and vary across individuals and brain regions. The study of developmental trajectories emerged from longitudinal [[neuroimaging]] studies that revealed the brain is not a static organ but undergoes continuous reorganization throughout life. This understanding has profound implications for both basic neuroscience and clinical applications, as it provides a framework for understanding typical development and identifying atypical patterns that may benefit from early intervention.

The conceptual foundation for developmental trajectories draws upon several theoretical frameworks. [[neurodevelopment]] encompasses the entire process of brain formation and refinement, from neural tube closure in embryogenesis through the complex synaptic pruning and myelination that continues into the third decade of life. [[plasticity]] refers to the brain's capacity to modify its structure and function in response to experience, and this capacity varies across the lifespan—being highest in early development (critical periods), remaining elevated during adolescence, and declining in adulthood and aging.

## Trajectory Patterns

### Linear Trajectories

Linear trajectories represent a constant rate of change in brain measures over time, manifesting as either simple increases or decreases. These patterns are relatively rare in brain development, as most biological processes involve more complex dynamics. However, some aspects of aging, particularly the gradual loss of brain volume in later life, can be approximated by linear decline in the absence of neurodegenerative disease. Linear models are computationally simpler and can serve as reasonable approximations when the timescale of interest is short relative to the total developmental span, or when the phenomenon of interest shows minimal non-linearity within the observed window.

### Non-Linear Trajectories

The majority of developmental processes follow non-linear trajectories, reflecting the cascade of biological events that characterize brain maturation. Several canonical patterns have been identified across numerous neuroimaging studies:

**Inverted U-shape trajectories** represent perhaps the most characteristic pattern in brain development, capturing processes that initially increase rapidly and then decline. This pattern is exemplified by synaptic density, which reaches peak levels in early childhood followed by extensive pruning that continues through adolescence. Some cognitive functions also follow this pattern, showing improvements through childhood and adolescence before reaching a plateau or experiencing modest decline in older age. The inverted U-shape reflects the fundamental developmental process of exuberant growth followed by selective elimination—a principle that applies across neural systems from synaptic connections to large-scale [[functional-connectivity|functional networks]].

**U-shape trajectories** are less common in brain measures but appear in certain contexts where an initial decrease is followed by recovery. These patterns can emerge in response to environmental challenges or during recovery from injury, where initial disruption gives way to compensatory reorganization.

**Logarithmic trajectories** capture rapid early change that subsequently slows, approaching an asymptote. [[structural-connectivity|White matter]] development follows this pattern reasonably well, with rapid myelination in the first years of life that continues at a diminishing rate through adolescence and into adulthood. Similarly, language acquisition shows logarithmic dynamics, with rapid vocabulary growth in early childhood that decelerates as the language system matures.

**Sigmoidal trajectories** exhibit slow-fast-slow dynamics, with an initial slow phase, a period of rapid change, and a final plateau. Pubertal development exemplifies this pattern, as the hormonal changes that trigger puberty produce rapid neurological changes during adolescence that stabilize in early adulthood. Some structural brain measures also show sigmoidal patterns as they approach biological limits.

## Regional Differences in Cortical Development

### The Gogtay et al. (2004) Framework

The landmark longitudinal study by Gogtay et al. (2004) established the spatial-temporal pattern of human cortical development using repeated MRI scans of 13 children followed from ages 4 to 21 years. This work revealed that cortical maturation follows a hierarchical "back-to-front" pattern, with phylogenetically older regions maturing before newer ones. The study demonstrated that cortical thinning, far from representing mere loss, reflects the coordinated processes of synaptic pruning and myelination that refine neural circuitry.

**Primary regions** (sensory and motor cortex) demonstrate the earliest maturation, reaching peak thickness in middle childhood and then gradually declining. These regions mature first because they are essential for basic sensorimotor function and have relatively straightforward computational demands. Their earlier maturation also reflects their earlier phylogenetic development, as sensory and motor cortices are conserved across mammalian evolution.

**Association regions** (temporal and parietal cortex) show intermediate maturation, with peak thickness reached during adolescence. These regions support higher-order functions such as language, spatial cognition, and integrative sensory processing, and their longer developmental window provides extended opportunity for experience-dependent refinement.

**Prefrontal cortex** exhibits the latest maturation, with peak development in early adulthood (third decade) followed by a steeper decline than other regions. The prolonged development of prefrontal cortex reflects its role in executive functions, working memory, and impulse control—cognitive capacities that continue to develop into the third decade of life and that benefit fromextended experience-dependent plasticity.

### White Matter Development

[[white-matter]] development follows a distinct temporal pattern characterized by early rapid myelination, continued maturation through adolescence, and gradual decline in later adulthood. Diffusion tensor imaging (DTI) studies have shown that [[fractional-anisotropy]] increases while mean diffusivity decreases during childhood and adolescence, reflecting theongoing process of myelination andaxonal packing. The development of white matter tracts follows a roughly posterior-to-anterior gradient, with sensory and motor pathways maturing before frontal pathways—a pattern consistent with the cortical thickness findings from Gogtay et al. This sequence has implications for the development of [[functional-connectivity|functional connectivity]], as white matter tract integrity constrains the strength and timing of inter-regional communication.

## Network Trajectories

### Functional Connectivity Development

The work of [[damien-fair|Fair et al.]] (2009) demonstrated that functional brain networks undergo a fundamental organizational transformation from a "local to distributed" configuration across development. Using resting-state [[fmri]] in 210 participants aged 7-31, the authors found that children show predominantly short-range, locally clustered connections, while adults show stronger long-range connections linking distant brain regions. This shift reflects the ongoing process of [[neurodevelopment|neural development]], where initial local circuits are refined and integrated into distributed networks capable of sophisticated information processing.

The default mode network (DMN) exemplifies these developmental changes. In children, DMN activity is more localized, while in adolescents and adults, the DMN shows more distributed patterns and stronger correlations with other networks, particularly the frontoparietal attention network. These changes parallel improvements in cognitive control and the ability to flexibly switch between internal (self-referential) and external (task-oriented) processing modes.

### Network Topology

Power et al. (2010) (2010) provided a comprehensive review of how large-scale [[brain-network]] topology develops across childhood and adolescence. Several key metrics show characteristic developmental patterns:

**Modularity** increases from childhood through adolescence, reflecting the differentiation of functionally specialized subnetworks within the broader brain network. This increase in modularity represents a refinement of functional segregation, where different network modules become more specialized for specific cognitive processes while maintaining integration through hub regions.

**Small-world properties** evolve with development, with children showing more random network configurations and adults showing more organized small-world topology. This maturation reflects the balance between local efficiency (via dense short-range connections) and global integration (via long-range hub connections).

**Hub organization** strengthens during development, with the [[rich-club]] coefficient increasing as hub regions become more densely interconnected. This maturation supports efficient global communication across the brain network and is thought to underlie the improved cognitive flexibility seen in adulthood. The development of hub structure is closely tied to white matter maturation, as long-range white matter tracts provide the anatomical substrate for hub connectivity.

## Individual Differences and Moderators

### Genetic and Environmental Influences

Developmental trajectories are shaped by the interplay of genetic predisposition and environmental experience. Heritability studies have shown that many brain structural measures show moderate to high heritability, meaning that a substantial proportion of individual variation in trajectory shape is explained by genetic factors. However, experience-dependent changes remain substantial, and environmental factors including nutrition, cognitive stimulation, physical activity, and stress can significantly modify developmental trajectories.

Sex differences in development emerge during puberty, with hormonal changes influencing the timing and pace of brain maturation. Studies have shown that some aspects of cortical development proceed slightly earlier in females than males, though the functional significance of these differences remains an active area of investigation. Socioeconomic status also influences developmental trajectories, with differences in access to cognitive enrichment, healthcare, and nutritional resources contributing to variation in brain development outcomes.

### Sensitive and Critical Periods

[[plasticity]] is not uniform across development but is concentrated in specific windows termed sensitive periods and critical periods. Sensitive periods represent windows of heightened plasticity during which experience has maximal impact on development, but where development can proceed reasonably well even in the absence of typical experience. Critical periods are stricter time-limited windows where experience is essential for normal development, and where deprivation leads to irreversible deficits.

Classic examples of critical periods include the visual system, where normal binocular vision requires exposure to visual stimuli during infancy, and language acquisition, where exposure to language in early childhood is necessary for normal linguistic development. More recent research has identified sensitive periods for social development, with attachment relationships in infancy shaping social-cognitive capacities throughout life. These periods have important implications for intervention, as the timing of therapeutic approaches can substantially influence outcomes.

## Implications for Whole-Brain Modeling

### Age-Specific Models

Understanding developmental trajectories is essential for building biologically realistic [[whole-brain-modeling|whole-brain models]]. Age-specific models require different parameter values that reflect the underlying neurobiology of the target developmental stage. A model of a 10-year-old child should differ from a model of a 30-year-old adult not merely in parameter values but in the fundamental dynamics that those parameters produce, reflecting the different balances of excitation and inhibition, pruning and myelination, and local versus distributed connectivity that characterize different developmental stages.

Neural mass models and [[neural-mass-models|neural mass]] approaches can incorporate developmental trajectories through age-dependent parameter functions that capture the non-linear changes in synaptic parameters, delays, and coupling strength that characterize brain maturation. Extensions to [[dynamic-causal-modeling|dynamic causal modeling]] can similarly incorporate developmental changes in [[effective-connectivity]], allowing researchers to test hypotheses about how the causal structure of brain networks changes across development.

### Individual Prediction and Personalized Models

Developmental trajectories provide the foundation for [[personalized-brain-modeling|personalized brain models]] that can forecast individual outcomes and identify atypical development. By establishing norms for typical trajectories, deviations can be detected early—when intervention is most effective—and personalized models can be used to simulate the effects of different intervention strategies. This approach has particular promise for neurodevelopmental disorders such as autism spectrum disorder and schizophrenia, where early identification and personalized intervention may improve long-term outcomes.

### Lifespan Models

Comprehensive whole-brain models must account for the full lifespan trajectory from development through aging. This requires integrating the inverted U-shaped developmental trajectories of childhood and adolescence with the approximately linear or accelerating declines of aging. Models that capture this full lifespan dynamics can address questions about how early-life experiences influence later-life brain health, and how the brain maintains function or succumbs to decline across the lifespan.

## Related Concepts

- [[neurodevelopment]] – The broader process of brain formation and refinement
- [[aging]] – Later-life changes in brain structure and function
- [[plasticity]] – Experience-dependent structural and functional changes
- [[critical-periods]] – Time-limited windows of essential experience
- [[personalized-brain-modeling]] – Individual-specific computational models
- [[functional-connectivity]] – Correlated activity between brain regions
- [[structural-connectivity]] – Anatomical white matter connections
- [[modularity]] – Network organization into specialized subnetworks
- [[network-hubs]] – Highly connected regions that integrate networks
- [[whole-brain-modeling]] – Large-scale computational models of [[brain-dynamics]]
- [[resting-state]] – Intrinsic brain activity measured without task
- [[default-mode-network]] – Network active during rest and self-referential processing
- [[nonlinear-dynamics]] – Mathematical framework for complex time-dependent systems

## References

1. (authors unknown). *Dynamic Mapping of Human Cortical Development During Childhood Through Early Adulthood*.
2. (authors unknown). *Functional Brain Networks Develop from a 'Local to Distributed' Organization*.
3. (authors unknown). *The Development of Human Functional Brain Networks*.
4. (authors unknown). *Normal Development of Brain Circuits*.
5. Tingting Liu, Mingyang Li, Y. You, Hongxi Zhang, Ying Lv, Chai Ji, Yuting Li, Dan Wu, Shenghong Ju. (2026). *Maturation and reorganization of structural connectivity in infants within half a year*. NeuroImage. [DOI](https://doi.org/10.1016/j.neuroimage.2026.121728)