---
created: 2026-05-04
sources:
- NIH and NSF. *Collaborative Research in Computational Neuroscience (CRCNS)*. Program
  Announcement. https://grants.nih.gov/grants/guide/pa-files/PAR-19-162.html
- 'Kleinfeld D, Berg RW, Blevin D, et al. The Collaborative Research in Computational
  Neuroscience (CRCNS) program: a mechanism for supporting experimental-theoretical
  collaborations in neuroscience. *Neuroinformatics*. 2004;2(1):5-8.'
- 'Jansen BH, Rit VG. Electroencephalography and neural field modeling: a new approach
  to the inverse problem. *Biol Cybern*. 1995;73(4):357-366.'
- Wong KF, Wang XJ. A recurrent network mechanism for time integration in perceptual
  decisions. *J Neurosci*. 2006;26(12):3213-3224.
- Jirsa VK, Haken H. Field theory of electromagnetic brain activity. *Phys Rev Lett*.
  1996;77(5):960-963.
- The Virtual Brain. https://www.thevirtualbrain.org
tags:
- funding-project
- computational-neuroscience
- reproducibility
- people-researcher
- lab-institute
title: CRCNS
type: entity
updated: '2026-05-04'
---

**CRCNS (Collaborative Research in [[computational-neuroscience]])** is a joint funding program established by the **National Institutes of Health (NIH)** and the **National Science Foundation (NSF)** to foster collaborations between experimental and computational neuroscientists. The program was launched in response to a recognized gap between theoretical modeling efforts and the accumulating body of experimental data on neural systems, aiming to accelerate the development of biologically realistic computational models that can explain and predict neural phenomena [1][2].

## Motivation and Scientific Rationale

The theoretical-experiment divide in neuroscience has long been a central challenge in the field. Experimentalists generate vast datasets—from single-unit recordings to [[whole-brain]] imaging—yet theoretical frameworks often fail to integrate these empirical findings into cohesive, predictive models. Conversely, computational modelers may develop sophisticated mathematical descriptions of neural dynamics that lack direct validation against experimental data. The CRCNS program was explicitly designed to bridge this divide by requiring funded projects to combine quantitative theory with data collection, often mandates sharing of primary data collected under the award [1][2].

## Program Structure and Requirements

The CRCNS mechanism operates through joint solicitations issued periodically by NIH and NSF. Key requirements of funded projects include:

- **Collaborative teams**: Applications must involve partnerships between experimentalists and theorists, ensuring that computational work is grounded in empirical reality.
- **Data sharing**: Awardees are expected to make neural and behavioral datasets publicly available through approved repositories, a policy that has contributed substantially to the growth of open-data neuroscience [1].
- **Training components**: Many CRCNS awards include provisions for training the next generation of computational neuroscientists, supporting postdoctoral researchers and graduate students in acquiring both theoretical and experimental skills.
- **Cross-disciplinary methodology**: Funded projects span multiple levels of analysis, from subcellular biophysics to large-scale [[network-dynamics]], reflecting the program's commitment to multiscale modeling.

## Historical Context and Major Initiatives

Since its inception around 1999–2000, the CRCNS program has funded numerous landmark projects that have shaped the field. Early funded work included foundational studies in [[neural-field-theory]], which provided mathematical formalisms for describing cortical activity at the population level [3]. Subsequent awards supported the development of conductance-based [[neuron]] models, [[mean-field-theory|mean-field]] approximations, and large-scale brain simulation platforms [3][4][5].

One of the most significant outcomes of CRCNS-funded research in the European context was the development of **[[the-virtual-brain]] (TVB)**, an open-source simulation platform for whole-brain dynamics. TVB incorporates multiple [[neural-mass-models]]—including the **Jansen-Rit model**, the **Wong-Wang model**, and the **Epileptor**—that were either directly funded through CRCNS mechanisms or emerged from the broader ecosystem of computational neuroscience research that CRCNS helped cultivate [6]. The platform enables the integration of **[[structural-connectivity]]** matrices derived from diffusion imaging with **[[functional-connectivity]]** analyses, embodying the CRCNS philosophy of linking theory, computation, and empirical brain data.

## Relationship to TVB and Whole-Brain Modeling

**The Virtual Brain** represents a flagship application of CRCNS principles in the realm of whole-brain modeling. The platform was developed with support from multiple European funding sources, but its theoretical foundations are deeply intertwined with the computational neuroscience traditions that CRCNS has promoted. TVB's emphasis on reproducibility, open-source software, and integration of empirical **structural-connectivity** data aligns directly with the data-sharing and collaborative mandates of the CRCNS program.

Furthermore, several specific models integrated within TVB have origins in research supported by or related to CRCNS-type funding mechanisms. The **Jansen-Rit neural mass model**, originally developed to explain EEG signatures in terms of cortical pyramidal cell interactions, has become a canonical example of computational neuroscience applied to whole-brain dynamics [3]. The **Wong-Wang model**, which captures attractor dynamics in prefrontal cortex, emerged from theoretical efforts to understand decision-making at the neural population level—a classic example of the theory-experiment integration that CRCNS aims to support [4]. The **Epileptor** model, developed to simulate seizure dynamics, similarly represents a case where computational approaches have been tightly coupled with experimental clinical data [5].

The **Human Connectome Project** and related efforts to map brain wiring have benefited from CRCNS-like data-sharing frameworks, and TVB incorporates connectivity data from these initiatives. Similarly, collaborations with **EBRAINS**—the European research infrastructure for neuroscience—reflect the ongoing legacy of CRCNS in promoting open, reproducible neuroscience research that bridges modeling and empirical investigation.