# Batch 1: how five medical models were trained

Cached cards read: newest README under `revision_3_experiments/hf_inventory/cache/readmes/` (2026-10-05). Inventory row: `revision_3_experiments/hf_inventory/results/medical/2026-10-06/kept.csv`. Hub file lists: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__008.csv`, `2026-10-05__009.csv`, `2026-10-05__010.csv`, and `2026-10-05__016.csv`. None of the five repositories contains `adapter_config.json`.

No paper, notebook, or blog found names any of these five repository ids. Papers below describe the datasets, or a different model trained on the same kind of data.

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Task trained for | Language | Matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sweatSmile/Gemma-2-2B-MedicalQA-Assistant | none | not stated | 4-bit base plus LoRA, rank 8, alpha 16; merge not stated | ChatDoctor-HealthCareMagic: card says 1,500 of 112,165; real HealthCareMagic dialogues | google/gemma-2-2b-it (instruction-tuned) | patient-doctor dialogue | en | partly |
| alpha-ai/Medical-Diagnosis-COT-Gemma3-270M | none | supervised fine-tuning | LoRA; rank and alpha not stated; card heading says merged weights | medical-o1-reasoning-SFT, English split 19,704, GPT-4o traces; card also says about 10,000 human rows with no Hub id | google/gemma-3-270m-it (instruction-tuned) | reasoning traces | en | partly |
| divyanshvats2004/medical-gemma-3-270m | none | supervised fine-tuning | not stated | ChatDoctor-HealthCareMagic: card says 4,500 of 112,165; real HealthCareMagic dialogues | google/gemma-3-270m-it (instruction-tuned) | patient-doctor dialogue | en | partly |
| tulas/gemma-3-270m-medical | none | not stated | LoRA, rank 64, alpha 16; card says adapters were merged | medrescue: corpus 86,667 English rows; how many of those 813 steps used is not stated; mixed human exam text and Gemma 3n synthetic Q&A | YAML: google/gemma-3-270m-it (instruction-tuned) | not stated | en | yes |
| SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it | none | supervised fine-tuning (YAML tag only) | not stated | PubMedQA via LlamaFactory: 10,000 train and 1,000 test; abstract conclusions, not a stated training count | google/gemma-3-1b-it (instruction-tuned) | open biomedical question answering | en | partly |

## 1. sweatSmile/Gemma-2-2B-MedicalQA-Assistant

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/sweatSmile__Gemma-2-2B-MedicalQA-Assistant__2026-10-05.md`. Names this repo id. Author line on the card: sweatSmile. No personal name.
- Hub file list, cache `2026-10-05__016.csv`: three `model-0000*-of-00003.safetensors` shards, no `adapter_config.json`. Safetensors total 2,614,341,888 float32 parameters. Hub tag `base_model:adapter:google/gemma-2-2b-it`. Created 2025-10-23.
- Dataset API: https://huggingface.co/api/datasets/lavita/ChatDoctor-HealthCareMagic-100k . Train split 112,165 rows. The dataset README says "More Information needed" and does not name this model.
- ChatDoctor paper, arXiv 2303.14070, PMC text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10364849/ . Describes collection of the HealthCareMagic dialogues and a LLaMA fine-tune. Does not print this repo id.
- GitHub repository search for `Gemma-2-2B-MedicalQA-Assistant` (7 Oct 2026): no repository with that name. https://github.com/azizdeniz890/gemma-medical-qa-lora is a different Gemma-2-2B-IT medical LoRA and points at `azizdeniz890/gemma-medical-qa-lora`, not this repo.
- Base-model card: https://huggingface.co/google/gemma-2-2b-it . Does not describe this fine-tune.

### Training record

**(a) Objective.** Not stated anywhere found. Card says: "This is a fine-tuned version of google/gemma-2-2b-it" and "Framework: TRL + Transformers + PEFT." It does not say supervised fine-tuning, preference optimization, reinforcement learning, or continued pre-training. TRL can run more than one of those. The word "fine-tuned" does not name the loss.

