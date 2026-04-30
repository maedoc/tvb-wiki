---
title: BioSemi BDF Format Specification
created: 2026-04-30
updated: 2026-04-30
type: source
tags: [data-format ,eeg ,biosemi]
authors:
  - S. Perreault
year: 2011
venue: IETF
doi: 10.17487/rfc6350
bibtex: |
  @book{perreault2011biosemi,
    title={BioSemi BDF Format Specification},
    author={"S. Perreault"},
    year={2011},
    doi={10.17487/rfc6350},
  }
---




# BioSemi BDF Format Specification

The BioSemi Data Format (BDF) is a 24-bit extension of the European Data Format (EDF) developed by BioSemi B.V. for high-density EEG recordings. Unlike the original 16-bit EDF format, BDF uses three bytes per sample to achieve 24-bit resolution, providing significantly higher dynamic range for electrophysiological signals. The format includes a dedicated status channel for encoding trigger events and system status information.

## Key Technical Details

- **24-bit encoding**: Each sample is stored as a 3-byte signed integer, allowing for much finer resolution than 16-bit formats
- **Status channel**: The final channel in BDF files encodes trigger codes and system status (CMS active/inactive, battery level, quality metrics)
- **Header structure**: Similar to EDF but with modifications for handling the increased bit depth and additional metadata
- **Sampling rates**: Supports rates up to 4096 Hz per channel
- **Channel count**: Practically limited only by hardware; systems with 256+ channels are supported