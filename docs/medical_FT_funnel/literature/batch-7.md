# Batch 7: how five medical models were trained

Cached cards read: newest README under `revision_3_experiments/hf_inventory/cache/readmes/` (2026-10-05). Inventory row: `revision_3_experiments/hf_inventory/results/medical/2026-10-06/kept.csv`. Hub file lists: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__005.csv`, `2026-10-05__007.csv`, and `2026-10-05__008.csv`. None of the five repositories contains `adapter_config.json`.

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Task trained for | Language | Matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rishidar/autoscientist-healthcare-qlora | Kaggle model page (same repo name); no paper or script | supervised fine-tuning, then direct preference optimization (Kaggle page) | QLoRA, 4-bit NF4, rank 32, alpha 64 | healthcare adapted rows in `Rishidar/autoscientist-competition-datasets`: 60 English prompt/completion pairs; raw file also has chosen/rejected; produced by Adaption Labs; generator model not named | Qwen/Qwen2.5-0.5B-Instruct (instruction-tuned) | open medical explanation | en | partly |
| abaryan/BioXP-0.5B-MedMCQA | preprint (TechRxiv; full text read from the Exa copy) | supervised fine-tuning, then group relative policy optimization | not stated; paper says the model was quantized and does not name LoRA | MedMCQA (`openlifescienceai/medmcqa`): Hub train split 182,822 English exam questions; paper also says a 50,000-example GRPO run; missing explanations filled with GPT-4.1-mini | Qwen/Qwen2.5-0.5B-Instruct (instruction-tuned) | multiple-choice medical exam, with explanations | en | yes |
| Mingsmilet/Qwen2.5-1.5B-R1-Distill-Medical | trainer log files in the same Hub repo | supervised fine-tuning | not stated; uploaded file is full bfloat16 weights and the training-args text has no LoRA field | `Mingsmilet/Medical-R1-Distill-Data-Chinese`: 10,880 train and 2,720 test Chinese rows; one train question is the same text as a row in FreedomIntelligence's DeepSeek-R1 distillation (17,000 rows) | Qwen/Qwen2.5-1.5B-Instruct (instruction-tuned) | medical questions with reasoning traces | zh | yes |
| Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2 | none beyond the model card and the uploaded config | not stated | QLoRA, 4-bit nf4, rank 16, alpha 32 | MedMCQA; card says about 182k questions and only single-choice items; Hub train split is 182,822; exam questions written for AIIMS and NEET-PG | Qwen/Qwen2.5-1.5B-Instruct (instruction-tuned) | multiple-choice medical exam | en | yes |
| Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned | author's Chinese post on Modelers (CSDN) | supervised fine-tuning | LoRA; rank and alpha not stated | `FreedomIntelligence/medical-o1-reasoning-SFT`; printed examples are Chinese; Chinese config has 20,171 rows; built with GPT-4o; how many rows the run used is not stated | Qwen/Qwen2.5-3B-Instruct (instruction-tuned) | medical questions with reasoning traces | zh (English medical use is not shown) | partly |

## 1. Rishidar/autoscientist-healthcare-qlora

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/Rishidar__autoscientist-healthcare-qlora__2026-10-05.md`. Names this repo id.
- Kaggle model page: https://www.kaggle.com/models/rishidard/autoscientist-healthcare-qlora . Slug `rishidard/autoscientist-healthcare-qlora`. The HTML meta description names this model. The page body is a script shell, so the description is the sentence that was retrieved.
- Dataset files, retrieved 7 Oct 2026 from https://huggingface.co/datasets/Rishidar/autoscientist-competition-datasets : `healthcare_adapted.jsonl` (60 lines) and `healthcare_v5_raw.csv` (60 data rows). `adaption_results.json` in the same repo.
- Hub model API: https://huggingface.co/api/models/Rishidar/autoscientist-healthcare-qlora . Created 2026-06-29. Tag `base_model:finetune:Qwen/Qwen2.5-0.5B-Instruct`.
- Other Rishidar dataset cards (science, language, finance, marketing) state QLoRA supervised fine-tuning plus direct preference optimization for other category models. Those cards do not name `autoscientist-healthcare-qlora`. They are not a source for this checkpoint.
- Featherless page https://featherless.ai/models/Rishidar/autoscientist-healthcare-qlora repeats the Hugging Face card. It is not a second witness.
- GitHub repository search for `autoscientist-healthcare-qlora` returned 0 repositories.
- Adaption's hyperparameter page https://docs.adaptionlabs.ai/autoscientist/recommended-hyperparameters/index.md describes the platform's LoRA and alignment options. It does not name this repo.

