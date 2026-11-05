# Batch 11: how five medical models were trained

Cached cards read: newest README under `revision_3_experiments/hf_inventory/cache/readmes/` (2026-10-05). Inventory row: `revision_3_experiments/hf_inventory/results/medical/2026-10-06/kept.csv`. Hub file lists: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__004.csv` (Baize), `2026-10-05__013.csv` (the three mlxha repos), `2026-10-05__016.csv` (vinhnguyenxu). Saved trainer files were read from the Hub on 7 Oct 2026: `training_args.bin` (unzipped `training_args/data.pkl`) and `trainer_state.json` / `all_results.json`. None of the five repositories contains `adapter_config.json`.

The three `mlxha` checkpoints are one series. They share one training program (`open_r1.configs.GRPOConfig`), one system prompt, and the same three reward names. What changes is the question subset, the fraction of an epoch, the learning rate, the batch, the number of processes, and the reward weights. Those differences are in the table below and in sections 2–4.

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Task trained for | Language | Matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit | none (model card and dataset card) | supervised fine-tuning | LoRA (rank not stated); upload is a full BF16 file, no adapter file | Baize-TCM-Corpus V3: 157,438 Chinese question-answer rows; card says collated and proofread; writer not stated | Qwen/Qwen3-8B (post-trained) | open question answering | zh | yes |
| mlxha/Qwen3-8B-grpo-medmcqa | code (saved GRPO config) | GRPO | full weights; no LoRA fields in the saved config | mlxha/medmcqa-grpo train: 182,822 English exam items; same ids as MedMCQA; human-written | Qwen/Qwen3-8B (post-trained) | multiple-choice exam answering | en | yes |
| mlxha/Qwen3-8B-grpo-medmcqa-medi70 | code (saved GRPO config) | GRPO | full weights; no LoRA fields in the saved config | mlxha/medmcqa-grpo-meditron70b: 16,885 English exam items, every row labeled Advanced Knowledge; name contains meditron70b; a checked id is a MedMCQA item | Qwen/Qwen3-8B (post-trained) | multiple-choice exam answering | en | yes |
| mlxha/Qwen3-8B-grpo-medmcqa-v2 | code (saved GRPO config) | GRPO | full weights; no LoRA fields in the saved config | same Hub set as the plain run: 182,822 train rows | Qwen/Qwen3-8B (post-trained) | multiple-choice exam answering | en | yes |
| vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical | code (saved SFT config) | supervised fine-tuning (negative log likelihood) | full weights; no LoRA fields in the saved config | trainer counted 49,704 rows; card prose names two reasoning sets; YAML names mamachang/medical-reasoning (3,702 rows) | Qwen/Qwen3-8B (post-trained) | reasoning traces | en and zh named; the 49,704-row mix is not identified | partly |

## 1. DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/DigitalIntelligenceCenter-of-ICMM__Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit__2026-10-05.md`. Title names this repo. Language tag `zh`. Base `Qwen/Qwen3-8B`.
- `config.json`, cached 2026-10-06: `revision_3_experiments/hf_inventory/cache/configs/DigitalIntelligenceCenter-of-ICMM__Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit__2026-10-06.json`. Keys `unsloth_fixed` and `unsloth_version`.
- Hub model API, retrieved 7 Oct 2026: https://huggingface.co/api/models/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit . Created 2025-10-07. Siblings are four `model-*-of-00004.safetensors` shards. No `adapter_config.json`. `safetensors.parameters.BF16` is 8,190,735,360.
- Dataset card: https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3/raw/main/README.md . The two JSON files on that repo, concatenated, parse as 157,438 objects (counted 7 Oct 2026).
- Sibling 0.6B card, not this repo: `revision_3_experiments/hf_inventory/cache/readmes/DigitalIntelligenceCenter-of-ICMM__Baize-Traditional-Chinese-Medicine-Large-Language-Model__2026-10-05.md`. It names LLaMA-Factory. This V3 card does not.
- Institute news, 中国中医科学院中药研究所, https://icmm.ac.cn/sndt/content_3154.html . Says a “白泽中医药” agent platform went live. It does not name this repo or a training method.
- Xu et al., “Baize: An Open-Source Chat Model with Parameter-Efficient Tuning on Self-Chat Data,” https://arxiv.org/html/2304.01196v4/ . That paper fine-tunes LLaMA. It does not name this repo. It is a different model that happens to use the word Baize.
- No GitHub repository and no paper were found that name `Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit`.

### Training record

**(a) Objective.** Card says: “基于通用大模型在 **157,438 条高质量中医问答语料** 上进行指令微调（Supervised Fine-Tuning）.” That is supervised fine-tuning on instruction pairs. The card does not say preference optimization, reinforcement learning, or continued pre-training.

