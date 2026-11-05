# Batch 6: how five medical models were trained

Cached cards read: newest README under `revision_3_experiments/hf_inventory/cache/readmes/` (2026-10-05). Inventory row: `revision_3_experiments/hf_inventory/results/medical/2026-10-06/kept.csv`. Hub file lists checked live on 7 Oct 2026 through the model API.

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Task trained for | Language | Matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HexQuant/Pars-Medical-o1-Llama-FFT | none | not stated | full (card) | medical-o1-reasoning-SFT, card ~40,000 English; Hub English config 19,704; two Persian sets, card ~5,000 and ~3,000, row counts not confirmed; English set is GPT-4o synthetic | unsloth/Llama-3.2-3B-Instruct (instruction-tuned) | reasoning traces and open questions | fa, en | partly |
| MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged | paper and code | supervised next-token fine-tuning | QLoRA, rank 128, alpha 256; card says the adapter was merged | Med-LLaMA3 corpus, 1,651,357 English rows; mixed human exam and dialogue text and machine-generated rows | meta-llama/Llama-3.2-3B-Instruct (instruction-tuned) | multiple-choice exams, open questions, and patient-doctor dialogue | en | partly |
| aakthepaak/clinical-llm-r32 | blog (same author as the card) | not stated | QLoRA, rank 32, alpha 64; upload is a full checkpoint | medical_meadow_medqa, 2,500 of 10,178 rows; human exam questions | meta-llama/Llama-3.2-3B-Instruct (instruction-tuned) | multiple-choice exam answering | en | partly |
| miike-ai/4o-3b-medical | none | not stated | not stated | YAML names medical-o1-reasoning-SFT; which split was used is not stated; English config is 19,704 GPT-4o rows | meta-llama/Llama-3.2-3B-Instruct (instruction-tuned) | not stated | not stated | partly |
| prithivMLmods/Llama-Doctor-3.2-3B-Instruct | none | not stated | not stated | chat_doctor, 119,486 English rows; human patient-doctor web text; ChatGPT 5k portion excluded by the dataset author | meta-llama/Llama-3.2-3B-Instruct (instruction-tuned) | patient-doctor dialogue | en | yes |

