# Prediction of Combustion Parameters and Pollutant Emissions of a Dual-Fuel Engine Based on Recurrent Neural Networks

**Source**: semantic-scholar
**ID**: 58b971d79a86a0298c8da31ebaa53b6ef1d3e737
**DOI**: 10.3390/app15189868
**URL**: https://www.semanticscholar.org/paper/58b971d79a86a0298c8da31ebaa53b6ef1d3e737
**Date**: 2025-09-09
**Year**: 2025
**Authors**: Joel Freidy Ebolembang, Fabrice Parfait Nang Nkol, Lionel Merveil Anague Tabejieu, Fernand Toukap Nono, Claude Valéry Ngayihi Abbe
**Venue**: Applied Sciences
**Citations**: 1

## Abstract

A critical challenge in engine research lies in minimizing harmful emissions while optimizing the efficiency of internal combustion engines. Dual-fuel engines, operating with methanol and diesel, offer a promising alternative, but their combustion modeling remains complex due to the intricate thermochemical interactions involved. This study proposes a predictive framework that combines validated CFD simulations with deep learning techniques to estimate key combustion and emission parameters in a methanol–diesel dual-fuel engine. A three-dimensional CFD model was developed to simulate turbulent combustion, methanol injection, and pollutant formation, using the RNG k-ε turbulence model. A temporal dataset consisting of 1370 samples was generated, covering the compression, combustion, and early expansion phases—critical regions influencing both emissions and in-cylinder pressure dynamics. The optimal configuration identified involved a 63° spray injection angle and a 25% methanol proportion. A Gated Recurrent Unit (GRU) neural network, consisting of 256 neurons, a Tanh activation function, and a dropout rate of 0.2, was trained on this dataset. The model accurately predicted in-cylinder pressure, temperature, NOx emissions, and impact-related parameters, achieving a Pearson correlation coefficient of ρ = 0.997. This approach highlights the potential of combining CFD and deep learning for rapid and reliable prediction of engine behavior. It contributes to the development of more efficient, cleaner, and robust design strategies for future dual-fuel combustion systems.
