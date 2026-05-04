---
created: 2024-01-15
sources:
- raw/papers/sanz-leon-2013.md
- raw/papers/arxiv-2603.07524.md
- raw/papers/semanticscholar-92f4183665f3.md
tags:
- connectomics
- brain-network
- computational-neuroscience
title: Neuromorpho.Org
type: entity
updated: '2026-04-30'
---

# Neuromorpho.Org

## Overview

Neuromorpho.Org is a publicly accessible, curated archive of digital reconstructions of neuronal morphologies from a wide variety of species, brain regions, and cell types. The database represents one of the most comprehensive efforts to standardize and share morphological data for computational neuroscience research. Founded in 2006 by Giorgio A. Ascoli and colleagues at George Mason University, the platform has grown to contain tens of thousands of reconstructions contributed by laboratories worldwide [@ascoli2007neuromorpho]. Each entry in the database represents a digitally reconstructed neuron—including its soma, dendrites, and axon—represented as a three-dimensional tree structure with associated metadata describing the experimental conditions, brain region, species, and cell-type classification.

## Key Features

The database distinguishes itself through several important features that make it valuable for computational modeling. First, all morphological reconstructions in Neuromorpho.Org are stored in standardized file formats, primarily SWC and ASC, which are compatible with most major neuronal simulation platforms including [[neuron]], [[brian]], [[brian2]], [[netpyne]], and [[neuroconstruct]] [@state2020bmtk]. Each reconstruction includes detailed morphometric measurements such as total dendritic length, branch order statistics, soma size, and axon length, enabling researchers to select appropriate morphologies for their specific modeling needs.

Second, the database maintains rigorous curation standards. Every reconstruction undergoes quality control to ensure proper tree topology, correct identification of soma and dendritic compartments, and appropriate dendritic-axonal polarity. The curation process also standardizes nomenclature using the NeuroNames ontology, ensuring consistency across contributions from different laboratories [@nielsen2008noneuronsource]. This standardization is crucial because raw morphological data from different labs often uses varying conventions, making integration challenging without such curation.

Third, Neuromorpho.Org provides extensive metadata for each entry. Researchers can search and filter reconstructions by species (including mouse, rat, human, non-human primates, and various other vertebrates), brain region (cortex, hippocampus, cerebellum, basal ganglia, and subcortical structures), cell type (pyramidal cells, interneurons, granule cells, Purkinje cells, etc.), and experimental condition (developmental stage, disease state, or experimental manipulation). This rich metadata enables systematic studies of morphological variation across brain regions and species.

## Relationship to TVB

Neuromorpho.Org represents a valuable data resource for [[whole-brain-modeling]] efforts, particularly those seeking to incorporate realistic single-neuron morphology into brain network simulations. While [[the-virtual-brain]] (TVB) primarily employs [[neural-mass-models]] that represent the collective activity of neuronal populations, there are scenarios where detailed single-neuron properties become important—for example, when modeling [[epilepsy-modeling]] where focal cortical dynamics depend on the interaction between specific neuronal subtypes, or when studying the effects of [[brain-stimulation]] at the cellular level where morphology determines how electric fields interact with neuronal compartments.

The database can serve as a source of realistic morphological templates for building detailed [[spiking-neural-networks]] that feed into or interface with TVB simulations. This is particularly relevant for the [[personalized-brain-modeling]] paradigm, where patient-specific structural data from [[neuroimaging]] can be combined with morphological reconstructions from Neuromorpho.Org to create more biophysically accurate models. Additionally, the morphometric data in the database supports [[parameter-estimation]] efforts in neural modeling by providing realistic bounds on morphological parameters.

## Key Computational Considerations

When using Neuromorpho.Org data in computational models, several practical considerations arise. One must distinguish between *reconstructed* morphologies—which represent the static structure of a neuron at a point in time—and *optimized* morphologies, which may have been adjusted computationally to fit electrophysiological recordings. The database explicitly labels reconstructions that have been optimized against experimental data, allowing modelers to choose appropriately for their application. Furthermore, different brain regions exhibit vastly different morphological complexity; cortical pyramidal neurons typically have extensive apical and basal dendritic trees, while cerebellar granule cells have much simpler morphologies—a factor that must be considered when selecting reconstructions for network models.

Another important consideration is species scaling. Morphological measurements do not scale linearly across species; a mouse cortical pyramidal neuron cannot simply be scaled up to represent a human neuron. Neuromorpho.Org provides reconstructions from multiple species, enabling comparative studies and allowing modelers to select the most appropriate species for their research question.

## Related Software

Neuromorpho.Org integrates with numerous software tools in the computational neuroscience ecosystem. The [[neuron]] simulation environment has built-in import functions for SWC-format morphologies from Neuromorpho. Similarly, [[brian]] and [[brian2]] can directly import these reconstructions for use in detailed single-neuron models. The [[neuroconstruct]] platform provides a graphical interface for managing neuronal simulations with morphologies from the database. For visualization, tools like [[neuron]]'s built-in GUI, [[pycortex]], and [[brainnet-viewer]] can render reconstructed morphologies in three dimensions.

Beyond simulation software, Neuromorpho.Org data feeds into analysis tools that quantify neuronal structure. The [[bctpy]] can be extended to analyze topological features of dendritic trees, while specialized tools like [[lfpy]] use detailed morphology to compute local field potentials from network simulations. The database also connects to [[neuroml]] standards, as morphological structure can be encoded in NeuroML format for interoperability across platforms [@gleeson2019sonata].

## Data Contribution and Curation Process

The database operates as a collaborative resource, welcoming contributions from researchers worldwide. Laboratories wishing to contribute reconstructions submit their data in standard formats along with comprehensive metadata. Submitted reconstructions undergo peer review by the Neuromorpho.Org team, who verify the morphological integrity and ensure proper metadata annotation. This collaborative model has enabled the database to grow continuously since its founding, with contributions from hundreds of laboratories globally.

## Key Papers

- Ascoli, G. A., et al. (2007). Neuromorpho.org: A central repository for neuronal morphometry. *Neuroinformatics*, 5(2), 111–115. [@ascoli2007neuromorpho]
- Ascoli, G. A. (2015). Sharing neuron data: Carving cartography from their configuration space. *Network: Computation in Neural Systems*, 26(2-4), 73–96. [@ascoli2015neuromorpho]
- Cannon, R. C., et al. (1998). Towards reliable reconstruction of neuronal topology. *Journal of Neuroscience Methods*, 84(1-2), 49–54.
- Donohue, D. E., & Ascoli, G. A. (2011). The mutual inspirations of dendritic form and function. *Frontiers in Computational Neuroscience*, 5, 90.
- Teeter, C., et al. (2018). Generalized leaky integrate-and-fire neurons parameterized by architecture, biophysics, and adaptation. *Physical Review E*, 98(2), 021301.

## See Also

- [[whole-brain-modeling]]
- [[spiking-neural-networks]]
- [[computational-neuroscience]]
- [[neural-mass-models]]
- [[the-virtual-brain]]
- [[neuron]]
- [[brain-network]]
- [[connectomics]]