# Awesome Weight-Space Programming [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Check](https://github.com/eladb3/awesome-weight-space-programming/actions/workflows/check.yml/badge.svg)](https://github.com/eladb3/awesome-weight-space-programming/actions/workflows/check.yml)

> A curated list of papers on reading, editing, and writing the weights of neural networks directly.

**Weight-space programming (WSP)** is the practice of having a language model or agent work on a neural network's weights directly: *read* them to say what the network does, *edit* them to fix a failure or change a behaviour, or *write* them from scratch from a specification. It is guided by a goal stated in natural language instead of by gradient descent on data. The term was introduced by Takehi, Teoh, Zhang and Khattab in ["Sparks of Weight-Space Programming"](https://www.lesswrong.com/llmRuns/zSHqRnRtDKnuAGNpW) (MIT CSAIL, November 2026). Within weeks it was followed by replications, critiques, benchmarks, security studies, and applications from robotics to medicine.

The list has three parts:

- **[Weight-Space Programming](#weight-space-programming)**: the papers on LLMs and agents reading, editing, and writing weights.
- **[Foundations and Related Areas](#foundations-and-related-areas)**: older lines of work that already treat weights as something to compute, compose, learn from, or read. These are model and knowledge editing (ROME, MEMIT, MEND and successors), task arithmetic and model merging, weight-space learning, weight generation (hypernetworks, diffusion over weights, text-to-LoRA), and weight-based interpretability.
- **[Resources](#resources)**: benchmarks, datasets, tools, model zoos, and surveys.

Out of scope: ordinary fine-tuning, parameter-efficient fine-tuning that is only a training recipe, activation steering with no weight change, and pruning or quantization unless the paper is about weight-space structure.

Entries are sorted newest first within each section. Every entry has been checked against its arXiv or publisher page.

## Contents

- [Weight-Space Programming](#weight-space-programming) (45)
  - [Reading Weights](#reading-weights) (4)
  - [Editing and Repairing Models](#editing-and-repairing-models) (15)
  - [Writing Weights from Scratch](#writing-weights-from-scratch) (14)
  - [Self-Editing Models](#self-editing-models) (3)
  - [Replications, Critiques and Alternatives](#replications-critiques-and-alternatives) (6)
  - [Security](#security) (3)
- [Foundations and Related Areas](#foundations-and-related-areas) (185)
  - [Model and Knowledge Editing](#model-and-knowledge-editing) (38)
  - [Analyses of Weight Edits](#analyses-of-weight-edits) (22)
  - [Task Vectors, Task Arithmetic and Model Merging](#task-vectors-task-arithmetic-and-model-merging) (36)
  - [Weight-Space Learning](#weight-space-learning) (36)
  - [Weight Generation](#weight-generation) (28)
  - [Weight-Based Interpretability](#weight-based-interpretability) (25)
- [Resources](#resources) (29)
  - [Benchmarks, Datasets, Tools and Model Zoos](#benchmarks-datasets-tools-and-model-zoos) (21)
  - [Surveys and Position Papers](#surveys-and-position-papers) (8)
- [Contributing](#contributing)
- [License](#license)

## Weight-Space Programming

Language models and agents that read, edit, or write the weights of other networks (or their own) directly, guided by a goal in natural language rather than by gradient descent.

### Reading Weights

Models that inspect another network's weights or weight diffs and say what the network does.

- [From LoRA to Language: Recovering Skill Documents from Adapters](https://arxiv.org/abs/2611.09454) - *Saranya Dintakurthy Swadha et al. (2026), arXiv preprint.* Tries to recover the skill document that a LoRA adapter was compiled from, comparing weights-only readers with agents that run or diff the adapter.
- [Weight-space programming for auditing clinical decision networks](https://arxiv.org/abs/2611.05341) - *Humza Nusrat and Omar Nusrat (2026), arXiv preprint.* An LLM audits clinical decision networks from their weights alone and repairs a hidden shortcut by changing a handful of parameters.
- [Weight Oracles: Reading Neural Network Weights with Language Models](https://arxiv.org/abs/2610.07334) - *Krishna Kabra et al. (2026), NeurIPS 2026 Workshop.* Fine-tunes LLMs to read another network's raw weights as tokens and answer diagnostic questions about it, such as whether it contains a backdoor.
- [Learning to Interpret Weight Differences in Language Models](https://arxiv.org/abs/2510.05092) - *Avichal Goel et al. (2025), arXiv preprint.* Trains a model to describe its own fine-tuning weight diff in natural language, exposing hidden behaviours and new knowledge from weights alone.

**[⬆ back to top](#contents)**

### Editing and Repairing Models

An LLM or agent changes an existing network's weights to fix a failure or change a behaviour.

- [Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation](https://arxiv.org/abs/2611.27089) - *Yalin Yang et al. (2026), arXiv preprint.* Compares an LLM-written weight patch with LoRA fine-tuning on spatial-reasoning tasks for a small LM.
- [Weight-space programming and mechanistic interpretability for model editing in particle physics](https://arxiv.org/abs/2611.27079) - *Raphaël Bonnet-Guerrini et al. (2026), arXiv preprint.* Combines LLM weight-space programming with SAE-guided analysis to remove an infrared-safety violation from a particle-physics foundation model by direct weight edits.
- [Weight-Space Programming Writes In-Context Learning and Matches Fine-Tuning in Language Models](https://arxiv.org/abs/2611.26841) - *Konstantinos Skianis and Aristidis Likas (2026), arXiv preprint.* Frontier editors turn in-context examples into MLP weight edits so a weaker LM performs the task with an empty prompt, matching ICL and LoRA fine-tuning.
- [Training Vision Models for LLM-Driven Weight-Space Programming](https://arxiv.org/abs/2611.26408) - *Timo Ropinski and Sebastian Kranz (2026), arXiv preprint.* Benchmarks LLM weight editing of CNNs and ViTs at scale and proposes training networks to be easier for LLMs to edit.
- [Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights](https://arxiv.org/abs/2611.25257) - *Jiajun Fan et al. (2026), arXiv preprint.* A frontier model diagnoses why a small VLM falls into reasoning loops and fixes it by rewriting the VLM's weights, given only the symptom.
- [Can Weight-Space Programming Alter Learned Ethical Priorities?](https://arxiv.org/abs/2611.24330) - *Kai Yi Ji (2026), arXiv preprint.* Edits the fitted choice weights of a concept-supervised text model to change how it trades off keeping a pledge against helping more people.
- [Weight Space Programming for Vision Language Model Repair](https://arxiv.org/abs/2611.23615) - *Avinash Goutham Aluguvelly (2026), arXiv preprint.* Plants faults in VLM weights and checks each repair a coding agent makes, revealing which cues gradient-free weight repairs rely on.
- [What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement](https://arxiv.org/abs/2611.22228) - *Zitian Gao et al. (2026), arXiv preprint.* Compares LM-written weight-update programs for diffusion concept editing against published editors and finds a mostly negative result.
- [Can AI Mature a Model's Geometry? Training-Free Weight Baking in LLMs](https://arxiv.org/abs/2611.21310) - *Amin Golnari and Saeid Sanei (2026), arXiv preprint.* An analyst model reads topological summaries of a frozen LM's layers and proposes a transformation that is written into its FFN weights in closed form.
- [Weight-Space Programming Changes How an LLM Uses Python for Computational Biology](https://arxiv.org/abs/2611.20566) - *Makoto Sato (2026), arXiv preprint.* A frontier LLM edits a small LM's weights and changes how it uses Python on computational-biology problems, nearly doubling strictly correct answers.
- [Weights & Caches: LLMs Can Program Tabular Foundation Models](https://arxiv.org/abs/2611.20174) - *Shi Bin Hoo et al. (2026), arXiv preprint.* Shows that LLMs can program statistical computations into a tabular foundation model's weights directly.
- [Mixed Signals: Weight-Space Programming for EEG and ECG](https://arxiv.org/abs/2611.13758) - *Dara Varam et al. (2026), arXiv preprint.* Applies LLM weight reading and editing to EEG and ECG models, repairing planted faults by reasoning rather than gradient descent.
- [Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations](https://arxiv.org/abs/2611.09382) - *Junru Hu et al. (2026), arXiv preprint.* Systematic study of agent weight-editing trajectories on small LMs: small localized edits can give large gains, but generalization across tasks is inconsistent.
- [Can LLMs Debug Robots by Editing Their Weights?](https://arxiv.org/abs/2611.09376) - *Jusheng Zhang et al. (2026), arXiv preprint.* An LLM repairs a robot foundation policy's instruction grounding by editing a few dozen embedding rows with simulator feedback and no gradient updates.
- [WeightLoop: Weight-Space Programming with Experimental Feedback](https://arxiv.org/abs/2611.07319) - *Mengran Li et al. (2026), arXiv preprint.* Turns experimental feedback into persistent weight corrections of scientific predictors through LLM-written update programs.

**[⬆ back to top](#contents)**

### Writing Weights from Scratch

An LLM writes all the weights of a network, or installs a new capability, from a specification instead of training.

- [WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming](https://arxiv.org/abs/2611.25476) - *Bo Li et al. (2026), arXiv preprint.* A frozen LM writes executable weight programs that install new capabilities into trained vision and navigation networks, outperforming fine-tuning baselines.
- [Weight-Space Programming Doesn't Need Transformers](https://arxiv.org/abs/2611.22055) - *Hyunjong Ok and Jaeho Lee (2026), arXiv preprint.* Lets LLMs that write weights by hand also choose the architecture, and finds they need not keep the transformer.
- [Weight-Space Programming for Materials Science](https://arxiv.org/abs/2611.22013) - *Sk Md Ahnaf Akif Alvi and Raymundo Arróyave (2026), arXiv preprint.* An LLM writes the weights of a small candidate-ranking network from a task description, for materials discovery with almost no labels.
- [Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor](https://arxiv.org/abs/2611.21958) - *Timo Oksanen (2026), arXiv preprint.* LLMs write and adapt the weights of a 253-parameter steering network that is deployed on a real tractor, with no optimizer.
- [Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets](https://arxiv.org/abs/2611.19292) - *Eduardo C. Garrido-Merchán (2026), arXiv preprint.* Has an LLM write every weight of a feed-forward network from a small dataset shown in full, so the LLM must do the statistical inference itself.
- [Interpretable weight-space programming builds transparent transformers and brain encoding models](https://arxiv.org/abs/2611.18114) - *Yash Mehta et al. (2026), arXiv preprint.* An LLM agent programs the weights of transparent transformers and brain-encoding models so their computations stay human-readable.
- [Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games](https://arxiv.org/abs/2611.16981) - *Jens Lehmann (2026), arXiv preprint.* LLM writers compile known game rules directly into the weights of compact recurrent agents that generalize to unseen levels.
- [Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models](https://arxiv.org/abs/2611.12954) - *Shogo Sato et al. (2026), arXiv preprint.* Has an LLM generate both the architecture and the weights of networks that solve PDEs directly from the governing physical laws (Physics2Weight).
- [Weight-Space Programming for Medical Imaging: Do We Still Need Training Data?](https://arxiv.org/abs/2611.12066) - *Maximilian Lindholz et al. (2026), arXiv preprint.* Has LLMs write the weights of medical image classifiers from medical knowledge alone, asking whether training data is needed at all.
- [Weight-Space Programming of Policies and Their Verification via Model Checking](https://arxiv.org/abs/2611.11604) - *Dennis Gross (2026), arXiv preprint.* Combines LLM-written policy weights with probabilistic model checking so that a written policy can be verified against a formal requirement.
- [Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer](https://arxiv.org/abs/2611.11537) - *Debarshi Kundu et al. (2026), arXiv preprint.* Extends weight writing to quantum computing: an LLM sets variational quantum circuit angles directly, with no optimizer.
- [Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application](https://arxiv.org/abs/2611.09559) - *Renan Butkeraites (2026), arXiv preprint.* Has an LLM write small scoring networks for column generation and MILP branching in exact optimization solvers.
- [Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games](https://arxiv.org/abs/2611.09271) - *Eduardo C. Garrido-Merchán (2026), arXiv preprint.* Tests how far zero-shot hand-writing of network weights goes across games of increasing difficulty, from Nim to a chess endgame.
- [NeuronGen: Neural Network Parameter Generation via Large Language Models](https://arxiv.org/abs/2505.12470) - *Jiaqi Wang et al. (2025), arXiv preprint.* Has an LLM directly emit the parameters of small networks from task, data, and architecture descriptions, an early instance of LLM-written weights.

**[⬆ back to top](#contents)**

### Self-Editing Models

Models that produce updates to their own weights.

- [Language Models Can Rewrite Their Own Weights](https://arxiv.org/abs/2611.21885) - *Jiajun Fan et al. (2026), arXiv preprint.* A language model improves itself by reasoning about and rewriting its own weights, with no gradients or training run.
- [Search over Self-Edit Strategies for LLM Adaptation](https://arxiv.org/abs/2601.14532) - *Alistair Cheong et al. (2026), arXiv preprint.* Lets an LLM choose its own self-edit strategy and hyperparameters, deciding from task feedback how its weights should be updated.
- [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) - *Adam Zweiger et al. (2025), NeurIPS 2025.* An LLM generates its own self-edits (fine-tuning data and update directives) that become persistent weight updates, trained with RL (SEAL).

**[⬆ back to top](#contents)**

### Replications, Critiques and Alternatives

Independent replications, tests of what the reading and writing really rely on, and non-LLM alternatives to the same edits.

- [Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers](https://arxiv.org/abs/2611.21449) - *Roksana Goworek et al. (2026), arXiv preprint.* Independent replication of LLM weight-space programming; finds that written networks behave like compiled programs and that weight reading relies mostly on the input layer.
- [Just sort it! A note on the LP behind rank-one anti-loop edits](https://arxiv.org/abs/2611.21432) - *Matteo Fischetti (2026), arXiv preprint.* Shows that the sparse linear program behind the agent's rank-one anti-loop edit can be replaced by a simple sort, simplifying a celebrated WSP fix.
- [Same Fix, Different Weights: Replicating Weight-Space Programming with Claude](https://arxiv.org/abs/2611.20953) - *Subham Kundu (2026), arXiv preprint.* Pre-registered replication of weight reading, repair, and writing with a different frontier model, with untrained-network and permutation controls.
- [Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210) - *Hadi Salloum and Ammar Ali (2026), arXiv preprint.* Replaces an LLM agent's weight repair with a sparse discrete optimization over the model's own bits, a solver-based contrast to agent-driven editing.
- [Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"](https://arxiv.org/abs/2611.08070) - *Nazmus Sakib Ahmed (2026), arXiv preprint.* Probes whether an LLM reading raw CNN weights is reasoning about the weights or relying on local arithmetic plus memorized dataset priors.
- [Computation, not weight access: large language models as auditors of clinical prediction networks](https://arxiv.org/abs/2611.07847) - *Zhiyu Liu and Xinyu Yang (2026), arXiv preprint.* Separates an LLM reading weights in its prompt from an LLM running code on them, and shows that reliable auditing of clinical networks comes from computation, not weight access.

**[⬆ back to top](#contents)**

### Security

Using weight-space programming to implant backdoors, and the risks this creates.

- [Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models](https://arxiv.org/abs/2611.27920) - *Xuyang Liu et al. (2026), arXiv preprint.* Shows that an LLM can turn a natural-language backdoor specification into persistent rank-one or single-neuron weight edits on another LM, a security risk of weight-space programming.
- [TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming](https://arxiv.org/abs/2611.27425) - *Ahaan Dabholkar et al. (2026), arXiv preprint.* LLM agents inspect a VLM's weights, edit them, and co-design a visual trigger to implant a backdoor in one shot with no training.
- [Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming](https://arxiv.org/abs/2611.17395) - *Zhaojia Wang et al. (2026), arXiv preprint.* Security study of several LLMs acting as weight editors that inject backdoors into MLPs, ResNets, and a small LM with few parameter changes.

**[⬆ back to top](#contents)**

## Foundations and Related Areas

Older lines of work that treat weights as objects to compute, compose, learn from, or read, and that weight-space programming builds on.

### Model and Knowledge Editing

Methods that change specific facts or behaviours by computing or learning a targeted weight update.

- [MuEdit: An efficient multi-task editing method towards inter-domain knowledge conflicts](https://arxiv.org/abs/2611.14910) - *Songshi Liang et al. (2026), NeurIPS 2026.* Explains multi-domain edit collapse as a shrinking shared null space and expands it with conflict-aware ordering and low-rank updates (MuEdit).
- [Capacity Allocation at the Source: Sparse Target Optimization for LLM Knowledge Editing](https://arxiv.org/abs/2611.12995) - *Dongyao Chen et al. (2026), NeurIPS 2026.* Traces cross-edit interference in batched editing to overlapping target vectors and reduces it with sparse targets.
- [AnyEdit++: Adaptive Long-Form Knowledge Editing via Bayesian Surprise](https://arxiv.org/abs/2606.01053) - *Bowen Tian et al. (2026), ICML 2026.* Long-form knowledge editing that segments targets by surprisal and uses orthogonal anchor keys to limit interference between weight updates (AnyEdit++).
- [From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing](https://arxiv.org/abs/2605.00358) - *Wei Liu et al. (2026), ICML 2026.* Revisits how MEMIT spreads residual targets over layers and computes per-layer targets by forward replay instead.
- [CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing](https://arxiv.org/abs/2602.15823) - *Zarif Ikram et al. (2026), ICML 2026.* Projects edits onto low-curvature directions of a capability-preserving loss, unifying null-space editors as a second-order method (CrispEdit).
- [MoEEdit: Efficient and Routing-Stable Knowledge Editing for Mixture-of-Experts LLMs](https://arxiv.org/abs/2602.10965) - *Yupu Gu et al. (2026), arXiv preprint.* A parameter-modifying editor for mixture-of-experts LLMs that keeps router inputs unchanged, so edits do not disturb routing (MoEEdit).
- [Steer2Edit: From Activation Steering to Component-Level Editing](https://arxiv.org/abs/2602.09870) - *Chung-En Sun et al. (2026), NeurIPS 2026.* Converts activation-steering vectors into rank-one weight edits on selected heads and neurons, bridging steering and weight editing (Steer2Edit).
- [Multiplicative Orthogonal Sequential Editing for Language Models](https://arxiv.org/abs/2601.07873) - *Hao-Xiang Xu et al. (2026), AAAI 2026.* Replaces additive weight deltas with multiplicative orthogonal updates that preserve the norm and conditioning of edited matrices.
- [Massive Editing for Large Language Models Based on Dynamic Weight Generation](https://arxiv.org/abs/2512.14395) - *Wentao Wan et al. (2025), ICLR 2026.* Performs large-scale knowledge editing by having a diffusion model generate the weights of an added neuron for each query (MeG).
- [Constructing Efficient Fact-Storing MLPs for Transformers](https://arxiv.org/abs/2512.00207) - *Owen Dugan et al. (2025), arXiv preprint.* Constructs fact-storing MLP weights explicitly rather than training them, analysing how many facts a given weight budget can hold.
- [Transmuting prompts into weights](https://arxiv.org/abs/2510.08734) - *Hanna Mazzawi et al. (2025), arXiv preprint.* Gives a theory of the implicit weight update a prompt induces and condenses it into token-independent weight edits.
- [ACE: Attribution-Controlled Knowledge Editing for Multi-hop Factual Recall](https://arxiv.org/abs/2510.07896) - *Jiayu Yang et al. (2025), ICLR 2026.* Locates the neuron pathways used for implicit multi-hop recall and edits them, fixing a known failure of single-site weight edits (ACE).
- [Energy-Regularized Sequential Model Editing on Hyperspheres](https://arxiv.org/abs/2510.01172) - *Qingyuan Liu et al. (2025), ICLR 2026.* Links sequential-edit collapse to the hyperspherical energy of neuron weights and constrains edits to keep that geometry stable (SPHERE).
- [Fine-tuning Done Right in Model Editing](https://arxiv.org/abs/2509.22072) - *Wanli Yang et al. (2025), ICLR 2026.* Shows that localized fine-tuning with a breadth-first, mini-batch schedule rivals locate-then-edit methods, resetting the baselines for weight editing.
- [PropMEND: Hypernetworks for Knowledge Propagation in LLMs](https://arxiv.org/abs/2506.08920) - *Zeyu Leo Liu et al. (2025), arXiv preprint.* Meta-trains a MEND-style hypernetwork so that weight edits propagate to multi-hop consequences of the edited fact (PropMEND).
- [MEMOIR: Lifelong Model Editing with Minimal Overwrite and Informed Retention for LLMs](https://arxiv.org/abs/2506.07899) - *Ke Wang et al. (2025), NeurIPS 2025.* Lifelong editing in a residual memory module where each edit touches a sparse, sample-specific mask of parameters (MEMOIR).
- [Efficient Knowledge Editing via Minimal Precomputation](https://arxiv.org/abs/2506.04226) - *Akshat Gupta et al. (2025), ACL 2025.* Shows that most of the expensive covariance precomputation in ROME, MEMIT, and EMMET is unnecessary, and gives its theoretical minimum.
- [UltraEdit: Training-, Subject-, and Memory-Free Lifelong Editing in Language Models](https://arxiv.org/abs/2505.14679) - *Xiaojie Gu et al. (2025), TMLR 2026.* A training-free, closed-form lifelong editor that uses normalization statistics to scale to millions of edits (UltraEdit).
- [AnyEdit: Edit Any Knowledge Encoded in Language Models](https://arxiv.org/abs/2502.05628) - *Houcheng Jiang et al. (2025), ICML 2025.* Extends locate-then-edit to long-form, multi-token knowledge by editing weights autoregressively chunk by chunk (AnyEdit).
- [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://arxiv.org/abs/2410.02355) - *Junfeng Fang et al. (2024), ICLR 2025.* Projects each locate-then-edit weight update onto the null space of preserved knowledge, which greatly reduces damage from sequential edits (AlphaEdit). [[Code](https://github.com/jianghoucheng/AlphaEdit)]
- [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768) - *Peng Wang et al. (2024), NeurIPS 2024.* Routes lifelong edits into a side copy of an FFN weight matrix, sharded across subspaces and merged, to balance reliability and locality (WISE). [[Code](https://github.com/zjunlp/EasyEdit)]
- [Locating and Editing Factual Associations in Mamba](https://arxiv.org/abs/2404.03646) - *Arnab Sen Sharma et al. (2024), COLM 2024.* Shows that ROME-style rank-one weight edits transfer to the Mamba state-space architecture.
- [A Unified Framework for Model Editing](https://arxiv.org/abs/2403.14236) - *Akshat Gupta et al. (2024), Findings of EMNLP 2024.* Unifies ROME and MEMIT as one preservation-memorization objective and derives EMMET, a closed-form batched equality-constrained edit.
- [Massive Editing for Large Language Models via Meta Learning](https://arxiv.org/abs/2311.04661) - *Chenmien Tan et al. (2023), ICLR 2024.* Scales hypernetwork-based editing to thousands of facts by aggregating parameter shifts with a least-squares solve (MALMEN). [[Code](https://github.com/ChenmienTan/malmen)]
- [Unified Concept Editing in Diffusion Models](https://arxiv.org/abs/2308.14761) - *Rohit Gandikota et al. (2023), WACV 2024.* Gives a single closed-form cross-attention weight update that erases, debiases, or moderates many concepts in a diffusion model at once (UCE).
- [PMET: Precise Model Editing in a Transformer](https://arxiv.org/abs/2308.08742) - *Xiaopeng Li et al. (2023), AAAI 2024.* Refines locate-then-edit by optimizing attention and FFN hidden states jointly but writing the update only into FFN weights (PMET). [[Code](https://github.com/xpq-tech/PMET)]
- [ReFACT: Updating Text-to-Image Models by Editing the Text Encoder](https://arxiv.org/abs/2306.00738) - *Dana Arad et al. (2023), NAACL 2024.* Edits factual knowledge in text-to-image models by a rank-one style update to the text encoder's weights (ReFACT).
- [Editing Common Sense in Transformers](https://arxiv.org/abs/2305.14956) - *Anshita Gupta et al. (2023), EMNLP 2023.* Adapts MEMIT-style MLP weight edits to commonsense judgments rather than encyclopedic facts.
- [Editing Implicit Assumptions in Text-to-Image Diffusion Models](https://arxiv.org/abs/2303.08084) - *Hadas Orgad et al. (2023), ICCV 2023.* Edits implicit assumptions of text-to-image diffusion models with a closed-form update to cross-attention projection weights (TIME).
- [Transformer-Patcher: One Mistake worth One Neuron](https://arxiv.org/abs/2301.09785) - *Zeyu Huang et al. (2023), ICLR 2023.* Fixes each mistake by writing one new neuron into the last FFN layer, an edit that adds weights rather than changing existing ones. [[Code](https://github.com/ZeroYuHuang/Transformer-Patcher)]
- [Mass-Editing Memory in a Transformer](https://arxiv.org/abs/2210.07229) - *Kevin Meng et al. (2022), ICLR 2023.* Extends ROME to thousands of simultaneous edits by spreading a least-squares weight update across several MLP layers (MEMIT). [[Code](https://github.com/kmeng01/memit)]
- [Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262) - *Kevin Meng et al. (2022), NeurIPS 2022.* Locates factual recall in mid-layer MLPs and rewrites a single fact with a closed-form rank-one weight update (ROME), the template for most later locate-then-edit methods. [[Code](https://github.com/kmeng01/rome)]
- [Editing a classifier by rewriting its prediction rules](https://arxiv.org/abs/2112.01008) - *Shibani Santurkar et al. (2021), NeurIPS 2021.* Edits an image classifier's prediction rules by rewriting a layer's weights as an associative memory, using a single exemplar.
- [Fast Model Editing at Scale](https://arxiv.org/abs/2110.11309) - *Eric Mitchell et al. (2021), ICLR 2022.* Trains small hypernetworks that map a fine-tuning gradient to a low-rank weight edit, making single-fact edits fast on large models (MEND). [[Code](https://github.com/eric-mitchell/mend)]
- [Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696) - *Damai Dai et al. (2021), ACL 2022.* Attributes facts to individual FFN neurons and shows that directly modifying those neurons' weights updates or erases the fact. [[Code](https://github.com/Hunter-DDM/knowledge-neurons)]
- [Editing Factual Knowledge in Language Models](https://arxiv.org/abs/2104.08164) - *Nicola De Cao et al. (2021), EMNLP 2021.* Learns a hypernetwork that predicts a constrained weight update to change one fact while preserving the rest of the model (KnowledgeEditor). [[Code](https://github.com/nicola-decao/KnowledgeEditor)]
- [Rewriting a Deep Generative Model](https://arxiv.org/abs/2007.15646) - *David Bau et al. (2020), ECCV 2020.* Treats a GAN layer as a linear associative memory and rewrites a generative rule with a constrained rank-one weight update, a precursor of ROME. [[Code](https://github.com/davidbau/rewriting)]
- [Editable Neural Networks](https://arxiv.org/abs/2004.00345) - *Anton Sinitsin et al. (2020), ICLR 2020.* Early formulation of model editing: meta-trains a network so that targeted errors can later be fixed with a few gradient steps without breaking other behaviour. [[Code](https://github.com/xtinkt/editable)]

**[⬆ back to top](#contents)**

### Analyses of Weight Edits

Work on what weight edits look like and how they fail, including rank-one structure, locality, side effects, and collapse under many edits.

- [On the Geometric Bottlenecks of Cross-Lingual Knowledge Editing](https://arxiv.org/abs/2611.10646) - *Aastha A K Verma et al. (2026), NeurIPS 2026.* Decomposes in closed form why ROME, MEMIT, and AlphaEdit edits fail to carry across languages, pointing to representational anisotropy.
- [Selective Knowledge Edit Reversal via Gated Singular Vector Shrinkage](https://arxiv.org/abs/2609.02091) - *Weifeng Jiang et al. (2026), Findings of EMNLP 2026.* Finds individual edits concentrated in a few singular components of the update, so they can be removed one at a time.
- [Exposing the Illusion of Erasure in Knowledge Editing for LLMs](https://arxiv.org/abs/2606.23276) - *Advik Raj Basani and Anshuman Chhabra (2026), NeurIPS 2026.* Shows that low-rank edits hide rather than erase old knowledge, which adversarial elicitation can recover.
- [Knowledge Editing for Masked Diffusion Language Models](https://arxiv.org/abs/2606.03924) - *Haewon Park and Yohan Jo (2026), EMNLP 2026.* Finds that locate-then-edit transfers to masked diffusion language models at the same MLP sites, but multi-token edits degrade sharply.
- [Revisiting Parameter-Based Knowledge Editing in Large Language Models: Theoretical Limits and Empirical Evidence](https://arxiv.org/abs/2606.00570) - *Wanying Ren et al. (2026), ICML 2026.* Argues from dimensional collapse that localized weight edits cause global interference, with evidence that retrieval beats parameter editors in realistic tests.
- [One Mask to Rule Them All: On Hidden Facts after Editing and How to Find Them](https://arxiv.org/abs/2605.28839) - *Ali Holmov et al. (2026), Findings of ACL 2026.* Shows that one binary mask over the edited weights reverses most ROME and MEMIT edits: the edits suppress old facts rather than overwrite them.
- [The Labyrinth and the Thread: Rethinking Regularizations in Sequential Knowledge Editing for Large Language Models](https://arxiv.org/abs/2605.26670) - *Zheng Wang et al. (2026), ICML 2026.* Proves that sequential and one-shot editing coincide when accumulated constraints are kept, making many null-space regularizers unnecessary.
- [More Edits, More Stable: Understanding the Lifelong Normalization in Sequential Model Editing](https://arxiv.org/abs/2605.11836) - *Xin Ma et al. (2026), ICML 2026.* Explains theoretically why normalization-based lifelong editors stay stable: their weight updates become nearly orthogonal and stay norm-bounded.
- [Reverse-Engineering Model Editing on Language Models](https://arxiv.org/abs/2602.10134) - *Zhiyu Sun et al. (2026), ICML 2026.* Shows that the row space of a rank-one or low-rank edit fingerprints the edited subject, so edits can be reverse-engineered from weights alone.
- [Norm Anchors Make Model Edits Last](https://arxiv.org/abs/2602.02543) - *Mingda Liu et al. (2026), arXiv preprint.* Models sequential locate-then-edit failure as a positive norm-feedback loop and shows that anchoring value norms greatly extends the editing horizon.
- [Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse](https://arxiv.org/abs/2601.11042) - *Chi Zhang et al. (2026), ACL 2026.* Ties sequential-editing collapse to disruption of the dominant singular directions of pretrained weights, and protects that subspace (REVIVE).
- [Can Fine-Tuning Erase Your Edits? On the Fragile Coexistence of Knowledge Editing and Adaptation](https://arxiv.org/abs/2511.05852) - *Yinjie Cheng et al. (2025), KDD 2026.* Large-scale study showing that AlphaEdit, MEMIT, and other weight edits decay under later fine-tuning.
- [Believe It or Not: How Deeply do LLMs Believe Implanted Facts?](https://arxiv.org/abs/2510.17941) - *Stewart Slocum et al. (2025), arXiv preprint.* Measures how deeply implanted facts are believed, finding that mechanistic weight editors implant shallower beliefs than synthetic-document fine-tuning.
- [Is Model Editing Built on Sand? Revealing Its Illusory Success and Fragile Foundation](https://arxiv.org/abs/2510.00625) - *Wei Liu et al. (2025), arXiv preprint.* Shows that weight editors often succeed through shortcuts that negative-example tests expose, questioning reported success rates.
- [Bilinear representation mitigates reversal curse and enables consistent model editing](https://arxiv.org/abs/2509.21993) - *Dong-Kyum Kim et al. (2025), ICLR 2026.* Shows that bilinear relational structure is what lets a weight edit carry over to reverse and implied facts.
- [The Mirage of Model Editing: Revisiting Evaluation in the Wild](https://arxiv.org/abs/2502.11177) - *Wanli Yang et al. (2025), ACL 2025.* Re-evaluates popular editors in realistic generation settings and finds their reported success largely disappears.
- [Rebuilding ROME : Resolving Model Collapse during Sequential Model Editing](https://arxiv.org/abs/2403.07175) - *Akshat Gupta et al. (2024), EMNLP 2024.* Traces sudden ROME collapse to an implementation asymmetry in the key vectors and fixes it (r-ROME), showing that collapse comes from the edit's form.
- [The Butterfly Effect of Model Editing: Few Edits Can Trigger Large Language Models Collapse](https://arxiv.org/abs/2402.09656) - *Wanli Yang et al. (2024), Findings of ACL 2024.* Shows that even a single locate-then-edit weight update can collapse an LLM, and proposes perplexity as a cheap collapse signal.
- [Model Editing at Scale leads to Gradual and Catastrophic Forgetting](https://arxiv.org/abs/2401.07453) - *Akshat Gupta et al. (2024), Findings of ACL 2024.* Shows that sequential ROME and MEMIT edits first erode and then abruptly collapse model ability.
- [Model Editing Harms General Abilities of Large Language Models: Regularization to the Rescue](https://arxiv.org/abs/2401.04700) - *Jia-Chen Gu et al. (2024), EMNLP 2024.* Measures how weight editing damages general abilities, traces it to overfitting of edited weights, and regularizes the edit to prevent it.
- [Edit at your own risk: evaluating the robustness of edited models to distribution shifts](https://arxiv.org/abs/2303.00046) - *Davis Brown et al. (2023), arXiv preprint.* Studies how weight-edited models behave under distribution shift and finds that edits can quietly hurt robustness.
- [Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models](https://arxiv.org/abs/2301.04213) - *Peter Hase et al. (2023), NeurIPS 2023.* Finds that where causal tracing localizes a fact barely predicts which layer is best to edit, questioning localization as a guide to weight edits. [[Code](https://github.com/google/belief-localization)]

**[⬆ back to top](#contents)**

### Task Vectors, Task Arithmetic and Model Merging

Treating fine-tuning deltas as vectors to add, negate, and combine, and merging trained models directly in weight space.

- [Platonic Task Arithmetic](https://arxiv.org/abs/2610.00929) - *Junghwan Park and Woojin Cho (2026), NeurIPS 2026.* Proposes architecture-agnostic task descriptors so task arithmetic works across different models.
- [When Do Task Vectors Interfere? Mapping the Validity Boundaries of Weight-Space Composition](https://arxiv.org/abs/2608.09490) - *Chencheng Zhu et al. (2026), arXiv preprint.* Pre-registered study showing that task-vector interference is real but depends on the input and prompt.
- [Scaling Linear Mode Connectivity and Merging to Billion Parameter Pretrained Transformers](https://arxiv.org/abs/2606.23607) - *Tianyi Li and Zhiqiang Shen (2026), arXiv preprint.* Uses function-preserving weight transformations to reach linear mode connectivity and merging for billion-parameter transformers.
- [RogueMerge: Robust and Unified Attacks against LLM Model Merging](https://arxiv.org/abs/2606.03344) - *Jinghuai Zhang et al. (2026), IEEE S&P 2027.* Shows that malicious task vectors can attack merged LLMs, a supply-chain risk of weight-space composition.
- [Understanding and Enforcing Weight Disentanglement in Task Arithmetic](https://arxiv.org/abs/2604.17078) - *Shangge Liu et al. (2026), CVPR 2026.* Explains weight disentanglement and task-vector orthogonality through task-feature specialization, and enforces it.
- [Dataless Weight Disentanglement in Task Arithmetic via Kronecker-Factored Approximate Curvature](https://arxiv.org/abs/2602.17385) - *Angelo Porrello et al. (2026), ICLR 2026.* Disentangles task vectors with a K-FAC curvature regularizer that needs no task data.
- [Transporting Task Vectors across Different Architectures without Training](https://arxiv.org/abs/2602.12952) - *Filippo Rinaldi et al. (2026), ICML 2026.* Transfers task updates in closed form across models of different width and architecture (Theseus).
- [The Appeal and Reality of Recycling LoRAs with Adaptive Merging](https://arxiv.org/abs/2602.12323) - *Haokun Liu et al. (2026), arXiv preprint.* Tests adaptive LoRA merging on about a thousand real Hugging Face adapters and finds the practical gains much smaller than claimed.
- [Symmetry-Aware Graph Metanetwork Autoencoders: Model Merging through Parameter Canonicalization](https://arxiv.org/abs/2511.12601) - *Odysseas Boufalis et al. (2025), arXiv preprint.* Canonicalizes permutation and scaling symmetries with a metanetwork autoencoder so that independently trained models can be merged.
- [Model Merging with Functional Dual Anchors](https://arxiv.org/abs/2510.21223) - *Kexuan Shi et al. (2025), arXiv preprint.* Constructs synthetic inputs whose gradients match task vectors, connecting parameter-space and input-space merging.
- [Gradient-Sign Masking for Task Vector Transport Across Pre-Trained Models](https://arxiv.org/abs/2510.09658) - *Filippo Rinaldi et al. (2025), ICLR 2026.* Transports a task vector to a newer release of the base model with gradient-sign masking (GradFix).
- [Do We Really Need Permutations? Impact of Model Width on Linear Mode Connectivity](https://arxiv.org/abs/2510.08023) - *Akira Ito et al. (2025), ICLR 2026.* Revisits whether permutation alignment is needed for linear mode connectivity, highlighting the role of width.
- [How does the optimizer implicitly bias the model merging loss landscape?](https://arxiv.org/abs/2510.04686) - *Chenxiang Zhang et al. (2025), ICLR 2026.* Shows that the effective noise scale of the optimizer shapes how mergeable the resulting weights are.
- [Model Merging Scaling Laws in Large Language Models](https://arxiv.org/abs/2509.24244) - *Yuanyi Wang et al. (2025), ICML 2026.* Finds power-law scaling of merging gains with model size and number of merged experts.
- [Null-Space Filtering for Data-Free Continual Model Merging: Preserving Stability, Promoting Plasticity](https://arxiv.org/abs/2509.21413) - *Zihuan Qiu et al. (2025), ICLR 2026.* Shows that task vectors align with representation subspaces and uses null-space filtering for data-free continual merging.
- [Generalized Linear Mode Connectivity for Transformers](https://arxiv.org/abs/2506.22712) - *Alexander Theus et al. (2025), NeurIPS 2025.* Unifies permutation, orthogonal, and invertible symmetries to obtain linear mode connectivity and merging for transformers.
- [Model Merging in Pre-training of Large Language Models](https://arxiv.org/abs/2505.12082) - *Yunshui Li et al. (2025), arXiv preprint.* Merges checkpoints during LLM pre-training and shows that the merges predict the gains of learning-rate annealing.
- [No Task Left Behind: Isotropic Model Merging with Common and Task-Specific Subspaces](https://arxiv.org/abs/2502.04959) - *Daniel Marczak et al. (2025), ICML 2025.* Merges by flattening the singular-value spectrum of the summed task matrix, with separate common and task-specific subspaces (Iso-C, Iso-CTS).
- [Task Singular Vectors: Reducing Task Interference in Model Merging](https://arxiv.org/abs/2412.00081) - *Antonio Andrea Gargiulo et al. (2024), CVPR 2025.* Analyses task vectors layer by layer through their singular vectors, which enables compression and interference-aware merging (TSV-Merge).
- [Model merging with SVD to tie the Knots](https://arxiv.org/abs/2410.19735) - *George Stoica et al. (2024), ICLR 2025.* Aligns LoRA updates in a shared SVD basis before merging so that existing merging methods work on LoRA models (KnOTS).
- [What Matters for Model Merging at Scale?](https://arxiv.org/abs/2410.03617) - *Prateek Yadav et al. (2024), arXiv preprint.* Systematic study of merging LLMs up to 64B parameters, showing how base-model quality and size change what works.
- [Localizing Task Information for Improved Model Merging and Compression](https://arxiv.org/abs/2405.07813) - *Ke Wang et al. (2024), ICML 2024.* Shows that task information survives merging and can be localized in weights with binary masks, enabling near-lossless recovery (TALL masks).
- [Evolutionary Optimization of Model Merging Recipes](https://arxiv.org/abs/2403.13187) - *Takuya Akiba et al. (2024), arXiv preprint.* Uses evolutionary search over parameter-space and layer-routing merge recipes to build new models automatically.
- [Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch](https://arxiv.org/abs/2311.03099) - *Le Yu et al. (2023), ICML 2024.* Shows that most fine-tuning delta parameters can be randomly dropped and the rest rescaled, which makes merging LLM deltas easy (DARE).
- [Transformer Fusion with Optimal Transport](https://arxiv.org/abs/2310.05719) - *Moritz Imfeld et al. (2023), ICLR 2024.* Fuses transformers with soft optimal-transport alignment of their components, including models of different widths.
- [Chat Vector: A Simple Approach to Equip LLMs with Instruction Following and Model Alignment in New Languages](https://arxiv.org/abs/2310.04799) - *Shih-Cheng Huang et al. (2023), ACL 2024.* Adds the weight difference between a chat model and its base to a model continually pre-trained in a new language, transplanting instruction following (Chat Vector).
- [AdaMerging: Adaptive Model Merging for Multi-Task Learning](https://arxiv.org/abs/2310.02575) - *Enneng Yang et al. (2023), ICLR 2024.* Learns task-wise and layer-wise merging coefficients without labels by minimizing prediction entropy (AdaMerging).
- [LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition](https://arxiv.org/abs/2307.13269) - *Chengsong Huang et al. (2023), COLM 2024.* Composes many LoRA modules for a new task with a few examples and gradient-free search over the combination weights (LoraHub).
- [TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708) - *Prateek Yadav et al. (2023), NeurIPS 2023.* Resolves interference between task vectors by trimming small deltas and electing a sign per parameter before merging (TIES-Merging). [[Code](https://github.com/prateeky2806/ties-merging)]
- [Task Arithmetic in the Tangent Space: Improved Editing of Pre-Trained Models](https://arxiv.org/abs/2305.12827) - *Guillermo Ortiz-Jimenez et al. (2023), NeurIPS 2023.* Explains task arithmetic through weight disentanglement and shows that fine-tuning in the tangent space makes task vectors compose better.
- [ZipIt! Merging Models from Different Tasks without Training](https://arxiv.org/abs/2305.03053) - *George Stoica et al. (2023), ICLR 2024.* Merges differently initialized models trained on different tasks by zipping redundant features within and across models (ZipIt!).
- [Dataless Knowledge Fusion by Merging Weights of Language Models](https://arxiv.org/abs/2212.09849) - *Xisen Jin et al. (2022), ICLR 2023.* Merges linear layers in closed form by solving a regression on stored activation statistics, with no training data (RegMean).
- [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089) - *Gabriel Ilharco et al. (2022), ICLR 2023.* Introduces task vectors, the weight difference from fine-tuning, and shows that adding, negating, and combining them edits model behaviour. [[Code](https://github.com/mlfoundations/task_vectors)]
- [Git Re-Basin: Merging Models modulo Permutation Symmetries](https://arxiv.org/abs/2209.04836) - *Samuel K. Ainsworth et al. (2022), ICLR 2023.* Permutes one network's neurons to match another's so independently trained models land in one basin and can be merged (Git Re-Basin). [[Code](https://github.com/samuela/git-re-basin)]
- [Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time](https://arxiv.org/abs/2203.05482) - *Mitchell Wortsman et al. (2022), ICML 2022.* Shows that averaging the weights of several fine-tuned models beats selecting the best one, establishing weight-space ensembling (model soups). [[Code](https://github.com/mlfoundations/model-soups)]
- [Merging Models with Fisher-Weighted Averaging](https://arxiv.org/abs/2111.09832) - *Michael Matena and Colin Raffel (2021), NeurIPS 2022.* Frames merging as combining posteriors and weights each parameter by its Fisher information when averaging models.

**[⬆ back to top](#contents)**

### Weight-Space Learning

Networks that take other networks' weights as input, including equivariant metanetworks, neural functionals, and weight embeddings.

- [Adapters as Data: The Latent Space of LoRAs](https://arxiv.org/abs/2611.07775) - *Moritz Grävinghoff et al. (2026), NeurIPS 2026 Workshop.* Learns a latent space over populations of LoRA adapters that supports sampling, editing, and inverting adapters.
- [Interfaces and Modules: A Scalable Representation for Weight-Space Learning across Architectures](https://arxiv.org/abs/2610.21995) - *Michał Kozyra and Michael Bronstein (2026), arXiv preprint.* Compiles arbitrary PyTorch models into typed symmetry graphs, giving one scalable weight encoder across architectures.
- [Graph Metanetworks for Transformer Based Language Models](https://arxiv.org/abs/2610.18471) - *Yonathan Wolanowsky et al. (2026), arXiv preprint.* A graph metanetwork that respects the full symmetry group of transformer language-model weights, including attention-head symmetries.
- [Who Built This Model? Tracing LLM Lineage via Spectral Fingerprints in Weight Space](https://arxiv.org/abs/2608.07786) - *Yiwei Chen et al. (2026), COLM 2026.* Determines LLM lineage (independent, same series, or shared base) from spectral fingerprints of the weights alone.
- [WeightCLIP: Aligning Datasets and Models for Weight Space Learning](https://arxiv.org/abs/2607.03551) - *Aron Asefaw et al. (2026), ICML 2026.* Learns a contrastive space shared by datasets and model weights, enabling retrieval of models for a dataset and the reverse.
- [WARP: Weight-Space Analysis for Recovering Training Data Portfolios](https://arxiv.org/abs/2607.01686) - *Tzu-Heng Huang et al. (2026), ICML 2026 Workshop.* Infers the mixture of fine-tuning data a released model was trained on from its weights.
- [What Linear Probes Miss: Multi-View Probing for Weight-Space Learning](https://arxiv.org/abs/2605.23410) - *Eunwoo Heo et al. (2026), ICML 2026.* Extends probe-based weight-space learning with multi-view higher-order probing for analysing heterogeneous checkpoint collections.
- [Quasi-Equivariant Metanetworks](https://arxiv.org/abs/2604.23720) - *Viet-Hoang Tran et al. (2026), ICLR 2026.* Relaxes strict equivariance in metanetworks toward the true functional symmetries of parameters.
- [W2T: LoRA Weights Already Know What They Can Do](https://arxiv.org/abs/2603.15990) - *Xiaolong Han et al. (2026), arXiv preprint.* Puts LoRA updates in a canonical form and predicts an adapter's behaviour and performance directly from its weights.
- [Weight space Detection of Backdoors in LoRA Adapters](https://arxiv.org/abs/2602.15195) - *David Puertolas Merenciano et al. (2026), arXiv preprint.* Screens LoRA adapters for backdoors from spectral features of their weights, with no data and no knowledge of the trigger.
- [On the Expressive Power of Permutation-Equivariant Weight-Space Networks](https://arxiv.org/abs/2602.01083) - *Adir Dayan et al. (2026), ICML 2026.* A systematic theory of what permutation-equivariant weight-space networks can and cannot express.
- [Metanetworks as Regulatory Operators: Learning to Edit for Requirement Compliance](https://arxiv.org/abs/2512.15469) - *Ioannis Kalogeropoulos et al. (2025), arXiv preprint.* Trains metanetworks that act as operators editing other networks' weights to meet requirements such as fairness or sparsity.
- [Symmetry-Aware Fully-Amortized Optimization with Scale Equivariant Graph Metanetworks](https://arxiv.org/abs/2510.08300) - *Bart Kuipers et al. (2025), arXiv preprint.* Uses symmetry-aware metanetworks to amortize optimization, mapping a network's weights to fine-tuned weights in one shot.
- [Can this Model Also Recognize Dogs? Zero-Shot Model Search from Weights](https://arxiv.org/abs/2502.09619) - *Jonathan Kahana et al. (2025), arXiv preprint.* Searches model repositories by querying weights directly, for example for models that can recognize a given concept.
- [Learning on Model Weights using Tree Experts](https://arxiv.org/abs/2410.13569) - *Eliahu Horwitz et al. (2024), CVPR 2025.* Learns weight representations with per-model-tree experts (ProbeX), aligning weights with text to enable zero-shot model classification and retrieval.
- [Deep Linear Probe Generators for Weight Space Learning](https://arxiv.org/abs/2410.10811) - *Jonathan Kahana et al. (2024), arXiv preprint.* Learns probe inputs that are passed through a network to read its function, a strong simple baseline for weight-space tasks.
- [Learning on LoRAs: GL-Equivariant Processing of Low-Rank Weight Spaces for Large Finetuned Models](https://arxiv.org/abs/2410.04207) - *Theo Putterman et al. (2024), arXiv preprint.* Designs GL-equivariant metanetworks that take LoRA factors as input, so populations of fine-tuned models can be learned on directly.
- [Monomial Matrix Group Equivariant Neural Functional Networks](https://arxiv.org/abs/2409.11697) - *Viet-Hoang Tran et al. (2024), NeurIPS 2024.* Builds metanetworks equivariant to the full monomial-matrix symmetry group (permutations plus scaling and sign flips), with far fewer parameters.
- [Scale Equivariant Graph Metanetworks](https://arxiv.org/abs/2406.10685) - *Ioannis Kalogeropoulos et al. (2024), NeurIPS 2024.* Extends graph metanetworks to be equivariant to scaling symmetries as well as permutations (ScaleGMN). [[Code](https://github.com/jkalogero/scalegmn)]
- [Towards Scalable and Versatile Weight Space Learning](https://arxiv.org/abs/2406.09997) - *Konstantin Schürholt et al. (2024), ICML 2024.* Scales weight-space representation learning to large models by processing weights as sequences of tokens, for both analysis and generation (SANE). [[Code](https://github.com/HSG-AIML/SANE)]
- [Interpreting the Weight Space of Customized Diffusion Models](https://arxiv.org/abs/2406.09413) - *Amil Dravid et al. (2024), NeurIPS 2024.* Models the space of personalized diffusion model weights as a linear subspace that can be sampled, edited along semantic directions, and inverted (weights2weights).
- [The Empirical Impact of Neural Parameter Symmetries, or Lack Thereof](https://arxiv.org/abs/2405.20231) - *Derek Lim et al. (2024), NeurIPS 2024.* Trains networks with parameter symmetries removed to measure empirically how those symmetries affect merging, optimization, and weight-space learning.
- [Unsupervised Model Tree Heritage Recovery](https://arxiv.org/abs/2405.18432) - *Eliahu Horwitz et al. (2024), ICLR 2025.* Recovers the fine-tuning genealogy of a model population from weight statistics alone (MoTHer).
- [Graph Neural Networks for Learning Equivariant Representations of Neural Networks](https://arxiv.org/abs/2403.12143) - *Miltiadis Kofinas et al. (2024), ICLR 2024.* Encodes networks as neural graphs and processes them with equivariant GNNs and transformers that handle heterogeneous architectures. [[Code](https://github.com/mkofinas/neural-graphs)]
- [Universal Neural Functionals](https://arxiv.org/abs/2402.05232) - *Allan Zhou et al. (2024), NeurIPS 2024.* Automatically constructs permutation-equivariant layers for any weight space, including RNNs and transformers, which removes per-architecture design.
- [Improved Generalization of Weight Space Networks via Augmentations](https://arxiv.org/abs/2402.04081) - *Aviv Shamsian et al. (2024), ICML 2024.* Diagnoses overfitting in weight-space networks and fixes it with symmetry-preserving weight-space augmentations, including MixUp in weight space.
- [Graph Metanetworks for Processing Diverse Neural Architectures](https://arxiv.org/abs/2312.04501) - *Derek Lim et al. (2023), ICLR 2024.* Represents a network as a parameter graph so one graph neural network can process weights of diverse architectures (graph metanetworks).
- [Equivariant Deep Weight Space Alignment](https://arxiv.org/abs/2310.13397) - *Aviv Navon et al. (2023), ICML 2024.* Learns to align two networks' weights up to permutation with an equivariant metanetwork, replacing costly combinatorial weight matching.
- [Set-based Neural Network Encoding Without Weight Tying](https://arxiv.org/abs/2305.16625) - *Bruno Andreis et al. (2023), NeurIPS 2024.* Encodes weights of arbitrary architectures as sets, without weight tying, for property prediction across architectures.
- [Neural Functional Transformers](https://arxiv.org/abs/2305.13546) - *Allan Zhou et al. (2023), NeurIPS 2023.* Builds attention-based neural functional transformers that process weight spaces while respecting their permutation symmetry. [[Code](https://github.com/AllanYangZhou/nfn)]
- [Permutation Equivariant Neural Functionals](https://arxiv.org/abs/2302.14040) - *Allan Zhou et al. (2023), NeurIPS 2023.* Introduces neural functionals: permutation-equivariant layers that take a network's weights as input and output predictions or new weights. [[Code](https://github.com/AllanYangZhou/nfn)]
- [Deep Learning on Implicit Neural Representations of Shapes](https://arxiv.org/abs/2302.05438) - *Luca De Luigi et al. (2023), ICLR 2023.* Embeds the weights of implicit neural representations so downstream deep learning runs on weights instead of on the underlying shapes (inr2vec).
- [Equivariant Architectures for Learning in Deep Weight Spaces](https://arxiv.org/abs/2301.12780) - *Aviv Navon et al. (2023), ICML 2023.* Characterizes the layers that are equivariant to neuron permutations in MLP weight spaces and builds DWSNets, a founding metanetwork architecture. [[Code](https://github.com/AvivNavon/DWSNets)]
- [From data to functa: Your data point is a function and you can treat it like one](https://arxiv.org/abs/2201.12204) - *Emilien Dupont et al. (2022), ICML 2022.* Treats each datapoint as the weights (modulations) of a neural field and runs learning and generation on those weights (functa).
- [Hyper-Representations: Self-Supervised Representation Learning on Neural Network Weights for Model Characteristic Prediction](https://arxiv.org/abs/2110.15288) - *Konstantin Schürholt et al. (2021), NeurIPS 2021.* Self-supervised hyper-representations of model weights that predict model characteristics such as accuracy and hyperparameters. [[Code](https://github.com/HSG-AIML/NeurIPS_2021-Weight_Space_Learning)]
- [Predicting Neural Network Accuracy from Weights](https://arxiv.org/abs/2002.11448) - *Thomas Unterthiner et al. (2020), arXiv preprint.* Shows that a network's test accuracy can be predicted from its weights alone, and releases a large dataset of trained CNNs.

**[⬆ back to top](#contents)**

### Weight Generation

Hypernetworks and generative models (diffusion, flow matching, autoregressive) that output network weights, including prompt-to-weights and text-to-LoRA.

- [Internalizer: Portable Context-to-Parameter Mapping for Very Large Language Models](https://arxiv.org/abs/2610.11715) - *Peter Devine et al. (2026), arXiv preprint.* A document-to-LoRA hypernetwork that scales context-to-parameter mapping to a very large target LM.
- [HyperThink: Text-to-Parameter Hypernetworks for Efficient Reasoning](https://arxiv.org/abs/2610.03039) - *Donggyun Kim et al. (2026), COLM 2026.* Generates question-conditioned parameter updates that amortize long chain-of-thought reasoning into weights.
- [Permutation-Equivariant Flow Matching for Alignment-Free Neural Weight Generation](https://arxiv.org/abs/2609.32833) - *Arkadi Piven et al. (2026), arXiv preprint.* Flow matching with a permutation-equivariant velocity field that learns to generate weights from unaligned, independently trained networks.
- [Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models](https://arxiv.org/abs/2607.19604) - *Nischay Dhankhar et al. (2026), arXiv preprint.* Scaling laws for hypernetworks that write knowledge into LoRA weights.
- [Doc-to-LoRA: Learning to Instantly Internalize Contexts](https://arxiv.org/abs/2602.15902) - *Rujikorn Charakorn et al. (2026), arXiv preprint.* A hypernetwork writes a document's content into LoRA weights in one pass, internalizing context without fine-tuning.
- [SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass](https://arxiv.org/abs/2602.06358) - *Yewei Liu et al. (2026), arXiv preprint.* Reuses a frozen LLM as an in-context hypernetwork that maps a context directly to LoRA weights.
- [DeepWeightFlow: Re-Basined Flow Matching for Generating Neural Network Weights](https://arxiv.org/abs/2601.05052) - *Saumya Gupta et al. (2026), ICLR 2026.* Flow matching over full network weights, with re-basin alignment, that generates ResNets and ViTs.
- [Instant Personalized Large Language Model Adaptation via Hypernetwork](https://arxiv.org/abs/2510.16282) - *Zhaoxuan Tan et al. (2025), ACL 2026.* A hypernetwork maps a user profile to a personalized LoRA, with no per-user training.
- [Text2Weight: Bridging Natural Language and Neural Network Weight Spaces](https://arxiv.org/abs/2508.13633) - *Bowen Tian et al. (2025), ACM MM 2025.* Generates task-specific classifier weights from natural-language descriptions with a text-conditioned diffusion model.
- [Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights](https://arxiv.org/abs/2506.16406) - *Zhiyuan Liang et al. (2025), arXiv preprint.* Maps a handful of unlabeled task prompts directly to full LoRA weight sets with a generator, skipping per-task training.
- [Generative Modeling of Weights: Generalization or Memorization?](https://arxiv.org/abs/2506.07998) - *Boya Zeng et al. (2025), arXiv preprint.* Finds that current weight-generative models largely memorize their training checkpoints instead of generating novel weights.
- [Text-to-LoRA: Instant Transformer Adaption](https://arxiv.org/abs/2506.06105) - *Rujikorn Charakorn et al. (2025), ICML 2025.* A hypernetwork maps a natural-language task description to LoRA weights for an LLM in a single forward pass.
- [Instruction-Guided Autoregressive Neural Network Parameter Generation](https://arxiv.org/abs/2504.02012) - *Soro Bedionita et al. (2025), arXiv preprint.* An autoregressive, instruction-guided generator that produces network parameters token by token across architectures (IGPG).
- [ORAL: Prompting Your Large-Scale LoRAs via Conditional Recurrent Diffusion](https://arxiv.org/abs/2503.24354) - *Rana Muhammad Shahroz Khan et al. (2025), arXiv preprint.* Conditional recurrent diffusion that generates LoRA weights for large models from prompts (ORAL).
- [Flow to Learn: Flow Matching on Neural Network Parameters](https://arxiv.org/abs/2503.19371) - *Daniel Saragih et al. (2025), arXiv preprint.* Applies flow matching to network parameters, generating weights that act as good initializations or finished models.
- [Recurrent Diffusion for Large-Scale Parameter Generation](https://arxiv.org/abs/2501.11587) - *Kai Wang et al. (2025), arXiv preprint.* Generates parameters of large models by recurrently diffusing over tokenized weight chunks (RPG).
- [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://arxiv.org/abs/2411.05877) - *Tong Chen et al. (2024), arXiv preprint.* Maps a context to adapter weights in a single forward pass, so a frozen LM absorbs new information without fine-tuning.
- [Diffusion-Based Neural Network Weights Generation](https://arxiv.org/abs/2402.18153) - *Bedionita Soro et al. (2024), ICLR 2025.* Dataset-conditioned latent diffusion over weights that generates models for new tasks, including LLM layers (D2NWG).
- [Neural Network Diffusion](https://arxiv.org/abs/2402.13144) - *Kai Wang et al. (2024), arXiv preprint.* Shows that a latent diffusion model trained on checkpoints generates high-performing network parameters (p-diff). [[Code](https://github.com/NUS-HPC-AI-Lab/Neural-Network-Diffusion)]
- [HyperDreamBooth: HyperNetworks for Fast Personalization of Text-to-Image Models](https://arxiv.org/abs/2307.06949) - *Nataniel Ruiz et al. (2023), CVPR 2024.* A hypernetwork predicts personalization weights for a text-to-image model from a single face image (HyperDreamBooth).
- [HyperDiffusion: Generating Implicit Neural Fields with Weight-Space Diffusion](https://arxiv.org/abs/2303.17015) - *Ziya Erkoç et al. (2023), ICCV 2023.* Runs diffusion directly on the weights of neural fields to generate new 3D shapes and 4D sequences (HyperDiffusion).
- [Can We Scale Transformers to Predict Parameters of Diverse ImageNet Models?](https://arxiv.org/abs/2303.04143) - *Boris Knyazev et al. (2023), ICML 2023.* Scales graph hypernetworks with transformers to predict initial parameters for diverse ImageNet models (GHN-3). [[Code](https://github.com/SamsungSAILMontreal/ghn3)]
- [HINT: Hypernetwork Instruction Tuning for Efficient Zero- & Few-Shot Generalisation](https://arxiv.org/abs/2212.10315) - *Hamish Ivison et al. (2022), ACL 2023.* A hypernetwork turns a task instruction into parameter-efficient module weights once, so the instruction need not be reprocessed (HINT).
- [HyperTuning: Toward Adapting Large Language Models without Back-propagation](https://arxiv.org/abs/2211.12485) - *Jason Phang et al. (2022), arXiv preprint.* Uses an LLM as a hypernetwork that produces adapter parameters from few-shot examples, adapting a model without backpropagation (HyperTuning).
- [Hyper-Representations as Generative Models: Sampling Unseen Neural Network Weights](https://arxiv.org/abs/2209.14733) - *Konstantin Schürholt et al. (2022), NeurIPS 2022.* Samples new working network weights from generative hyper-representations learned on model zoos.
- [Learning to Learn with Generative Models of Neural Network Checkpoints](https://arxiv.org/abs/2209.12892) - *William Peebles et al. (2022), arXiv preprint.* Trains a generative model on checkpoints that, given a target loss or return, writes parameters reaching it in one step (G.pt).
- [Parameter Prediction for Unseen Deep Architectures](https://arxiv.org/abs/2110.13100) - *Boris Knyazev et al. (2021), NeurIPS 2021.* A graph hypernetwork that predicts parameters for unseen architectures in one forward pass (GHN-2). [[Code](https://github.com/facebookresearch/ppuda)]
- [HyperNetworks](https://arxiv.org/abs/1609.09106) - *David Ha et al. (2016), ICLR 2017.* Introduces hypernetworks, small networks that generate the weights of a larger main network.

**[⬆ back to top](#contents)**

### Weight-Based Interpretability

Reading what a network computes directly from its parameters, including parameter decomposition and circuit-level weight edits.

- [Interpreting Language Model Parameters](https://arxiv.org/abs/2610.20748) - *Lucius Bushnaq et al. (2026), arXiv preprint.* Decomposes a 67M-parameter language model's weights into rank-one subcomponents and uses them to edit behaviour.
- [Weights Read and Write Features: Scalable Parameter Decomposition Grounded in Activation Space](https://arxiv.org/abs/2609.37731) - *Tue M. Cao et al. (2026), arXiv preprint.* Grounds parameter decomposition in activation features and scales it to an 8B LLM, yielding editable weight components.
- [Sparse Weight Decomposition for Efficient Circuit Extraction](https://arxiv.org/abs/2608.03913) - *Chuanhao Yan et al. (2026), arXiv preprint.* Factorizes pretrained weights into sparse factors that serve as circuit units.
- [Individual Parameters in Weight-Sparse Transformers Appear Interpretable](https://arxiv.org/abs/2607.02964) - *Arnau Marin-Llobet and Stefan Heimersheim (2026), arXiv preprint.* Automatically describes when individual weights in weight-sparse transformers matter, and finds many of them interpretable.
- [Spectral Query-Key Product Weight Steering for Training-Free VLM Hallucination Mitigation](https://arxiv.org/abs/2606.20419) - *Karn Tiwari et al. (2026), arXiv preprint.* A data-free weight edit that suppresses dominant query-key singular modes to reduce VLM hallucination.
- [When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability](https://arxiv.org/abs/2605.15183) - *ML Nissen Gonzalez et al. (2026), arXiv preprint.* A symmetry-invariant similarity between tensor-network weights that measures functional equivalence without data.
- [Spectral Geometry of LoRA Adapters Encodes Training Objective and Predicts Harmful Compliance](https://arxiv.org/abs/2604.08844) - *Roi Paul (2026), arXiv preprint.* Shows that the spectral geometry of LoRA deltas reveals the training objective and predicts harmful compliance.
- [Disentangling MLP Neuron Weights in Vocabulary Space](https://arxiv.org/abs/2604.06005) - *Asaf Avrahamy et al. (2026), COLM 2026.* Rotates MLP neuron weights in vocabulary space to disentangle them into interpretable channels, with no data or forward pass (ROTATE).
- [From Weights to Concepts: Data-Free Interpretability of CLIP via Singular Vector Decomposition](https://arxiv.org/abs/2603.24653) - *Francesco Gentile et al. (2026), CVPR 2026.* Interprets CLIP attention heads data-free by reading their value-output singular vectors as sparse concept combinations (SITH).
- [What Does a Sparse Autoencoder Feature Do? A Weight-Based Account](https://arxiv.org/abs/2601.22447) - *Yiting Liu and Zhi-Hong Deng (2026), NeurIPS 2026.* Explains what SAE features do from model weights alone, without activation data.
- [Weight-sparse transformers have interpretable circuits](https://arxiv.org/abs/2511.13653) - *Leo Gao et al. (2025), arXiv preprint.* Trains transformers with mostly-zero weights so that their circuits are small enough to read off the weights.
- [Decomposition of Small Transformer Models](https://arxiv.org/abs/2511.08854) - *Casper L. Christensen and Logan Riggs (2025), NeurIPS 2025 Workshop.* Applies stochastic parameter decomposition to small transformers, recovering mechanisms such as induction heads in weights.
- [Backdoor Unlearning by Linear Task Decomposition](https://arxiv.org/abs/2510.14845) - *Amel Abdelraheem et al. (2025), arXiv preprint.* Finds backdoors disentangled in weight space and removes them by subtracting a task-vector-like direction.
- [Preserving Bilinear Weight Spectra with a Signed and Shrunk Quadratic Activation Function](https://arxiv.org/abs/2509.01874) - *Jason Abohwo and Thomas Mosen (2025), arXiv preprint.* An activation function that keeps gated MLPs spectrally interpretable from their weights at competitive performance.
- [Watch the Weights: Unsupervised monitoring and control of fine-tuned LLMs](https://arxiv.org/abs/2508.00161) - *Ziqian Zhong and Aditi Raghunathan (2025), ICLR 2026.* Reads new behaviours such as backdoors or unlearning from the top singular vectors of fine-tuning weight diffs.
- [Stochastic Parameter Decomposition](https://arxiv.org/abs/2506.20790) - *Lucius Bushnaq et al. (2025), arXiv preprint.* A more scalable and robust successor to attribution-based parameter decomposition (SPD).
- [Compositionality Unlocks Deep Interpretable Models](https://arxiv.org/abs/2504.02667) - *Thomas Dooms et al. (2025), arXiv preprint.* A tensor-network architecture whose computations can be read from its weights by diagonalization.
- [Interpretability in Parameter Space: Minimizing Mechanistic Description Length with Attribution-based Parameter Decomposition](https://arxiv.org/abs/2501.14926) - *Dan Braun et al. (2025), arXiv preprint.* Decomposes a network's parameters into faithful, minimal, and simple mechanism components (APD).
- [PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2411.17453) - *Zhen Sun et al. (2024), IEEE S&P 2025.* Detects backdoored PEFT adapters with a classifier on adapter weights, and releases a benchmark of thousands of adapters (PEFTGuard).
- [Solving Trojan Detection Competitions with Linear Weight Classification](https://arxiv.org/abs/2411.03445) - *Todd Huster et al. (2024), arXiv preprint.* Shows that a linear classifier on preprocessed weights solves many trojan-detection benchmarks.
- [Bilinear MLPs enable weight-based mechanistic interpretability](https://arxiv.org/abs/2410.08417) - *Michael T. Pearce et al. (2024), ICLR 2025.* Shows that bilinear MLPs can be interpreted directly from weights by eigendecomposing their interaction tensors, with no data.
- [Talking Heads: Understanding Inter-layer Communication in Transformer Language Models](https://arxiv.org/abs/2406.09519) - *Jack Merullo et al. (2024), NeurIPS 2024.* Finds low-rank communication channels between attention heads from SVDs of weight matrices and edits them to change behaviour.
- [Analyzing Transformers in Embedding Space](https://arxiv.org/abs/2209.02535) - *Guy Dar et al. (2022), ACL 2023.* Projects all transformer parameters into the embedding space so weights can be read directly without running inputs.
- [Transformer Feed-Forward Layers Build Predictions by Promoting Concepts in the Vocabulary Space](https://arxiv.org/abs/2203.14680) - *Mor Geva et al. (2022), EMNLP 2022.* Reads FFN value vectors by projecting them onto the vocabulary, and uses the reading to switch off weights that promote toxic tokens.
- [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913) - *Mor Geva et al. (2020), EMNLP 2021.* Shows that FFN layers act as key-value memories whose weight rows can be read as input patterns and output distributions, the basis for MLP-targeted editing.

**[⬆ back to top](#contents)**

## Resources

Benchmarks, datasets, tools, model zoos, and surveys.

### Benchmarks, Datasets, Tools and Model Zoos

Evaluation suites for weight-space programming, weight edits and merges, software for manipulating weights, and collections of trained networks for weight-space research.

- [WeightBench: Evaluating Language Models as Weight-Space Programmers](https://arxiv.org/abs/2611.18553) - *Aayush Marasini et al. (2026), arXiv preprint.* A benchmark of reading, repairing, and writing tasks that scores LLMs as weight-space programmers, from tiny policies up to 7B language models, including edits that should be refused as impossible.
- [IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection](https://arxiv.org/abs/2611.08647) - *Chris von Csefalvay et al. (2026), arXiv preprint.* Benchmarks an editor LLM that changes a target language model's behaviour only through read-weight and write-weight tools, with no gradients.
- [A Night at the LLM Zoo: Data Conditioned Flow Matching for Generating Pretrained LLM Weights](https://arxiv.org/abs/2611.07103) - *Scott Biggs et al. (2026), arXiv preprint.* Releases hundreds of GPT-2-scale models trained on controlled data mixtures and a data-conditioned flow-matching model of their weights.
- [BrainSurgery: Reproducible and Flexible Declarative Weight Manipulations for Model Editing and Upcycling](https://arxiv.org/abs/2606.09707) - *Gianluca Barmina et al. (2026), arXiv preprint.* Tool that expresses checkpoint surgery (merging, low-rank rewriting, casting, upcycling) as declarative, reproducible plans over weight tensors.
- [Do Text Edits Generalize to Visual Generation? Benchmarking Cross-Modal Knowledge Editing in UMMs](https://arxiv.org/abs/2606.00477) - *Xin Gao et al. (2026), ICML 2026.* Benchmark showing that text-side weight edits in unified multimodal models rarely carry over to image generation (UniKE).
- [Are We Evaluating the Edit Locality of LLM Model Editing Properly?](https://arxiv.org/abs/2601.17343) - *Wei Liu et al. (2026), arXiv preprint.* Shows that standard CounterFact and zsRE locality metrics are insensitive, and proposes a better protocol for measuring edit locality.
- [KnowledgeSmith: Uncovering Knowledge Updating in LLMs with Model Editing and Unlearning](https://arxiv.org/abs/2510.02392) - *Yinyi Luo et al. (2025), ICLR 2026.* A unified framework and graph-structured benchmark for studying how weight edits and unlearning propagate (KnowledgeSmith).
- [MergeBench: A Benchmark for Merging Domain-Specialized LLMs](https://arxiv.org/abs/2505.10833) - *Yifei He et al. (2025), NeurIPS 2025 (Datasets and Benchmarks).* Benchmark for merging domain-specialized LLMs at realistic scale (MergeBench).
- [A Model Zoo of Vision Transformers](https://arxiv.org/abs/2504.10231) - *Damian Falk et al. (2025), arXiv preprint.* A model zoo of vision transformers for weight-space research on modern architectures.
- [We Should Chart an Atlas of All the World's Models](https://arxiv.org/abs/2503.10633) - *Eliahu Horwitz et al. (2025), arXiv preprint.* Argues for and begins building an atlas of public models linked by their weight-space lineage.
- [Implicit-Zoo: A Large-Scale Dataset of Neural Implicit Functions for 2D Images and 3D Scenes](https://arxiv.org/abs/2406.17438) - *Qi Ma et al. (2024), NeurIPS 2024.* A large dataset of neural implicit functions for 2D images and 3D scenes, which serve as weight-space training data (Implicit-Zoo).
- [FusionBench: A Unified Library and Comprehensive Benchmark for Deep Model Fusion](https://arxiv.org/abs/2406.03280) - *Anke Tang et al. (2024), arXiv preprint.* A unified benchmark and library for comparing model fusion and merging methods (FusionBench).
- [Arcee's MergeKit: A Toolkit for Merging Large Language Models](https://arxiv.org/abs/2403.13257) - *Charles Goddard et al. (2024), EMNLP 2024 (Industry).* The standard open-source toolkit for merging LLM weights, implementing task arithmetic, TIES, DARE, SLERP, and layer stacking. [[Code](https://github.com/arcee-ai/mergekit)]
- [A Comprehensive Study of Knowledge Editing for Large Language Models](https://arxiv.org/abs/2401.01286) - *Ningyu Zhang et al. (2024), arXiv preprint.* Introduces the KnowEdit benchmark and compares editing methods by where in the model they write knowledge. [[Code](https://github.com/zjunlp/EasyEdit)]
- [EasyEdit: An Easy-to-use Knowledge Editing Framework for Large Language Models](https://arxiv.org/abs/2308.07269) - *Peng Wang et al. (2023), ACL 2024 (Demo).* Open-source framework implementing most weight-editing methods behind one interface, widely used for editing experiments (EasyEdit). [[Code](https://github.com/zjunlp/EasyEdit)]
- [Evaluating the Ripple Effects of Knowledge Editing in Language Models](https://arxiv.org/abs/2307.12976) - *Roi Cohen et al. (2023), TACL 2024.* Evaluates whether an edited fact's logical ripple effects are updated too (RippleEdits).
- [Detecting Edit Failures In Large Language Models: An Improved Specificity Benchmark](https://arxiv.org/abs/2305.17553) - *Jason Hoelscher-Obermaier et al. (2023), Findings of ACL 2023.* Adds harder specificity tests to CounterFact (CounterFact+), exposing that ROME and MEMIT edits leak into unrelated prompts.
- [MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions](https://arxiv.org/abs/2305.14795) - *Zexuan Zhong et al. (2023), EMNLP 2023.* A multi-hop question benchmark showing that weight-edited models often fail to propagate edited facts to their implications (MQuAKE). [[Code](https://github.com/princeton-nlp/MQuAKE)]
- [Sparsified Model Zoo Twins: Investigating Populations of Sparsified Neural Network Models](https://arxiv.org/abs/2304.13718) - *Dominik Honegger et al. (2023), arXiv preprint.* Pairs dense model zoos with sparsified twins to study how pruning shows up in weight space.
- [Model Zoos: A Dataset of Diverse Populations of Neural Network Models](https://arxiv.org/abs/2209.14764) - *Konstantin Schürholt et al. (2022), NeurIPS 2022.* Releases structured populations of trained networks as a standard dataset for weight-space learning. [[Code](https://github.com/ModelZoos/ModelZooDataset)]
- [Classifying the classifier: dissecting the weight space of neural networks](https://arxiv.org/abs/2002.05688) - *Gabriel Eilertsen et al. (2020), ECAI 2020.* Builds a large set of trained classifiers and shows that properties such as training data and hyperparameters can be read from their weights.

**[⬆ back to top](#contents)**

### Surveys and Position Papers

Overviews of one or more of these areas.

- [Position: Weight Space Should Be a First-Class Generative AI Modality](https://arxiv.org/abs/2605.18632) - *Zhangyang Wang et al. (2026), arXiv preprint.* Position paper arguing that weight space should be treated as a first-class generative modality.
- [A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090) - *Xiaolong Han et al. (2026), arXiv preprint.* Survey of weight-space learning organized into understanding, representing, and generating weights. [[Code](https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning)]
- [Model Merging in the Era of Large Language Models: Methods, Applications, and Future Directions](https://arxiv.org/abs/2603.09938) - *Mingyang Song and Mao Zheng (2026), arXiv preprint.* Up-to-date survey of model merging for large language models.
- [Symmetry in Neural Network Parameter Spaces](https://arxiv.org/abs/2506.13018) - *Bo Zhao et al. (2025), TMLR.* Surveys parameter-space symmetries and their consequences for merging, optimization, and networks that process weights.
- [Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities](https://arxiv.org/abs/2408.07666) - *Enneng Yang et al. (2024), arXiv preprint.* Comprehensive survey of model merging methods, theory, and applications across LLMs, multimodal models, and other settings. [[Code](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications)]
- [Knowledge Editing for Large Language Models: A Survey](https://arxiv.org/abs/2310.16218) - *Song Wang et al. (2023), ACM Computing Surveys.* Broad survey of knowledge editing for LLMs, organized by where and how the edit is stored.
- [A Brief Review of Hypernetworks in Deep Learning](https://arxiv.org/abs/2306.06955) - *Vinod Kumar Chauhan et al. (2023), arXiv preprint.* Reviews hypernetworks, the main family of models that write another network's weights.
- [Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172) - *Yunzhi Yao et al. (2023), EMNLP 2023.* Taxonomy and empirical comparison of LLM editing methods, separating parameter-preserving from parameter-modifying approaches. [[Code](https://github.com/zjunlp/EasyEdit)]

**[⬆ back to top](#contents)**

## Contributing

Contributions are welcome! The list is generated from [`papers.yaml`](papers.yaml): add an entry there, run `python scripts/build_readme.py`, and open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for the scope and the entry format.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work. See [LICENSE](LICENSE).

<sub>259 papers. This file is generated from `papers.yaml` by `scripts/build_readme.py`; do not edit it by hand.</sub>
