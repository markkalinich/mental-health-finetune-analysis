# Batch 4: how five mental-health fine-tunes were trained

Date of search: 2026-10-06. Cards read: the 2026-10-05 copies under `revision_3_experiments/hf_inventory/cache/readmes/`. Inventory rows: `revision_3_experiments/hf_inventory/results/mental-health/archive/2026-10-06/kept.csv`. Hub file lists: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__020.csv`. None of the five uploads contains `adapter_config.json`.

A claim below is tied to a URL or a cached file. If a field is missing from every source that was found, it is marked "not stated anywhere found." A method word inside a dataset name is not treated as the training method. The pilot note on `gustavecortal/Piaget-8B` is `docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/mh-finetune-literature-pilot-2026-10-06.md`.

## Summary

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Matches inventory row |
|---|---|---|---|---|---|---|
| dzur658/smollm2-mentalhealth-360m-V2 | code | supervised next-token training (SFTTrainer) | full weights; no LoRA in the script | `Amod/mental_health_counseling_conversations`, 3,512 English question-answer rows, described as real counseling replies | `HuggingFaceTB/SmolLM2-360M-Instruct` | yes |
| ecorbari/Gemma-2b-it-Psych-Merged | code and a blog | supervised fine-tuning on the preferred reply only (SFTTrainer) | QLoRA (4-bit NF4, rank 16, alpha 32), then `merge_and_unload` | `jkhedri/psychology-dataset`, 9,846 rows; notebook uses 8,861 train and 985 test; provenance not stated | `google/gemma-2b-it` | partly |
| gustavecortal/Piaget-0.6B | thesis sentence; no training script | not stated (card says LoRA fine-tuning on reasoning traces; it does not name SFT, DPO, or distillation) | LoRA rank 8, alpha 16; merge not stated | `PsychologicalReasoning-15k`, 15,006 English rows, filtered from Dolphin R1 and GeneralThought-430K | `Qwen/Qwen3-0.6B` (post-trained, not the Base checkpoint) | yes |
| gustavecortal/Piaget-1.7B | same thesis sentence; no training script | same as 0.6B | same LoRA settings; nothing on the card changes with size | same 15,006-row set | `Qwen/Qwen3-1.7B` (post-trained, not the Base checkpoint) | yes |
| gustavecortal/Piaget-4B | same thesis sentence; no training script | same as 0.6B | same LoRA settings; nothing on the card changes with size | same 15,006-row set | `Qwen/Qwen3-4B` (post-trained, not the Base checkpoint) | yes |

## 1. dzur658/smollm2-mentalhealth-360m-V2

The training script is in the GitHub repository the model card links. No paper or thesis was found. The script uses TRL `SFTTrainer` on the full SmolLM2-360M-Instruct weights.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/dzur658__smollm2-mentalhealth-360m-V2__2026-10-05.md`. Live page: https://huggingface.co/dzur658/smollm2-mentalhealth-360m-V2 . Hub metadata in `2026-10-05__020.csv`: created 2025-06-08, last modified 2025-06-09. Author on the card: Alex Dzurec. Files: one `model.safetensors`, tokenizer files, no `adapter_config.json`. This card names the GitHub repository. It does not print the string `dzur658/smollm2-mentalhealth-360m-V2` inside the training-arguments block.
- Training script: https://github.com/dzur658/smollm2-mentalhealth-360m/blob/main/smollm_finetuningv2.py . README: https://github.com/dzur658/smollm2-mentalhealth-360m/blob/main/README.md . The README says `smollm_finetuningv2.py` is the script for the v2 model. The script does not contain the Hub id. `push_to_hub.py` leaves `hub_model_id = ""` and the commit message string is "Upload fine-tuned SmolLM2-360M-V2 for mental health counseling."
- LinkedIn post by Alex Dzurec, 2025-06-09: https://www.linkedin.com/posts/alex-dzurec-103180254_ai-llm-finetuning-activity-7337981565886504961-_6R3 . It says there is "a robust 3-epoch version" and links V2. It does not add a learning rate, a dataset id, or a score.
- Dataset card: https://huggingface.co/datasets/Amod/mental_health_counseling_conversations . Dataset API: https://huggingface.co/api/datasets/Amod/mental_health_counseling_conversations (tag `language:en`). Owner comment, 2023-07-20: https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/discussions/1 .
- Base card: https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct . That page describes Hugging Face's own post-training of SmolLM2. It is not Dzurec's run.
- PubMed and Google Scholar queries for Dzurec and this model name returned unrelated counseling papers. No arXiv paper names this repository.

### Training record

