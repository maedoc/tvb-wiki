# H -HIGNN: A scalable graph neural network framework with hierarchical matrix acceleration for simulation of large-scale particulate suspensions

**Source**: semantic-scholar
**ID**: 02cd5e562e5e63d995de24ec30a2054b65936145
**DOI**: 10.1016/j.jcp.2025.114429
**URL**: https://www.semanticscholar.org/paper/02cd5e562e5e63d995de24ec30a2054b65936145
**Date**: 2025-05-13
**Year**: 2025
**Authors**: Zhan Ma, Zisheng Ye, Ebrahim Safdarian, Wenxiao Pan
**Venue**: Journal of Computational Physics
**Citations**: 3

## Abstract

We present a fast and scalable framework, leveraging graph neural networks (GNNs) and hierarchical matrix ($\mathcal{H}$-matrix) techniques, for simulating large-scale particulate suspensions, which have broader impacts across science and engineering. The framework draws on the Hydrodynamic Interaction Graph Neural Network (HIGNN) that employs GNNs to model the mobility tensor governing particle motion under hydrodynamic interactions (HIs) and external forces. HIGNN offers several advantages: it effectively captures both short- and long-range HIs and their many-body nature; it realizes a substantial speedup over traditional methodologies, by requiring only a forward pass through its neural networks at each time step; it provides explainability beyond black-box neural network models, through direct correspondence between graph connectivity and physical interactions; and it demonstrates transferability across different systems, irrespective of particles'number, concentration, configuration, or external forces. While HIGNN provides significant speedup, the quadratic scaling of its overall prediction cost (with respect to the total number of particles), due to intrinsically slow-decaying two-body HIs, limits its scalability. To achieve superior efficiency across all scales, in the present work we integrate $\mathcal{H}$-matrix techniques into HIGNN, reducing the prediction cost scaling to quasi-linear. Through comprehensive evaluations, we validate $\mathcal{H}$-HIGNN's accuracy, and demonstrate its quasi-linear scalability and superior computational efficiency. It requires only minimal computing resources; for example, a single mid-range GPU is sufficient for a system containing 10 million particles. Finally, we demonstrate $\mathcal{H}$-HIGNN's ability to efficiently simulate practically relevant large-scale suspensions of both particles and flexible filaments.