## 1. HexQuant/Pars-Medical-o1-Llama-FFT

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/HexQuant__Pars-Medical-o1-Llama-FFT__2026-10-05.md`. Names this repo id. Author line on the card: TheRealPourya. Links: GitHub `xPOURY4`, X `@TheRealPourya`, org `HexQuant`.
- Hub model API, 7 Oct 2026: https://huggingface.co/api/models/HexQuant/Pars-Medical-o1-Llama-FFT . Created 2025-12-22. Siblings are two `model-*.safetensors` shards, no `adapter_config.json`. Parameter count: 3,212,749,824 BF16. Relation tag: `base_model:finetune:unsloth/Llama-3.2-3B-Instruct`. Commit messages on the file list say "Upload model trained with Unsloth".
- GGUF card, same author: https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT-GGUF . Describes quantization of this checkpoint. It is not a second training record.
- Discussions tab: https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT/discussions . No posts.
- GitHub user https://github.com/xPOURY4 . Public repos returned by search are a prompt assistant, a Telegram bot, and forks. None is a Pars-Medical training script.
- English dataset card: https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT . Does not name this model.
- A different Persian medical model, Gaokerena-V (arXiv 2505.16000), fine-tunes `aya-expanse-8b`. It does not name this repo.

The name starts with "Pars". The card states the use languages in words: Persian (Farsi) and English. The name "FFT" is also stated in a sentence on the card, quoted below. The name alone is not the evidence.

### Training record

**(a) Objective.** Not stated anywhere found. Card says: "Pars-Medical is a medical AI model trained with **Full Fine-Tuning** on Persian and English medical datasets." That sentence names which weights were updated. It does not say supervised next-token fine-tuning, preference optimization, reinforcement learning, continued pre-training, or distillation. One listed dataset id contains `SFT`. That is a dataset name, not a statement of this run's loss.

**(b) Parameter-update scope.** Card says: "Method | Full Fine-Tune (FFT)" and "Full Fine-Tune - Not LoRA/adapter". Framework line: "Unsloth + Transformers". Precision: BF16. Context length: 4096 tokens. Hub siblings are a full BF16 checkpoint and no `adapter_config.json`. Rank, alpha, and target modules: not stated anywhere found. Whether an adapter was merged: the card says the run was not an adapter.

**(c) Training data.** Card table:

| Dataset | Language | Samples |
| medical-o1-reasoning-SFT | English | ~40,000 |
| persian-medical-qa | Persian | ~5,000 |
| Persian-Medical-Dataset | Persian | ~3,000 |

YAML ids: `FreedomIntelligence/medical-o1-reasoning-SFT`, `erfan226/persian-medical-qa`, `SeyedAli/Persian-Medical-Dataset`. Feature line: "48K+ Samples".

The English dataset card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." Hub size API, English config `en`: 19,704 train rows. Chinese config `zh`: 20,171. Mixed configs: `en_mix` 24,887 and `zh_mix` 25,358. All four configs sum to 90,120. The card's "~40,000" does not match the current English config. The card does not say which config was loaded.

The two Persian ids: the 2026-10-06 inventory marks both `not_found`. A web search for those exact ids did not return dataset pages. A fetch of `SeyedAli/Persian-Medical-Dataset` returned HTTP 401. A fetch of `erfan226/persian-medical-qa` timed out. Provenance and row counts for those two sets are not stated anywhere found beyond the card's "~5,000" and "~3,000".

**(d) Base model.** YAML: `unsloth/Llama-3.2-3B-Instruct`. Training table: "`Llama-3.2-3B-Instruct`" without the Unsloth prefix. The id is the instruction-tuned Llama 3.2 3B checkpoint. Unsloth packages that checkpoint; the card does not say a base-only, non-instruct Llama was trained.

**(e) Hyperparameters.** Epochs, learning rate, and batch size: not stated anywhere found. Card says hardware "NVIDIA A100 80GB". The GGUF card says the quantized files were made on "NVIDIA A100 80GB SXM". That second sentence is about quantization, not about the fine-tuning run.

**(f) Evaluation.** Not stated anywhere found. The card prints two example dialogues, one Persian and one English, with `<think>` tags. It also says: "This is a beta version and does not have the ability to correctly respond to or handle local runs on its own."

**(g) Task and language.** Card feature row: "Chain-of-Thought - Step-by-step reasoning" and "Clinical Focus - Diagnosis & treatment". The printed examples are a Persian chest-pain case and an English hypothyroidism case, each with a step list and then a diagnosis. YAML `language`: `en` and `fa`. The English named dataset is reasoning traces. The Persian names are question-answer sets. The card does not say a named-entity or note-generation loss.

### Discrepancies

1. Inventory `methods` is `full_finetune|sft`. The card states full fine-tuning. It does not state a supervised next-token loss. The `sft` label follows the dataset id `medical-o1-reasoning-SFT`.
2. Card English sample count is ~40,000. The Hub English config has 19,704 rows.
3. YAML base id is `unsloth/Llama-3.2-3B-Instruct`. The training table drops the `unsloth/` prefix.
4. Inventory marks `erfan226/persian-medical-qa` and `SeyedAli/Persian-Medical-Dataset` as `not_found`. This pass did not retrieve public row counts for either id.

### Confidence

Medium. The card states full fine-tuning, the upload is a full BF16 file, and the card states Persian and English in words. No script or paper confirms the run, and the English row count on the Hub does not match the card.

### Queries tried

- `HexQuant Pars-Medical-o1-Llama-FFT full fine-tune TheRealPourya xPOURY4`
- `site:github.com/xPOURY4 Pars-Medical OR HexQuant FFT persian medical llama`
- `"Pars-Medical" OR "Pars Medical o1" Pourya OR HexQuant fine-tune A100 persian`
- Hugging Face model API and the empty discussions tab
- GGUF card https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT-GGUF
- Dataset card and size API for `FreedomIntelligence/medical-o1-reasoning-SFT`
- Fetches and search for `erfan226/persian-medical-qa` and `SeyedAli/Persian-Medical-Dataset`
- Gaokerena-V, arXiv 2505.16000 (a different Persian medical model)

## 2. MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/MohamedAhmedAE__Llama-3.2-3B-Instruct-Medical-Finetuned-merged__2026-10-05.md`. Names this repo id. Authors: Mohamed Ahmed Abo El-Enen, Sally S. Ismail, Taymoor Mohamed Nazmy.
- Journal article, full HTML, Applied Sciences 2026, 16(12), 6158: https://www.mdpi.com/2076-3417/16/12/6158 . DOI 10.3390/app16126158. Published 17 June 2026. The code-availability line prints `https://huggingface.co/Mohamed AhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned` (a space in the org name, and no `-merged`). It does not print this merged repo id.
- Training script `Training/main_3b.py`: https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/Med-LLaMa3%20Advancing%20Medical%20Question%20Answering%20through%20Parameter-Efficient%20Fine-Tuning%20of%20Large%20Language%20Models/Training/main_3b.py . Does not print this merged repo id. The script hard-codes a Weights & Biases key and a Hugging Face token. Those strings are omitted here.
- Dataset card: https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset . Says the corpus fine-tuned the 1B, 3B, and 8B family. The model links on that card point at the adapter repos and say "merged versions also available" without printing this repo id.
- Adapter card, same authors: https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned . Points at this merged repo.

