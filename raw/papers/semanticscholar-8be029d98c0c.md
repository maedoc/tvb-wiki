# Automatic detection of simulated artifacts on T1w magnetic resonance images: comparing performance of different QC strategies

**Source**: semantic-scholar
**ID**: 8be029d98c0c38e654e059d81b1c95ebb9a31fa4
**DOI**: 10.1101/2025.10.31.25339144
**URL**: https://www.semanticscholar.org/paper/8be029d98c0c38e654e059d81b1c95ebb9a31fa4
**Date**: 2025-11-02
**Year**: 2025
**Authors**: Janine Hendriks, M. G. Jansen, R. Joules, Ó. Peña-Nogales, P. Rodrigues, F. Barkhof, A. Schrantee, H. Mutsaerts
**Venue**: medRxiv
**Citations**: 0

## Abstract

The reliability of MRI-derived measures critically depends on image quality. Poor-quality scans can obscure anatomical detail and compromise the accuracy of automated image analysis, underscoring the need for robust quality control (QC) procedures. Automated QC offers scalability for large neuroimaging datasets, yet the comparative performance of different approaches for detecting specific artifact types remains poorly understood.

We systematically compared rule-based (RB), classical machine learning (ML), and deep learning (DL) QC algorithms using 1,000 high-quality T1w scans. Four artifact types, blurring, ghosting, motion, and noise were synthetically introduced across ten severity levels using TorchIO, yielding 40,000 degraded images. Visual QC of a subset confirmed strong inter-rater reliability (Krippendorffs =0.82, mean Spearmans {rho}=0.87). RB and ML models used 62 image quality metrics (IQMs) from MRIQC, whereas DL models were trained directly on minimally preprocessed images. Models were trained with participant-level five-fold cross-validation and tested on an independent dataset.

DL models achieved the highest overall performance across artifact types (Youdens Index=0.83-0.97). RB and ML performed comparably at high artifact severities (YI[≥]0.75) but showed limited sensitivity to subtle ghosting and noise (YI[≤]0.15). Feature analysis indicated that RB relied primarily on normative metrics, whereas ML flexibly adapted feature use by artifact type and severity.

These findings highlight DLs superior generalizability for detecting subtle artifacts and provide practical guidance for selecting QC strategies in large-scale neuroimaging pipelines, where reliable QC is essential for maintaining statistical power and reproducibility.
