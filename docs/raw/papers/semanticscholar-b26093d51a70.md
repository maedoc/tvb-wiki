# Nested hierarchical group-wise registration with a graph-based subgrouping strategy for efficient template construction

**Source**: semantic-scholar
**ID**: b26093d51a70abc87629e65992572f1806710d46
**DOI**: 10.1016/j.media.2025.103624
**URL**: https://www.semanticscholar.org/paper/b26093d51a70abc87629e65992572f1806710d46
**Date**: 2025-05-01
**Year**: 2025
**Authors**: Tongtong Che, Lin Zhang, Debin Zeng, Yan Zhao, Haoying Bai, Jichang Zhang, Xiuying Wang, Shuyu Li
**Venue**: Medical Image Anal.
**Citations**: 1

## Abstract

Accurate and efficient group-wise registration for medical images is fundamentally important to construct a common template image for population-level analysis. However, current group-wise registration faces the challenges posed by the algorithm's efficiency and capacity, and adaptability to large variations in the subject populations. This paper addresses these challenges with a novel Nested Hierarchical Group-wise Registration (NHGR) framework. Firstly, to alleviate the registration burden due to significant population variations, a new subgrouping strategy is proposed to serve as a "divide and conquer" mechanism that divides a large population into smaller subgroups. The subgroups with a hierarchical sequence are formed by gradually expanding the scale factors that relate to feature similarity and then conducting registration at the subgroup scale as the multi-scale conquer strategy. Secondly, the nested hierarchical group-wise registration is proposed to conquer the challenges due to the efficiency and capacity of the model from three perspectives. (1) Population level: the global group-wise registration is performed to generate age-related sub-templates from local subgroups progressively to the global population. (2) Subgroup level: the local group-wise registration is performed based on local image distributions to reduce registration error and achieve rapid optimization of sub-templates. (3) Image pair level: a deep multi-resolution registration network is employed for better registration efficiency. The proposed framework was evaluated on the brain datasets of adults and adolescents, respectively from 18 to 96 years and 5 to 21 years. Experimental results consistently demonstrated that our proposed group-wise registration method achieved better performance in terms of registration efficiency, template sharpness, and template centrality.
