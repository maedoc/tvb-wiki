# A graph-based Neural Network surrogate model for accelerating semi-analytical model of galaxy formation and evolution

**Source**: semantic-scholar
**ID**: 2e633255872505c257b204e470e2ffb49b4f6fde
**URL**: https://www.semanticscholar.org/paper/2e633255872505c257b204e470e2ffb49b4f6fde
**Date**: 2026-04-25
**Year**: 2026
**Authors**: Xuejie Li, Zhongxu Zhai, Xiaohu Yang, Andrew Benson, Yun Wang
**Citations**: 0

## Abstract

Understanding how galaxy populations emerge and evolve from the growth of dark matter structure is a central challenge in galaxy formation theory. Semi-analytic models (SAMs) provide an efficient framework to address this problem, but exploring large ensembles of merger trees across broad parameter spaces remains computationally demanding. We develop a conditional graph neural network surrogate model that combines merger tree information with SAM parameters to predict galaxy properties across cosmic time. Using merger trees of dark matter halos from the Uchuu simulation and the Galacticus SAM, the model predicts stellar mass, luminosity, angular momentum, gas metal mass, and specific star formation rate across the wide redshift range of 0<= z<= 5. For instance, the model can predict stellar mass at 0<= z<= 3 with a scatter of 0.19-0.28 dex and coefficient of determination R^2 of 0.946-0.973 (R^2 close to 1 indicates prediction closely matching the truth). The results show that a single graph based model can reproduce these galaxy properties with good accuracy over multiple SAM realizations, merger trees and redshifts. This catalog-level model provides a practical route for accelerating SAM based studies of galaxy formation to enable a more detailed investigation of the model parameter space. The inference code, trained models, and example data products are publicly available at https://github.com/MutongCat/sam2galaxy-gnn.
