# TorchBraid: High-Performance Layer-Parallel Training of Deep Neural Networks with MPI and GPU Acceleration

**Source**: semantic-scholar
**ID**: 2d6ce9a9b36841ce3649fd393aa21fec82339c85
**DOI**: 10.1145/3759244
**URL**: https://www.semanticscholar.org/paper/2d6ce9a9b36841ce3649fd393aa21fec82339c85
**Date**: 2025-08-14
**Year**: 2025
**Authors**: Eric C. Cyr, Jens Hahne, Nicholas S. Moore, Jacob B. Schroder, Ben S. Southworth, David A. Vargas
**Venue**: ACM Transactions on Mathematical Software
**Citations**: 4

## Abstract

TorchBraid is a high-performance implementation of layer-parallel training for deep neural networks (DNNs) supporting MPI-based parallelism and GPU acceleration. Layer-parallel training has been developed to overcome the serialization inherent in forward and backward propagation of DNNs that limits utilization of computational resources in the strong scaling limit. To achieve this, TorchBraid integrates the PyTorch neural network framework with the state-of-the-art XBraid time-parallel library. This article presents the use and performance of TorchBraid, in addition to solutions for overcoming the algorithmic challenges inherent in combining automatic differentiation with layer-parallel. Results are presented with and without GPU acceleration for the Tiny ImageNet and MNIST image classification data sets, as well as recurrent neural networks. Overall, TorchBraid enables fast training of DNNs, both in a strong and weak scaling context. In addition to the TorchBraid software, several new advances in applying layer-parallel algorithms are detailed. Integration of layer-parallel with data-parallel algorithms is presented for the first time, showing the computational advantages of the combination. Standard deep learning techniques, like batch-normalization, are developed for layer-parallel training. Finally, a new approach combining layer-parallel with spatial coarsening in order to accelerate training for 3D image classification shows roughly a 10× speedup over serial execution.
