# Medical fine-tune literature, batch 5

How five medical language models were trained. Facts are quoted from a paper, a script, a dataset card, or a cached model card. A word in a repository name is not treated as evidence.

| model | source found | objective | update scope | data (name, n, provenance) | base | task trained for | language | matches inventory row |
|---|---|---|---|---|---|---|---|---|
| taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA | code (training config in the model repo); no paper | distillation | DoRA (card also says 4-bit) | 1,101 teacher traces from MedQA, a hematology corpus, and PubMedQA; synthetic reasoning | Llama-3.1-8B-Instruct | reasoning traces | en | partly |
| GetSoloTech/Llama3.2-Medical-Notes-1B | preprint | supervised next-token fine-tuning on transcript–note pairs | LoRA, then merged | 1,500 synthetic endocrinology transcript–note pairs in the paper; Hub row count is 1,930 | Llama-3.2-1B-Instruct | note generation | en | partly |
| MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged | paper and training script | supervised next-token fine-tuning | QLoRA, then merged | Med-LLaMA3 corpus, 1,651,357 rows; mixed human and machine-written | Llama-3.2-1B-Instruct | multiple-choice exams, open questions, and patient–doctor dialogue | en | partly |
| UMCU/CardioLlama.nl_clinical | preprint for the corpus; the clinical stage is on the card only | continued pre-training, then a second continued pre-training | not stated | Dutch medical corpus, then 5 million UMCU cardiology records mixed with that corpus | Llama-3.2-1B-Instruct | other (next-token modeling of Dutch medical text) | nl | partly |
| emrullahcelik/Llama-3.2-1B-Instruct-Medical-SFT | none beyond the card and the dataset card | supervised fine-tuning | QLoRA (4-bit LoRA) | TUSGPT-TR-Medical-Dataset-v1, 55,465 Turkish question–answer rows; who wrote the answers is not stated | Llama-3.2-1B-Instruct | open medical questions | tr | yes |

## 1. taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA

### Sources

No journal paper, preprint, or thesis names this repository. The citation on the card points back at the Hugging Face page. GitHub user `tayden1990` has no repository for this model. An EMNLP 2024 paper titled MedCoT is a different visual question-answering method and is not this checkpoint.

