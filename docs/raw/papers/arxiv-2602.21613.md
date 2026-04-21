# Virtual Biopsy for Intracranial Tumors Diagnosis on MRI

**arXiv ID**: 2602.21613
**Published**: 2026-02-25
**Updated**: 2026-02-25
**Authors**: Xinzhe Luo, Shuai Shao, Yan Wang, Jiangtao Wang, Yutong Bai, Jianguo Zhang
**Categories**: cs.CV, cs.AI
**URL**: https://arxiv.org/abs/2602.21613
**PDF**: https://arxiv.org/pdf/2602.21613
**Source**: arXiv

## Abstract

Deep intracranial tumors situated in eloquent brain regions controlling vital functions present critical diagnostic challenges. Clinical practice has shifted toward stereotactic biopsy for pathological confirmation before treatment. Yet biopsy carries inherent risks of hemorrhage and neurological deficits and struggles with sampling bias due to tumor spatial heterogeneity, because pathological changes are typically region-selective rather than tumor-wide. Therefore, advancing non-invasive MRI-based pathology prediction is essential for holistic tumor assessment and modern clinical decision-making.   The primary challenge lies in data scarcity: low tumor incidence requires long collection cycles, and annotation demands biopsy-verified pathology from neurosurgical experts. Additionally, tiny lesion volumes lacking segmentation masks cause critical features to be overwhelmed by background noise. To address these challenges, we construct the ICT-MRI dataset - the first public biopsy-verified benchmark with 249 cases across four categories. We propose a Virtual Biopsy framework comprising: MRI-Processor for standardization; Tumor-Localizer employing vision-language models for coarse-to-fine localization via weak supervision; and Adaptive-Diagnoser with a Masked Channel Attention mechanism fusing local discriminative features with global contexts. Experiments demonstrate over 90% accuracy, outperforming baselines by more than 20%.