**(b) Parameter-update scope.** Card table says: “训练方式 | LoRA”. Rank, alpha, and target modules are not stated anywhere found. Whether the adapter was merged is not stated. The Hub repo has four full BF16 shards and no `adapter_config.json`. The parameter count, 8,190,735,360 BF16, is the same count as `Qwen/Qwen3-8B`. `config.json` says `"unsloth_fixed": true` and `"unsloth_version": "2025.8.9"`. Those keys say Unsloth wrote the config. They do not state the LoRA rank. The 0.6B sibling card says “训练软件 | LLaMA-Factory”. This V3 card does not.

**(c) Training data.** Card YAML dataset id: `DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3`. Dataset card says: “语料数量：157,438 条”, “语言：中文”, “格式：问答对（QA Pair）”, and “157,438 条 经过整理与校对的问答对”. The concatenated JSON files contain 157,438 objects with keys `instruction`, `input`, `output`, and `system`. `input` and `system` are empty on all 157,438 rows. The card’s scope list is 中医基础理论, 中药学, 方剂学, 诊断学, 针灸推拿, 经典医籍, and 临床实践. The card does not say whether a person or a model wrote the answers. The example printed on the dataset card is a Chinese question about the broad and narrow transcriptome, not a classical formula question. Of the 157,438 instructions, 157,437 contain Chinese characters. One instruction is English: “Tritrophic interactions involve which three levels of organisms”, and its `output` is an English sentence about producers, herbivores, and predators. 3,176 rows contain at least 40 Latin letters, usually an English species or chemical name inside a Chinese question, for example “根瘤菌与印楝内生菌共生于 Artemisia annua 时对青蒿素含量有何促进作用？”

**(d) Base model.** Card YAML: `Qwen/Qwen3-8B`. Qwen’s card, https://huggingface.co/Qwen/Qwen3-8B/raw/main/README.md , says “Training Stage: Pretraining & Post-training” and `base_model: Qwen/Qwen3-8B-Base`. It describes instruction following and a thinking-mode switch. This id is the post-trained checkpoint, not `Qwen/Qwen3-8B-Base`.

**(e) Hyperparameters.** Epochs, learning rate, batch size, and GPU type are not stated anywhere found. The card table says “上下文长度 | 2048 tokens”. `config.json` has `"max_position_embeddings": 40960`, which is the Qwen3 default, and `"torch_dtype": "bfloat16"`.

**(f) Evaluation.** Not stated anywhere found. No benchmark table is on the card.

**(g) Task and language.** The training rows are open question-answer pairs (`instruction` to `output`). The card lists uses: 中医智能问答, 中医药知识辅助诊断, 医学生教学与考试辅助, and local deployment. The only inference example is Chinese: “问题：气虚的主要症状有哪些？\n答案：”. Language tag on the card: `zh`. English use is not shown in the inference example. One of the 157,438 training instructions is English, as quoted above.

### Discrepancies

1. The card says LoRA. The upload is four full BF16 shards, 8,190,735,360 parameters, and no `adapter_config.json`. Rank and merge are not stated.
2. The card’s load example uses `torch.float16` and the placeholder `your-username/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit`. The Hub dtype is BF16.
3. The card table says context length 2048. `config.json` says `max_position_embeddings` 40960.
4. The dataset link in the card points at `https://huggingface.co/datasets/your-username/baize-tcm-corpus-v3`. The YAML id is `DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3`.
5. `config.json` carries Unsloth keys. The 0.6B sibling card says LLaMA-Factory. This V3 card names neither tool in prose.
6. Inventory `methods` is `lora|sft`, which matches the card’s two statements. Inventory `datasets` matches the YAML id.

### Confidence

Medium. The card states supervised fine-tuning with LoRA on 157,438 Chinese question-answer rows, and that row count is the length of the published JSON. No training script states the rank, the learning rate, or that the adapter was merged into the full file that was uploaded.

### Queries tried

- `Baize Traditional Chinese Medicine Large Language Model V3 ICMM 白泽 中医药`
- `DigitalIntelligenceCenter-of-ICMM Baize-TCM LoRA supervised fine-tuning`
- `"白泽中医药" 大语言模型 中国中医科学院 DigitalIntelligenceCenter`
- `"Baize-TCM" OR "白泽中医药大模型语料库" LoRA Unsloth OR LLaMA-Factory 论文`
- Hugging Face model API and dataset README for the V3 corpus
- https://icmm.ac.cn/sndt/content_3154.html
- arXiv 2304.01196 (Xu et al. Baize; a different model) and arXiv 2411.11027 (BianCang; a different TCM model)
- Concatenated corpus JSON: row count, empty `input`/`system`, and Chinese vs English instructions

