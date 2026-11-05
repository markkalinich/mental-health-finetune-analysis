# Medical fine-tune literature, batch 10

How five medical models were trained, from the model card, the saved training file, or a paper about the dataset. A method word in a repository name is not treated as evidence by itself.

## Summary

| model | source found: paper / code / blog / none | objective | update scope | data (name, n, provenance) | base | task trained for | language | matches inventory row: yes / partly / no |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tommi09/MedicalChatBot-Qwen3-4b | none | sft | not stated | Huatuo26M-Lite, 1,000 sampled rows, plus 100 author-built adversarial QA pairs (1,100 total). Lite answers were rewritten by ChatGPT; the 100 adversarial pairs are described as independently constructed | Qwen/Qwen3-4B (post-trained) | open_qa | zh, en tagged; only Chinese use is shown | partly |
| XformAI-india/Qwen3-4B-medicaldataset | none | sft | not stated | FreedomIntelligence/medical-o1-reasoning-SFT. Count used is not stated. Hub splits are 19,704 English, 20,171 Chinese, plus two larger mixes. Trajectories are GPT-4o | Qwen/Qwen3-4B (post-trained) | reasoning_traces | en shown; dataset also has zh | yes |
| mlxha/Qwen3-4B-grpo-medmcqa | code | grpo | full | mlxha/medmcqa-grpo, 182,822 train rows used. Reformatted MedMCQA exam items (human-written AIIMS and NEET PG questions) | Qwen/Qwen3-4B (post-trained) | mcq_exam | en | yes |
| DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V1-16bit | none | sft | lora | Baize-TCM-Corpus V1, 4,735 Chinese QA pairs, described as organized and proofread. Human vs synthetic not stated | Qwen/Qwen3-8B (post-trained) | open_qa | zh. English use is not shown | yes |
| DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V2-16bit | none | sft | lora | Baize-TCM-Corpus V2, 10,578 Chinese QA pairs, same provenance statement as V1 | Qwen/Qwen3-8B (post-trained) | open_qa | zh. English use is not shown | yes |

## 1. Tommi09/MedicalChatBot-Qwen3-4b

### Sources

