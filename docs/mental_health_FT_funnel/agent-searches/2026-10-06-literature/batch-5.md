# Batch 5: training records for five mental-health models

Date of search: 2026-10-06. Cards read: the 2026-10-05 copies under `revision_3_experiments/hf_inventory/cache/readmes/`. Hub file lists: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__020.csv` and `2026-10-05__022.csv`. Inventory reading: `revision_3_experiments/hf_inventory/results/mental-health/archive/2026-10-06/kept.csv`.

A claim below is tied to a source. If a field is missing from every source that was found, it is marked "not stated anywhere found." A method word inside a dataset or repository name is recorded as "name contains X" and is not treated as evidence of the training method.

## Summary

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Matches inventory row |
|---|---|---|---|---|---|---|
| howardbaik/gemma-4-E4B-it-mentalchat16k | blog (same author as the card) | supervised fine-tuning (SFT) | full weights in the published code; no LoRA block | ShenLab/MentalChat16K; blog printout 16,084 rows; 70/30 split; paper: 9,775 GPT-3.5 Turbo pairs plus 6,338 interview pairs paraphrased by Mistral-7B-Instruct-v0.2 | google/gemma-4-E4B-it (instruction-tuned) | yes |
| i5-8300h/gemma3-4b-psychology-dpo | blog (Reddit post; does not print this repo id). The detailed recipe is the model card | DPO | QLoRA (4-bit) plus LoRA; card says the uploaded weights are merged. Rank and alpha not stated | entfane/psychotherapy-dpo; 168 rows; provenance not stated | google/gemma-3-4b-it (card says instruction-tuned) | yes |
| iwalton3/phoenix | none for this checkpoint. A dataset card describes a file named for Phoenix and, separately, the training of a different model | not stated | not stated | card points at iwalton3/sycofact-training-data; that card's `phoenix_train.jsonl` is 5,970 synthetic conversations (steered Gemma 3 27B assistant turns, abliterated Gemma 3 27B user turns) | google/gemma-3-4b-it | partly |
| kebbbnnn/TinyLlama-Friendly-Psychotherapist | none | not stated. Inventory's `dpo` is the dataset name, not a stated method | not stated | four Hub sets in the card YAML, plus a Kaggle set named only in the card body. Counts and provenance differ by set; see section 4 | Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct (parent card says instruct-tuned) | no |
| lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented | none | not stated | not stated | RaviSheel04/Psychology-Data; 600,000 rows; provenance not stated | meta-llama/Llama-3.2-3B-Instruct | yes on the card (no outside source) |

## 1. howardbaik/gemma-4-E4B-it-mentalchat16k

The author's blog names this repository and prints the supervised-fine-tuning code. The model card repeats that recipe. A different repository, `mira2020/gemma-4-e4b-mentalchat16k-qlora`, is a QLoRA adapter for a different paper. It is not this checkpoint.

### Sources

- Blog post by Howard Baik, published 2026-04-13, "Finetuning with TRL." https://passthetorch.dev/posts/finetuning-with-trl/index.html . It prints `howardbaik/gemma-4-E4B-it-mentalchat16k`. The about page names the author: https://passthetorch.dev/about.html . The Colab link in the post did not survive as a URL in the fetched text, and a search for that notebook did not find it.
- Model card, cached at `revision_3_experiments/hf_inventory/cache/readmes/howardbaik__gemma-4-E4B-it-mentalchat16k__2026-10-05.md`. The training numbers match the blog. This is the same author's shortened card, not a second witness.
- Dataset paper, KDD 2025, also arXiv:2503.13509. Authors: Jia Xu, Tianyi Wei, Bojian Hou, Patryk Orzechowski, Shu Yang, Ruochen Jin, Rachael Paulbeck, Joost Wagenaar, George Demiris, Li Shen. https://arxiv.org/pdf/2503.13509v2.pdf . It describes MentalChat16K and the authors' own QLoRA runs on 7B models. It does not name this repository.
- Dataset card: https://huggingface.co/datasets/ShenLab/MentalChat16K
- Near miss, a different checkpoint: https://huggingface.co/mira2020/gemma-4-e4b-mentalchat16k-qlora . That card says the adapter is for "When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA" (KDD Undergraduate Consortium 2026) and gives QLoRA rank 64, alpha 16. It does not say those settings were used for `howardbaik/gemma-4-E4B-it-mentalchat16k`.
- Hub file list (2026-10-05 card cache): `model.safetensors` and no `adapter_config.json`. Created 2026-04-12, modified 2026-04-14. Relation recorded as finetune of `google/gemma-4-E4B-it`.

### Training record

**(a) Objective.** Supervised next-token fine-tuning.

- Blog says: "We then set up the `SFTTrainer` from the TRL library to perform supervised fine-tuning on our dataset." The printed code is `from trl import SFTConfig, SFTTrainer` and `trainer = SFTTrainer(...)`. https://passthetorch.dev/posts/finetuning-with-trl/index.html
- Card says: "Method: Supervised fine-tuning (SFT)" and "Framework: TRL `SFTTrainer` with `SFTConfig`." Cached card path above. The card also has a YAML tag `sft`.
- The blog's opening sentence mentions that TRL also supports PPO. The training code that follows is `SFTTrainer` only. PPO is not the method used for this run.

**(b) Parameter-update scope.** The published code loads the full base model and does not attach a LoRA adapter or a 4-bit quantizer.

- Blog code: `model = AutoModelForCausalLM.from_pretrained(MODEL_ID, dtype="auto", device_map="auto")` with `MODEL_ID = "google/gemma-4-E4B-it"`, then that model is passed to `SFTTrainer`. No `LoraConfig`, no `BitsAndBytesConfig`, and no PEFT import appears in the post. https://passthetorch.dev/posts/finetuning-with-trl/index.html
- The post never uses the words "full fine-tune" or "all parameters." The evidence is the code that is printed.
- Hub siblings: one `model.safetensors`, no `adapter_config.json`. LoRA rank, alpha, and target modules: not stated anywhere found. Adapter merge: not stated anywhere found, and no adapter file is in the repository.

**(c) Training data.**

- Blog says: `dataset = load_dataset("ShenLab/MentalChat16K")` and the printed dataset is `num_rows: 16084` with fields `instruction`, `input`, `output`. It then does `train_test_split(..., test_size=0.3, random_state=42)`. https://passthetorch.dev/posts/finetuning-with-trl/index.html
- Card says: "`ShenLab/MentalChat16K` — ~16K counselor-style conversational turns combining synthetic data and anonymized interview transcripts" and "Training and validation sets (70/30 split)." Cached card.
- Paper says: "we used the OpenAI GPT-3.5 Turbo model to generate 9,775 question-answer pairs" and, for the interview half, "we employed the local Mistral-7B-Instruct v0.2 model" and "filtered out any conversations with less than 40 words in the question and answer, resulting in a total of 6,338 question-answer pairs." The interview text started as human transcripts of a clinical trial and was then paraphrased by that Mistral model. Language: "an English benchmark dataset." https://arxiv.org/pdf/2503.13509v2.pdf
- 9,775 + 6,338 = 16,113. The blog's load printout says 16,084. Both numbers are stated. This search did not re-download the dataset to decide which count the Hub file has today.

**(d) Base model.** `google/gemma-4-E4B-it`.

- Blog says: `MODEL_ID = "google/gemma-4-E4B-it"`. https://passthetorch.dev/posts/finetuning-with-trl/index.html
- Google's card for that id says: "This release includes open-weights models in both pre-trained and instruction-tuned variants." The Hub model tree for `google/gemma-4-E4B-it` is labeled "Base model / Finetuned." https://huggingface.co/google/gemma-4-E4B-it
- The Howard card says: "Causal language model (Gemma 4, E4B variant, instruction-tuned)."

**(e) Hyperparameters and hardware.**

- Blog and card agree: 3 epochs; per-device batch size 1 for training and 2 for evaluation; gradient accumulation 16; learning rate 2e-5; cosine schedule; warmup 5 steps; AdamW fused; bf16; gradient checkpointing with `use_reentrant=False`; max gradient norm 1.0; A100 High RAM on Google Colab; "After 6 hrs (!!!) of training." https://passthetorch.dev/posts/finetuning-with-trl/index.html
- Both also say the warmup is "5 steps (~3% of 183 total steps)." See discrepancy 1. That step count is not compatible with training on about 70% of 16,084 rows at an effective batch of 16 for 3 epochs. Using the blog's own formula, `total_steps = (num_samples // (batch_size * gradient_accumulation_steps)) * num_epochs`, 70% of 16,084 is about 11,258 examples, and 11,258 // 16 * 3 = 2,109 steps, not 183. The post does not say the run was cut short or subsampled.

**(f) Evaluation.** No benchmark scores for this checkpoint.

- Blog: training and evaluation loss are described as decreasing, with two figures that the fetch did not include as numbers, plus one side-by-side generation against a MentalChat16K target answer. https://passthetorch.dev/posts/finetuning-with-trl/index.html
- Card: evaluation and checkpointing every epoch, and "loading the best model at end." No scores. It also says "performance on other languages is not evaluated."
- The MentalChat16K paper's 200-question judge evaluation is for the paper's own 7B fine-tunes (LLaMA-2, Mistral, Mixtral, Vicuna). It does not include this Gemma 4 model.

### Discrepancies

1. The same post states 16,084 rows, a 30% validation split, effective batch 16, 3 epochs, and 183 total steps. Those figures do not describe one uninterrupted pass over that split. The card copies the 183-step sentence from the post.
2. The blog's row printout is 16,084. The dataset paper's two halves add to 16,113 (9,775 + 6,338).
3. `mira2020/gemma-4-e4b-mentalchat16k-qlora` is QLoRA, rank 64, alpha 16, learning rate 5e-5. That is a different repository. The inventory row for Howard Baik is `sft`, which matches the blog, not that adapter.
4. The dataset paper fine-tunes its own models with QLoRA on one A40 or A100. That recipe is not the recipe in Howard Baik's post.

### Confidence

High. The blog prints this repository id, the base id, `SFTTrainer`, and the hyperparameters that the card repeats, and the Hub dates (created 2026-04-12, blog published 2026-04-13) sit next to that post.

### Queries tried

- howardbaik gemma-4-E4B-it-mentalchat16k fine-tune
- "gemma-4-E4B-it-mentalchat16k"
- MentalChat16K ShenLab dataset paper synthetic interview transcripts
- passthetorch Howard Baik MentalChat16K SFTTrainer Colab
- site:colab.research.google.com MentalChat16K gemma-4-E4B howardbaik OR "passthetorch"
- "Howard Baik" MentalChat16K OR gemma-4-E4B SFT OR fine-tune
- google/gemma-4-E4B-it instruction-tuned model card

## 2. i5-8300h/gemma3-4b-psychology-dpo

The model card is the detailed recipe. A Reddit post by u/i5_8300h describes the same hardware and the same two method words, and does not print the repository id. No paper and no training script were found. The name contains "dpo"; the card also states DPO in the training section, which is the evidence used here.

### Sources

- Model card, cached at `revision_3_experiments/hf_inventory/cache/readmes/i5-8300h__gemma3-4b-psychology-dpo__2026-10-05.md`. Author on the card: Ram Sundar Radhakrishnan. The Hugging Face user page https://huggingface.co/i5-8300h uses that same display name.
- Reddit post by u/i5_8300h, r/LocalLLaMA, thread `1s5z0kx`. https://www.reddit.com/r/LocalLLaMA/comments/1s5z0kx/local_llm_evaluation_advice_after_dpo_on_a/ . The live page and old.reddit.com returned a block page. The quote below is the text returned by web search for that thread (a snapshot indexed with the date 2026-04-03). The post does not print `i5-8300h/gemma3-4b-psychology-dpo`.
- Dataset page https://huggingface.co/datasets/entfane/psychotherapy-dpo . README body is empty. The Hub dataset API says 168 train examples, columns `illness`, `input`, `chosen`, `rejected`, last modified 2025-03-30. The dataset page lists this model and `i5-8300h/gemma3-4b-psychology-dpo-Q4_K_M-GGUF` as models trained on it. That listing is the Hub's "trained on this dataset" link, not a second write-up of the method.
- A different dataset by the same user, https://huggingface.co/datasets/entfane/psychotherapy , says it was generated by Gemini 2.0 Flash and has 1,260 rows. It does not say that `entfane/psychotherapy-dpo` was built from it.
- Hub file list: `model.safetensors` and no `adapter_config.json`. Created 2026-02-06, modified 2026-04-01. Dtype code in the inventory row: F16. Relation: finetune of `google/gemma-3-4b-it`.

### Training record

**(a) Objective.** Direct preference optimization, as stated on the card and in the Reddit post.

- Card says: "DPO Finetuning + PeFT and LoRA" and "Beta = 0.1" and "Used precomputed reference log probabilities to avoid loading a reference model." Cached card.
- Reddit text from the search index: "I fine-tuned Gemma 3 4B on a psychotherapy dataset using DPO as part of an experiment to make a local chatbot that can act as a companion." https://www.reddit.com/r/LocalLLaMA/comments/1s5z0kx/local_llm_evaluation_advice_after_dpo_on_a/
- The repository name contains "dpo". That is not the evidence. The training-section sentence is.

**(b) Parameter-update scope.** QLoRA: a 4-bit base plus a LoRA adapter, then merged into the file that was uploaded. Rank, alpha, and target modules are not stated anywhere found.

- Card says: "Training regime: FP16 mixed precision and QLoRA quantized weights (4bits), 3 epochs at 2e-5 lr" and "This repo contains merged weights." Cached card.
- Reddit text: "I must thank whoever invented QLoRa and PeFT - I was able to run the finetuning on my RTX 3050Ti laptop."
- Hub siblings contain `model.safetensors` and do not contain `adapter_config.json`, which fits a merged upload. The rank is still not stated.

**(c) Training data.**

- Card says the training data URL is `https://huggingface.co/datasets/entfane/psychotherapy-dpo`. Card YAML `language: en`.
- Dataset API: 168 examples in the train split. README: empty, so the generator is not stated anywhere found. Viewer rows are English client statements with a `chosen` answer and a `rejected` answer, and an `illness` field with 21 classes. That layout is not a statement of who wrote the text.
- `entfane/psychotherapy` (1,260 rows, Gemini 2.0 Flash, 21 named conditions) is a different dataset. This search did not find a sentence that says the 168-row preference set was derived from it.

**(d) Base model.** `google/gemma-3-4b-it`.

- Card says: "Finetuned from model: Google Gemma 3 4B (Instruction Tuned)" and the YAML `base_model` is `google/gemma-3-4b-it`. Cached card.
- Google's Gemma 3 model card says the family has "open weights for both pre-trained variants and instruction-tuned variants." https://ai.google.dev/gemma/docs/core/model_card_3 . The fetch of `google/gemma-3-4b-it`'s raw README returned HTTP 401, so that page was not quoted directly.

**(e) Hyperparameters and hardware.**

- Card: learning rate 2e-5; 3 epochs; max prompt length 128; max length 256; beta 0.1; dtype float16; "~6.5 hours for all 3 epochs (33 steps)"; "3.8/4 GB VRAM used on RTX 3050Ti"; machine "Acer Swift X SFX14 R1SG", "AMD Ryzen 7 5800u", "NVIDIA RTX 3050Ti 4GB", "16GB DDR4". Software list includes `trl: 0.21.0`, `peft: 0.18.1`, `bitsandbytes: 0.46.0`. Cached card.
- Per-device batch size: not stated anywhere found. 168 examples times 3 epochs is 504 example-presentations. The card's 33 steps do not divide 168. The card does not say how 33 steps were counted, so this search does not turn 33 into a batch size.
- Reddit text names the RTX 3050Ti and does not give the learning rate, epoch count, or step count.

**(f) Evaluation.** Not stated anywhere found. The Reddit post asks which local tests to run and does not report scores. The card has no results section.

### Discrepancies

1. The Reddit post does not print the repository id or `entfane/psychotherapy-dpo`. It does match the card on Gemma 3 4B, DPO, QLoRA, PEFT, and an RTX 3050Ti.
2. The card says 33 steps for 3 epochs. The dataset has 168 rows. The card does not explain the gap.
3. Inventory `kept.csv` methods are `dpo|qlora`, dataset `entfane/psychotherapy-dpo`, parent `google/gemma-3-4b-it`. That matches the card. The inventory row does not record "merged weights" or the missing LoRA rank. Those are omissions, not a conflicting method.

### Confidence

Medium. The card is attached to this repository and states the recipe. The Reddit account name, the GPU, and the method words line up, but that post never prints the Hugging Face id, so it is not by itself a proof that the uploaded file is that run.

### Queries tried

- "gemma3-4b-psychology-dpo" Ram Sundar Radhakrishnan
- "i5-8300h/gemma3-4b-psychology-dpo"
- entfane/psychotherapy-dpo dataset Hugging Face
- site:github.com i5-8300h gemma3 psychology dpo OR "psychotherapy-dpo"
- "gemma3-4b-psychology-dpo" OR "psychotherapy-dpo" LoRA QLoRA
- Hugging Face user page https://huggingface.co/i5-8300h and dataset API for entfane/psychotherapy-dpo
- Reddit thread 1s5z0kx (search index; live fetch blocked)

## 3. iwalton3/phoenix

The Phoenix card says "custom fine-tune" and points at a dataset. That dataset card's hyperparameter list is for SycoFact, a different model in the same account. No paper, GitHub training script, or notebook naming `iwalton3/phoenix` was found. Izzie Walton's public GitHub account (https://github.com/iwalton3) did not show a Phoenix or SycoFact repository in the repository list that was fetched.

### Sources

- Model card, cached at `revision_3_experiments/hf_inventory/cache/readmes/iwalton3__phoenix__2026-10-05.md`. It does not print an objective, a LoRA config, or a step count.
- Dataset card by Izzie Walton, https://huggingface.co/datasets/iwalton3/sycofact-training-data . Citation block: author "Izzie Walton", title "SycoFact 4B", year 2026. It does not print the string `iwalton3/phoenix`. It does name `phoenix_train.jsonl` and "Phoenix therapeutic data." The "Models trained or fine-tuned on" list on that page names `iwalton3/sycofact` only.
- SycoFact model card, cached at `revision_3_experiments/hf_inventory/cache/readmes/iwalton3__sycofact__2026-10-05.md`. That card is an evaluator, not Phoenix. Its benchmark tables are for SycoFact. The paper link on that card, arXiv:2509.10970, is Psychosis-Bench, cited as an evaluation set for SycoFact, not as a training paper for Phoenix.
- Reddit post by u/scratchr, 2026-03-20, https://www.reddit.com/r/LocalLLaMA/comments/1rz1igl/phoenix_4b_an_honest_mental_health_companion/ . The fetched text repeats the model card, including "This is a custom fine-tune of Gemma3 4B," and links the Hub id. It adds no training settings. Ollama https://ollama.com/izzie/phoenix repeats the same card text.
- Hub file list: two safetensors shards, `Phoenix_4B-Q8_0.gguf`, no `adapter_config.json`. Created 2026-03-20, modified 2026-03-29. Inventory dtype BF16. `baseModels.relation` in the card cache is `quantized`, not `finetune`, while the card text says fine-tune.

### Training record

**(a) Objective.** Not stated anywhere found for this checkpoint.

- Card says: "This is a custom fine-tune of Gemma3 4B, see the Phoenix training data linked in the model card for details." Cached Phoenix card. "Custom fine-tune" does not say supervised fine-tuning, DPO, or reinforcement learning.
- Dataset card says each evaluator record "is in chat messages format compatible with SFTTrainer / TRL." That sentence is about file format. It is under the evaluator-data description. It is not a statement that Phoenix was trained with `SFTTrainer`.
- The same dataset card says: "SycoFact was trained on both the evaluator data and the Phoenix therapeutic data" and then "Full finetune (all parameters); 3 epochs, LR 5e-6, batch size 1 × 8 gradient accumulation." Those parameters are in the section "Reproducing SycoFact." They are not stated for `iwalton3/phoenix`.

**(b) Parameter-update scope.** Not stated anywhere found for this checkpoint.

- The SycoFact sentence "Full finetune (all parameters)" is in that reproducing section. Applying it to Phoenix would be a guess.
- This repository's files are full BF16 weights plus a Q8_0 GGUF, and there is no `adapter_config.json`. That shows what was uploaded. It does not say whether training updated every weight or a LoRA adapter that was merged before upload. Rank and alpha: not stated anywhere found.

**(c) Training data.** The Phoenix card's YAML `datasets` entry is `iwalton3/sycofact-training-data`. The dataset card separates three files.

- Dataset card says: "`phoenix_train.jsonl` | 5,970 | Therapeutic conversation data" and "This data was synthetically generated using steered Gemma 3 27B for assistant turns and Gemma 3 27B abliterated for user turns." https://huggingface.co/datasets/iwalton3/sycofact-training-data
- The same table lists `sycofact_train.jsonl` at 37,898 records and `sycofact_val.jsonl` at 4,210. The page total is 48,078 rows. Those larger files are the evaluator set. The dataset card says SycoFact used both the evaluator data and the Phoenix file. It does not say Phoenix was trained on the evaluator files.
- Phoenix card YAML `language: en`. The SycoFact card says "English only" for SycoFact. The Phoenix card does not repeat that sentence.

**(d) Base model.** YAML `base_model: google/gemma-3-4b-it` on the Phoenix card. The prose says "Gemma3 4B" and does not say "instruction-tuned." The id is the `-it` checkpoint. Google's Gemma 3 card says the release includes instruction-tuned variants (https://ai.google.dev/gemma/docs/core/model_card_3). The raw README for `google/gemma-3-4b-it` returned HTTP 401.

**(e) Hyperparameters and hardware.** Not stated anywhere found for this checkpoint. The 3 epochs, learning rate 5e-6, batch 1 × 8, bf16, and "single A40 GPU (RunPod)" lines are in the SycoFact section of the dataset card.

**(f) Evaluation.** Not stated anywhere found for Phoenix. The detection rates, correlations, and RewardBench numbers on the SycoFact card are for `iwalton3/sycofact`.

### Discrepancies

1. Inventory methods are blank. That matches "not stated." Inventory datasets are the whole repo `iwalton3/sycofact-training-data`, which is what the Phoenix card YAML lists. The dataset card's Phoenix file is the 5,970-row `phoenix_train.jsonl`, and the only model that page lists as trained on the dataset is `iwalton3/sycofact`.
2. Hub `baseModels.relation` is `quantized`. The card says "custom fine-tune." The repository contains both BF16 safetensors and a Q8_0 GGUF.
3. Copying the dataset card's "full finetune, 3 epochs, 5e-6" block onto Phoenix would contradict the heading those bullets sit under ("Reproducing SycoFact").

### Confidence

Medium that `phoenix_train.jsonl` is the file the Phoenix card means by "Phoenix training data." Low that any particular objective or hyperparameter on the SycoFact card was used to produce `iwalton3/phoenix`. No source prints both the Phoenix repository id and a training procedure.

### Queries tried

- "iwalton3/phoenix" Gemma mental health
- iwalton3 phoenix sycofact github gemma fine-tune
- "Izzie Walton" OR iwalton3 OR scratchr phoenix gemma "full finetune" OR SFT
- "iwalton3/phoenix" OR "phoenix_train.jsonl" site:github.com
- dataset page https://huggingface.co/datasets/iwalton3/sycofact-training-data
- GitHub user page https://github.com/iwalton3
- Reddit r/LocalLLaMA Phoenix 4B (u/scratchr) and Ollama izzie/phoenix

## 4. kebbbnnn/TinyLlama-Friendly-Psychotherapist

The card is the Hugging Face template. The only sentence that says this model was fine-tuned is the Kaggle paragraph. No paper, GitHub script, or notebook naming this repository was found. The Hugging Face display name on https://huggingface.co/kebbbnnn is Kevin Ladan. A separate repository, `kebbbnnn/lora-tinyllama-1.1b-chat-v1.0.Q4_K_M-Mental_Health-LATEST.bin`, is a LoRA adapter for a different TinyLlama file. It is not this checkpoint. Dataloop's page about this model repeats the Kaggle sentence from the card; that is not a second witness.

### Sources

- Model card, cached at `revision_3_experiments/hf_inventory/cache/readmes/kebbbnnn__TinyLlama-Friendly-Psychotherapist__2026-10-05.md`. Created 2024-09-15, modified 2024-09-16. Files: `model.safetensors`, no `adapter_config.json`. Inventory dtype F16. Relation: finetune of `Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct`.
- Kaggle dataset named in the card: https://www.kaggle.com/datasets/kreeshrajani/3k-conversations-dataset-for-chatbot . The fetched page is the public about-text. It does not mention this model.
- Dataset APIs, fetched 2026-10-06: `Amod/mental_health_counseling_conversations`, `mpingale/mental-health-chat-dataset`, `heliosbrahma/mental_health_chatbot_dataset`, `SAGI-1/Greetings_DPO_dataset_V1`.
- Parent card: https://huggingface.co/Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct/raw/main/README.md . That page describes the parent, not this fine-tune.
- v1.5 card `kebbbnnn__TinyLlama-Friendly-Psychotherapist-v1.5__2026-10-05.md` is the same empty template and does not add a method.

### Training record

**(a) Objective.** Not stated anywhere found.

- Card body, training procedure: "[More Information Needed]." Cached card.
- Card body, the one positive sentence: "One of the datasets used to finetune this model is from Kaggle, specifically the 3K Conversations Dataset for ChatBot." "Finetune" here is not SFT, DPO, or reinforcement learning.
- Inventory methods: `dpo`. The inventory evidence quote is the YAML dataset line that includes `SAGI-1/Greetings_DPO_dataset_V1`. The dataset name contains "DPO". The card never says this model was trained with DPO. `SAGI-1/Greetings_DPO_dataset_V1` is a preference file (columns `prompt`, `chosen`, `rejected`; 891 rows; README empty). A preference-shaped file is not a statement that this checkpoint's loss was DPO.

**(b) Parameter-update scope.** Not stated anywhere found. The upload is one `model.safetensors` and has no `adapter_config.json`. Rank, alpha, and merge: not stated anywhere found. The other LoRA repository named above is a different file (`tinyllama-1.1b-chat`, Q4_K_M) and its card says "lora adapter for tinyllama-1.1b-chat-v1.0.Q4_K_M, fine-tuned using Mental Health Counseling Dataset."

**(c) Training data.** Two lists, and they are not the same list.

Card YAML `datasets`:

- `Amod/mental_health_counseling_conversations`. API description: "real one-on-one mental health counseling conversations between individuals and licensed professionals." Language tag `en`. Size category on the API card: `1K<n<10K`. The API payload did not include an example count (the size endpoint returned HTTP 401).
- `mpingale/mental-health-chat-dataset`. API: 2,775 train examples. Columns include `questionText`, `therapistInfo`, `answerText`. The short description is "More Information needed." Provenance: not stated anywhere found in that payload. Language: not stated in the tags that were returned.
- `heliosbrahma/mental_health_chatbot_dataset`. API: 172 train examples, language `en`. Card summary: "curated from popular healthcare blogs like WebMD, Mayo Clinic and HeatlhLine, online FAQs" (spelling as on the card). That is edited web text, not a named generator model.
- `SAGI-1/Greetings_DPO_dataset_V1`. API: 891 train examples. README empty. Viewer rows are English greetings. Several `chosen` answers say the speaker is an assistant created by SuperAGI. The card does not state a generator model or a language tag.

Card body, not in the YAML list:

- Kaggle "3K Conversations Dataset for ChatBot." The Kaggle about-text says: "The dataset may include various types of conversations such as casual or formal discussions, interviews, customer service interactions, or social media conversations." The model card drops "may" and otherwise copies that sentence. Exact row count: not stated on the fetched Kaggle page; the title says 3K. Provenance: not stated anywhere found.

**(d) Base model.** Card YAML: `Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct`.

- Parent card says: "This is an instruct-tuned TinyLlama-1.1B-32k on several open-source instruct datasets, intended primarily for speculative decoding." https://huggingface.co/Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct/raw/main/README.md
- The same parent card says "This model was trained as a full finetune for 3 epochs using a single A100 GPU for around 3.5 hours." That sentence is about `Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct`, not about `kebbbnnn/TinyLlama-Friendly-Psychotherapist`.

**(e) Hyperparameters and hardware.** Not stated anywhere found. The card's training-regime line is the template placeholder "[More Information Needed]."

**(f) Evaluation.** Not stated anywhere found. The evaluation headings on the card are the empty template.

### Discrepancies

1. Inventory methods `dpo` do not match a stated training objective. The evidence string in `kept.csv` is the dataset name `Greetings_DPO_dataset_V1`.
2. Inventory datasets are the four YAML ids. The card body also names the Kaggle 3K conversations set, which is not in the inventory datasets column.
3. The parent model's "full finetune, 3 epochs, A100" sentence is not a description of this repository.

### Confidence

Low that any specific objective or update scope produced this file. High that the card itself does not state one. The Kaggle sentence is the only sentence that says the model was fine-tuned, and it names one dataset.

### Queries tried

- "TinyLlama-Friendly-Psychotherapist" kebbbnnn
- Kevin Ladan TinyLlama Friendly Psychotherapist kaggle fine-tune
- site:github.com kebbbnnn TinyLlama Psychotherapist OR "Friendly-Psychotherapist"
- Kaggle page kreeshrajani/3k-conversations-dataset-for-chatbot
- Hugging Face user https://huggingface.co/kebbbnnn and the LoRA repo `kebbbnnn/lora-tinyllama-1.1b-chat-v1.0.Q4_K_M-Mental_Health-LATEST.bin`
- Dataset APIs for Amod, mpingale, heliosbrahma, and SAGI-1/Greetings_DPO_dataset_V1
- Parent README Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct

## 5. lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented

The card says the model is a fine-tuned Llama 3.2 3B Instruct and names one dataset. It does not say which loss was used or whether all weights were updated. No paper, GitHub repository, or notebook naming this repository or "lavanyamurugesan123" was found. Other Llama-3.2-3B therapy fine-tunes that search returned (CBT-Copilot, CogBeTh, Ishan93/Fine_tuned_ver2, rockson8/llama-3.2-3b-psychotherapy-cbt) are different repositories and are not evidence about this file.

### Sources

- Model card, cached at `revision_3_experiments/hf_inventory/cache/readmes/lavanyamurugesan123__Llama3.2-3B-Instruct-finetuned-Therapy-oriented__2026-10-05.md`. Created 2025-05-20, modified the same day. Files: two safetensors shards, no `adapter_config.json`. Inventory dtype F16. Relation: finetune of `meta-llama/Llama-3.2-3B-Instruct`.
- Dataset page https://huggingface.co/datasets/RaviSheel04/Psychology-Data . "README.md exists but content is empty." The datasets-server rows API returned `num_rows_total: 600000` and columns `Human`, `Assistant`, `Instructions`. The page lists this model under "Models trained or fine-tuned on" this dataset. That is the Hub link from the card's YAML, not a training write-up. A second dataset, `RaviSheel04/Psychology-Data2`, has 820,615 rows and an empty README, and does not list this model.
- Author page https://huggingface.co/RaviSheel04 shows the display name Ravi Sheel and no models. A LinkedIn page for that name does not mention this checkpoint or this dataset.

### Training record

**(a) Objective.** Not stated anywhere found.

- Card says: "Finetuned variant of Meta's Llama-3.2-3B-Instruct model for therapy-oriented, empathetic dialogue based on psychological principles." Cached card. "Finetuned" is not SFT, DPO, or reinforcement learning. The repository name contains "finetuned". That is the same word, not a method.

**(b) Parameter-update scope.** Not stated anywhere found. The upload is full safetensors shards and has no `adapter_config.json`. Rank, alpha, and merge: not stated anywhere found.

**(c) Training data.**

- Card YAML: `datasets: RaviSheel04/Psychology-Data`, `language: en`.
- Rows API: 600,000 examples. Columns `Human`, `Assistant`, `Instructions`. One returned instruction is "you are a Pyschology bot who answers user question in a polite manner." Provenance (human-written or synthetic, and any generator): not stated anywhere found. The empty README does not say.

**(d) Base model.** Card says: "Finetuned from model: meta-llama/Llama-3.2-3B-Instruct." The id contains "Instruct." Meta's README for that id was not opened in this search. The card does not quote Meta's training report.

**(e) Hyperparameters and hardware.** Not stated anywhere found. The card has no training-procedure section beyond the template leftovers that were not filled in.

**(f) Evaluation.** Not stated anywhere found.

### Discrepancies

None between the card and the inventory row. Inventory methods are blank, datasets are `RaviSheel04/Psychology-Data`, and the parent is `meta-llama/Llama-3.2-3B-Instruct`. There is no paper or script to disagree with the card. The empty dataset README does not say whether all 600,000 rows were used.

### Confidence

Low that a particular training procedure produced this file, because no procedure is written down. The card and the dataset page do name each other.

### Queries tried

- "Llama3.2-3B-Instruct-finetuned-Therapy-oriented" lavanyamurugesan
- "lavanyamurugesan123" OR "Llama3.2-3B-Instruct-finetuned-Therapy-oriented"
- RaviSheel04 Psychology-Data Llama therapy fine-tune lavanya
- "RaviSheel04/Psychology-Data" OR "you are a Pyschology bot" 600000
- "finetuned-Therapy-oriented" OR "Therapy-oriented" Llama-3.2-3B lavanya OR Murugesan
- datasets-server rows API for RaviSheel04/Psychology-Data
- Hugging Face user https://huggingface.co/RaviSheel04 and https://huggingface.co/lavanyamurugesan123 (the model page is the card already read)

## Patterns in this batch

Only one of the five repositories has a training write-up that both names the repository and shows the code: Howard Baik's blog, which is supervised fine-tuning with `SFTTrainer` and no LoRA block in the published script. The psychology model is the only preference-optimization run, and the evidence is the author's card plus a Reddit post that never prints the repository id. The card says QLoRA and says the weights were merged, and it never states the LoRA rank.

Phoenix and SycoFact share an author and a dataset repository. The only full-parameter recipe on that dataset card is headed as SycoFact's. Phoenix's own card stops at "custom fine-tune." Treating those SycoFact hyperparameters as Phoenix's would erase that distinction.

The TinyLlama inventory label `dpo` comes from a dataset id that contains the letters DPO. The card's training section is still the empty template. The therapy-oriented Llama card names a 600,000-row dataset and does not name a loss or an adapter. Across the batch, a YAML `datasets:` list and a word in a repository name are present even when the training objective is not.