### Training record

**(a) Objective.** Supervised next-token fine-tuning. Paper Table 5: "Task type | Causal language modeling", shared by the 1B, 3B, and 8B runs. The data are instruction-response pairs. Script line: `from trl import SFTTrainer, SFTConfig`, and later `trainer = SFTTrainer(...)`. Paper, section 2.4: "rather than compressing a large model through distillation, we adopted parameter-efficient fine-tuning (PEFT)". No DPO, ORPO, PPO, or GRPO step is described for this family.

**(b) Parameter-update scope.** QLoRA. Paper: "quantized low-rank adaptation (QLoRA) and low-rank adaptation (LoRA) with 4-bit quantization." Table 5, shared: rank 128, alpha 256, dropout 0.05, bias none, target modules "all linear layers (q, k, v, o, gate, up, down projections)". Equation in the paper: "LLaMA 3.2 3B: 194.51 M / 3.40 B = 5.70%". Paper: "All models were quantized to 4-bit precision using NormalFloat 4 (NF4)". Script: `load_in_4bit=True`, `bnb_4bit_quant_type="nf4"`, `bnb_4bit_use_double_quant=True`, `LoraConfig` with `r=128`, `lora_alpha=256`, `TaskType.CAUSAL_LM`, and `find_all_linear_names` over `bnb.nn.Linear4bit` modules, dropping `lm_head`.

This repository is the merged file. Card says: "QLoRA fine-tuning (4-bit NF4 base + LoRA, `r=128`, `α=256`, all linear layers), then `merge_and_unload()` into the base" and "the medical LoRA is already fused into the weights". The script pushes a PEFT adapter with `trainer.push_to_hub()` and its test function loads `PeftModel`. The script does not call `merge_and_unload`.

**(c) Training data.** Card and dataset card name `MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`. Hub size API: 1,651,357 rows (1,636,982 train, 14,375 validation). Dataset card: "Total examples | 1,651,357" and "Language | English". Paper: "a medical instruction dataset of over 1.5 million samples" and Table 1 "Fine-tuning corpus | ~1.5 M". Table 1 caption: "All counts refer to English-language subsets."

Dataset card: `annotations_creators` are `expert-generated` and `machine-generated`. It does not name one generator model for the whole corpus. Paper Table 1 mixes exam questions (MedMCQA 194,000; MedQA-USMLE 12,723), patient-doctor dialogue (HealthCareMagic 112,165; MedDialog 257,337; ChatDoctor iCliniq 30,000; CovidDialog 6,032), biomedical literature, encyclopedic text, and "Alpaca-EN-AN | 52,000". Exam items and the HealthCareMagic-style transcripts are human-written. The machine-generated tag is on the dataset card; the paper does not say which rows a model wrote.