### Training record

**(a) Objective.** Kaggle page says: "Qwen2.5-0.5B-Instruct fine-tuned (QLoRA SFT + DPO) for healthcare." That is supervised fine-tuning, then direct preference optimization. The Hugging Face card does not say supervised fine-tuning or direct preference optimization. Card says: "Method: QLoRA (4-bit NF4, r=32, alpha=64)." QLoRA names the update method.

**(b) Parameter-update scope.** Card says: "Method: QLoRA (4-bit NF4, r=32, alpha=64)." Target modules are not stated anywhere found. Whether the adapter was merged: not stated anywhere found. Hub siblings (`2026-10-05__007.csv`): `model.safetensors` only, float16, 494,032,768 parameters. No `adapter_config.json`. That is a full weights file of the 0.5B Qwen2 size.

**(c) Training data.** Card says the model was fine-tuned "on the healthcare adapted dataset" `Rishidar/autoscientist-competition-datasets` "produced by Adaption Labs." `healthcare_adapted.jsonl` has 60 rows with keys `prompt` and `completion`. `healthcare_v5_raw.csv` has the same 60 prompts and columns `prompt`, `completion`, `enhanced_prompt`, `chosen`, `rejected`, `reasoning_trace`. The first prompt is an English explanation task about GLP-1 receptor agonists. Language of the rows read: English. Card language tag: `en`. Provenance: the card says Adaption Labs produced the set. The files do not name a generator model and do not say a person wrote the completions. `adaption_results.json` says healthcare `grade_before` B, `grade_after` A, `improvement_percent` 17.5. Card says: "Dataset quality: Grade A (Adaption Labs evaluation)."

**(d) Base model.** Card YAML: `Qwen/Qwen2.5-0.5B-Instruct`. The Qwen card for that id says: "This repo contains the instruction-tuned 0.5B Qwen2.5 model" and "Training Stage: Pretraining & Post-training" (https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct).

**(e) Hyperparameters.** Card says: "Epochs: 3" and "Learning rate: 0.0002." Batch size and hardware are not stated anywhere found.

**(f) Evaluation.** No medical exam score is stated. The stated evaluation is Adaption's grade: card says Grade A; `adaption_results.json` says a 17.5 percent improvement for the healthcare category.

**(g) Task and language.** The prompts ask for explanations of drugs and a clinical choice (beta-blocker class for a patient with asthma and atrial fibrillation). That is open medical explanation, not a multiple-choice exam. Intended language on the card: English. The rows read are English.

### Discrepancies

1. The Kaggle description says supervised fine-tuning and direct preference optimization. The Hugging Face card says only QLoRA, epochs, and learning rate.
2. Inventory `methods` is `qlora`. That matches the card's update method. It does not record supervised fine-tuning or direct preference optimization.
3. The raw file has `chosen` and `rejected` columns. Those columns show the file can support preference optimization. They do not, by themselves, show that this checkpoint was trained with that loss. The Kaggle sentence is the statement that does.

### Confidence

Medium. The card, the 60-row files, and the Kaggle description agree on this repo name, Qwen2.5-0.5B-Instruct, and QLoRA. No training script was found, and the Hugging Face card never says direct preference optimization.

### Queries tried

- `Rishidar autoscientist-healthcare-qlora QLoRA training Adaption Labs`
- `site:github.com Rishidar autoscientist healthcare qlora` (no matching repository)
- GitHub API search `autoscientist-healthcare-qlora` (total 0)
- `"autoscientist-competition-datasets" healthcare Rishidar`
- Kaggle page https://www.kaggle.com/models/rishidard/autoscientist-healthcare-qlora
- Dataset files `healthcare_adapted.jsonl`, `healthcare_v5_raw.csv`, `adaption_results.json`
- Sibling cards for science, language, finance, and marketing (do not name this repo)
- Adaption recommended-hyperparameters page (platform options, not this run)
- Featherless page (copy of the Hugging Face card)

