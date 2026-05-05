# When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models

**Source**: arxiv
**ID**: 2605.00817
**URL**: https://arxiv.org/abs/2605.00817
**Date**: 2026-05-01
**Year**: 2026
**Authors**: Sailesh Panda, Pritam Kadasi, Abhishek Upperwal, Mayank Singh
**Categories**: cs.CL

## Abstract

Large language models (LLMs) often achieve strong performance on reasoning benchmarks, but final-answer accuracy alone does not show whether they faithfully execute the procedure specified in a prompt. We study this question through a controlled diagnostic benchmark for procedural execution, where models are given a step-wise arithmetic algorithm and two numeric inputs, and must return the final computed value. The benchmark uses simple arithmetic operations but increases complexity through algorithm length and look-back dependencies over intermediate variables. Across 14 models and 55 datasets, average first-answer accuracy drops from 61% on 5-step procedures to 20% on 95-step procedures. Generation-level analysis shows that failures often involve missing answers, premature answers, self-correction after an initial error, under-executed traces, and hallucinated extra steps. These findings suggest that apparent reasoning ability can mask substantial weaknesses in faithful instruction execution.
