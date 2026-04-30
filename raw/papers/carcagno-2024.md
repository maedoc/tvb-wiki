---
title: "pybdf: Python library for BioSemi BDF files"
created: 2026-04-30
updated: 2026-04-30
type: source
tags: [software-python, eeg, biosemi, bdf, data-format]
sources: [https://github.com/scarcagno/pybdf]
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