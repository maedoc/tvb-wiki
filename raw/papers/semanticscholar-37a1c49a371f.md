# Dual Neural Network Framework with SPICE Integration for Fast and Accurate Transistor Modeling

**Source**: semantic-scholar
**ID**: 37a1c49a371f5655bbbff1f33450fef7f7bd7ce5
**DOI**: 10.1002/aisy.202401085
**URL**: https://www.semanticscholar.org/paper/37a1c49a371f5655bbbff1f33450fef7f7bd7ce5
**Date**: 2025-04-21
**Year**: 2025
**Authors**: Rodion Novkin, Hussam Amrouch
**Venue**: Advanced Intelligent Systems
**Citations**: 1

## Abstract

Neural network (NN)‐based compact transistor models have recently emerged as a promising solution to simplify device modeling. However, they are often deployed and evaluated standalone due to the lack of compatibility with existing simulation program with integrated circuit emphasis (SPICE) software. To investigate the benefits of the NN‐based compact models, the proposed framework is integrated into commercial SPICE tool, and NN models’ speed is compared with the existing in‐built and Verilog‐A industry standard implementations. Additionally, the speed‐up of NN‐based compact models provided by GPU acceleration is demonstrated for variability analysis, and design technology co‐optimization with genetic algorithm is explored. For the best trade‐off between NN simulation speed and accuracy, the proposed dual‐NN structure employs a parameter generator network, representing devices with different transistor geometry, to generate weights for a current/charge prediction network (CPN). In addition to drain voltage VD$V_{\text{D}}$ and gate voltage VG$V_{\text{G}}$ , CPN also incorporates environment temperature and achieves 0.797% ID$I_{\text{D}}$ error with higher than 0.995 R2$R^{2}$ scores for DC characteristics. Moreover, it maintains the speed within SPICE, outperforming Verilog‐A Berkeley short‐channel insulated gate field‐effect transistor model (BSIM), and can simulate up to 18.8 million DC points per second with GPU acceleration.