Script loads local disks `./train_dataset_clean_V2` and `./valid_dataset_clean_V2`, not the Hub id.

**(d) Base model.** Card, paper, and script: `meta-llama/Llama-3.2-3B-Instruct`. That id is the instruction-tuned checkpoint. Script: `base_model_name: str = "meta-llama/Llama-3.2-3B-Instruct"`. Paper Table 3 lists the 3.21 B architectural parameter count for "LLaMA 3.2 3B". The 3.40 B figure in the 5.70% ratio is the training-time total the paper uses as the denominator, not a second base model.

**(e) Hyperparameters.** Paper Table 5 for the 3B column: learning rate 2.0 × 10^−5, cosine annealing, Paged AdamW 8-bit, weight decay 0.1, 5 epochs, 5 warmup steps, max gradient norm 1.0, max sequence length 2048, batch size 4 per device, gradient accumulation 16. Paper: "LLaMA 3.2 3B: 2 × NVIDIA RTX4050 12 GB, 30 days training time." Card repeats those 3B numbers, including "2 × NVIDIA RTX 4050 (12 GB), ~30 days".

Script `TrainingConfig` for the 3B file: `num_epochs: int = 6`, `learning_rate: float = 2.0e-05`, `per_device_batch_size: int = 4`, `gradient_accumulation_steps: int = 16`, `max_length: int = 2048`, `lora_rank: int = 128`, `lora_alpha: int = 256`. `SFTConfig` sets `lr_scheduler_type="cosine"` and `optim="paged_adamw_8bit"`. The DeepSpeed JSON in the same file sets optimizer type `AdamW`. The script sets `resume_from_checkpoint` to `checkpoint-4000`. Its banner string says "Llama 3.2 1B" inside `main_3b.py`.

**(f) Evaluation.** Paper Table 7, row "Med-LLaMA3.2 3B (Ours)", 5-shot accuracy with 95% bootstrap intervals: Anatomy 59.52 (±4.26), Clinical Knowledge 68.17 (±2.89), College Biology 71.53 (±3.77), College Medicine 57.65 (±3.78), Medical Genetics 75.00 (±4.35), Nutrition 68.32 (±2.69), Professional Medicine 70.59 (±2.77), Virology 43.17 (±3.84). Card mean of those eight: 64.24. Table 6's MedMCQA 61.8, MedQA 62.4, and PubMedQA 77.0 are the 8B row, not the 3B row. Card says the paper does not report an untuned `Llama-3.2-3B` baseline on these subsets.

**(g) Task and language.** Paper title and abstract: medical question answering. Table 1 formats include multiple-choice exams, open questions, and generative dialogue. Dataset card: "Open-ended QA, multiple-choice QA, clinical case reading, abstract-to-title summarization, relationship classification" and "Clinical dialogue — patient-message → doctor-style response." Language: English. Card: "English only. Performance outside English is not evaluated."

### Discrepancies

1. Paper Table 5 and the model card say 5 epochs. `main_3b.py` sets `num_epochs` to 6.
2. The model card says this repo was produced with `merge_and_unload()`. `main_3b.py` trains and pushes a PEFT adapter and does not call `merge_and_unload`. Its Hub id string is `Llama-3.2-3B-Instruct-Medical-Finetune-v5`, not this repo id.
3. Paper Table 1 and the dataset-card prose list MIMIC-III (465,200), UMLS (312,450), MedDialog, Alpaca-EN-AN, ChatDoctor iCliniq, and CovidDialog. The model-card YAML and the dataset-card `source_datasets` field do not list those ids. The model-card prose adds MedQuAD, BigBIO MedQA, and `deepset/covid_qa_deepset`, which are not rows in Table 1.
4. Paper fine-tuning corpus is "~1.5 M". The Hub dataset has 1,651,357 rows. Paper text also says PubMed Causal has 2,169 samples; Table 1 says 2,446.
5. Inventory `methods` is `qlora` only. The paper and the script also state supervised causal-language-model training. Inventory datasets follow the model-card YAML, not the extra sources in Table 1.
6. The paper's code-availability URL has a space in `Mohamed AhmedAE` and points at the adapter repo.

