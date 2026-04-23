# Predicting Alzheimer's disease progression using rs-fMRI and a history-aware graph neural network

**Source**: arxiv
**ID**: 2604.06469
**URL**: https://arxiv.org/abs/2604.06469
**Date**: 2026-04-07
**Year**: 2026
**Authors**: Mahdi Moghaddami, Mohammad-Reza Siadat, Austin Toma, Connor Laming, Huirong Fu
**Categories**: cs.CV

## Abstract

Alzheimer's disease (AD) is a neurodegenerative disorder that affects more than seven million people in the United States alone. AD currently has no cure, but there are ways to potentially slow its progression if caught early enough. In this study, we propose a graph neural network (GNN)-based model for predicting whether a subject will transition to a more severe stage of cognitive impairment at their next clinical visit. We consider three stages of cognitive impairment in order of severity: cognitively normal (CN), mild cognitive impairment (MCI), and AD. We use functional connectivity graphs derived from resting-state functional magnetic resonance imaging (rs-fMRI) scans of 303 subjects, each with a different number of visits. Our GNN-based model incorporates a recurrent neural network (RNN) block, enabling it to process data from the subject's entire visit history. It can also work with irregular time gaps between visits by incorporating visit distance information into our input features. Our model demonstrates robust predictive performance, even with missing visits in the subjects' visit histories. It achieves an accuracy of 82.9%, with an especially impressive accuracy of 68.8% on CN to MCI conversions - a task that poses a substantial challenge in the field. Our results highlight the effectiveness of rs-fMRI in predicting the onset of MCI or AD and, in conjunction with other modalities, could offer a viable method for enabling timely interventions to slow the progression of cognitive impairment.
