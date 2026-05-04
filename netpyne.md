---
title: NetPyNE
created: 2025-01-15
updated: 2026-05-04
type: entity
tags: [software-tools, software-neuron, spiking-neural-networks, network-dynamics, python, neural-mass-models]
sources:
  - https://doi.org/10.7554/eLife.44494
  - https://www.ebrains.eu/news-and-events/co-simulation-interface-marks-a-new-milestone-for-multiscale-modelling
  - https://pubmed.ncbi.nlm.nih.gov/31025934/
---

NetPyNE (Networks using Python and NEURON) is an open-source Python package designed to facilitate the construction, simulation, and analysis of multiscale neuronal network models. Developed primarily at SUNY Downstate Medical Center under the leadership of Salvador Dura-Bernal and William Lytton, NetPyNE provides a high-level interface for specifying network architecture, connectivity, and dynamics while leveraging the NEURON simulator's computational engine for efficient parallel simulation [[cite:https://doi.org/10.7554/eLife.44494]]. The tool bridges the gap between abstract network models (where connectivity is often specified statistically) and detailed biologically realistic models (where every synapse and receptor must be explicitly defined), enabling researchers to explore brain dynamics across multiple scales of organization.

## Motivation and Context

The landscape of computational neuroscience encompasses a vast hierarchy of modeling approaches, from simplified [[neural-mass-models]] that treat populations of neurons as single mathematical entities, to detailed [[spiking-neural-networks]] that simulate individual neurons with channel-level biophysics. Historically, researchers had to choose between simplicity (which sacrificed biological detail) or detail (which sacrificed tractability and computational efficiency). NetPyNE emerged to address this tension by providing a unified specification language that allows users to define networks at whatever level of detail their research question requires, while still producing simulations that run efficiently on parallel computing architectures.

The tool is particularly valuable for researchers interested in [[brain-dynamics]] at the mesoscale—understanding how interactions between populations of neurons give rise to oscillatory patterns, propagating waves, and emergent computational properties. Unlike [[the-virtual-brain]] (which operates at the macroscopic whole-brain scale using [[neural-mass-models]] of brain regions), NetPyNE focuses on the mesoscopic scale where cortical columns and microcircuits are the primary units of organization. This makes it complementary to TVB: while TVB models whole-brain dynamics using [[structural-connectivity]] derived from tractography, NetPyNE can model the detailed intracellular and interneuronal dynamics that underlie the region-level equations that TVB employs.

## Key Features

NetPyNE's specification format allows users to define network models through a declarative configuration dictionary rather than imperative code. This configuration includes definitions of cell types (with parameters for ion channel conductances, morphology, and synaptic properties), populations (groups of neurons with shared properties), connectivity rules (specified through probability functions, weight distributions, and delay matrices), and stimulation parameters. The specification is hierarchical: users can define templates for cell types and then instantiate multiple populations with different parameter values, creating complex layered architectures reminiscent of cortical microcircuits.

The software includes automatic conversion of high-level specifications into NEURON/hoc code, enabling simulation on both single processors and distributed computing clusters. Parameter sweeps and optimization routines are integrated natively, allowing users to systematically explore how changes in synaptic strength, connection probability, or intrinsic neuronal properties affect network dynamics. Visualization tools allow inspection of connectivity matrices, raster plots, firing rate heatmaps, and local field potential recordings directly from the simulation environment. NetPyNE also supports integration with [[brian]] and [[brian2]] through export capabilities, though its primary computational backend remains NEURON.

## Relationship to TVB

While [[the-virtual-brain]] operates at the macroscopic scale by coupling [[neural-mass-models]] representing brain regions via [[functional-connectivity]] or [[structural-connectivity]] matrices, NetPyNE provides the microscopic and mesoscopic detail that can inform those region-level models. Researchers have used NetPyNE to simulate detailed cortical microcircuits and then use model reduction techniques to derive the effective [[neural-mass-models]] parameters that TVB requires. Conversely, TVB's region-level connectivity estimates (derived from [[diffusion-imaging]] and tractography) can provide constraints for NetPyNE network models investigating specific cortical pathways.

The two tools are thus complementary rather than competing: TVB is optimized for whole-brain simulation where computational efficiency is paramount, while NetPyNE excels at detailed investigation of specific circuits where biophysical realism is the primary concern. A notable development is the co-simulation interface between NetPyNE/NEURON and TVB, developed by researchers at SUNY Downstate and integrated into the EBRAINS platform. This interface enables multiscale modeling that links molecular chemical signaling (via NEURON's Reaction-Diffusion framework) to whole-brain network dynamics, representing a significant advancement in multiscale brain modeling capability [[cite:https://www.ebrains.eu/news-and-events/co-simulation-interface-marks-a-new-milestone-for-multiscale-modelling]]. For researchers pursuing [[personalized-brain-modeling]] workflows, NetPyNE can serve as a tool for validating the reduced models that TVB uses, or for investigating phenomena (such as seizure propagation via specific white matter tracts) that require intermediate-scale resolution.

## Key Papers

The primary reference for NetPyNE is the original publication describing the tool's architecture and capabilities:

> Dura-Bernal S, Suter BA, Gleeson P, Cantarelli M, Quintana A, Rodriguez F, Kedziora DJ, Chadderdon GL, Kerr CC, Neymotin SA, McDougal RA, Hines M, Shepherd GMG, Lytton WW. (2019). "NetPyNE, a tool for data-driven multiscale modeling of brain circuits." *eLife* 8:e44494. [[cite:https://doi.org/10.7554/eLife.44494]]

This paper has been cited over 200 times and serves as the canonical reference for the tool. Subsequent work has demonstrated NetPyNE's application in studying cortical dynamics, epilepsy modeling (related to [[epilepsy-modeling]]), and neural coding. The tool has been employed to investigate how different inhibitory neuron classes contribute to oscillatory dynamics, how [[brain-stimulation]] affects network responses, and how small-world and scale-free network topologies (via [[graph-theory]]) emerge from plastic synaptic rules.

## Related Software

NetPyNE shares conceptual territory with other neural simulation platforms including [[neuron]], [[nest]], and [[brian2]], each offering different tradeoffs between ease of specification and biophysical detail. For users interested in [[whole-brain-simulators]], [[the-virtual-brain]] provides a complementary macroscopic approach, while [[tvb-multiscale]] offers capabilities for coupling different simulation scales. Other related tools include [[pynest]] (Python bindings for NEST), [[brian2genn]] (GPU-accelerated Brian2), and [[arbor]] (which focuses on performance scalability for detailed single-cell models).

## References

1. Dura-Bernal S, Suter BA, Gleeson P, Cantarelli M, Quintana A, Rodriguez F, Kedziora DJ, Chadderdon GL, Kerr CC, Neymotin SA, McDougal RA, Hines M, Shepherd GMG, Lytton WW. (2019). NetPyNE, a tool for data-driven multiscale modeling of brain circuits. *eLife* 8:e44494. https://doi.org/10.7554/eLife.44494

2. Co-simulation interface marks a new milestone for multiscale modelling. (2022). EBRAINS. https://www.ebrains.eu/news-and-events/co-simulation-interface-marks-a-new-milestone-for-multiscale-modelling