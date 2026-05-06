---
created: 2026-04-20
sources:
- raw/papers/basser-1994.md
- raw/papers/mori-1999.md
- raw/papers/jones-2010.md
- raw/papers/arxiv-2603.21067.md
- raw/papers/arxiv-2506.06234.md
- raw/papers/smith-2013-connectomics.md
- raw/papers/honey-2009.md
- raw/papers/arxiv-2603.07524.md
tags:
- structural-connectivity
- connectomics
- neuroimaging-dti
- diffusion-imaging
- tractography
- network-dynamics
- whole-brain-modeling
title: Structural Connectivity
type: concept
updated: '2026-05-06'
---

**Structural [[connectivity]]** (SC) refers to the anatomical connections between brain regions, typically represented as white matter fiber tracts that enable direct communication between neuronal populations. Unlike [[functional-connectivity]]—which captures statistical dependencies in activity patterns—structural connectivity reflects the physical "wiring diagram" of the brain, comprising axonal fiber bundles that provide the substrate for information transmission across distributed neural circuits. This distinction is fundamental: while functional connectivity can reveal coordinated activity between brain areas even in the absence of direct anatomical links, structural connectivity constrains the possible pathways through which neural signals can propagate.

## Motivation and Context

The characterization of structural connectivity emerged as a central goal in neuroscience with the recognition that brain function arises from the interaction of anatomically linked regions. The advent of [[diffusion-mri]] in the 1990s, particularly [[dti|Diffusion Tensor Imaging]] introduced by Basser, Mattiello, and LeBihan (1994), enabled researchers to non-invasively map white matter pathways in the living human brain for the first time [@basser-1994]. Prior to this, anatomical connectivity could only be studied post-mortem through histological methods or in animal models via invasive tracer injections. The ability to reconstruct fiber tracts in vivo using tractography algorithms—pioneered by Mori and colleagues (1999)—revolutionized [[connectomics]] by providing the structural foundation upon which dynamic brain models could be built [@mori-1999].

In the context of whole-brain modeling, structural connectivity serves as the primary anatomical constraint that determines how neural activity propagates across the [[brain-network]]. Without accurate SC data, computational models lack the essential substrate for reproducing realistic [[brain-dynamics]]. The field has consequently wrestled with fundamental questions about the validity and limitations of SC measurements derived from diffusion MRI, questions thoroughly examined in Derek Jones's influential review [@jones-2010].

## Measurement Methods

### In Vivo (Human)

The primary method for measuring structural connectivity in living humans is **diffusion tensor imaging** (DTI), which exploits the anisotropic diffusion of water molecules along myelinated fiber tracts. Water diffuses more freely parallel to axonal fibers than perpendicular to them, and this directional dependence of diffusion provides information about fiber orientation at each voxel. The diffusion tensor—a 3×3 symmetric matrix—characterizes this anisotropy and enables estimation of principal fiber directions.

**Tractography** algorithms use these directional estimates to reconstruct putative fiber pathways through space. Streamline tractography integrates the principal diffusion direction to trace continuous paths from seed regions to target regions, with the assumption that these paths correspond to actual axonal bundles. However, as Jones (2010) extensively documented, tractography faces significant challenges: crossing fibers (where multiple fiber populations occupy the same voxel) cannot be resolved with standard DTI, the method provides no direct information about connection strength or directionality, and track counts correlate only weakly with actual fiber counts [@jones-2010].

Advanced diffusion models, including **diffusion spectrum imaging** (DSI) and **constrained spherical deconvolution** (CSD), partially address the crossing fiber problem by resolving multiple fiber orientations per voxel.

### Ex Vivo (Animal)

For animal studies, invasive tracers remain the gold standard for structural connectivity mapping. Anterograde tracers (e.g., biotinylated dextran amine) label axons from their cell bodies to terminals, while retrograde tracers (e.g., fluorogold) label neurons that project to an injection site. These methods provide directional information—distinguishing afferent from efferent connections—and quantitative estimates of connection strength based on label density. Histological methods, including myelin staining and axonal tracing, enable microscopic verification of connectivity, but these approaches are incompatible with human research.

## Connectome Construction Pipeline

The process of constructing a structural connectivity matrix from diffusion MRI data involves several stages, each introducing choices that affect the final connectivity estimate.

**Parcellation** defines the nodes of the network by dividing the brain into discrete regions. Common atlases include the [[desikan-killiany-atlas|Desikan-Killiany]] cortical parcellation (34 regions per hemisphere), the [[aal-atlas|Automated Anatomical Label]] (90 regions), and the more recent [[brainnetome-atlas|Brainnetome]] atlas (210 regions). The choice of parcellation fundamentally determines the granularity of connectivity estimates—finer parcellations reveal more detail but yield sparser individual connections.

**Tractography** generates candidate fiber pathways between parcellated regions. Tools like [[mrtrix3]], [[dipy]], and [[dsi-studio|DSI Studio]] implement various algorithms with different performance characteristics. Probabilistic tractography provides uncertainty estimates but at computational cost.

