# Open-source Large Language Models can Generate Labels from Radiology Reports for Training Convolutional Neural Networks.

**Source**: semantic-scholar
**ID**: e942dd09b787e0747516c3c6d37cd0199fbd9e01
**DOI**: 10.1016/j.acra.2024.12.028
**URL**: https://www.semanticscholar.org/paper/e942dd09b787e0747516c3c6d37cd0199fbd9e01
**Date**: 2025-01-01
**Year**: 2025
**Authors**: Fares Al Mohamad, Leonhard Donle, Felix J. Dorfner, Laura Romanescu, K. Drechsler, M. P. Wattjes, J. Nawabi, Marcus R. Makowski, Hartmut Häntze, Lisa C Adams, Lina Xu, Felix Busch, Aymen Meddeb, K. Bressem
**Venue**: Academic Radiology
**Citations**: 15

## Abstract

RATIONALE AND OBJECTIVES
Training Convolutional Neural Networks (CNN) requires large datasets with labeled data, which can be very labor-intensive to prepare. Radiology reports contain a lot of potentially useful information for such tasks. However, they are often unstructured and cannot be directly used for training. The recent progress in large language models (LLMs) might introduce a new useful tool in interpreting radiology reports. This study aims to explore the use of the LLM to classify radiology reports and generate labels. These labels will be utilized then to train a CNN to detect ankle fractures to evaluate the effectiveness of using automatically generated labels.


MATERIALS AND METHODS
We used the open-weight LLM Mixtral-8×7B-Instruct-v0.1 to classify radiology reports of ankle x-ray images. The generated labels were used to train a CNN to recognize ankle fractures. The model's accuracy, sensitivity, specificity, and area under the receiver operating characteristics curve were used for evaluation.


RESULTS
Using common prompt engineering techniques, a prompt was found that reached an accuracy of 92% on a test dataset. By parsing all radiology reports using the LLM, a training dataset of 15,896 images and labels was created. Using this dataset, a CNN was trained, which achieved an accuracy of 89.5% and an area under the receiver operating characteristic curve of 0.926 on a test dataset.


CONCLUSION
Our classification model based on labels generated with a large language model achieved high accuracy. This performance is comparable to models trained with manually labeled data, demonstrating the potential of language models in automating the labeling process.


SUMMARY
Large language models can be used to reliably detect pathologies in radiology reports.


KEY RESULTS
In this study, 7561 radiological reports of ankle X-ray images were automatically classified as describing an ankle fracture or not using a large language model. Using a dataset of 250 reports, the language model showed a classification accuracy of 92%. The generated labels were used to train an image classifier to detect ankle fractures on X-ray images. 15,896 images were used for training. The resulting model achieved an accuracy of 89.5% on a test dataset.
