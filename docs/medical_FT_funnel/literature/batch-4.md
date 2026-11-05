# Medical fine-tune literature, batch 4

Five Hugging Face models. The question for each is what training objective and parameter update produced the uploaded weights, on what data, from what base, and for what medical task.

| model | source found | objective | update scope | data (name, n, provenance) | base | task trained for | language | matches inventory row |
|---|---|---|---|---|---|---|---|---|
| ruslanmv/ai-medical-model-32bit | none | not stated | not stated | ruslanmv/ai-medical-dataset, 21,210,000 rows in the dataset-card YAML (prose says about 27 million), question/context rows drawn from ClinicalTrials, EMEA, and PubMed | meta-llama/Meta-Llama-3-8B-Instruct (instruction-tuned) | open medical question answering | en | yes |
| MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged | paper | supervised next-token fine-tuning | QLoRA, then merged | MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset, 1,651,357 examples, mixed expert-written and machine-written medical instructions | meta-llama/Llama-3.1-8B-Instruct (instruction-tuned) | multiple-choice exams, open medical questions, and patient–doctor replies | en | yes |
| empirischtech/Llama-3.1-8B-Instruct-MedQA | dataset card | not a named method; the model card says “reinforcement learning” | not stated | empirischtech/med-qa-orpo-dpo, 357,058 pairs, human exam and literature items reformatted into chosen/rejected answers | meta-llama/Llama-3.1-8B-Instruct (instruction-tuned) | multiple-choice and yes/no medical questions | en | partly |
| graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5 | code | supervised next-token fine-tuning | full weights | graliuce/MedMCQA.20.01, 4,780 train / 100 test, synthetic doctor–patient prefixes with GPT-4o reasons, built from MedMCQA cases | meta-llama/Llama-3.1-8B-Instruct (instruction-tuned) | a written reason plus a stop-or-diagnose decision | en | yes |
| mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa | code | GRPO | not stated | mlxha/medmcqa-grpo-meditron70b, 16,885 rows, MedMCQA items whose stored answer is the correct option letter | meta-llama/Llama-3.1-8B-Instruct (instruction-tuned) | multiple-choice exam answering, with a required think/answer format | en | yes |