**Weighting** assigns values to each connection reflecting its anatomical strength. Common metrics include streamline count (the number of reconstructed fibers), [[fractional-anisotropy]] (FA) averaged along tracts, and quantitative anisotropy. Each weighting scheme captures different aspects of connectivity—streamline count reflects anatomical presence, while FA reports microstructural properties.

The final product is an N×N connectivity matrix where element (i,j) represents the structural connection from region i to region j. Due to the bidirectional nature of tractography reconstruction, such matrices are typically symmetric. However, this symmetry is a limitation—actual anatomical connections may be unidirectional, a fact onlycapturable through invasive tracer methods.

## Role in Whole-Brain Modeling

Structural connectivity provides the anatomical skeleton upon which whole-brain dynamics unfold. In [[whole-brain]] models such as those implemented in [[tvb|The Virtual Brain]], SC matrices determine:

1. **Coupling strength**: Connection weights establish the magnitude of interregional interactions, directly modulating the extent to which activity in one region influences its targets.
2. **Network topology**: The graph-theoretic properties of SC networks—including [[small-world-networks|small-world]] organization, [[rich-club|rich-club]] architecture, and [[modularity]]—shape emergent dynamics. Hub regions with high degree exert disproportionate influence on network behavior.
3. **Signal transmission delays**: Fiber length estimates derived from tractography enable calculation of conduction delays, which become critical for accurate simulation of temporal dynamics, particularly for EEG/MEG forward modeling.
4. **Individual variability**: Subject-specific SC matrices enable [[personalized-brain-modeling|personalized brain models]], allowing researchers to investigate how anatomical differences contribute to individual differences in brain function and clinical phenotypes.

## Key Network Properties

Empirical characterization of structural connectomes has revealed several canonical topological properties. The human brain connectome exhibits **sparsity**—only approximately 20-30% of possible pairwise connections exist—reflecting efficient, specialized wiring. The network displays **small-world** organization, combining high clustering among nearby regions with short path lengths enabling global integration. A **rich-club** phenomenon emerges wherein highly connected hub regions are densely interconnected among themselves, forming a backbone for global communication. Community structure or **[[modularity]]** reflects functional segregation, with distinct subnetworks supporting sensory, motor, and association functions.

These properties emerge from the interaction of developmental mechanisms and evolutionary optimization, and they constrain the dynamical possibilities accessible to brain networks.

## Limitations and Open Questions

Despite its centrality to connectomics, structural connectivity estimation faces persistent challenges. Tractography's inability to resolve directionality or precise connection strength limits its utility for certain modeling applications. Validation studies comparing tractography-derived connectivity with ground truth from tracer experiments reveal systematic biases, particularly for weak Connections [@jones-2010]. The field continues to grapple with fundamental questions about how best to weight connections, how to account for inter-subject variability, and how to integrate structural data with functional measurements.

## Related Concepts

- [[functional-connectivity]] – Statistical dependencies in neural activity
- [[effective-connectivity]] – Causal directional interactions
- [[connectome]] – Complete map of neural connections
- [[tractography]] – Fiber tracking algorithms
- [[dti]] – Diffusion tensor imaging
- [[diffusion-mri]] – Broader class of [[diffusion-imaging]] methods
- [[white-matter]] – Myelinated fiber tracts
- [[parcellation]] – Brain parcellation schemes
- [[modularity]] – Community structure in networks
- [[rich-club]] – Hub region connectivity
- [[personalized-brain-modeling]] – Individualized modeling approaches
- [[connectivity-types]] – Taxonomy of connectivity types
- [[whole-brain]] – Whole-brain modeling framework
- [[connectome-mapper-3]] – Connectivity pipeline software
- [[brain-connectivity-toolbox]] – Network analysis software
- [[mrtrix3-connectome|Mrtrix3 Connectome]]

## References

1. (authors unknown). *MR diffusion tensor spectroscopy and imaging*.
2. (authors unknown). *Three-dimensional tracking of axonal projections in the brain by magnetic resonance imaging*.
3. (authors unknown). *Challenges and limitations of quantifying brain connectivity in vivo with diffusion MRI*.
4. Sakul Mahat, Sharmistha Guha, Jessica Bernard. (2026). *A [[bayesian]] Framework for Quantifying Association Between Functional and Structural Data in [[neuroimaging]]*. [Link](](https://arxiv.org/abs/2603.21067))
5. Caitlin Lienkaemper, G. Ocker. (2025). *Diverse [[mean-field-theory|mean-field]] dynamics of clustered, inhibition-stabilized Hawkes networks via combinatorial threshold-[[linear]] networks*. [Link](](https://www.semanticscholar.org/paper/fbd6e0d74d7094beee2f373371f61ee03edaa40d))
6. (authors unknown). *Functional Connectomics from [[resting-state|Resting-State fMRI]]*.
7. (authors unknown). *Predicting Human Resting-State Functional Connectivity from Structural Connectivity*.
8. Hongjie Jiang, Yifei Tang, Shuqiang Wang. *Neural Dynamics-Informed Pre-trained Framework for Personalized Brain Functional Network Construction*. [Link](](https://arxiv.org/abs/2603.07524))