## 2. mlxha/Qwen3-8B-grpo-medmcqa

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/mlxha__Qwen3-8B-grpo-medmcqa__2026-10-05.md`. Names this repo in the pipeline example.
- Saved config: https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa/resolve/main/training_args.bin . Unzipped `training_args/data.pkl` is class `open_r1.configs.GRPOConfig`.
- Saved logs: https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa/resolve/main/trainer_state.json and `all_results.json`. `all_results.json` says `"train_samples": 182822`.
- Hub model API: https://huggingface.co/api/models/mlxha/Qwen3-8B-grpo-medmcqa . Created 2025-05-08. Four BF16 shards, 8,190,735,360 parameters. No `adapter_config.json`. Pickle imports listed on the file tree include `open_r1.configs.GRPOConfig`.
- Dataset API: https://huggingface.co/api/datasets/mlxha/medmcqa-grpo . Train 182,822, validation 4,183, test 6,150. Language tag `en`. README content is empty.
- MedMCQA dataset card: https://huggingface.co/datasets/openlifescienceai/medmcqa . Train row 0 has id `e9ad821a-c438-4965-9f77-760819dfa155`, the same id and question as train row 0 of `mlxha/medmcqa-grpo` (datasets-server, 7 Oct 2026).
- Pal, Umapathi, and Sankarasubbu, PMLR 174, 2022: https://proceedings.mlr.press/v174/pal22a.html and the dataset card text “AIIMS & NEET PG entrance exam MCQs”. The mlxha card does not cite this paper. The DeepSeekMath citation on the mlxha card is the GRPO method paper (arXiv 2402.03300), not a paper about this checkpoint.
- W&B link on the card: https://wandb.ai/alexs-team/reasoning/runs/c9405090-f026-471a-b761-4bc72236aefe . No public report for `alexs-team` was found. GitHub search for `mcq_accuracy_reward` returned no code. No mlxha GitHub repository was found.
- Shared program for sections 2–4: https://github.com/huggingface/open-r1/blob/main/src/open_r1/grpo.py . That file builds a `GRPOTrainer` and can pass a PEFT config. It does not name these three repos.

### Training record

**(a) Objective.** Card says: “This model was trained with GRPO”. The saved object is `open_r1.configs.GRPOConfig`. `trainer_state.json` logs `kl`, `clip_ratio/*`, and `rewards/mcq_accuracy_reward`, `rewards/format_reward`, and `rewards/tag_count_reward`. That is reinforcement learning with a reward (GRPO), not supervised fine-tuning. The repo name contains `grpo`; the card and the saved class say GRPO as well. `loss_type` in the saved config is `bnpo`. `beta` is 0.04. `num_iterations` is 1. `epsilon` is 0.2. `scale_rewards` is true. `num_generations` is 8. `use_vllm` is true.

**(b) Parameter-update scope.** The saved `GRPOConfig` has no LoRA rank, alpha, or target-module fields. `deepspeed` on the config object is null. `distributed_state.distributed_type` is `DEEPSPEED`, `num_processes` is 4, and `deepspeed_plugin.zero_stage` is 3, with optimizer offload `none` and parameter offload `none`. `hf_ds_config` says `train_batch_size` 64, `train_micro_batch_size_per_gpu` 1, and `stage3_gather_16bit_weights_on_model_save` true. A nested `dschf.config` copy says `train_micro_batch_size_per_gpu` 1 as well on this run. The upload is four BF16 shards, 8,190,735,360 parameters, and no `adapter_config.json`. The card does not say “full fine-tuning” or “LoRA”.

**(c) Training data.** Card YAML: `mlxha/medmcqa-grpo`. Dataset API: 182,822 train, 4,183 validation, 6,150 test. Columns include `id`, `question`, `opa`, `opb`, `opc`, `opd`, `cop`, `choice_type`, `exp`, `subject_name`, `topic_name`, `problem`, and `solution`. Train row 0, datasets-server: id `e9ad821a-c438-4965-9f77-760819dfa155`, the same id as `openlifescienceai/medmcqa` train row 0, question “Chronic urethral obstruction due to benign prismatic hyperplasia…”, `solution` “C”. The `problem` field is that question plus “Options:” A–D. MedMCQA’s card says: “The training set of MedMCQA consists of all the collected mock & online test series, whereas the test set consists of all AIIMS PG exam MCQs (years 1991-present). The development set consists of NEET PG exam MCQs (years 2001-present).” Those are human-written exam items. Language tag on `mlxha/medmcqa-grpo`: `en`. The mlxha README does not say this. The match is the shared id, the shared question text, and the split sizes 182,822 / 6,150 / 4,183, which the MedMCQA card prints as Train / Test / Valid.

**(d) Base model.** Card YAML: `Qwen/Qwen3-8B`. Same post-trained checkpoint as in section 1. Qwen’s card says “Training Stage: Pretraining & Post-training”.

**(e) Hyperparameters.** From `training_args/data.pkl` for this repo: learning rate 3e-6, `num_train_epochs` 0.25, cosine schedule, warmup ratio 0.1, `per_device_train_batch_size` 1, gradient accumulation 16, 4 processes, bf16 true, AdamW (`adamw_torch`), seed 42, gradient checkpointing true, max prompt length 2048, max completion length 8192, temperature 0.9, top-p 1.0, top-k 50. `trainer_state.json`: epoch 0.24999179529815888, global step 5713, `max_steps` 5713, `train_batch_size` 1. `all_results.json`: `train_runtime` 190832.2518 seconds, `train_samples` 182822. `eval_strategy` is `no`. GPU product name is not stated. The logging directory is `data/Qwen3-8B-grpo-medmcqa/runs/May09_17-24-54_qwen3-8b-0-5`. Reward weights in the saved config: `[1.0, 0.25, 0.25]`. The file does not say which weight belongs to which of the three reward names.

System prompt in the saved config: “You are a helpful AI Assistant, designed to provided well-reasoned and detailed responses. You FIRST think about the reasoning process as an internal monologue and then provide the user with the answer. The reasoning process and answer are enclosed within <think> </think> and <answer> </answer> tags, respectively. Respond in the following format: <think> ... </think> <answer> X is the correct answer. </answer>”.

**(f) Evaluation.** `eval_strategy` is `no`. `trainer_state.json` has no `eval_` keys. The log is the training reward on generated completions, not a score on the 6,150-row test split. At step 5713 the log says `rewards/mcq_accuracy_reward/mean` 0.59375, `rewards/format_reward/mean` 0.0, and `rewards/tag_count_reward/mean` 1.0. Those are the last logged training batch, not a test accuracy.

**(g) Task and language.** The prompts are four-option medical exam questions. The system prompt asks for a reasoning block and then “X is the correct answer.” The logged reward name is `mcq_accuracy_reward`. Language of the dataset tag and of row 0: English.

### What is shared with medi70 and v2

Sections 3 and 4 use the same class, the same system prompt, the same three reward names, `num_generations` 8, max prompt 2048, max completion 8192, temperature 0.9, beta 0.04, epsilon 0.2, `loss_type` `bnpo`, cosine schedule, warmup ratio 0.1, bf16, AdamW, seed 42, gradient checkpointing, vLLM, ZeRO stage 3, and `eval_strategy` `no`. The base id is `Qwen/Qwen3-8B` for all three. TRL on all three cards: 0.18.0.dev0. Transformers: 4.52.0.dev0.

### Discrepancies

1. Inventory `methods` is `grpo` and `datasets` is `mlxha/medmcqa-grpo`. That matches the card and the saved class. The inventory does not record the 0.25 epoch or the reward weights.
2. The nested `dschf` micro-batch and the `hf_ds_config` micro-batch both say 1 on this run, which matches `per_device_train_batch_size` 1. On medi70 and v2 those two copies disagree; see those sections.
3. The card’s W&B page was not readable as a public report. The numbers above are from `training_args.bin` and `trainer_state.json`, not from W&B.

### Confidence

High for the objective, the MedMCQA identity of the training split, and the hyperparameters in the saved config. The function body of `mcq_accuracy_reward` was not found, and the saved weight list does not name which reward gets 1.0.

### Queries tried

- `mlxha Qwen3-8B-grpo-medmcqa GRPO training medmcqa`
- `mlxha github medmcqa-grpo open-r1 GRPO Qwen3`
- `"medmcqa-grpo-meditron70b" OR "Qwen3-8B-grpo-medmcqa-v2" mlxha`
- `mcq_accuracy_reward format_reward tag_count_reward open-r1 github`
- `"mcq_accuracy_reward" github code search`
- `site:wandb.ai alexs-team reasoning Qwen3-8B-grpo-medmcqa`
- `Pal 2022 MedMCQA 182822 mlxha`
- Hub `training_args.bin`, `trainer_state.json`, dataset API, and datasets-server row 0 compared with `openlifescienceai/medmcqa`

## 3. mlxha/Qwen3-8B-grpo-medmcqa-medi70

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/mlxha__Qwen3-8B-grpo-medmcqa-medi70__2026-10-05.md`.
- Saved config: https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-medi70/resolve/main/training_args.bin . Class `open_r1.configs.GRPOConfig`.
- Saved logs: https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-medi70/resolve/main/all_results.json (`train_samples` 16885) and `trainer_state.json`.
- Dataset API: https://huggingface.co/api/datasets/mlxha/medmcqa-grpo-meditron70b . Train only, 16,885 rows. README content is empty.
- datasets-server statistics, 7 Oct 2026: https://datasets-server.huggingface.co/statistics?dataset=mlxha/medmcqa-grpo-meditron70b&config=default&split=train . `difficulty` has one value, `Advanced Knowledge`, on all 16,885 rows. `solution` frequencies: A 6,604, B 3,833, C 3,511, D 2,937.
- datasets-server row 0: id `73515f05-e947-4801-8077-3abdeca95c84`, question starting “Characteristics of Remifentanyl”, `solution` “C”. That same id is on the `openlifescienceai/medmcqa` viewer (the remifentanil item, `cop` class 2, which is option C).
- W&B link on the card: https://wandb.ai/alexs-team/reasoning/runs/a353e548-7458-41bd-a49d-4ba5a41cdc37 . Not retrieved as a public report.
- The name contains `meditron70b` and `medi70`. No paper or script was found that says Meditron-70B wrote or filtered these rows. Chen et al., arXiv 2311.16079, is the Meditron paper. It does not name this dataset.

### Training record

**(a) Objective.** Card says: “This model was trained with GRPO”. Saved class: `GRPOConfig`. Same reward names in `trainer_state.json` as section 2. Reward weights in this file: `[1.0, 0.1, 0.1]`, not `[1.0, 0.25, 0.25]`.

**(b) Parameter-update scope.** No LoRA fields in the saved config. DeepSpeed ZeRO stage 3, `num_processes` 6, offload `none`. `hf_ds_config.train_batch_size` is 768 and `train_micro_batch_size_per_gpu` is 8, which matches `per_device_train_batch_size` 8 times 6 processes times gradient accumulation 16. The nested `dschf.config.train_micro_batch_size_per_gpu` is 1. Upload: four BF16 shards, 8,190,735,360 parameters, no `adapter_config.json` (Hub API, cache `2026-10-05__013.csv`).

**(c) Training data.** Card says the dataset is `mlxha/medmcqa-grpo-meditron70b`. 16,885 train rows. Columns: `id`, `question`, `opa`, `opb`, `opc`, `opd`, `cop`, `difficulty`, `problem`, `solution`. There is no column of model-written text. `solution` is a single letter A–D. Every row’s `difficulty` is the string `Advanced Knowledge`. The checked id `73515f05-e947-4801-8077-3abdeca95c84` is a MedMCQA exam item. A join of all 16,885 ids onto MedMCQA was not run. The dataset card does not say how the 16,885 rows were chosen, and it does not say that Meditron-70B generated them. Language of row 0: English. The dataset API has no language tag.

**(d) Base model.** Card YAML: `Qwen/Qwen3-8B`. Post-trained, as in section 1.

**(e) Hyperparameters.** Saved config: learning rate 5e-6, `num_train_epochs` 1.0, `per_device_train_batch_size` 8, gradient accumulation 16, 6 processes, otherwise the shared settings in section 2. `trainer_state.json`: epoch 0.9946714031971581, global step 175, `train_batch_size` 8. `all_results.json`: `train_runtime` 39419.1987 seconds, `train_samples` 16885. Logging directory: `data/Qwen3-8B-grpo-medmcqa-medi70/runs/May27_00-08-12_grpo-qwen3-8b-medi70-0-0`.

**(f) Evaluation.** `eval_strategy` is `no`. At step 175 the training log says `rewards/mcq_accuracy_reward/mean` 0.48854167461395265, `rewards/format_reward/mean` 0.9997395873069763, and `rewards/tag_count_reward/mean` 0.9995442748069763. That is the last logged training step, not a test score.

**(g) Task and language.** Same exam-letter task and the same system prompt as section 2. Dataset language of the checked row: English.

### What differs from the plain run and from v2

| | plain | medi70 | v2 |
| --- | --- | --- | --- |
| Hub dataset | `mlxha/medmcqa-grpo` | `mlxha/medmcqa-grpo-meditron70b` | `mlxha/medmcqa-grpo` |
| Train rows | 182,822 | 16,885, all labeled Advanced Knowledge | 182,822 |
| Epochs in the config | 0.25 | 1.0 | 0.5 |
| Learning rate | 3e-6 | 5e-6 | 2e-6 |
| Per-device batch | 1 | 8 | 4 |
| Processes | 4 | 6 | 4 |
| DeepSpeed global batch in `hf_ds_config` | 64 | 768 | 256 |
| Reward weights | 1.0, 0.25, 0.25 | 1.0, 0.1, 0.1 | 1.0, 0.1, 0.1 |
| Steps finished | 5,713 | 175 | 2,857 |

### Discrepancies

1. Inventory `methods` is `grpo` and `datasets` is `mlxha/medmcqa-grpo-meditron70b`. That matches the card.
2. The name contains `meditron70b`. No source states that Meditron-70B wrote the questions, the letters, or the difficulty label. The checked row is a MedMCQA item, and `solution` is the letter C.
3. `hf_ds_config` micro-batch is 8. The nested `dschf.config` micro-batch is 1.

### Confidence

High for GRPO, the 16,885-row set, and the hyperparameters. Low for what “meditron70b” means in the dataset name, because no source states a filter or a generator.

### Queries tried

- `mlxha Qwen3-8B-grpo-medmcqa-medi70`
- `"medmcqa-grpo-meditron70b" OR "Qwen3-8B-grpo-medmcqa-v2"`
- `"Advanced Knowledge" medmcqa grpo meditron difficulty subset`
- datasets-server statistics and row 0 for `mlxha/medmcqa-grpo-meditron70b`
- Same id `73515f05-e947-4801-8077-3abdeca95c84` on the `openlifescienceai/medmcqa` viewer
- Meditron paper arXiv 2311.16079
- Saved `training_args.bin` and `trainer_state.json` for this repo
- W&B run `a353e548-7458-41bd-a49d-4ba5a41cdc37`

## 4. mlxha/Qwen3-8B-grpo-medmcqa-v2

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/mlxha__Qwen3-8B-grpo-medmcqa-v2__2026-10-05.md`. Dataset in the YAML is `mlxha/medmcqa-grpo`, the same id as the plain run.
- Saved config: https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/resolve/main/training_args.bin . Class `open_r1.configs.GRPOConfig`.
- Saved logs: https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa-v2/resolve/main/all_results.json (`train_samples` 182822) and `trainer_state.json`.
- W&B link: https://wandb.ai/alexs-team/reasoning/runs/37495502-90ff-46e9-b734-a5e8db41c00e . Not retrieved as a public report.
- Dataset identity: same Hub dataset as section 2. This card does not describe a second corpus.

### Training record

**(a) Objective.** Card says: “This model was trained with GRPO”. Saved class `GRPOConfig`. Same three reward names. Reward weights `[1.0, 0.1, 0.1]`, the same list as medi70 and not the plain run’s `[1.0, 0.25, 0.25]`.

**(b) Parameter-update scope.** No LoRA fields. DeepSpeed ZeRO stage 3, `num_processes` 4, offload `none`. `hf_ds_config.train_batch_size` is 256 and `train_micro_batch_size_per_gpu` is 4, matching per-device batch 4, 4 processes, and accumulation 16. Nested `dschf.config.train_micro_batch_size_per_gpu` is 1. Upload: four BF16 shards, 8,190,735,360 parameters, no `adapter_config.json`.

**(c) Training data.** Same dataset id and the same 182,822 / 4,183 / 6,150 splits as section 2. `all_results.json` says `train_samples` 182822. Provenance is the MedMCQA exam set, as in section 2. The config difference is not a different corpus.

**(d) Base model.** `Qwen/Qwen3-8B`, post-trained.

**(e) Hyperparameters.** Saved config: learning rate 2e-6, `num_train_epochs` 0.5, `per_device_train_batch_size` 4, gradient accumulation 16, 4 processes. `trainer_state.json`: epoch 0.5000711074159565, global step 2857, `train_batch_size` 4. `all_results.json`: `train_runtime` 242159.7767 seconds. Logging directory: `data/Qwen3-8B-grpo-medmcqa-v2/runs/May16_14-02-30_grpo-qwen3-8b-0-0`. Shared lengths, temperature, beta, and the system prompt are in section 2.

**(f) Evaluation.** `eval_strategy` is `no`. At step 2857 the training log says `rewards/mcq_accuracy_reward/mean` 0.763671875, `rewards/format_reward/mean` 1.0, and `rewards/tag_count_reward/mean` 1.0. That is the last logged training step.

**(g) Task and language.** English multiple-choice exam items, with the think/answer system prompt from section 2.

### Discrepancies

1. Inventory `methods` is `grpo` and `datasets` is `mlxha/medmcqa-grpo`. That matches this card. The inventory row does not say that v2 used a different learning rate and a half epoch on that same set.
2. `hf_ds_config` micro-batch is 4. The nested `dschf.config` micro-batch is 1.
3. The plain run’s format reward at the last logged step is 0.0. This run’s last logged format reward is 1.0. Both numbers are training logs. The card does not discuss them.

### Confidence

High. The card, the dataset id, and the saved config agree that this is a second GRPO run on `mlxha/medmcqa-grpo`, with learning rate 2e-6 and half an epoch.

### Queries tried

- `Qwen3-8B-grpo-medmcqa-v2 mlxha`
- `"medmcqa-grpo-meditron70b" OR "Qwen3-8B-grpo-medmcqa-v2"`
- Hub `training_args.bin` and `trainer_state.json` for this repo
- Dataset API for `mlxha/medmcqa-grpo` (same id as the plain run)
- W&B run `37495502-90ff-46e9-b734-a5e8db41c00e`
- `open_r1.configs.GRPOConfig` in the pickle header
- Comparison of the three `training_args.bin` files (they are not byte-identical)
- GitHub `huggingface/open-r1` `src/open_r1/grpo.py`

## 5. vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/vinhnguyenxu__OpenR1-Distill-Qwen3-8B-Medical__2026-10-05.md`. The prose names two datasets. The YAML `datasets` field is `mamachang/medical-reasoning`.
- Saved config: https://huggingface.co/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical/resolve/main/training_args.bin . Class `open_r1.configs.SFTConfig`.
- Saved logs: https://huggingface.co/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical/resolve/main/all_results.json and `trainer_state.json`. `all_results.json` says `"epoch": 5.0` and `"train_samples": 49704`.
- Hub model API: https://huggingface.co/api/models/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical . Created 2025-10-27. Four safetensors shards. `safetensors.parameters.BF16` is 8,190,735,360. No `adapter_config.json`. Tag `sft`. Also a GGUF file `OpenR1-Distill-Qwen3-8B-Medical-F16.gguf`.
- `mamachang/medical-reasoning` file `instruction-dataset-w-reasoning2.json`, downloaded 7 Oct 2026: 3,702 objects with keys `instruction`, `input`, `output`. No README in the dataset API siblings. Created 2023-11-08.
- `FreedomIntelligence/medical-o1-reasoning-SFT` size API: English config 19,704 rows, Chinese config 20,171 rows, English mix 24,887, Chinese mix 25,358. Dataset card says the set “is constructed using GPT-4o”. Paper: Chen et al., https://arxiv.org/abs/2412.18925 . That paper’s training section fine-tunes Llama-3.1 and Qwen2.5 for HuatuoGPT-o1. It does not name this repo.
- `Intelligent-Internet/II-Medical-Reasoning-SFT` README: “The training dataset comprises 2,197,741 samples”, including synthetic answers from Qwen3-235B-A22B and filtered R1 traces. It does not name this repo.
- open-r1 SFT script: https://github.com/huggingface/open-r1/blob/main/src/open_r1/sft.py . The docstring example uses learning rate 4e-5, 5 epochs, max sequence length 32768, per-device batch 2, and `use_liger_kernel`, on `open-r1/Mixture-of-Thoughts`, not on a medical set. The script sets `train_samples` to the length of the train split.
- W&B link on the card: https://wandb.ai/vinh-nguyenxv-bosch/huggingface/runs/99mefmqa . Not retrieved as a public report. No GitHub repository under the name vinhnguyenxu was found for this model. Featherless, https://featherless.ai/models/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical , repeats the card.

### Training record

**(a) Objective.** Card says: “This model was trained with SFT.” Saved `SFTConfig.loss_type` is `nll`. `trainer_state.json` logs `loss` and `learning_rate` only. It does not log `kl` or rewards. That is supervised next-token training. The repo name contains `Distill` and `OpenR1`. The open-r1 README uses “SFT distillation” for supervised training on reasoning traces. This saved config does not set a distillation loss other than `nll`. The name is not, by itself, the training objective.

**(b) Parameter-update scope.** The saved `SFTConfig` has no LoRA rank or alpha. `use_liger_kernel` is true. `packing` is false. `packing_strategy` is `bfd`. `max_length` is 32768. `dataset_text_field` is `text`. DeepSpeed: `distributed_type` `DEEPSPEED`, `num_processes` 1, ZeRO stage 3, `offload_optimizer_device` `cpu`, `offload_param_device` `none`. `hf_ds_config.train_batch_size` is 4 and `train_micro_batch_size_per_gpu` is 2, matching per-device batch 2 and gradient accumulation 2 on one process. Nested `dschf.config.train_micro_batch_size_per_gpu` is 1. Upload: four BF16 shards, 8,190,735,360 parameters, no `adapter_config.json`. The Hub page also prints a 308k parameter total; that number is not the BF16 shard count.

**(c) Training data.** Three statements do not match each other.

- Card prose: “fine-tuned version of Qwen/Qwen3-8B on two merged datasets: FreedomIntelligence/medical-o1-reasoning-SFT … Intelligent-Internet/II-Medical-Reasoning-SFT”.
- Card YAML and the Hub tag: `mamachang/medical-reasoning`. That file has 3,702 rows. Row 0 `instruction` is “Please answer with one of the option in the bracket. Write reasoning in between <analysis></analysis>. Write answer in between <answer></answer>.” The `input` is an English clinical vignette. Provenance of those 3,702 rows is not stated on the dataset repo.
- `all_results.json`: `train_samples` 49704. `trainer_state.json`: 62,130 steps and epoch 5.0. With global batch 4, 49,704 times 5 divided by 4 is 62,130, so the trainer’s row count and the step count agree with each other.

Published sizes: medical-o1 English 19,704; medical-o1 English plus Chinese 39,875; II-Medical-Reasoning-SFT 2,197,741; mamachang 3,702. None of those counts is 49,704. medical-o1’s card says the English reasoning text was built with GPT-4o. II-Medical’s README says the 2,197,741 rows mix public medical reasoning sets, Qwen3-235B-A22B answers, and filtered R1 traces, in English and with a Chinese R1 source listed. Those descriptions apply to those datasets. They are not a statement that all of those rows were in this 49,704-row run. The saved config expects a column named `text`. The published medical-o1 columns are `Question`, `Complex_CoT`, and `Response`. The II-Medical columns are `model`, `question`, `problem`, and `messages`. The mamachang columns are `instruction`, `input`, and `output`. None of those published schemas is a column named `text`.

**(d) Base model.** Card YAML: `Qwen/Qwen3-8B`. Post-trained, as in section 1. The open-r1 example command uses `Qwen/Qwen3-0.6B-Base` for a different distill run. This saved run’s card names `Qwen/Qwen3-8B`.

**(e) Hyperparameters.** Saved config: learning rate 4e-5, 5 epochs, cosine schedule with `min_lr_rate` 0.1, warmup ratio 0.03, per-device train batch 2, gradient accumulation 2, one process, max gradient norm 0.2, bf16, seed 42, gradient checkpointing true, `eos_token` `<|im_end|>`, logging steps 1, save steps 2000. `trainer_state.json`: epoch 5.0, global step 62130, `train_batch_size` 2. `all_results.json`: `train_loss` 0.07142430102201106, `train_runtime` 444789.0665 seconds. Logging directory: `data/OpenR1-Distill-Qwen3-8B-Medical/runs/Nov02_12-08-57_vm-25072235123`. GPU product name is not stated. These learning-rate, epoch, length, and batch numbers match the numbers in the open-r1 `sft.py` docstring. That docstring’s dataset is `open-r1/Mixture-of-Thoughts`, which this card does not name.

**(f) Evaluation.** `eval_strategy` init args are `NO`. `trainer_state.json` has 62,131 log lines and no `eval_` key. No benchmark table is on the card.

**(g) Task and language.** The card prose says the model was fine-tuned on medical reasoning sets whose fields are a question, a reasoning trace, and an answer. That is the task the prose claims. The YAML dataset’s row 0 is an English multiple-choice vignette with `<analysis>` and `<answer>` tags. The 49,704-row mix that the trainer counted is not identified, so the language of that mix is not stated. The two datasets named in prose are English and Chinese (medical-o1) and a mostly English collection that also lists a Chinese R1 source (II-Medical).

### Discrepancies

1. Inventory `methods` is `sft`, which matches the card and `loss_type` `nll`. Inventory `datasets` is `mamachang/medical-reasoning`, which matches the YAML and not the prose.
2. The prose names two datasets. Their published row counts do not add to 49,704. The YAML dataset has 3,702 rows, not 49,704.
3. The repo name contains Distill. The saved loss is `nll`.
4. `hf_ds_config` micro-batch is 2. The nested `dschf.config` micro-batch is 1.
5. The Hub UI’s 308k parameter figure does not match `safetensors.parameters.BF16` 8,190,735,360.

### Confidence

Medium for the objective and the hyperparameters, because both are in the saved `SFTConfig` and the step count matches 49,704 rows for 5 epochs at batch 4. Low for which rows those 49,704 were, because the prose, the YAML, and the published dataset lengths disagree.

### Queries tried

- `vinhnguyenxu OpenR1-Distill-Qwen3-8B-Medical SFT medical reasoning`
- `HuatuoGPT-o1 medical-o1-reasoning-SFT dataset paper arxiv 2412.18925`
- `"49704" medical Qwen3 SFT OR OpenR1 OR medical-o1`
- `github.com vinhnguyenxu OpenR1-Distill-Qwen3 medical`
- II-Medical-Reasoning-SFT README and the datasets-server size of medical-o1
- Downloaded `mamachang/medical-reasoning` JSON (3,702 rows)
- https://github.com/huggingface/open-r1/blob/main/src/open_r1/sft.py
- Saved `training_args.bin` and `trainer_state.json`; Featherless page repeats the card

## Patterns in this batch

The three mlxha checkpoints are one GRPO series on English medical exam questions, saved from `open_r1.configs.GRPOConfig`, with the same think/answer system prompt and the same three logged reward names (`mcq_accuracy_reward`, `format_reward`, `tag_count_reward`). The plain run and v2 use the 182,822-row MedMCQA train split; medi70 uses a 16,885-row set whose every row is labeled Advanced Knowledge and whose name contains meditron70b. No source states that Meditron-70B wrote that subset. The runs also differ in learning rate (3e-6, 5e-6, and 2e-6), epoch fraction (0.25, 1.0, and 0.5), batch, process count, and reward weights. None of the five models has a paper that describes that checkpoint. Baize V3’s card states supervised fine-tuning with LoRA on 157,438 Chinese question-answer rows; the upload is a full BF16 Qwen3-8B file with Unsloth keys and no adapter file, and English use is not in the demo (one training instruction is English). The OpenR1 medical checkpoint is supervised fine-tuning with negative log likelihood for 5 epochs; the name contains Distill, and the card’s two dataset names, the YAML id `mamachang/medical-reasoning`, and the trainer’s 49,704-row count are three different accounts of the data.