## 2. abaryan/BioXP-0.5B-MedMCQA

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/abaryan__BioXP-0.5B-MedMCQA__2026-10-05.md`. Names this repo id. Cites https://doi.org/10.36227/techrxiv.175695836.60215814/v1 .
- Preprint: Rasoul Abaryan, "Learning Through Mistakes: Explainable Medical Question-Answering using Reinforcement Learning in Large Language Models," TechRxiv, DOI above. TechRxiv returned HTTP 403 on 7 Oct 2026. The full text used here is the copy at https://exa.ai/library/publication/wxpd5l4vmdl . That copy names BioXP-0.5B and the author Rasoul Abaryan. It does not print `abaryan/BioXP-0.5B-MedMCQA`. The author's site https://abaryan.dev/ lists the same preprint title. A LinkedIn post by Rasoul Abaryan repeats the model card and links the Hub model.
- MedMCQA dataset API: https://huggingface.co/api/datasets/openlifescienceai/medmcqa . Train 182,822, validation 4,183, test 6,150.
- GitHub repository search `BioXP-0.5B MedMCQA abaryan` returned 0 repositories. Other GRPO repositories that use Qwen2.5-0.5B do not name BioXP and are not this training run.
- Semantic Scholar search for the title did not return this preprint.

### Training record

**(a) Objective.** Card says: "1. Supervised Fine-Tuning (SFT)" on MedMCQA, then "2. Group Relative Policy Optimization (GRPO)." Paper says: "standard Supervised Fine-Tuning (SFT) ... is used with structured prompts to guide the model to select the correct option (A, B, C, or D) and provide an accompanying explanation. In the second stage, the model is further refined using Group Relative Policy Optimization (GRPO) ... with custom-designed reward functions targeting answer correctness, XML-format compliance ... and reasoning coherence." The paper says GRPO compares a group of generated answers and does not use a separate reward model. That is reward-based reinforcement learning (GRPO), not direct preference optimization and not PPO.

**(b) Parameter-update scope.** Not stated anywhere found. The paper says: "Model: Fine-tuning of the quantized Qwen-2.5-0.5B-Instruct model" and "memory-efficient quantization settings." It does not say LoRA, QLoRA, rank, alpha, or target modules. Hub siblings (`2026-10-05__008.csv`): `model.safetensors` only, float16, 494,032,768 parameters. No `adapter_config.json`. The uploaded file is float16, not a 4-bit file.

**(c) Training data.** Card YAML: `openlifescienceai/medmcqa`. Dataset card says: "MedMCQA has more than 194k high-quality AIIMS & NEET PG entrance exam MCQs" and `language_creators: expert-generated`, language English. Hub counts: train 182,822, validation 4,183, test 6,150. Paper says: "Training set: 182,822 questions" and "Validation set: 4,183 questions." Paper also says: "Missing explanations were filled using GPT-4.1-mini." Another sentence says "GPT-4-mini." Paper says: "Using just 50k examples (about 27% of the data) yielded similar results (~64.6%) to using the full dataset." Provenance: human-written exam items, with synthetic explanations from GPT-4.1-mini where the original explanation was missing.

**(d) Base model.** Card: `Qwen/Qwen2.5-0.5B-Instruct`. Paper says both "Qwen-v2.5-0.5B" and "quantized Qwen-2.5-0.5B-Instruct." The Hub base id is the instruction-tuned checkpoint. Qwen's card for that id says it "contains the instruction-tuned 0.5B Qwen2.5 model."

**(e) Hyperparameters.** Paper says supervised fine-tuning used "Learning Rate: 3e-5" and "Epochs: 7." It says the GRPO stage used "a lower learning rate of 3e-5" after trials at 2e-6 and 5e-6, "Over 2 epochs," temperature 0.6, and top_p 0.9. It says "SFT performed on 2× NVIDIA RTX 4090 GPUs, and GRPO on 8× RTX 4090 GPUs (via Vast.ai)." Batch size is not stated. A later sentence says "Current experiments use a 1024-token cap."

**(f) Evaluation.** Card says: "The final model achieves an accuracy of 64.58% on the MedMCQA benchmark." Paper abstract says the same 64.58%, from a zero-shot baseline of about 23% and a supervised-fine-tuning stage of about 52%. On the 2,205 validation items that have explanations, the paper reports BERTScore 0.834, BLEU 0.032, and ROUGE-1 0.257. Another paragraph says the GRPO model "reached 64.36% accuracy." A future-work sentence says "the current 64.7%."

**(g) Task and language.** Multiple-choice medical exam questions (four options) plus an explanation. Card language: English. MedMCQA language tag: English.

### Discrepancies

1. The extracted preprint gives three final accuracies: 64.58%, 64.36%, and 64.7%. The model card matches 64.58%.
2. The paper describes both a full 182,822-question supervised run and a 50,000-example GRPO run that reached about 64.6%. It does not say which of those runs is the uploaded file.
3. One sentence says GPT-4.1-mini filled missing explanations. Another says GPT-4-mini.
4. The paper says the trained model was quantized. The uploaded weights are a float16 file of 494,032,768 parameters. The paper does not say those float16 weights were dequantized after training.
5. Inventory `methods` is `grpo|sft`. Both stages are what the card and paper describe. The paper's order is supervised fine-tuning, then GRPO.

### Confidence

Medium. The card, the author, the DOI, and the 64.58% figure tie this repo to the preprint. The preprint text disagrees with itself on the final accuracy, the example count used in GRPO, and the name of the explanation model, and it never states LoRA or full-weight updates.

### Queries tried

- `BioXP-0.5B-MedMCQA techrxiv 10.36227/techrxiv.175695836.60215814 GRPO SFT`
- `techrxiv 175695836.60215814 Abaryan BioXP pdf`
- TechRxiv DOI and full-text URL (403)
- Exa full text of the preprint
- https://abaryan.dev/ and the LinkedIn post by Rasoul Abaryan
- GitHub API search `BioXP-0.5B MedMCQA abaryan` (total 0)
- `"BioXP-0.5B" Abaryan github GRPO 4090` (other people's GRPO scripts; none name BioXP)
- Semantic Scholar title search (this preprint was not in the results)
- MedMCQA dataset API row counts

## 3. Mingsmilet/Qwen2.5-1.5B-R1-Distill-Medical

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/Mingsmilet__Qwen2.5-1.5B-R1-Distill-Medical__2026-10-05.md`. Names this repo id.
- Trainer files in the same repo, retrieved 7 Oct 2026: https://huggingface.co/Mingsmilet/Qwen2.5-1.5B-R1-Distill-Medical/resolve/main/trainer_state.json , `train_results.json`, `all_results.json`, and `training_args.bin`. `trainer_state.json` says `num_train_epochs` 1 and `train_batch_size` 4. `training_args.bin` is a pickle of class `SFTConfig` from `open_r1.configs`. It did not unpickle cleanly. A strings listing of the file contains `SFTConfig`, `bf16`, `flash_attention_2`, `cosine_with_min_lr`, output directory `data/Qwen2.5-1.5B-R1-Distill-Medical`, and log directory `.../Feb28_15-48-57_micro4028`. The strings listing does not contain `lora` or `peft`.
- Dataset API: https://huggingface.co/api/datasets/Mingsmilet/Medical-R1-Distill-Data-Chinese . Train 10,880 examples, test 2,720. The dataset README is only the split table. It does not name a generator.
- FreedomIntelligence dataset card: https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data-Chinese . Says: "This dataset is an SFT dataset distilled from Deepseek-R1 (Full Power Version), based on Chinese medical verifiable problems from HuatuoGPT-o1." "The distillation originates from the native Deepseek-R1 API requests." Datasets-server size: 17,000 rows. Column names match Mingsmilet's `question`, `reasoning (reasoning_content)`, and `response (content)`.
- Row check: Mingsmilet train row 0, the arteriovenous-malformation question, is the same question and the same opening reasoning text as row 3369 of the FreedomIntelligence file.
- Weights & Biases link on the card, https://wandb.ai/1653401183-mingmingai/huggingface/runs/b3bymjh8 , returned HTTP 301 and no public run text.
- GitHub repository search `Mingsmilet Medical-R1-Distill` returned 0 repositories.
- mradermacher GGUF pages copy the model card and add a language tag `en`. That tag is not on the Mingsmilet card.

