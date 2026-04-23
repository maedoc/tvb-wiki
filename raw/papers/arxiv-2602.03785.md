# From Pre- to Intra-operative MRI: Predicting Brain Shift in Temporal Lobe Resection for Epilepsy Surgery

**Source**: arxiv
**ID**: 2602.03785
**URL**: https://arxiv.org/abs/2602.03785
**Date**: 2026-02-03
**Year**: 2026
**Authors**: Jingjing Peng, Giorgio Fiore, Yang Liu, Ksenia Ellum, Debayan Daspupta, Keyoumars Ashkan, Andrew McEvoy, Anna Miserocchi, Sebastien Ourselin, John Duncan, Alejandro Granados
**Categories**: cs.CV

## Abstract

Introduction: In neurosurgery, image-guided Neurosurgery Systems (IGNS) highly rely on preoperative brain magnetic resonance images (MRI) to assist surgeons in locating surgical targets and determining surgical paths. However, brain shift invalidates the preoperative MRI after dural opening. Updated intraoperative brain MRI with brain shift compensation is crucial for enhancing the precision of neuronavigation systems and ensuring the optimal outcome of surgical interventions. Methodology: We propose NeuralShift, a U-Net-based model that predicts brain shift entirely from pre-operative MRI for patients undergoing temporal lobe resection. We evaluated our results using Target Registration Errors (TREs) computed on anatomical landmarks located on the resection side and along the midline, and DICE scores comparing predicted intraoperative masks with masks derived from intraoperative MRI. Results: Our experimental results show that our model can predict the global deformation of the brain (DICE of 0.97) with accurate local displacements (achieve landmark TRE as low as 1.12 mm), compensating for large brain shifts during temporal lobe removal neurosurgery. Conclusion: Our proposed model is capable of predicting the global deformation of the brain during temporal lobe resection using only preoperative images, providing potential opportunities to the surgical team to increase safety and efficiency of neurosurgery and better outcomes to patients. Our contributions will be publicly available after acceptance in https://github.com/SurgicalDataScienceKCL/NeuralShift.
