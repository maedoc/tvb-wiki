# μGlia-Flow, An Automatic Workﬂow for Microglia Segmentation and Classification.

**Source**: semantic-scholar
**ID**: 7b1d7b7ab9131e67a1b390d094e0312ae49c431b
**DOI**: 10.1016/j.jneumeth.2025.110446
**URL**: https://www.semanticscholar.org/paper/7b1d7b7ab9131e67a1b390d094e0312ae49c431b
**Date**: 2025-04-01
**Year**: 2025
**Authors**: Huangrui Xiong, Siling Zheng, Xiuhong Qi, Ji Liu
**Venue**: Journal of Neuroscience Methods
**Citations**: 0

## Abstract

BACKGROUND
Microglia are important immune cells in the central nervous system, playing a key role in various pathological processes. The morphological diversity of microglia is closely linked to the development of brain diseases, yet accurate segmentation and automatic classification of microglia remain challenging.


NEW METHOD
We proposed a workflow, μGlia-Flow, which integrates both segmentation and classification for microglia analysis. The Frangi filtering algorithm was employed for branch segmentation, and an edge-guided attention TransUNet (EGA-Net) was used for soma segmentation. A Vision Transformer (ViT) network was applied to classify different morphologies.


RESULTS
The Frangi filtering algorithm produces more complete branches with smoother edges and clearer structures. The EGA-Net improves Dice and IoU scores by 4.02% and 6.75%, respectively. ViT achieves over 99% precision in classification. Post-processing reveals decreasing complexity during activation, validating the accuracy of μGlia-Flow.


COMPARISON WITH EXISTING METHODS
μGlia-Flow introduces deep learning, significantly improving segmentation accuracy and addressing the parameter dependency of existing classification methods.


CONCLUSION
we present an automatic workflow for segmenting and classifying microglia, providing a powerful tool for different morphology analysis.
