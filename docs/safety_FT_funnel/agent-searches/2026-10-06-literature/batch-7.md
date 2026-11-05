# Safety fine-tune literature, batch 7

Five Hugging Face models. The two DynaGuard rows are one paper, read once, with the learning rate that the appendix marks for each size. Facts below are quoted from a paper, a script, a blog, a dataset card, or a cached model card. A method word inside a repository or dataset name is recorded as a name, not as a training method.

Earlier output-type reading: `docs/safety_FT_funnel/how-models-are-filtered.md`. Agreement is stated in each model section.

## Summary

| model | source found | objective | update scope | data (name, n, provenance) | base | output type | matches inventory row |
|---|---|---|---|---|---|---|---|
| tomg-group-umd/DynaGuard-1.7B | paper | SFT, then GRPO | not stated (full checkpoint uploaded; paper never says LoRA or full) | DynaBench 40,000 + four safety sets 40,000 for SFT; 11,000 of the mix for GRPO. DynaBench dialogues are synthetic. | Qwen/Qwen3-1.7B, instruction model | verdict | partly |
| jdleo1/tinysafe-3 | blog and code | SFT on teacher labels (distillation) | QLoRA, merged | ToxicChat, WildGuard, hard negatives, synthetic boundary cases. Card total ~16,700; itemized rows sum to 10,843. Human labels plus Claude, DeepSeek, and Grok text. | Qwen/Qwen3-4B-Instruct-2507, instruction model | verdict | partly |
| ryo-llm/qwen3-4b-agent-trajectory-lora-alf-guard | none (model card only) | loss on assistant turns (SFT). The word SFT is in the dataset name. | LoRA, full-precision base. Card says adapter only. Files are a full 4B checkpoint. | u-10bei/sft_alfworld_trajectory_dataset_v5, 2,502 rows, programmatic synthetic trajectories, no generator model | Qwen/Qwen3-4B-Instruct-2507, instruction model | reply | partly |
| tomg-group-umd/DynaGuard-4B | paper | SFT, then GRPO | not stated (full checkpoint uploaded; paper never says LoRA or full) | same mix as the 1.7B model | Qwen/Qwen3-4B, instruction model | verdict | partly |
| vominhmanh/qwen3-4b-vihsd | none for the training run; dataset card and a 2021 paper for the labels | SFT (next-token loss) | LoRA on the merged-model card; the adapter card says a 4-bit base. Merged into this repo. | vominhmanh/vihsd-explainable, train 24,048. Human ViHSD labels; explanations from GPT-4o-mini. | unsloth/Qwen3-4B-Instruct-2507, instruction model | verdict | partly |

## tomg-group-umd/DynaGuard-1.7B

### Sources

