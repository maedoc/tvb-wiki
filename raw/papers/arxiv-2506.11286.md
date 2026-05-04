# Mapping and Scheduling Spiking Neural Networks On Segmented Ladder Bus Architectures

**Source**: semantic-scholar
**ID**: f6eead434858fad34315ce59dbaa9d613d5df95d
**DOI**: 10.1016/j.sysarc.2025.103590
**URL**: https://www.semanticscholar.org/paper/f6eead434858fad34315ce59dbaa9d613d5df95d
**Date**: 2025-06-12
**Year**: 2025
**Authors**: P. Huynh, F. Catthoor, Anup Das
**Venue**: Journal of systems architecture
**Citations**: 1

## Abstract

Large-scale neuromorphic architectures consist of computing tiles that communicate spikes using a shared interconnect. The communication patterns in such systems are inherently sparse, asynchronous, and localized due to the spiking nature of neural events, characterized by temporal sparsity with occasional bursts of traffic. These characteristics necessitate interconnects optimized for handling high-activity bursts while consuming minimal power during idle periods. Dynamic segmented bus has been proposed a promising interconnect for its simplicity, scalability and low power consumption. However, deploying spiking neural network applications on such buses presents challenges, including substantial inter-cluster traffic, which can lead to network congestion, spike loss, and unnecessary energy expenditure. In this paper, we propose a three-step process to deploy SNN applications on dynamic segmented buses aiming to reduce spike loss and conserve energy. Firstly, we formulate optimization heuristics to mitigate spike loss and energy consumption based on application connectivity. Secondly, we analyze the application traffic to determine spike schedules that minimize traffic flooding. Lastly, we propose a routing algorithm to minimize spike traffic path crossings. We evaluate our approach using a cycle-accurate network simulator. The simulation results show that our algorithms can eliminate spike loss while keeping energy consumption significantly lower compared to conventional NoCs.
