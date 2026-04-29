---
created: 2026-04-23
sources:
- raw/papers/semanticscholar-eb4197c24bf2.md
- raw/papers/arxiv-2505.16861.md
- raw/papers/arxiv-2509.12873.md
tags:
- software-brain-modeling
title: OpenViBE
type: entity
updated: '2026-04-29'
---

title: OpenViBE
created: 2025-01-15
updated: 2026-04-29
type: entity
tags: [[neuroimaging]]-eeg, [[neuroimaging]]-meg, electrophysiology, software-visualization
sources:
  - https://openvibe.inria.fr/
  - https://hal.science/hal-00477153
  - https://inria.hal.science/inria-00551379
  - https://www.bbci.de/competition/iv/results/

---

# OpenViBE

## Overview

OpenViBE is an open-source software platform designed for real-time processing of neurophysiological signals, primarily electroencephalography (EEG) and magnetoencephalography (MEG) data. Developed at the French National Institute for Research in Computer Science and Automation (Inria) under the leadership of Anatole Lécuyer, OpenViBE provides a modular framework for building brain-computer interface (BCI) applications, neurofeedback systems, and real-time neuroscience experiments. The platform combines a visual programming environment with a comprehensive library of signal processing algorithms, enabling researchers to design, prototype, and deploy real-time brain signal analysis pipelines without extensive programming knowledge.

The software emerged from the French BCI research community in the mid-2000s, with its initial releases focused on providing a standardized platform for BCI research that could interface with various EEG acquisition systems [1]. OpenViBE has since expanded to support a broader range of neurophysiological modalities and is widely used in laboratories conducting research on neural decoding, neuroplasticity through neurofeedback, and cognitive neuroscience experiments requiring real-time signal analysis.

## Key Features

OpenViBE offers several distinctive capabilities that make it particularly valuable for real-time brain signal research. The platform's visual programming environment, called the **OpenViBE Designer**, allows users to construct signal processing pipelines by connecting pre-built boxes representing individual algorithms through a drag-and-drop interface. This visual approach significantly reduces the barrier to entry for researchers who may be proficient in neuroscience but less experienced with software development, while simultaneously accelerating the prototyping of new experimental paradigms.

The software includes an extensive library of signal processing modules spanning preprocessing (filtering, artifact rejection, spatial filtering), feature extraction (spectral analysis, spatial decomposition methods like PCA and ICA), and classification algorithms ([[linear]] classifiers, support vector machines, neural networks). Particularly notable is OpenViBE's implementation of motor imagery classification pipelines, which have been extensively validated in BCI competitions and benchmark datasets [2]. The platform also provides dedicated modules for evoked potential detection, including the P300 event-related potential commonly used in attention and oddball paradigm research.

OpenViBE supports real-time operation through a dedicated acquisition server that can stream data from various EEG and MEG systems via standardized protocols, including GDF/EDF for file storage and LSL (Lab Streaming Layer) for real-time streaming [3]. This real-time capability is essential for closed-loop experiments where neural signals must be processed and decoded with minimal latency to enable responsive neurofeedback or BCI control. The software achieves latencies on the order of tens of milliseconds for typical processing pipelines, making it suitable for most BCI and neurofeedback applications [4].

## Relationship to TVB

While OpenViBE and [[TVB]] (The Virtual Brain) serve distinct roles in the [[computational-neuroscience]] ecosystem, they can be complementary tools within a research pipeline. OpenViBE focuses on real-time signal acquisition and processing—the "input" side of brain modeling—whereas The Virtual Brain provides large-scale [[brain-network]] simulations for studying dynamics at the [[whole-brain]] level. In practice, empirical data processed through OpenViBE can inform [[whole-brain-modeling]] efforts by providing estimates of [[functional-connectivity]] or by validating simulated signals against real EEG/MEG recordings.

The two platforms also differ in their modeling approaches: OpenViBE primarily operates at the level of signal features and classification, often using relatively simple linear models for real-time decodeability, while [[TVB]] implements sophisticated [[neural-mass-models]] and [[whole-brain-modeling]] frameworks that simulate the underlying dynamical systems generating the observed neural activity. Researchers studying epilepsy modeling or brain stimulation might use OpenViBE for real-time monitoring during experiments while employing TVB for retrospective simulation and prediction.

