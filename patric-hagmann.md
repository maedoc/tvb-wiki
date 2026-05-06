---
title: Patric Hagmann
created: 2026-04-20
updated: 2026-05-06
type: concept
tags: [connectomics, structural-connectivity, diffusion-imaging, neuroimaging-dti, network-dynamics, software-connectome-mapper, people-researcher, whole-brain-modeling]
sources: [raw/papers/hagmann-2008.md]
---

Patric Hagmann is a Swiss neuroradiologist and professor whose seminal work on mapping the human connectome through diffusion MRI established foundational methods for whole-brain modeling. He is widely recognized for coining the term "connectomics" in his doctoral thesis and for developing the Diffusion Spectrum Imaging (DSI) methodology that enables non-invasive reconstruction of white matter fiber tracts as network representations. His research demonstrating that human brain structural networks exhibit small-world topology while lacking scale-free properties fundamentally shaped the field's understanding of brain architecture.

## Background and Institutional Affiliations

Patric Hagmann completed his medical training at the University of Lausanne (UNIL) in 2000 before undertaking postgraduate training in biomedical engineering at the École Polytechnique Fédérale de Lausanne (EPFL) in 2001. He earned his PhD in computer science and telecommunications from EPFL in 2005, where his dissertation "From diffusion MRI to brain connectomics" introduced the conceptual framework for mapping brain connectivity non-invasively using diffusion MRI. Following his PhD, Hagmann retained a dual affiliation as associate professor at EPFL and as a practicing physician in diagnostic neuroradiology at the Centre Hospitalier Universitaire Vaudois (CHUV) in Lausanne.

In 2008, Hagmann established the Connectomics Lab at UNIL and CHUV, where his group focuses on imaging brain structural connectivity and analyzing the relationship between anatomical wiring and functional communication. The lab has developed open-source software tools including the Connectome Mapper and the Multiscale Brain Parcellator, which are widely used in the neuroimaging community for constructing individual-level connectomes from diffusion MRI, functional MRI, and EEG data.

## Contributions to Diffusion MRI and Tractography

The core of Hagmann's methodological contribution lies in advancing Diffusion Spectrum Imaging (DSI), a diffusion MRI technique that images the three-dimensional diffusion function in every brain voxel. Unlike conventional Diffusion Tensor Imaging (DTI), which assumes Gaussian diffusion and cannot resolve crossing fibers, DSI captures non-Gaussian diffusion behavior and provides sufficient angular resolution to map complex white matter architectures where multiple fiber populations intersect within a single voxel.

In his 2005 PhD thesis and subsequent publications, Hagmann developed tractography algorithms specifically designed for high-angular-resolution diffusion data. These algorithms reconstruct three-dimensional curves—termed fibers—that represent estimated trajectories of axonal bundles through the white matter. The approach initiates fibers from every white matter voxel along directions corresponding to local maxima of the Orientation Density Function (ODF), which captures the predominant diffusion directions at each location. Fibers are grown iteratively with a step size of 1 mm, and the process terminates when fibers change direction sharper than 15 degrees per millimeter or exit the white matter.

A key innovation in Hagmann's methodology was the development of a two-phase partitioning heuristic for creating Regions of Interest (ROIs) at the white matter-gray matter interface. This approach produces compact, roughly equal-surface ROIs that become nodes in the connectivity graph, avoiding the pitfalls of coarse parcellations like Brodmann areas (limited to 50-55 regions) or regular lattice partitions that produce ROI sizes varying by orders of magnitude.

## Mapping Whole-Brain Structural Networks

The landmark 2007 publication "Mapping Human Whole-Brain Structural Networks with Diffusion MRI" in PLoS ONE demonstrated the first complete methodology for constructing individual human connectomes non-invasively. Applying this approach to two healthy volunteers, Hagmann and colleagues generated graphs with approximately 1,000 nodes representing small cortical areas and 45,000-50,000 edges representing white matter connections between them.