**(a) Objective.** Supervised next-token training on chat-formatted counseling pairs. Script says `from trl import SFTConfig, SFTTrainer, setup_chat_format` and builds `trainer = SFTTrainer(...)` then `trainer.train()`. `format_example` fills a system, user, and assistant turn from `Context` and `Response`. The card does not print the letters "SFT". It says "Full fine tune of SmolLm2-360m in BF16 precision using the TRL library". No DPO, ORPO, PPO, or reward model appears in the script. The base model's own card says Hugging Face applied DPO to produce `SmolLM2-360M-Instruct`. That sentence is about the starting checkpoint, not this fine-tune.

**(b) Parameter-update scope.** All weights. Card says: "the model was fully fine tuned locally on a 3050 TI with only 4gb of VRAM" and "This Model should in no way be used to treat, diagnose, or otherwise prevent mental health disorders, and is simply a demonstration of full fine tuning a small model on a consumer GPU." The script loads `AutoModelForCausalLM.from_pretrained("HuggingFaceTB/SmolLM2-360M-Instruct")` and has no `LoraConfig` and no bitsandbytes 4-bit config. The upload is one `model.safetensors` and has no `adapter_config.json`. Rank, alpha, and target modules: not stated anywhere found, and the script does not create an adapter. Adapter merged: no adapter in the script or the file list.