- Paper, ICLR 2026 proceedings and arXiv: Hoover et al., "DynaGuard: A Dynamic Guardian Model With User-Defined Policies", https://arxiv.org/abs/2509.02563 and https://arxiv.org/html/2509.02563v3. The proceedings PDF is https://proceedings.iclr.cc/paper_files/paper/2026/file/8d2aad53fa148791ffd004a7c9cce5ad-Paper-Conference.pdf. Bold numbers below are from the arXiv HTML, because the PDF text extract does not keep bold.
- OpenReview poster page: https://openreview.net/forum?id=gc8Ylt0lbm. The abstract matches the paper. A search hit on a different OpenReview attachment (WebArbiter) is a different paper and is not used here.
- Code: https://github.com/montehoover/DynaGuard. The repository is an evaluation script (`eval.py`). It has no training script.
- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/tomg-group-umd__DynaGuard-1.7B__2026-10-06.md`.
- Hub file list: https://huggingface.co/api/models/tomg-group-umd/DynaGuard-1.7B. One `model.safetensors`, 2,031,739,904 BF16 parameters. No `adapter_config.json`.
- Dataset size: https://datasets-server.huggingface.co/size?dataset=montehoover/DynaBench. The model-card id `tomg-group-umd/DynaBench` resolves to `montehoover/DynaBench` on that API.

### Training record

(a) Objective. Supervised next-token fine-tuning, then GRPO. Paper says: "The first stage of our training pipeline is supervised fine-tuning over a mixture of 40,000 samples from DynaBench and 40,000 samples from the four safety datasets (WildGuard, BeaverTails, ToxicChat, and Aegis 2.0). We run SFT for 1 epoch, followed by GRPO using 11,000 samples from the data mixture." URL: https://arxiv.org/html/2509.02563v3. The same section writes the GRPO objective as a sampled thinking trace and compliance label with a KL penalty. Card says: "The model was trained using Supervised Fine-Tuning (SFT) for one epoch, followed by GRPO."

(b) Parameter-update scope. Not stated. The paper says training used VERL for both SFT and GRPO. The HTML of the paper contains no "LoRA" and no "PEFT". It also never says that every weight was updated. The upload is a full checkpoint (one safetensors file, 2,031,739,904 BF16 parameters, no adapter file). That file list does not say whether training updated every weight or a merged adapter.

(c) Training data. Paper: 40,000 DynaBench samples plus 40,000 samples from WildGuard, BeaverTails, ToxicChat, and Aegis 2.0, then 11,000 samples from that mixture for GRPO. The chosen safety/DynaBench mix in the appendix is 50/50 (the bold cell). Hub ids for the four safety sets are not stated in the paper. The card names only `tomg-group-umd/DynaBench`.

Released file sizes, which are not the same numbers as the 40,000/40,000 training cut: DynaBenchTrain 61,496 rows; DynaBenchSafetyMix train 70,313 and validation 7,813; DynaBench test 543. Source: the datasets-server size API above. Dataset card says SafetyMix "includes samples from external safety datasets (WildGuard, BeaverTails, ToxicChat, Aegis 2.0) and used to train DynaGuard." URL: https://huggingface.co/datasets/montehoover/DynaBench.

Language: English. Card YAML `language: en`.

Provenance. DynaBench rules and dialogues are synthetic. Paper says rules were expanded with Claude Sonnet 3.5 to 5,000 unique rules, then paraphrased into 40,000 policies. Dialogues were written by GPT-4o-mini and GPT-4.1-mini. Labels and reasoning traces were written by GPT-4o and Gemini-2.0-Flash. A human check of 743 harder training examples had Cohen's kappa 0.85 against the synthetic labels. The four safety sets were converted into policy form ("Do not print harmful content" and subcategory policies). Paper says: "GuardReasoner also provides reasoning traces for these datasets, which we integrate into our Chain of-Thought SFT training." One third of SFT examples include a reasoning trace; two thirds are a direct PASS/FAIL plus a short explanation.

(d) Base model. Card says `Qwen/Qwen3-1.7B`. Paper says: "We use the Qwen3 family of instruction models (Yang et al., 2025) as the models for fine-tuning our guardian models." The Qwen card for that id says "Training Stage: Pretraining & Post-training" and describes instruction following and a chat template. URL: https://huggingface.co/Qwen/Qwen3-1.7B. It is the post-trained model, not `Qwen/Qwen3-1.7B-Base`.

(e) Epochs, learning rate, batch size, hardware. SFT: 1 epoch. GRPO is stated as 11,000 samples, not as a number of epochs. Appendix A.9, arXiv HTML, says the chosen values are in bold. For the 1.7B model the bold SFT learning rate is `3e-5` (options were 1e-5, 3e-5, 6e-5). The bold GRPO learning rate is `3e-6` (options were 1e-6, 3e-6, 6e-6). SFT batch size bold is 128 (options 64, 128, 256). GRPO batch size bold is 48 (options 32, 48, 64, 128, 256). GRPO rollouts bold is 8 (options 8, 12, 16). Shared settings, not swept: cosine schedule, gradient clipping 1.0, weight decay 1e-2, Adam betas 0.9 and 0.95, GRPO KL coefficient 1e-3, response length 1024, temperature 1.0, top-p 1.0. Training hardware is not stated. An H100 is mentioned only for inference timing in appendix A.10.

(f) Evaluation. Card table: DynaGuard-1.7B DynaBench F1 63.5, safety-task average F1 78.5. The paper's Table 3 is a wider F1 table (Aegis 2.0, BeaverTails, HarmBench, SafeRLHF, WildGuard, XSTest, DynaBench) against GPT-4o-mini, Qwen3-8B, WildGuard, LlamaGuard3, NemoGuard, ShieldGemma, and GuardReasoner. Ablations in the paper's Table 4 are on Qwen3-4B, not on the 1.7B model.

(g) Output. A verdict, not a chat reply to the user. Paper says the output "is the compliance classification." Card says fast mode "Provides a direct `PASS` or `FAIL` classification" and a second mode writes a reasoning trace before that label. It reads a natural-language policy plus a user-agent dialogue, and it judges whether the dialogue violates that policy. It is not tied to one fixed harm list.

Agreement with `docs/safety_FT_funnel/how-models-are-filtered.md`: yes. That note says the input is a prompt and a reply and the output is a binary label. The card's chain-of-thought mode adds a written reason before PASS or FAIL. That is still a verdict.

### Discrepancies

1. The card's dataset list is only DynaBench. The paper's training mix is half DynaBench and half WildGuard, BeaverTails, ToxicChat, and Aegis 2.0.
2. The inventory row copies that card list, so its datasets cell omits the four safety sets. Its methods cell `grpo|sft` matches the paper.
3. The released DynaBenchTrain split has 61,496 rows and SafetyMix train has 70,313 rows. The paper says the training run used 40,000 and 40,000.
4. The card's project-page URL points at a GitHub user page (`https://github.com/taruschirag/DynaGuard`). The paper's project page is https://taruschirag.github.io/DynaGuard/.