Independent of the README, the repository contains `training_config.yaml`, `adapter/adapter_config.json`, and `training_metrics.json`.

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/taksa1990__Medical-CoT-Hematology-Llama3.1-8B-DoRA__2026-10-05.md`
- Config: https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/resolve/main/training_config.yaml
- Adapter config: https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/resolve/main/adapter/adapter_config.json
- Metrics: https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/resolve/main/training_metrics.json

### Training record

**(a) Objective.** Distillation. Card says: "Chain-of-Thought distillation from DeepSeek-R1-Distill-Llama-8B teacher" and "learns to reproduce the teacher's reasoning patterns." The yaml project name is `medical-cot-distillation`, and the teacher id is `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`. The student run logs a causal-language-model loss and `mean_token_accuracy` (final train loss 0.780, final mean token accuracy 0.862). The files do not say SFT, DPO, or reinforcement learning. The teacher was loaded in 4-bit and sampled traces (`temperature: 0.6`, `max_new_tokens: 4096`).

**(b) Update scope.** DoRA. `adapter_config.json` says `"peft_type": "LORA"` and `"use_dora": true`, with `"r": 128`, `"lora_alpha": 256`, `"lora_dropout": 0.05`, and target modules `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`, `lm_head`. The yaml says `method: dora` with the same rank, alpha, and targets. Card says: "PEFT method | DoRA" and "Quantization | QLoRA 4-bit NF4, double quantization." The student block of `training_config.yaml` does not contain a quantization section; only the teacher block does. The published adapter is not described as already merged. The card's load example calls `merge_and_unload()` at inference time. The Hub file list also includes a root `model.safetensors` of 8,030,261,248 BF16 parameters. The card does not say that file is the merged adapter.

**(c) Data.** Card says: "1,101 teacher-generated CoT reasoning samples" from MedQA (USMLE) ~1,000 (weight 0.50), Hematology Corpus ~51 (weight 0.25), and PubMedQA ~50 (weight 0.10), split 1,046 / 55. YAML data mix names `teacher_reasoning_medqa.jsonl` (weight 0.5), `hematology_reasoning.jsonl` (weight 0.25), `teacher_reasoning_pubmedqa.jsonl` (weight 0.1), and `image_reasoning.jsonl` (weight 0.15). Hub dataset ids on the current card: `GBaker/MedQA-USMLE-4-options` and `qiaojin/PubMedQA`. The hematology set is local files, not a Hub id. Reasoning traces are synthetic, from `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`. The yaml sets `qa_per_chunk: 5` for the hematology PDFs; the card does not name a model that wrote those questions. Language on the card: English.

**(d) Base.** `meta-llama/Llama-3.1-8B-Instruct`. It is the instruction-tuned checkpoint. `adapter_config.json` says `"base_model_name_or_path": "meta-llama/Llama-3.1-8B-Instruct"`.

**(e) Hyperparameters.** Yaml and card: 3 epochs, learning rate 0.0002, cosine schedule, warmup ratio 0.05, per-device batch 8, gradient accumulation 4. Card says about 37 minutes and 99 steps on one Google Colab A100 80 GB. `training_metrics.json` ends at step 99, epoch 3.0, `train_runtime` 2249.3 seconds. Optimizer in the yaml: `paged_adamw_32bit`. Max sequence length 4096.

**(f) Evaluation.** The card compares the base model and this adapter on three hematology questions (megaloblastic anemia, acute hemolytic transfusion reaction, iron deficiency versus anemia of chronic disease). It does not report a numeric test-set accuracy, ROUGE, or BERTScore, although those names are listed. The yaml lists planned metrics (`accuracy`, `reasoning_consistency`, `rouge_l`, `bertscore`, `medical_entity_recall`) and a consistency judge using the same DeepSeek teacher. Those scores are not in `training_metrics.json`.

**(g) Task and language.** The model is trained to write `<think>` reasoning and then an answer for hematology and blood-transfusion questions. Use language: English (`en`). Card says: "Not for clinical use."

### Discrepancies

1. Inventory methods cell is `qlora`. The adapter file and the yaml say DoRA. The card uses both words: DoRA as the adapter, and 4-bit QLoRA as the quantization.
2. The card's 1,101-sample table has three sources and weights that sum to 0.85. The yaml adds `image_reasoning.jsonl` at weight 0.15 and does not give that file's row count.
3. The student block of the yaml does not set 4-bit loading. The card says the student was trained as 4-bit QLoRA.
4. An earlier commit README listed dataset `openlifescienceai/medqa` and loaded the repository with `AutoModelForCausalLM`. The current card lists `GBaker/MedQA-USMLE-4-options` and tells users to load the PEFT adapter.
5. The repository contains both `adapter/adapter_model.safetensors` and a full-size root `model.safetensors`. The card does not say the root file is the merged adapter.

### Confidence

Medium. Rank, alpha, targets, epochs, step count, and the teacher id agree across the card, the yaml, the adapter file, and the metrics file. The image mix and the student's 4-bit setting do not.

### Queries tried

1. `taksa1990 Medical-CoT-Hematology-Llama3.1-8B-DoRA`
2. `"Medical Chain-of-Thought Distillation for Hematology" Taher Akbari Saeed`
3. `github tayden1990 Medical-CoT-Hematology DoRA Taher Akbari`
4. `"Taher Akbari Saeed" OR "0000-0002-9517-9773" hematology language model DoRA`
5. `MatrusMedAI 412ky1ao Medical CoT Hematology DoRA wandb`
6. Hub file fetch of `adapter_config.json`, `training_config.yaml`, and `training_metrics.json`

## 2. GetSoloTech/Llama3.2-Medical-Notes-1B

### Sources

Preprint: Johnson Thomas, Ayush Mudgal, Wendao Liu, Nisten Tahiraj, Zeeshaan Mohammed, and Dhruv Diddi, "Preserving Privacy, Increasing Accessibility, and Reducing Cost: An On-Device Artificial Intelligence Model for Medical Transcription and Note Generation," arXiv:2507.03033 (3 July 2025). Same manuscript on medRxiv, doi 10.1101/2025.07.01.25330679. Full text read from https://arxiv.org/pdf/2507.03033v1.

The paper's data-availability line names a different model id: `OnDeviceMedNotes/Medical_Summary_Notes`. Two authors work at Solo Tech. The GetSoloTech card copies the same method sentence and cites this paper. No LoRA rank was found in the paper, the medRxiv abstract, or either model card.

Cached card: `revision_3_experiments/hf_inventory/cache/readmes/GetSoloTech__Llama3.2-Medical-Notes-1B__2026-10-05.md`

### Training record

**(a) Objective.** Supervised fine-tuning on paired text. Paper says: "We fine-tuned a Llama 3.2 1B model using Parameter-Efficient Fine-Tuning (PEFT) with LoRA on 1,500 synthetic medical transcription-to-structured note pairs." The paper does not say DPO, PPO, or continued pre-training.

**(b) Update scope.** LoRA, and the authors say the Unsloth run included merging. Paper says: "Fine-tuning was performed using PEFT with LoRA adaptation, implemented through the Unsloth library for accelerated training and merging." Card says the same sentence. Rank, alpha, and target modules: not stated anywhere found. The GetSoloTech repository has `model.safetensors` (1,235,814,400 BF16 parameters) and no `adapter_config.json`. Cached `config.json` has `"unsloth_fixed": true` and `"unsloth_version": "2025.5.7"`.

**(c) Data.** Paper says the training set is 1,500 synthetic endocrinology transcriptions and structured notes, public at `starfishdata/endocrinology_structured_notes_1500`. Generation was "using advanced LLM prompting"; the generator model is not named. The first 20 samples were reviewed by an endocrinologist before the set was expanded. The card's dataset field is `starfishdata/playground_endocronology_notes_1500` (the spelling in the card). A Hub API request for that id returned the record whose id is `starfishdata/endocrinology_structured_notes_1500`, with 1,930 train rows, columns `topic`, `transcript`, `structured_note`. Language: English.

**(d) Base.** Paper says: "We employed Llama 3.2 1B Instruct as our base model." Card base: `meta-llama/Llama-3.2-1B-Instruct`. It is the instruction-tuned checkpoint.

**(e) Hyperparameters.** Epochs, learning rate, batch size, and hardware: not stated anywhere found.

**(f) Evaluation.** Paper, ACI benchmark, fine-tuned versus base: ROUGE-1 0.346 to 0.496, BERTScore F1 0.832 to 0.866, major hallucinations 85 to 35 of 140 cases. Internal set of 100 synthetic notes: composite LLM-judge score 3.13 to 4.43. Judge model named in the paper: `gpt-4.1-mini-2025-04-14`. The paper attaches these numbers to the OnDevice model, whose released id is `OnDeviceMedNotes/Medical_Summary_Notes`, not this repository.

**(g) Task and language.** Transcript in, structured clinical note out (demographics through assessment and plan). The card calls the task SOAP notes; the section list is longer than the four SOAP headings. Use language: English (`en`). The paper's evaluation is endocrinology, and the authors say other specialties were not tested.

### Discrepancies

1. The paper releases `OnDeviceMedNotes/Medical_Summary_Notes` and trains on `starfishdata/endocrinology_structured_notes_1500`. This card cites the paper but uses the id `GetSoloTech/Llama3.2-Medical-Notes-1B` and the dataset id `starfishdata/playground_endocronology_notes_1500`.
2. The paper says 1,500 training pairs. The Hub dataset that the card id currently resolves to has 1,930 rows.
3. Inventory methods cell is `lora`, which matches the paper. Inventory does not record that the card says the adapter was merged.

### Confidence

Medium. The method, base, task, and synthetic endocrinology notes are stated in the paper and repeated on this card. This repository is not the id in the paper's data-availability section, and the LoRA rank is absent.

### Queries tried

1. `GetSoloTech Llama3.2-Medical-Notes-1B arxiv 2507.03033`
2. `OnDeviceMedNotes Medical_Summary_Notes Llama LoRA rank Unsloth GetSoloTech`
3. `starfishdata playground_endocronology_notes_1500 vs endocrinology_structured_notes_1500`
4. `"Medical_Summary_Notes" OR "Llama3.2-Medical-Notes-1B" LoRA rank OR r= OR lora_alpha`
5. Hub API for both dataset ids
6. Full text of arXiv:2507.03033 and the medRxiv record 10.1101/2025.07.01.25330679

## 3. MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged

### Sources

Paper: Mohamed Ahmed Abo El-Enen, Sally S. Ismail, and Taymoor Mohamed Nazmy, "Med-LLaMA3: Advancing Medical Question-Answering Through Parameter-Efficient Fine-Tuning of Large Language Models," Applied Sciences 16, no. 12 (2026): 6158, doi 10.3390/app16126158. Full text read from https://www.mdpi.com/2076-3417/16/12/6158.

Training script: `Training/main_1b.py` in https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers. The script uses `SFTTrainer` and 4-bit NF4 LoRA. It also contains hardcoded access tokens; those tokens are not copied here.

Dataset card: https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset

Cached card: `revision_3_experiments/hf_inventory/cache/readmes/MohamedAhmedAE__Llama-3.2-1B-Instruct-Medical-Finetuned-merged__2026-10-05.md`

The paper's model link is the adapter repository `MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned`, not this merged repository. The dataset card says the adapters were released and "merged versions also available."

### Training record

**(a) Objective.** Supervised next-token fine-tuning. Paper Table 5, shared across the 1B, 3B, and 8B runs: "Task type | Causal language modeling." The 1B script imports `SFTTrainer` and `SFTConfig`. The paper does not use preference optimization or reinforcement learning for this family. A separate earlier project, DistilLLM-Med, is distillation into a different 1B student; the paper treats that as prior work, not as this training run.

**(b) Update scope.** QLoRA. Paper section 3.3: "All models were quantized to 4-bit precision using NormalFloat 4 (NF4) quantization." Section 3.4: "We employed QLoRA (quantized low-rank adaptation) for parameter-efficient fine-tuning across all three model variants." Table 5 for the 1B column: rank 128, alpha 256, dropout 0.05, bias none, target modules all linear layers (q, k, v, o, gate, up, down). Trainable parameters: "LLaMA 3.2 1B: 90.17 M / 1.32 B = 6.80%." The script's `LoraConfig` uses those rank, alpha, and dropout values, drops `lm_head` from the 4-bit linear modules, and sets `load_in_4bit=True` with NF4 and double quantization. This repository is the merged weights. Card says: "QLoRA fine-tuning (4-bit NF4 base + LoRA, `r=128`, `α=256`, all linear layers), then `merge_and_unload()` into the base." Released weights are bfloat16, not 4-bit. Hub API: 1,235,814,400 BF16 parameters, no adapter file.

**(c) Data.** Dataset card says 1,651,357 English examples (about 1,636,957 train and about 14,400 validation). Paper Table 1 says the fine-tuning corpus is about 1.5 million after holding out MMLU medical items. Sources in the paper table include MIMIC-III (465,200), UMLS (312,450), MedDialog English (257,337), MedMCQA (194,000), HealthCareMagic (112,165), WikiDoc patient information (67,233), Alpaca-EN-AN (52,000), medical flashcards (33,955), ChatDoctor/iCliniq (30,000), CORD-19 (17,721), MEDIQA (16,412), MedQA-USMLE (12,723), WikiDoc (10,000), CovidDialog (6,032), and PubMed Causal (2,446). Dataset-card tags: `annotations_creators: expert-generated` and `machine-generated`. The generator model for the machine-written rows is not named. The compiled Hub id is `MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`.

**(d) Base.** `meta-llama/Llama-3.2-1B-Instruct`. Paper Table 3 describes LLaMA 3.2 1B (1.24 B parameters, 16 layers). The script sets `model_name` to `meta-llama/Llama-3.2-1B-Instruct`. It is the instruction-tuned checkpoint.

**(e) Hyperparameters.** Paper Table 5, 1B column: learning rate 2.0 × 10⁻⁵, cosine, 5 epochs, 5 warmup steps, per-device batch 10, gradient accumulation 40, max sequence length 1024, paged AdamW 8-bit, weight decay 0.1. Paper section 3.7: "LLaMA 3.2 1B: 2 × NVIDIA RTX4050 12 GB, 23 days training time." DeepSpeed and FlashAttention were used for the 1B and 3B runs on the RTX 4050s. The script matches rank, alpha, learning rate, batch 10, accumulation 40, max length 1024, and 4-bit NF4. The script sets `num_epochs` to 6, and its output name is `Llama-3.2-1B-Instruct-Medical-Finetune-v5`, which is not this Hub id.

**(f) Evaluation.** Paper Table 7, Med-LLaMA3.2 1B, 5-shot MMLU medical accuracy: Anatomy 47.41, Clinical Knowledge 48.30, College Biology 46.53, College Medicine 38.15, Medical Genetics 52.00, Nutrition 59.15, Professional Medicine 56.62, Virology 40.96. Card mean of those eight: 48.64. The paper does not report an untuned Llama-3.2-1B baseline on that table. MedMCQA, MedQA, and PubMedQA numbers in Table 6 are for the 8B model. The named-entity scores on 100 discharge summaries are a zero-shot evaluation, not a training task.

**(g) Task and language.** The corpus mixes exam multiple-choice questions, open questions, and patient–doctor dialogue, plus case passages and a smaller set of literature tasks. Use language: English. Dataset card says the corpus is English only.

### Discrepancies

1. The paper links the 1B adapter repository. This repository is the merged copy. The card says the merge does not change outputs.
2. The published script sets 6 epochs. Table 5 and the model card say 5.
3. The inventory dataset list is the card's Hub ids. The paper table also counts MIMIC-III, UMLS, MedDialog, HealthCareMagic, Alpaca-EN-AN, ChatDoctor, and MEDIQA, which are not separate ids in the inventory row.
4. Paper text says about 1.5 million fine-tuning samples. The dataset card's total is 1,651,357, including validation.

### Confidence

High for the published 1B recipe (QLoRA, rank 128, alpha 256, 5 epochs, the 1B batch settings, English instruction data, instruct base). Medium for treating the current `main_1b.py` as the exact run that produced this file, because that script says 6 epochs and a different output name.

### Queries tried

1. `Med-LLaMA3 Advancing Medical Question-Answering Abo El-Enen QLoRA`
2. `Mohamed-Ahmed-Abo-El-Enen MasterPapers Med-LLaMA3 QLoRA github`
3. `"Med-LLaMA3" "Abo El-Enen" filetype:pdf OR html training QLoRA "1.5 million"`
4. `"Llama-3.2-1B-Instruct-Medical-Finetuned-merged" Abo El-Enen`
5. Full text of doi 10.3390/app16126158
6. `Training/main_1b.py` and the Med_LLaMa3 dataset README

## 4. UMCU/CardioLlama.nl_clinical

### Sources

Preprint: Bram van Es, "Language corpora for the Dutch medical domain," arXiv:2604.25374 (28 April 2026). Full text read from https://arxiv.org/html/2604.25374.

That paper names `CardioLlama.nl` as "domain-adapted pre-training of English Llama 3.2, 1B parameters." It does not name `CardioLlama.nl_clinical`, and it does not give the 5 million records, the 768-token stage, or the perplexity of 4.

The clinical-stage description is the model card. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/UMCU__CardioLlama.nl_clinical__2026-10-05.md`. A sibling card, `UMCU/CardioLlama.nl`, describes an earlier continuous-pre-training run and says "Planned: on-premise continuous pre-training on Dutch clinical texts." arXiv:2402.15449, tagged on that sibling, is an embeddings paper ("Repetition Improves Language Model Embeddings") and is not a training paper for this model.

