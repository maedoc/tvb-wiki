# Big data approaches to bovine bioacoustics: a FAIR-compliant dataset and scalable ML framework for precision livestock welfare

**Source**: semantic-scholar
**ID**: 077796f397e5e5037bd3b1341e2e83242cc65d3f
**DOI**: 10.3389/fdata.2025.1723155
**URL**: https://www.semanticscholar.org/paper/077796f397e5e5037bd3b1341e2e83242cc65d3f
**Date**: 2025-10-16
**Year**: 2025
**Authors**: Mayuri Kate, Suresh Neethirajan
**Venue**: Frontiers Big Data
**Citations**: 2

## Abstract

The convergence of IoT sensing, edge computing, and machine learning is revolutionizing precision livestock farming. Yet bioacoustic data streams remain underexploited due to computational-complexity and ecological-validity challenges. We present one of the most comprehensive bovine vocalization datasets to date-569 expertly curated clips spanning 48 behavioral classes, recorded across three commercial dairy farms using multi-microphone arrays and expanded to 2,900 samples through domain-informed data augmentation. This FAIR-compliant resource addresses key Big Data challenges: volume (90 h of raw recordings, 65.6 GB), variety (multi-farm, multi-zone acoustic environments), velocity (real-time processing requirements), and veracity (noise-robust feature-extraction pipelines). A modular data-processing workflow combines denoising implemented both in iZotope RX 11 for quality control and an equivalent open-source Python pipeline using noisereduce, multi-modal synchronization (audio-video alignment), and standardized feature engineering (24 acoustic descriptors via Praat, librosa, and openSMILE) to enable scalable welfare monitoring. Preliminary machine-learning benchmarks reveal distinct class-wise acoustic signatures across estrus detection, distress classification, and maternal-communication recognition. The dataset's ecological realism-embracing authentic barn acoustics rather than controlled conditions-ensures deployment-ready model development. This work establishes the foundation for animal-centered AI, where bioacoustic streams enable continuous, non-invasive welfare assessment at industrial scale. By releasing a Zenodo-hosted, FAIR-compliant dataset (restricted access) and an open-source preprocessing pipeline on GitHub, together with comprehensive metadata schemas, we advance reproducible research at the intersection of Big Data analytics, sustainable agriculture, and precision livestock management. The framework directly supports UN SDG 9, demonstrating how data science can transform traditional farming into intelligent, welfare-optimized production systems capable of meeting global food demands while maintaining ethical animal-care standards.