### Confidence

High. The paper states the objective, the data cut, and the 1.7B learning rates. It does not state whether training updated every weight.

### Queries tried

1. `DynaGuard A Dynamic Guardrail Model With User-Defined Policies Hoover training SFT GRPO`
2. `site:arxiv.org DynaGuard 2509.02563 Qwen3-1.7B Qwen3-4B fine-tuning`
3. `montehoover DynaGuard github training script GRPO SFT hyperparameters`
4. `DynaGuard Hoover VERL full fine-tuning LoRA Qwen3-1.7B hyperparameters bold`
5. `DynaGuard WildGuard BeaverTails ToxicChat Aegis dataset huggingface id 40000`
6. `Hoover Baherwani DynaGuard ICLR 2026 site:openreview.net training`
7. Fetched the arXiv HTML, the ICLR PDF, the GitHub tree, the Hub model API, the DynaBench size API, and the Qwen3-1.7B card.

## jdleo1/tinysafe-3

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/jdleo1__tinysafe-3__2026-10-06.md`. The live card matches it: https://huggingface.co/jdleo1/tinysafe-3.
- Blog, John Leonardo, 7 March 2026: https://jdleo.me/blog/tinysafe-v3. This is an independent write-up, not a copy of the card. The two texts share numbers and then diverge (below).
- Code: https://github.com/jdleo/tinysafe-3. Training script `scripts/04_train.py`, config `configs/config.json`, merge script `scripts/06_export.py`, data loader `scripts/01_prepare_data.py`.

### Training record

(a) Objective. Supervised next-token fine-tuning on labels produced by a teacher. The gradient step is not a preference loss and not a logit-matching loss. Script says: "Step 4 (GPU): QLoRA fine-tuning with TRL SFTTrainer" and `LoraConfig(..., task_type="CAUSAL_LM")` then `trainer = SFTTrainer(...)`. URL: https://github.com/jdleo/tinysafe-3/blob/main/scripts/04_train.py. Card says: "Fine-tuned with QLoRA (4-bit NF4, r=16, alpha=32) via teacher distillation from Claude Sonnet 4.6 + Constitution v3." Blog says: "Train the student on this teacher-aligned data" and "The student learns the constitution's behavior from the labels, not from reading it."

(b) Parameter-update scope. QLoRA. The adapter was merged into the uploaded weights. Card says: "Parameters | 4B (full merged)" and "Fine-tuning | QLoRA (4-bit NF4)" and "LoRA rank | r=16, alpha=32" and "Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj". Script loads `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", ...)` and the same rank, alpha, and target modules, plus `lora_dropout` 0.05, which the card does not mention. `scripts/06_export.py` says "Merge LoRA adapter into base model" and calls `merge_and_unload()` after loading the base in bf16, not in 4-bit.

