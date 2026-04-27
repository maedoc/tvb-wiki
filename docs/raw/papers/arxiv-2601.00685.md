# Human-like AI-based Auto-Field-in-Field Whole-Brain Radiotherapy Treatment Planning With Conversation Large Language Model Feedback

**Source**: semantic-scholar
**ID**: 49598dd4e5463e182a83f2d7ebdf64d2d8ab27fa
**URL**: https://www.semanticscholar.org/paper/49598dd4e5463e182a83f2d7ebdf64d2d8ab27fa
**Date**: 2026-01-02
**Year**: 2026
**Authors**: A. Jafar, A. Qin, G. Atkins, Xiaoyu Hu, Yin Gao, Xun Jia
**Venue**: arXiv.org
**Citations**: 0

## Abstract

Background: Whole-brain radiotherapy (WBRT) is a common treatment due to its simplicity and effectiveness. While automated Field-in-Field (Auto-FiF) functions assist WBRT planning in modern treatment planning systems, it still requires manual approaches for optimal plan generation including patient-specific hyperparameters definition and plan refinement based on quality feedback. Purpose: This study introduces an automated WBRT planning pipeline that integrates a deep learning (DL) Hyperparameter Prediction model for patient-specific parameter generation and a large-language model (LLM)-based conversational interface for interactive plan refinement. Methods: The Hyperparameter Prediction module was trained on 55 WBRT cases using geometric features of clinical target volume (CTV) and organs at risk (OARs) to determine optimal Auto-FiF settings in RayStation treatment planning system. Plans were generated under predicted hyperparameters. For cases in which the generated plan was suboptimal, quality feedback via voice input was captured by a Conversation module, transcribed using Whisper, and interpreted by GPT-4o to adjust planning settings. Plan quality was evaluated in 15 independent cases using clinical metrics and expert review, and model explainability was supported through analysis of feature importance. Results: Fourteen of 15 DL-generated plans were clinically acceptable. Normalized to identical CTV D95% as the clinical plans, the DL-generated and clinical plans showed no statistically significant differences in doses to the eyes, lenses, or CTV dose metrics D1% and D99%. The DL-based planning required under 1 minute of computation and achieved total workflow execution in approximately 7 minutes with a single mouse click, compared to 15 minutes for manual planning. In cases requiring adjustment, the Conversational module successfully improved dose conformity and hotspot reduction. Conclusions: The proposed system improves planning efficiency while maintaining clinically acceptable plan quality. It demonstrates the feasibility of combining DL-based hyperparameter prediction with LLM interaction for streamlined, high-quality WBRT planning.
