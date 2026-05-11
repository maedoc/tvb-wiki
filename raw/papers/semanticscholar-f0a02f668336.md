# Spatio-Temporal Enhancement-Based Spiking Neural Network for Morphological Neuron Classification

**Source**: semantic-scholar
**ID**: f0a02f668336a5577fe6d12b494a608713d1c973
**DOI**: 10.1109/TETCI.2025.3549763
**URL**: https://www.semanticscholar.org/paper/f0a02f668336a5577fe6d12b494a608713d1c973
**Date**: 2025-12-01
**Year**: 2025
**Authors**: Chunli Sun, Qinghai Guo, Luziwei Leng, Feng Wu, Fengjun Zhao
**Venue**: IEEE Transactions on Emerging Topics in Computational Intelligence
**Citations**: 2

## Abstract

The morphology of neurons plays a crucial role in identifying their types and investigating the structure and function of the brain. While existing methods recognize neuron types through efficient morphology representations based on their tree-like structure, they can be further enhanced when analyzing neurons with complex and varied morphologies. In this paper, we introduce a shallow yet efficient multi-branch spatio-temporal enhancement-based Spiking Neural Network (SNN), consisting of three spiking VGG5 models, to fully delineate neuronal morphologies and precisely identify neuron types. Our method captures neuronal morphologies from the spatio-temporal domain and explores the relationships among different neuronal branches, thereby providing a comprehensive description of neurons with complex structures and significantly improving the classification performance. Specifically, we first decompose the neuron tree with complex and varied morphologies into multiple subtrees to represent neuronal morphology fully and then explicitly project these subtrees onto the temporal dimension. Then, we introduce the spiking VGG5 model to characterize neuronal morphology through spiking sequences and learn the relation of these subtrees from the spatio-temporal dimensions. Furthermore, we design a plug-and-play Spatio-Temporal Enhancement Module (STEM) for the spiking VGG5, enabling maximal activation of the spiking activity and facilitating information transfer and representation learning. In this way, our SNN architecture can comprehensively learn neuronal morphology representations based on the tree-like structure and depict the relationships of subtrees, accurately describing the morphological features of neurons with complex arbors. Experimental results demonstrate that our method precisely depicts the neuronal morphologies and achieves accuracies of 87.40% and 82.96% on two NeuroMorpho datasets, respectively, outperforming other approaches. Besides, our method displays significant generalizability and performs remarkably on the JML and BIL datasets.