## 1. ruslanmv/ai-medical-model-32bit

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/ruslanmv__ai-medical-model-32bit__2026-10-05.md`. Hub config `cache/configs/ruslanmv__ai-medical-model-32bit__2026-10-06.json` stores `"torch_dtype": "float32"`.
- Dataset card: https://huggingface.co/datasets/ruslanmv/ai-medical-dataset/raw/main/README.md
- A related notebook exists and does not document this checkpoint: https://github.com/ruslanmv/Meta-Llama3-Fine-Tuning/blob/master/How-to-FineTune-Llama-3-with-SFTTrainer.ipynb
- No paper, blog post, or gist was found that says how `ai-medical-model-32bit` was trained. The author’s other medical Llama notebooks train or serve `Medical-Llama3-v2` and a Mixtral chatbot, on `ruslanmv/ai-medical-chatbot`, not this model.

### Training record

(a) Objective. Not stated. Card says: “This repository provides a fine-tuned version of the powerful Llama3 8B Instruct model.” The card tags include `trl`. That tag names a library. It does not say supervised fine-tuning, preference optimization, or reinforcement learning.

(b) Parameter update. Not stated. The uploaded config is a full `LlamaForCausalLM` in float32. There is no adapter file in the cached config. The name contains `32bit`. The config’s `torch_dtype` is `float32`. Nothing found says that training itself ran in 32-bit, or that an adapter was merged.

The notebook above does use this dataset and this base with QLoRA (4-bit NF4, LoRA `r=32`, `lora_alpha=16`, targets `k_proj`, `q_proj`, `v_proj`, `up_proj`, `down_proj`, `gate_proj`) and `SFTTrainer`. It then does `dataset.select(range(100))`, sets `max_steps = 5`, and saves the name `ai-medical-model`. Those settings are a short demo. They are not a record of the published `ai-medical-model-32bit` weights.

(c) Data. Card says it “leverages the rich knowledge contained in the AI Medical Dataset (ruslanmv/ai-medical-dataset).” Dataset card YAML: 21,210,000 train rows, columns `question` and `context`, language `en`. Prose on the same card says: “approximately 27 million rows” and “Total rows: 27,000,000.” Sources named on that card: ClinicalTrials (127.4M words), EMEA (12M words), PubMed (968.4M words). How the question strings were written is not stated. No generator model is named.

(d) Base. Card says: “Finetuned from model: meta-llama/Meta-Llama-3-8B-Instruct.” That base is the instruction-tuned Llama 3 8B, not the pretrained base.

(e) Epochs, learning rate, batch size, hardware. Not stated anywhere found for this checkpoint.

(f) Evaluation on the model card, Open LLM Leaderboard: average 67.67; AI2 Reasoning Challenge (25-shot) 61.43; HellaSwag (10-shot) 78.69; MMLU (5-shot) 68.10; TruthfulQA (0-shot) 51.99; Winogrande (5-shot) 75.77; GSM8k (5-shot) 70.05. These are general benchmarks, not a medical exam score.

(g) Task and language. Card says the model is “specifically designed to answer medical questions in an informative way.” The training rows are a question and a context, not a multi-turn chat and not a multiple-choice exam. Language on the model card and the dataset card: English.

### Discrepancies

1. The dataset card’s YAML count is 21,210,000 rows. The same card’s prose says about 27,000,000 rows.
2. The author’s SFT notebook uses this dataset and this base, then trains for 5 steps on 100 rows and saves a different name.
3. Inventory methods cell is empty. That agrees with the card, which does not name a training algorithm.

### Confidence

Low. The base and the dataset name are on the model card. The training algorithm and which rows were actually used are not.

### Queries tried

`ruslanmv ai-medical-model-32bit fine-tune Llama3`; `site:ruslanmv.com ai-medical-model llama fine-tuning`; `github ruslanmv ai-medical-dataset SFTTrainer`; `huggingface ruslanmv/ai-medical-dataset rows description`; `"ai-medical-model-32bit" notebook OR kaggle OR blog`; `site:github.com/ruslanmv "ai-medical-model" SFTTrainer`; GitHub gist list for user `ruslanmv` (no gist text matched this model).

## 2. MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged

### Sources

- Paper: Abo El-Enen, Ismail, and Nazmy, “Med-LLaMA3: Advancing Medical Question-Answering Through Parameter-Efficient Fine-Tuning of Large Language Models,” *Applied Sciences* 2026, 16(12), 6158. https://www.mdpi.com/2076-3417/16/12/6158 DOI 10.3390/app16126158. Full text read, including Tables 4–7.
- Model card: `revision_3_experiments/hf_inventory/cache/readmes/MohamedAhmedAE__Llama-3.1-8B-Instruct-Medical-Finetuned-merged__2026-10-05.md`
- Dataset card: https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset/raw/main/README.md
- Code linked by the paper and both cards: https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers
- Adapter-only sibling, same recipe: https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned

The paper, the merged-model card, and the adapter card describe one 8B run. The numbers below are the 8B column, not the 1B or 3B variants.

### Training record

(a) Objective. Supervised next-token training on instruction–response pairs. Paper Table 5: “Task type | Causal language modeling.” Dataset card says the rows are “delivered in a unified instruction format suitable for supervised fine-tuning (SFT) / instruction-tuning of causal language models.” This is not preference optimization and not reinforcement learning. The paper discusses distillation only as a method the authors did not use: “rather than compressing a large model through distillation, we adopted parameter-efficient fine-tuning.”

(b) Parameter update. QLoRA, then the adapter was merged into this repo. Paper: “4-bit NF4 quantization and LoRA adapters (r = 128, α = 256) applied to all linear layers, training only ∼4% of the parameters.” Table 5, shared across the 1B, 3B, and 8B runs: rank 128, alpha 256, dropout 0.05, bias none, all linear layers (q, k, v, o, gate, up, down). 8B trainable parameters in the paper: 335.54 million of 8.36 billion (4.01%). Card says: “QLoRA fine-tuning (4-bit NF4 base + LoRA, r=128, α=256, all linear layers), then merge_and_unload() into the base.” This repository is the merged checkpoint. The adapter-only weights are a different repo. Released weights here are bf16/fp16, not the 4-bit training copy. Quantization during training was 4-bit NF4 with double quantization.

(c) Data. Hub id `MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`. Dataset card: 1,651,357 examples (about 1,636,957 train and about 14,400 validation), English. `annotations_creators`: expert-generated and machine-generated. Paper: “a medical instruction dataset of over 1.5 million samples.” Row types on the dataset card: `QA`, `MCQ`, and `CASE`. The dataset card’s source table (counts it attributes to the paper) includes MIMIC-III 465,200, UMLS 312,450, MedDialog (EN) 257,337, MedMCQA 194,000, HealthCareMagic 112,165, WikiDoc Patient Info 67,233, Alpaca-EN-AN 52,000, Medical Flashcards 33,955, ChatDoctor (iCliniq) 30,000, CORD-19 17,721, MEDIQA 16,412, MedQA-USMLE 12,723, WikiDoc 10,000, CovidDialog (EN) 6,032, PubMed Causal 2,446. The model card says MMLU medical subsets were held out, and that MedMCQA, MedQA-USMLE, and PubMedQA contributed only their official training splits.

(d) Base. Card and paper: `meta-llama/Llama-3.1-8B-Instruct`, the instruction-tuned checkpoint. Card: “the 8B uses LLaMA 3.1, not 3.2.”

(e) Paper Table 5, 8B column, matching the model card: learning rate 2.0×10⁻⁵, cosine annealing, 5 warmup steps, 5 epochs, max sequence length 4096, batch size 1 per device, gradient accumulation 4, max gradient norm 1.0, Paged AdamW 8-bit (β1 0.9, β2 0.999), weight decay 0.1, float16, gradient checkpointing. Hardware on the card: “2 × NVIDIA T4 (30 GB total, free-tier Kaggle); ~15–25 days per run.” The paper says one rank-128 all-linear run sits at the upper end of that 15–25 day range, and that six LoRA configurations plus evaluation took 183 calendar days on preemptible free-tier GPUs.

(f) Paper and card, EleutherAI harness v0.4.2, 5-shot. Mean of eight MMLU medical subsets: 75.71% (Anatomy 71.11, Clinical Knowledge 79.62, College Biology 84.03, College Medicine 67.63, Medical Genetics 84.00, Nutrition 83.66, Professional Medicine 77.21, Virology 58.43). MedMCQA 61.8, MedQA 62.4, PubMedQA 77.0. Zero-shot NER on 100 MIMIC-III discharge summaries: macro F1 0.94 (Disease F1 0.92, Procedure F1 0.95); dual-annotator κ 0.87. The NER numbers are an evaluation. The dataset card does not list NER labels as a training task.

(g) Task and language. The corpus mixes multiple-choice exam items, open questions, and patient–doctor replies. English only, stated on the model card and the dataset card.

### Discrepancies

1. The model-card YAML lists eleven Hub datasets (the MedAlpaca subsets, MedMCQA, BigBIO MedQA, PubMedQA, and COVID-QA). The dataset card’s source table also counts MIMIC-III, UMLS, MedDialog, HealthCareMagic, Alpaca-EN-AN, ChatDoctor, and CovidDialog. The model-card prose names MedQuAD, which is not a row in that source table (MEDIQA is).
2. Inventory method `qlora` matches the training method. This repo is the merged result of that QLoRA run, which the inventory label does not spell out.

### Confidence

High. The journal paper, the model card, and the dataset card give the same rank, alpha, learning rate, epoch count, and 8B hardware.

### Queries tried

`Med-LLaMA3 Advancing Medical Question-Answering QLoRA Abo El-Enen`; full text of https://www.mdpi.com/2076-3417/16/12/6158; `github Mohamed-Ahmed-Abo-El-Enen MasterPapers`; dataset README and Hub API for `MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`; adapter card `Llama-3.1-8B-Instruct-Medical-Finetuned`; DOI `10.3390/app16126158`.

## 3. empirischtech/Llama-3.1-8B-Instruct-MedQA

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/empirischtech__Llama-3.1-8B-Instruct-MedQA__2026-10-05.md`
- Hub config `cache/configs/empirischtech__Llama-3.1-8B-Instruct-MedQA__2026-10-06.json`: `"unsloth_version": "2025.1.7"`, `vocab_size` 128258, `_name_or_path` pointing at a `meta-llama/Llama-3.1-8B-Instruct` snapshot. The tokenizer on the Hub uses `<|im_start|>` / `<|im_end|>`.
- Dataset card: https://huggingface.co/datasets/empirischtech/med-qa-orpo-dpo/raw/main/README.md
- Author named on the dataset card: Dr. Wasif Masood, Empirisch Tech GmbH. No paper and no training script for this checkpoint were found. GitHub user `wasifmasood` has no medical ORPO trainer in the public repo list.