**(b) Parameter-update scope.** Card says: "Fine-tuning Method: LoRA (Low-Rank Adaptation)" and "Quantization: 4-bit (nf4) for efficient training and inference." That is a 4-bit base plus LoRA. Card also says: "Rank (r): 8", "Alpha: 16", "Dropout: 0.1", "Target Modules: All linear layers", and "Precision: BF16". It does not list module names. Whether the adapter was merged: not stated anywhere found. The usage example loads `AutoModelForCausalLM`, not a PEFT adapter. Hub siblings are three full float32 shards and no `adapter_config.json`. The upload is not a 4-bit file: the safetensors total is 2,614,341,888 float32 parameters, about 10.5 GB. Card says "Trainable Parameters: ~4.2M (0.2% of base)."

**(c) Training data.** Card YAML: `lavita/ChatDoctor-HealthCareMagic-100k`. Card says: "a curated subset" and "Training Samples: 1,500 high-quality medical Q&A pairs." The Hub dataset has 112,165 train rows with columns `instruction`, `input`, and `output`. The instruction text on the viewer is "If you are a doctor, please answer the medical questions based on the patient's description." Language on the model card: English. Card says: "Real patient questions from HealthCareMagic platform" and "Professional doctor responses." ChatDoctor paper says: "we chose to gather authentic patient-doctor conversations, collecting around 100k such interactions from the online medical consultation website, HealthCareMagic" and "we erased any information identifying the doctor or the patient and employed LanguageTool to rectify any grammatical errors." Provenance of the corpus: human patient and physician text from that website, then filtered and grammar-corrected. Not a synthetic generator model. The paper's own fine-tune is LLaMA, not this Gemma file. The card does not say how the 1,500 rows were chosen from the 112,165.

**(d) Base model.** Card YAML and prose: `google/gemma-2-2b-it`. Google's card for that repo says Gemma has "open weights for both pre-trained variants and instruction-tuned variants" and, on this `-it` page, "The instruction-tuned models use a chat template." The pre-trained sibling is `google/gemma-2-2b`.

**(e) Hyperparameters.** Card says: epochs 3, learning rate 2e-5, batch size 4 per device, max sequence length 1024, cosine scheduler with 10% warmup, AdamW weight decay 0.01, gradient clipping 1.0. Hardware line: "Single GPU (T4/V100/A100)". That is three GPU names, not one machine. Training time: "~30-45 minutes". No other source states these numbers.

**(f) Evaluation.** Card says: "Not validated against clinical benchmarks." It also says "4-bit quantization maintains ~95% of full precision performance," without a table for this checkpoint. No ROUGE, exam score, or held-out set is reported.

**(g) Task and language.** Card says the model was "specialized for medical question answering" and "trained on real patient-doctor conversations." The dataset rows are a patient description and a doctor reply. Task trained for: patient-doctor dialogue. Language of use: English (`en` on the card).

### Discrepancies

1. Inventory `methods` is `lora`. The card states 4-bit nf4 for training as well as LoRA, which is the 4-bit-base definition of QLoRA. Inventory does not record an objective. The card does not name one either.
2. Card says 4-bit training and bfloat16 precision. The uploaded weights are full float32 shards, and there is no `adapter_config.json`, while the Hub tag says `base_model:adapter`.
3. Card says 1,500 training samples. The named dataset has 112,165 rows. The card does not publish the subset.
4. Hardware is written as "T4/V100/A100", not a single device.

### Confidence

Medium. The card gives rank, alpha, a 1,500-row count, and hyperparameters, and no second source repeats them. The 4-bit claim and the float32 upload are not the same file format.

### Queries tried

- `sweatSmile Gemma-2-2B-MedicalQA-Assistant fine-tuning LoRA ChatDoctor`
- `"Gemma-2-2B-MedicalQA-Assistant" OR "sweatSmile" gemma medical github`
- `site:github.com sweatSmile Gemma-2-2B-MedicalQA OR "1,500 curated" ChatDoctor gemma`
- GitHub repository search API for `Gemma-2-2B-MedicalQA-Assistant` (no matching repo; `azizdeniz890/gemma-medical-qa-lora` is a different upload)
- Hugging Face dataset API for `lavita/ChatDoctor-HealthCareMagic-100k` (112,165 rows)
- ChatDoctor paper, PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC10364849/ and arXiv 2303.14070
- Base card https://huggingface.co/google/gemma-2-2b-it
- Hub file list in `2026-10-05__016.csv`

