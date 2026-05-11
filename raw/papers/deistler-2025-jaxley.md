# Jaxley: differentiable simulation enables large-scale training of detailed biophysical models of neural dynamics

**DOI**: 10.1038/s41592-025-02895-w
**Published**: 2025
**Journal**: Nature Methods
**Authors**: Deistler, Michael and Kadhim, Kyra L and Pals, Matthijs and Beck, Jonas and Huang, Ziwei and Gloeckler, Manuel and Lappalainen, Janne K and Schröder, Cornelius and Berens, Philipp and Goncalves, Pedro J and Macke, Jakob H
**URL**: https://www.nature.com/articles/s41592-025-02895-w
**Preprint**: https://www.biorxiv.org/content/10.1101/2024.08.21.608979

## Abstract

We present Jaxley, a differentiable simulator for biophysical neuron models written in JAX. Jaxley enables gradient-based optimization of thousands of parameters in detailed neuron models, supports simulations on CPU, GPU, or TPU without code modifications, and achieves performance competitive with other simulators through just-in-time compilation. The framework supports multicompartment neurons and elegant parameter sharing mechanisms. We demonstrate Jaxley's capabilities by fitting detailed biophysical models to intracellular recordings, optimizing ion channel conductances across cell populations, and training networks with thousands of neurons and millions of synaptic connections.