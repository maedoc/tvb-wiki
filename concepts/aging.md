---
created: 2026-04-20
sources:
- raw/papers/buckner-2004.md
- raw/papers/grady-2012.md
- raw/papers/damoiseaux-2008.md
- raw/papers/fjell-walhovd-2010.md
- raw/papers/semanticscholar-b63e3d8a1467.md
tags:
- aging-brain
- neuroimaging-fmri
- neuroimaging-dti
- cognitive-reserve
- brain-maintenance
- functional-connectivity
- structural-connectivity
- whole-brain-modeling
- resting-state
- default-mode-network
- developmental-trajectories
- neural-mass-models
title: Brain Aging
type: concept
updated: '2026-04-28'
---

Brain aging encompasses the progressive structural, functional, and connectomic changes that occur in the human brain from early adulthood through senescence. Unlike neurodevelopment, which is characterized by growth and integration, aging involves a complex interplay of decline and adaptation—both normative losses in gray matter volume, white matter integrity, and [[functional-connectivity]], as well as compensatory reorganizations that allow many older adults to maintain cognitive function. Understanding these trajectories is essential for [[whole-brain|whole-brain modeling]] approaches that aim to simulate individual brains, as age-related parameter changes fundamentally alter [[network-dynamics]], synchronization properties, and the brain's computational capacity.

## Definition and Scope

Brain aging represents a lifespan process beginning in the third decade of life, though the rate and magnitude of changes vary substantially across individuals and brain regions. The field distinguishes between normal aging, which involves predictable but benign changes, and pathological aging associated with neurodegenerative diseases such as Alzheimer's disease. Critically, aging is not a uniform process: some circuits and cognitive systems show remarkable preservation while others exhibit marked decline. This heterogeneity poses both a challenge and an opportunity for [[personalized-brain-modeling]], as individual differences in aging trajectories must be captured by computational models to make accurate predictions about cognitive outcomes and disease progression.

## Structural Changes

### Gray Matter Alterations

The cortex undergoes gradual thinning throughout adulthood, with approximately 0.5-1% annual loss in cortical volume after age 50. However, this decline is highly heterogeneous: prefrontal regions show greater susceptibility than primary sensory and motor cortices, following a posterior-to-anterior gradient that mirrors the pattern of myelination in reverse. These regional variations reflect differential vulnerability of neuronal subpopulations, with larger pyramidal neurons in prefrontal cortex showing particular sensitivity to age-related synaptic loss.

Ventricular enlargement provides a reliable proxy for global brain volume loss, with lateral ventricles expanding approximately 3-5% per decade after age 40. This expansion reflects the combined effects of gray matter reduction and [[white-matter]] loss, and accelerated ventricular enlargement is associated with poorer cognitive outcomes and increased risk for neurodegenerative disease.

### White Matter Degradation

Diffusion tensor imaging studies reveal progressive decline in [[fractional anisotropy]] and increases in mean diffusivity with age, indicating degradation of white matter microstructure. These changes follow tract-specific patterns: long-range association fibers such as the uncinate fasciculus and cingulum bundle show earlier and more pronounced alterations than short-range intra-hemispheric connections. The vulnerability of specific pathways likely reflects both intrinsic properties of myelinated axons and vascular contributions, as white matter hyperintensities on T2-weighted MRI accumulate preferentially in periventricular and deep white matter regions.

Notably, age-related white matter changes differ fundamentally from those observed in [[neurodevelopment]]: whereas developmental processes involve progressive myelination and fiber strengthening, aging involves demyelination, axonal loss, and disrupted node architecture in large-scale brain networks.

## Functional Changes

### Resting-State Network Alterations

Aging profoundly affects large-scale brain networks, with particularly consistent findings in the [[default-mode-network]] (DMN). The DMN, which is active during internally-directed cognition and shows reduced activity during external task demands, exhibits decreased internal [[functional-connectivity]] with advancing age. Specifically, the correlation between posterior cingulate cortex and medial prefrontal cortex weakens substantially after age 60, and this reduction predicts poorer performance on episodic memory and executive function tasks.

