# Timing Synchronization and Symbol Detection in Ambient Backscatter Communication

**Source**: semantic-scholar
**ID**: d758eb4342253a60ef83491d3ed25c00933352c8
**DOI**: 10.1109/TWC.2026.3675785
**URL**: https://www.semanticscholar.org/paper/d758eb4342253a60ef83491d3ed25c00933352c8
**Year**: 2026
**Authors**: Yuxin Li, Guangyue Lu, Yinghui Ye, Zehui Xiong, Marie Siew, Liqin Shi, Xuli Gao
**Venue**: IEEE Transactions on Wireless Communications
**Citations**: 0

## Abstract

Ambient backscatter communication (AmBC) enables ultra-low-power, low-cost and massive connectivity. However, practical AmBC systems suffer from symbol timing offset (STO) due to propagation delay and backscatter receiver (BR) activation latency, while conventional correlation-based synchronization methods are inapplicable because ambient radio frequency sources are non-cooperative. Moreover, residual STO (RSTO) inevitably remains due to the finite synchronization sequence, which degrades symbol detection performance. To address these challenges, we first design a specialized synchronization sequence with alternating “0” and “1” bits at the backscatter device to induce observable sampling errors at the BR. Based on this, we propose a pilot-aided, sampling-error-aware maximum likelihood estimation (PSE-MLE) method for STO estimation and compensation, which exploits the statistical variations in the received synchronization signal. After STO compensation, the remaining RSTO is statistically modeled as a discrete bilateral Laplace distribution, with its parameter estimated via ridge regression. Leveraging this prior information, we further develop a Bayesian average energy detector (ave-ED) and derive closed-form expressions for both the detection threshold and bit error rate. Simulation and experimental results on a practical AmBC platform validate the effectiveness of the proposed methods.