## 2. alpha-ai/Medical-Diagnosis-COT-Gemma3-270M

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/alpha-ai__Medical-Diagnosis-COT-Gemma3-270M__2026-10-05.md`. Names this repo. Organization: Alpha AI (www.alphaai.biz). README commit `6b58f63` is by Hugging Face user tushar310 (25 Aug 2025). Alpha AI's company page names founder Tushar Bhatnagar: https://alphaai.biz/alpha-ai-in-a-jiffy-1 . That page does not name this repo.
- Config, cached 2026-10-06: `revision_3_experiments/hf_inventory/cache/configs/alpha-ai__Medical-Diagnosis-COT-Gemma3-270M__2026-10-06.json`. Contains `"unsloth_fixed": true` and `"unsloth_version": "2025.8.6"`. No LoRA rank.
- Hub file list, cache `2026-10-05__009.csv`: `model.safetensors`, two GGUF files, no `adapter_config.json`. Safetensors total 268,098,176 parameters (167,828,096 BF16 and 100,270,080 F16). Hub tag `base_model:adapter:google/gemma-3-270m-it`. Created 2025-08-17.
- Dataset card: https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT . Does not name this repo. Datasets-server size API: English config 19,704 rows; all four configs sum to 90,120 rows.
- HuatuoGPT-o1 paper, arXiv 2412.18925: https://arxiv.org/pdf/2412.18925 . Describes how that dataset was built and how HuatuoGPT-o1 (Llama) was trained. Does not print `alpha-ai/Medical-Diagnosis-COT-Gemma3-270M`.
- Training script for HuatuoGPT-o1: https://github.com/FreedomIntelligence/HuatuoGPT-o1/blob/main/README.md . The SFT command uses `--model_path [meta-llama/Llama-3.1-8B-Instruct]`. It does not train this Gemma file.
- Alpha AI blog https://alphaai.biz/articles-and-blogs/f/building-on-our-clinical-reasoning-agent-what-we-learned-next returned a title and no training recipe. https://alphaai.biz/custom-ai-models says the company uses "Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and custom adapter-based architectures" as a service list. It does not name this repo or a LoRA rank.
- GitHub search for the repo name: no repository.

### Training record

**(a) Objective.** Card says: "Training: SFT with LoRA via Unsloth; assistant-only loss" and "Trainer: TRL `SFTTrainer` (supervised finetuning)." The loss is masked to assistant tokens. The HuatuoGPT-o1 paper's second stage is reinforcement learning with PPO for HuatuoGPT-o1, not for this Gemma upload. This card does not say DPO, PPO, or GRPO.

**(b) Parameter-update scope.** Card says: "Fine-tuning: Parameter-Efficient Fine-Tuning (LoRA) using Unsloth." Rank, alpha, and target modules: not stated anywhere found. A loading section is titled "Transformers (merged weights)" and calls `AutoModelForCausalLM.from_pretrained`. A second section is titled "PEFT LoRA (if this repo hosts LoRA adapters)." The repo does not contain `adapter_config.json`. It contains `model.safetensors` at the full 270M parameter count. Config records an Unsloth version. Adapter merged: the card's heading says "merged weights." The PEFT section is conditional and is not a statement that adapters are in the repo.

**(c) Training data.** Card YAML: `FreedomIntelligence/medical-o1-reasoning-SFT`. Card says the English split, columns `Question`, `Complex_CoT`, `Response`, "about 19.7k rows." Datasets-server: `en` train has 19,704 rows. All configs together have 90,120 rows, which matches the card's "Total dataset ≈ 90,120 rows across splits/languages." Card also says: "Human annotated and filtered medical diagnosis data" and "Human annotated data ~ 10k rows with similar fields." No Hub id is given for those 10,000 rows. They are not in the inventory dataset cell.

Dataset card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." Paper says: "We synthesize 20K SFT data points from the verifiable problem set using GPT-4o" and "We use GPT-4o as the verifier." The questions were reformatted from MedQA-USMLE and MedMCQA multiple-choice items into open questions with a ground-truth answer. Provenance of the public English file: synthetic reasoning and replies written by GPT-4o, checked by a GPT-4o verifier, on exam questions that started as human-written multiple choice. The paper's 20,000 count and the Hub's 19,704 English rows are the same release described at two precisions. The card's extra "about 10k" human rows are not in that file. Language the card says it trained on: English.

**(d) Base model.** Card: `google/gemma-3-270m-it`. Google's card for that repo says Gemma 3 has "open weights for both pre-trained variants and instruction-tuned variants." The `-it` id is the instruction-tuned checkpoint. The pre-trained sibling is `google/gemma-3-270m`.

**(e) Hyperparameters.** Card labels these as "Key hyperparameters (demo run that produced loss ≈ 3.3)": `max_steps=500`, "ideall go beyond 1500", optimizer `adamw_8bit`, weight decay 0.01, linear schedule, learning rate `5e-5` ("for longer runs, `2e-5` is often more stable"), `per_device_train_batch_size=8`, `gradient_accumulation_steps=1`, `warmup_steps=5`, seed `3407`. Epochs: not stated anywhere found. The T4 16 GB sentence is advice ("consider `per_device_train_batch_size=1`"), not a statement of the GPU used. Card later says loss "Further decreased to ~2.3 with parameter tuning," so the 500-step list may not be the uploaded run.

**(f) Evaluation.** Card says: "Training loss: ~3.3 at step 500 (demo run). Further decreased to ~2.3 with parameter tuning." "Format compliance: qualitatively verified to produce `<think>…</think>` followed by an answer." "No formal clinical benchmarks reported yet."

**(g) Task and language.** Card says the training target is "`<think>{Complex_CoT}</think>\n{Response}`" for a medical question. Task trained for: reasoning traces, then a final answer. Language of use: English.

### Discrepancies

1. Inventory `methods` is `lora|sft` and `datasets` is `FreedomIntelligence/medical-o1-reasoning-SFT`. Both match the card's public data and the named objective. The card also claims about 10,000 human-annotated rows with no Hub id. Inventory does not list them.
2. The hyperparameter block is labeled a demo run. A later sentence says loss fell to about 2.3 after further tuning. The card does not say which of those runs was uploaded.
3. Code samples load `alphaaico/Medical-Diagnosis-COT-Gemma3-270M`. This repository is `alpha-ai/Medical-Diagnosis-COT-Gemma3-270M`.
4. Hub tag says `base_model:adapter`. The file list is a full `model.safetensors` plus GGUF, and the card heading says "merged weights."
5. The HuatuoGPT-o1 paper trains Llama with supervised fine-tuning and then PPO. That paper does not say this 270M Gemma was trained that way.

### Confidence

Medium. The card, the Unsloth fields in `config.json`, and the English row count agree on supervised fine-tuning with LoRA on the public English reasoning file. Rank is missing, the step count is labeled a demo, and the extra human set is only on the card.

### Queries tried

- `"alpha-ai" Medical-Diagnosis-COT-Gemma3-270M Unsloth SFT training`
- `tushar310 Medical-Diagnosis-COT-Gemma3 alphaai.biz github unsloth`
- HuatuoGPT-o1 paper https://arxiv.org/pdf/2412.18925 (training section and dataset construction; does not name this repo)
- Dataset card and datasets-server size for `FreedomIntelligence/medical-o1-reasoning-SFT` (en 19,704; all configs 90,120)
- GitHub `FreedomIntelligence/HuatuoGPT-o1` README (`SFT_stage1.py` hard-codes a Llama path)
- https://alphaai.biz/custom-ai-models and the clinical-reasoning blog (no repo id, no rank)
- GitHub repository search for the model name (no hit)
- Hub file list in `2026-10-05__009.csv` and cached `config.json` (`unsloth_version` 2025.8.6)

## 3. divyanshvats2004/medical-gemma-3-270m

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/divyanshvats2004__medical-gemma-3-270m__2026-10-05.md`. Names the dataset and base model. Author line: "Divyansh Vats — github.com/vatsdivyansh".
- Hub file list, cache `2026-10-05__010.csv`: `model.safetensors` only, no `adapter_config.json`. Safetensors total 268,098,176 BF16 parameters. Hub relation `finetune` of `google/gemma-3-270m-it`. Created 2026-03-17.
- GitHub user https://github.com/vatsdivyansh : 15 public repositories. The listed names are course and automation projects. None is named `medical-gemma-3-270m`.
- GitHub search hit https://github.com/Divyansh-Purohit/The-Smart-Doctor is a different GitHub login. Its description says it adapts Gemma-3-270M-IT with LoRA. The fetched README does not name `divyanshvats2004/medical-gemma-3-270m`.
- Same ChatDoctor dataset API and paper as model 1. They do not name this repo.