The seminal study by Andrews-Hanna and colleagues (2007) established DMN [[connectivity]] as a sensitive biomarker of brain aging, demonstrating that older adults with higher connectivity maintained better cognitive function. Subsequent work has extended these findings to show that network-level changes are not limited to the DMN but also involve frontoparietal control networks and salience networks, with complex reconfiguration patterns that sometimes show increased internetwork connectivity [[compensation]].

### Compensatory Reorganizations

Older adults frequently recruit additional neural resources to maintain cognitive performance—a phenomenon termed neural compensation. This compensation manifests as increased bilateral activation during unilateral tasks, recruitment of prefrontal regions during episodic memory retrieval, and elevated activation during challenging cognitive operations. Grady's comprehensive review (2012) synthesized [[neuroimaging]] evidence for functional reserve, demonstrating that the ability to compensate predicts cognitive outcomes better than raw brain structure.

However, compensation is not without limits: when pathology exceeds the capacity for reorganization, compensation fails and cognitive decline becomes evident. This framework, developed by Buckner and colleagues and formalized by Cabeza et al. (2018), provides a theoretical foundation for understanding individual differences in aging trajectories.

## Theoretical Frameworks

### The Reserve, Maintenance, and Compensation Framework

The conceptual framework distinguishing [[brain-maintenance]], [[cognitive-reserve]], and compensation provides the dominant theoretical structure for understanding aging outcomes. Brain maintenance refers to the preservation of brain structure and function, with individuals exhibiting less age-related change demonstrating superior maintenance. This preservation is influenced by genetic factors (including [[APOE]] status), education, cardiovascular health, and lifestyle factors such as physical exercise and cognitive engagement.

Cognitive reserve represents the capacity to withstand pathology through pre-existing neural resources. Two forms are distinguished: passive reserve (structural [[brain-reserve]], including brain size and [[neuron]] count) and active reserve (the efficiency and capacity of cognitive networks). Compensation involves the recruitment of additional brain regions or alternative neural circuits to maintain function—a dynamic process that requires both structural integrity and flexibility in network reconfiguration.

## Role in Whole-Brain Modeling

Incorporating age-related changes into whole-brain models requires systematic modification of multiple parameter classes. At the level of [[neural-mass-models]], synaptic time constants tend to lengthen with age, reflecting altered calcium dynamics and neurotransmitter availability. Connection strengths between regions must be adjusted to reflect empirical findings on [[structural-connectivity]] decline, with connection density reduced particularly in long-range pathways. Network topology shifts toward less efficient configurations, with reduced [[small-world-networks]] properties and altered hub architecture.

Computational models incorporating these parameters have been used to predict cognitive decline trajectories, simulate dementia progression particularly in Alzheimer's disease, and identify modifiable lifestyle factors that promote [[successful-aging]]. The [[dynamic-causal-modeling]] framework has proved particularly valuable for characterizing age-related changes in [[effective-connectivity]], demonstrating both reduced feedforward connectivity and altered feedback modulation.

Applications to personalized modeling involve fitting individual parameters to empirical neuroimaging data—including regional volumes, white matter integrity measures, and [[resting-state]] connectivity patterns—to generate predictions about future cognitive trajectories or responses to interventions. This approach requires careful attention to the non-stationarity of [[brain-dynamics]] with age, as the same model structure may require different parameter constraints across the lifespan.

## References

1. (authors unknown). *Memory and Executive Function in Aging and AD: Multiple Factors that Cause Decline and Reserve Factors that Compensate*.
2. (authors unknown). *The Cognitive Neuroscience of Ageing and Functional Reserve*.
3. (authors unknown). *Effects of Aging on Functional Connectivity of the Default Mode Network*.

[[andrei-medvedev]]

## ORPHAN PAGE CONTEXT (andrei-medvedev)
---
created: 2026-04-20
sources:
- raw/papers/sporns-2011.md
- raw/papers/semanticscholar-a4f4c699c90f.md
- raw/papers/arxiv-2603.24343.md
- raw/papers/semanticscholar-929b90566fc8.md
tags:
- people-researcher
title: Andrei Medvedev
type: entity
updated: '2026-04-27'
---

# Andrei Medvedev

Researcher in neuroscience. Mentioned in the context of Domain 5 sources.

## Related Concepts
- [[neurodevelopment]]
- [[aging]]

## Note
This page was created as part of Domain 5 ingestion. More specific co