(c) Training data. Card table: ToxicChat train 5,082 (human safe/unsafe labels kept, teacher reasoning added); WildGuard train 4,000 (full relabel, 787 labels flipped); hard negatives 694 (full relabel, all stayed safe); synthetic boundary 679; v3.4 surgical synthetic 388; total cell "~16,700". Those five rows sum to 10,843, not 16,700. Blog for the 0.822 run (called v3.3 there): "9,500 training samples + 500 validation." Blog for the later run (v3.4): the 388 new samples were "merged them with the 16,377 existing training samples." The blog does not itemize what the extra rows inside 16,377 are.

Hub ids on the card YAML: `lmsys/toxic-chat`, `allenai/wildguardmix`, `PKU-Alignment/BeaverTails`, `google/civil_comments`. The script loads `lmsys/toxic-chat` (`toxicchat0124` train), `allenai/wildguardmix` (`wildguardtrain`), `google/civil_comments`, and `google/jigsaw_toxicity_pred`. The script does not mention BeaverTails. The blog's v3.3 and v3.4 sample lists do not mention Jigsaw or BeaverTails.

Language of the training text: English. Card says: "English-centric training data. Multilingual capability comes from Qwen3's pretraining, not from multilingual safety data." The YAML language list (en, zh, es, fr, ja, ko, de) is the claimed inference coverage.

Provenance. ToxicChat labels kept from humans. WildGuard labels replaced by the teacher. Teacher is Claude Sonnet 4.6 with a system prompt the author calls Constitution v3. Blog says unsafe synthetic examples that Sonnet refused were generated by DeepSeek V3.2 Speciale on OpenRouter, and the v3.4 unsafe examples by Grok 4.1 Fast on OpenRouter. The 694 hard negatives are not given a generator name on the card. The script's hard-negative block names `claude-sonnet-4-6` and `total: 12000`, which is a different count from 694.

(d) Base model. Card, script, and config all say `Qwen/Qwen3-4B-Instruct-2507`. The id contains Instruct. It is an instruction-tuned model.

(e) Epochs, learning rate, batch size, hardware. Config says `num_epochs` 3, `learning_rate` 2e-4, `batch_size` 4, `gradient_accumulation_steps` 8 (the script prints that product as the effective batch size, 32), `weight_decay` 0.01, `warmup_ratio` 0.05, `max_length` 1024, bf16. URL: https://github.com/jdleo/tinysafe-3/blob/main/configs/config.json. Blog for the 0.822 run: "891 steps ... 70 minutes on an RTX 4090" and "Token accuracy hit 85%+ by mid-epoch 1." 9,500 / 32 × 3 is about 891, so that step count matches the config's 3 epochs on the smaller v3.3 set. Blog for v3.4: "1 epoch from the base model wasn't enough ... I continued from that checkpoint for 2 more epochs at half learning rate." The script uses one learning rate for all epochs. It does not implement a half-rate second phase. v3.4 hardware in the blog is "RunPod GPU", not a named chip.

(f) Evaluation. Card: ToxicChat test n=5,083, F1 0.822, precision 0.815, recall 0.829, false-positive rate 1.4%. WildGuardBench F1 0.804. OR-Bench false-positive rate about 4.6%. Blog: the same 0.822 is v3.3. v3.4, after the extra 388 samples, scored ToxicChat F1 0.818 (precision 0.783, recall 0.856). The uploaded card reports 0.822.

(g) Output. A verdict. Card says: "Generates structured JSON with safe/unsafe verdict, 7 safety categories, and chain-of-thought reasoning." Categories named: violence, hate, sexual, self_harm, dangerous_info, harassment, illegal_activity. It reads a user message. It does not write the reply the user asked for.

Agreement with the classification note: yes. That note says the input is a user prompt and the output is reasoning and a verdict.

### Discrepancies

