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

## Contents

- [Model and Knowledge Editing](#model-and-knowledge-editing) (1)
- [Analyses of Weight Edits](#analyses-of-weight-edits) (0)
- [Task Vectors, Task Arithmetic and Model Merging](#task-vectors-task-arithmetic-and-model-merging) (0)
- [Weight-Space Learning](#weight-space-learning) (0)
- [Weight Generation](#weight-generation) (0)
- [Weight-Based Interpretability](#weight-based-interpretability) (0)
- [Agent- and LLM-Driven Weight Editing](#agent--and-llm-driven-weight-editing) (0)
- [Benchmarks, Datasets and Model Zoos](#benchmarks-datasets-and-model-zoos) (0)
- [Surveys](#surveys) (0)
- [Contributing](#contributing)
- [License](#license)

## Model and Knowledge Editing

Methods that change specific facts or behaviours by computing or learning a targeted weight update.

- [Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262) - *Kevin Meng et al. (2022), NeurIPS 2022.* Locates factual recall in mid-layer MLPs and rewrites a fact with a closed-form rank-one weight update (ROME). [[Code](https://github.com/kmeng01/rome)]

**[⬆ back to top](#contents)**

## Analyses of Weight Edits

Work on what weight edits look like and how they fail, including rank-one structure, locality, side effects, and collapse under many edits.


**[⬆ back to top](#contents)**

## Task Vectors, Task Arithmetic and Model Merging

Treating fine-tuning deltas as vectors to add, negate, and combine, and merging trained models directly in weight space.


**[⬆ back to top](#contents)**

## Weight-Space Learning

Networks that take other networks' weights as input, including equivariant metanetworks, neural functionals, and weight embeddings.


**[⬆ back to top](#contents)**

## Weight Generation

Hypernetworks and generative models (diffusion, flow matching, autoregressive) that output network weights, including prompt-to-weights and text-to-LoRA.


**[⬆ back to top](#contents)**

## Weight-Based Interpretability

Reading what a network computes directly from its parameters, including parameter decomposition and circuit-level weight edits.


**[⬆ back to top](#contents)**

## Agent- and LLM-Driven Weight Editing

A model reading, generating, or modifying another model's (or its own) weights, including LLMs that write weight updates and agents that edit models.


**[⬆ back to top](#contents)**

## Benchmarks, Datasets and Model Zoos

Evaluation suites for weight edits and merges, and collections of trained networks for weight-space research.


**[⬆ back to top](#contents)**

## Surveys

Overviews of one or more WSP areas.


**[⬆ back to top](#contents)**

## Contributing

Contributions are welcome! The list is generated from [`papers.yaml`](papers.yaml): add an entry there, run `python scripts/build_readme.py`, and open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for the scope and the entry format.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work. See [LICENSE](LICENSE).

<sub>1 papers. This file is generated from `papers.yaml` by `scripts/build_readme.py`; do not edit it by hand.</sub>