Corpus code linked from the preprint: https://github.com/bramiozo/PubScience and https://github.com/UPOD-datascience/TPU_compute. No public script was found that trains `CardioLlama.nl_clinical`.

### Training record

**(a) Objective.** Continued pre-training, in two stages. Card says: "domain adapted pretraining (DAPT), also called Continuous Pre-training (CPT) on a Dutch medical corpus, slightly biased towards cardiology." Then: "This model is then further pre-trained on 5 million cardiology records from the UMCU mixed with a random selection of the Dutch medical corpus to avoid model collapse." The paper's phrase for the related model is "domain-adapted pre-training." No SFT, preference optimization, or reinforcement learning is stated for this checkpoint.

**(b) Update scope.** Not stated. The card does not say full-parameter updates, LoRA, or QLoRA. The repository is a complete Llama checkpoint: `model.safetensors`, 1,235,814,400 BF16 parameters, no adapter file. That is the same parameter count as Llama-3.2-1B. The sibling `UMCU/CardioLlama.nl` is larger (Hub API: 1,498,482,688 BF16 parameters). The card does not explain that difference.

**(c) Data.** Stage 1 dataset id: `UMCU/DutchMedicalText`. The dataset card calls it "Version 1 of the Dutch medical language corpus, slightly biased towards cardiology," and lists Dutch guidelines, NtvG, translated PMC and PubMed text, translated PMC patient cases, and translated MIMIC-III and MIMIC-IV. The preprint says the broader corpus is about 36 billion tokens in about 105 million documents, built by translating English biomedical text (NLLB, MariaNMT, GPT-3.5, GPT-4o, Gemini, and Google Translate) and by collecting Dutch web text, theses, and guidelines. Stage 2: "5 million cardiology records from the UMCU," mixed with a random selection of the Dutch medical corpus. The card does not give a Hub id for those records. They are hospital records, so the text is human clinical writing. The card does not say they were translated. MIMIC access is required to use `UMCU/DutchMedicalText`.

