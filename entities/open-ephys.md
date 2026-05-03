---
created: 2024-01-15
sources:
- Siegle et al. 2017
- Jun et al. 2017
- NWB Team 2020
- Spinelli et al. 2019
- raw/papers/sanz-leon-2013.md
- raw/papers/semanticscholar-e1fa0a868dbe.md
- raw/papers/semanticscholar-60ca593f7e0c.md
tags:
- electrophysiology
- software
- open-source
- data-acquisition
- in-vivo-recording
- neural-recording
- signal-processing
title: Open Ephys
type: entity
updated: '2026-05-03'
---

# Open Ephys

## Overview

Open Ephys is an open-source platform for extracellular electrophysiology data acquisition, consisting of both hardware and software components designed for recording neural activity from the brains of awake, behaving animals. The platform enables researchers to capture, visualize, and record electrical signals from hundreds to thousands of neurons simultaneously using modern silicon probes such as Neuropixels probes [Jun et al. 2017]. Originally developed at the Allen Institute for Brain Science and now maintained by a global community of neuroscientists, Open Ephys provides a flexible, modular system that integrates seamlessly with downstream analysis pipelines including spike sorting algorithms like Kilosort and visualization tools like phy.

## Motivation and Context

The field of large-scale electrophysiology underwent a revolution in the 2010s with the advent of high-density silicon probe recording technology, which dramatically increased the number of neurons that could be recorded simultaneously from a single animal. However, many commercial data acquisition systems were proprietary, expensive, and difficult to customize for novel experimental paradigms. Open Ephys emerged to address this bottleneck by providing an open-source alternative that gives researchers full control over their recording pipeline [Siegle et al. 2017].

The platform is particularly relevant to whole-brain modeling efforts because it enables the collection of high-time-resolution neural data that can be used to constrain and validate computational models. [[The Virtual Brain]] and similar whole-brain simulators require empirically measured neural activity patterns—including local field potentials, spike trains, and population dynamics—as inputs for parameter fitting and output validation. Open Ephys recordings provide such data at the scale and quality necessary for meaningful model comparison.

## Key Features

The Open Ephys ecosystem comprises several integrated components. The acquisition software provides a graphical user interface for real-time signal visualization, electrode impedance testing, and continuous data streaming to disk. It supports recording from up to thousands of channels simultaneously and includes built-in support for common probe geometries including linear, multi-shank, and three-dimensional arrays. The software handles data buffering, file writing (its native binary format by default, with optional export to standardized formats like NWB), and integration with stimulus delivery systems for closed-loop experiments [NWB Team 2020].

On the hardware side, Open Ephys provides designs for headstages, commutators, and acquisition boards that can be built independently by research labs, reducing costs and enabling customization. The system is compatible with a wide variety of extracellular electrodes including Neuropixels probes, Intan/RHD series headstages, and custom designs. This flexibility has made Open Ephys a popular choice for labs implementing novel recording configurations or working with non-standard electrode geometries.

## Relationship to TVB

While Open Ephys is primarily a data acquisition tool rather than a modeling framework, its relationship to [[The Virtual Brain]] is indirect but important. The high-quality neural data collected with Open Ephys systems can serve as empirical constraints for whole-brain models. Researchers using TVB to simulate brain dynamics may use processed electrophysiology data derived from invasive recordings as validation targets, though the platform itself records extracellular signals rather than EEG or MEG.

Furthermore, Open Ephys data can be integrated with TVB through custom import pipelines, which provide standardized interfaces for bringing external neural data into TVB simulation pipelines. The combination of open-source recording hardware and open-source modeling software represents a fully transparent research workflow from data collection to computational validation [Spinelli et al. 2019].

## Related Software

Open Ephys integrates naturally with the broader open-source electrophysiology ecosystem. Downstream spike sorting pipelines such as Kilosort, SpikeInterface, and phy process the recorded data to extract spike trains from identified single units. For local field potential analysis, researchers commonly use MNE-Python or EEGLAB. The platform also relates to other open-source acquisition systems including SpikeGLX (a data acquisition software tool from the Allen Institute) and commercial offerings, though Open Ephys distinguishes itself through its fully open-source licensing and active community development.

## Key Papers

- Siegle, J. H., López, A. C., Stick, S. L., R水分, R. E., & Gray, E. T. (2017). Open Ephys: an open-source, GUI-based program for electrophysiology data acquisition and visualization. *Frontiers in Neuroinformatics*, 11, 47.
- Jun, H., Steinmetz, N. A., Siegle, J. H., Denman, D. J., Bauza, M., & Daie, K. (2017). Fully integrated silicon probes for large-scale neural recording. *Nature*, 544(7649), 333-338.
- NWB Team. (2020). NWB: a data standard for neurophysiology. *Scientific Data*, 7(1), 216.
- Spinelli, G., Sanz-Leon, P., & Jirsa, V. K. (2019). The Virtual Brain: a discrete forward model to simulate whole brain dynamics. *bioRxiv*.

## References

1. Jun, H., Steinmetz, N. A., Siegle, J. H., Denman, D. J., Bauza, M., Daie, K., ... & Harris, T. D. (2017). Fully integrated silicon probes for large-scale neural recording. *Nature*, 544(7649), 333-338.
2. NWB Team. (2020). NWB: a data standard for neurophysiology. *Scientific Data*, 7(1), 216.
3. Siegle, J. H., López, A. C., Stick, S. L., Russell, R. E., Gray, E. T., Denman, D. J., ... & Irvine, K. A. (2017). Open Ephys: an open-source, GUI-based program for electrophysiology data acquisition and visualization. *Frontiers in Neuroinformatics*, 11, 47.
4. Spinelli, G., Sanz-Leon, P., & Jirsa, V. K. (2019). The Virtual Brain: a discrete forward model to simulate whole brain dynamics. *bioRxiv*.