- Model card (cached): `revision_3_experiments/hf_inventory/cache/readmes/Tommi09__MedicalChatBot-Qwen3-4b__2026-10-05.md`. Live page: https://huggingface.co/Tommi09/MedicalChatBot-Qwen3-4b
- Hub metadata: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__008.csv` (full F16 checkpoint, 4,022,468,096 parameters; files include `Data/mixed_medical_dataset.jsonl` and a GGUF; no `adapter_config.json`)
- Dataset card for the source corpus: https://huggingface.co/datasets/FreedomIntelligence/Huatuo26M-Lite
- Paper for that corpus, not for this fine-tune: Li et al., Huatuo-26M, https://arxiv.org/abs/2305.01526
- Featherless (https://featherless.ai/models/Tommi09/MedicalChatBot-Qwen3-4b) repeats the model card. It is not an independent training source.
- No GitHub repository, paper, or training script under the name Tommi09 or MedicalChatBot-Qwen3 was found.

### Training record

(a) Objective. The card says the model was fine-tuned on question-answer pairs and does not name a loss. Card says: "Based on the qwen3-4b model, we fine-tuned this model using a self-constructed dataset." Chinese section: "基于qwen3-4b模型，我们使用自行构造的数据集（1100条QA对）对该模型进行了微调。" No preference method and no reinforcement-learning method is named. Recorded as supervised fine-tuning because the only described procedure is fine-tuning on labeled QA pairs. The words "SFT" and "supervised" are not on the card.

(b) Parameter-update scope. Not stated. The uploaded weights are a full float16 Qwen3 checkpoint (4,022,468,096 parameters in the Hub safetensors header) and the file list has no adapter file. That does not say whether training updated every weight or a LoRA adapter that was later merged. Rank, alpha, and target modules: not stated anywhere found.

(c) Training data. Card says: "Based on the Huatuo26M-Lite dataset, we randomly selected 1000 pieces of data from this dataset and independently constructed 100 adversarial data (including problems outside the medical field, prompt injection, model attack problems, etc.), and organized them into the form of QA pairs to train the model." Hub id for the public corpus: `FreedomIntelligence/Huatuo26M-Lite`. The 1,100-pair mix is in the model repo at `Data/mixed_medical_dataset.jsonl`, not as a separate Hub dataset. Huatuo26M-Lite card says the parent collection came from Common Crawl and that "We then used ChatGPT to rewrite the answers to the high-scoring questions." Lite size on that card: 178k, language Chinese. The 100 adversarial pairs are described as independently constructed. Their language and whether a model wrote them: not stated anywhere found.

(d) Base model. Card YAML: `base_model: Qwen/Qwen3-4B`. The official Qwen3-4B card says "Training Stage: Pretraining & Post-training" and lists `base_model: Qwen/Qwen3-4B-Base` (https://huggingface.co/Qwen/Qwen3-4B). This fine-tune starts from the post-trained checkpoint, not from `Qwen/Qwen3-4B-Base`.

(e) Epochs, learning rate, batch size, hardware: not stated anywhere found.

(f) Evaluation. No benchmark numbers. Card says: "after fine-tuning, the effect of this 4b model seems to be better than that of the deepseek-7b-base model after fine-tuning" and "sometimes the fine-tuned model will give disastrous answers." The author recommends the q4 GGUF in LM Studio with a ChatML template.

(g) Task and language. The training text is single-turn medical QA. The demo prompt is Chinese: "我最近得了感冒，你有什么治疗建议吗？" The recommended system prompt is Chinese and says the model should answer only medical questions. Card YAML `language` is `zh` and `en`. No English training example or English prompt is shown. Intended use that is actually demonstrated is Chinese medical question answering.

### Discrepancies

1. The Hub relation of this repo to `Qwen/Qwen3-4B` is stored as `quantized`, while the card describes a fine-tune. The repo contains both a full float16 checkpoint and a GGUF.
2. The inventory row records the dataset and the parent and leaves the method blank. The card's word is "fine-tuned" / "微调", not "SFT".
3. Featherless calls the checkpoint BF16. The Hub safetensors header for this repo is F16.

### Confidence

Medium. The data mix and the base model id are stated on the card. The loss and the parameter-update scope are not.

### Queries tried

1. `Tommi09 MedicalChatBot-Qwen3-4b fine-tune Huatuo26M`
2. `"MedicalChatBot-Qwen3" OR "Tommi09" fine-tune LoRA github`
3. `Huatuo-26M a large-scale chinese medical question answering dataset arxiv 2305.01526 Lite`
4. `Qwen/Qwen3-4B Hugging Face post-trained vs Qwen3-4B-Base`
5. `Tommi09 github MedicalChatBot OR Qwen3-4b adversarial`
6. Huatuo26M-Lite dataset card and README (opened from query 1)

## 2. XformAI-india/Qwen3-4B-medicaldataset

### Sources

- Model card (cached): `revision_3_experiments/hf_inventory/cache/readmes/XformAI-india__Qwen3-4B-medicaldataset__2026-10-05.md`. Live page: https://huggingface.co/XformAI-india/Qwen3-4B-medicaldataset
- Hub metadata: full F16 checkpoint, 4,022,468,096 parameters, no adapter file (`2026-10-05__008.csv`)
- Dataset card: https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT
- Dataset paper, which describes HuatuoGPT-o1, not this XformAI run: Chen et al., https://arxiv.org/abs/2412.18925
- Sister cards that repeat the same hyperparameter block: https://huggingface.co/XformAI-india/Qwen3-1.7B-medicaldataset and https://huggingface.co/XformAI-india/Qwen3-0.6B-medicaldataset-gguf
- Org page https://huggingface.co/XformAI-india lists Transformers, PEFT, and LoRA as tooling. It does not describe this run. https://xformai.in has no training writeup for this model. No paper or GitHub repo names this model id.

### Training record

(a) Objective. Card says: "Fine-tuning method: Supervised fine-tuning (SFT)". One stage. The dataset name contains "SFT"; the card also states the method in a sentence, so the name is not the only evidence.

(b) Parameter-update scope. Not stated on the card, in a script, or in a paper. The upload is a full float16 checkpoint with the same parameter count as Qwen3-4B and no `adapter_config.json`. Rank, alpha, target modules, and whether an adapter was merged: not stated anywhere found. The org page's mention of LoRA is not tied to this repository.

(c) Training data. Card says: "Dataset: FreedomIntelligence/medical-o1-reasoning-SFT". It does not say which split or how many rows were used. The Hub dataset has four configs (datasets-server, October 2026): English `medical_o1_sft.json` 19,704 rows; Chinese `medical_o1_sft_Chinese.json` 20,171 rows; English mix 24,887 rows; Chinese mix 25,358 rows. Dataset card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." Fields are `Question`, `Complex_CoT`, and `Response`. The only prompt on the model card is English. Which language split was used: not stated anywhere found.

(d) Base model. Card says: "Base Model: Qwen3-4B (from Qwen by Alibaba)" and YAML `base_model: Qwen/Qwen3-4B`. That checkpoint is post-trained ("Training Stage: Pretraining & Post-training" on https://huggingface.co/Qwen/Qwen3-4B), not `Qwen/Qwen3-4B-Base`.

(e) Card section "Training Configuration" says: "Epochs: 3", "Batch Size: 8", "Optimizer: AdamW", "Learning Rate: 2e-5", "Gradient Accumulation: 4", "Framework: PyTorch, Hugging Face Transformers". Hardware: not stated anywhere found. The same epochs, batch size, and learning rate are printed on the 0.6B GGUF sister card. There is no training log in this repo to check them against.

(f) Evaluation. The card states no scores. It says the model "May hallucinate" and "Trained only on publicly available or synthetic datasets — not real patient data."

(g) Task and language. The named dataset is open medical questions with a written reasoning trace and a final response, so the training task is reasoning traces for open questions, not multiple-choice scoring. The card's intended-use list also names "Summarizing patient records" and "Medical reasoning and triage". Those uses are not what the dataset fields contain. Demonstrated language is English. The dataset also contains a Chinese split, and the card does not say it was used.

### Discrepancies

1. Inventory methods are `sft` and the dataset id matches the card. The inventory does not record an update scope, and none was found.
2. The hyperparameter block is shared, almost unchanged, with the 0.6B and 1.7B XformAI medical cards. It may be a template. Nothing in this repo confirms a finished training run.
3. The HuatuoGPT-o1 paper describes that group's own SFT-then-RL training on about 40k verifiable problems. It does not mention `XformAI-india/Qwen3-4B-medicaldataset`. Those paper details are not this model's training record.
4. "Summarizing patient records" is an intended use on the card, not a dataset this card names.

### Confidence

Medium. Supervised fine-tuning and the dataset id are explicit. The split, the row count used, and the parameter-update scope are not, and the hyperparameters are copied across model sizes.

### Queries tried

1. `XformAI-india Qwen3-4B-medicaldataset supervised fine-tuning medical-o1`
2. `"XformAI-India" OR "XformAI-india" Qwen3 medical github OR arxiv`
3. `HuatuoGPT-o1 medical-o1-reasoning-SFT dataset paper arxiv`
4. `Qwen/Qwen3-4B Hugging Face post-trained vs Qwen3-4B-Base`
5. `site:xformai.in Qwen3-4B-medicaldataset fine-tune`
6. Datasets-server info for `FreedomIntelligence/medical-o1-reasoning-SFT` (row counts by config)

## 3. mlxha/Qwen3-4B-grpo-medmcqa

### Sources

Shared source for the mlxha MedMCQA GRPO series: Michael Ha's fork https://github.com/mlxha/open-r1 (a DeepSeek-R1 / Hugging Face open-r1 fork). The public `recipes/` tree does not contain a MedMCQA config. The medical reward functions are in `src/open_r1/rewards.py` (`mcq_accuracy_reward`, `mcq_accuracy_reward_v2`, `format_reward`, `tag_count_reward`). The run that produced this checkpoint is saved on the model repo, not in that recipes folder.

This model's files:

- Card (cached): `revision_3_experiments/hf_inventory/cache/readmes/mlxha__Qwen3-4B-grpo-medmcqa__2026-10-05.md`. Live: https://huggingface.co/mlxha/Qwen3-4B-grpo-medmcqa
- `training_args.bin` on that repo: an `open_r1.configs.GRPOConfig` (read from the pickle opcodes, not from a prose card)
- `trainer_state.json` and `all_results.json` on that repo
- Dataset: https://huggingface.co/datasets/mlxha/medmcqa-grpo (README is empty). Row counts from the datasets server
- MedMCQA paper for the underlying questions: Pal, Umapathi, and Sankarasubbu, https://arxiv.org/abs/2203.14371
- Weights & Biases link on the card: https://wandb.ai/alexs-team/reasoning/runs/abe1faca-0f47-471a-b13c-22b48a63c0a6. The page did not load. Other mlxha MedMCQA cards point at the same entity and project (`alexs-team` / `reasoning`) with different run ids.

The name contains "grpo". The card also says the method in a sentence: "This model was trained with GRPO, a method introduced in DeepSeekMath."

### Training record

(a) Objective. GRPO, one stage. Card: "This model was trained with GRPO." Tags include `open-r1`, `trl`, and `grpo`. Framework versions on the card: TRL 0.18.0.dev0, Transformers 4.52.0.dev0, PyTorch 2.6.0. No earlier supervised stage is stated for this checkpoint. `do_eval` in the saved config is false.

(b) Parameter-update scope. The saved `GRPOConfig` has no LoRA, QLoRA, or DoRA fields. The upload is two full bfloat16 shards, 4,022,468,096 parameters, the same count as Qwen3-4B, and there is no `adapter_config.json`. The DeepSpeed block in that file has ZeRO stage 3 and `stage3_gather_16bit_weights_on_model_save: true`. Recorded as full-weight training. The open-r1 `ModelConfig`, which is where `use_peft` would be set, is not inside `training_args.bin`, so a merged adapter is not ruled out by a sentence. Rank and alpha: not stated anywhere found.

(c) Training data. Card: "a fine-tuned version of Qwen/Qwen3-4B on the mlxha/medmcqa-grpo dataset." `all_results.json` says `train_samples` 182822, which is the train split. Datasets-server: train 182,822, test 6,150, validation 4,183 (193,155 rows). Columns include the original MedMCQA fields plus `problem` (question plus options A–D) and `solution` (the letter). Dataset README: empty. Pal et al. say MedMCQA is "More than 194k high-quality AIIMS & NEET PG entrance exam MCQs." Those questions are exam items, not model-written. The mlxha card does not say who reformatted them. Language of the questions is English.

(d) Base model. Card YAML: `base_model: Qwen/Qwen3-4B`. Post-trained Qwen3-4B, as in section 2. Not `Qwen/Qwen3-4B-Base`.

(e) From `training_args.bin` (pickle opcodes): `learning_rate` 5e-6, `num_train_epochs` 1.0, `max_steps` -1, `per_device_train_batch_size` 4, `gradient_accumulation_steps` 32, `warmup_ratio` 0.1, `bf16` true, `num_generations` 8, `max_prompt_length` 2048, `max_completion_length` 8192, `temperature` 1.0, `beta` 0.04, `epsilon` 0.2, `num_iterations` 1, `loss_type` bnpo, `use_vllm` true, `reward_weights` [1.0, 0.1, 0.1], `seed` 42, `logging_steps` 5, `save_steps` 50. PartialState in the same file: `num_processes` 2, `distributed_type` DEEPSPEED, `device` cuda, backend nccl. The DeepSpeed config records `train_micro_batch_size_per_gpu` 4 and `train_batch_size` 256, which is 4 × 32 × 2. GPU model name: not stated anywhere found.

The system prompt stored in that file is: "You are a helpful AI Assistant, designed to provided well-reasoned and detailed responses. You FIRST think about the reasoning process as an internal monologue and then provide the user with the answer. The reasoning process and answer are enclosed within <think> </think> and <answer> </answer> tags, respectively. Respond in the following format: <think> ... </think> <answer> X is the correct answer. </answer>" (the ellipsis and the line breaks are in the file; "provided" is the file's spelling).

`trainer_state.json` does not match that learning rate or a finished 1.0 epoch. The log's highest `learning_rate` is 2.999977e-6. The state ends at `global_step` 1904, `epoch` 0.4998933394594772, `max_steps` 1904, `num_train_epochs` 1, `train_runtime` 15331.4788 seconds, `train_loss` 0.0036022694108365965. `train_samples_per_second` 5.962 times that runtime is about 91,411 rows, half of 182,822. Logged reward names are `format_reward`, `mcq_accuracy_reward`, and `tag_count_reward`. The weight list is not labeled, so which weight belongs to which reward is not stated in the file. In `rewards.py`, `mcq_accuracy_reward` scores 1 when a letter inside `<answer>` matches the solution letter, else 0.

(f) Evaluation. No held-out benchmark is reported. `do_eval` is false. The last log step reports training-reward means, not a test accuracy: `rewards/mcq_accuracy_reward/mean` 0.720703125, `rewards/format_reward/mean` 0.96484375, `rewards/tag_count_reward/mean` 0.9879557192325592, overall `reward` 1.2089030146598816.

(g) Task and language. The scored target is the multiple-choice letter. The prompt also requires a `<think>` trace and an `<answer>` letter. Task recorded as multiple-choice exam answering. Language of the data, the system prompt, and the questions is English.

Series note. Other mlxha cards (`Qwen3-8B-grpo-medmcqa`, `Qwen3-8B-grpo-medmcqa-v2`, `Qwen3-8B-grpo-medmcqa-medi70`, `Qwen-2.5-3B-grpo-medmcqa`, `Llama-3.1-8B-Instruct-GRPO-medmcqa`, and others) use the same TRL card template, the tag `open-r1`, and the W&B project `alexs-team/reasoning`. The shared dataset for this 4B run is `mlxha/medmcqa-grpo`. Separate datasets `mlxha/medmcqa-grpo-meditron70b` (16,885 rows) and `mlxha/medmcqa-grpo-meditron8b` exist for the "medi70" runs. Those other runs were not unpacked here.

### Discrepancies

1. `training_args.bin` says learning rate 5e-6. The logged learning rate never exceeds about 3e-6.
2. `training_args.bin` says 1.0 epoch and `max_steps` -1. The saved trainer state stops at epoch 0.50 and step 1904, after about half of the 182,822 training rows. The commit message on the Hub is "End of training".
3. The public GitHub `recipes/` directory has no MedMCQA yaml. The reward code is in the fork; the run config is the file on the model repo.
4. The dataset README is empty, so the reformatting steps are not written down. The column layout matches MedMCQA plus `problem` and `solution`.
5. Inventory methods are `grpo` and the dataset id matches. That part agrees. The inventory does not record the learning-rate mismatch.

### Confidence

Medium. GRPO, the dataset, the base model, and the reward names are directly in the card, the log, and `rewards.py`. The learning rate and the epoch count disagree between the saved config and the training log.

### Queries tried

1. `mlxha Qwen3-4B-grpo-medmcqa GRPO training github open-r1`
2. `mlxha medmcqa-grpo dataset huggingface alexs-team wandb`
3. `mlxha github medmcqa GRPO Qwen "open-r1" site:github.com`
4. `"mlxha" huggingface OR github medmcqa GRPO Qwen`
5. `MedMCQA Pal 2022 AIIMS NEET PG arxiv`
6. `site:github.com/mlxha/open-r1 medmcqa`

## 4 and 5. Baize TCM V1-16bit and V2-16bit

Shared source, read once. No paper and no GitHub repository were found for DigitalIntelligenceCenter-of-ICMM or for 白泽中医药大语言模型. The project-baize paper (Xu et al., https://arxiv.org/abs/2304.01196) is a different model: LoRA on LLaMA using ChatGPT self-chat, including a healthcare LoRA. It does not name these Qwen3 checkpoints or this organization.

Cards (cached):

- V1: `revision_3_experiments/hf_inventory/cache/readmes/DigitalIntelligenceCenter-of-ICMM__Baize-Traditional-Chinese-Medicine-Large-Language-Model-V1-16bit__2026-10-05.md`
- V2: `...V2-16bit__2026-10-05.md`
- Also read, for the series only: the unsuffixed model card and the V3-16bit card, same cache directory, dated 2026-10-05
- Corpus cards: https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V1 and the V2 and V3 dataset pages

What differs across the series, from those cards:

| repo | card's base | card's corpus | card's example count | other card statements |
| --- | --- | --- | --- | --- |
| unsuffixed `...Large-Language-Model` | Qwen3-0.6B (model tree on the live page points at `Qwen/Qwen3-0.6B-Base`) | V3 | the count is blank in the sentence | LoRA; software named as LLaMA-Factory; context listed as 4096; "16bit" listed under 量化方式 |
| V1-16bit | Qwen3-8B | V1 | 4,735 | LoRA; 未量化; context listed as 2048 |
| V2-16bit | Qwen3-8B | V2 | 10,578 | LoRA; 未量化; context listed as 2048 |
| V3-16bit (not in this batch) | Qwen3-8B | V3 | 157,438 | LoRA; 未量化; context listed as 2048 |

V1 and V2 `config.json` files in the inventory cache are byte-identical, including `"unsloth_fixed": true` and `"unsloth_version": "2025.8.9"`. The V3-16bit config has the same two Unsloth fields. The unsuffixed 0.6B config does not, and its card is the only one that names LLaMA-Factory. Weights were not downloaded, so identical configs do not mean identical weights.

Hub safetensors for both V1 and V2: BF16, 8,190,735,360 parameters, four shards, no adapter file. The official Qwen3-8B card says "Number of Parameters: 8.2B" and "Training Stage: Pretraining & Post-training" (https://huggingface.co/Qwen/Qwen3-8B). Both uploads are full checkpoints of that size, not a small adapter file.

Language for the whole series: corpus cards say 语言：中文. Model cards set `language: zh`. The demo prompt on V1 and V2 is Chinese: "问题：气虚的主要症状有哪些？ 答案：". The dataset example is a Chinese instruction about 转录组. No English question, answer, or prompt is shown. English use is not shown.

### V1 training record

(a) Objective. Card says: "基于通用大模型在 **4,735 条高质量中医问答语料** 上进行指令微调（Supervised Fine-Tuning）。" One stage. The corpus card lists "预训练与微调" as things the corpus could be used for. The model card does not say this checkpoint was continued-pretrained.

(b) Parameter-update scope. Card table: "训练方式 | LoRA". Rank, alpha, and target modules: not stated anywhere found. The card also says "量化方式 | 未量化" and loads the repo with `AutoModelForCausalLM` in float16. The repo has no `adapter_config.json`. Whether the LoRA adapter was merged into the uploaded full checkpoint: not stated anywhere found. `config.json` says `unsloth_version` 2025.8.9. The card does not mention Unsloth.

(c) Training data. YAML dataset: `DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V1`. Corpus card: "版本：1.0 语料数量：4,735 条 语言：中文" and "4,735 条经过整理与校对的问答对". Fields in the V2/V3 example, and the same format is described for the series: `instruction`, `input`, `output`, `system`. Who wrote the pairs, and whether a model generated them: not stated anywhere found. Topics named on the corpus card: 中医基础理论, 中药学, 方剂学, 诊断学, 针灸推拿, 经典医籍, 临床实践.

(d) Base model. YAML and the architecture table: Qwen3-8B, Hub id `Qwen/Qwen3-8B`. That is the post-trained model, not `Qwen/Qwen3-8B-Base`.

(e) Epochs, learning rate, batch size, hardware: not stated anywhere found. The table's "上下文长度 | 2048 tokens" is not the `config.json` value. That file has `max_position_embeddings` 40960, the Qwen3 default.

(f) Evaluation. No scores anywhere found.

(g) Task and language. Chinese open traditional-medicine question answering. The card also lists 辅助诊断 and 医学生教学与考试辅助 as uses. The training text it names is QA pairs, not a named exam set and not clinical notes. Use language: Chinese. English use is not shown.

### V2 training record

Same statements as V1 except the count and the corpus id.

(a) Card says: "基于通用大模型在 **10,578 条高质量中医问答语料** 上进行指令微调（Supervised Fine-Tuning）。"

(b) Card: "训练方式 | LoRA". Same missing rank and the same full BF16 upload with no adapter file. Same Unsloth 2025.8.9 fields in `config.json`. Merge: not stated anywhere found.

(c) Dataset `DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V2`. Corpus card: "版本：2.0 语料数量：10,578 条 语言：中文" and "10,578 条经过整理与校对的问答对". The printed example is a Chinese definition of 广义转录组 versus 狭义转录组. Provenance beyond "organized and proofread": not stated anywhere found.

(d) `Qwen/Qwen3-8B`, post-trained, same as V1.

(e) Epochs, learning rate, batch size, hardware: not stated anywhere found. Card context 2048; `config.json` `max_position_embeddings` 40960.

(f) No scores.

(g) Chinese open traditional-medicine QA. English use is not shown.

### Discrepancies

1. The V1 card's Chinese title says V1, and the bold English title says `Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit`. The body then says V1 and 4,735 rows.
2. The V2 card's Chinese title and bold English title both say V3. The body says V2 and 10,578 rows. The YAML dataset is the V2 corpus.
3. Both cards say LoRA and also ship a full 8,190,735,360-parameter BF16 model with no adapter file. They do not say the adapter was merged. They do not give rank or alpha.
4. Both cards say context 2048. Both `config.json` files say `max_position_embeddings` 40960.
5. Unsloth 2025.8.9 is in the config and not on the card. LLaMA-Factory is named only on the unsuffixed 0.6B card, whose model tree points at `Qwen/Qwen3-0.6B-Base` while that card's table says Qwen3-0.6B, and whose example count is blank.
6. Inventory methods `lora|sft` and the V1/V2 corpus ids match the card bodies. The inventory does not record the mislabeled titles.
7. arXiv 2304.01196 is not this series.

### Confidence

Medium for both. The card body states supervised fine-tuning, LoRA, the corpus id, and the row count, and the corpus card states Chinese. Rank, merge, author of the text, epochs, and learning rate are not stated, and the titles name the wrong version.

### Queries tried

1. `Baize Traditional Chinese Medicine Large Language Model ICMM 白泽 LoRA Qwen3`
2. `DigitalIntelligenceCenter-of-ICMM Baize-TCM-Corpus training`
3. `"白泽" 中医药 大语言模型 Qwen3 LoRA 论文`
4. `"Baize-TCM" OR "Baize-Traditional-Chinese-Medicine" OR "白泽中医药大模型" arxiv OR github`
5. `"DigitalIntelligenceCenter-of-ICMM" OR "Digital Intelligence Center" ICMM Baize TCM LLaMA-Factory`
6. `中国中医科学院 白泽中医药大语言模型 微调`

## Patterns in this batch

Two of the five repos, the XformAI model and the Tommi09 chatbot, state a dataset and a base model and ship a full float16 Qwen3-4B-sized checkpoint, and neither states whether training updated every weight or a LoRA adapter. Only the XformAI card uses the words "Supervised fine-tuning (SFT)", and that hyperparameter block is copied onto the smaller XformAI medical cards.

The mlxha 4B model is the one run with a saved trainer file. It is GRPO on English MedMCQA letters, with think and answer tags, from the post-trained Qwen3-4B, using the open-r1 fork's `mcq_accuracy_reward`. The saved config says learning rate 5e-6 and 1 epoch. The training log peaks near 3e-6 and stops at epoch 0.50. The public recipes folder does not contain this MedMCQA config. The run file on the model repo is the source.

The two Baize 8B models are the same card template with a larger Chinese traditional-medicine QA corpus: 4,735 rows for V1 and 10,578 for V2, both LoRA supervised fine-tuning from post-trained Qwen3-8B. Their titles call them V3. Both configs carry Unsloth 2025.8.9, which the cards do not mention, and both uploads are full bfloat16 checkpoints with no adapter file. The unsuffixed 0.6B model is the one that names LLaMA-Factory, and its model tree points at Qwen3-0.6B-Base. No English example is shown for any version in the series. The 2023 Baize self-chat paper is a different project.