### Confidence

High for the training recipe of the 3B family: the paper, the model card, and `main_3b.py` agree on QLoRA rank 128, alpha 256, 4-bit NF4, `Llama-3.2-3B-Instruct`, and `SFTTrainer`. The epoch count and the merge step do not agree across those three sources.

### Queries tried

- `Med-LLaMA3 Advancing Medical Question-Answering QLoRA Abo El-Enen Applied Sciences 2026`
- Full HTML of https://www.mdpi.com/2076-3417/16/12/6158 (Tables 1, 3, 5, 6, and 7 and sections 3.4–3.6)
- `github Mohamed-Ahmed-Abo-El-Enen MasterPapers QLoRA Llama-3.2-3B training config`
- GitHub contents API for the Med-LLaMA3 folder and raw `Training/main_3b.py`
- Dataset card and size API for `MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`
- Adapter model card `MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned`

## 3. aakthepaak/clinical-llm-r32

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/aakthepaak__clinical-llm-r32__2026-10-05.md`. Names this repo id. WandB link on the card: https://wandb.ai/aakarsh3110-stevens-institute-of-technology/clinical-llm . That page was not opened.
- Author portfolio, same numbers: https://www.aakarshthumma.com/projects/clinical-llm . Author name on the site: Aakarsh Reddy Thumma. The page does not print `aakthepaak/clinical-llm-r32`.
- Resume PDF: https://www.aakarshthumma.com/Aakarsh_Resume.pdf . Same project paragraph. Does not print this repo id.
- GitHub https://github.com/aakarsh31 (display name aakthepaak, 20 public repos). A search of that user's repos for "clinical" did not return a training repository for this model.
- Hub model API, 7 Oct 2026: https://huggingface.co/api/models/aakthepaak/clinical-llm-r32 . Created 2026-03-15. `library_name` is `peft`. Relation tag: `base_model:adapter:meta-llama/Llama-3.2-3B-Instruct`. Siblings are `model-00001-of-00002.safetensors` and `model-00002-of-00002.safetensors`. There is no `adapter_config.json`. Parameter count: 3,212,749,824 BF16.
- Dataset card: https://huggingface.co/datasets/medalpaca/medical_meadow_medqa . Does not name this model. Hub size: 10,178 train rows.

The name contains `r32`. The card also states the rank in a table, quoted below. The name alone is not the evidence.

### Training record

**(a) Objective.** Not stated anywhere found. Card says: "A QLoRA fine-tune of Meta's Llama 3.2 3B Instruct on the MedQA dataset" and "Fine-tuning method: QLoRA via Unsloth + PEFT + TRL". Portfolio: "Used QLoRA (Quantized Low-Rank Adaptation) via Unsloth to fine-tune on 2,500 MedQA samples." Neither source names `SFTTrainer`, a preference loss, or a reward. TRL can run more than one trainer. The inventory `methods` cell is `qlora` only, which matches that silence on the loss.

**(b) Parameter-update scope.** QLoRA. Card table: "LoRA rank (r) | 32 (best checkpoint)", "lora_alpha | 64", target modules `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`, "lora_dropout | 0", "Quantization | 4-bit (nf4) during training". Ablation table: r=32 has "~48M (1.50%)" trainable parameters. Portfolio: ranks 4, 8, 16, and 32, and a box "fp16 merge". Card benchmark heading: "Quantization Benchmark (merged r=32, L4 GPU)". The uploaded files are a full 3.21 B BF16 checkpoint with no `adapter_config.json`. The Hub tag still says `adapter`.

**(c) Training data.** Card: "medalpaca/medical_meadow_medqa (2,500 samples — 2,250 train / 250 val)". Hub dataset size: 10,178 train rows, so the card describes a subset. Dataset card cites Jin et al., "What Disease does this Patient Have?", and says the questions come from medical exams in the US, mainland China, and Taiwan. That is human exam text. The dataset card's language tags are `en` and `zh`. The model card says the task is "MedQA / USMLE-style" and YAML language is `en`. It does not say the Chinese items were included.

**(d) Base model.** Card: `meta-llama/Llama-3.2-3B-Instruct`. Instruction-tuned. Portfolio: "Llama 3.2 3B Instruct".

**(e) Hyperparameters.** Card: 3 epochs, batch size 2, gradient accumulation 8 (effective batch size 16), learning rate 2e-4, warmup 50, max sequence length 2048. Hardware: "Google Colab L4 GPU (23.7 GB VRAM)". Unsloth version "2026.3.4". The portfolio does not repeat the learning rate, epochs, or alpha.

**(f) Evaluation.** Card ablation, same 250-row validation setup implied by the 2,250/250 split: base accuracy 0.100 and ROUGE-L 0.128; r=32 accuracy 0.592 and ROUGE-L 0.355. Card: "The base model's low score is largely a format compliance issue — it generates verbose explanations rather than the concise single-letter answer the benchmark expects." Merged r=32 latency table: 4-bit accuracy 0.588, fp16 accuracy 0.596. No external paper reports these scores.

**(g) Task and language.** Card: "Task: Multiple-choice clinical question answering (MedQA / USMLE-style)". Language: English.

### Discrepancies

1. The card uses 2,500 rows. The Hub dataset has 10,178 rows.
2. Hub `library_name` is `peft` and the relation tag is `adapter`. The files are a full BF16 checkpoint and there is no `adapter_config.json`. The card's benchmark heading says "merged r=32".
3. Inventory `methods` is `qlora` and `datasets` is the full Hub id. The card's subsample and the merged upload are not in that row.

### Confidence

Medium. The card and the author's portfolio agree on QLoRA, rank 32, 2,500 MedQA rows, and 59.2% accuracy. No training script was found, and the Hub tag still says the repo is an adapter.

### Queries tried

- `aakthepaak clinical-llm-r32 QLoRA MedQA Llama 3.2 aakarsh3110`
- `Aakarsh Reddy Thumma clinical-llm github wandb Stevens QLoRA r=32`
- Portfolio https://www.aakarshthumma.com/projects/clinical-llm and the resume PDF
- `site:github.com aakarsh31 clinical-llm OR "clinical llm" MedQA QLoRA`
- GitHub user page https://github.com/aakarsh31
- Hub model API for `aakthepaak/clinical-llm-r32`
- Dataset card and size API for `medalpaca/medical_meadow_medqa`

## 4. miike-ai/4o-3b-medical

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/miike-ai__4o-3b-medical__2026-10-05.md`. The body is only YAML: `datasets: FreedomIntelligence/medical-o1-reasoning-SFT` and `base_model: meta-llama/Llama-3.2-3B-Instruct`. No prose.
- Hub model API, 7 Oct 2026: https://huggingface.co/api/models/miike-ai/4o-3b-medical . Created 2025-03-02. Siblings: three `model-*.safetensors` shards, no `adapter_config.json`. Parameter count: 3,212,749,824 BF16. Relation tag: `base_model:finetune:meta-llama/Llama-3.2-3B-Instruct`.
- Same author's other repo https://huggingface.co/miike-ai/Llama-3.2-3B-Instruct-FP4 has no model card. It is a different file.
- Dataset card: https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT . Does not name `miike-ai`.
- arXiv 2510.05003, "Resource-Efficient Fine-Tuning of LLaMA-3.2-3B for Medical Chain-of-Thought Reasoning", trains on the same dataset and links `imranmansha/llama3-medical-finetuned`. It does not name `miike-ai/4o-3b-medical`.