### Training record

**(a) Objective.** Card says: "Framework: HuggingFace Transformers + TRL SFTTrainer." That is supervised fine-tuning. It does not say preference optimization or reinforcement learning.

**(b) Parameter-update scope.** Not stated anywhere found. The card does not say LoRA, QLoRA, or full-weight updates. Hub siblings are one BF16 `model.safetensors` with 268,098,176 parameters, the same count as the 270M Gemma, and no `adapter_config.json`. That shows a full weights file was uploaded. It does not say whether training updated every weight. Adapter merged: not stated anywhere found.

**(c) Training data.** Card YAML: `lavita/ChatDoctor-HealthCareMagic-100k`. Card says: "Dataset: ChatDoctor-HealthCareMagic (4,500 samples)." Hub row count for the named dataset: 112,165. Provenance: same HealthCareMagic patient-doctor text as in section 1. Paper says the conversations were collected from the website, identity fields removed, and grammar corrected with LanguageTool. Language: English. The card does not say how the 4,500 rows were chosen.

**(d) Base model.** Card: `google/gemma-3-270m-it`. Instruction-tuned Gemma 3 270M, as in section 2.

**(e) Hyperparameters.** Card says: "Training: 2 epochs, RTX 3050 (4.3GB VRAM)". Learning rate: not stated anywhere found. Batch size: not stated anywhere found.

