# FCMagnet: A Fully Complex-Valued Magnetic Graph Convolutional Neural Network for Emotion Recognition Using Brain Effective Connectivity

**Source**: semantic-scholar
**ID**: ae895ac8c8d0961c11907ca2fbbfb2761a43e23b
**DOI**: 10.1109/ACCESS.2026.3667596
**URL**: https://www.semanticscholar.org/paper/ae895ac8c8d0961c11907ca2fbbfb2761a43e23b
**Year**: 2026
**Authors**: Armin Pishehvar, Eghbal G. Mansoori, Abbas Mehrbaniyan, R. Tahmasebi
**Venue**: IEEE Access
**Citations**: 1

## Abstract

Emotions play a foundational role in human cognition and social interactions, influencing interpersonal relationships, communication effectiveness, decision-making, and the customization of health and technology services. Accurately interpreting these internal emotional states from physiological signals is methodologically challenging, especially when it comes to decoding emotions from neurophysiological data, which presents significant signal-processing and representational difficulties. Electroencephalography (EEG) has been a primary modality for decoding emotions, but it is complicated by unique complexities that hinder reliable interpretation. Additionally, existing literature has mainly focused on broad emotional distinctions, such as positive versus negative emotions, and has given relatively little attention to classification of multiple emotional states, like distinguishing between nine discrete emotional categories. We propose FCMagnet, a fully complex-valued magnetic graph convolutional network for nine-class EEG emotion recognition. Directed effective connectivity is estimated via MVAR modeling and Partial Directed Coherence and encoded as Hermitian (magnetic) Laplacians. FCMagnet applies complex spectral filtering, native complex linear and convolutional layers with polar-tanh activations, and a complex-valued label encoding that maps the arousal–valence circumplex to prototype points in the complex plane. Evaluated on the FACED dataset, FCMagnet achieves $33.4~\pm ~4.0$ % nine-class accuracy and improved F1 relative to classical real-valued GNNs while remaining compact. Results demonstrate that fully complex spectral filtering of effective connectivity yields richer, phase-aware representations for fine-grained emotion decoding.