1. The card's five data rows sum to 10,843. The total cell says ~16,700. The blog says 9,500 train + 500 validation for the 0.822 model, and 16,377 existing samples before the v3.4 add.
2. The card reports F1 0.822 and also lists the v3.4 surgical 388 samples. The blog says those 388 samples produced F1 0.818, and 0.822 was the earlier v3.3 checkpoint.
3. Card YAML lists `PKU-Alignment/BeaverTails`. The data-prep script never loads BeaverTails. The script does load `google/civil_comments` and `google/jigsaw_toxicity_pred`, which the blog's v3.3/v3.4 narrative does not list.
4. Config dropout is 0.05. The card does not state dropout.
5. Inventory methods cell is `qlora` only. The card tag list also says distillation, and the script shows that distillation is teacher labels into `SFTTrainer`, not a separate logit loss.

### Confidence

Medium. QLoRA, the merge, the base id, and SFT-on-teacher-labels are stated in both the blog and the script. Which exact row set is inside the uploaded 0.822 checkpoint is not pinned down, because the card mixes the 0.822 score with the later data table.

### Queries tried

1. `jdleo tinysafe-3 QLoRA distillation Claude Sonnet training`
2. `github jdleo tinysafe-3 train.py QLoRA epochs learning rate RTX 4090`
3. Fetched https://jdleo.me/blog/tinysafe-v3
4. Fetched https://github.com/jdleo/tinysafe-3 and the GitHub git tree
5. Fetched `configs/config.json`, `scripts/04_train.py`, `scripts/06_export.py`, `scripts/01_prepare_data.py`
6. Compared the card YAML datasets with the loader (BeaverTails, civil_comments, Jigsaw)

## ryo-llm/qwen3-4b-agent-trajectory-lora-alf-guard

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/ryo-llm__qwen3-4b-agent-trajectory-lora-alf-guard__2026-10-05.md`.
- Hub API: https://huggingface.co/api/models/ryo-llm/qwen3-4b-agent-trajectory-lora-alf-guard. `adapter_config.json` returns 404.
- Dataset card: https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v5. Size API: 2,502 train rows.
- No paper, thesis, blog, or training script names this repository. Searching the exact repo id returns other people's near-copy cards, not a write-up of this upload. Those copies are not used as evidence for this repo.

### Training record

(a) Objective. The card states a supervised loss on assistant tokens and does not use the words SFT, DPO, PPO, or GRPO. Card says: "Loss is applied to all assistant turns in the multi-turn trajectory, enabling the model to learn environment observation, action selection, tool use, and recovery from errors." That is next-token training on the assistant turns. The dataset id is `u-10bei/sft_alfworld_trajectory_dataset_v5`. The name contains "sft". The dataset card uses the same word for the data, not for this training run: "This is a synthetic SFT (Supervised Fine-Tuning) dataset". The repo name contains "guard" and "lora". Neither name is treated as a method statement.

(b) Parameter-update scope. Card says: "This repository provides a LoRA adapter" and "Method: LoRA (full precision base)" and "LoRA: r=64, alpha=128" and "This repository contains LoRA adapter weights only. The base model must be loaded separately." Target modules are not stated. Whether the adapter was merged is contradicted by the files. The card says it was not merged. The Hub file list is `model-00001-of-00002.safetensors` and `model-00002-of-00002.safetensors`, 4,022,468,096 BF16 parameters, and no `adapter_config.json`. A rank-64 adapter file would be far smaller than a 4B checkpoint. The API tag still says `base_model:adapter`.

(c) Training data. Card says: "Training data: u-10bei/sft_alfworld_trajectory_dataset_v5". The dataset has 2,502 rows (datasets-server). The card does not say a subset was held out. Dataset card: English task text in the examples; Hub language tags are `en` and `ja`. Provenance, dataset card: "The dataset programmatically generates expert trajectories without requiring an actual ALFWorld environment or a large language model." Template simulator and a rule-based expert. No generator model. The model card also says the adapter is for "ALFWorld (household tasks) and DBBench (database operations)." No DBBench dataset id is listed.

(d) Base model. Card says `Qwen/Qwen3-4B-Instruct-2507`. The id contains Instruct. It is an instruction-tuned model. This is not `Qwen/Qwen3-4B`, the base used for DynaGuard-4B.

(e) Epochs 2. Learning rate 2e-06. Max sequence length 2,048. Batch size not stated. Hardware not stated. The usage snippet loads the base in float16. The training line says "full precision base", and the tensor type on the Hub is BF16. No target modules.

(f) Evaluation. Not stated anywhere found. No benchmark number on the card.

(g) Output. A chat reply: the next assistant action in a household-task trajectory, including tool calls. It is not built to emit safe/unsafe. The name contains "guard". The card does not describe a detector.

Agreement with the classification note: yes. That note says the input is an agent trajectory, the output is a chat reply, and the training is a different skill from safety judgment.

### Discrepancies

1. Card says the repo holds adapter weights only. The files are a full 4,022,468,096-parameter BF16 model and `adapter_config.json` is missing.
2. Card objective mentions DBBench. The only dataset id is the ALFWorld v5 set.
3. Inventory methods are `lora|sft`. LoRA is stated. The inventory's SFT evidence quote is the dataset id `sft_alfworld...`, not the loss sentence. The loss sentence does support next-token training on assistant turns.
4. Other Hub repos reuse this card template with different epoch counts and datasets. They are not this upload.

### Confidence

Medium for the card's own training lines (LoRA, r=64, alpha=128, 2 epochs, 2e-6, assistant-turn loss, that dataset). Low for whether the uploaded tensors are the adapter or a merged model, because the card and the file list disagree. No second source describes this repo.

### Queries tried

1. `ryo-llm qwen3-4b-agent-trajectory-lora-alf-guard LoRA training`
2. `"qwen3-4b-agent-trajectory-lora-alf-guard" ryo-llm`
3. `u-10bei sft_alfworld_trajectory_dataset_v5 huggingface examples`
4. `ryo-llm github ALFWorld Qwen3 LoRA Unsloth`
5. `"alf-guard" Qwen3 LoRA ryo`
6. Hub model API, raw `adapter_config.json` (404), and the dataset size API

## tomg-group-umd/DynaGuard-4B

### Sources

Same paper, code, and dataset as DynaGuard-1.7B. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/tomg-group-umd__DynaGuard-4B__2026-10-06.md`. Hub API: https://huggingface.co/api/models/tomg-group-umd/DynaGuard-4B. Two safetensors shards, 4,411,424,256 BF16 parameters. No `adapter_config.json`.

