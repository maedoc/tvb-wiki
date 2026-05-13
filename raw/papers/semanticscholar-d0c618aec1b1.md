# TrioSim: A Lightweight Simulator for Large-Scale DNN Workloads on Multi-GPU Systems

**Source**: semantic-scholar
**ID**: d0c618aec1b12b82434b63ab705617ca83c8f36d
**DOI**: 10.1145/3695053.3731082
**URL**: https://www.semanticscholar.org/paper/d0c618aec1b12b82434b63ab705617ca83c8f36d
**Date**: 2025-06-20
**Year**: 2025
**Authors**: Ying Li, Yuhui Bao, Gongyu Wang, Xinxin Mei, Pranav Vaid, Anandaroop Ghosh, Adwait Jog, Darius Bunandar, Ajay Joshi, Yifan Sun
**Venue**: International Symposium on Computer Architecture
**Citations**: 2

## Abstract

Deep Neural Networks (DNNs) have become increasingly capable of performing tasks ranging from image recognition to content generation. The training and inference of DNNs heavily rely on GPUs, as GPUs’ massively parallel architecture delivers extremely high computing capability. With the growing complexity of DNNs and the size of training datasets, training DNNs with a large number of GPUs is becoming a prevalent strategy. Researchers have been exploring how to design software and hardware systems for GPU farms to achieve the best utilization, efficiency, and DNN accuracy during training or inference. However, when designing and deploying such systems, designers usually rely on testing on physical hardware platforms equipped with many GPUs, incurring high costs that are almost prohibitive for system designers to test different configurations and designs, even for highly resourceful companies. While an alternative solution is to test on GPU simulators, they are often too slow for these large-scale systems and depend on profiling details collected from real distributed systems to initiate the simulation. To address these challenges, we present TrioSim, a novel lightweight simulator for DNNs on multi-GPU systems. TrioSim combines performance modeling techniques and simulation methods to achieve high flexibility, high simulation speed, and high accuracy. TrioSim minimizes the required input from users by only relying on operator-level execution traces collected on a single GPU and can simulate new software and hardware designs that involve multiple GPUs connected with complex, asymmetrical interconnects. Completing within seconds, TrioSim predicts the execution time of DNN training on multi-GPU systems with average errors of 2.91%, 4.54%, and 6.82% for data parallelism, tensor parallelism, and pipeline parallelism, respectively.