### Training record

(a) Objective. Not a named algorithm. Model card says: “Task-Specific Training: Trained with reinforcement learning and domain-specific optimizations.” The dataset card, which this model lists, says the pairs were built for ORPO: “ORPO (Odds Ratio Preference Optimization) streamlines this process by combining SFT and preference alignment into a single step. … we therefore curate a dataset for fineuting on medical tasks using this approach.” That paragraph describes the dataset. It does not say this checkpoint was optimized with the ORPO loss. The model card’s phrase “reinforcement learning” is also not DPO, ORPO, PPO, or GRPO. `unsloth_version` in the config says the file was written by Unsloth 2025.1.7. It does not say which Unsloth trainer was used.

(b) Parameter update. Not stated. The upload is a full Llama checkpoint (four safetensors shards, no `adapter_config.json`). No rank, alpha, or target modules are stated. Whether an adapter was merged is not stated.

(c) Data. Model-card YAML lists `openlifescienceai/medmcqa`, `bigbio/med_qa`, `bigbio/pubmed_qa`, and `empirischtech/med-qa-orpo-dpo`. The preference dataset’s own card says those three public sets were restructured into one Hub dataset. Split sizes on that card: `bigbio_med_qa_orpo_dpo` 12,723; `pubmed_qa_orpo_dpo` 212,269; `medmcqa_orpo_dpo` 132,066. Total 357,058. Columns: `question`, `direct-answer`, `chosen`, `rejected`. Language `en`. An example rejected answer is a wrong option from the same multiple-choice item (“The answer is: Diazepam” against chosen “The answer is: Trazodone”). No generator model is named. The items come from human exam and literature questions (MedMCQA, PubMedQA, BigBIO MedQA).