### Training record

(a) Same statement as the 1.7B model. Paper: SFT for 1 epoch on the 40,000 + 40,000 mix, then GRPO on 11,000 samples. The recipe is not described as a separate run with different data. Card says: "The model was trained using Supervised Fine-Tuning (SFT) for one epoch, followed by GRPO."

(b) Not stated, for the same reason as the 1.7B model. The paper never says LoRA and never says full-weight updates. The upload is a full checkpoint of 4,411,424,256 BF16 parameters.

(c) Same mixture, same synthetic DynaBench provenance, same four safety sets. Card dataset id: `tomg-group-umd/DynaBench`.

(d) Card says `Qwen/Qwen3-4B`. Paper includes this size in "the Qwen3 family of instruction models." That id is the post-trained Qwen3-4B, not `Qwen/Qwen3-4B-Base` and not `Qwen/Qwen3-4B-Instruct-2507`. The uploaded parameter count (4,411,424,256) is the original Qwen3-4B count. The Instruct-2507 models in this batch are 4,022,468,096 parameters.

(e) SFT learning rate for 4B: the HTML bold span is `1e-5`, and a nested medium-weight span holds `, 2e-5, 4e-5`. The paper says the chosen value is bold, and the 1.7B row uses that pattern to mark only the chosen rate. Read that way, the 4B SFT rate is 1e-5. GRPO learning rate for 4B: the same markup, bold `1e-6` and medium `, 2e-6, 4e-6`. Batch size, rollouts, schedule, clipping, weight decay, and KL coefficient are in the shared rows, not per size: SFT batch 128, GRPO batch 48, rollouts 8. SFT is 1 epoch. GRPO epochs are not stated. Training hardware is not stated.