The repo name contains `4o`. That is a hint, not a training statement. The dataset card, not the model name, is what says GPT-4o built the data.

### Training record

**(a) Objective.** Not stated anywhere found. Inventory `methods` is `sft` because the dataset id contains `SFT`. The model card does not state a loss.

**(b) Parameter-update scope.** Not stated anywhere found. The upload is a full BF16 checkpoint with no `adapter_config.json`. That shows which file was uploaded. It does not say whether training updated every weight or a LoRA adapter that was later merged. Rank and alpha: not stated anywhere found.

**(c) Training data.** The only statement is the YAML dataset id. The dataset card says the set "is constructed using GPT-4o" and was used to fine-tune HuatuoGPT-o1. Hub sizes: English 19,704, Chinese 20,171, English mix 24,887, Chinese mix 25,358, total 90,120. This model card does not say which config, or how many rows, were used. Provenance of that named dataset: synthetic, generator GPT-4o, checked by the authors' medical verifier. That is a property of the dataset, not a statement that this repo ran a distillation loss.

**(d) Base model.** YAML and Hub tag: `meta-llama/Llama-3.2-3B-Instruct`. Instruction-tuned.

**(e) Hyperparameters.** Not stated anywhere found.

**(f) Evaluation.** Not stated anywhere found.

