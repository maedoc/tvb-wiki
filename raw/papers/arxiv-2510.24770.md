# DMVFC: Deep Learning Based Functionally Consistent Tractography Fiber Clustering Using Multimodal Diffusion MRI and Functional MRI

**Source**: semantic-scholar
**ID**: 29b8e391102326a60138e78f58a8b2d2f0c64ed2
**DOI**: 10.1109/JSTSP.2025.3632542
**URL**: https://www.semanticscholar.org/paper/29b8e391102326a60138e78f58a8b2d2f0c64ed2
**Date**: 2025-10-24
**Year**: 2025
**Authors**: Bocheng Guo, Jin Wang, Yijie Li, Junyi Wang, Mingyu Gao, Puming Feng, Yuqian Chen, Jarrett Rushmore, N. Makris, Y. Rathi, Lauren J. O’Donnell, Fan Zhang
**Venue**: IEEE Journal on Selected Topics in Signal Processing
**Citations**: 2

## Abstract

Tractography fiber clustering using diffusion MRI (dMRI) is a crucial method for white matter (WM) parcellation to enable analysis of brain’s structural connectivity in health and disease. Current fiber clustering strategies primarily use the fiber geometric characteristics (i.e., the spatial trajectories) to group similar fibers into clusters, while neglecting the functional and microstructural information of the fiber tracts. There is increasing evidence that neural activity in the WM can be measured using functional MRI (fMRI), providing potentially valuable multimodal information for fiber clustering to enhance its functional coherence. Furthermore, microstructural features such as fractional anisotropy (FA) can be computed from dMRI as additional information to ensure the anatomical coherence of the clusters. In this paper, we develop a novel deep learning fiber clustering framework, namely Deep Multi-view Fiber Clustering (DMVFC), which uses joint multi-modal dMRI and fMRI data to enable functionally consistent WM parcellation. DMVFC can effectively integrate the geometric and microstructural characteristics of the WM fibers with the fMRI BOLD signals along the fiber tracts. DMVFC includes two major components: (1) a multi-view pretraining module to compute embedding features from each source of information separately, including fiber geometry, microstructure measures, and functional signals, and (2) a collaborative fine-tuning module to simultaneously refine the differences of embeddings. In the experiments, we compare DMVFC with two state-of-the-art fiber clustering methods and demonstrate superior performance in achieving functionally meaningful and consistent WM parcellation results.
