# Neural ODE-Based Dynamic Modeling and Predictive Control for Power Regulation in Distribution Networks

**Source**: semantic-scholar
**ID**: 760e5091948eca3c54cc65f85c390dca76105436
**DOI**: 10.3390/en18133419
**URL**: https://www.semanticscholar.org/paper/760e5091948eca3c54cc65f85c390dca76105436
**Date**: 2025-06-29
**Year**: 2025
**Authors**: Libin Wen, Jinji Xi, Hong Hu, Li Xiong, Guangling Lu, Tannan Xiao
**Venue**: Energies
**Citations**: 3

## Abstract

The increasing penetration of distributed energy resources (DERs) and power electronic loads challenges the modeling and control of modern distribution networks (DNs). The traditional models often fail to capture the complex aggregate dynamics required for advanced control strategies. This paper proposes a novel framework for DN power regulation based on Neural Ordinary Differential Equations (NODEs) and Model Predictive Control (MPC). NODEs are employed to develop a data-driven, continuous-time dynamic model capturing the aggregate relationship between the voltage at the point of common coupling (PCC) and the network’s power consumption, using only PCC measurements. Building upon this NODE model, an MPC strategy is designed to regulate the DN’s active power by manipulating the PCC voltage. To ensure computational tractability for real-time applications, a local linearization technique is applied to the NODE dynamics within the MPC, transforming the optimization problem into a standard Quadratic Programming (QP) problem that can be solved efficiently. The framework’s efficacy is comprehensively validated through simulations. The NODE model demonstrates high accuracy in predicting the dynamic behavior in a DN against a detailed simulator, with maximum relative errors below 0.35% for active power. The linearized NODE-MPC controller shows effective tracking performance, constraint handling, and computational efficiency, with typical QP solve times below 0.1 s within a 0.1 s control interval. The validation includes offline tests using the NODE model and online co-simulation studies using CloudPSS and Python via Redis. Application scenarios, including Conservation Voltage Reduction (CVR) and supply–demand balancing, further illustrate the practical potential of the proposed approach for enhancing the operation and efficiency of modern distribution networks.
