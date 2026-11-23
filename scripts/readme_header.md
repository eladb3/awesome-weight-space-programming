# Awesome Weight-Space Programming [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Check](https://github.com/eladb3/awesome-weight-space-programming/actions/workflows/check.yml/badge.svg)](https://github.com/eladb3/awesome-weight-space-programming/actions/workflows/check.yml)

> A curated list of papers on reading, editing, and writing the weights of trained neural networks directly.

**Weight-space programming (WSP)** treats the weights of a trained network as an object you program: something you directly *read* (to find out what the network computes), *edit* (to change specific behaviour or knowledge), and *write* (to create or combine networks), instead of something you reach only indirectly by running gradient descent on data.

In scope:

- **Model and knowledge editing**: closed-form or learned weight updates that change specific facts or behaviours (ROME, MEMIT, MEND and successors), and analyses of what those edits look like in weight space.
- **Task vectors and model merging**: arithmetic on fine-tuning deltas, and combining trained models in weight space.
- **Weight-space learning**: networks that take other networks' weights as input.
- **Weight generation**: hypernetworks and generative models that output weights, including prompt-to-weights and text-to-LoRA methods.
- **Weight-based interpretability**: reading function from parameters, parameter decomposition, and circuit-level weight edits.
- **Agent- and LLM-driven weight editing**: one model reading or modifying another model's (or its own) weights.
- **Benchmarks, datasets, model zoos, and surveys** for the above.

Out of scope: ordinary fine-tuning, parameter-efficient fine-tuning that is only a training recipe, activation steering with no weight change, and pruning or quantization unless the paper is about weight-space structure.

Entries are sorted newest first within each section. Every entry has been checked against its arXiv or publisher page. Years are the year of the first public version, usually arXiv v1.
