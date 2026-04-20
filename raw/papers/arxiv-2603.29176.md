# Predicting Neuromodulation Outcome for Parkinson's Disease with Generative Virtual Brain Model

**arXiv ID**: 2603.29176
**Published**: 2026-03-31
**Updated**: 2026-03-31
**Authors**: Siyuan Du, Siyi Li, Shuwei Bai, Ang Li, Haolin Li, Mingqing Xiao, Yang Pan, Dongsheng Li, Weidi Xie, Yanfeng Wang, Ya Zhang, Chencheng Zhang, Jiangchao Yao
**Categories**: q-bio.NC, cs.AI, cs.CE, cs.CV
**URL**: https://arxiv.org/abs/2603.29176
**PDF**: https://arxiv.org/pdf/2603.29176
**Source**: arXiv

## Abstract

Parkinson's disease (PD) affects over ten million people worldwide. Although temporal interference (TI) and deep brain stimulation (DBS) are promising therapies, inter-individual variability limits empirical treatment selection, increasing non-negligible surgical risk and cost. Previous explorations either resort to limited statistical biomarkers that are insufficient to characterize variability, or employ AI-driven methods which is prone to overfitting and opacity. We bridge this gap with a pretraining-finetuning framework to predict outcomes directly from resting-state fMRI. Critically, a generative virtual brain foundation model, pretrained on a collective dataset (2707 subjects, 5621 sessions) to capture universal disorder patterns, was finetuned on PD cohorts receiving TI (n=51) or DBS (n=55) to yield individualized virtual brains with high fidelity to empirical functional connectivity (r=0.935). By constructing counterfactual estimations between pathological and healthy neural states within these personalized models, we predicted clinical responses (TI: AUPR=0.853; DBS: AUPR=0.915), substantially outperforming baselines. External and prospective validations (n=14, n=11) highlight the feasibility of clinical translation. Moreover, our framework provides state-dependent regional patterns linked to response, offering hypothesis-generating mechanistic insights.
