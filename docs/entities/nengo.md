---
title: Nengo
created: 2026-04-24
updated: 2026-04-27
type: entity
tags: [software-brain-modeling]
sources: 
  - https://nengo.ai/
  - https://ncbi.nlm.nih.gov/pmc/articles/PMC3880998/
  - https://compneuro.uwaterloo.ca/files/publications/eliasmith.2012.pdf
---

# Nengo

## Overview

Nengo is a Python-based neural modeling and simulation platform developed by the [Centre for Theoretical Neuroscience](https://compneuro.uwaterloo.ca/) at the University of Waterloo, Canada. It is designed to build, test, and deploy large-scale neural network models based on the Neural Engineering Framework (NEF). Nengo enables researchers to create brain models that can perform cognitive tasks including perception, memory, reasoning, and motor control.

Nengo gained prominence for implementing Spaun (Semantic Pointer Architecture Unified Network), at the time the world's largest functional brain model with 2.5 million spiking neurons [[1]](https://compneuro.uwaterloo.ca/files/publications/eliasmith.2012.pdf).

## Key Features

### Neural Engineering Framework (NEF)

Nengo implements the Neural Engineering Framework, which provides three principles for building neural models [[2]](https://ncbi.nlm.nih.gov/pmc/articles/PMC3880998/):

- **Representation**: Populations of neurons collectively represent time-varying vectors through non-linear encoding and linear decoding
- **Transformation**: Connections between neural populations compute functions through the NEF's factorization method
- **Dynamics**: Recurrent connections implement dynamical systems where neural activity represents state variables

### Multiple Backend Support

Nengo supports simulation on various hardware platforms:

| Backend | Description | Use Case |
|---------|-------------|----------|
| Reference Simulator | CPU-based, Python default | General development |
| OpenCL | GPU acceleration | Large-scale models |
| NengoLoihi | Intel Loihi neuromorphic chip | Low-power neuromorphic computing |
| NengoFPGA | FPGA acceleration | Real-time applications |
| NengoSpiNNaker | SpiNNaker neuromorphic board | Massively parallel neuromorphic |

### Extensible Architecture

Nengo provides a clean Python API that separates model construction from simulation, allowing the same model to run on different backends with minimal changes. The platform supports:

- Custom neuron types
- Custom learning rules
- Integration with deep learning frameworks (TensorFlow, Keras via NengoDL)
- Interactive visualization with NengoGUI

## Notable Implementations

### Spaun

Spaun (Semantic Pointer Architecture Unified Network) was built using Nengo and demonstrated eight cognitive tasks including [[3]](https://www.nature.com/news/simulated-brain-scores-top-test-marks-1.11914):

- Image recognition
- Serial working memory
- Counting
- Question answering
- Fluid reasoning (Raven's Progressive Matrices)
- Reinforcement learning

Spaun contains 2.5 million spiking neurons organized into brain regions including the prefrontal cortex, basal ganglia, thalamus, and motor cortex. It receives visual input and produces motor output through a simulated physical arm.

### NengoLoihi

Nengo includes support for Intel's Loihi neuromorphic chip, which provides [[4]](https://arxiv.org/abs/2007.10227):

- On-chip learning capabilities
- Low-power operation (significantly less than CPU/GPU)
- Event-driven processing for efficient sensory processing

## Relationship to Other Projects

### Comparison with NEST and Brian

While NEST and Brian simulators focus on biological detail and flexibility, Nengo emphasizes large-scale functional models built according to NEF principles. Nengo's factored weight matrices enable efficient simulation of models considerably larger than Spaun on commodity hardware.

### NengoDL Integration

NengoDL extends Nengo's API to integrate with Keras and TensorFlow, enabling:

- Training deep neural networks and converting them to spiking networks
- Using TensorFlow's distributed computing for efficient simulation
- Deep learning approaches combined with neuromorphic hardware

## Key Papers

- Bekolay, T. et al. (2014). "Nengo: a python tool for building large-scale functional brain models." *Frontiers in Neuroinformatics* [[2]](https://ncbi.nlm.nih.gov/pmc/articles/PMC3880998/)
- Eliasmith, C. et al. (2012). "A large-scale model of the functioning brain." *Science* [[1]](https://compneuro.uwaterloo.ca/files/publications/eliasmith.2012.pdf)
- DeWolf, T., Jaworski, P. & Eliasmith, C. (2020). "Nengo and Low-Power AI Hardware for Robust, Embedded Neurorobotics." *Frontiers in Neurorobotics* [[4]](https://arxiv.org/abs/2007.10227)

## Hardware Backend Details

### Intel Loihi vs IBM TrueNorth

Nengo's primary neuromorphic backend is **Intel's Loihi** chip, not IBM TrueNorth. While Nengo can work with models trained for TrueNorth via NengoDL's deep learning integration [[4]](https://arxiv.org/abs/2007.10227), TrueNorth is not a natively supported backend. The NengoLoihi package provides dedicated support for compiling Nengo models to run on Loihi hardware.

### Real-Time Processing

Nengo's real-time performance depends on the backend and model size. While neuromorphic hardware like Loihi and TrueNorth can achieve low-latency processing for specific tasks, Nengo simulations on standard CPUs GPUs are generally **not real-time** - one second of neural simulation typically requires more than one second of compute time for large models.

## Related Software

* [[TVB]] - The Virtual Brain
* [[NEST]] - Neural Simulation Tool
* [[Brian]] - Neural simulator
* [[Spaun]] - Large-scale brain model

## References

[1] Eliasmith, C. et al. (2012). "A large-scale model of the functioning brain." Science, 338(6113), 1202-1205.

[2] Bekolay, T. et al. (2014). "Nengo: a python tool for building large-scale functional brain models." Frontiers in Neuroinformatics, 7:48.

[3] Yong, E. (2012). "Simulated brain scores top test marks." Nature.

[4] DeWolf, T., Jaworski, P. & Eliasmith, C. (2020). "Nengo and Low-Power AI Hardware for Robust, Embedded Neurorobotics." arXiv:2007.10227.