**(d) Base.** `meta-llama/Llama-3.2-1B-Instruct`. The paper calls the related model "domain-adapted pre-training of English Llama 3.2." The starting checkpoint is the instruction-tuned English model. This run is continued pre-training, not a second instruction-tuning stage.

**(e) Hyperparameters.** Card: one full epoch on the Dutch corpus, batch size 256, maximum sequence length 768, linear-cosine schedule. Second stage: maximum sequence length 1024, linear decay with warmup, "for about 1 epoch." Learning rate: not stated on this card. The sibling `CardioLlama.nl` card states LRmax 1e-4; that sentence is not on the clinical card, and the two cards describe different sequence lengths, so that learning rate is not recorded for this model. Hardware: not stated for this checkpoint. The preprint lists the lab's machines (RTX 2080, RTX 4000, two A10s, a TPU pod) for building the corpus, not as this model's training log. Validation perplexity on the card: "around 4."

**(f) Evaluation.** The only number on the card is that perplexity. The preprint does not report a benchmark for `CardioLlama.nl_clinical`.

**(g) Task and language.** The training objective is next-token modeling of Dutch medical text, then of UMCU cardiology records mixed back with that corpus. It is not exam question answering, dialogue, or note generation. Language field on the card: `nl`.

Dutch use. The card and the preprint describe Dutch training text. The second stage is records from University Medical Center Utrecht, a Dutch hospital, mixed with the Dutch corpus "to avoid model collapse." The card does not contain a sentence that says the model may be used only for Dutch, and it does not report an English evaluation. The language tag is Dutch only. The sibling card's "planned" clinical stage is the stage this repository says it completed. This checkpoint is the Dutch, cardiology-leaning clinical continued-pre-training run, not a general-domain instruction model.