The paper's Table 4 ablation is specifically Qwen3-4B. Label-only SFT on 40k DynaBench reaches combined WildGuard+DynaBench F1 64.6. Label-plus-CoT SFT plus 11k GRPO reaches 71.7. The mixed safety/DynaBench recipe in Table 5 is the one the text says was used for the released models.

(f) Card table: DynaGuard-4B DynaBench F1 68.2, safety-task average F1 78.4. The paper's Table 3 includes this size on the wider benchmark list.

(g) Same verdict as the 1.7B model: PASS or FAIL on a user-written policy plus a dialogue, with an optional reasoning trace. It does not answer the user's request.

Agreement with the classification note: yes, same as the 1.7B row. Binary label, with an optional written reason in the chain-of-thought mode.

### Discrepancies

1. Same dataset-list gap as the 1.7B card: YAML names only DynaBench; the paper trains on a 50/50 mix with four safety sets.
2. Inventory methods `grpo|sft` and parent `Qwen/Qwen3-4B` match the paper and the card. Inventory datasets do not.
3. Do not treat this checkpoint as the same base as `Qwen/Qwen3-4B-Instruct-2507`. The parameter counts differ.

### Confidence

High for the shared recipe and the 4B learning-rate reading above. The 4B rate depends on reading the bold/medium HTML the same way as the unambiguous 1.7B row. Update scope is not stated.

### Queries tried

The six DynaGuard queries in the 1.7B section, plus the Hub API for `tomg-group-umd/DynaGuard-4B`. The 4B learning-rate row was read in the same appendix HTML as the 1.7B row.

