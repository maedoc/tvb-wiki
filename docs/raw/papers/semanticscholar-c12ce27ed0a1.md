# VAE deep learning model with domain adaptation, transfer learning and harmonization for diagnostic classification from multi-site neuroimaging data

**Source**: semantic-scholar
**ID**: c12ce27ed0a15532dfc30c4e97b1ac0a2207ae16
**DOI**: 10.3389/fninf.2025.1553035
**URL**: https://www.semanticscholar.org/paper/c12ce27ed0a15532dfc30c4e97b1ac0a2207ae16
**Date**: 2025-09-11
**Year**: 2025
**Authors**: Shailesh Appukuttan, Gemma C. Monté-Rubio, Gopikrishna Deshpande, Bonian Lu, Nguyen Huynh, D. Rangaprakash
**Venue**: Frontiers Neuroinformatics
**Citations**: 0

## Abstract

In large public multi-site fMRI datasets, the sample characteristics, data acquisition methods, and MRI scanner models vary across sites and datasets. This non-neural variability obscures neural differences between groups and leads to poor machine learning based diagnostic classification of neurodevelopmental conditions. This could be potentially addressed by domain adaptation, which aims to improve classification performance in a given target domain by utilizing the knowledge learned from a different source domain by making data distributions of the two domains as similar as possible. In order to demonstrate the utility of domain adaptation for multi-site fMRI data, this research developed a variational autoencoder—maximum mean discrepancy (VAE-MMD) deep learning model for three-way diagnostic classification: (i) Autism, (ii) Asperger's syndrome, and (iii) typically developing controls. This study chooses ABIDE-II (Autism Brain Imaging Data Exchange) dataset as the target domain and ABIDE-I as the source domain. The results show that domain adaptation from ABIDE-I to ABIDE-II provides superior test accuracy of ABIDE-II compared to just using ABIDE-II for classification. Further, augmenting the source domain with additional healthy control subjects from Healthy Brain Network (HBN) and Amsterdam Open MRI Collection (AOMIC) datasets enables transfer learning and improves ABIDE-II classification performance. Finally, a comparison with statistical data harmonization techniques, such as ComBat, reveals that domain adaptation using VAE-MMD achieves comparable performance, and incorporating transfer learning (TL) with additional healthy control data substantially improves classification accuracy beyond that achieved by statistical methods (such as ComBat) alone. The dataset and the model used in this study are publicly available. The neuroimaging community can explore the possibility of further improving the model by utilizing the ever-increasing amount of healthy control fMRI data in the public domain.
