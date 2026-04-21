# Network inference via approximate Bayesian computation. Illustration on a stochastic multi-population neural mass model

**arXiv ID**: 2306.15787
**Published**: 2023-06-27
**Updated**: 2025-08-26
**Authors**: Susanne Ditlevsen, Massimiliano Tamborrino, Irene Tubikanec
**Categories**: stat.ME, math.NA
**URL**: https://arxiv.org/abs/2306.15787
**PDF**: https://arxiv.org/pdf/2306.15787
**Source**: arXiv

## Abstract

In this article, we propose an adapted sequential Monte Carlo approximate Bayesian computation (SMC-ABC) algorithm for network inference in coupled stochastic differential equations (SDEs) used for multivariate time series modeling. Our approach is motivated by neuroscience, specifically the challenge of estimating brain connectivity before and during epileptic seizures. To this end, we make four key contributions. First, we introduce a 6N-dimensional SDE to model the activity of N coupled neuronal populations, extending the (single-population) stochastic Jansen and Rit neural mass model used to describe human electroencephalography (EEG) rhythms, particularly epileptic activity. Second, we construct a reliable and efficient numerical splitting scheme for the model simulation. Third, we apply the proposed adapted SMC-ABC algorithm to the neural mass model and validate it on different types of simulated data. Compared to standard SMC-ABC, our approach significantly reduces computational cost by requiring fewer model simulations to reach the desired posterior region, thanks to the inclusion of binary parameters describing the presence or absence of coupling directions. Finally, we apply our method to real multi-channel EEG data, uncovering potential similarities in patients' brain activities across different epileptic seizures, as well as differences between pre-seizure and seizure periods.