## vominhmanh/qwen3-4b-vihsd

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/vominhmanh__qwen3-4b-vihsd__2026-10-06.md`. Live page: https://huggingface.co/vominhmanh/qwen3-4b-vihsd.
- Adapter card that points at this repo as the merged model: https://huggingface.co/vominhmanh/qwen3-4b-vihsd-lora.
- A different model, not this one: https://huggingface.co/vominhmanh/qwen3-4b-vihsd-dpo. It says DPO. It is not the training record for this repo.
- Dataset card: https://huggingface.co/datasets/vominhmanh/vihsd-explainable. 33,400 rows.
- Original labels: Luu, Nguyen, and Nguyen, "A Large-scale Dataset for Hate Speech Detection on Vietnamese Social Media Texts", https://arxiv.org/abs/2103.11528. Hub copy named by the adapter card: `htdung167/ViHSD`.
- No paper or GitHub repository was found for this fine-tune. Searches for a learning rate or target-module list returned other people's Unsloth notebooks, not this author. Those notebooks are not evidence.

### Training record

(a) Objective. Supervised next-token fine-tuning. Merged-model card says: "Objective: Causal language modeling (NLL loss)" and "Framework: Unsloth + TRL `SFTTrainer`" and "Prompt format: Chat-style (user → assistant JSON response)". Adapter card says: "Method: Supervised Fine-Tuning (SFT)" and "Objective: Cross-entropy (NLL)". The DPO dataset and the DPO model are a later repo. This card does not say this upload was trained with DPO.

(b) Parameter-update scope. The merged-model card says LoRA, then merged. It says "LoRA-finetuned and merged version", "Fine-tuning method: LoRA", "Trainable parameters: ~0.8% of total parameters", "r = 16", "alpha = 32", "dropout = 0", "Precision: bf16", "Optimizer: AdamW (8-bit)". It does not say the base was 4-bit. Target modules are not stated. The adapter card, which says this repo is the merged model, says "Quantization: `4-bit` base model" and the same rank and alpha. 4-bit base plus LoRA is QLoRA. The two cards disagree on that point. Hub files for this repo are two full shards, 4,022,468,096 BF16 parameters, no `adapter_config.json`, which matches a merged upload. The Hub tag still says `base_model:adapter`.

(c) Training data. Card: `vominhmanh/vihsd-explainable`, train 24,048, validation 2,672, test 6,680. Dataset card: 33,400 rows, same splits as ViHSD. Language: Vietnamese. Provenance, dataset card: "Original labels from `htdung167/ViHSD`. `explanation` and `evidence` were generated using an LLM (GPT-4o-mini on Azure) as a teacher, and reviewed/curated by authors." The 2021 paper says the labels are human annotations of social-media comments, three classes CLEAN, OFFENSIVE, and HATE, 33,400 comments. The explanations are not from that paper.

(d) Base model. Card says `unsloth/Qwen3-4B-Instruct-2507` and "Type: Instruction-tuned causal language model." It is an instruction-tuned model.

(e) Epochs 2. Sequence length 512. Learning rate not stated. Batch size not stated. Hardware not stated. Optimizer AdamW 8-bit is stated. That is the optimizer bit-width, not a statement that the base weights were 4-bit.

(f) Evaluation. Card: macro F1 on 6,680 test samples, same prompt and JSON parser for the base and the fine-tune. Base Qwen3-4B-Instruct-2507 0.5085. This model 0.6370. The adapter card rounds those to ~0.51 and ~0.64 and says explanation quality was only checked qualitatively.

(g) Output. A verdict. Card says the model generates JSON with `label` CLEAN, OFFENSIVE, or HATE, a short Vietnamese `explanation`, and `evidence` spans copied from the text. It reads one piece of Vietnamese text. It does not write a chat reply to the author of that text. It is built to detect hate speech and offensive language under the ViHSD label rules.

Agreement with the classification note: yes. That note says the input is a piece of text and the output is reasoning and a verdict, with labels CLEAN, OFFENSIVE, and HATE.

### Discrepancies

1. Merged-model card says LoRA and bf16 and does not say 4-bit. Adapter card says the base was 4-bit. Inventory methods are `lora`, which matches the merged card and misses the 4-bit sentence.
2. Hub relation tag is `adapter`. The card says the adapter was merged, and the files are a full 4B checkpoint.
3. A sibling repo, `vominhmanh/qwen3-4b-vihsd-dpo`, is DPO on a different dataset (`vominhmanh/vihsd-explainable-dpo`). That is not this model's training.

### Confidence

Medium. SFT, rank 16, alpha 32, two epochs, the dataset, and the merged upload are stated on the model card. Whether the base was 4-bit during training depends on which of the author's two cards is followed. No learning rate and no paper.

### Queries tried

1. `vominhmanh qwen3-4b-vihsd LoRA SFTTrainer ViHSD explainable`
2. `"vominhmanh" ViHSD Qwen3 explainable hate speech fine-tuning`
3. `vominhmanh vihsd-explainable dataset GPT-4o explanation htdung167`
4. `ViHSD Vietnamese Hate Speech Detection Luu 2021 dataset human annotation`
5. `vominhmanh qwen3-4b-vihsd learning rate batch size target_modules github`
6. Fetched the merged card, the adapter card, the DPO card, and the explainable dataset card

## Patterns in this batch

Two of the five rows are one guardian paper. DynaGuard-1.7B and DynaGuard-4B are supervised fine-tuning for one epoch and then GRPO, on the same 80,000-example mix, with a lower learning rate at 4B than at 1.7B. The paper never says whether that update touched every weight. Both uploads are full checkpoints, not adapter repos.

TinySafe and the ViHSD model are both verdict models on top of Qwen3-4B-Instruct-2507. TinySafe's gradient step is QLoRA SFT on labels written by Claude Sonnet 4.6, with some unsafe synthetic text from DeepSeek and Grok. The ViHSD model is SFT on human CLEAN/OFFENSIVE/HATE labels plus GPT-4o-mini explanations. Its own merged card says LoRA; the adapter card says the base was 4-bit.

The remaining repo is not a safety detector. `ryo-llm/qwen3-4b-agent-trajectory-lora-alf-guard` is a LoRA for household-task actions. The word "guard" is in the name. The card says the files are an adapter; the Hub files are a full 4B checkpoint.

The inventory's method words are in the right neighborhood, and its dataset cells are not. DynaGuard's inventory row drops the four safety sets the paper trained on. TinySafe's inventory row keeps BeaverTails from the card YAML, which the training script never loads. The ViHSD inventory row says LoRA and does not record the adapter card's 4-bit line.
