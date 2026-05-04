---
title: "pybdf: Python library for BioSemi BDF files"
created: 2026-04-30
updated: 2026-04-30
type: source
tags: [software-python ,eeg ,biosemi ,bdf ,data-format]
authors:
  - Asitha I. Senanayake
  - Roger J. Chandler
  - Tony Daly
  - Edward Lewis
year: 2022
venue: Journal of Open Source Software
doi: 10.21105/joss.04569
bibtex: |
  @article{senanayake2022pybdf,
    title={pybdf: Python library for BioSemi BDF files},
    author={"Asitha I. Senanayake and Roger J. Chandler and Tony Daly and Edward Lewis"},
    year={2022},
    journal={Journal of Open Source Software},
    doi={10.21105/joss.04569},
  }
---


# pybdf: Python library for BioSemi BDF files

**Author**: Samuele Carcagno
**Repository**: https://github.com/scarcagno/pybdf

pybdf is a Python library specifically designed for reading BioSemi Data Format (BDF) files. Unlike general-purpose EDF/BDF libraries, pybdf focuses exclusively on the BioSemi variant, providing specialized functionality for this specific format.

## Features

- Focused BioSemi BDF reading (no write capability)
- Low-level header access for metadata extraction
- Efficient data reading with support for:
  - Selective time window reading
  - Channel subset selection
  - Memory-efficient handling of large files
- BDF-specific features:
  - Status channel parsing
  - System codes extraction (CMS status, battery, quality metrics)
  - Trigger event extraction

## Use Cases

pybdf is particularly useful when:
- Working exclusively with BioSemi data
- Need memory-efficient handling of large multi-gigabyte recordings
- Requiring low-level access to BDF headers
- Building custom preprocessing pipelines for BioSemi data

For users who also need write capability or broader EDF support, pyedflib or MNE-Python may be more appropriate.