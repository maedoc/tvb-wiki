# Effective Connectivity-Based Unsupervised Channel Selection Method for EEG

**Source**: arxiv
**ID**: 2510.12910
**URL**: https://arxiv.org/abs/2510.12910
**Date**: 2025-10-14
**Year**: 2025
**Authors**: Neda Abdollahpour, N. Sertac Artan, Ian Daly, Mohammadreza Yazdchi, Zahra Baharlouei
**Categories**: eess.SP

## Abstract

Analyzing neural data such as Electroencephalography (EEG) data often involves dealing with high-dimensional datasets, where not all channels provide equally meaningful informa- tion. Selecting the most relevant channels is crucial for improving computational efficiency and ensuring robust insights into neural dynamics. This study introduces the Importance of Channels based on Effective Connectivity (ICEC) criterion for quantifying effective connectivity (EC) in each channel. Effective connectivity refers to the causal influence one neural region exerts over another, providing insights into the directional flow of information. Using this criterion, we propose an unsupervised channel selection method that accounts for the intensity of interactions among channels. To evaluate the proposed channel selection method, we applied it to three well-known EEG datasets across four categories. The assessment involved calculating the ICEC criterion using five effective connectivity metrics: partial directed coherence (PDC), generalized PDC (GPDC), renormalized PDC (RPDC), directed transfer function (DTF), and direct DTF (dDTF). To focus on the effect of channel selection, we employed the Common Spatial Pattern (CSP) algorithm for feature extraction and a Support Vector Machine (SVM) for classification across all participants. Results were compared with other CSP-based methods. The evaluation included comparing participant- specific accuracies with and without the proposed method across five effective connectivity metrics. The results showed consistent performance improvements and a significant reduction in the number of selected electrodes for all participants. Compared to state-of-the-art methods, our approach achieved the highest accuracies: 82% (13 out of 22 channels), 86.01% (29 out of 59 channels), and 87.56% (48 out of 118 channels) across three datasets.
