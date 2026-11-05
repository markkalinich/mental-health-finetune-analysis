# Medical fine-tune literature, batch 9

Five Qwen3 medical uploads. Two cards state supervised fine-tuning. One of those also states that every layer was updated. The graliuce checkpoint has a saved trainer config and a shared training script. Cannae-AI and PopiT name datasets and a starting checkpoint, and do not name the loss or whether training updated every weight.

| model | source found | objective | update scope | data (name, n, provenance) | base | task trained for | language | matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| suayptalha/Qwen3-0.6B-Medical-Expert | none | sft | full | FreedomIntelligence/medical-o1-reasoning-SFT, 90,120 rows in the dataset, GPT-4o medical reasoning set | Qwen/Qwen3-0.6B (post-trained) | reasoning traces | en | yes |
| XformAI-india/Qwen3-1.7B-medicaldataset | none | sft | not stated | same dataset, 90,120 rows, GPT-4o | Qwen/Qwen3-1.7B (post-trained) | reasoning traces | en | yes |
| graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5 | code | sft | full | graliuce/MedMCQA.20.01, 4,880 rows, GPT-4o dialogues plus Llama and GPT-4o labels | Qwen/Qwen3-1.7B (post-trained) | other: stop or continue a diagnostic interview | en | yes |
| Cannae-AI/MedicalQwen3-Reasoning-4B | none | not stated | not stated | medical-o1-reasoning-SFT (90,120) and Mohammed-Altaf/medical-instruction-120k (112,165) | Qwen/Qwen3-4B (post-trained) | other: instructions, reasoning, and clinical decisions | en | partly |
| Hoshino-Yumetsuki/PopiT-Qwen3-4B-Medical-SFT-1128 | none | not stated | not stated | four Chinese sets: HuatuoGPT SFT 226,042; dialogue 799,743; medical_o1 Chinese 21,057; Huatuo26M-Lite 177,703 | unsloth/Qwen3-4B-Instruct-2507 (instruct) | open question answering | zh | partly |

