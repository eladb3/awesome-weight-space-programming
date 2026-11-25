# Awesome Weight-Space Programming [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Check](https://github.com/eladb3/awesome-weight-space-programming/actions/workflows/check.yml/badge.svg)](https://github.com/eladb3/awesome-weight-space-programming/actions/workflows/check.yml)

> A curated list of papers on reading, editing, and writing the weights of neural networks directly.

**Weight-space programming (WSP)** is the practice of having a language model or agent work on a neural network's weights directly: *read* them to say what the network does, *edit* them to fix a failure or change a behaviour, or *write* them from scratch from a specification. It is guided by a goal stated in natural language instead of by gradient descent on data. The term was introduced by Takehi, Teoh, Zhang and Khattab in ["Sparks of Weight-Space Programming"](https://rikiyat.github.io/blog/weight-space-programming/) (MIT CSAIL, November 2026). Within weeks it was followed by replications, critiques, benchmarks, security studies, and applications from robotics to medicine.

The list has three parts:

- **[Weight-Space Programming](#weight-space-programming)**: the papers on LLMs and agents reading, editing, and writing weights.
- **[Foundations and Related Areas](#foundations-and-related-areas)**: older lines of work that already treat weights as something to compute, compose, learn from, or read. These are model and knowledge editing (ROME, MEMIT, MEND and successors), task arithmetic and model merging, weight-space learning, weight generation (hypernetworks, diffusion over weights, text-to-LoRA), and weight-based interpretability.
- **[Resources](#resources)**: benchmarks, datasets, tools, model zoos, and surveys.

Out of scope: ordinary fine-tuning, parameter-efficient fine-tuning that is only a training recipe, activation steering with no weight change, and pruning or quantization unless the paper is about weight-space structure.

Entries are sorted newest first within each section. Every entry has been checked against its arXiv or publisher page.