**(f) Evaluation.** Card table, fine-tuned versus base: average ROUGE-1 0.1724 versus 0.2577, ROUGE-2 0.0593 versus 0.1139, ROUGE-L 0.1356 versus 0.2082, average response time 3.01 s versus 6.10 s, average response length 63.8 versus 104.8. The fine-tuned numbers are lower on every ROUGE column. The card says the lower scores "reflect focused answers not longer generic responses." No exam accuracy is reported. The card does not say how many prompts were scored.

**(g) Task and language.** Card says: "Answers medical questions in a conversational doctor-patient style learned from real doctor responses." Task trained for: patient-doctor dialogue. Language of use: English.

### Discrepancies

1. Inventory `methods` is blank. The card names `SFTTrainer`. Inventory `datasets` and the parent `google/gemma-3-270m-it` match the card.
2. Card says 4,500 samples. The named dataset has 112,165 rows.
3. https://github.com/Divyansh-Purohit/The-Smart-Doctor is a different author and does not point at this Hub repo.

### Confidence

Medium. The card names `SFTTrainer`, 4,500 rows, 2 epochs, an RTX 3050, and a ROUGE table. The author's GitHub account does not contain a script for this repo, and the card does not say whether training updated every weight.

### Queries tried

- `divyanshvats2004 medical-gemma-3-270m ChatDoctor SFTTrainer vatsdivyansh`
- `"vatsdivyansh" OR "divyanshvats2004" OR "Divyansh Vats" gemma medical 270m`
- GitHub user page https://github.com/vatsdivyansh (15 public repos; none named this model)
- GitHub repository search API (`medical-gemma-3-270m`); hit `Divyansh-Purohit/The-Smart-Doctor` is a different login
- Hugging Face dataset API for `lavita/ChatDoctor-HealthCareMagic-100k`
- ChatDoctor paper PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC10364849/
- Hub file list in `2026-10-05__010.csv`
- Google Gemma 3 270M card https://huggingface.co/google/gemma-3-270m-it (instruction-tuned family; does not describe this fine-tune)