### Discrepancies

1. Inventory methods cell is empty. The card states continued pre-training. Inventory datasets and base model match the card (`UMCU/DutchMedicalText`, `meta-llama/Llama-3.2-1B-Instruct`).
2. The cited preprint describes `CardioLlama.nl`, not `CardioLlama.nl_clinical`, and does not mention 5 million cardiology records.
3. The sibling card still says clinical continued pre-training is planned and reports perplexity 5. This card says that stage was run and reports perplexity around 4.
4. Featherless repeats the model card. It is not an independent training source.

### Confidence

Medium. The two-stage Dutch continued-pre-training description is explicit on the card. The paper confirms the corpus and a related Llama 3.2 1B domain-adaptation run, and it does not document this clinical checkpoint.

### Queries tried

1. `CardioLlama.nl_clinical van Es Dutch medical corpus arxiv 2604.25374`
2. `"CardioLlama.nl_clinical" OR "CardioLlama.nl" "5 million" cardiology UMCU`
3. `arxiv 2402.15449 CardioLlama OR Dutch medical Llama`
4. `site:github.com CardioLlama.nl_clinical OR "CardioLlama.nl" van Es pretraining`
5. Full text of arXiv:2604.25374
6. Hub API for `UMCU/CardioLlama.nl_clinical`, `UMCU/CardioLlama.nl`, and `UMCU/DutchMedicalText`

