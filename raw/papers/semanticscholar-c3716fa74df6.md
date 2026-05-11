# Crowd Dynamics Demand Adaptivity: Self-Adaptive Physics-Informed Neural Network for Crowd Simulation

**Source**: semantic-scholar
**ID**: c3716fa74df6eb7ab272eddcfc9179aca61025ef
**DOI**: 10.1145/3746027.3754569
**URL**: https://www.semanticscholar.org/paper/c3716fa74df6eb7ab272eddcfc9179aca61025ef
**Date**: 2025-10-27
**Year**: 2025
**Authors**: Ziying Tan, Linbo Luo, Haiyan Yin, Y. Ong, Wentong Cai
**Venue**: ACM Multimedia
**Citations**: 2

## Abstract

Crowd simulation is crucial for urban planning, traffic management, public safety, and immersive environments. A fundamental challenge is capturing adaptive human behaviors that evolve dynamically with social interactions and task demands. Recently, physics-informed neural networks (PINNs) seamlessly integrate interpretable physics-based models with flexible data-driven learning, significantly enhancing simulation realism. However, current PINN-based methods typically rely on rigid representations of pedestrian perceptions and static task priorities of motion planning, limiting their ability to capture real-world social complexities and behavioral adaptability. To this end, we introduce SA-PINN, a novel Self-Adaptive Physics-Informed Neural Network specifically designed for modeling adaptive crowd behaviors. SA-PINN features two innovative adaptive modules: a self-adaptive social perception module, guided by a visual-field physics model to capture context-dependent social interactions dynamically; and a self-adaptive multi-task PINN training module, automatically balancing key motion objectives such as goal-reaching, collision avoidance, and alignment with real data. By jointly enabling perception-level and task-level adaptations within a unified physics-informed framework, SA-PINN generates highly realistic and physically consistent crowd simulations across diverse environmental contexts. Comprehensive evaluations on three real-world datasets (Lane, Cross 90, and GC) reveal that SA-PINN achieves a 29.7% gain in microscopic trajectory accuracy and enhances macroscopic density similarity by 23.5% compared to the best-performing baselines.