### Training record

**(a) Objective.** Card says: "This model was trained with SFT." Tags include `sft`, `trl`, and `generated_from_trainer`. The uploaded `training_args.bin` is an `SFTConfig`. That is supervised fine-tuning. The repo name and the dataset name contain "Distill." Those names are not a distillation loss. The FreedomIntelligence card uses "distilled" for how DeepSeek-R1 wrote the Chinese answers.

**(b) Parameter-update scope.** Not stated anywhere found. The card does not say LoRA, QLoRA, or full updates. The strings of `training_args.bin` include `bf16` and do not include `lora` or `peft`. Hub siblings (`2026-10-05__005.csv`): `model.safetensors` only, bfloat16, 1,543,714,304 parameters. No `adapter_config.json`. `config.json` `_name_or_path` is `Qwen/Qwen2.5-1.5B-Instruct`.

**(c) Training data.** Card YAML: `Mingsmilet/Medical-R1-Distill-Data-Chinese`. Dataset API: 10,880 train rows and 2,720 test rows. `train_results.json` says `train_samples` 10880, the same count as the train split. Language: the card's own example and the dataset rows are Chinese (a traditional-medicine formula question, and exam items with options A–E). The Mingsmilet dataset card does not say who wrote the answers. The FreedomIntelligence card, whose file contains the same arteriovenous-malformation item, says the answers were distilled from DeepSeek-R1. Mingsmilet has 13,600 rows in total. FreedomIntelligence has 17,000. This note does not claim every Mingsmilet row is in the 17,000.