## 4. tulas/gemma-3-270m-medical

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/tulas__gemma-3-270m-medical__2026-10-05.md`. Names this repo in the loading example.
- Hub file list, cache `2026-10-05__016.csv`: `model.safetensors` only, no `adapter_config.json`. Safetensors total 268,098,176 float32 parameters. Hub tag `base_model:adapter:google/gemma-3-270m-it` and tag `merged`. Created 2025-08-24.
- Dataset card: https://huggingface.co/datasets/ericrisco/medrescue . Datasets-server: 86,667 rows, language tag English. The dataset card does not say tulas trained on a stated subset.
- Eric Risco's training repo https://github.com/ericrisco/medical-gemma-3n trains `unsloth/gemma-3n-E4B-it`, not Gemma 3 270M, and does not name `tulas/gemma-3-270m-medical`. Its LoRA rank on that other model is 8, not 64.
- GitHub https://github.com/hashvibe007/gemma-3-270m-medical shares the model-name string. The fetched page has no README body and does not name tulas.
- GGUF copies `mradermacher/gemma-3-270m-medical-GGUF` repeat this card. They are not a second training record.
- Kaggle notebook https://www.kaggle.com/code/gpreda/fine-tune-gemma-3-270m-using-lora-for-medical-q-a and https://github.com/gabrielpreda/fine-tune-gemma3-keras-jax-medical-q-a use MedQuAD, not `ericrisco/medrescue`, and do not name this repo.

### Training record

**(a) Objective.** Not stated anywhere found. Card says: "This model is a fine-tuned version of gemma-3-270m-it using LoRA (Low-Rank Adaptation) on medical data just for testing purpose." It does not say supervised fine-tuning, preference optimization, or reinforcement learning. The dataset name and the word "fine-tuned" do not name the loss.

**(b) Parameter-update scope.** Card says: "Fine-tuning Method: LoRA (Low-Rank Adaptation)", "LoRA Rank: 64", "LoRA Alpha: 16", "Target Modules: q_proj, k_proj, v_proj, o_proj", and "Merged: Yes, LoRA adapters have been merged with the base model." It does not say 4-bit training. Hub siblings are one float32 `model.safetensors` and no `adapter_config.json`, which matches a merged upload. The Hub tag still says `base_model:adapter`.

**(c) Training data.** Card YAML: `ericrisco/medrescue`. The prose says "on medical data" and does not repeat the Hub id. Datasets-server: 86,667 rows. Dataset card says "80,000+ high-quality medical question-answer pairs" and lists 11 source files, including `medical_o1_reasoning_sft` (19,704, the GPT-4o set from section 2), `medical_o1_verifiable_problem` (40,316), `truehealth/medqa` (10,177 exam-style questions), Wikipedia medical terms, and first-aid sets. It also says about 2,000 question-answer pairs were generated with "Ollama + Gemma3N" from 14 PDFs (WHO, ICRC, and government guides). Language tag: English. The tulas card does not say that all 86,667 rows were used. Training steps are 813, and no batch size is given, so the step count does not identify a subset.

**(d) Base model.** Card YAML: `google/gemma-3-270m-it`, the instruction-tuned checkpoint. The prose says "Base Model: google/gemma-3-270m" and drops the `-it` suffix. Inventory uses the YAML id.

**(e) Hyperparameters.** Card says: "Training Steps: 813", "Learning Rate: 3e-4". Epochs: not stated anywhere found. Batch size: not stated anywhere found. Hardware: not stated anywhere found.

**(f) Evaluation.** Not stated anywhere found.

**(g) Task and language.** Not stated anywhere found as a training objective. The card says: "This model is NOT intended for medical text generation but for testing purpose only." The only prompt in the card is "Patient presents with chest pain and", which is a prefix to continue, not a question. The named dataset is question-answer text of several kinds (exam items, first aid, reasoning traces). The card does not say which of those formats was the training target. Language tag on the card: English.

### Discrepancies

1. Inventory `methods` is `lora`, `datasets` is `ericrisco/medrescue`, and the parent is `google/gemma-3-270m-it`. Those three match the YAML and the LoRA paragraph.
2. Prose base id is `google/gemma-3-270m`. YAML base id is `google/gemma-3-270m-it`.
3. Eric Risco's published Gemma-3n recipe (rank 8, alpha 8, learning rate 2e-5, 4-bit load) is a different model. It is not this card's rank 64, alpha 16, learning rate 3e-4.

### Confidence

Medium. Rank, alpha, target modules, the merge sentence, 813 steps, and the learning rate are on the card, and the file list matches a merged full checkpoint. No script names this repo, and the card does not name the loss or how many medrescue rows were used.

### Queries tried

- `tulas gemma-3-270m-medical LoRA medrescue ericrisco`
- `"tulas/gemma-3-270m-medical" OR "gemma-3-270m-medical" github OR kaggle OR blog`
- `"tulas" huggingface gemma-3-270m-medical OR site:github.com "LoRA Rank: 64" gemma medical 813`
- Dataset card and datasets-server size for `ericrisco/medrescue` (86,667 rows)
- GitHub `ericrisco/medical-gemma-3n` (Gemma 3n E4B, not this repo)
- GitHub `hashvibe007/gemma-3-270m-medical` (empty page; does not name tulas)
- GitHub `gabrielpreda/fine-tune-gemma3-keras-jax-medical-q-a` and the Kaggle twin (MedQuAD; do not name this repo)
- Hub file list in `2026-10-05__016.csv`

## 5. SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/SumanKoo7__Pharmapedia-FT-Gemma-3-1b-it__2026-10-05.md`. The body says: "This model card has been automatically generated" and "Developed by: Sumankanth." Training sections say "[More Information Needed]".
- Hub file list, cache `2026-10-05__008.csv`: `model.safetensors` only, no `adapter_config.json`. Safetensors total 1,052,068,992 float32 parameters. Hub relation `finetune` of `google/gemma-3-1b-it`. Created 2025-03-29. YAML tags include `trl` and `sft`. YAML `new_version` is `google/gemma-3-1b-it`, the same id as the base.
- Dataset card: https://huggingface.co/datasets/llamafactory/PubMedQA . Says: "The training set is composed of 10,000 examples of the PQA-U dataset and the test set is composed of 1,000 examples of the PQA-L dataset." Datasets-server: 10,000 train and 1,000 test. Does not name this model.
- PubMedQA paper, EMNLP 2019: https://aclanthology.org/D19-1259/ . Does not name this model.
- GitHub https://github.com/SumanKoo7/pharmapedia : stub page, "Contribute to sumankanthk/pharmapedia development." No training script in the fetched page. It does not print this Hub id.
- https://model.aibase.com/models/details/1945719621596483584 is a different model, "Gemma 3 1b It Medical O1 Reasoning Finetune," developed by ArindamSingh, trained on `medical-o1-reasoning-SFT`. It is not this repo. Its LoRA recipe is not evidence for Pharmapedia.
- A LinkedIn post titled Pharmapedia by Kavin sarathi S is a retrieval system over FDA labels. It is a different person and does not name this Hub repo. https://www.linkedin.com/posts/s-kavin-sarathi_ai-rag-genai-activity-7435328528050548736-sVsu

