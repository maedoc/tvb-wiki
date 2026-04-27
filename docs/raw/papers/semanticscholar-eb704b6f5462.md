# Arbor-TVB: a novel multi-scale co-simulation framework with a case study on neural-level seizure generation and whole-brain propagation

**Source**: semantic-scholar
**ID**: eb704b6f54621c3867bc9f0a17e4cc89b7318389
**DOI**: 10.3389/fncom.2025.1731161
**URL**: https://www.semanticscholar.org/paper/eb704b6f54621c3867bc9f0a17e4cc89b7318389
**Date**: 2026-02-02
**Year**: 2026
**Authors**: Thorsten Hater, Juliette Courson, Han Lu, Sandra Díaz-Pier, Thanos Manos
**Venue**: Frontiers Comput. Neurosci.
**Citations**: 0

## Abstract

Computational neuroscience has traditionally focused on isolated scales, limiting understanding of brain function across multiple levels. While microscopic models capture biophysical details of neurons, macroscopic models describe large-scale network dynamics. Integrating these scales, however, remains a significant challenge. In this study, we present a novel co-simulation framework that bridges these levels by integrating the neural simulator Arbor with The Virtual Brain (TVB) platform. Arbor enables detailed simulations from single-compartment neurons to populations of such cells, while TVB models whole-brain dynamics based on anatomical features and the mean neural activity of a brain region. By linking these simulators for the first time, we provide an example of how to model and investigate the onset of seizures in specific areas and their propagation to the whole brain. This framework employs an MPI intercommunicator for real-time bidirectional interaction, translating between discrete spikes from Arbor and continuous TVB activity. Its fully modular design enables independent model selection for each scale, requiring minimal effort to translate activity across simulators. The novel Arbor-TVB co-simulator allows replacement of TVB nodes with biologically realistic neuron populations, offering insights into seizure propagation and potential intervention strategies. The integration of Arbor and TVB marks a significant advancement in multi-scale modeling, providing a comprehensive computational framework for studying neural disorders and optimizing treatments.
