---
title: Aging Brain
created: 2026-04-20
updated: 2026-05-08
type: concept
tags: [aging-brain, neuroimaging-fmri, functional-connectivity, cognitive-reserve, brain-maintenance, brain-reserve, successful-aging, alzheimers-disease, personalized-brain-modeling, whole-brain-modeling]
sources: [raw/papers/grady-2012.md, raw/papers/semanticscholar-b63e3d8a1467.md, raw/papers/smith-2021.md]
---

The aging brain refers to the structural and functional changes that occur in the human brain across the adult lifespan, encompassing alterations in neural connectivity, metabolism, and cognitive capacity. These changes reflect the intersection of normative biological aging processes with pathological processes that may lead to neurodegenerative conditions such as Alzheimer's disease. Understanding the aging brain is fundamental to whole-brain modeling because computational models must incorporate age-related changes in structural connectivity, neural dynamics, and neurovascular coupling to accurately simulate brain function across the lifespan.

## Neuroimaging Evidence of Age-Related Changes

Functional neuroimaging studies have revealed profound reorganization of brain networks during normal aging. Resting-state functional magnetic resonance imaging (fMRI) studies demonstrate that healthy older adults often exhibit increased functional connectivity between large-scale networks, including the default mode network, central executive network, and attention networks, compared to younger adults [[1]]. This increased connectivity is thought to reflect **neural compensation**, whereby the aging brain recruits additional neural resources to maintain cognitive performance in the face of structural and metabolic declines. Grady's comprehensive review synthesizing functional neuroimaging evidence synthesized evidence for the concept of **functional reserve**, proposing that individual differences in the capacity for compensatory network recruitment explain variability in cognitive outcomes during aging [[1]].

Structural MRI studies using large population cohorts such as the [[uk-biobank]] have identified distinct patterns of brain aging across individuals. Smith and colleagues analyzed structural brain changes across the lifespan in UK Biobank participants, identifying multiple "brain aging modes" that characterize different trajectories of gray matter volume loss and white matter degradation [[3]]. These population-level analyses revealed substantial heterogeneity in brain aging, with some individuals showing accelerated structural decline while others maintain relatively youthful brain structure into late adulthood. This variability has important implications for computational modeling, as whole-brain models must account for inter-individual differences in structural connectivity that emerge from differential aging trajectories.

## Functional Connectivity Changes Across the Dementia Spectrum

A critical frontier in aging brain research concerns the distinction between normative cognitive aging and pathological progression to mild cognitive impairment (MCI) and Alzheimer's disease. King and colleagues recently investigated whole-brain [[functional-connectivity]] measures in relation to cognitive performance across a spectrum of cognitively intact older adults, individuals with amnestic MCI, and patients with mild dementia due to probable Alzheimer's disease [[2]]. Their study of 108 older adults (mean age 74.1 years) revealed that lower scores on the Repeatable Battery for the Assessment of Neuropsychological Status (RBANS) were significantly associated with increased connectivity between the ventral attention network, central executive network, limbic system, and [[default-mode-network]] [[2]]. Notably, this pattern of increased inter-network connectivity became progressively more pronounced across the continuum from cognitively intact individuals to MCI to Alzheimer's disease, suggesting that the compensatory connectivity increases observed in normal aging may become dysregulated in pathological contexts.

These findings have significant implications for computational neuroscience. The phenomenon of aberrant increased functional connectivity in cognitive decline may represent a breakdown of efficient network organization, where the brain attempts to compensate through excessive integration that ultimately proves maladaptive. Whole-brain models that incorporate parameter estimation frameworks may help distinguish between adaptive compensation and pathological hyperconnectivity, potentially providing biomarkers for early detection of neurodegenerative processes.

## Computational Modeling of the Aging Brain

Whole-brain modeling approaches increasingly incorporate age-related changes in neural parameters to simulate brain dynamics across the lifespan. The Wong-Wang model and similar neural mass models can be parameterized to capture age-related changes in excitation-inhibition balance, which computational studies associate with altered gamma-aminobutyric acid (GABA)ergic signaling and glutamate dynamics in the aging brain. The Wong-Wang model describes the mean activity of coupled excitatory and inhibitory neural populations through the following equations:

$$\frac{dE}{dt} = -E + \tanh\left(\frac{c_1 E - c_2 I + P}{\sqrt{1 + c_3 E^2}}\right)$$

$$\frac{dI}{dt} -I + \tanh\left(\frac{c_4 E + P}{\sqrt{1 + c_5 E^2}}\right)$$

where $E$ and $I$ represent the excitatory and inhibitory population activities respectively, $P$ is the external input, and $c_1$ through $c_5$ are coupling parameters that can be tuned to capture age-related changes in excitation-inhibition balance. Parameter estimation techniques applied to empirical neuroimaging data enable construction of personalized brain models that account for individual differences in structural connectivity derived from diffusion tensor imaging (DTI) [[3]].

The concept of brain reserve—individual differences in the structural and functional capacity of the brain to cope with age-related pathology—provides a theoretical framework for understanding variability in aging outcomes that computational models aim to capture [[1]]. Successful aging, characterized by maintenance of cognitive function into late adulthood despite evidence of brain pathology, represents a key target for computational investigation. Models incorporating brain maintenance mechanisms may help identify factors that promote resilient brain aging, potentially informing interventions for age-related neurological conditions.

## Relationships to Related Concepts

The aging brain connects to multiple foundational concepts in computational neuroscience. Structural connectivity derived from diffusion imaging provides the anatomical substrate for whole-brain simulations, and age-related changes in white matter integrity directly affect signal propagation in computational models. [[Functional-connectivity]] analyses inform the coupling parameters between brain regions in neural mass models, and age-related changes in network dynamics require corresponding adjustments to model parameters. The [[default-mode-network]], which shows altered activation patterns in aging, plays a central role in whole-brain models of spontaneous brain activity.

The relationship to Alzheimer's disease modeling is particularly important, as computational models increasingly address the transition from normal aging to pathological cognitive decline. Personalized brain modeling approaches that incorporate individual structural connectivity and neurovascular parameters may help predict individual trajectories of brain aging and identify targets for therapeutic intervention. Whole-brain simulators such as The Virtual Brain provide frameworks for integrating multimodal neuroimaging data to model age-related changes in brain dynamics.

## References

1. Grady, C. L. (2012). The cognitive neuroscience of ageing and functional reserve. *European Journal of Neuroscience*, 35(5), 761-767. https://doi.org/10.1111/j.1460-9568.2012.08099.x

2. King, J., Prigge, M., Koppelmans, V., Hoffman, J. M., & Duff, K. (2026). Altered functional connectivity is associated with Repeatable Battery for the Assessment of Neuropsychological Status across the dementia spectrum. *Journal of the International Neuropsychological Society*. https://doi.org/10.1017/s135561772610191x

3. Smith, S. M., Elliott, L. T., et al. (2021). UK Biobank Brain Imaging: Structural MRI in a Massive Population Resource. *bioRxiv*. https://doi.org/10.1101/2021.05.28.446063