### Training record

**(a) Objective.** The YAML tags are `trl` and `sft`. The repo name contains `FT`. A tag and a name are labels, not a training paragraph. The body says the training regime is "[More Information Needed]." The tag `sft` is what the inventory recorded. No sentence on the card says supervised fine-tuning, and no script was found. Recorded objective: supervised fine-tuning, from the YAML tag only.

**(b) Parameter-update scope.** Not stated anywhere found. No rank or alpha. Hub siblings are one float32 `model.safetensors` with 1,052,068,992 parameters and no `adapter_config.json`. Hub relation is `finetune`, not `adapter`. That shows a full weights file was uploaded. It does not say whether training updated every weight. Adapter merged: not stated anywhere found.

**(c) Training data.** Card YAML: `llamafactory/PubMedQA`. The body says training data is "[More Information Needed]." LlamaFactory's card says the file is a subset of https://github.com/pubmedqa/pubmedqa , with 10,000 PQA-U training rows and 1,000 PQA-L test rows. Datasets-server matches those two counts. PubMedQA paper says: each instance has "(1) a question which is either an existing research article title or derived from one, (2) a context which is the corresponding abstract without its conclusion, (3) a long answer, which is the conclusion of the abstract." PQA-L is "1k expert-annotated" yes/no/maybe labels. PQA-U is the unlabeled pool (paper: 61.2k); this export uses 10,000 of them. The viewer rows use the conclusion sentence as `output`, not the yes/no/maybe label. Provenance: human-written PubMed titles and abstract conclusions. Not an LLM generator. Language: English. The model card does not say whether training used the 10,000-row train split, the 1,000-row test split, or both.