## 1. suayptalha/Qwen3-0.6B-Medical-Expert

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/suayptalha__Qwen3-0.6B-Medical-Expert__2026-10-05.md`. Live page matches: https://huggingface.co/suayptalha/Qwen3-0.6B-Medical-Expert
- Weight commit message "Upload model trained with Unsloth": https://huggingface.co/suayptalha/Qwen3-0.6B-Medical-Expert/commit/2eaedfcfdd1b4ec94958a32310e34655ec3f626c
- Dataset card: https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT
- Starting checkpoint card: https://huggingface.co/Qwen/Qwen3-0.6B
- No GitHub, Kaggle, Colab, or paper by suayptalha for this repo id. Sibling cards `suayptalha/Qwen3-0.6B-Diagnose` and `suayptalha/Qwen3-0.6B-Treatment` use the same Unsloth wording and different datasets. Their epoch and learning-rate lines are not copied onto this card.

### Training record

(a) Objective. Supervised fine-tuning. Card says: "Fine-tuning was conducted using the Hugging Face TRL library with the Supervised Fine-Tuning (SFT) approach." YAML tags include `trl` and `sft`.

(b) Update scope. Full. Card says: "All model layers were fully updated (`full_finetuning=True`)." Also: "Qwen3 base model weights were loaded via the `unsloth` library in bf16 precision." No rank, alpha, or target modules. The 2026-10-05 card cache (`revision_3_experiments/hf_inventory/cache/cards/2026-10-05__016.csv`) lists one `model.safetensors`, no adapter file, and 596,049,920 bfloat16 parameters. Config field `unsloth_version` is `2025.4.7` (`revision_3_experiments/hf_inventory/cache/configs/suayptalha__Qwen3-0.6B-Medical-Expert__2026-10-06.json`).

(c) Data. Hub id `FreedomIntelligence/medical-o1-reasoning-SFT`. Dataset page: "Number of rows: 90,120." Dataset card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." Columns in the viewer are `Question`, `Complex_CoT`, and `Response`. Language of the rows is English. A later news line on the same card says a DeepSeek-R1 distilled file was also released in the repo. The model card names the repo and does not name which file was loaded. The model card says each example is "medically relevant instructions or questions paired with detailed, step-by-step clinical reasoning responses."

(d) Base. YAML: `Qwen/Qwen3-0.6B`. That card says: "Training Stage: Pretraining & Post-training." The Hub tree places `Qwen/Qwen3-0.6B` after `Qwen/Qwen3-0.6B-Base`. So the starting checkpoint is the post-trained Qwen3-0.6B model, which follows instructions and can emit a thinking block. The medical card's phrase "base model weights" is the author's name for that starting checkpoint.

(e) Epochs, learning rate, batch size, hardware: not stated anywhere found for this repo id.

(f) Evaluation: not stated anywhere found.

(g) Task and language. Card says the model was "trained to follow clinical instructions, interpret symptoms, and generate reasoned diagnoses or treatment suggestions," on step-by-step clinical reasoning. That is reasoning traces for medical questions. Card YAML `language: en`.

### Discrepancies

1. The card says "Qwen3 base model weights." The YAML id and the Hub tree are the post-trained `Qwen/Qwen3-0.6B`, not `Qwen/Qwen3-0.6B-Base`.

### Confidence

High. The card states TRL supervised fine-tuning and `full_finetuning=True`. Epochs, learning rate, batch size, hardware, and evaluation are not on the card.

### Queries tried

1. `suayptalha Qwen3-0.6B-Medical-Expert full fine-tuning unsloth`
2. `github suayptalha Qwen3-0.6B-Medical-Expert unsloth notebook`
3. `suayptalha github OR kaggle OR colab Qwen3 Medical Expert full_finetuning`
4. Hugging Face model page, file tree, and the Unsloth upload commit
5. `FreedomIntelligence/medical-o1-reasoning-SFT` dataset card
6. Sibling cards `Qwen3-0.6B-Diagnose` and `Qwen3-0.6B-Treatment`
7. `Qwen/Qwen3-0.6B` model card, training-stage line

## 2. XformAI-india/Qwen3-1.7B-medicaldataset

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/XformAI-india__Qwen3-1.7B-medicaldataset__2026-10-05.md`. Live page: https://huggingface.co/XformAI-india/Qwen3-1.7B-medicaldataset
- Same dataset card as model 1.
- Starting checkpoint: https://huggingface.co/Qwen/Qwen3-1.7B
- Featherless page repeats the model card: https://featherless.ai/models/XformAI-india/Qwen3-1.7B-medicaldataset
- No GitHub or paper. The sibling `XformAI-india/Qwen3-4B-medicaldataset` uses the same card outline and the same dataset id. That is a second card from the same author, not an independent training log.

### Training record

(a) Objective. Supervised fine-tuning. Card says: "Fine-tuning method: Supervised fine-tuning (SFT)."

(b) Update scope. Not stated. No LoRA, QLoRA, rank, or "all weights" sentence. The 2026-10-05 card cache (`revision_3_experiments/hf_inventory/cache/cards/2026-10-05__008.csv`) lists one `model.safetensors`, no adapter file, and 1,720,574,976 float16 parameters. The card also says "Precision: bfloat16 / float16." A full weight file does not say whether training updated every weight or merged an adapter first.

(c) Data. `FreedomIntelligence/medical-o1-reasoning-SFT`, 90,120 rows. Dataset card: constructed using GPT-4o, as quoted under model 1. The model card says: "Trained only on publicly available or synthetic datasets — not real patient data." It does not say which file inside the dataset repo was used.

(d) Base. Card says: "Base Model: Qwen3-1.7B (from Qwen by Alibaba)." YAML: `Qwen/Qwen3-1.7B`. That card says: "Training Stage: Pretraining & Post-training." Same post-trained checkpoint family as Qwen3-0.6B, with a thinking mode and an instruction chat template.

(e) Card says: "Epochs: 3." "Batch Size: 8." "Learning Rate: 2e-5." "Gradient Accumulation: 4." "Optimizer: AdamW." "Framework: PyTorch, Hugging Face Transformers." Hardware: not stated.

