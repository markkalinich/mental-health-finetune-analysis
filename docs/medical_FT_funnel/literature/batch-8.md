# Medical fine-tune literature, batch 8

Five models. Two have a paper or a training script that names the checkpoint. Two were trained with the same Group Relative Policy Optimization (GRPO) code. Two have no paper; the model card is the training record.

| model | source found | objective | update scope | data (name, n, provenance) | base | task trained for | language | matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5 | paper + code | supervised fine-tuning (SFT) | full weights | graliuce/MedMCQA.20.01, 4,880 Hub rows (paper says 4.78k); GPT-4o conversations and reasons, Llama-3.1-8B-Instruct success labels, from MedMCQA and MedQA exam items | Qwen/Qwen2.5-3B-Instruct (instruction-tuned) | other: decide whether a doctor–patient conversation has enough information to diagnose, and write the reason | en | yes |
| mlxha/Qwen-2.5-3B-grpo-medmcqa | code | GRPO | not stated | mlxha/medmcqa-grpo, 182,822 train rows; human-written MedMCQA exam items, reformatted | Qwen/Qwen2.5-3B-Instruct (instruction-tuned) | multiple-choice exam answering | en | yes |
| mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70 | code | GRPO | not stated | mlxha/medmcqa-grpo-meditron70b, 16,885 rows; MedMCQA-style items; how the subset was chosen is not stated | Qwen/Qwen2.5-7B-Instruct (instruction-tuned) | multiple-choice exam answering | en | yes |
| DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model | none | SFT | LoRA | Baize-TCM-Corpus V3; dataset card says 157,438 Chinese question–answer pairs, collated and checked; generator not stated | Qwen/Qwen3-0.6B (post-trained) | open medical question answering | zh | yes |
| khazarai/Medical-QA | none | SFT | not stated | medalpaca/medical_meadow_medical_flashcards, 33,955 rows; student Anki cards rephrased by GPT-3.5-turbo | unsloth/Qwen3-0.6B (post-trained Qwen3-0.6B) | open medical question answering | en | yes |

## 1. graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5

### Sources

- Preprint: Grace Liu, Yuxiao Qu, Jeff Schneider, Aarti Singh, and Aviral Kumar, “CaRT: Teaching LLM Agents to Know When They Know Enough,” arXiv:2510.08517. https://arxiv.org/abs/2510.08517 (HTML used: https://arxiv.org/html/2510.08517v1). Also submitted to the NeurIPS 2025 Efficient Reasoning workshop: https://openreview.net/forum?id=kkKsmPeasY
- Code that builds this exact Hub id: https://github.com/graliuce/CaRT — `bash/sft/submit.slurm`, `bash/sft/task.sh`, `finetune/sft.py`. README: https://github.com/graliuce/CaRT/blob/main/README.md
- Model card cache: `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/graliuce__Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5__2026-10-05.md`
- Dataset page: https://huggingface.co/datasets/graliuce/MedMCQA.20.01 (4,880 rows; README empty)

### What `20.01` and `1.0e-5` mean

