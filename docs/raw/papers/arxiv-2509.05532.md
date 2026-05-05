# SuperSNN: A Hardware-Aware Framework for Physically Realizable, High-Performance Superconducting Spiking Neural Network Chips

**Source**: semantic-scholar
**ID**: 1c117e3b01cb20d080fdbff3a7f6f2c73c783c53
**DOI**: 10.48550/arXiv.2509.05532
**URL**: https://www.semanticscholar.org/paper/1c117e3b01cb20d080fdbff3a7f6f2c73c783c53
**Date**: 2025-09-05
**Year**: 2025
**Authors**: Changxu Song, Arda Çalışkan, Beyza Zeynep Ucpinar, Yasemin Kopur, M. A. Karamuftuoglu, S. Razmkhah, Shahin Nazarian, M. Pedram
**Venue**: arXiv.org
**Citations**: 2

## Abstract

Despite numerous proposed designs for superconducting neural networks (SNNs), most have overlooked practical fabrication constraints, leading to implementations limited to only a few neurons or synapses. Current superconducting technologies, such as MIT LL SFQ5ee, impose severe limitations on chip area, routing, and input/output pin counts (e.g., 5x5 mm^2 chip with 40 pins), drastically restricting network size and complexity. These hardware constraints necessitate a comprehensive framework to tailor network designs for physical realizability while minimizing accuracy loss. This paper introduces SuperSNN, a comprehensive framework for the implementation of full superconducting SNNs on a chip within these constraints. The key technical contributions include: (1) A hardware-aware training methodology for SNNs, utilizing off-chip pruning and weight quantization for energy-efficient superconducting implementations. (2) Design and layout of an inference SNN chip that incorporates novel high fan-in neurons and custom superconducting cells. (3) An optimized locally synchronous, globally synchronous (LAGS) clock distribution scheme for robust circuit implementation and management of data transfer delays in SFQ SNNs. The main results and findings demonstrate the effectiveness of the framework: (1) The complete network achieved 96.47% accuracy on the full MNIST dataset after quantization and pruning. (2) The fabricated SuperSNN chip successfully classified a reduced set of digits (2, 3, and 4) with 80.07% accuracy, reaching a maximum of 86.2% accuracy for digits 0, 1, and 2. (3) The chip operates at an ultra-high 3.02 GHz clock frequency. (4) It occupies a compact area of 3.4 x 3.9 mm^2, incorporates 5,822 Josephson Junctions, consumes 2.15 mW static power, and has an exceptionally low energy cost of 6.55 fJ (or 1.31e-6 nJ) per inference.
