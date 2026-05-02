---
title: Cytoscape
created: 2025-01-15
updated: 2026-05-02
type: entity
tags: [software-visualization, connectomics, graph-theory, network-dynamics, structural-connectivity, functional-connectivity]
sources:
- "Shannon P, Markiel A, Ozier O, Baliga NS, Wang JT, Bamage D, Ideker T. (2003). Cytoscape: a software environment for integrated models of biomolecular interaction. Genome Research 13(1): 2498-2504. https://doi.org/10.1101/gr.1239303"
- "Cline MS, Smoot M, Cerami E, Kuchinsky A, Landys N, Workman C, et al. (2007). Integration of biological networks and gene expression data using Cytoscape. Nature Protocols 2(10): 2366-2382. https://doi.org/10.1038/nprot.2007.324"
- "Hagmann P, Cammoun L, Gigandet X, Meuli R, Honey CJ, Wedeen VJ, Sporns O. (2008). Mapping the structural core of human cerebral cortex. PLoS Biology 6(7): e159. https://doi.org/10.1371/journal.pbio.0060159"
- "Bullmore ET, Sporns O. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. Nature Reviews Neuroscience 10(3): 186-198. https://doi.org/10.1038/nrn2576"
- "Sanz-Leon P, Reck A, Schelter B, Jirsa VK. (2013). Targeting data assimilation to large-scale brain model. Proceedings of the 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society. https://doi.org/10.1109/EMBC.2013.6610767"
- "Jirsa VK, Proix T, Perdikis D, Woodman MM, Wang H, Gonzalez-Martinez J, et al. (2020). The Virtual Brain: a whole-brain modeling platform for modeling, dynamical systems and network-based simulations. Neuroinformatics 18(1): 1-22. https://doi.org/10.1007/s12021-020-09461-x"
- "Otasek D, Morris JH, Bouças J, Pico AR, Demchak B. (2019). Cytoscape Automation: empowering workflow-based network analysis. Genome Biology 20(1): 185. https://doi.org/10.1186/s13059-019-1758-4"
---

# Cytoscape

## Overview

Cytoscape is an open-source software platform designed for the visualization, analysis, and modeling of complex networks (graphs). Originally developed for bioinformatics applications—particularly the visualization of protein-protein interaction networks and other biological pathways—the software has evolved into a general-purpose network analysis tool widely used across multiple scientific domains [1][2]. In the context of computational neuroscience and whole-brain modeling, Cytoscape provides capabilities for visualizing structural and functional brain networks derived from neuroimaging data, performing graph-theoretic analysis on connectivity matrices, and integrating diverse data types within a unified network representation framework.

The software operates as a Java-based desktop application with a plugin architecture that allows extensibility through Apps—contributed modules that add specialized functionality. The core application provides standard network visualization primitives (nodes and edges with customizable visual properties), a variety of layout algorithms for positioning network elements, and built-in tools for basic network analysis. The App ecosystem extends these capabilities significantly, with hundreds of community-contributed plugins addressing domains ranging from network inference to semantic integration with external databases [7].

## Key Features

### Network Visualization and Editing

Cytoscape supports multiple network file formats, including standard graph exchange formats such as GraphML, SIF (Simple Interaction Format), and XGMML, as well as more specialized formats common in bioinformatics like BioPAX. Users can create networks manually through the graphical interface or import them from tabular data (e.g., edge lists in CSV format). The visualization engine provides fine-grained control over node and edge appearance, including size, color, shape, transparency, and labels, enabling the creation of publication-quality figures. Networks can be exported in vector formats (PDF, SVG) suitable for manuscript preparation.

### Layout Algorithms

A distinguishing feature of Cytoscape is its collection of network layout algorithms, which compute positions for nodes in two- or three-dimensional space based on various optimization criteria. The software includes force-directed layouts (which treat edges as springs and nodes as repelling particles, similar to algorithms used in [[graph-theory]]), hierarchical layouts, circular layouts, and grid-based arrangements. For brain network visualization, force-directed layouts are particularly useful because they naturally cluster densely connected regions and reveal the overall network topology. Users can also apply different layouts to selected subnetworks while preserving their relative positions.

### Network Analysis Tools

The core Cytoscape installation includes basic network statistics: node degree (the number of connections per node), betweenness centrality (a measure of how often a node lies on shortest paths between other nodes), clustering coefficient, and network density. These metrics are fundamental to [[brain-network]] analysis in computational neuroscience, where metrics like [[modularity]] and [[rich-club]] coefficients are used to characterize the topological organization of brain connectivity [4]. More advanced analysis capabilities are available through dedicated Apps, such as the ClusterViz App for community detection and the jActiveModules App for identifying network modules associated with particular phenotypes.

