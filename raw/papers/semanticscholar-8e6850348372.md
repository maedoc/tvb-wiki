# FastCTM (v1.0): Atmospheric chemical transport modelling with a principle-informed neural network for air quality simulations

**Source**: semantic-scholar
**ID**: 8e68503483724e5dbb99628a6bf5ffb90dfd6d19
**DOI**: 10.5194/gmd-18-6295-2025
**URL**: https://www.semanticscholar.org/paper/8e68503483724e5dbb99628a6bf5ffb90dfd6d19
**Date**: 2025-09-25
**Year**: 2025
**Authors**: Baolei Lyu, Ran Huang, Xinlu Wang, Weiguo Wang, Yongtao Hu
**Venue**: Geoscientific Model Development
**Citations**: 3

## Abstract

Abstract. Chemical-transport models (CTMs) are indispensable for air-quality assessment and policy development, yet their operational use is hampered by high computational cost. We present FastCTM, a physics-informed neural-network emulator that rapidly predicts hourly concentrations of ten key pollutant variables: major PM2.5 species (SO42-, NO3-, NH4-, organic matter, elemental carbon, crustal material), coarse PM10, SO2, NO2, CO, and O3. FastCTM embeds five process-specific neural modules – primary emissions, horizontal transport, turbulent diffusion, chemical reactions and deposition within a unified framework. Given 1 h initial condition data, FastCTM can simulate future 24 h concentrations for ten air pollutants using corresponding meteorological fields and emissions as input. Trained on 2018–2022 WRF-CMAQ forecasts over China and evaluated on 2023 data, FastCTM reproduces CMAQ with mean RMSE (µg m−3) of 9.1, 11.9, 4.4, 4.0, 48.9, 10.9 and R2 of 0.80, 0.81, 0.80, 0.83, 0.90, 0.70 for PM2.5, PM10, SO2, NO2, CO and O3, respectively. Sensitivity tests confirm physically plausible responses to temperature, wind speed, boundary-layer height and precursor emissions. The modular architecture enables quantitative process analysis, offering CTM-like insight at GPU-accelerated speeds. In a nutshell, FastCTM provides a computationally efficient solution for air-quality simulations, sensitivity analysis, and process attribution with high accuracy and physical consistency.

