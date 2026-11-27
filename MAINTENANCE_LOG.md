# Maintenance log

One line per maintenance run that changed `papers.yaml`, newest first. The "skipped borderline" column lists judgment calls the maintainer may want to overrule. To overrule a skip, add the paper with `scripts/arxiv_lookup.py`.

| Date | Changes | Skipped borderline |
|---|---|---|
| 2026-11-27 | added: Agentic Model Editing for VLM few-shot adaptation (2611.34036), Kolpona neuron programming (2611.33973), Do We Really Need an LLM for WSP? / FWSP (2611.34612), Hierarchical Graph Metanetworks (2611.34726), Displacement Probing / DSProbe (2611.33998), vSFT (2611.34440), The Marauder's Map / Nimbus (2611.33353); backfilled: none (primary venue sites openreview.net, jmlr.org, iclr.cc, neurips.cc unreachable from this session; candidates to recheck: What Matters for Model Merging at Scale? (2410.03617) possibly TMLR, Learning on LoRAs (2410.04207) possibly ICLR 2025 Workshop, Transmuting prompts into weights (2510.08734) possibly NeurIPS 2026) | Closed-form LLM-written classifiers (2611.33972): LLM writes classical closed-form heads, no encoder weights change; Rethinking Sequential Locate-Then-Edit (2611.33692): batch-equivalent sequential editor, crowded space (cf. RLSEdit skip); TASK Memory (2611.34762): memory system that uses knowledge editing only as a component; Localizing Cross-Lingual Generalization in Parameter Space (2611.31975): LMC analysis of LoRA adapters, mostly an adaptation recipe; C2LoRA-TS (2611.34206): incremental text-to-LoRA variant; RaTW (2611.33315), BRR (2611.33308): incremental merging methods; Flakes of WSP (Snowflake blog): page unreachable, could not verify |
| 2026-11-26 | added: Tool-free WSP repair of a quantized network (2611.33031), Game-theoretic policies in weight space (2611.31979), A Bias in Disguise / gradient baseline for the MATH-500 edit (2611.33133), RL for Neural Model Editing (2606.13461, older, found by web search); backfilled: venue and code for Evolutionary Optimization of Model Merging Recipes (2403.13187), venue for Deep Linear Probe Generators (2410.10811) | GUI-WEdit/GUI-SkillEvo (2611.32332): closed-form MLP edit of a GUI agent, algorithmic rather than LLM-driven, incremental; Latent Merger (2611.33048): incremental hypernetwork-LoRA merging; ReQOR (2611.32755): closed-form backdoor repair adapter, marginal; Sandbagging elicitation via head ablation (2611.31615): activation-based, weights fixed; Layer-wise FFN intrinsic dimensionality (2611.32782): activation PCA for pruning; Medical segmentation as a coding task (2611.31673): agents write code, not weights; Invariance training controls (2611.23907): out of scope |
| 2026-11-25 | added (manually): Weight-Space Micromachines (papail.io blog). Title and code from the page and its GitHub source; author inferred from site ownership, as the page has no byline; date from the public-launch commit | - |
| 2026-11-25 | added (manually, verified from page source): Sparks of Weight-Space Programming (Takehi et al., MIT CSAIL blog); Looped Weight-Space Programming (Elsayed et al., MBZUAI blog) | - |
| 2026-11-25 | added: Imprint Reader (2609.35261), Targeted Recovery of Weight-Space Mechanisms / tPD (2607.13047) (both older than the 7-day window, found by web search); backfilled: code for Weight-space programming for auditing clinical decision networks (2611.05341) | Empirical Margin Sensitivity (2611.30675): neuron-column ablation probe of medical LLMs, interpretability-only; Spectral Circuit Analysis (2611.30939): gradient-based circuit discovery, not weight-based; VIPE (2611.28135): privacy erasure acts on visual representations, not weights; Learning with Unlearning (2611.24205): incremental continual-learning/unlearning method; DiVE (2611.28420): RSI agents rewrite programs, not weights; Evolving Agent Harnesses (2611.25380): explicitly avoids weight updates; WSP-Scope (2611.09382): linked repo holds only a PDF, so no code link added |
| 2026-11-24 | added: TowerBridge (2611.31233), Weight Coding (2611.29613), HypoLoop (2611.23718), Optics as code (2611.23875), Self-Upgrading Embodied Agents (2611.31117), SELFWRITE (2611.29513), Self-WSP (2611.28833), BaseRSI (2611.24578), Don't Train It, Write It (2611.28483), C2 rewiring control (2611.29120), LLM repair without gradients (2611.25613), Weight-editing agent on vision faults (2611.28781), LLM weight edits on YOLO26 (2611.17789), IR-ODWSP (2611.29882), CPU inside an LLM (2611.26450), Interference bounds (2611.25430), Watch Where You Linearize (2611.25000), Comparing representations from computation graphs (2611.26081), Video-as-Weights (2611.28221); backfilled: code for Learning to Interpret Weight Differences (2510.05092), Editing Common Sense in Transformers (2305.14956) | PAWP-TTS (2611.29455): mainly a TTS system, WSP study finds no gain beyond controls; Cleave (2611.27426): training-free guardrail-removal attack, not WSP-driven; Rank-One Bypass of Linear Erasure (2611.23880): attack on erasure layers, marginal; Memento (2611.10450): prompt-space recovery, no weight change; Abliteration harder? (2611.17846): refusal-removal benchmarking; Self-Replicating LMs (2611.25839): weight copying/mutation only incidental; Towards Autoregressive Parameter Generation (2611.25538): appears to be the IGPG method already listed; Learning trajectories in weight space (2611.24782): small-scale study; WaXup (2611.27353): weight interpolation only as data augmentation; Capability regions under optimization (2611.27445): marginal; HR-Merge (2611.27377), AMARIS (2611.27369), MATE (2611.28855), Altair-Nidhogg (2611.27550), TCR (2611.25575), HOSE (2611.30592), BiSpace (2611.25861), MI-Hyper (2611.22968), WASP (2611.30134), CDPG (2611.25592): incremental merging/editing/hypernetwork variants |
| 2026-11-23 | Reorganized into Weight-Space Programming / Foundations / Resources; added 14 WSP papers (2611.20566, 2611.27089, 2611.13758, 2611.24330, 2611.12066, 2611.22055, 2611.19292, 2611.09271, 2611.11604, 2611.11537, 2611.12954, 2611.09559, 2611.22013, 2611.21432) | 2611.18690 and 2611.04268 (see below) |
| 2026-11-23 | Seed: 245 papers added (see below for skipped candidates) | See "Seed run" section |

