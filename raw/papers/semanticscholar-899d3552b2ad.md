# A brain-constrained neural model of cognition and language with NEST: transitioning from the Felix framework

**Source**: semantic-scholar
**ID**: 899d3552b2ad319ccdb9921d7632fe94e0826220
**DOI**: 10.1007/s11571-026-10415-5
**URL**: https://www.semanticscholar.org/paper/899d3552b2ad319ccdb9921d7632fe94e0826220
**Date**: 2026-02-06
**Year**: 2026
**Authors**: Maxime Carriere, Fynn R. Dobler, H. Plesser, Agata Feledyn, Rosario Tomasello, Thomas Wennekers, F. Pulvermüller
**Venue**: Cognitive Neurodynamics
**Citations**: 0

## Abstract

We introduce a brain-constrained neurocomputational model designed to simulate higher cognitive functions of the human brain, implemented using NEST, a widely used open-source simulator optimised for high-performance spiking neural network simulations. Previously implemented in the custom-built C-based Felix simulation library, transitioning the model to NEST enhances accessibility, reproducibility, and computational efficiency. At the cellular level, the model comprises spiking excitatory neurons and local inhibitory neurons, whereas at the network level, it replicates the structural and functional organisation of 12 cortical regions spanning frontal, temporal, and occipital cortices, along with their associated inter-area connectivity. Additionally, global inhibition mechanisms and neuronal noise are integrated. Learning in the model follows biologically plausible Hebbian plasticity principles, incorporating both long-term potentiation and long-term depression. To validate the NEST implementation, we replicated previous simulation findings obtained with the Felix-based model. The new implementation successfully reproduced the same topographical distribution of cell assemblies following associative learning of object and action words within action and perception systems, replicating a range of previous neuroimaging results. Although the NEST model produced larger cell assemblies than Felix, the overall topographical patterns remained similar, indicating preservation of fundamental network characteristics. Moreover, the transition to NEST significantly enhanced computational efficiency, reducing simulation runtime nearly sixfold compared to Felix. This improvement in computational speed is crucial for expanding the model to include additional cortical regions, such as extending to the right hemisphere, which necessitates increased computational resources.