**(g) Task and language.** Not stated anywhere found on this model. The named dataset is medical reasoning traces in English and Chinese. The model card does not say which language this model was trained to use. A quantizer card at `mradermacher/4o-3b-medical-GGUF` sets language `en`. That is the quantizer's tag, not a training statement.

### Discrepancies

1. Inventory `methods` is `sft`. The card does not state a supervised loss. The label comes from the dataset id.
2. arXiv 2510.05003 uses the same dataset and the same base-model size, and it describes QLoRA. Its Hugging Face link is `imranmansha/llama3-medical-finetuned`, not this repo. Those hyperparameters are not this model's.

### Confidence

Low. The card names a dataset and a base model and nothing else. No paper, script, or blog states how this file was trained.

### Queries tried

- `miike-ai 4o-3b-medical Llama-3.2-3B medical-o1-reasoning-SFT`
- `"4o-3b-medical" OR "miike-ai" Llama medical fine-tune`
- `"miike-ai" OR "4o-3b-medical" huggingface OR github OR kaggle OR wandb`
- Hub model API for `miike-ai/4o-3b-medical`
- Dataset card and size API for `FreedomIntelligence/medical-o1-reasoning-SFT`
- arXiv HTML 2510.05003 (different author and repo)
- `miike-ai/Llama-3.2-3B-Instruct-FP4` (different repo, no card)