**(d) Base model.** Card YAML: `google/gemma-3-1b-it`. Same Gemma 3 family card as the 270M `-it` checkpoint: instruction-tuned variant, with a separate pre-trained id `google/gemma-3-1b`. The YAML `new_version` field repeats `google/gemma-3-1b-it`.

**(e) Hyperparameters.** Not stated anywhere found. Epochs, learning rate, batch size, and hardware are the template line "[More Information Needed]."

**(f) Evaluation.** YAML `metrics` lists `accuracy`. The results section is empty. No accuracy number is stated.

**(g) Task and language.** The card body does not state a task. The named dataset is biomedical research questions whose target text in this export is the abstract's conclusion sentence. Task trained for, from that file's fields: open question answering over a PubMed abstract. The original PubMedQA decision label is yes/no/maybe; this LlamaFactory export's `output` column is the conclusion sentence, not that label. Language tag: English. The repo name says Pharmapedia. The YAML dataset is PubMedQA, which is not a pharmacy-label corpus.

### Discrepancies

1. Inventory `methods` is `sft` and `datasets` is `llamafactory/PubMedQA`, taken from the YAML tags and the datasets field. The card body does not describe a training run.
2. The repo name says Pharmapedia. The only named dataset is PubMedQA.
3. YAML `new_version` is the base model id, `google/gemma-3-1b-it`.
4. The aibase Gemma-3-1B medical-o1 page is ArindamSingh's model, not this one.

### Confidence

Low. The only training statements are YAML tags `trl` and `sft` and the dataset id, on an otherwise blank auto-generated card. No paper or script names the repo.

### Queries tried

- `SumanKoo7 Pharmapedia-FT-Gemma-3-1b-it PubMedQA LlamaFactory fine-tune`
- `"Pharmapedia" Gemma OR "SumanKoo7" OR "Sumankanth" PubMedQA fine-tune`
- GitHub https://github.com/SumanKoo7/pharmapedia (stub; no training script)
- Dataset card and datasets-server size for `llamafactory/PubMedQA` (10,000 train, 1,000 test)
- PubMedQA paper https://aclanthology.org/D19-1259/ (PQA-U and PQA-L; does not name this repo)
- aibase model page 1945719621596483584 (ArindamSingh medical-o1 Gemma, a different model)
- LinkedIn Pharmapedia RAG post by a different author (FDA labels, not this Hub id)
- Hub file list in `2026-10-05__008.csv`

## Patterns in this batch

None of the five repositories is named in a paper or a training script. What is known comes from the model card, and for Pharmapedia the card body is still the blank template.

Two models, sweatSmile's 2B Gemma and Divyansh Vats's 270M Gemma, both start from an instruction-tuned Gemma and both cite ChatDoctor-HealthCareMagic. The cards say they used 1,500 and 4,500 rows of a 112,165-row set of real HealthCareMagic patient-doctor dialogues. Only the 270M card names `SFTTrainer`. Only the 2B card states LoRA, and it also states 4-bit nf4 during training. The 270M card does not say whether every weight was updated. Its ROUGE scores are lower than the base model's.

Alpha AI is the only card that states both supervised fine-tuning and LoRA, and the training target is a `<think>` reasoning trace plus an answer. The public English file has 19,704 GPT-4o traces. The card adds about 10,000 human rows that are not on the Hub. Rank is not stated, and the printed step count is labeled a demo run. The HuatuoGPT-o1 paper's reinforcement-learning stage belongs to that Llama model, not to this Gemma file.

tulas states a merged LoRA (rank 64, alpha 16, attention projections only) and 813 steps at learning rate 3e-4, and does not name the loss. The YAML dataset, medrescue, has 86,667 English rows from exam sets, Wikipedia, and about 2,000 Gemma 3n question-answer pairs. The card does not say that all of those rows were used. Pharmapedia's YAML tag is `sft` and its YAML dataset is PubMedQA (10,000 unlabeled-subset rows and 1,000 expert-labeled test rows, with the abstract conclusion as the target text). The name Pharmapedia is not that dataset, and no hyperparameter is written down.
