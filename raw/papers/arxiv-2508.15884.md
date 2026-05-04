# Jet-Nemotron: Efficient Language Model with Post Neural Architecture Search

**Source**: semantic-scholar
**ID**: c7b8d5f73f1b7a49e83e30c7215c247956cdae2f
**DOI**: 10.48550/arXiv.2508.15884
**URL**: https://www.semanticscholar.org/paper/c7b8d5f73f1b7a49e83e30c7215c247956cdae2f
**Date**: 2025-08-21
**Year**: 2025
**Authors**: Yuxian Gu, Qinghao Hu, Shang Yang, Haocheng Xi, Junyu Chen, Song Han, Han Cai
**Venue**: arXiv.org
**Citations**: 22

## Abstract

We present Jet-Nemotron, a new family of hybrid-architecture language models, which matches or exceeds the accuracy of leading full-attention models while significantly improving generation throughput. Jet-Nemotron is developed using Post Neural Architecture Search (PostNAS), a novel neural architecture exploration pipeline that enables efficient model design. Unlike prior approaches, PostNAS begins with a pre-trained full-attention model and freezes its MLP weights, allowing efficient exploration of attention block designs. The pipeline includes four key components: (1) learning optimal full-attention layer placement and elimination, (2) linear attention block selection, (3) designing new attention blocks, and (4) performing hardware-aware hyperparameter search. Our Jet-Nemotron-2B model achieves comparable or superior accuracy to Qwen3, Qwen2.5, Gemma3, and Llama3.2 across a comprehensive suite of benchmarks while delivering up to 53.6x generation throughput speedup and 6.1x prefilling speedup. It also achieves higher accuracy on MMLU and MMLU-Pro than recent advanced MoE full-attention models, such as DeepSeek-V3-Small and Moonlight, despite their larger scale with 15B total and 2.2B activated parameters.