## Technical Implementation

The OpenViBE platform consists of several interconnected software components that work together to enable real-time neurophysiological signal processing. The **Acquisition Server** handles communication with hardware recording systems, performing initial digitization and streaming data to the processing pipeline. The **Designer** provides the graphical environment for building processing chains, while the **Runtime** executes the constructed pipelines with minimal latency to ensure timely signal processing and feedback delivery.

Under the hood, OpenViBE uses a box-and-stream architecture where data flows between processing modules (boxes) as continuous streams. Each box implements a specific algorithm and communicates with adjacent boxes through typed data buffers, allowing flexible reconfiguration of processing chains. The platform supports integration with [[tractography]] systems from multiple manufacturers through vendor-specific drivers, and can export processed signals in standard formats for offline analysis in tools like [[eeglab]] or [[fieldtrip]].

## Key Papers

1. Renard, Y., Lotte, F., Gibert, G., Congedo, M., Maby, E., Delannoy, V., Bertrand, O., & Lécuyer, A. (2010). OpenViBE: An Open-Source Software Platform to Design, Test and Use Brain-Computer Interfaces in Real and Virtual Environments. *Presence: Teleoperators and Virtual Environments*, 19(1), 35-53. https://doi.org/10.1162/pres.19.1.35 [5]

2. Renard, Y., Bonnet, L., Payan, B., Bougrain, L., & Lécuyer, A. (2010). OpenViBE Tutorial: A Novel Open-Source Software to Design, Test and Use Brain-Computer Interfaces. *BCI Meeting 2010*, Asilomar. [6]

3. Brodu, N., Lotte, F., & Lécuyer, A. (2012). Exploring Two Novel Features for EEG-based Brain-Computer Interfaces: Multifractal Cumulants and Predictive Complexity. *Neurocomputing*, 79, 87-94. [7]

## Related Software

OpenViBE occupies a niche in the neurophysiology software landscape that partially overlaps with several other widely-used tools. [[eeglab]] provides comprehensive offline signal processing capabilities for EEG data but lacks native real-time operation; similarly, [[fieldtrip]] excels at offline analysis but requires additional infrastructure for real-time applications. For real-time BCI applications, OpenViBE competes with [[bci2000]], another established platform that has been widely used in BCI research communities. The platform also relates to [[mne-python]] and [[spikeinterface]], which offer sophisticated analysis pipelines for neurophysiological data, though these are primarily oriented toward offline analysis in Python rather than real-time processing.

For researchers working with [[electrophysiology]] data who require both real-time capabilities and integration with large-scale brain modeling, OpenViBE may be used in conjunction with simulation environments like [[nest]] or [[the-virtual-brain]], where the former handles signal acquisition and processing while the latter provides computational models of brain dynamics. The complementary nature of these tools reflects the broader trend toward integrated experimental-computational neuroscience workflows that bridge empirical measurement and theoretical modeling.

## References

[1] OpenViBE Official Website. https://openvibe.inria.fr/

[2] BCI Competition IV Results. https://www.bbci.de/competition/iv/results/

[3] OpenViBE Supported File Formats. https://openvibe.inria.fr/supported-file-formats/

[4] OpenViBE Documentation - Latency Configuration. http://openvibe.inria.fr/drivers-openbci/

[5] Renard, Y. et al. (2010). OpenViBE: An Open-Source Software Platform to Design, Test and Use Brain-Computer Interfaces in Real and Virtual Environments. *Presence: Teleoperators and Virtual Environments*, 19(1), 35-53. https://hal.science/hal-00477153

[6] Renard, Y. et al. (2010). OpenViBE Tutorial: A Novel Open-Source Software to Design, Test and Use Brain-Computer Interfaces. *BCI Meeting 2010*. https://inria.hal.science/inria-00551379

[7] Brodu, N., Lotte, F., & Lécuyer, A. (2012). Exploring Two Novel Features for EEG-based Brain-Computer Interfaces. *Neurocomputing*, 79, 87-94.