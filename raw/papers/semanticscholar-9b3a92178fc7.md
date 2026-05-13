# A Transformer-based Framework for Large-Scale EM Segmentation Stitching

**Source**: semantic-scholar
**ID**: 9b3a92178fc73db7196eb563d48ac3a965d6d5dc
**DOI**: 10.1142/s0219691326500116
**URL**: https://www.semanticscholar.org/paper/9b3a92178fc73db7196eb563d48ac3a965d6d5dc
**Date**: 2026-02-27
**Year**: 2026
**Authors**: Jingbin Yuan, Jiazheng Liu, Hongyu Liu, Jing Liu, Lijun Shen, Hua Han
**Venue**: International Journal of Wavelets, Multiresolution and Information Processing
**Citations**: 0

## Abstract

Accurate neuron stitching across large-scale electron microscopy volumes is crucial for reconstructing complete neural circuits. We propose TransStitch, a distributed Transformer-based framework that addresses these challenges by integrating multimodal feature fusion with topology-aware self- and cross-attention mechanisms to model global structural dependencies across adjacent electron microscopy blocks. To refine uncertain predictions, a dynamic 1-nearest-neighbor strategy progressively converts the probabilistic connectivity matrix into discrete associations without relying on a fixed threshold. Additionally, a mapping-based lazy relabeling strategy reduces merging complexity from voxel to fragment level, significantly improving computational efficiency and scalability. Extensive experiments on public electron microscopy datasets (SNEMI3D, CREMI-C, FIB25) with ground truth demonstrate superior stitching accuracy of proposed method compared to baseline, while qualitative evaluation on a large-scale, self-collected zebrafish whole-brain dataset confirms coherent 3D reconstruction across tens of thousands of sections. These results highlight TransStitch as an accurate and scalable solution for large-scale connectomics reconstruction.
