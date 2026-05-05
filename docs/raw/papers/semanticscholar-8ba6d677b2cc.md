# Online Test of a Neural Network Deep Convection Parameterization in ARP-GEM1

**Source**: semantic-scholar
**ID**: 8ba6d677b2cc66d12a2f824701099d5231b52884
**DOI**: 10.1175/aies-d-24-0100.1
**URL**: https://www.semanticscholar.org/paper/8ba6d677b2cc66d12a2f824701099d5231b52884
**Date**: 2025-05-22
**Year**: 2025
**Authors**: B. Balogh, D. Saint‐Martin, O. Geoffroy
**Venue**: Artificial Intelligence for the Earth Systems
**Citations**: 0

## Abstract


In this study, we integrate a neural network-based parameterization into the global atmospheric model ARP-GEM1 using the Python interface of the OASIS coupler. This setup enables the exchange of fields between the Fortran-based ARP-GEM1 model and a Python component implementing the neural network inference. The Python component was deployed on a separate partition from the general circulation model, using GPUs. As a proof-of-concept, we trained a neural network to emulate ARP-GEM1’s deep convection parameterization. Leveraging the flexible Fortran/Python interface, we successfully replaced ARP-GEM1’s deep convection scheme with the neural network emulator. To evaluate its online performance, we realized a 30-year ARP-GEM1 simulation using the neural network for deep convection. The evaluation of the averaged fields showed good agreement with the output of an ARP-GEM1 simulation using the physics-based deep convection scheme.