(d) Base. YAML and the config path: `meta-llama/Llama-3.1-8B-Instruct`. The prose says only “Base Model: Llama-3.1-8B.” The config path is the instruction-tuned snapshot, and the vocabulary is 128,258, two tokens above Llama 3.1’s 128,256.

(e) Epochs, learning rate, batch size, hardware. Not stated anywhere found.

(f) The card lists metric `accuracy` and reports no number.

(g) The preference rows are multiple-choice or yes/no/maybe medical questions. The card also says the model was tuned for topic tagging and sentiment analysis. No dataset for those two tasks is named.

### Discrepancies

1. Inventory method is `dpo`, taken from the dataset name `med-qa-orpo-dpo`. The model card says “reinforcement learning.” The dataset card describes ORPO. None of those three labels is tied to a training script for this checkpoint.
2. Prose base name drops “Instruct.” The YAML, the config `_name_or_path`, and the Hub base relation say `Llama-3.1-8B-Instruct`.
3. Prose training data is “Curated medical literature, clinical case studies, and healthcare FAQs.” The YAML dataset is chosen/rejected pairs from MedMCQA, PubMedQA, and MedQA.

### Confidence

Low. The files show a preference dataset and an Unsloth save. They do not show which loss was optimized.

### Queries tried

`empirischtech Llama-3.1-8B-Instruct-MedQA ORPO DPO training`; dataset page and raw README for `empirischtech/med-qa-orpo-dpo`; `"Wasif Masood" ORPO medical Llama`; `empirischtech.at` team page; GitHub `wasifmasood`; Featherless model page; Hub model API (config and file list).

## 4. graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/graliuce__Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5__2026-10-05.md`
- Saved trainer arguments on the Hub: https://huggingface.co/graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5/resolve/main/training_args.bin (`SFTConfig`, output directory `/data/user_data/gliu2/models/info-seek/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5`, run folder `Nov13_18-10-28_babel-t9-32`)
- Naming script: https://github.com/graliuce/CaRT/blob/main/bash/sft/submit.slurm and https://github.com/graliuce/CaRT/blob/main/bash/sft/task.sh
- Trainer: https://github.com/graliuce/CaRT/blob/main/finetune/sft.py
- Paper for the dataset and the shared SFT setup: Grace Liu, Yuxiao Qu, Jeff Schneider, Aarti Singh, and Aviral Kumar, “CaRT: Teaching LLM Agents to Know When They Know Enough,” arXiv:2510.08517. https://arxiv.org/abs/2510.08517. Appendix B (data) and Appendix C (hyperparameters) were read. The checked-in slurm and the paper’s Table 2 name Qwen bases. This Llama checkpoint’s saved arguments are what fix the learning rate and the batch size for this repo id.
- Dataset: https://huggingface.co/datasets/graliuce/MedMCQA.20.01 (4,780 train, 100 test)

