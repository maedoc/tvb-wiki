# Arbor-TVB: A Novel Multi-Scale Co-Simulation Framework with a Case Study on Neural-Level Seizure Generation and Whole-Brain Propagation

**arXiv ID**: 2505.16861
**Published**: 2025-05-22
**Updated**: 2025-12-16
**Authors**: Thorsten Hater, Juliette Courson, Han Lu, Sandra Diaz-Pier, Thanos Manos
**Categories**: q-bio.NC
**URL**: https://arxiv.org/abs/2505.16861
**PDF**: https://arxiv.org/pdf/2505.16861
**Source**: arXiv

## Abstract

Computational neuroscience has traditionally focused on isolated scales, limiting understanding of brain function across multiple levels. While microscopic models capture biophysical details of neurons, macroscopic models describe large-scale network dynamics. Integrating these scales, however, remains a significant challenge. In this study, we present a novel co-simulation framework that bridges these levels by integrating the neural simulator Arbor with The Virtual Brain (TVB) platform. Arbor enables detailed simulations from single-compartment neurons to populations of such cells, while TVB models whole-brain dynamics based on anatomical features and the mean neural activity of a brain region. By linking these simulators for the first time, we provide an example of how to model and investigate the onset of seizures in specific areas and their propagation to the whole brain. This framework employs an MPI intercommunicator for real-time bidirectional interaction, translating between discrete spikes from Arbor and continuous TVB activity. Its fully modular design enables independent model selection for each scale, requiring minimal effort to translate activity across simulators. The novel Arbor-TVB co-simulator allows replacement of TVB nodes with biologically realistic neuron populations, offering insights into seizure propagation and potential intervention strategies. The integration of Arbor and TVB marks a significant advancement in multi-scale modeling, providing a comprehensive computational framework for studying neural disorders and optimizing treatments.