(f) Evaluation: not stated.

(g) Intended use on the card: "Medical question answering," "Summarizing patient records," "Medical reasoning and triage," and non-diagnostic chatbot support. The named dataset is exam-style questions with a reasoning chain and a short response, so the training task that is actually tied to data is reasoning traces. Language is not in the YAML. The dataset rows are English. Use language recorded as `en`.

### Discrepancies

None against the inventory row. The inventory method `sft` and the dataset id match the card.

### Confidence

Medium. The card states SFT and the four hyperparameters. There is no script or trainer file, and a sibling card from the same author uses the same outline.

### Queries tried

1. `XformAI-india Qwen3-1.7B-medicaldataset supervised fine-tuning`
2. `github XformAI-india Qwen3 medical fine-tune`
3. Hugging Face discussions page
4. Featherless model page
5. Sibling `XformAI-india/Qwen3-4B-medicaldataset`
6. `FreedomIntelligence/medical-o1-reasoning-SFT` dataset card
7. `Qwen/Qwen3-1.7B` training-stage line

## 3. graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/graliuce__Qwen3-1.7B_MedMCQA.20.01_1.0e-5__2026-10-05.md`. Live page: https://huggingface.co/graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5
- Saved trainer file on that repo: `training_args.bin` (TRL `SFTConfig`, 7,224 bytes). Unpacked fields are quoted below. Output path inside the file: `/data/user_data/gliu2/models/info-seek/Qwen3-1.7B_MedMCQA.20.01_1.0e-5`. Log directory ends in `Nov13_14-32-51_babel-u9-32`.
- Naming script: https://github.com/graliuce/CaRT `bash/sft/submit.slurm` and `bash/sft/task.sh`. Trainer: `finetune/sft.py`.
- Paper: Grace Liu et al., "CaRT: Teaching LLM Agents to Know When They Know Enough," https://arxiv.org/abs/2510.08517 (HTML: https://arxiv.org/html/2510.08517v1). Appendix B is the data construction. Appendix C is the hyperparameter table.
- Dataset page: https://huggingface.co/datasets/graliuce/MedMCQA.20.01 (README body is empty; the viewer and row count are on the page).
- Weights & Biases link on the card, https://wandb.ai/grace_rl/infoseek/runs/g38pydz5, did not load.
- The original MedMCQA paper (Pal, Umapathi, Sankarasubbu, 2022, https://arxiv.org/abs/2203.14371) describes the exam questions. It does not describe this fine-tune.

The name pattern is defined in `submit.slurm`:

```bash
dataset_names=( MedMCQA.20.01 )
learning_rates=( 1.0e-5 )
model_name=Qwen2.5-3B-Instruct
job_name=${model_name}_${dataset_name}_${learning_rate}
```

`task.sh` then passes `--hub_model_id graliuce/${task}`. So a run name is `{short model name}_MedMCQA.<dataset version>_<learning rate>`. The checked-in array hardcodes `Qwen2.5-3B-Instruct` and one learning rate. The Hub account has the same pattern for other learning rates (`1.0e-6`, `5.0e-5`, `1.0e-4`) and for this Qwen3 id. The saved config's `hub_model_id` is `graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5`.

### Training record

(a) Objective. Supervised fine-tuning. Card says: "This model was trained with SFT." The saved file is a TRL `SFTConfig`. `sft.py` builds an `SFTTrainer`. The paper says: "We perform supervised fine-tuning (SFT) on counterfactual pairs with reasoning traces." The CaRT+RL stage in the paper and in the repo uses GRPO and different dataset ids (`MedMCQA.20.03_rl`). This checkpoint's dataset id is `MedMCQA.20.01`, and the saved config is SFT only.

(b) Update scope. Full. `task.sh` does not pass `--use_peft` or a LoRA flag. The saved `SFTConfig` has `quantization_config` none. DeepSpeed ZeRO stage is 3, `zero3_save_16bit_model` true, `num_processes` 8, global `train_batch_size` 256. The 2026-10-05 card cache (`revision_3_experiments/hf_inventory/cache/cards/2026-10-05__011.csv`) lists one `model.safetensors`, `training_args.bin`, no adapter file, and 1,720,574,976 bfloat16 parameters.

(c) Data. Card says the model is "a fine-tuned version of Qwen/Qwen3-1.7B on the graliuce/MedMCQA.20.01 dataset." Dataset page: "Number of rows: 4,880." Columns are `messages` and `suffix`. Viewer rows are English doctor-patient dialogues. The suffix is a paragraph that starts "There is insufficient information to provide a diagnosis because..." or "There is sufficient information to provide a diagnosis because...".

Paper, Appendix B: training conversations are built from MedQA-USMLE (Craft-MD) and MedMCQA diagnostic questions. "we simulated 20 doctor-patient conversations for each problem in the MedMCQA split using GPT-4o (gpt-4o-2024-11-20) as both the seeker and provider agent." Prefix labels use "Llama-3.1-8B-Instruct as an external reward model." Counterfactual questions are from GPT-4o. "This resulted in a dataset of 1.95k conversations" then resampling "until the dataset contained 80% continue examples and 20% terminate examples. The final dataset size was 4.78k examples." "For the models with reasoning, we queried GPT-4o ... to generate an explanation." `sft.py` puts the loss on the suffix: the collator masks with `<MASK_START>` and `<MASK_END>` and keeps completion tokens after `<MASK_END>`.

(d) Base. Card and saved run: `Qwen/Qwen3-1.7B`. That checkpoint's card says "Training Stage: Pretraining & Post-training." Paper Appendix C: "The base models are directly loaded from Hugging Face: Qwen3-1.7B and Qwen2.5-3B-Instruct."

(e) Saved `SFTConfig` for this repo id: `learning_rate` 1e-5, `num_train_epochs` 3.0, `per_device_train_batch_size` 1, `gradient_accumulation_steps` 32, global batch 256, `max_seq_length` 4096, `warmup_ratio` 0.0, `lr_scheduler_type` linear, `weight_decay` 0.0, `optim` adamw_torch, `bf16` true, `gradient_checkpointing` true, `seed` 42, `report_to` wandb, DeepSpeed ZeRO-3, 8 processes. Log host name `babel-u9-32`. The checked-in slurm asks for `#SBATCH --gres=gpu:A6000:8` and then calls `task.sh` with epoch argument `3`. That slurm file sets `model_name=Qwen2.5-3B-Instruct`. The numeric flags in `task.sh` match this Qwen3 config (`--max_seq_length 4096`, `--per_device_train_batch_size 1`, `--gradient_accumulation_steps 32`, `--bf16`).

(f) This model card reports no score. The GitHub README names `graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5` as the "CaRT termination model," not this Qwen3 id. The paper's medical plots are for that method. They are not a result table for this Hub id.

(g) The trained suffix is a judgment of whether the dialogue has enough information for a diagnosis, plus the reason. The paper calls this termination. It is not multiple-choice answering. Language of the dialogues is English.

### Discrepancies

1. Paper Appendix C table: `max_seq_length` 16384 and warmup ratio 0.1. Saved config for this id: `max_seq_length` 4096 and `warmup_ratio` 0.0. Epochs 3, learning rate 1e-5, global batch 256, bfloat16, and 8 processes match.
2. Paper: "The final dataset size was 4.78k examples." Hub dataset `graliuce/MedMCQA.20.01`: 4,880 rows.
3. Inventory row is `sft` on `graliuce/MedMCQA.20.01`. That matches. The inventory does not record the full ZeRO-3 update, which the saved config and script do.

### Confidence

High. The saved `SFTConfig` names this Hub id, and the CaRT script uses the same flags. The paper describes the data and the SFT objective. Two hyperparameter cells in the paper table differ from the saved config.

### Queries tried

1. `graliuce MedMCQA.20.01 Qwen3-1.7B wandb infoseek`
2. `graliuce MedMCQA.20.01 dataset card training sweep learning rate`
3. `site:huggingface.co/graliuce MedMCQA Qwen3-1.7B models`
4. `"MedMCQA.20.01" Grace Liu OR graliuce OR infoseek learning rate`
5. GitHub `graliuce/CaRT` README, `submit.slurm`, `task.sh`, `finetune/sft.py`
6. arXiv 2510.08517 full HTML, Appendices B and C
7. `training_args.bin` on the model repo
8. MedMCQA paper 2203.14371 (question source, not this run)
9. Weights & Biases run `grace_rl/infoseek/g38pydz5` (page did not load)

## 4. Cannae-AI/MedicalQwen3-Reasoning-4B

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/Cannae-AI__MedicalQwen3-Reasoning-4B__2026-10-05.md`. Live page: https://huggingface.co/Cannae-AI/MedicalQwen3-Reasoning-4B
- File-tree commits are labeled "(Trained with Unsloth)": https://huggingface.co/Cannae-AI/MedicalQwen3-Reasoning-4B/tree/main
- Config `unsloth_version` `2025.11.4` and `unsloth_fixed` true.
- Sibling card `Cannae-AI/MedicalQwen3-Reasoning-14B-IT` uses the same three sentences and swaps the base id to `Qwen/Qwen3-14B`. Same two dataset ids.
- Dataset cards: medical-o1 as above; https://huggingface.co/datasets/Mohammed-Altaf/medical-instruction-120k
- No GitHub, paper, or training-args file. No `adapter_config.json` in the file tree.

### Training record

(a) Objective. Not stated as SFT, DPO, or reinforcement learning. Card says: "This is a fine-tuned version of Qwen/Qwen3-4B" and "The model has been trained on high-quality medical instruct and reasoning datasets." The string `SFT` appears inside the dataset id `medical-o1-reasoning-SFT`. That is a name, not a training statement. Unsloth can run more than one loss. The commit label says the tool, not the loss.

(b) Update scope. Not stated. No rank or alpha. The 2026-10-05 card cache (`revision_3_experiments/hf_inventory/cache/cards/2026-10-05__004.csv`) lists `model-00001-of-00002.safetensors` and `model-00002-of-00002.safetensors`, no `adapter_config.json`, and 4,022,468,096 bfloat16 parameters. Config has `unsloth_fixed: true`. That does not say whether every weight was updated or an adapter was merged before upload.

(c) Data. YAML lists `FreedomIntelligence/medical-o1-reasoning-SFT` (90,120 rows; dataset introduction says GPT-4o, quoted under model 1) and `Mohammed-Altaf/medical-instruction-120k`. That dataset page: "Number of rows: 112,165." The name says 120k. The card says: "I have used all the available opensource datasets and combined them into a single datsource for training." It does not name those source datasets or a generator model. Rows are English human/assistant medical conversations. A heading "Qlora Fine Tuning" on that dataset card points at an example script. It is not a statement about Cannae-AI.

(d) Base. YAML and prose: `Qwen/Qwen3-4B`. That card says: "Training Stage: Pretraining & Post-training."

(e) Epochs, learning rate, batch size, hardware: not stated anywhere found.

(f) Evaluation: not stated.

(g) Other. Card says the model is "specifically optimized for medical instructions,reasoning and clinical decision-making." That sentence covers instruction following, reasoning, and clinical decisions together. Language YAML: `en`.

### Discrepancies

1. Inventory method is `sft`. The card says "fine-tuned" and "trained." It does not say supervised fine-tuning. The inventory evidence quote includes the dataset name `medical o1 reasoning SFT`.

### Confidence

Low. Datasets and the starting checkpoint are in the card. The loss and the parameter update are not.

### Queries tried

1. `Cannae-AI MedicalQwen3-Reasoning-4B fine-tune`
2. `Cannae-AI MedicalQwen3 github unsloth LoRA training`
3. `CannaeAI OR "Cannae-AI" MedicalQwen3 unsloth OR lora OR "medical-instruction-120k"`
4. Sibling `Cannae-AI/MedicalQwen3-Reasoning-14B-IT`
5. `Mohammed-Altaf/medical-instruction-120k` dataset card
6. `FreedomIntelligence/medical-o1-reasoning-SFT` dataset card
7. Hugging Face file tree and Unsloth commit labels
8. `Qwen/Qwen3-4B` training-stage line

## 5. Hoshino-Yumetsuki/PopiT-Qwen3-4B-Medical-SFT-1128

### Sources

Shared series, not a paper. Collection: https://huggingface.co/collections/Hoshino-Yumetsuki/popit-qwen3-medical-sft

- This model: `revision_3_experiments/hf_inventory/cache/readmes/Hoshino-Yumetsuki__PopiT-Qwen3-4B-Medical-SFT-1128__2026-10-05.md`. Live: https://huggingface.co/Hoshino-Yumetsuki/PopiT-Qwen3-4B-Medical-SFT-1128
- `Hoshino-Yumetsuki/PopiT-Gemma-3-12B-Medical-SFT-1213`
- `Hoshino-Yumetsuki/PopiT-Gemma-3-12B-Medical-SFT-1218` raw README: https://huggingface.co/Hoshino-Yumetsuki/PopiT-Gemma-3-12B-Medical-SFT-1218/raw/main/README.md
- Author GitHub https://github.com/Hoshino-Yumetsuki and blog https://yumetsuki.moe/ have no PopiT training post in search.
- Dataset pages listed below. HuatuoGPT data table: https://github.com/FreedomIntelligence/HuatuoGPT
- Upstream dialogue repo linked by ticoAg: https://github.com/Toyhom/Chinese-medical-dialogue-data
- Starting checkpoint: https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507 which copies https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

The three medical cards share one sentence. Qwen card: "本模型在 unsloth/Qwen3-4B-Instruct-2507 的基础上进行医学微调，适用于前期或者用于网络基础病症查询及问答。" Gemma 1213 and 1218 use the same sentence with `unsloth/gemma-3-12b-it`. All three list the same four dataset ids. Gemma 1218 adds `llamafactory/alpaca_zh` and says the mix is there to repair non-medical answers after the 1213 medical-only run. That extra dataset is not on this Qwen card. The repo name contains `SFT`. The cards say 医学微调 (medical fine-tuning) and do not name the loss.

### Training record

(a) Objective. Not stated. Name contains `SFT`. The card says medical fine-tuning. No sentence says supervised next-token training, preference optimization, or reinforcement learning.

(b) Update scope. Not stated. No rank or alpha. Config has `unsloth_version` `2025.11.3` and `unsloth_fixed` true. The 2026-10-05 card cache (`revision_3_experiments/hf_inventory/cache/cards/2026-10-05__005.csv`) lists two safetensors shards, no `adapter_config.json`, and 4,022,468,096 bfloat16 parameters. The card does not say whether training updated every weight.

(c) Data, all listed in YAML. The card does not say that every row was used.

- `FreedomIntelligence/HuatuoGPT-sft-data-v1`. Dataset page: 226,042 rows. README body is empty. GitHub says this is "The data used in the Supervised Fine-Tuning (SFT) stage of HuatuoGPT" and "To leverage the best of both distilled data (from ChatGPT) and real-world data (from Doctors)." The four counts are 61,400 distilled instructions, 69,768 real-world doctor instructions, 68,888 distilled ChatGPT conversations, and 25,986 real-world doctor conversations. Sum is 226,042. Language: Chinese.
- `ticoAg/Chinese-medical-dialogue`. Card YAML: `examples: 799743`. Card says: "process data from Chinese-medical-dialogue-data" and "单轮医患对话" (single-turn doctor-patient dialogue). Upstream README lists 792,099 question-answer pairs in six departments (andrology 94,596, internal medicine 220,606, obstetrics and gynecology 183,751, oncology 75,553, pediatrics 101,602, surgery 115,991). That README does not say who wrote the answers.
- `Ronndy/medical_o1_sft_Chinese`. Dataset page: 21,057 rows. "No dataset card yet." Viewer rows are mostly Chinese exam-style questions with a long reasoning answer, plus some English non-medical items. Who wrote the answers is not stated.
- `FreedomIntelligence/Huatuo26M-Lite`. Dataset page: 177,703 rows. Card says "Size: [178k]" and "Language: [Chinese]." Questions come from Common Crawl medical pages after deduplication and ChatGPT scoring. "We then used ChatGPT to rewrite the answers to the high-scoring questions."

(d) Base. YAML: `unsloth/Qwen3-4B-Instruct-2507`. The Qwen card for `Qwen/Qwen3-4B-Instruct-2507` says: "We introduce the updated version of the Qwen3-4B non-thinking mode, named Qwen3-4B-Instruct-2507" and "Training Stage: Pretraining & Post-training." This is an instruction-tuned checkpoint.

(e) Epochs, learning rate, batch size, hardware: not stated anywhere found.

(f) Card reports a CMB run on 1 December 2025: 11,200 questions, accuracy 51.56%. Nursing exams 59.31% (949/1,600), physician exams 51.30% (1,026/2,000), pharmacist exams 50.78% (1,625/3,200). Gemma 1218 reports its own CMB number, 42.00% on the same 11,200 questions, on 18 December 2025. Those are evaluation scores, not training hyperparameters.

(g) The shared sentence says the model is for early or web-style basic symptom lookup and question answering. That is open medical question answering. Card YAML `language: zh`. CMB is a Chinese multiple-choice exam used as a benchmark, not named as the training objective.

### Discrepancies

1. Inventory method is `sft`. Support in the inventory quote is the repo name and dataset ids that contain `sft`. The card's own verb is 微调.
2. Gemma 1218, the later card in the same series, adds `llamafactory/alpaca_zh`. This Qwen card does not.

### Confidence

Medium for the four dataset ids, the instruct starting checkpoint, Chinese use, and the CMB score, because those are on the card. Low for the loss and the update scope.

### Queries tried

1. `Hoshino-Yumetsuki PopiT Qwen3-4B Medical SFT Gemma`
2. `site:yumetsuki.moe PopiT 医学微调 Qwen`
3. GitHub user `Hoshino-Yumetsuki`
4. Hugging Face collection `popit-qwen3-medical-sft` and the Gemma 1213 and 1218 cards
5. `"PopiT" Hoshino unsloth HuatuoGPT OR "Chinese-medical-dialogue" lora OR qlora`
6. `PopiT-Qwen3-4B-Medical-SFT-1128 unsloth 微调 学习率 OR lora`
7. The four dataset pages, HuatuoGPT GitHub data table, and Toyhom dialogue README
8. `Qwen/Qwen3-4B-Instruct-2507` and `unsloth/Qwen3-4B-Instruct-2507` cards

## Patterns in this batch

Three of the five cards point at `FreedomIntelligence/medical-o1-reasoning-SFT`. That dataset card says the SFT file was built with GPT-4o on verifiable medical problems, and the viewer has 90,120 English rows with a reasoning field and a response field. suayptalha states TRL supervised fine-tuning and `full_finetuning=True`. XformAI states supervised fine-tuning, 3 epochs, learning rate 2e-5, and batch size 8, and does not say whether every weight was updated.

The graliuce name is `{model}_MedMCQA.<version>_<learning rate>`. `bash/sft/submit.slurm` in https://github.com/graliuce/CaRT builds that string and pushes it to `graliuce/`. The checked-in array is the Qwen2.5 run. This Qwen3 checkpoint's saved `SFTConfig` uses the same script's numbers: learning rate 1e-5, 3 epochs, batch 1 with 32 accumulation steps, 8 processes, global batch 256, sequence length 4,096, bfloat16, DeepSpeed ZeRO-3, and no quantization flag. The CaRT paper's table lists sequence length 16,384 and warmup 0.1 for the same method. The data are 4,880 English dialogues whose training target is a stop-or-continue diagnosis judgment, not the MedMCQA letter.

Cannae-AI and PopiT both save full bfloat16 weights with an Unsloth flag in `config.json`. Neither card says LoRA or full updates. PopiT is one series with a Qwen3-4B card and two Gemma-3-12B cards. They share the sentence about medical fine-tuning for symptom lookup, and they share four Chinese datasets. Only the later Gemma card adds general Chinese instructions and explains why. The Qwen PopiT card's own measured result is 51.56% on 11,200 CMB questions.