What the two tokens in the name mean. `submit.slurm` sets `dataset_names=(MedMCQA.20.01)`, `dataset_paths=(graliuce/MedMCQA.20.01)`, and `learning_rates=(1.0e-5)`, then `job_name=${model_name}_${dataset_name}_${learning_rate}` and `task.sh` pushes `graliuce/${task}`. So `20.01` is the dataset-name token, and `1.0e-5` is the learning rate written into the Hub id. The paper does not define the digits `20.01`. The dataset’s 4,780 training rows match the paper’s “final dataset size was 4.78k examples.” The checked-in slurm hardcodes `model_name=Qwen2.5-3B-Instruct`. This checkpoint’s saved `hub_model_id` is `graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5`, which is the same pattern with the Llama base name.

### Training record

(a) Objective. Supervised next-token fine-tuning. Card says: “This model was trained with SFT.” The saved file is an `SFTConfig`. Paper: “We perform supervised fine-tuning (SFT) on the counterfactual examples described above.” `sft.py` trains with TRL `SFTTrainer` and a completion-only collator: loss is on the suffix after `<MASK_END>`, which in the dataset is the `<think>` reason plus the decision. The paper’s extra GRPO stage is a different model (`Qwen2.5-3B-Instruct_20.03_rl_0.5` in the CaRT README), not this checkpoint.

(b) Parameter update. Full weights. `task.sh` does not pass `--use_peft`. `sft.py` sets `peft_config=get_peft_config(model_config)` and the launch command supplies no PEFT flags. The upload has no `adapter_config.json`. It is a bf16 `LlamaForCausalLM` with 8,030,261,248 parameters, the same count as Llama 3.1 8B. Rank and alpha are not stated because this recipe does not create an adapter.

(c) Data. `graliuce/MedMCQA.20.01`. Dataset card: 4,780 train rows and 100 test rows. Columns `messages` and `suffix`. A training row is a doctor–patient prefix, a system instruction to decide whether there is enough information for a diagnosis, and a suffix that is a `<think>` paragraph plus either `Need More Information` or `Final Diagnosis: ...`. Paper Appendix B: the set was built from MedMCQA diagnostic questions and Craft-MD / MedQA-USMLE conversations; counterfactual questions were generated by GPT-4o; reasoning traces were generated by GPT-4o; the final mix is 80% continue and 20% terminate. Language of the published row and of the paper’s medical setting: English.

(d) Base. Card and saved Hub id: `meta-llama/Llama-3.1-8B-Instruct`. Instruction-tuned. In the paper, Llama-3.1-8B-Instruct is also the external model that labels diagnostic accuracy. It is not the base of the Qwen CaRT run in Table 2.

(e) From this checkpoint’s `training_args.bin`: learning rate `1e-05`, 3 epochs, per-device train batch size 1, gradient accumulation 32, max sequence length 4096, bf16, gradient checkpointing, warmup ratio 0.0, max grad norm 1.0, weight decay 0.0, optimizer string `adamw_torch`, scheduler string `linear`, logging every step, eval every 5 steps, save every 20 steps, seed 42, report to wandb. `task.sh` launches that script with `--num_processes 8`. `submit.slurm` requests 8 A6000 GPUs, 100G memory, and 40 hours. The run directory name contains `babel-t9-32`. The paper’s Table 2, for the Qwen CaRT runs, lists the same learning rate and 3 epochs, batch size 256, max sequence length 16384, and warmup ratio 0.1. Eight processes times batch 1 times accumulation 32 is 256, which matches the paper’s batch size. The sequence length and warmup ratio in the paper do not match this file.

