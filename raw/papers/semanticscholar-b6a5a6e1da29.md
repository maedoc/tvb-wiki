# A paper mill detection model based on citation manipulation paradigm

**Source**: semantic-scholar
**ID**: b6a5a6e1da29db0311cf9fa4da6fdfe345eb54ea
**DOI**: 10.2478/jdis-2025-0003
**URL**: https://www.semanticscholar.org/paper/b6a5a6e1da29db0311cf9fa4da6fdfe345eb54ea
**Date**: 2025-01-06
**Year**: 2025
**Authors**: Jun Zhang, Jianhua Liu, E. Haihong, Tianyi Hu, Xiaodong Qiao, Zichen Tang
**Venue**: Journal of Data and Information Science
**Citations**: 3

## Abstract

ABSTRACT Purpose In this paper, we develop a heterogeneous graph network using citation relations between papers and their basic information centered around the “Paper mills” papers under withdrawal observation, and we train graph neural network models and classifiers on these heterogeneous graphs to classify paper nodes. Design/methodology/approach Our proposed citation network-based “Paper mills” detection model (PDCN model for short) integrates textual features extracted from the paper titles using the BERT model with structural features obtained from analyzing the heterogeneous graph through the heterogeneous graph attention network model. Subsequently, these features are classified using LGBM classifiers to identify “Paper mills” papers. Findings On our custom dataset, the PDCN model achieves an accuracy of 81.85% and an F1-score of 80.49% in the “Paper mills” detection task, representing a significant improvement in performance compared to several baseline models. Research limitations We considered only the title of the article as a text feature and did not obtain features for the entire article. Practical implications The PDCN model we developed can effectively identify “Paper mills” papers and is suitable for the automated detection of “Paper mills” during the review process. Originality/value We incorporated both text and citation detection into the “Paper mills” identification process. Additionally, the PDCN model offers a basis for judgment and scientific guidance in recognizing “Paper mills” papers.