**(d) Base model.** Card: `Qwen/Qwen2.5-1.5B-Instruct`. That id is the instruction-tuned Qwen2.5 checkpoint of this size. The 0.5B Instruct card, which uses the same series wording, says the Instruct repo is the instruction-tuned model, as distinct from the base model.

**(e) Hyperparameters.** `trainer_state.json` says `num_train_epochs` 1, final `epoch` 0.9970559371933267, `global_step` 254, `max_steps` 254, `train_batch_size` 4. The highest learning rate written in the log is 4.999235366054742e-05 at step 15, then the logged rate falls. The scheduler name in the pickle strings is `cosine_with_min_lr`. Gradient accumulation, the exact configured learning rate, and the GPU model are not stated. The log directory name ends in `micro4028`. `train_results.json` says `train_runtime` 4436.1847 seconds and `train_loss` 1.2186088543238602. Card framework lines: TRL 0.15.2, Transformers 4.49.0, PyTorch 2.5.1.

**(f) Evaluation.** The log records `eval_loss` 1.2679216861724854 at step 50, then 1.219738245010376, 1.1888347864151, 1.1670364141464233, and 1.1561425924301147 at step 250. No exam accuracy is stated. The logged eval rate does not equal 2,720 divided by the eval runtime, so the log does not by itself say the 2,720-row test split was the eval set.