## Seed run (2026-11-23): candidates considered and left out

These papers were found and checked during the initial population but left out as borderline, incremental, or out of scope. Add any of them with `scripts/arxiv_lookup.py` if you disagree. The titles here are short working labels; `arxiv_lookup.py` gives the verified title.

| arXiv | Paper | Reason |
|---|---|---|
| [2611.18690](https://arxiv.org/abs/2611.18690) | Perceptual WSP for Diffusion Super-Resolution | the authors' arXiv comment says the evaluation has issues and the findings may not be reliable |
| [2611.04268](https://arxiv.org/abs/2611.04268) | WSP for Image-Restoration Diffusion Models | explicitly conjectural (per its arXiv comment), with no established results yet |
| [2404.14394](https://arxiv.org/abs/2404.14394) | MAIA: Multimodal Automated Interpretability Agent | Agent runs interpretability experiments but does not write persistent weight edits |
| [2311.10905](https://arxiv.org/abs/2311.10905) | Flexible Model Interpretability through NL Model Editing | Short abstract links NL-driven editing and interpretability but gives no clear mechanism by which a model writes weights |
| [2601.07309](https://arxiv.org/abs/2601.07309) | ARM: Role-Conditioned Neuron Transplantation for Agent Merging | Merges agent LLMs via neuron transplantation; the merge is algorithmic, not LLM-driven |
| [2511.23473](https://arxiv.org/abs/2511.23473) | ThetaEvolve | Test-time RL updates of the proposer LLM; ordinary RL fine-tuning, not self-authored edits |
| [2605.03808](https://arxiv.org/abs/2605.03808) | Agentic-imodels | Agent evolves interpretable tabular model code, not neural weights |
| [2611.08438](https://arxiv.org/abs/2611.08438) | Understanding AI from the Inside (mech-interp survey) | Survey; discusses interpretability agents but is not a weight-editing contribution |
| [2601.15686](https://arxiv.org/abs/2601.15686) | RLSEdit: Soft Recursive Least-Squares Lifelong Editing | solid closed-form Woodbury online editor with bounds, but crowded space |
| [2605.09285](https://arxiv.org/abs/2605.09285) | BetaEdit | null-space plus history-aware variant; incremental |
| [2510.13851](https://arxiv.org/abs/2510.13851) | EvoEdit (null-space alignment, ACL 2026 Findings) | incremental AlphaEdit successor |
| [2610.25914](https://arxiv.org/abs/2610.25914) | FisherEdit | interesting claim that AlphaEdit gains come from regularization, not projection; overlaps with 2605.26670 |
| [2606.26783](https://arxiv.org/abs/2606.26783) | AlphaEdit reproducibility study | useful negative result (does not carry over to newer architectures or long horizons); optional |
| [2510.22139](https://arxiv.org/abs/2510.22139) | NMKE dynamic sparse neuron masking (NeurIPS 2025) | lifelong neuron-masked editing; incremental |
| [2507.18028](https://arxiv.org/abs/2507.18028) | NeuralDB | casts L&E as a KV database but adds a gated external module; semi-parametric |
| [2605.08143](https://arxiv.org/abs/2605.08143) | HoReN | codebook/Hopfield parameter-preserving editor; borderline on "changes weights" |
| [2611.25861](https://arxiv.org/abs/2611.25861) | BiSpace | memory-based, retrieval-heavy |
| [2610.11160](https://arxiv.org/abs/2610.11160) | LadderEdit (EMNLP 2026) | per-edit LoRA compression; more adapter storage than weight geometry |
| [2610.34768](https://arxiv.org/abs/2610.34768) | DynEdit (NeurIPS 2026) | long-form chunked editing variant; AnyEdit++ chosen as representative |
| [2609.29045](https://arxiv.org/abs/2609.29045) | Toketive: tokenization bypasses editing/unlearning | security of edits; secondary |
| [2611.10450](https://arxiv.org/abs/2611.10450) | Memento: prompt-space recovery of edits | complements 2605.28839/2606.23276 but recovers edits through inputs only |
| [2512.04144](https://arxiv.org/abs/2512.04144) | RippleBench | mostly an unlearning ripple benchmark, not editing |
| [2609.00184](https://arxiv.org/abs/2609.00184) | ParallelEvents/SYNAPSE (NeurIPS 2026) | knowledge insertion via instruction tuning; closer to fine-tuning |
| [2607.26455](https://arxiv.org/abs/2607.26455) | ForgetBench | sequential-editing forgetting benchmark; not yet at a venue |
| [2604.05995](https://arxiv.org/abs/2604.05995) | Surface Compliance (ACL 2026 Findings) | evaluation critique; overlaps with 2510.00625 |
| [2510.25798](https://arxiv.org/abs/2510.25798) | MemEIC (NeurIPS 2025) | multimodal; hybrid external memory plus LoRA |
| [2512.04753](https://arxiv.org/abs/2512.04753) | EtCon | edit then GRPO consolidation; closer to a fine-tuning recipe |
| [2605.16686](https://arxiv.org/abs/2605.16686) | Tensor-structured MoE editing | MEMIT for MoE via Woodbury; alternative to MoEEdit |
| [2506.01153](https://arxiv.org/abs/2506.01153) | WARP: Weight-Space Linear RNNs | hidden state = weights of aux net; weight-space as sequence model, not learning on trained models |
| [2611.08866](https://arxiv.org/abs/2611.08866) | Reconstructing LLM Lineage Trees via Fine-Tuning Path Inference | lineage tree recovery but explicitly gray-box (log-likelihoods, no weights) |
| [2607.29463](https://arxiv.org/abs/2607.29463) | Weight-Space MoE for INR Classification | solid INR-weight classifier but niche |
| [2601.23181](https://arxiv.org/abs/2601.23181) | Semantics in INR weights via Implicit Function Theorem | INR weight-space theory |
| [2604.25119](https://arxiv.org/abs/2604.25119) | Evaluation without Generation (Gaussian probing of LoRAs) | auditing LoRAs via probing, safety application |
| [2610.41375](https://arxiv.org/abs/2610.41375) | BULLPEN: LLM profiling via model embeddings | model embeddings from behavior not weights |
| [2512.08826](https://arxiv.org/abs/2512.08826) | CARLoS: LoRA retrieval at scale | LoRA retrieval via generated outputs, not weights |
| [2611.09650](https://arxiv.org/abs/2611.09650) | TensorMutation | GNN on neural graphs predicts weight mutations; SE application |
| [2610.00820](https://arxiv.org/abs/2610.00820) | On-the-fly Weight Generation on ARC-1D | toy hypernetwork proof-of-concept |
| [2606.06492](https://arxiv.org/abs/2606.06492) | Code2LoRA | repo -> LoRA hypernetwork; application of Doc-to-LoRA idea |
| [2610.34413](https://arxiv.org/abs/2610.34413) | T2L-ICAG for audio LMs | Text-to-LoRA extension to audio LLMs |
| [2604.23750](https://arxiv.org/abs/2604.23750) | The Override Gap (Doc-to-LoRA failure analysis) | useful analysis of D2L conflicts |
| [2609.38374](https://arxiv.org/abs/2609.38374) | Doc2LoRA representations of scientific ideas | uses doc->LoRA adapters as representations |
| [2610.31017](https://arxiv.org/abs/2610.31017) | Mostly Reading: document-level LoRA adapters | evaluation of doc-LoRAs |
| [2506.11638](https://arxiv.org/abs/2506.11638) | LoRA-Gen | cloud LLM generates LoRA for edge model from task description |
| [2509.10535](https://arxiv.org/abs/2509.10535) | Semantic-guided LoRA Parameters Generation | conditional LoRA generation for edge users |
| [2510.19733](https://arxiv.org/abs/2510.19733) | Zhyper: Factorized Hypernetworks for Conditioned LLM Fine-Tuning | text-conditioned hypernetwork LoRA |
| [2608.03275](https://arxiv.org/abs/2608.03275) | MoEGen | expert-conditioned LoRA generation for PEFT |
| [2609.18842](https://arxiv.org/abs/2609.18842) | Infinite-Parameter LLMs | generates weights from live data; preliminary |
| [2611.04497](https://arxiv.org/abs/2611.04497) | SKILL2STEER | NL skill -> activation shifts (not weights) |
| [2601.15912](https://arxiv.org/abs/2601.15912) | TeNet: Text-to-Network policies | text-conditioned hypernetwork for small robot policies |
| [2509.04145](https://arxiv.org/abs/2509.04145) | Hyper Diffusion Avatars | weight-space diffusion applied to avatar NeRF-like nets |
| [2511.00543](https://arxiv.org/abs/2511.00543) | Lo-Hp learned optimizer for weight generation | weight-generation-as-optimizer |
| [2406.11717](https://arxiv.org/abs/2406.11717) | Refusal Is Mediated by a Single Direction | Weight orthogonalization edit, but the direction comes from activations; steering-adjacent |
| [2603.10806](https://arxiv.org/abs/2603.10806) | Backdoor Directions in ViTs | Trigger direction found in activations (needs the trigger); has parameter-space interventions |
| [2611.27353](https://arxiv.org/abs/2611.27353) | WaXup: Weight Averaging for Introspection | Extends DIT-style introspection with weight-space interpolation; incremental |
| [2608.22034](https://arxiv.org/abs/2608.22034) | Coherentist View of Transformer Computation | Weight-space role signatures across 15 models; framework is speculative |
| [2510.14936](https://arxiv.org/abs/2510.14936) | Circuit Insights (WeightLens/CircuitLens) | Partly weight-based via transcoders; mostly transcoder-feature analysis |
| [2609.34970](https://arxiv.org/abs/2609.34970) | Mechanistic Diagnosis and Parameter-Space Mitigation of Emergent Misalignment | Parameter-space projection fix, but analysis is gradient/Hessian based |
| [2507.09816](https://arxiv.org/abs/2507.09816) | Compressed Computation (toy Universal-AND) | Toy-model circuit study used as an APD/SPD testbed; marginal |
| [2601.21690](https://arxiv.org/abs/2601.21690) | Unified Generalization Framework for Model Merging | Theory (L2-stability) of merging; possible addition if more theory is wanted |
| [2606.04754](https://arxiv.org/abs/2606.04754) | LMC via Neuron Identifiability | Symmetry theory for LMC; more about symmetry than merging practice |
| [2611.04108](https://arxiv.org/abs/2611.04108) | Common-Unique Subspace Decomposition | Solid but incremental subspace-merging variant (one of many such 2026 papers) |
| [2605.28444](https://arxiv.org/abs/2605.28444) | Bilinear Coordinate Alignment for Task-Vector Transfer | Another task-vector transport method; overlaps GradFix and Theseus |
| [2611.11177](https://arxiv.org/abs/2611.11177) | Cross-Task Merging in Neural Thickets | Merging of random-perturbation experts; niche |
| [2405.17461](https://arxiv.org/abs/2405.17461) | EMR-Merging | Elect-mask-rescale; well cited but incremental after TIES/TALL |
| [2406.15479](https://arxiv.org/abs/2406.15479) | Twin-Merging | Dynamic routing of modular experts; drifts toward MoE |
| [2403.19522](https://arxiv.org/abs/2403.19522) | Model Stock | Few-model soups via geometric interpolation; could join the core list |
| [2312.06795](https://arxiv.org/abs/2312.06795) | Model Breadcrumbs | Sparse-mask task-vector merging; incremental |
| [2504.02620](https://arxiv.org/abs/2504.02620) | TaLoS: Task-Localized Sparse Fine-tuning | Fine-tunes for better task arithmetic; borderline core |
| [2211.08403](https://arxiv.org/abs/2211.08403) | REPAIR | Renormalization fix for permuted-model interpolation; complements Git Re-Basin |
| [1910.05653](https://arxiv.org/abs/1910.05653) | Model Fusion via Optimal Transport | Early OT neuron-alignment fusion; historical precursor |
| [2605.01580](https://arxiv.org/abs/2605.01580) | Model Merging: Foundations and Algorithms (PhD thesis) | Thesis; useful reference but not a paper |
| [2610.00420](https://arxiv.org/abs/2610.00420) | Transferable Graph Metanetworks | judged lower priority than the selected papers in its category |
| [2610.01649](https://arxiv.org/abs/2610.01649) | CrossGMN: Cross-Architecture Weight-Space Transformations | judged lower priority than the selected papers in its category |
| [2602.16316](https://arxiv.org/abs/2602.16316) | WS-KAN: Graph Meta-Network for Kolmogorov-Arnold Networks | judged lower priority than the selected papers in its category |
| [2609.33901](https://arxiv.org/abs/2609.33901) | Finite Probes Suffice (HiddenProbe) | judged lower priority than the selected papers in its category |
| [2607.10617](https://arxiv.org/abs/2607.10617) | modelDNA: Lineage Verification from Sampled Weight Fingerprints | judged lower priority than the selected papers in its category |
| [2607.02166](https://arxiv.org/abs/2607.02166) | Dynamic Neural Graph Encoding (DNG-Encoder) | judged lower priority than the selected papers in its category |
| [2611.26081](https://arxiv.org/abs/2611.26081) | Learning to Compare Representations from Parameterized Computation Graphs | judged lower priority than the selected papers in its category |
| [2610.38356](https://arxiv.org/abs/2610.38356) | CLIK: Internalizing Context via Parametric Flow | judged lower priority than the selected papers in its category |
| [2606.22429](https://arxiv.org/abs/2606.22429) | Graph-aware LoRA Generation for LLMs | judged lower priority than the selected papers in its category |
| [2603.00180](https://arxiv.org/abs/2603.00180) | NNiT: Width-Agnostic NN Generation | judged lower priority than the selected papers in its category |
| [2507.10623](https://arxiv.org/abs/2507.10623) | Flows and Diffusions on the Neural Manifold | judged lower priority than the selected papers in its category |
| [2611.25538](https://arxiv.org/abs/2611.25538) | Towards Autoregressive NN Parameter Generation (IGPG) | judged lower priority than the selected papers in its category |
| [2603.23408](https://arxiv.org/abs/2603.23408) | GeoSANE: Learning Geospatial Representations from Models | judged lower priority than the selected papers in its category |
| [2512.08785](https://arxiv.org/abs/2512.08785) | LoFA: Predicting Personalized Priors for Visual Generative Models | judged lower priority than the selected papers in its category |
| [2610.20606](https://arxiv.org/abs/2610.20606) | Weight Diffusion for Humanoid Policies | judged lower priority than the selected papers in its category |
| [2611.04614](https://arxiv.org/abs/2611.04614) | Policy Network Diffusion (DPPG) | judged lower priority than the selected papers in its category |
| [2505.13919](https://arxiv.org/abs/2505.13919) | DynaDiff: Weight-space Diffusion for Dynamics Adaptation | judged lower priority than the selected papers in its category |
| [2610.30847](https://arxiv.org/abs/2610.30847) | JEPAWG on Parametric Dynamical Systems (model zoos with ground truth) | judged lower priority than the selected papers in its category |
| [2408.01415](https://arxiv.org/abs/2408.01415) | Conditional LoRA Parameter Generation (COND P-DIFF) | judged lower priority than the selected papers in its category |