(f) This model card reports no scores. The paper’s termination curves are for Qwen2.5-3B-Instruct and Qwen3-1.7B, not for this Llama checkpoint. Weights & Biases link on the card: https://wandb.ai/grace_rl/infoseek/runs/j51w490x (not retrieved).

(g) The trained suffix is a written reason and a stop-or-diagnose decision on a medical conversation. It is not an answer to a MedMCQA multiple-choice item. The MedMCQA questions are the cases behind the conversations. Intended language: English.

### Discrepancies

1. Paper Table 2 lists max sequence length 16384 and warmup ratio 0.1, and names Qwen2.5-3B-Instruct and Qwen3-1.7B. This Llama file’s saved arguments set max sequence length 4096 and warmup ratio 0.0.
2. The paper never defines the string `20.01`. The slurm uses it only as the dataset id. The 20% terminate rate in Appendix B is a property of the data, and the paper does not say the filename encodes that rate.
3. Inventory `sft` and dataset `graliuce/MedMCQA.20.01` match the card and the saved arguments.

### Confidence

High for this checkpoint’s objective, learning rate, epochs, batch size, sequence length, and dataset. The paper explains what the dataset is. It does not report this Llama run’s scores.

### Queries tried

`graliuce MedMCQA.20.01 1.0e-5 SFT wandb grace_rl infoseek`; `"Counterfactuals and Reasoning for Termination" CaRT MedMCQA`; GitHub tree `graliuce/CaRT` including `submit.slurm`, `task.sh`, and `sft.py`; arXiv HTML and PDF `2510.08517`; dataset API and row sample for `graliuce/MedMCQA.20.01`; OpenReview CaRT; Hub `training_args.bin` for this repo id.

## 5. mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/mlxha__Llama-3.1-8B-Instruct-GRPO-medmcqa__2026-10-05.md`
- Saved arguments: https://huggingface.co/mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa/resolve/main/training_args.bin (`GRPOConfig`). Also `trainer_state.json`, `train_results.json`, and `eval_results.json` on that repo.
- Shared code: Michael Ha’s fork https://github.com/mlxha/open-r1 (fork of https://github.com/huggingface/open-r1). `src/open_r1/grpo.py` builds a TRL `GRPOTrainer`. `src/open_r1/rewards.py` defines `mcq_accuracy_reward`, `format_reward`, and `tag_count_reward`. The public tree has no yaml that names this Hub id. The same reward names appear in this run’s `trainer_state.json`, and the same card template (`open-r1`, `trl`, `grpo`) is on the other mlxha MedMCQA GRPO models.
- Dataset: https://huggingface.co/datasets/mlxha/medmcqa-grpo-meditron70b (16,885 train rows; README body is empty). Hub user page: https://huggingface.co/mlxha (Michael Ha).

### Training record

(a) Objective. GRPO, group relative policy optimization, a reinforcement-learning update with a reward. Card says: “This model was trained with GRPO, a method introduced in DeepSeekMath.” The saved file is a `GRPOConfig`. `trainer_state.json` logs `kl`, `reward`, and three reward channels: `rewards/format_reward`, `rewards/mcq_accuracy_reward`, and `rewards/tag_count_reward`. In `rewards.py`, `mcq_accuracy_reward` scores 1 when the letter inside `<answer>` matches the stored solution and 0 otherwise. `format_reward` scores 1 only if the completion matches a `<think>` block followed by an `<answer>` block. `tag_count_reward` gives up to 1 for exactly one of each think and answer tag. Saved `reward_weights` are `[1.0, 0.1, 0.1]`. The log lists the three channels in the order format, mcq accuracy, tag count. The file does not label which weight belongs to which channel. Saved system prompt: “You FIRST think about the reasoning process as an internal monologue and then provide the user with the answer. The reasoning process and answer are enclosed within `<think> </think>` and `<answer> </answer>` tags.” `beta` is 0.04. `num_generations` is 8. `temperature` is 1.0. `vllm_mode` is `server`.

(b) Parameter update. Not stated. `grpo.py` passes `peft_config=get_peft_config(model_args)`, and the saved `GRPOConfig` does not contain a `use_peft` field (that flag lives on the model config, which was not uploaded). The repo has no `adapter_config.json`. The weights are a bf16 Llama of 8,030,261,248 parameters. That is equally compatible with full-weight GRPO and with a merged adapter. Rank and alpha are not stated.

