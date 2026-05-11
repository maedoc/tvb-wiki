# Unraveling Patterns in mTLE: A DWI-Centric and Machine Learning Investigation

**Source**: semantic-scholar
**ID**: 52867e41005c3e4b3af9cb98d7e8e426b3ecb7ad
**DOI**: 10.1109/EMBC58623.2025.11254142
**URL**: https://www.semanticscholar.org/paper/52867e41005c3e4b3af9cb98d7e8e426b3ecb7ad
**Date**: 2025-07-01
**Year**: 2025
**Authors**: Hadi Kamkar, Seyed Alireza Khanghahi, Hossein Rahimzadeh, Fatemeh Salimi, Mohammad-Reza Nazem-Zadeh
**Venue**: Annual International Conference of the IEEE Engineering in Medicine and Biology Society
**Citations**: 0

## Abstract

Background: Mesial temporal lobe epilepsy (mTLE) is one of the most common forms of drug-resistant epilepsy. Diffusion weighted imaging (DWI) is gaining interest as a safer alternative to neuroimaging techniques like 18F-FDG PET, which uses ionizing radiation for mTLE lateralization identification. This study aimed to develop machine learning models using DWI-derived features to classify left mTLE, right mTLE, and healthy controls.Methods: DWI data were collected from 66 subjects (24 left mTLE, 22 right mTLE, and 20 healthy controls). Features were extracted using MRtrix software. Three feature selection methods (genetic algorithm, principal component analysis, and XGBoost) were compared, followed by classification using four different algorithms (support vector machines, decision tree, ridge classifier, and naïve Bayes). Model performance was evaluated using a 5-fold cross-validation.Results: The genetic algorithm consistently outperformed other feature selection methods across all datasets. The ridge classifier achieved the highest performance with accuracies of 0.957 (F1-score: 0.920) for left vs. normal, 0.957 (F1-score: 0.937) for right vs. normal, and 0.839 (F1-score: 0.815) for left vs. right classification. Key discriminative features included measures of local efficiency, modularity, clustering coefficient, betweenness centrality, and PageRank in specific brain regions.Conclusion: This study demonstrates the potential of DWI-based machine learning models for automated lateralization of mTLE. The high accuracy achieved suggests that this approach could serve as a reliable, non-invasive tool for clinical decision-making in mTLE diagnosis and surgical planning.Clinical Relevance— The study underscores the clinical value of DWI and AI in accurately identifying the side of the brain affected by mTLE, presenting DWI as an alternative yet effective neuroimaging approach.
