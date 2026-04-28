# DiffLSTM-MTE: A Hybrid LSTM-Diffusion Framework for Virtual iEEG Reconstruction From MEG

**Source**: semantic-scholar
**ID**: 554ba2bab0d7b2393cf51b1aa437182558f76e72
**DOI**: 10.1109/ACCESS.2026.3665952
**URL**: https://www.semanticscholar.org/paper/554ba2bab0d7b2393cf51b1aa437182558f76e72
**Year**: 2026
**Authors**: Xiangyu Xue, Liankun Ren, Hongyu Zhou, Anqi Dai, Di Wang, Huaqiang Zhang
**Venue**: IEEE Access
**Citations**: 0

## Abstract

Accurate non-invasive characterization of complex brain dynamics, especially aberrant network activity in epilepsy, is crucial yet challenging due to the invasiveness of iEEG and limitations of non-invasive MEG. We introduce DiffLSTM-MTE, a novel deep learning framework that reconstructs virtual iEEG (ViEEG) from MEG recordings. This framework synergistically integrates an LSTM for temporal modeling of MEG with a conditional Denoising Diffusion Probabilistic Model (DDPM) for synthesizing realistic iEEG. Our physiologically-informed training objective incorporates losses for noise prediction, spectral fidelity, and Interictal Epileptiform Discharges (IEDs) preservation. Evaluated on data from five epilepsy patients, DiffLSTM-MTE demonstrates high temporal fidelity (mean Pearson <inline-formula> <tex-math notation="LaTeX">$R=0.71\pm 0.08$ </tex-math></inline-formula>), preserves spectral characteristics (The mean PSD RMSE is <0.071), reconstructs spatial coherence (mean correlation <inline-formula> <tex-math notation="LaTeX">$0.92\pm 0.04$ </tex-math></inline-formula>), and accurately characterizes IEDs (76% <inline-formula> <tex-math notation="LaTeX">$\pm ~7$ </tex-math></inline-formula>% alignment). These results highlight DiffLSTM-MTE’s potential as a non-invasive tool to enhance epilepsy diagnostics and pre-surgical assessment by providing richer, patient-specific neurophysiological insights.