The analysis revealed several fundamental properties of human brain network organization. Most notably, the node degree distribution followed an exponential rather than heavy-tailed (scale-free) distribution, indicating that the brain does not contain the highly connected "hub" regions characteristic of scale-free networks like the World Wide Web. This finding was surprising given that many complex networks in nature and technology exhibit scale-free properties, and it suggested that brain network architecture is shaped by different constraints than those driving hub formation in other systems.

Despite lacking scale-free topology, the brain networks displayed classic small-world organization with high clustering coefficients (significantly exceeding random graph baselines) and short average path lengths comparable to random networks. This small-world property emerged at all tested resolutions ranging from 500 to 4,000 nodes, indicating robustness across scales. The combination of high local clustering and efficient global routing makes evolutionary and developmental sense: it provides economical information processing where locally dense computations need only occasional transmission to distant regions.

The edge weight analysis revealed a broad, heavy-tailed distribution, indicating that while most connections are relatively weak, a significant number of very strong connections exist—including long-range pathways such as the optic radiation and interhemispheric callosal projections. Notably, these strong connections predominantly involved short fiber tracts, consistent with the principle that the brain minimizes total wiring length while maintaining the capacity for distributed processing.

## Relationship to Structural Core and Rich-Club

Hagmann's subsequent work identified a "structural core" of highly connected regions in the posterior cingulate cortex, precuneus, and superior parietal lobule that serve as connector hubs linking both hemispheres and multiple functional networks. This structural core corresponds to regions exhibiting high metabolic activity at rest and forms the backbone of the human connectome.

The structural core overlaps significantly with the brain's rich-club phenomenon—the tendency for highly connected hub regions to be more densely interconnected among themselves than expected by chance. The rich-club infrastructure provides a central switching mechanism for distributed processing and may explain why hub regions show early developmental maturation and selective vulnerability in neurodegenerative conditions.

## Relationship to TVB and Whole-Brain Modeling

Patric Hagmann's connectomics methodology directly enables the workflows used in [[the-virtual-brain]] (TVB) for constructing personalized brain models. TVB requires individual structural connectivity matrices derived from diffusion MRI tractography to constrain large-scale neural simulations, and the Connectome Mapper pipeline developed in Hagmann's lab provides validated methods for generating such matrices.

The structural connectivity patterns mapped using DSI and related techniques serve as the anatomical scaffold upon which TVB simulates neural dynamics. The small-world architecture revealed by Hagmann's work provides theoretical justification for why TVB models can capture realistic brain dynamics with relatively sparse sampling of the connectome—the efficient path structure means that information can flow between any regions through only a few synaptic steps.

## Open Questions and Ongoing Research

Despite the foundational contributions, several questions remain regarding brain network organization. The relationship between structural connectivity and functional connectivity—whether and how anatomical wiring determines spontaneous and task-evoked neural activity—continues to be actively investigated. Recent work in Hagmann's lab focuses on spatio-temporal connectomics, extending the framework to model time-varying brain networks using both fMRI and source-reconstructed EEG.

Clinical applications investigating connectivity alterations in psychosis and neurodevelopment remain a major focus. The interplay between developmental processes and the emergence of small-world architecture, and how these are disrupted in psychiatric conditions, represents an open area of investigation.

## Related Concepts

- [[connectomics]] – The study of the complete set of neural connections in the brain
- [[diffusion-mri]] – MRI technique for mapping white matter microstructure
- [[tractography]] – Method for reconstructing fiber tracts from diffusion data
- [[structural-connectivity]] – Anatomical wiring between brain regions
- [[small-world-networks]] – Networks with high local clustering and short path lengths
- [[network-hubs]] – Highly connected nodes serving critical communication roles
- [[structural-core]] – Central backbone of highly connected regions
- [[rich-club]] – Dense interconnection among hub regions
- [[whole-brain-modeling]] – Large-scale computational models of brain dynamics
- [[connectome-mapper-3]] – Open-source software for connectome reconstruction