## 5. emrullahcelik/Llama-3.2-1B-Instruct-Medical-SFT

### Sources

No paper, preprint, thesis, or training repository was found. The training record is the model card. The dataset card supplies the row count and the column names. The 9B model `turkerberkdonmez/TUSGPT-TR-Medical-9B` uses the same dataset with a different base and a two-stage DoRA run; that is not this 1B run.

Cached card: `revision_3_experiments/hf_inventory/cache/readmes/emrullahcelik__Llama-3.2-1B-Instruct-Medical-SFT__2026-10-05.md`

Dataset: https://huggingface.co/datasets/turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1

### Training record

**(a) Objective.** Supervised fine-tuning. Card says: "Yöntem | SFT (Supervised Fine-Tuning) + LoRA (Unsloth)" and "Framework: Unsloth + TRL SFTTrainer" and "Training: train_on_responses_only." No preference optimization or reinforcement learning is stated. The name contains "SFT"; the card also states the method in a sentence, which is the evidence used here.

**(b) Update scope.** QLoRA. Card says: "Precision: 4-bit quantization (QLoRA)," LoRA rank 16, alpha 32, dropout 0, target modules `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`. The card does not say the adapter was merged. The published files are a full checkpoint: `model.safetensors`, 1,235,814,400 F16 parameters, no `adapter_config.json`. Cached `config.json` has `"unsloth_fixed": true`. The Hub relation tag is `base_model:adapter`, which disagrees with the file list. The load example uses `AutoModelForCausalLM` on this repository.

