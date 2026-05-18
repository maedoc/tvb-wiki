# Exploiting network topology in brain-scale simulations of spiking neural networks

**Source**: semantic-scholar
**ID**: 5f2aeb20cc8f2137869cd38e2a96e7195524172e
**DOI**: 10.48550/arXiv.2602.23274
**URL**: https://www.semanticscholar.org/paper/5f2aeb20cc8f2137869cd38e2a96e7195524172e
**Date**: 2026-02-26
**Year**: 2026
**Authors**: Melissa Lober, Markus Diesmann, Susanne Kunkel
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Simulation code for conventional supercomputers serves as a reference for neuromorphic computing systems. The present bottleneck of distributed large-scale spiking neuronal network simulations is the communication between compute nodes. Communication speed seems limited by the interconnect between the nodes and the software library orchestrating the data transfer. Profiling reveals, however, that the variability of the time required by the compute nodes between communication calls is large. The bottleneck is in fact the waiting time for the slowest node. A statistical model explains total simulation time on the basis of the distribution of computation times between communication calls. A fundamental cure is to avoid communication calls because this requires fewer synchronizations and reduces the variability of computation times across compute nodes. The organization of the mammalian brain into areas lends itself to such an optimization strategy. Connections between neurons within an area have short delays, but the delays of the long-range connections across areas are an order of magnitude longer. This suggests a structure-aware mapping of areas to compute nodes allowing for a partition into more frequent communication between nodes simulating a particular area and less frequent global communication. We demonstrate a substantial performance gain on a real-world example. This work proposes a local-global hybrid communication architecture for large-scale neuronal network simulations as a first step in mapping the structure of the brain to the structure of a supercomputer. It challenges the long-standing belief that the bottleneck of simulation is synchronization inherent in the collective calls of standard communication libraries. We provide guidelines for the energy efficient simulation of neuronal networks on conventional computing systems and raise the bar for neuromorphic systems.
