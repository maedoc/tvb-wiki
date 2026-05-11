# Distributed cortico-subcortical networks enable robust speech state detection from sparse intracranial recordings

**Source**: semantic-scholar
**ID**: 08849c6bbf452444c2bfb14306bf73ef802cd820
**DOI**: 10.3389/fnins.2026.1816455
**URL**: https://www.semanticscholar.org/paper/08849c6bbf452444c2bfb14306bf73ef802cd820
**Date**: 2026-05-08
**Year**: 2026
**Authors**: Chen Feng, En Zhang, Yifei Jia, Zhoule Zhu, Junming Zhu, Di Wu, Kedi Xu
**Venue**: Frontiers in Neuroscience
**Citations**: 0

## Abstract


 
 Accurate and reliable detection of speech state transitions is a prerequisite for practical speech brain–computer interfaces (BCIs). While cortical language areas have been extensively studied, it remains unclear whether speech onset information is exclusively localized to these regions or distributed across a broader cortico-subcortical network. Here, we investigated the feasibility of decoding speech state transitions using sparse stereo-electroencephalography (SEEG) recordings that sample both cortical and subcortical structures.
 
 
 
 Four Mandarin-speaking epilepsy patients undergoing clinical SEEG monitoring performed a sentence-reading task. Neural signals were segmented and labeled as rest or speech based on acoustic onset. A convolutional neural network was trained to classify speech states using broadband or high-gamma features derived from different anatomical channel subsets. We further evaluated continuous decoding performance, model robustness to channel dropout, and the specific contributions of different brain regions.
 
 
 
 Speech state decoding accuracy exceeded chance level (50%) in all participants, with peak single-participant accuracies surpassing 90%. Models integrating both cortical and subcortical signals generally outperformed those restricted to a single anatomical domain. Notably, broadband signals yielded higher classification accuracy than high-gamma features. In continuous decoding simulations, performance remained above chance, although reduced relative to discretized evaluation. Crucially, decoding accuracy was robust to random channel reduction (up to 50%) and remained above 70% even after excluding classical speech-related cortical regions. Contribution analyses indicated participant-specific patterns of model sensitivity, with relatively higher contributions observed in frontal regions and the thalamus in multiple participants.
 
 
 
 These findings support the hypothesis that speech state information is represented in a distributed cortico-subcortical network rather than being confined to canonical language areas. The robustness of decoding performance despite channel reduction and regional exclusion suggests that sparsely sampled SEEG data can effectively drive speech detection modules. This study demonstrates the feasibility of utilizing deep brain recordings for speech BCIs, offering a pathway toward more stable and generalized implantable systems. Moreover, such autonomous speech state detection may also serve as an ethical safeguard, ensuring that neural language decoding is activated only during intended communicative acts.