**(c) Training data.** Card and script: `Amod/mental_health_counseling_conversations`. The script loads `split="train"` and then `train_test_split(test_size=0.1, seed=training_args.seed)` with seed 3407. It does not print the resulting row counts. The Hub commit that added `combined_dataset.json` is a 3,512-line file with one JSON object per line (https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/commit/b4b6169296f484c689546769c5cba03e5db9312a). The dataset viewer reports 3.51k train rows. Dataset card says: "This dataset is a collection of real counselling question-and-answer pairs taken from two public mental-health platforms." API tag: `language:en`. The owner wrote: "the conversations were sourced mainly from https://github.com/nbertagnolli/counsel-chat/tree/master/data". The counsel-chat card says that scrape is therapist replies from counselchat.com (https://huggingface.co/datasets/nbertagnolli/counsel-chat, 2,775 rows). The Amod card still says two websites. The second site is not named. Provenance stated on the Amod card: real counseling question-answer pairs, not a named generator model.

**(d) Base model.** Card YAML and script: `HuggingFaceTB/SmolLM2-360M-Instruct`. The base card says: "We developed the instruct version through supervised fine-tuning (SFT) using a combination of public datasets and our own curated datasets. We then applied Direct Preference Optimization (DPO) using UltraFeedback." This fine-tune starts from that instruct checkpoint, not from `HuggingFaceTB/SmolLM2-360M`.

**(e) Hyperparameters.** The card pastes the same `TrainingArguments` as the script: `per_device_train_batch_size=2`, `gradient_accumulation_steps=4`, `gradient_checkpointing=True`, `warmup_steps=100`, `num_train_epochs=3`, `learning_rate=2e-4`, `optim="adamw_8bit"`, `weight_decay=0.01`, `lr_scheduler_type="linear"`, `seed=3407`, `output_dir="smollm2-mentalhealth-360m-fp16-v2"`. Precision in the script is `bf16` when `torch.cuda.is_bf16_supported()` is true, otherwise `fp16`. The card's prose says "BF16 precision" and also pastes that conditional. Hardware on the card: "3050 TI mobile GPU", "~18 hours". The script does not name the GPU.

**(f) Evaluation.** The script sets `eval_strategy="epoch"`, `metric_for_best_model="eval_loss"`, and `load_best_model_at_end=True`. No numeric eval loss is stored in the repository that was fetched. The card says "From my limited testing the model appears to excel at describing common mental health problems" and "this model has significantly better performance than the previous" v1. No benchmark table.

### Discrepancies

1. Inventory `methods` is `full_finetune`, dataset `Amod/mental_health_counseling_conversations`, parent `HuggingFaceTB/SmolLM2-360M-Instruct`. The card and the script agree with that row.
2. The script does not contain `dzur658/smollm2-mentalhealth-360m-V2`. The card links the GitHub repository, the README assigns `smollm_finetuningv2.py` to v2, and the script's `output_dir` matches the directory in the card's usage example (`smollm2-mentalhealth-360m-fp16-v2`, including a local `checkpoint-1185` path).
3. Card prose says the run was BF16. The shared code block uses BF16 only when the GPU reports support, otherwise FP16.

### Confidence

High. The card links this repository, the v2 script's arguments match the block pasted on the card, and the output directory name matches the card's local path. The script file itself does not print the Hub id.

### Queries tried

- `dzur658/smollm2-mentalhealth-360m-V2 Alex Dzurec fine-tune`
- `"smollm2-mentalhealth-360m" OR "SmolHealth" Dzurec training epochs`
- `"Alex Dzurec" OR dzur658 SmolLM2 mental health arxiv OR thesis OR paper`
- GitHub contents API for `dzur658/smollm2-mentalhealth-360m`, then `smollm_finetuningv2.py`, `README.md`, and `push_to_hub.py`
- `site:pubmed.ncbi.nlm.nih.gov OR site:scholar.google.com "smollm2-mentalhealth" OR "SmolLM2" Dzurec counseling`
- `Amod/mental_health_counseling_conversations` dataset card, API, and the 2023 source discussion
- `HuggingFaceTB/SmolLM2-360M-Instruct` model card (base post-training only)
- LinkedIn post, 2025-06-09

## 2. ecorbari/Gemma-2b-it-Psych-Merged

The weights in this repository are the merge of a LoRA adapter. The training notebook that produced the adapter uses 4-bit QLoRA and TRL `SFTTrainer` on `response_j` only. A Medium post by the same author restates that pipeline. No paper was found.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/ecorbari__Gemma-2b-it-Psych-Merged__2026-10-05.md`. Live page: https://huggingface.co/ecorbari/Gemma-2b-it-Psych-Merged . Hub metadata: created 2026-02-01, last modified 2026-02-01. Author on the card: Ederson Corbari (e@NeuroQuest.ai). Files: one `model.safetensors`, tokenizer files, no `adapter_config.json`. The card names this repo id and the adapter repo `ecorbari/Gemma-2b-it-Psych`.
- Adapter card: https://huggingface.co/ecorbari/Gemma-2b-it-Psych . It says this other repository "contains LoRA adapters only."
- Training notebook, dated January 25, 2026 in the notebook header: https://github.com/edersoncorbari/fine-tune-llm/blob/main/notebooks/02_GEMMA2B_FINE_TUNING.ipynb . The header URL is `https://huggingface.co/ecorbari/Gemma-2b-it-Psych`, not the Merged id. The saved outputs include `CommitInfo` for `ecorbari/Gemma-2b-it-Psych`.
- Merge notebook, dated February 01, 2026: https://github.com/edersoncorbari/fine-tune-llm/blob/main/notebooks/03_GEMMA2B_MERGE_LORA.ipynb . It prints `https://huggingface.co/ecorbari/Gemma-2b-it-Psych-Merged` and the saved output includes `CommitInfo` for that repo.
- README: https://github.com/edersoncorbari/fine-tune-llm/blob/main/README.md . It names both Hub ids and says the merged repo is "LoRA adapters merged into base weights."
- Blog, Ederson Corbari, 2026-04-12: https://ecorbari.medium.com/beyond-helpfulness-specialized-fine-tuning-for-empathetic-ai-with-gemma-2b-and-qlora-afcb08dea000 . The retrieved text links the GitHub repository. It describes the same SFT-on-`response_j` and QLoRA steps. It is the author's write-up of this project, not an independent lab report.
- Dataset page: https://huggingface.co/datasets/jkhedri/psychology-dataset . The page says "No dataset card yet" and "Number of rows: 9,846". API: https://huggingface.co/api/datasets/jkhedri/psychology-dataset . No `language` tag and no README.
- Base card: https://huggingface.co/google/gemma-2b-it . "This model card corresponds to the 2B instruct version of the Gemma model."
- Searches for an arXiv or PubMed paper by Ederson Corbari on this Gemma run returned the Medium post, not a paper.

### Training record

**(a) Objective.** Supervised fine-tuning on the preferred reply. The training notebook imports `SFTTrainer`, maps each row to a user turn plus `response["response_j"]`, and the training markdown says: "This step starts the supervised fine-tuning process". The Medium post says: "Filtering a preference-based dataset to extract only high-empathy responses for Supervised Fine-Tuning (SFT)." `response_k` is not a training target in that code. The opening markdown of the same notebook also says the dataset enables learning "rather than relying on standard supervised fine-tuning" and lists "Preference-based fine-tuning approaches (e.g., DPO-style methods)" as something the notebook "serves as a starting point for." The executed cells are `SFTTrainer`, not a DPO trainer. No ORPO, PPO, or reward model is in the notebook. The phrase "Behavioral Distillation" in the Medium post is defined there as that filtering step before SFT. The post does not describe training against a teacher model's token probabilities.

**(b) Parameter-update scope.** QLoRA, then a merge into this repository. Training notebook: `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True)` and `LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM", target_modules=modules)`. The printed modules are `down_proj`, `gate_proj`, `k_proj`, `o_proj`, `q_proj`, `up_proj`, `v_proj`. The finder excludes `lm_head`. Printed trainable count: "trainable params: 19,611,648 || all params: 2,525,784,064 || trainable%: 0.7765". Merge notebook: load `google/gemma-2b-it` in `torch.float16`, `PeftModel.from_pretrained(..., "ecorbari/Gemma-2b-it-Psych")`, then `model.merge_and_unload()`, then `model.push_to_hub("Gemma-2b-it-Psych-Merged")`. The merged card says: "This model integrates the LoRA adapter weights from ecorbari/Gemma-2b-it-Psych directly into the base model using the `merge_and_unload()` process." This upload is one `model.safetensors` and has no `adapter_config.json`. Adapter merged: yes, for this repository.

**(c) Training data.** Notebook: `DATASET_NAME = "jkhedri/psychology-dataset"`, `load_dataset(..., split="all")`, shuffle seed 65, `train_test_split(test_size=0.1, seed=42)`. The saved dataset printout is 8,861 train rows and 985 test rows (9,846 total), matching the Hub row count. Columns in that printout: `question`, `response_j`, `response_k`, `text`. Only `response_j` is placed in the assistant turn. System line in the notebook: "You are a compassionate mental health assistant." Language: the merged card says "Language(s): English." The dataset page does not state a language. Provenance: not stated anywhere found. There is no dataset card, and neither the notebook nor the Medium post names a human author or a generator model for the pairs. The notebook does say `response_j` is the "empathetic/therapeutic" pole and `response_k` is the "judgmental/aggressive" pole.

**(d) Base model.** Card, both notebooks, and README: `google/gemma-2b-it`. The Google card calls this "the 2B instruct version." The merge loads that instruct checkpoint in float16, not `google/gemma-2b`.

**(e) Hyperparameters.** Training notebook `TrainingArguments`: `per_device_train_batch_size=1`, `per_device_eval_batch_size=1`, `gradient_accumulation_steps=2`, `optim="paged_adamw_32bit"`, `num_train_epochs=1`, `learning_rate=2e-4`, `warmup_steps=10`, `fp16=False`, `bf16=False`, `group_by_length=True`. It does not set `lr_scheduler_type`. Saved run: "4431/4431", "Epoch 1/1", `train_runtime` 27632.8753 seconds (the progress line also prints 7:40:29), `TrainOutput` `training_loss` 0.7069022529242512. Device printout: "NVIDIA T1000 8GB". The Medium post says the run used "a Cosine Scheduler." That scheduler is not in the notebook's `TrainingArguments`. The learning-rate number in the Medium post was an image in the retrieved page, so the number used here is the notebook's `2e-4`.

**(f) Evaluation.** The notebook logs validation loss every 200 steps, from 0.846223 at step 200 to 0.597766 at step 4400. The README says training loss fell from about 3.36 to about 0.55 and evaluation loss settled around 0.60 to 0.70, and it derives perplexity as exp(loss), about 1.82 at eval loss 0.60. The last logged training loss in the notebook table is 0.5618 at step 4400. The average `training_loss` in `TrainOutput` is 0.707. The Medium post repeats the about-3.36-to-0.55 story and a qualitative reply to "I've been feeling very lonely lately." The merge notebook prints one anxiety reply. No external benchmark is named.

### Discrepancies

1. Inventory `methods` is `lora`, from the card sentence about integrating LoRA weights. The training notebook is QLoRA: a 4-bit NF4 base plus LoRA. The uploaded repository is the merged float16 model, not the adapter. Inventory dataset `jkhedri/psychology-dataset` and parent `google/gemma-2b-it` match the card and the notebooks.
2. The merged card says the adapters were "trained on preference-based psychological data" and does not say SFT. The training notebook's first paragraphs say the setup is not standard supervised fine-tuning and mention DPO-style methods as a later direction. The cells that ran, the later notebook markdown, the adapter card ("instruction–response pairs"), and the Medium post all describe supervised training on `response_j` only.
3. The training notebook header calls `ecorbari/Gemma-2b-it-Psych` "the final merged model." That repository is the adapter. The merge notebook and the merged card name `ecorbari/Gemma-2b-it-Psych-Merged`.
4. The Medium post says a cosine scheduler. The notebook does not set one. The README's final train loss of about 0.55 matches the late logged step (0.562), not the average `training_loss` of 0.707.

### Confidence

High that this merged repository is the `merge_and_unload` output of `ecorbari/Gemma-2b-it-Psych`, because the merge notebook names the id and its saved output records a push to that repo. High that the adapter was the QLoRA `SFTTrainer` run in the January 25 notebook, because that notebook's saved output records the push to the adapter repo and the README ties the two repos together.

### Queries tried

- `ecorbari Gemma-2b-it-Psych-Merged LoRA Ederson Corbari NeuroQuest`
- `"Ederson Corbari" OR ecorbari Gemma psychology QLoRA paper OR arxiv OR "Beyond Helpfulness"`
- Medium article, 2026-04-12, and the GitHub README
- Raw notebooks `02_GEMMA2B_FINE_TUNING.ipynb` and `03_GEMMA2B_MERGE_LORA.ipynb`
- Adapter card https://huggingface.co/ecorbari/Gemma-2b-it-Psych
- `jkhedri/psychology-dataset response_j response_k` and the dataset API (no card)
- `google/gemma-2b-it` model card ("2B instruct version")
- Hugging Face user page https://huggingface.co/ecorbari/models

## 3. gustavecortal/Piaget-0.6B

No training script was found. The model card states one LoRA recipe. Gustave Cortal's 2026 thesis mentions Piaget in one sentence and does not give that recipe. The dataset card and a Reddit post repeat the card.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/gustavecortal__Piaget-0.6B__2026-10-05.md`. Live page: https://huggingface.co/gustavecortal/Piaget-0.6B . Hub metadata: created 2025-07-08, last modified 2025-07-18. Files: one `model.safetensors`, tokenizer files, no `adapter_config.json`. The usage example sets `repo = "gustavecortal/Piaget-0.6B"`. The methodology paragraph does not repeat the size.
- Dataset card: `revision_3_experiments/hf_inventory/cache/datasets/gustavecortal__PsychologicalReasoning-15k__2026-10-06.md` and https://huggingface.co/datasets/gustavecortal/PsychologicalReasoning-15k . YAML: train split `num_examples: 15006`, `language: en`. The methodology paragraph matches the model card, including rank, alpha, epoch, and batch size. That paragraph is the same text, not a second account. The row count is dataset metadata.
- Reddit post, 2025-07-18, user `antcroca159`: https://www.reddit.com/r/MachineLearning/comments/1m3319j/p_piaget_a_language_model_for_psychological_and/ . It says "I just released Piaget" and then repeats the methodology paragraph, and it lists sizes 0.6B, 1.7B, 4B, and 8B. It does not add a learning rate or a score. Same status as in the pilot: a copy of the card.
- Thesis: Gustave Cortal, *Natural Language Processing for Subjectivity Analysis in Personal Narratives*, Université Paris-Saclay, 2026, NNT 2026UPASG003, https://theses.hal.science/tel-05501345 . In the closing section "Speculative ideas," under "Preferences and reasoning data," the text says: "in my personal time, I have trained Piaget, a language model finetuned on 15,000 psychological and philosophical reasoning traces." The next sentences say Beck "is based on Piaget and was aligned with psychotherapeutic preferences using direct preference optimization." The HTML conversion of the PDF marks that Piaget sentence with footnote 27. The footnote body was not in the extracted text. The extracted thesis does not contain `Piaget-0.6B`, `gustavecortal/Piaget-0.6B`, "LoRA", or rank 8. A slides PDF at https://gustavecortal.com/data/nlp_for_subjectivity_analysis_david_cohen.pdf is a talk version and does not describe this training run.
- CV line, no hyperparameters: "Piaget, a model fine-tuned for psychological reasoning, and Beck, a model aligned with psychotherapeutic preferences." https://gustavecortal.com/data/CV_Gustave_CORTAL.pdf . The site https://gustavecortal.com/ does not describe the training. The lab page http://www.lmf.cnrs.fr/Perso/GustaveCortal lists Piaget as a 2025 project and does not add hyperparameters.
- Position paper named on the card, CMCL 2024: https://aclanthology.org/2024.cmcl-1.23/ . The pilot already reported that this paper does not describe Piaget. It was not re-read in full for this batch.
- EMNLP 2025 paper, arXiv 2510.08649, "Formalizing Style in Personal Narratives": the HTML at https://arxiv.org/html/2510.08649v2 does not contain "Piaget". It is the style paper, not this fine-tune.
- A later repository uses a local snapshot of `gustavecortal/Piaget-0.6B` as the starting weights for ORPO. It is not the recipe for Piaget. https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_0.6b.yaml . That file sets LoRA `r: 4`, `lora_alpha: 8`, ORPO learning rate `0.0005`, and `output_dir: roger-0.6b`. The README says the repository "fine-tunes Hugging Face models for preference optimization using ORPO + LoRA." Created 2025-10-03, after the Piaget upload.
- Source-dataset cards, for provenance of the traces only: `revision_3_experiments/hf_inventory/cache/datasets/cognitivecomputations__dolphin-r1__2026-10-06.md` and `revision_3_experiments/hf_inventory/cache/datasets/GeneralReasoning__GeneralThought-430K__2026-10-06.md`.

### Training record

**(a) Objective.** Not stated anywhere found as SFT, DPO, ORPO, PPO, continued pre-training, or distillation. Card says: "Piaget, a language model finetuned on 15k psychological and philosophical reasoning traces" and "Clusters tagged psychology or philosophy were retained for LoRA finetuning (rank=8, alpha=16, max length=2048, epoch=1, batch size=16)." The thesis says "finetuned" on those traces and, in the same paragraph, says Beck used direct preference optimization. That sentence does not name the loss used for Piaget. It does say the preference-optimization step belongs to Beck, not to this fine-tune. The dataset has `messages`, `reasoning`, and `answer`. Those column names are not a trainer.

**(b) Parameter-update scope.** LoRA, as stated on the card: rank 8, alpha 16. Target modules: not stated anywhere found. Learning rate: not stated anywhere found. The upload is a full `model.safetensors` with no `adapter_config.json`. The card does not say whether the adapter was merged before upload. The ORPO config's rank 4 and alpha 8 are a later run that starts from these weights.

**(c) Training data.** Card YAML lists `cognitivecomputations/dolphin-r1`, `GeneralReasoning/GeneralThought-430K`, and `gustavecortal/PsychologicalReasoning-15k`. Card prose says the model "was finetuned on a subset of open reasoning traces" from Dolphin R1 and General Reasoning, and the released subset is the 15k set. Dataset YAML: 15,006 train rows, language `en`. Filtering, on the card: prompts embedded, k-means with k=20,000, majority-vote domain labels from `Qwen/Qwen3-1.7B`, clusters tagged psychology or philosophy kept. Dolphin R1's own card says that corpus is "300k reasoning samples from DeepSeek-R1", "300k reasoning samples from Gemini 2.0 flash thinking", and "200k samples of Dolphin chat." GeneralThought-430K's card says the traces come from several reasoning models, including DeepSeek-R1, DeepSeek-R1-Zero, OpenThinker-32B, LIMO, deepseek-r1-distill-llama-70b, DeepHermes-3-Llama-3-8B-Preview, and DeepScaleR-1.5B-Preview, plus final answers from o3-mini, Gemini 2.0 Flash Thinking, and Claude 3.7 Sonnet. The 15k card does not say which of those generators produced each kept row. Provenance of the released training set: a filter of those model-generated traces. The prompts' original human or dataset sources are not restated on the Piaget card.

**(d) Base model.** Card YAML: `Qwen/Qwen3-0.6B`. The cached parent card `revision_3_experiments/hf_inventory/cache/readmes/Qwen__Qwen3-0.6B__2026-10-05.md` says "Training Stage: Pretraining & Post-training". The separate Base card `Qwen__Qwen3-0.6B-Base__2026-09-24.md` says "Training Stage: Pretraining". This fine-tune names the post-trained checkpoint, not `Qwen/Qwen3-0.6B-Base`. The Qwen card does not use the word "instruct" for this id. It is the post-trained checkpoint, with the thinking-mode chat template described on that card.

**(e) Hyperparameters.** Stated on the card, and copied on the dataset card: rank 8, alpha 16, max length 2048, 1 epoch, batch size 16. Hardware on the card: "HPC resources (Jean Zay supercomputer) from GENCI-IDRIS (Grant 20XX-AD011014205)." The grant id is printed with "20XX". Learning rate and target modules: not stated anywhere found. Nothing in this paragraph is specific to 0.6B.

**(f) Evaluation.** Not stated anywhere found.

### Discrepancies

1. Inventory `methods` is `lora`, datasets are the three ids above, and parent is `Qwen/Qwen3-0.6B`. That matches the card. The inventory does not record an objective. The card does not name one either.
2. The dataset card and the Reddit post repeat the methodology paragraph. They are not a second measurement of rank, alpha, epoch, or batch size.
3. The thesis names Piaget and 15,000 traces. It does not name this repository id and does not restate LoRA. It does not contradict the card.
4. The card does not say the LoRA was merged. The file list is a full checkpoint without `adapter_config.json`. That does not decide the question.
5. `config_0.6b.yaml` in the ORPO repository is a later preference run. Its rank 4 and alpha 8 are not the Piaget card's rank 8 and alpha 16.

### Confidence

Medium. This repository's card states the recipe and puts `gustavecortal/Piaget-0.6B` in the usage example. The same paragraph is on the 1.7B, 4B, and 8B cards, with only the base id and the example repo string changed. The thesis confirms that Cortal trained a model he calls Piaget on about 15,000 traces, and it does not attach the LoRA settings to this size.

### Queries tried

- `"Gustave Cortal" Piaget Qwen3 psychological reasoning LoRA 2025 OR 2026`
- `"PsychologicalReasoning-15k" OR "Piaget-0.6B" OR "Piaget-1.7B" OR "Piaget-4B" Cortal`
- `"Piaget-0.6B" OR "Piaget-1.7B" OR "Piaget-4B" OR "gustavecortal/Piaget" site:arxiv.org OR site:openreview.net OR site:aclanthology.org`
- `"Natural language processing for subjectivity analysis in personal narratives" Cortal Piaget thesis`
- HAL thesis https://theses.hal.science/tel-05501345 (full-text HTML; Piaget appears in the closing section only)
- `site:github.com/gustavecortal Piaget-0.6B OR Piaget-1.7B OR Piaget-4B OR PsychologicalReasoning` (ORPO configs consume Piaget; they do not train it)
- https://gustavecortal.com/ and the CV PDF
- Reddit post cited above; dataset card; Dolphin R1 and GeneralThought cards
- arXiv HTML 2510.08649v2 searched for "Piaget": no match
- Diff of the 2026-10-05 cards for 0.6B, 1.7B, 4B, and 8B

## 4. gustavecortal/Piaget-1.7B

Same recipe text as Piaget-0.6B. The card differs in two places: `base_model: Qwen/Qwen3-1.7B`, and the usage example sets `repo = "gustavecortal/Piaget-1.7B"`. A line-by-line diff of the 2026-10-05 cards shows no other change. No paper or script states a 1.7B-specific rank, learning rate, epoch count, or data slice.

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/gustavecortal__Piaget-1.7B__2026-10-05.md`. Live page: https://huggingface.co/gustavecortal/Piaget-1.7B . Hub metadata: created 2025-07-08, last modified 2025-07-18. Files: one `model.safetensors`, no `adapter_config.json`. The live model tree on that page shows `Qwen/Qwen3-1.7B-Base`, then "Finetuned", then `Qwen/Qwen3-1.7B`, then this model.
- The dataset card, Reddit post, thesis, CV, website, CMCL 2024 paper, EMNLP 2025 paper, and Dolphin R1 / GeneralThought cards are the same documents as in section 3. None of them prints `Piaget-1.7B` except the model card, the dataset card's size list, and the Reddit size list.
- Later ORPO config, not this recipe: https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_1.7b.yaml . It points at a local snapshot of `gustavecortal/Piaget-1.7B` and sets LoRA `r: 4`, `lora_alpha: 8`, ORPO learning rate `0.0005`, batch size 4, `output_dir: roger-1.7b`.

### Training record

**(a) Objective.** Not stated anywhere found, for the same reason as 0.6B. The card's sentence is identical: "LoRA finetuning (rank=8, alpha=16, max length=2048, epoch=1, batch size=16)." The thesis does not single out 1.7B.

**(b) Parameter-update scope.** LoRA rank 8, alpha 16, from that sentence. Target modules: not stated anywhere found. Merge: not stated anywhere found. No `adapter_config.json`.

**(c) Training data.** Same three dataset ids and the same 15,006-row English `PsychologicalReasoning-15k` split. The card does not say this size saw a different subset. Provenance: the same filter of model-generated traces described in section 3. The label model used in that filter is `Qwen/Qwen3-1.7B`, which is also this checkpoint's base. The card does not say whether that coincidence changes the training.

**(d) Base model.** Card YAML: `Qwen/Qwen3-1.7B`. Cached parent card `Qwen__Qwen3-1.7B__2026-10-05.md`: "Training Stage: Pretraining & Post-training". Cached Base card `Qwen__Qwen3-1.7B-Base__2026-10-06.md`: "Training Stage: Pretraining". This fine-tune names the post-trained checkpoint.

**(e) Hyperparameters.** Same card sentence as 0.6B. No size-specific learning rate, batch size, or epoch count. Hardware sentence is the same Jean Zay / GENCI-IDRIS line, including the placeholder grant id.

**(f) Evaluation.** Not stated anywhere found.

### Discrepancies

1. Inventory `lora`, the three dataset ids, and parent `Qwen/Qwen3-1.7B` match this card.
2. The methodology paragraph is the 0.6B paragraph with the base id and the example repo string replaced. The dataset card and the Reddit post copy that paragraph.
3. The thesis does not name `gustavecortal/Piaget-1.7B`.
4. Merge of the LoRA is not stated. The ORPO config's rank 4 and alpha 8 are a later run.

### Confidence

Medium. The card on this repository states the shared recipe and names `gustavecortal/Piaget-1.7B` in the example. No source states a training difference for this size, and the thesis does not identify this file.

### Queries tried

- The shared Cortal, thesis, arXiv, OpenReview, ACL, GitHub, website, and Reddit queries listed in section 3
- Live page https://huggingface.co/gustavecortal/Piaget-1.7B (model tree: Base, then `Qwen/Qwen3-1.7B`)
- `configs/config_1.7b.yaml` in `gustavecortal/preference-optimization-orpo-lora`
- Diff against the 0.6B card, 2026-10-05 copies

## 5. gustavecortal/Piaget-4B

Same recipe text as Piaget-0.6B. The card differs in two places: `base_model: Qwen/Qwen3-4B`, and the usage example sets `repo = "gustavecortal/Piaget-4B"`. A line-by-line diff of the 2026-10-05 cards shows no other change. The weight layout differs: two safetensors shards plus `model.safetensors.index.json`, still with no `adapter_config.json`. That is a file-size split, not a stated change in the training recipe.

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/gustavecortal__Piaget-4B__2026-10-05.md`. Live page: https://huggingface.co/gustavecortal/Piaget-4B . Hub metadata: created 2025-07-08, last modified 2025-07-18.
- The dataset card, Reddit post, thesis, CV, website, CMCL 2024 paper, EMNLP 2025 paper, and the two source-dataset cards are the same documents as in section 3. The thesis text that was extracted does not contain `Piaget-4B`.
- Later ORPO config, not this recipe: https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_4b.yaml . It points at a local snapshot of `gustavecortal/Piaget-4B` and sets LoRA `r: 4`, `lora_alpha: 8`, ORPO learning rate `0.0005`, `per_device_train_batch_size: 2`, `gradient_accumulation_steps: 4`, `output_dir: roger-4b`.

### Training record

**(a) Objective.** Not stated anywhere found. Same card sentence as 0.6B and 1.7B. The thesis does not single out 4B, and it assigns direct preference optimization to Beck.

**(b) Parameter-update scope.** LoRA rank 8, alpha 16. Target modules: not stated anywhere found. Merge: not stated anywhere found.

**(c) Training data.** Same three dataset ids, same 15,006 English rows, same filter. The card does not say the 4B run used a different subset. Provenance: model-generated traces, as in section 3, without a per-row generator on the 15k card.

**(d) Base model.** Card YAML: `Qwen/Qwen3-4B`. Cached parent card `Qwen__Qwen3-4B__2026-10-05.md`: "Training Stage: Pretraining & Post-training". Cached Base card `Qwen__Qwen3-4B-Base__2026-09-24.md`: "Training Stage: Pretraining". This fine-tune names the post-trained checkpoint, not `Qwen/Qwen3-4B-Base` and not `Qwen/Qwen3-4B-Instruct-2507`.

**(e) Hyperparameters.** Same rank, alpha, max length, one epoch, and batch size 16. No 4B-specific learning rate. Same Jean Zay sentence.

**(f) Evaluation.** Not stated anywhere found.

### Discrepancies

1. Inventory `lora`, the three dataset ids, and parent `Qwen/Qwen3-4B` match this card.
2. The methodology paragraph matches the 0.6B and 1.7B cards aside from the base id and the example repo string. Two weight shards are not a stated change in rank, data, or epochs.
3. The thesis does not name `gustavecortal/Piaget-4B`.
4. Merge of the LoRA is not stated. The ORPO config is a later run, with rank 4 and alpha 8.

### Confidence

Medium. The card on this repository states the shared recipe and names `gustavecortal/Piaget-4B` in the example. No source states a training difference for this size.

### Queries tried

- The shared Cortal, thesis, arXiv, OpenReview, ACL, GitHub, website, and Reddit queries listed in section 3
- Live page https://huggingface.co/gustavecortal/Piaget-4B
- `configs/config_4b.yaml` in `gustavecortal/preference-optimization-orpo-lora`
- Diff against the 0.6B card, 2026-10-05 copies
- Cached `Qwen/Qwen3-4B` and `Qwen/Qwen3-4B-Base` training-stage lines

## Patterns in this batch

Two of the five repositories publish the training code. Dzurec's script is full-weight `SFTTrainer` for three epochs on 3,512 counseling question-answer rows, starting from `SmolLM2-360M-Instruct`. Corbari's notebook is 4-bit QLoRA and `SFTTrainer` on the preferred column of a 9,846-row preference set, then `merge_and_unload` into `Gemma-2b-it-Psych-Merged`. The merged card's phrase "preference-based" is the dataset shape. The code that ran does not optimize a preference loss.

The three smaller Piaget cards are one paragraph. A diff against each other and against Piaget-8B changes only the base id and the example repository string. Rank 8, alpha 16, one epoch, and batch size 16 do not vary by size. The 2026 thesis now mentions Piaget, which the July 2025 pilot could not have seen, and the mention is one sentence in a speculative closing section. It says the fine-tune used 15,000 reasoning traces, and it says direct preference optimization was used for Beck, not for Piaget. It does not name these three repository ids, and it does not restate LoRA. The dataset card and the Reddit post still copy the model card.

No source states whether the Piaget LoRA was merged before upload. A later ORPO repository starts from local copies of these checkpoints with a different rank (4) and alpha (8). Those numbers are not the Piaget recipe. None of the five models in this batch has a published accuracy or preference benchmark. Dzurec's script selects a checkpoint by eval loss without publishing the number. Corbari's notebook logs validation loss. The Piaget cards report none.