**(c) Data.** Card dataset id: `turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1`. Dataset card: 55,465 Turkish rows (train 47,169, test 4,148, validation 4,148), columns `instruction` and `output`. Dataset card says the set is for supervised fine-tuning of an assistant that answers medical questions in Turkish. It does not say whether the answers were written by a person or by a model, and it does not name a generator. The model card does not say which split was used. A LinkedIn post by the dataset author says the set was meant to be something other than a translation of an English set; that post still does not name the writers. Language: Turkish.

**(d) Base.** `meta-llama/Llama-3.2-1B-Instruct`. It is the instruction-tuned checkpoint.

**(e) Hyperparameters.** Card: AdamW 8-bit, learning rate 2e-4, batch size 2, gradient accumulation 4 (effective 8), 1 epoch, max sequence length 1024. Train loss 3.14 to 1.57. About 6 hours on an RTX 3050 Ti 4 GB, peak VRAM 2.88 GB.

**(f) Evaluation.** No held-out accuracy, ROUGE, or exam score is reported. The only training number is the train-loss drop.

**(g) Task and language.** Card: the model was fine-tuned to produce correct and thorough answers to Turkish medical questions. The example question is "Hipertansiyon nedir ve tedavisi nasıl yapılır?" which is an open question, not a multiple-choice exam item. The dataset name contains "TUS"; the dataset card does not say the rows are specialty-exam items. Use language: Turkish (`tr`). Card says the model is for research and education and should not be used for diagnosis or treatment.

