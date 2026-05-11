# Neural Configuration-Space Barriers for Manipulation Planning and Control

**Source**: semantic-scholar
**ID**: 8ba5642487d2f3167d8210d81481f353618ba314
**DOI**: 10.48550/arXiv.2503.04929
**URL**: https://www.semanticscholar.org/paper/8ba5642487d2f3167d8210d81481f353618ba314
**Date**: 2025-03-06
**Year**: 2025
**Authors**: Kehan Long, K. Lee, N. Raicevic, Niyas Attasseri, Melvin Leok, Nikolay Atanasov
**Venue**: arXiv.org
**Citations**: 4

## Abstract

Planning and control for high-dimensional robot manipulators in cluttered, dynamic environments require both computational efficiency and robust safety guarantees. Inspired by recent advances in learning configuration-space distance functions (CDFs) as robot body representations, we propose a unified framework for motion planning and control that formulates safety constraints as CDF barriers. A CDF barrier approximates the local free configuration space, substantially reducing the number of collision-checking operations during motion planning. However, learning a CDF barrier with a neural network and relying on online sensor observations introduce uncertainties that must be considered during control synthesis. To address this, we develop a distributionally robust CDF barrier formulation for control that explicitly accounts for modeling errors and sensor noise without assuming a known underlying distribution. Simulations and hardware experiments on a 6-DoF xArm manipulator show that our neural CDF barrier formulation enables efficient planning and robust real-time safe control in cluttered and dynamic environments, relying only on onboard point-cloud observations.
