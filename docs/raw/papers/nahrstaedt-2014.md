---
title: "Status Channel Parsing in BioSemi BDF Files"
created: 2026-04-30
updated: 2026-04-30
type: source
tags: [eeg, biosemi, data-format, status-channel, trigger]
sources: [https://github.com/holgern/pyedflib/issues, https://www.biosemi.com/Format.htm]
---

# Status Channel Parsing in BioSemi BDF Files

The status channel in BioSemi BDF files encodes both experimental trigger events and system status information. However, the documentation of this encoding is incomplete, leading to challenges for developers of analysis software.

## Contents of Status Channel

The BioSemi status channel typically contains:
1. **Trigger codes**: Event markers for experimental stimuli (values 1-255)
2. **System status**: CMS (Common Mode Sense) active/inactive flags
3. **Quality indicators**: Signal quality metrics
4. **Time markers**: Hardware timestamps

## Parsing Challenges

- **Incomplete documentation**: BioSemi provides partial documentation; edge cases are undocumented
- **Format variations**: Different BioSemi amplifier models encode status differently
- **Byte order**: The three-byte status channel requires careful parsing
- **Event collisions**: System status bits may overlap with trigger codes
- **Community workarounds**: Various analysis packages (MNE-Python, EEGLAB, pyedflib) implement different parsing strategies with varying degrees of completeness

The lack of a standardized, fully-documented parsing scheme means that researchers must often validate trigger extraction empirically or consult community discussions for specific use cases.