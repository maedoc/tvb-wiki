# Design of a 5G MIMO-OFDM System Using Artificial Neural Networks Under Realistic Channel Impairments

**Source**: semantic-scholar
**ID**: d2ab0a2cfdee0549cf57d242db1e01b544ef3e04
**DOI**: 10.29304/jqcsm.2026.18.12454
**URL**: https://www.semanticscholar.org/paper/d2ab0a2cfdee0549cf57d242db1e01b544ef3e04
**Date**: 2026-03-30
**Year**: 2026
**Authors**: Zahraa Luay Fouad
**Venue**: Journal of Al-Qadisiyah for Computer Science and Mathematics
**Citations**: 0

## Abstract

This paper attempts to design and compare an equalizer for a 5G 2×2 MIMO-OFDM system employing a data-driven ANN equalizer for realistic wireless channel impairments. The focus here is whether a data-driven equalizer approach can attain better or a comparable equalizer performance to classic linear techniques: Zero-Forcing (ZF), Minimum Mean Square Error (MMSE), MMSE-Successive Interference Cancellation MMSE-SIC, Decision Feedback Equalizer (DFE) but taking into account both accuracy and complexity. Build a 5G MIMO-OFDM simulator in Python for the physical 3GPP TDL-C and TDL-E and do add hurts like Doppler spread and existent inaccuracies like carrier frequency offset CFO phase noise and outdated or imperfect channel state information CSI. Propose a deep fully connected ANN and train using supervised learning on pairs of OFDMs exchanged using Monte Carlo simulating the wireless channel from the previous step. Vast range of SNR/Doppler/CFO/phase noise. Use the ANN as equalizer. For evaluation use BER/EVM/NMSE/and FLOPs and inference time per OFDM frame. Simulation results show that the ANN equalizer is much better than ZF and DFE. And matches / slightly better than MMSE and MMSE-SIC across varying SNR/Doppler/CFO/and phase noise – even in more severe settings with TDL-E with imperfect CSI. Finally, the ANN once trained has better latency for inference and FLOPs/value performance than classic equalizer results. Concluding that ANN based is a good avenue with a 5G MIMO-OFDM reception in mind.