`1.0e-5` is the learning rate. The Slurm script sets `learning_rates=(1.0e-5)` and builds the Hub id as `job_name=${model_name}_${dataset_name}_${learning_rate}`. Script says: `job_name=${model_name}_${dataset_name}_${learning_rate}` with `model_name=Qwen2.5-3B-Instruct`, `dataset_name=MedMCQA.20.01`, and `learning_rate=1.0e-5` (https://github.com/graliuce/CaRT/blob/main/bash/sft/submit.slurm). The paper’s SFT table lists the same value. Paper says: `learning_rate | 1.0e-5` (Appendix C.1, Table 2, https://arxiv.org/html/2510.08517v1). The Hub dataset page also lists sibling checkpoints whose names end in `1.0e-6`, `1.0e-4`, and `1.0e-5`, on the same dataset, so the suffix is the learning-rate sweep token.

`20.01` is the dataset-version token, not a second hyperparameter. The same Slurm file puts `MedMCQA.20.01` in `dataset_names` and `graliuce/MedMCQA.20.01` in `dataset_paths`. The README calls this checkpoint the CaRT termination model and points the dataset link at `graliuce/MedMCQA.20.01`. No file defines the digits `20` and `01` apart from that dataset id. The paper never uses the string `20.01`. The paper does say the CaRT medical training set was balanced to 80% “continue” and 20% “terminate” (Appendix B.2). That 20% figure is a property of the training set. The paper does not say the version number encodes it.

### Training record

(a) Objective. Supervised next-token fine-tuning on a completion that is a written reason plus a terminate-or-continue decision. Paper says: “We perform supervised fine-tuning (SFT) on the counterfactual examples described above.” Card says: “This model was trained with SFT.” The README assigns the extra GRPO stage to a different checkpoint, `graliuce/Qwen2.5-3B-Instruct_20.03_rl_0.5`. This checkpoint is the SFT termination model, not that RL run.

(b) Update scope. Full weights. The launch command does not pass `--use_peft`. `finetune/sft.py` passes `peft_config=get_peft_config(model_config)` into `SFTTrainer`. In TRL 0.16, `ModelConfig.use_peft` defaults to `False`, and `get_peft_config` returns no adapter unless that flag is set (https://github.com/huggingface/trl/blob/v0.16.0/trl/trainer/model_config.py). The upload is a full Qwen2 checkpoint: cached Hub metadata lists 3,085,938,688 BF16 parameters and `adapter: 0`. Rank, alpha, and target modules: not used. Adapter merged: no adapter.

(c) Data. Hub id `graliuce/MedMCQA.20.01`, 4,880 rows, columns `messages` and `suffix`. The suffix is an English paragraph that starts “There is sufficient information…” or “There is insufficient information…”. Paper Appendix B: the problems are filtered diagnostic items from MedMCQA (1,352 after a keyphrase filter) plus MedQA-USMLE items from Craft-MD; GPT-4o (`gpt-4o-2024-11-20`) simulates the doctor and the patient; Llama-3.1-8B-Instruct scores each conversation prefix (50 generations); GPT-4o writes the counterfactual question and the reason. Paper says the released training set is “4.78k examples,” 80% continue and 20% terminate. Language: English prompts and English conversations. The exam items are human-written; the conversations, counterfactuals, and reasons are synthetic.

(d) Base. `Qwen/Qwen2.5-3B-Instruct`, the instruction-tuned model. Paper says: “The base models are directly loaded from Hugging Face: Qwen3-1.7B and Qwen2.5-3B-Instruct.” This file is the Qwen2.5-3B-Instruct run. A separate question-asking model, `CohenQu/Qwen2.5-3B-Instruct_MedMCQA.11.01`, asks the questions. It is not this checkpoint.

(e) Hyperparameters. The script that names this checkpoint: learning rate `1.0e-5`, 3 epochs, per-device batch size 1, gradient accumulation 32, 8 processes (effective batch 256), max sequence length 4,096, bf16, DeepSpeed ZeRO-3, 8 A6000 GPUs, 100G memory, 40-hour Slurm limit (`submit.slurm`, `task.sh`). Paper Table 2: learning rate `1.0e-5`, 3 epochs, batch size 256, max sequence length 16,384, bf16, 8 GPUs, warmup ratio 0.1. The script and the paper agree on learning rate, epochs, effective batch, precision, and GPU count. They disagree on sequence length.

(f) Evaluation. The paper compares this method with the untouched Qwen2.5-3B-Instruct model and with an equal-sized SFT baseline on free-response diagnosis success, the gap versus a fixed-length stopping rule, and the rate of stopping at the first large jump in success. Figure 3 is the medical result. The text says CaRT is higher than both comparators on the holdout set and on dermatology questions held out of training, and that the extra RL run tends toward longer conversations. The HTML extract does not contain the plotted percentages. Appendix B.3: evaluation conversations are 261 in-distribution and 233 out-of-distribution, after dropping conversations the seeker never solved.

(g) Task and language. The trained behavior is a triage decision on a doctor–patient transcript: write a reason, then either give a diagnosis or say more information is needed. Paper prompt: “You are a Medical Triage Assistant. Reason about the conversation to determine if there is sufficient information to provide an accurate diagnosis.” It is not trained to answer the MedMCQA multiple-choice item. Intended language of the prompts and the conversations is English. The model card has no language tag.

### Discrepancies

1. Paper Table 2 says `max_seq_length` 16,384. The Slurm launch that writes this Hub id passes `--max_seq_length 4096`.
2. The paper says the final training set has 4.78k examples. The Hub dataset has 4,880 rows.
3. The inventory row is SFT on `graliuce/MedMCQA.20.01` from `Qwen/Qwen2.5-3B-Instruct`. That matches. The dataset name contains MedMCQA; the rows are termination dialogues built from exam items, not the original multiple-choice answers.

### Confidence

High. The preprint and the script that constructs `Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5` agree on the method, the learning rate, the epoch count, and the dataset id.

### Queries tried

1. `graliuce MedMCQA Qwen2.5 fine-tuning SFT paper`
2. `grace_rl infoseek MedMCQA.20.01 learning rate Qwen`
3. `site:github.com/graliuce MedMCQA.20.01 learning_rate sft`
4. `"MedMCQA.20.01" OR "dataset version" CaRT Grace Liu termination`
5. `"Grace" CaRT "Know When They Know Enough" author MedMCQA fine-tune hyperparameters`
6. Direct reads of arXiv HTML 2510.08517, the CaRT README, `submit.slurm`, `task.sh`, `finetune/sft.py`, the Hub dataset page, and TRL `ModelConfig.use_peft`

## 2. mlxha/Qwen-2.5-3B-grpo-medmcqa

### Sources

- Shared code: Michael Ha, https://github.com/mlxha/open-r1, file `src/open_r1/rewards.py`. The public recipe directory does not contain a MedMCQA config. The reward functions that this run logged are in that file.
- Trainer log stored in the model repo: https://huggingface.co/mlxha/Qwen-2.5-3B-grpo-medmcqa/raw/main/trainer_state.json and `all_results.json`
- Model card cache: `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/mlxha__Qwen-2.5-3B-grpo-medmcqa__2026-10-05.md`
- Dataset rows: https://huggingface.co/datasets/mlxha/medmcqa-grpo — datasets-server train split, 182,822 rows. The Hub page’s “Number of rows: 193,155” is train 182,822 + validation 4,183 + test 6,150, the official MedMCQA sizes.
- Card tags include `open-r1`. Wandb link on the card: `https://wandb.ai/alexs-team/reasoning/runs/9832a928-b485-4023-9e5f-b367f68a0b69` (not opened; the run page was not fetched).

### Training record

(a) Objective. GRPO, reinforcement learning with a reward. Card says: “This model was trained with GRPO, a method introduced in DeepSeekMath.” The logged reward names are `format_reward`, `mcq_accuracy_reward`, and `tag_count_reward`. Those three names are functions in `rewards.py`. `mcq_accuracy_reward` returns 1.0 when a letter A–D inside `<answer>` matches the solution string, and 0.0 otherwise. `format_reward` checks a `<think>` block followed by an `<answer>` block. `tag_count_reward` scores those tags. The DeepSeekMath citation on the card is the GRPO paper. It is not a paper about this checkpoint.

(b) Update scope. Not stated. The card does not say LoRA, QLoRA, or full-weight updates. The public MedMCQA launch yaml is not in the repo. The upload is a full Qwen2 checkpoint: 3,085,938,688 BF16 parameters, files `model-00001-of-00002.safetensors` and `model-00002-of-00002.safetensors`, no `adapter_config.json`. Rank, alpha, target modules, and whether an adapter was merged: not stated.

(c) Data. `mlxha/medmcqa-grpo`. Trainer log says `"train_samples": 182822`, which is the MedMCQA train split. A row has the original MedMCQA fields (`question`, `opa`–`opd`, `cop`, `exp`) plus `problem` (“Question: … Options: A–D”) and `solution` (the letter). The first row is the standard MedMCQA anatomy item on chronic urethral obstruction, solution `C`. Provenance: human-written AIIMS and NEET PG exam questions (MedMCQA paper, Pal, Umapathi, and Sankarasubbu, 2022, https://arxiv.org/abs/2203.14371). Language: English. This copy is a reformat, not a new set of questions.

(d) Base. `Qwen/Qwen2.5-3B-Instruct`, instruction-tuned. Card YAML: `base_model: Qwen/Qwen2.5-3B-Instruct`.

(e) From `trainer_state.json`, not from a yaml. `num_train_epochs` is 1. The run ended at `epoch` 0.250, `global_step` 1429, `max_steps` 1429, so the step cap stopped it at one quarter of an epoch. `train_batch_size` is 8. The highest `learning_rate` written in the log is 2.999995524115659e-06. The configured peak sits in `training_args.bin`, which was not decoded. `train_runtime` is 24,394.4 seconds. `train_loss` is 0.00125. Hardware: not stated.

(f) Evaluation. No held-out MedMCQA score is on the card. The log’s training-batch `rewards/mcq_accuracy_reward/mean` at step 1429 is 0.580. That is a training reward, not a test accuracy.

(g) Task and language. The reward pays for the correct multiple-choice letter, and also for a think-then-answer format. The task the reward defines is multiple-choice exam answering. Intended language is English. The card has no language tag.

### Discrepancies

1. The name contains `grpo`. The card also states GRPO, so the name and the card agree.
2. The inventory row is GRPO on `mlxha/medmcqa-grpo` from `Qwen/Qwen2.5-3B-Instruct`. That matches the card and the trainer log.

### Confidence

High for GRPO, the 182,822-row MedMCQA train set, the three reward functions, and the logged step count. Medium for the parameter-update scope, which no source states.

### Queries tried

1. `mlxha Qwen GRPO medmcqa medi70 meditron70b`
2. `huggingface.co/mlxha datasets medmcqa-grpo github alex-ht`
3. `mlxha huggingface profile "Alex" GRPO medmcqa open-r1 recipe`
4. `site:github.com/alex-ht medmcqa grpo medi70 OR meditron`
5. `"mcq_accuracy_reward" medmcqa GRPO`
6. Direct reads of `trainer_state.json`, `all_results.json`, the datasets-server row, and `src/open_r1/rewards.py`

## 3. mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70

### Sources

Same repository as model 2: https://github.com/mlxha/open-r1 `src/open_r1/rewards.py`. Trainer log: https://huggingface.co/mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70/raw/main/trainer_state.json. Model card cache: `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/mlxha__Qwen2.5-7B-Instruct-grpo-medmcqa-medi70__2026-10-05.md`. Dataset: https://huggingface.co/datasets/mlxha/medmcqa-grpo-meditron70b. Wandb link on the card: `https://wandb.ai/alexs-team/reasoning/runs/a6495433-dbba-4981-95eb-1982c52a28fc` (same project as model 2; run page not fetched).

### What `medi70` means

The card names the dataset `mlxha/medmcqa-grpo-meditron70b`. The model id shortens that to `medi70`. No README, paper, or script sentence defines the abbreviation. The dataset README is empty. The public `mlxha/open-r1` tree has no file whose name contains `meditron` or `medi70`. A row is a MedMCQA-style item whose `solution` is a letter (`C` on the first row), not a Meditron-70B generation. There are 16,885 rows, against 182,822 in `mlxha/medmcqa-grpo` train. The selection rule that produced 16,885 is not stated anywhere found. MediTron-70B (Chen et al., arXiv:2311.16079, https://arxiv.org/abs/2311.16079) is a different model; that paper’s MedMCQA training count after dropping empty explanations is 159,669, not 16,885. Do not read `medi70` as “trained on MediTron-70B outputs” from the name alone.

### Training record

(a) Objective. GRPO, same card sentence as model 2. The log records the same three rewards: `format_reward`, `mcq_accuracy_reward`, and `tag_count_reward`.

(b) Update scope. Not stated. The upload is a full Qwen2 checkpoint: 7,615,616,512 BF16 parameters in four safetensors shards, no `adapter_config.json`. Rank, alpha, and merge: not stated.

(c) Data. `mlxha/medmcqa-grpo-meditron70b`, 16,885 rows. Trainer log says `"train_samples": 16885`. Fields are `id`, `question`, `opa`–`opd`, `cop`, `difficulty`, `problem`, `solution`. The first question is an English multiple-choice item on remifentanil; `solution` is `C`. Provenance of the question text: MedMCQA-style exam wording. Who filtered these 16,885 rows, and whether Meditron-70B was used to filter or to write answers: not stated. Language: English in the fetched row.

(d) Base. `Qwen/Qwen2.5-7B-Instruct`, instruction-tuned. Card YAML: `base_model: Qwen/Qwen2.5-7B-Instruct`.

(e) From `trainer_state.json`. `num_train_epochs` is 1. Final `epoch` is 0.995, `global_step` 175, `max_steps` 176. `train_batch_size` is 8. The highest logged `learning_rate` is 4.999505824425164e-06. `train_runtime` is 6,291.8 seconds. `train_loss` is 0.00563. Hardware: not stated.

(f) Evaluation. No held-out score on the card. Training-batch `rewards/mcq_accuracy_reward/mean` at step 175 is 0.460.

(g) Task and language. Same reward as model 2: multiple-choice letter accuracy plus a think/answer format. Intended language of the fetched questions is English.

### Discrepancies

1. The inventory dataset id is `mlxha/medmcqa-grpo-meditron70b`, the method is GRPO, and the parent is `Qwen/Qwen2.5-7B-Instruct`. That matches the card and the trainer log.
2. The model name says `medi70`. The only definition on record is the dataset id that contains `meditron70b`. The subset rule is missing.

### Confidence

High for GRPO, the base model, and the 16,885-row dataset id. Low for any claim about what Meditron-70B did in building that subset, because no source states it.

### Queries tried

1. `mlxha Qwen GRPO medmcqa medi70 meditron70b`
2. `"meditron70b" mlxha OR "medi70" medmcqa grpo reasoning traces`
3. `medmcqa-grpo-meditron70b filter OR subset Meditron`
4. `site:github.com/mlxha meditron70b OR medi70 dataset filter`
5. `huggingface.co/mlxha datasets medmcqa-grpo github alex-ht`
6. Direct reads of the 7B `trainer_state.json`, the datasets-server first row, the empty dataset README, and `rewards.py`

## 4. DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model

### Sources

- Model card cache: `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/DigitalIntelligenceCenter-of-ICMM__Baize-Traditional-Chinese-Medicine-Large-Language-Model__2026-10-05.md`
- Live card and file list: https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model
- Dataset card: https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3
- No paper was found for this checkpoint. arXiv:2304.01196, “Baize: An Open-Source Chat Model with Parameter-Efficient Tuning on Self-Chat Data” (Xu, Guo, Duan, and McAuley), is a different model: LLaMA tuned on ChatGPT self-chat. It does not name this Qwen3 checkpoint, this organization, or this corpus.

### Training record

(a) Objective. Supervised fine-tuning. Card says: “基于通用大模型在 **   条高质量中医问答语料** 上进行指令微调（Supervised Fine-Tuning）.” The example count in that sentence is blank.

(b) Update scope. LoRA. Card table says: “训练方式 | LoRA” and “训练软件 | LLaMA-Factory.” Rank, alpha, and target modules: not stated. Adapter merged: not stated. The published repo is not an adapter folder. It contains `model.safetensors` with 596,049,920 BF16 parameters, the same order of magnitude as Qwen3-0.6B, and no `adapter_config.json`. The load snippet uses `AutoModelForCausalLM`, not a PEFT loader. The card does not say the LoRA weights were merged.

(c) Data. Card names `DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3`. Dataset card says: “语料数量：157,438 条 语言：中文” and “经过整理与校对的问答对.” Each row is `instruction`, `input`, `output`, `system`. The printed example asks, in Chinese, how a broad transcriptome differs from a narrow transcriptome. Provenance beyond “collated and checked”: not stated. Human-written versus model-written: not stated. The model card does not say how many of the 157,438 rows this 0.6B run used.

(d) Base. `Qwen/Qwen3-0.6B`. Card table: “基础模型 | Qwen3-0.6B.” The Hub tree places `Qwen/Qwen3-0.6B-Base` under `Qwen/Qwen3-0.6B`, so the named parent is the post-trained Qwen3-0.6B checkpoint, not the base pretrain. `config.json` is `Qwen3ForCausalLM`.

(e) Epochs, learning rate, batch size, and GPU count: not stated. The card lists context length 4,096 and “量化方式 | 16bit.” `config.json` still has `max_position_embeddings` 40,960 and dtype bfloat16. The load snippet comments `torch.float16`. Those three precision and length statements are not the same.

(f) Evaluation. Not stated anywhere found. No accuracy table.

(g) Task and language. The training rows are open question–answer pairs. The card lists uses as a Chinese-medicine question-answering system, knowledge support for diagnosis, and help for students. Training language: Chinese (`language: zh` on the card; dataset card “语言：中文”). The demo prompt is Chinese: “问题：气虚的主要症状有哪些？”. The Hub widget examples are Chinese. English medical use is not shown. The only English in the repo is the Qwen chat-template boilerplate about tool calls.

### Discrepancies

1. The model card’s example-count sentence is blank. The V3 dataset card says 157,438. The inventory copied both the blank sentence and the V3 dataset id. Method `lora|sft` and parent `Qwen/Qwen3-0.6B` match the card.
2. The card says LoRA and 16-bit, and also tells the user to load a full `AutoModelForCausalLM` in float16. The file on the Hub is one BF16 safetensors file. Merge and dtype are not settled by one sentence.
3. The 2023 Baize chatbot paper is a different model. It should not be cited as this model’s training paper.

### Confidence

Medium. LoRA, SFT, the V3 corpus, Chinese, and the Qwen3-0.6B parent are on the card or the dataset card. Rank, merge, epoch, learning rate, and whether every V3 row was used are not.

### Queries tried

1. `Baize Traditional Chinese Medicine Large Language Model 白泽 中医药 大语言模型`
2. `白泽中医药大语言模型 论文 arxiv Baize TCM LLM ICMM`
3. `DigitalIntelligenceCenter-of-ICMM Baize github LLaMA-Factory 白泽 中医药 English`
4. `"Baize-Traditional-Chinese-Medicine" OR "Baize-TCM-LLM" OR "白泽中医药大语言模型" 论文 OR paper OR arxiv`
5. The V3 dataset card and the model file list
6. arXiv:2304.01196, checked and set aside as a different Baize

## 5. khazarai/Medical-QA

### Sources

- Model card cache: `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/khazarai__Medical-QA__2026-10-05.md`
- Live card: https://huggingface.co/khazarai/Medical-QA. Commits on the repo are by the Hub user Rustamshry. No training notebook or GitHub repo for this run was found. Rustamshry’s GGUF copy repeats the same card: https://huggingface.co/Rustamshry/Medical-QA-GGUF
- Dataset: https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards (33,955 train rows, datasets-server size API)
- Dataset paper: Tianyu Han and colleagues, “MedAlpaca — An Open-Source Collection of Medical Conversational AI Models and Training Data,” arXiv:2304.08247, https://arxiv.org/abs/2304.08247. That paper built the flashcard set. It does not train `khazarai/Medical-QA`.

### Training record

(a) Objective. SFT, from the card tags, not from a methods paragraph. Card YAML: `tags: sft, unsloth, trl`. The prose says “a fine-tuned version of Qwen3-0.6B” and does not repeat the word SFT. No DPO, GRPO, or distillation step is stated for this checkpoint.

(b) Update scope. Not stated. The tag `unsloth` and `config.json` field `"unsloth_fixed": true` say the weights were saved with Unsloth. They do not say LoRA, QLoRA, or full updates. Rank and alpha: not stated. The repo file is `model.safetensors`, 1.19 GB, 596,049,920 BF16 parameters, no `adapter_config.json`. Adapter merged: not stated.

(c) Data. Card YAML dataset: `medalpaca/medical_meadow_medical_flashcards`. Card prose: “fine-tuned on a 34K medical Q&A dataset derived from the Anki Medical Curriculum flashcards” and “34,000 question-answer pairs.” The Hub dataset has 33,955 rows. Dataset card says: “After removing cards that contained images, we utilized OpenAI's GPT-3.5-turbo to rephrase the cards into coherent, contextually relevant question-answer pairs.” The MedAlpaca paper Table 1 lists “Medical Flash Cards | Anki Flashcards | Rephrased Q&A pairs | 33,955.” The flashcards were written by medical students; the released pairs are GPT-3.5-turbo rewrites. The model card describes the student flashcards and does not mention GPT-3.5-turbo. Language: English. Card YAML: `language: en`. Columns are `instruction` (“Answer this question truthfully”), `input` (the question), and `output` (a short answer).

(d) Base. `unsloth/Qwen3-0.6B`. Card says “Base Model: Qwen3-0.6B.” The inference snippet sets `enable_thinking = False`, which is the post-trained Qwen3 chat template, not the base pretrain. Instruction-tuned parent: yes.

(e) Epochs, learning rate, batch size, hardware: not stated anywhere found.

(f) Evaluation. Not stated. The card describes exam-style answers and says the model is not for patient care. It reports no score.

(g) Task and language. Open question answering: a short medical question in, a short answer out. The card calls the use “exam preparation.” The rows are not multiple-choice items. Intended language: English. The example question is “What can β-blockers cause or exacerbate due to excessive AV nodal inhibition?”

### Discrepancies

1. The card says 34,000 pairs. The dataset has 33,955 rows. The MedAlpaca paper also says 33,955.
2. The card says the flashcards were created by medical students. The dataset card and the MedAlpaca paper say the released pairs were rewritten by GPT-3.5-turbo after image cards were removed. Both can be true; the card omits the rewrite.
3. The body says “License: MIT.” The YAML says `apache-2.0`.
4. The inventory row is SFT on `medalpaca/medical_meadow_medical_flashcards` from `unsloth/Qwen3-0.6B`. That matches the card tags and YAML. The inventory does not claim a LoRA rank, and none is stated.

### Confidence

Medium. The dataset id, the English open-question task, and the SFT tag are on the card, and the 33,955-row GPT-3.5-turbo rewrite is on the dataset card. The parameter-update scope and the training hyperparameters of this run are not stated.

### Queries tried

1. `khazarai Medical-QA Qwen3-0.6B medical flashcards unsloth`
2. `Rustamshry khazarai Medical-QA unsloth fine-tune github`
3. `medalpaca medical_meadow_medical_flashcards Anki dataset paper`
4. `khazarai Medical-QA epochs learning rate LoRA rank unsloth Qwen3-0.6B`
5. The Hub model file list and the datasets-server size API (33,955 rows)
6. Featherless model page, which repeats the model card and adds no training hyperparameters

## Patterns in this batch

Two of the five checkpoints have a source outside the model card, and those two sources describe different jobs. The graliuce checkpoint is full-weight SFT, at learning rate 1e-5, on 4,880 synthetic doctor–patient prefixes. The name `MedMCQA.20.01_1.0e-5` is `{base}_{dataset id}_{learning rate}` in `submit.slurm`. The model is trained to stop a diagnostic interview, not to pick A–D on MedMCQA. The two mlxha checkpoints share one GRPO code path: `mcq_accuracy_reward`, `format_reward`, and `tag_count_reward` in `github.com/mlxha/open-r1`. One trained on all 182,822 MedMCQA train questions and stopped at step 1,429 (epoch 0.25). The other trained on 16,885 rows whose dataset id contains `meditron70b`. Nothing found says how those 16,885 rows were chosen. The Baize 0.6B card is Chinese LoRA SFT in LLaMA-Factory on the V3 question–answer corpus; the example count on that card is blank, the dataset card says 157,438 Chinese pairs, and no English medical example is shown. The 2023 Baize chatbot paper is a different model. khazarai/Medical-QA is an English open-question SFT run on the MedAlpaca flashcard set (33,955 GPT-3.5-turbo rewrites of student cards). The card rounds that to 34,000 and does not state LoRA rank, epochs, or learning rate. Inventory method and dataset ids match the cards for all five. The inventory does not record the graliuce task change from exam items to termination dialogues, or the missing medi70 filter.