### App Ecosystem and Extensibility

Cytoscape's extensibility through its App system represents one of its greatest strengths. The App Manager provides access to hundreds of community-contributed plugins that extend functionality in specialized domains [7]. Relevant Apps for neuroscience applications include BiNGO (for Gene Ontology enrichment in networks), ReactomeFIViz (for pathway analysis), and clusterONE (for clustering weighted networks). This ecosystem allows researchers to adapt Cytoscape for domain-specific workflows without modifying the core application.

## Relationship to TVB

[[The Virtual Brain]] (TVB) is a whole-brain modeling platform that simulates large-scale brain dynamics using neural mass models integrated through empirical structural and functional connectivity data [5][6]. While TVB focuses on the forward problem—generating simulated dynamical activity from anatomical connectivity—Cytoscape complements it in the analysis and exploration phase of research workflows. The typical integration occurs when researchers export connectivity matrices from TVB or related preprocessing pipelines (such as those generated from [[diffusion-imaging]] tractography) and visualize these networks in Cytoscape to identify topological features that may relate to the simulated dynamics.

The structural connectivity matrices produced by tractography pipelines (often processed through tools like [[mrtrix3]] or [[dipy]]) can be imported into Cytoscape as weighted edge lists, with nodes representing brain regions from parcellation schemes such as the [[desikan-killiany-atlas]] or [[schaefer-atlas]]. Once represented as networks, researchers can apply graph-theoretic analysis to quantify properties such as small-worldness, hub structure, and modular organization, providing anatomical context for understanding the dynamics generated by TVB [4]. The combination of TVB simulation and Cytoscape analysis supports the interpretation of model behavior in terms of known anatomical constraints and enables comparison between simulated and empirical brain networks.

## Key Papers

The foundational reference for Cytoscape itself is Shannon et al. (2003), which introduced the software as an integrated environment for visualizing biomolecular interaction networks [1]. This was subsequently expanded in a methodological review covering the App ecosystem and integration capabilities [2].

Though Cytoscape was not originally developed for neuroscience applications, its use in the field has grown substantially as network-based approaches to brain connectivity have matured. Key methodological references include seminal works on brain network construction from diffusion MRI, particularly Hagmann et al. (2008), which established the field of connectomics and employed network visualization tools like Cytoscape to display white matter tracts and inter-regional connectivity [3]. The mathematical framework for analyzing such brain networks—including small-worldness, scale-free properties, and modular organization—was comprehensively reviewed by Bullmore and Sporns (2009) [4].

For researchers using TVB, the primary methodological references include Sanz-Leon et al. (2013), which described the mathematical formulation of large-scale brain dynamics integrated through empirical connectivity [5], and Jirsa et al. (2020), which provided the comprehensive framework for the TVB platform including workflow integration with external analysis tools [6].

## Related Software

Cytoscape occupies a niche in the network visualization landscape that overlaps with several other tools available to computational neuroscience researchers. [[Gephi]] is another open-source network visualization platform that offers real-time visualization and similar layout algorithms, with a focus on exploratory analysis of large networks. The [[brain-connectivity-toolbox]] (BCT) provides MATLAB implementations of graph-theoretic metrics that complement Cytoscape's visualizations with quantitative analysis capabilities [4]. [[BrainNet Viewer]] is a specialized tool for visualizing brain networks in three-dimensional space overlaid on anatomical templates, offering neuroscience-specific rendering that Cytoscape lacks. For whole-brain modeling workflows, [[the-virtual-brain]] provides integrated simulation and analysis capabilities that can interface with external visualization tools [5][6]. The choice between these tools typically depends on the specific visualization requirements, the need for integration with existing analysis pipelines, and researcher familiarity with the respective software environments.

## Technical Considerations

Importing brain connectivity data into Cytoscape requires converting parcellated region-by-region connectivity matrices into edge list format—a straightforward transformation that can be accomplished in Python (using libraries like NumPy or pandas) or MATLAB. Users should be aware that fully dense connectivity matrices (representing all pairwise region connections) can create visually cluttered networks in Cytoscape; thresholding the matrix to retain only strong connections or converting to binary adjacency matrices often produces more interpretable visualizations. The choice of threshold and whether to use weighted or binary representations significantly affects the resulting topology and should be justified based on the scientific question [4]. Additionally, Cytoscape's Java-based architecture can present challenges on some systems, particularly when working with very large networks (thousands of nodes) arising from high-resolution parcellations, where specialized implementations or downsampling may be necessary.