**(g) Task and language.** The targets are long Chinese reasoning traces plus an answer. The questions are medical exam items, some with options A–E and some open (the card's formula question has no options). Intended language shown by the card example and the dataset: Chinese. No English medical example is on the card.

### Discrepancies

1. The model name contains "Distill." The card and `SFTConfig` say supervised fine-tuning.
2. mradermacher's GGUF card tags this model as language `en`. The training example and the dataset rows are Chinese.
3. Inventory `methods` is `sft` and `datasets` is `Mingsmilet/Medical-R1-Distill-Data-Chinese`. Both match the card and the trainer log.

### Confidence

High for supervised fine-tuning, one epoch, batch size 4, 10,880 train rows, and Chinese questions. Medium for calling the answers DeepSeek-R1 text, because that sentence is on FreedomIntelligence's card and only one shared row was checked. The parameter-update scope is not stated.

### Queries tried

- `Mingsmilet Qwen2.5-1.5B-R1-Distill-Medical Medical-R1-Distill-Data-Chinese SFT`
- Dataset page and API for `Mingsmilet/Medical-R1-Distill-Data-Chinese`
- `FreedomIntelligence/Medical-R1-Distill-Data-Chinese` card and the 17,000-row JSON
- Row comparison of the arteriovenous-malformation question
- Trainer files `trainer_state.json`, `train_results.json`, `training_args.bin`
- Weights & Biases run `b3bymjh8` (no public text)
- GitHub API search `Mingsmilet Medical-R1-Distill` (total 0)
- mradermacher GGUF card (copy, plus an English language tag)

## 4. Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/Satya-Dey__qwen2.5-1.5b-medmcqa-qlora-v2__2026-10-05.md`. Names this repo id.
- Uploaded `config.json`, cached as `revision_3_experiments/hf_inventory/cache/configs/Satya-Dey__qwen2.5-1.5b-medmcqa-qlora-v2__2026-10-06.json`. Contains `"unsloth_fixed": true` and `"unsloth_version": "2026.8.15"`. That says Unsloth wrote this config. It does not state the loss.
- MedMCQA dataset API, as in section 2. Hub model created 2026-08-12.
- GitHub API search `qwen2.5-1.5b-medmcqa-qlora-v2` returned 0 repositories.
- Searches for the repo id, for "Satya" with Unsloth, and for "42.5%" with "step 5600" found other people's Qwen2.5-1.5B QLoRA projects (MedQuAD, SQL, code, English proficiency). None of those pages name this repo. A step-5600 line in an unrelated repository reports 29.2% accuracy, not this card's 42.5%.

### Training record

**(a) Objective.** Not stated anywhere found. Card says: "Fine-tuned version of Qwen2.5-1.5B-Instruct on the MedMCQA dataset using QLoRA." It does not say supervised fine-tuning, preference optimization, or reinforcement learning. The name contains `qlora`. That names the update method.

**(b) Parameter-update scope.** Card says: "Method | QLoRA (4-bit nf4 + LoRA)", "LoRA rank | 16", "LoRA alpha | 32." Target modules are not stated. Whether the adapter was merged: not stated anywhere found. Hub siblings (`2026-10-05__008.csv`): `model.safetensors` only, bfloat16, 1,543,714,304 parameters. No `adapter_config.json`.

**(c) Training data.** Card YAML and prose: `openlifescienceai/medmcqa`. Card says: "MedMCQA contains ~182k multiple-choice questions from AIIMS and NEET-PG Indian medical entrance exams across 23 subjects. Only single-choice questions were used for training and evaluation." Hub train split is 182,822 questions of all choice types. The exact single-choice training count is not stated. Dataset card: expert-generated, language English. Provenance: human-written exam questions. No synthetic generator is named.

**(d) Base model.** Card: `Qwen/Qwen2.5-1.5B-Instruct`. That is the instruction-tuned Qwen2.5 checkpoint of this size.

**(e) Hyperparameters.** Card says: learning rate "2e-4 (cosine schedule)", "Epochs | 1", "Effective batch size | 16", "Best checkpoint | Step 5600 (selected by lowest eval loss)", "Hardware | Google Colab A100 40GB."

**(f) Evaluation.** Card says: "Evaluated on the full MedMCQA validation set (2,816 single-choice questions)" and accuracy 42.5% for this model, "~39% (estimated)" for the base model, and 25% for a random baseline. The Hub validation split has 4,183 rows, so 2,816 is the single-choice subset the card describes, not the full validation file. Subject rows on the card include Biochemistry 60.7% (122 questions) and Dental 37.0% (845 questions).

**(g) Task and language.** Multiple-choice medical exam answering. The usage prompt ends with `### Answer:` and `max_new_tokens=5`. Card language: English.

### Discrepancies

1. Inventory `methods` is `qlora` and `datasets` is `openlifescienceai/medmcqa`. Both match the card. The card does not name the training loss, so the objective cell in the table is "not stated" even though the inventory method word is QLoRA.
2. The card says the model was evaluated on "the full MedMCQA validation set (2,816 single-choice questions)." The Hub validation split has 4,183 rows. The 2,816 count is the single-choice subset.

### Confidence

High for the QLoRA settings, the base model, the hardware, and the 42.5% figure, because they are all on this model's card and no second source contradicts them. Low for any claim that the loss was supervised next-token training, because the card does not say that.

### Queries tried

- `Satya-Dey qwen2.5-1.5b-medmcqa-qlora-v2 QLoRA MedMCQA training`
- `"qwen2.5-1.5b-medmcqa-qlora-v2" Satya unsloth`
- `"42.5%" MedMCQA Qwen2.5-1.5B Satya-Dey OR "step 5600" qlora`
- GitHub API search `qwen2.5-1.5b-medmcqa-qlora-v2` (total 0)
- Nearby repos that do not name this model: `AliB0239/medical-qa-qlora-finetune-qwen`, `Pk3112/medmcqa-lora-qwen2.5-7b-instruct`, `melc030/MedQwen`
- Uploaded `config.json` (`unsloth_version` 2026.8.15)
- MedMCQA dataset API

## 5. Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/Joker-sxj__Qwen2.5-3B-instruct-medical-finetuned__2026-10-05.md`. The only prose is one Chinese sentence. YAML names this base model and `FreedomIntelligence/medical-o1-reasoning-SFT`.
- Uploaded `config.json`: `_name_or_path` is `D:\\Project\\llamaFactory\\Qwen2.5-3B-instruct`. `transformers_version` is 4.49.0.
- `Modelfile` in the same repo: "ollama modelfile auto-generated by llamafactory" and `SYSTEM """You are a helpful assistant."""`
- Author post, joker_sxj, 3 May 2025: https://modelers.csdn.net/69a7882a7bbde9200b9d09b8.html . Title: "[一文解决大模型微调+部署+RAG] LLamaFactory微调模型后使用Ollama + RAGFlow在Windows本地部署". The Hub repo was created 2025-03-25, before the post. The post does not print `Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned`. It does print the same Windows path as `config.json`.
- Dataset size API for `FreedomIntelligence/medical-o1-reasoning-SFT`: English config 19,704 rows; Chinese config 20,171 rows; English mix 24,887; Chinese mix 25,358. Dataset card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier."
- The post's example question "哪种中药方剂最适合小儿使用" occurs in `medical_o1_sft_Chinese.json`.
- Hub siblings (`2026-10-05__005.csv`): two bfloat16 shards, 3,085,938,688 parameters, plus `Modelfile`. No `adapter_config.json`.
- GitHub user search `Joker-sxj` returned 0 users. The model discussions page has no posts.
- A preprint about a 3B QLoRA run on this same dataset (Exa record "A Compact 3B Language Model...") does not name Joker-sxj. Its hyperparameters are not used here.

### Training record

**(a) Objective.** The post says: "训练阶段设置为 Supervised Fine-Tuning." It then defines that as training on labeled data for a task such as question answering. It lists reward modeling, PPO, DPO, and pre-training as other choices and does not say those were selected. The dataset name contains `SFT`. The training-stage sentence is the statement. Card prose does not say supervised fine-tuning. Card says: "模型经过医疗数据集微调后，已初步具备推理能力，可以进行基础的问诊，且文本的质量BLEU比原模型更优。"

**(b) Parameter-update scope.** The post says the fine-tuning method was set to `lora`, and that full updates and freeze updates were not chosen because they need more compute. It discusses LoRA rank in general and says one can start from small values such as 8, 10, or 12. It does not say which rank or alpha was used. Whether the adapter was merged: not stated. The post says the checkpoint is exported from LLaMA-Factory and that export writes a Modelfile. The Hub upload is two bfloat16 shards totaling 3,085,938,688 parameters and a Modelfile that says it was auto-generated by LLaMA-Factory. There is no `adapter_config.json`.

**(c) Training data.** Card YAML: `FreedomIntelligence/medical-o1-reasoning-SFT`. The post says the fine-tuning set is that dataset, "是使用 GPT-4o 构建的", and shows Chinese fields `Question`, `Complex_CoT`, and `Response`. The printed questions are a pediatric formula question and a 17-year-old with suspected atypical pneumonia. The pediatric question is in the Chinese JSON file, which has 20,171 rows. The post does not say the run used all 20,171 rows, and it does not say the English file (19,704 rows) was the training file. Provenance, from the dataset card: synthetic, generator GPT-4o, checked by a medical verifier. The underlying problems are "verifiable medical problems." The post does not say a person wrote the chain-of-thought.

**(d) Base model.** Card YAML: `Qwen/Qwen2.5-3B-Instruct`. The post says the model name was set to `Qwen2.5-3B-Instruct` and the files were placed in `D:\Project\llamaFactory\Qwen2.5-3B-instruct`. That path is the `_name_or_path` in the uploaded config. The Instruct id is the instruction-tuned Qwen2.5 checkpoint. The Hub model tree lists `Qwen/Qwen2.5-3B` as the parent of `Qwen/Qwen2.5-3B-Instruct`.

**(e) Hyperparameters.** The post says: "训练轮次根据数据集大小调整，这里设置为 100." Compute type: `bf16`. Learning rate: the post says "学习率通常设置为 1e-4 或 5e-5." That sentence says what is usual. It does not say which value this run used. Batch size, the LoRA rank that was used, and the GPU model are not stated. The environment check in the post prints `torch.__version__` as `2.6.0+cu126`. The uploaded config says `transformers_version` 4.49.0, and the repo was created on 25 March 2025, before the 3 May 2025 post, so that torch line is the write-up environment, not a field in the uploaded config.

**(f) Evaluation.** Card YAML metric: `bleu`. Card says the BLEU of the text is better than the original model. No BLEU number is stated. The post does not mention BLEU. It says to compare the model before and after fine-tuning with `ollama run qwen3b-finetuning`.

**(g) Task and language.** The post trains on a question, a chain-of-thought (`Complex_CoT`), and a response. The printed items are Chinese medical exam questions, not a patient-doctor dialogue transcript. The card says the model can do basic consultation (问诊). Training language shown by the post's examples: Chinese. English medical use: not shown. The Modelfile system line is the English sentence "You are a helpful assistant.", which is the default Qwen chat template, not a medical English example. The card's language list is `zho`, `eng`, `fra`, `spa`, `por`, `deu`, `ita`, `rus`, `jpn`, `kor`, `vie`, `tha`, `ara`. The post does not say the model was trained in those languages. The dataset repo does contain an English file. The examples the author printed are the Chinese ones.

### Discrepancies

1. The card lists 13 language codes, including English. The author's training examples are Chinese. No English medical question is shown on the card or in the post.
2. Inventory `methods` is `sft`, taken from the dataset name on the card. The post does say supervised fine-tuning, and it also says LoRA. The inventory row does not say LoRA.
3. The post sets epochs to 100 and does not record a finished run, a loss, or a BLEU number. The card claims a better BLEU and does not give the number.
4. The post's learning-rate sentence is "usually 1e-4 or 5e-5." That is not a recorded learning rate for this file.

### Confidence

Medium. The Windows path in `config.json`, the LLaMA-Factory Modelfile, the dataset id, and the author name `joker_sxj` tie the Hub file to the post. The post is a tutorial published after the upload, it does not print the Hub id, and it does not state rank, alpha, batch size, or the learning rate that was used.

### Queries tried

- `Joker-sxj Qwen2.5-3B-instruct-medical-finetuned medical-o1-reasoning-SFT LLaMA-Factory`
- Author post https://modelers.csdn.net/69a7882a7bbde9200b9d09b8.html
- `Modelfile` and `config.json` `_name_or_path` on the Hub repo
- `FreedomIntelligence/medical-o1-reasoning-SFT` card, README, and datasets-server row counts
- Search of `medical_o1_sft_Chinese.json` for the post's pediatric-formula question
- GitHub user search `Joker-sxj` (total 0) and the empty Hub discussions page
- Qwen LLaMA-Factory documentation (generic Qwen recipe; it does not name this repo)
- The unrelated 3B MedQA preprint that uses the same dataset and does not name this repo
- model.aibase.com page (a restatement of the card, including the 13 language names)

## Patterns in this batch

Four of the five cards name a training method, and one of those four still leaves the loss unnamed. Satya-Dey's card specifies QLoRA rank, alpha, epochs, learning rate, batch size, hardware, and a 42.5% MedMCQA accuracy, and it never says supervised fine-tuning or any other loss. Rishidar's Hugging Face card says only QLoRA; the Kaggle description of the same model name adds supervised fine-tuning and then direct preference optimization, on 60 English healthcare prompts.

BioXP is the only model in this batch with a preprint. The preprint and the card agree on supervised fine-tuning and then GRPO on MedMCQA, with a reported accuracy of 64.58%. The preprint text also contains 64.36% and 64.7%, and it says both a full 182,822-question run and a 50,000-example GRPO run. It says the model was quantized and does not say LoRA. The uploaded file is float16.

The two Chinese-facing models are supervised fine-tunes whose names or datasets say "distill" or "SFT" because of how the answers were written, not because a second loss was stated. Mingsmilet's own trainer log says one epoch of `SFTConfig` on 10,880 Chinese reasoning rows. Joker-sxj's card is one Chinese sentence plus a 13-language tag list; the author's LLaMA-Factory post shows Chinese GPT-4o reasoning examples, LoRA, and 100 epochs, and it does not show an English medical example. None of the five repos uploaded an `adapter_config.json`.
