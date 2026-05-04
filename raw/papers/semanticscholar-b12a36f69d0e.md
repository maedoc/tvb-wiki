# VSG-Based Adaptive Optimal Frequency Regulation for AC Microgrids With Nonlinear Dynamics

**Source**: semantic-scholar
**ID**: b12a36f69d0eb8d25030dd5e1e31746dadc02e6b
**DOI**: 10.1109/TASE.2024.3366700
**URL**: https://www.semanticscholar.org/paper/b12a36f69d0eb8d25030dd5e1e31746dadc02e6b
**Year**: 2025
**Authors**: Chong Liu, Zhousheng Chu, Zhongxing Duan, Yi Zhang
**Venue**: IEEE Transactions on Automation Science and Engineering
**Citations**: 23

## Abstract

In this paper, an optimal frequency control approach is proposed for VSG-based AC Microgrids (MGs) to improve the frequency regulation performance by considering the nonlinear dynamics. First, a nonlinear dynamics system of the MG are analytically modelled by using the VSG controller. Following, the optimal controller is designed based on the Hamilton-Jacobi-Bellman (HJB) equation and is obtained by using the adaptive dynamic programming (ADP) method without linearizing. Then, a single neural networks (NNs) construction is used to approximate the optimal controller and cost function, simultaneously. Unlike the conventional VSG approach with constant inertia, the novel method can determine the optimal inertia in an online and adaptive way, as well as preserve a balance between the frequency regulation performance and the control cost. Finally, simulation results based on MATLAB/Simulink verify that the proposed control method improves the frequency nadir and the rate of change of the frequency (RoCoF) while DC-side energy is also drastically preserved by comparing the existing three studies. Note to Practitioners—a) Previous methods always assume that the generator can instantly generate and absorb infinite power, however, capacitance is finite in practice. This paper proposes an adaptive VSG-based method to provide a bounded threshold of inertia, which facilitates practical applications. b) The AC MG system is modeled as a nonlinear system to cope with the strong disturbance, which is more suitable for practical system. c) The controller is approximated by NN, which is designed by three physical variables, i.e., angular deviation, frequency deviation and rate of change of the frequency (RoCoF), which can be measured from the practical system. d) Small signal state space model is used to analyze the stability of the controller, which further proves the stability of the proposed method and enhances its application prospect in engineering practice.
