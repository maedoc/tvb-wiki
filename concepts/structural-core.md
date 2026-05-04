---
created: 2026-04-20
sources:
- raw/papers/hagmann-2008.md
- raw/papers/sporns-2011.md
- raw/papers/deco-2013.md
- raw/papers/power-2011.md
- raw/papers/greicius-2003.md
- raw/papers/buckner-andrews-hanna-schacter-2008.md
tags:
- connectomics
- structural-connectivity
- network-dynamics
- network-hubs
- rich-club
title: Structural Core
type: concept
updated: '2026-05-04'
---

The structural core is a set of highly interconnected hub regions that form a central backbone for brain communication. Located predominantly in the posterior medial and parietal cortex, these regions exhibit the highest degree of anatomical [[connectivity]] in the brain and serve as major conduit points for information flow between disparate brain regions. The concept emerged from early [[connectomics]] work applying graph theoretical analysis to diffusion MRI data, revealing that [[brain-network]] organization is not homogeneous but contains a densely interconnected core of regions that anchor global communication.

## Discovery and Methodological Foundation

The structural core was first identified by Hagmann et al. (2008) using diffusion spectrum imaging (DSI), a variant of diffusion MRI that resolves multiple fiber orientations per voxel and provides superior angular resolution for tracking [[white-matter]] pathways. By constructing structural connectivity matrices from [[whole-brain]] [[tractography]] and applying graph analysis, the authors discovered that a subset of cortical regions showed dramatically higher inter-regional connectivity than expected by chance. These regions—primarily the precuneus, posterior cingulate cortex, superior parietal cortex, and isthmus cingulate—formed a heavily interconnected subgraph that the authors termed the "structural core."

The methodology combined deterministic tractography with graph theoretical measures including degree (the number of connections per node), betweenness centrality (the frequency with which a node lies on shortest paths between other nodes), and clustering coefficient (the tendency of neighbors to connect to each other). The structural core exhibited exceptionally high values on all three metrics, indicating that these regions are not merely highly connected individually but form a mutually interconnected "rich club" that serves as the brain's main communication infrastructure.

## Network Properties and Organization

The structural core displays several distinctive properties that set it apart from the rest of the cortical [[connectome]]. First, its members have among the highest degree values in the whole-brain network, meaning each core region connects to many more other regions than typical cortical areas. Second, core regions exhibit extremely high betweenness centrality, indicating that a disproportionate fraction of shortest paths between other brain regions pass through the core—this makes the core critical for global communication efficiency. Third, the core shows very high clustering coefficients among its members, meaning that core regions are highly interconnected with each other, forming a densely linked subgraph rather than a star-like structure.

These properties are the hallmarks of "rich-club" organization in network science, a principle first described in studies of social networks and later applied to biological systems. The rich-club phenomenon refers to the tendency of high-degree nodes (the "rich") to form dense interconnections among themselves (the "club"). In the brain, this organization suggests an evolutionary optimization where the most connected regions—which are metabolically expensive to maintain—are linked together to maximize the efficiency of whole-brain communication at minimal wiring cost.

## Relationship to Functional Networks

The structural core exhibits a correspondence with the [[default-mode-network]] (DMN), a set of brain regions that show high activity during resting-state conditions and are typically deactivated during task performance. This overlap includes the precuneus, posterior cingulate, and medial prefrontal cortex—regions that anchor both the structural core and the DMN. The correspondence between structural and functional network organization supports the hypothesis that [[functional-connectivity]] patterns at rest are substantially constrained by [[structural-connectivity]] pathways, though the relationship is not deterministic as functional connections canExist between regions lacking direct structural links through polysynaptic pathways.

This structural-functional alignment has important implications for understanding the neural basis of [[resting-state]] activity. The core's central position in the structural network enables it to serve as a hub for integrating information from multiple functional modules, potentially explaining why core regions are consistently recruited during internally directed cognition, memory retrieval, and self-referential processing—core functions of the DMN.

## Relationship to Other Network Concepts

The structural core is closely related to several other concepts in brain network science. It represents the anatomical manifestation of [[rich-club]] organization, where high-degree nodes form dense interconnections. The core regions function as [[network-hubs]]—the most connected nodes in the brain—and specifically as "connector hubs" that link different functional modules rather than "provincial hubs" that primarily connect within a single module. The core's existence also relates to the [[small-world-networks]] properties of brain connectivity, as the dense core combined with peripheral regions optimizes the balance between local clustering and global efficiency.

## Clinical and Functional Significance

The structural core has become a focus of clinical research due to its involvement in several neurological and psychiatric conditions. In Alzheimer's disease, core regions including the precuneus and posterior cingulate show early amyloid deposition, likely reflecting their high metabolic activity and synaptic density. Studies of disorders of consciousness have revealed that damage to core pathways correlates with impaired awareness and reduced integration of information across brain regions. Altered core connectivity has also been reported in schizophrenia, depression, and autism, suggesting that rich-club disruption may be a common pathway for diverse brain disorders.

From a [[brain-maintenance]] perspective, the structural core may be particularly vulnerable to age-related changes due to its high metabolic demands and central position in the network—the "hub" vulnerability hypothesis suggests that highly connected nodes are disproportionately affected by pathology due to their integrative role.

## Methodological Considerations

Identifying the structural core depends critically on the imaging modality and tractography algorithm used. Diffusion spectrum imaging provides superior angular resolution compared to diffusion tensor imaging, enabling detection of complex fiber crossings crucial for accurate structural connectivity estimation. However, the core has also been identified using other [[diffusion-imaging]] protocols, suggesting robust findings across methodologies. Ongoing developments in [[diffusion-mri]] acquisition and tractography continue to refine estimates of the structural core's extent and connectivity profile.