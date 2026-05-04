# SimHH: A Versatile, Multi-GPU Simulator for Extended Hodgkin-Huxley Networks

**Source**: semantic-scholar
**ID**: bceb6bea8311c2c92f536bbc46d95ff4946cc61c
**DOI**: 10.1109/ACCESS.2025.3550444
**URL**: https://www.semanticscholar.org/paper/bceb6bea8311c2c92f536bbc46d95ff4946cc61c
**Year**: 2025
**Authors**: Max C. W. Engelen, River Betting, Christos Strydis
**Venue**: IEEE Access
**Citations**: 0

## Abstract

Computational neuroscience relies on complex mathematical models to simulate brain activity and decipher underlying biological processes. However, these simulations are computationally intensive, prompting the exploration of high-performance computing systems as a viable solution to enhance efficiency. In this work, we introduce SimHH, an extended-Hodgkin-Huxley simulator designed for versatility and high performance. Leveraging the OpenMPI library, SimHH exhibits exceptional scalability, catering to a wide spectrum of computing environments. Scalability is optimized through two distinct configurations: one that distributes all possible cell-compartment potentials among network nodes and another that shares compartment potentials only among relevant nodes, employing MPI Allgather and Alltoall. Seamless support for CUDA, CUDA-aware MPI, and NVLink further enhances performance, with communication overhead minimized through concurrent execution of compute kernels. Benchmarking against various neuron models, including the challenging Inferior-Olivary Nucleus, demonstrates SimHH’s potential, achieving remarkable results on up to 256 compute nodes. Notably, large-scale GPU clusters enable the simulation of highly biologically plausible networks exceeding 10 million cells. Comparative analyses against CPU- and FPGA-based solutions underscore SimHH’s superiority, boasting a speedup of approximately <inline-formula> <tex-math notation="LaTeX">$150\times $ </tex-math></inline-formula> over single-threaded CPU implementations, <inline-formula> <tex-math notation="LaTeX">$10\times $ </tex-math></inline-formula> over single-FPGA setups, and <inline-formula> <tex-math notation="LaTeX">$10\times $ </tex-math></inline-formula> over multi-threaded CPU configurations with 128 threads, all for a fully connected network of approximately 7,000 IO cells. Additionally, a <inline-formula> <tex-math notation="LaTeX">$7\times $ </tex-math></inline-formula> speedup is attained compared to the established NEST neurosimulator running on 32 nodes, simulating a network of 94,720 Hodgkin-Huxley neurons with gap junctions. These findings underscore SimHH’s efficacy in advancing computational-neuroscience research by facilitating efficient and scalable simulation of complex neuronal networks.