### Discrepancies

1. Inventory methods `qlora|sft` and dataset `turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1` match the card.
2. The card does not say merged. The repository contains full 1B weights and no adapter file, while the Hub tag says adapter.
3. The 9B model card's "55,000+" count matches this dataset's 55,465 rows. That 9B card's DoRA method is not the method on this 1B card.

### Confidence

Medium. The card states SFT, QLoRA, rank, alpha, data id, and hardware, and the dataset card states the row count. No second source confirms that this file was produced by that run, or whether the adapter was merged before upload.

### Queries tried

1. `emrullahcelik Llama-3.2-1B-Instruct-Medical-SFT TUSGPT`
2. `TUSGPT-TR-Medical-Dataset-v1 rows instruction output provenance Turkish TUS`
3. `emrullahcelik Llama-3.2-1B-Instruct-Medical-SFT github OR kaggle OR wandb`
4. `"emrullahcelik" OR "Emrullah Çelik" OR "Emrullah Celik" Llama medical Turkish SFT RTX 3050`
5. Hub API for the model and for `turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1`
6. `turkerberkdonmez/TUSGPT-TR-Medical-9B` (same dataset, different training method; not used as this model's method)

## Patterns in this batch

Four of the five runs start from an instruction-tuned Llama and then do supervised training: one by copying a teacher's reasoning traces with DoRA, one by learning transcript-to-note pairs with LoRA, one by QLoRA on a 1.65-million-row English instruction mix, and one by QLoRA on Turkish question-answer pairs. The fifth run, `UMCU/CardioLlama.nl_clinical`, is continued pre-training on Dutch medical text and then on UMCU cardiology records. It is the only model whose training is not an instruction or preference objective, and the only one whose language tag is Dutch. The card does not say the model is limited to Dutch clinical text by a written restriction, but Dutch is the only language it assigns, and the second stage is hospital cardiology records mixed with the Dutch corpus.

The inventory's method cell is the coarse label. It records QLoRA for the hematology model and does not record DoRA. It records LoRA for the note model and does not record the merge. It leaves the Dutch model blank. It matches the Turkish card's QLoRA-plus-SFT label.

Released files and training-time adapters are different objects. The Med-LLaMA3 1B checkpoint in this batch is a merged bfloat16 model; the paper's download link is the adapter. The hematology repository publishes a DoRA adapter and also a full-size weight file. The Turkish card describes a 4-bit LoRA run and uploads a full float16 model without saying the adapter was merged. The note-model card does say Unsloth was used for merging, and the repository has no adapter file.

Counts should be taken from the source that states them, not from the name. The note paper says 1,500 pairs; the Hub table now has 1,930 rows. The Med-LLaMA3 paper says about 1.5 million; the dataset card says 1,651,357. The 1B training script in the Med-LLaMA3 repository sets 6 epochs; the paper's table sets 5.
