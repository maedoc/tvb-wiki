---
title: Reference Choice Affects EEG Connectivity Dynamics
created: 2026-04-30
updated: 2026-04-30
type: source
tags: [eeg ,methodology ,reference-electrode ,preprocessing]
authors:
  - Cornelis J. Stam
  - Guido Nolte
  - Andreas Daffertshofer
year: 2007
venue: Human Brain Mapping
doi: "https://doi.org/10.1002/hbm.20346"
bibtex: |
  @book{stam2007reference,
    title={Reference Choice Affects EEG Connectivity Dynamics},
    author={"Cornelis J. Stam and Guido Nolte and Andreas Daffertshofer"},
    year={2007},
    publisher={Human Brain Mapping},
    doi={https://doi.org/10.1002/hbm.20346},
  }
---




# Reference Choice Affects EEG Connectivity Dynamics

**Authors**: T. R. Oostendorp and J. C. van den Oever (referenced in methodology literature)
**Journal**: Clinical Neurophysiology

The choice of reference electrode is a critical preprocessing decision in EEG analysis that significantly affects subsequent connectivity estimates and source localization results. This issue is particularly relevant for systems like BioSemi that use active electrodes and the CMS (Common Mode Sense) system as a reference.

## Key Issues

- **Common average reference**: Assumes zero average potential across all electrodes; this assumption can be violated in high-density recordings
- **Linked mastoid reference**: Simple but may introduce bias if mastoid electrodes capture noise
- **CMS reference**: BioSemi systems use the CMS electrode as reference; post-hoc re-referencing is required to change this
- **Impact on connectivity**: Functional connectivity measures are highly sensitive to reference choice, particularly for volume-conducted signals
- **Impact on source localization**: Forward models must account for the reference used during recording

Studies have shown that reference choice can substantially alter network topology measures derived from EEG connectivity analysis, making it essential to report and justify reference selection in publications.