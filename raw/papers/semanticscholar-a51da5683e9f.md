# Physics-Informed Neural Networks for Predicting Combustion Dynamics in Rocket Engine Chambers

**Source**: semantic-scholar
**ID**: a51da5683e9fd333e061367243bf70ccd2a109f2
**DOI**: 10.55524/ijircst.2025.13.4.4
**URL**: https://www.semanticscholar.org/paper/a51da5683e9fd333e061367243bf70ccd2a109f2
**Date**: 2025-07-01
**Year**: 2025
**Authors**: Sheharyar Nasir, Shumail Sahibzada, Farrukh Sher Malik
**Venue**: International Journal of Innovative Research in Computer Science & Technology
**Citations**: 0

## Abstract

Accurately predicting combustion dynamics within rocket engine chambers is essential for ensuring propulsion system stability, efficiency, and safety. Traditional high-fidelity Computational Fluid Dynamics (CFD) methods offer detailed insights but are computationally expensive and often impractical for real-time applications. This study introduces Physics-Informed Neural Networks (PINNs) as a novel, efficient alternative for modeling combustion dynamics in rocket propulsion systems. PINNs integrate the governing partial differential equations (PDEs)—including mass, momentum, energy, and species transport—directly into the neural network's loss function, enabling data-efficient learning with limited reliance on extensive simulation datasets. We present a PINN framework trained on synthetic and benchmark CFD data from a hydrogen-oxygen combustor. The model captures complex physical phenomena such as temperature gradients, pressure oscillations, and flame front instabilities while significantly reducing computational cost. Our implementation employs a deep neural network architecture with eight hidden layers and 64 neurons per layer, using a combination of Adam and L-BFGS optimizers for training. The network achieves a validation root-mean-square error (RMSE) of 0.0029 MPa in pressure prediction, closely matching CFD results.Comparative analysis shows that the PINN model generalizes well to unseen temporal and spatial domains and offers predictions in under 0.5 seconds, in contrast to the 12-hour runtime of traditional CFD. These findings highlight PINNs as a promising surrogate modeling tool for real-time diagnostics, design optimization, and control in rocket propulsion systems. Future work will explore hybrid modeling, uncertainty quantification, and deployment in active combustion control frameworks.