## 5. prithivMLmods/Llama-Doctor-3.2-3B-Instruct

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/prithivMLmods__Llama-Doctor-3.2-3B-Instruct__2026-10-05.md`. Names this repo. The file table in that cached card lists `pytorch_model-00001-of-00002.bin` and `pytorch_model-00002-of-00002.bin`.
- Hub model API, 7 Oct 2026: https://huggingface.co/api/models/prithivMLmods/Llama-Doctor-3.2-3B-Instruct . Created 2024-11-16, last modified 2025-07-10. Siblings are two `model-*.safetensors` shards, no `adapter_config.json`. Parameter count: 3,212,749,824 F16. Relation tag: `base_model:finetune:meta-llama/Llama-3.2-3B-Instruct`. Tokenizer `pad_token` is `<|finetune_right_pad_id|>`.
- GGUF cards that repeat the same paragraph: https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct-GGUF and the bartowski and mradermacher quantizations. They are copies of the card, not a second training record.
- Dataset card: https://huggingface.co/datasets/avaliev/chat_doctor . Does not name this model.
- GitHub search for `prithivMLmods` plus `Llama-Doctor` or `chat_doctor` did not return a training script. https://github.com/PRITHIVSAKTHIUR/Llama-3.2-1B-GGUF-Fast-Gradio is a different 1B GGUF demo.

### Training record

**(a) Objective.** Not stated anywhere found. Card says: "This model is a fine-tuned version of the base Llama-3.2-3B-Instruct model" and "has been trained on a specialized dataset, avaliev/chat_doctor". "Fine-tuned" does not name supervised next-token training, a preference loss, or a reward. Inventory `methods` is empty.

**(b) Parameter-update scope.** Not stated anywhere found. The live upload is a full F16 checkpoint with no `adapter_config.json`. That does not say whether training updated every weight. The pad token `<|finetune_right_pad_id|>` is the token Unsloth writes when it saves a fine-tune. It does not state LoRA rank or full updates. Rank and alpha: not stated anywhere found.

**(c) Training data.** Card YAML: `avaliev/chat_doctor`. Dataset card: "100k real conversations between patients and doctors from HealthCareMagic.com HealthCareMagic-100k. - ADDED" and "10k real conversations between patients and doctors from icliniq.com icliniq-10k. - ADDED" and "5k generated conversations between patients and physicians from ChatGPT GenMedGPT-5k and disease database. - NOT ADDED". Hub size: 119,486 rows (95,588 train, 11,949 validation, 11,949 test). Language tag: English. The model card does not say which split was used. Provenance of the included rows: human patient-doctor text from those two websites. The dataset author says the ChatGPT 5k file was left out.

**(d) Base model.** Card: `meta-llama/Llama-3.2-3B-Instruct`. Instruction-tuned. The card's phrase "the base Llama-3.2-3B-Instruct model" uses "base" for that instruct checkpoint, not for a pre-trained-only Llama.

**(e) Hyperparameters.** Not stated anywhere found.

**(f) Evaluation.** Not stated anywhere found.

**(g) Task and language.** Card: "trained on a specialized dataset, avaliev/chat_doctor, to enhance its performance in providing conversational or advisory responses, especially in medical or technical fields" and "Medical Consultation Tools for generating advice or answering medical queries". YAML language: `en`. The dataset rows are patient questions and doctor replies. That is dialogue. The card also lists generic chatbot and content-creation uses. Those lines are not a second training task.

### Discrepancies

1. The cached card's file table lists two PyTorch `.bin` shards. The Hub API on 7 Oct 2026 lists two safetensors shards, F16, same 3,212,749,824 parameter count, and no adapter file.
2. None that change the inventory row. Inventory `methods` is empty, and no source states a method. Inventory `datasets` is `avaliev/chat_doctor`, which matches the card.

### Confidence

Low. The card names the dataset and says the model was fine-tuned for medical conversation. No script or paper states the loss or which weights were updated.

### Queries tried

- `prithivMLmods Llama-Doctor-3.2-3B-Instruct chat_doctor fine-tune`
- `"Llama-Doctor" prithiv OR prithiviraj OR prithivMLmods LoRA OR QLoRA OR epochs`
- `site:github.com prithivMLmods Llama-Doctor OR chat_doctor Llama-3.2-3B`
- Hub model API for `prithivMLmods/Llama-Doctor-3.2-3B-Instruct`
- GGUF commit that copies the same training paragraph
- Dataset card and size API for `avaliev/chat_doctor`
- GitHub `PRITHIVSAKTHIUR/Llama-3.2-1B-GGUF-Fast-Gradio` (a different model)

## Patterns in this batch

All five uploads name an instruction-tuned Llama 3.2 3B checkpoint as the parent. Only the Med-LLaMA3 3B model has both a paper and a script, and those two agree on QLoRA rank 128 and `SFTTrainer` while they disagree on the epoch count (5 in the paper, 6 in `main_3b.py`). The script trains an adapter; the card of this merged repo says the adapter was then fused, and the script never calls that merge. Pars-Medical and `miike-ai/4o-3b-medical` both name `FreedomIntelligence/medical-o1-reasoning-SFT`, a GPT-4o reasoning set whose English config has 19,704 rows. Pars's card says ~40,000 English rows and states full fine-tuning in a sentence; the `miike-ai` card states neither a loss nor an update scope, so the inventory `sft` label there is the dataset name. The rank in `clinical-llm-r32` is stated as 32 on the card, and the FFT in the Pars name is stated as full fine-tuning on the card. The `4o` in the `miike-ai` name is not a training statement. Llama-Doctor and the `miike-ai` model have no paper or script, and the Pars Persian dataset ids were not confirmed as public Hub datasets in this pass.
