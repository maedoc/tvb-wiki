# DeepNuParc: A novel deep clustering framework for fine-scale parcellation of brain nuclei using diffusion MRI tractography

**Source**: semantic-scholar
**ID**: 5f40ed471691c93ae43fd15b842a89a9a056e8aa
**DOI**: 10.1016/j.neuroimage.2025.121421
**URL**: https://www.semanticscholar.org/paper/5f40ed471691c93ae43fd15b842a89a9a056e8aa
**Date**: 2025-03-10
**Year**: 2025
**Authors**: Haolin He, Ce Zhu, Le Zhang, Yipeng Liu, Xiao Xu, Yuqian Chen, L. Zekelman, Jarrett Rushmore, Y. Rathi, N. Makris, L. O’Donnell, Fan Zhang
**Venue**: NeuroImage
**Citations**: 1

## Abstract

Brain nuclei are clusters of anatomically distinct neurons that serve as important hubs for processing and relaying information in various neural circuits. Fine-scale parcellation of the brain nuclei is vital for a comprehensive understanding of their anatomico-functional correlations. Diffusion MRI tractography is an advanced imaging technique that can estimate the brain's white matter structural connectivity to potentially reveal the topography of the nuclei of interest for studying their subdivisions. In this work, we present a deep clustering pipeline, namely DeepNuParc, to perform automated, fine-scale parcellation of brain nuclei using diffusion MRI tractography. First, we incorporate a newly proposed deep learning approach to enable accurate segmentation of the nuclei of interest directly on the dMRI data. Next, we design a novel streamline clustering-based structural connectivity feature for a robust representation of voxels within the nuclei. Finally, we improve the popular joint dimensionality reduction and k-means clustering approach to enable nuclei parcellation at a finer scale. We demonstrate DeepNuParc on two important brain structures, i.e. the amygdala and the thalamus, that are known to have multiple anatomically and functionally distinct nucleus subdivisions. Experimental results show that DeepNuParc enables consistent parcellation of the nuclei into multiple parcels across multiple subjects and achieves good correspondence with the widely used coarse-scale atlases. Our code is available at https://github.com/HarlandZZC/deep_nuclei_parcellation.