(c) Data. `mlxha/medmcqa-grpo-meditron70b`. `train_results.json`: `"train_samples": 16885`, matching the dataset card. Columns include MedMCQA fields `question`, `opa`–`opd`, `cop`, plus `problem` and `solution`. Row 0’s `solution` is `C`, the correct option letter, not a generated explanation. The name contains `meditron70b`. The empty README does not say whether Meditron-70B filtered the 16,885 rows, wrote them, or only named them. The questions are MedMCQA exam items. Language of the sample row: English. A separate dataset, `mlxha/medmcqa-grpo`, has 193,155 rows and is used by other models in the same series, not by this one.

(d) Base. Card: `meta-llama/Llama-3.1-8B-Instruct`. Instruction-tuned.

(e) From `training_args.bin`: learning rate `5e-06` (the trainer log peaks at 4.999945e-06 at step 55 and then falls; scheduler string `cosine`; warmup ratio 0.1), 1 epoch, per-device train batch size 4, gradient accumulation 32, `generation_batch_size` 256, `num_generations` 8, `max_completion_length` 8192, bf16, gradient checkpointing, optimizer string `adamw_torch`, max grad norm 1.0, weight decay 0.0, seed 42. `trainer_state.json`: `global_step` 527, `epoch` 0.9988. `train_results.json`: train loss 0.237, runtime 132,374 seconds. GPU count and machine type are not in the saved arguments. The run folder is `Jul01_02-08-57_grpo-llama8-0-0`.

(f) `eval_results.json`: eval loss 0.197 on 4,183 samples, runtime 5,919 seconds. No MedMCQA accuracy is published on the card. The dataset card has no test split, so those 4,183 rows are not identified there.

(g) The reward scores a multiple-choice letter, and the system prompt requires a reasoning trace before that letter. Intended language: English.

### Discrepancies

1. Inventory `grpo` and dataset `mlxha/medmcqa-grpo-meditron70b` match the card. The inventory does not record the three rewards or the learning rate.
2. The dataset name contains `meditron70b`. The stored `solution` in the first row is the letter `C`. Nothing in the README says Meditron-70B wrote the text.
3. `eval_samples` is 4,183. The dataset card publishes one train split of 16,885 rows and no test split.

### Confidence

High for GRPO, the reward names, the learning rate, the epoch count, and the batch settings, because they are in this checkpoint’s saved arguments and trainer log. Low for whether training updated all weights or a LoRA, and for what `meditron70b` means in the dataset name.

### Queries tried

`mlxha Llama-3.1-8B-Instruct-GRPO-medmcqa meditron70b open-r1`; `github mlxha medmcqa GRPO`; Hugging Face user `mlxha`; dataset row sample `mlxha/medmcqa-grpo-meditron70b`; `trainer_state.json`, `train_results.json`, `eval_results.json`, and `training_args.bin` on this repo; `src/open_r1/grpo.py` and `rewards.py` in `mlxha/open-r1`; `Qsingle/open-medical-r1` (a different MedMCQA GRPO repo, not this author).

## Patterns in this batch

Two of the five checkpoints can be classified from a paper or from saved trainer arguments. Mohamed Ahmed Abo El-Enen’s 8B model is supervised instruction tuning with QLoRA (rank 128, alpha 256, 4-bit NF4), then merged; the journal paper and the model card agree. Grace Liu’s Llama run is full-weight supervised fine-tuning for three epochs at learning rate 1e-5: `1.0e-5` in the name is that learning rate, and `20.01` is the id of a 4,780-row synthetic termination set, not a MedMCQA exam fine-tune. Michael Ha’s model is GRPO for one epoch at learning rate 5e-6, with rewards for a MedMCQA letter and for `<think>` / `<answer>` tags; the shared code is his fork of Hugging Face Open-R1, and the public tree does not say whether the update was full weights or LoRA.

The other two cards do not support a method label. `ruslanmv/ai-medical-model-32bit` only says “fine-tuned,” on a 21.2 million-row question/context set, and the author’s public SFT notebook is a 5-step demo under a different save name. `empirischtech/Llama-3.1-8B-Instruct-MedQA` says “reinforcement learning,” while its preference dataset’s card describes ORPO, and the inventory’s `dpo` label comes from the dataset name rather than from a trainer. Unsloth’s version string in that config shows which library wrote the file. It does not show the loss.
