# Safety fine-tune literature, batch 3 of 8

Five safety models. The question is how each one was trained: the loss, which weights moved, what the targets were, and whether the model writes a chat reply or a judgment.

Hand classification checked against `docs/safety_FT_funnel/how-models-are-filtered.md`: BenefitReporter and HarmReporter are structured trees (this reading agrees). Nemotron Safety Guard v3 and GA Guard 1B are harm-category labels (this reading agrees). Configurable Hermes 3 is a chat reply whose safety is chosen by the system prompt (this reading agrees).

## Summary

| Model | Source found | Objective | Update scope | Data (name, n, provenance) | Base | Output type | Matches inventory |
| --- | --- | --- | --- | --- | --- | --- | --- |
| jl3676/BenefitReporter | paper | SFT, used to distill synthetic trees (QLoRA) | QLoRA; rank not stated; merge not stated | SafetyAnalystData; Hub 19,188 prompt–tree rows; paper 18,901 prompts and 18.5 million features; trees written by frontier models | meta-llama/Llama-3.1-8B-Instruct (instruction-tuned) | structured tree | partly |
| jl3676/HarmReporter | paper | SFT, used to distill synthetic trees (QLoRA) | QLoRA; rank not stated; merge not stated | same dataset and prompt sources as BenefitReporter; the harm-tree specialist | meta-llama/Llama-3.1-8B-Instruct (instruction-tuned) | structured tree | partly |
| nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3 | paper | not stated (LoRA fine-tune; the loss is not named) | LoRA, rank 8, alpha 32, q_proj and v_proj; adapter shipped separately; merge not stated | Nemotron-Safety-Guard-Dataset-v3; paper 386,661 in 9 languages; later dataset card about 514,617 in 12 languages; mixed human labels and synthetic text | meta-llama/Llama-3.1-8B-Instruct (instruction-tuned) | verdict | yes |
| vicgalle/Configurable-Hermes-3-Llama-3.1-8B | paper | DPO, in the form the paper calls configurable safety tuning | not stated for this checkpoint | configurable-system-prompt-multitask; 1,952 English preference rows; synthetic | NousResearch/Hermes-3-Llama-3.1-8B (instruct and chat tuned) | reply | partly |
| GeneralAnalysis/GA_Guard_1B | code | SFT (negative log likelihood on the completion) | not stated | training set not named in the training file; the card’s dataset id resolves to a 2,795-row benchmark | meta-llama/Llama-3.2-1B-Instruct (instruction-tuned) | verdict | partly |

## jl3676/BenefitReporter

### Sources

The model card is a copy of the HarmReporter card with the benefit wording swapped in. Cached file `revision_3_experiments/hf_inventory/cache/readmes/jl3676__BenefitReporter__2026-10-06.md`. Independent sources are the ICML 2025 paper, the authors’ project page, the dataset card, and the GitHub repo. The GitHub repo loads the model. It does not contain a training script. The API listing of https://github.com/jl3676/SafetyAnalyst is README, `src/`, `docs/`, `saved_params/`, and `requirements.txt`.

- Paper (camera-ready HTML): https://arxiv.org/html/2410.16665v3
- Proceedings: https://proceedings.mlr.press/v267/li25bw.html
- Author project page: https://jl3676.github.io/SafetyAnalyst/
- Dataset card: https://huggingface.co/datasets/jl3676/SafetyAnalystData
- Code (inference and aggregation, not training): https://github.com/jl3676/SafetyAnalyst

The ICML HTML does not use the strings BenefitReporter or HarmReporter. The author project page does. The Hub id `jl3676/BenefitReporter` appears on the model card.

### Training record

**(a) Objective.** Supervised fine-tuning, used as symbolic knowledge distillation. The weight update is next-token supervised fine-tuning. The paper also calls that step distillation because the targets are trees written by larger models.

Paper says: "We applied supervised fine-tuning using qlora (Dettmers et al., 2024; Lambert et al., 2024) to distill the knowledge about harms and benefits from the teacher LMs into the student LM (West et al., 2021). We trained one specialist model to generate harm trees and another for benefit trees." https://arxiv.org/html/2410.16665v3

Project page says: "which were then used to train two specialist models—one to generate harms and one to generate benefits (`HarmReporter` and `BenefitReporter`)—through symbolic knowledge distillation via supervised fine-tuning of Llama-3.1-8B-Instruct." https://jl3676.github.io/SafetyAnalyst/

Card says: "Benefit feature generation model trained on synthetic datasets from a mixture of SOTA LLMs." Cached card above. The card does not name SFT, QLoRA, or distillation.

**(b) Parameter-update scope.** QLoRA. Rank, alpha, and target modules are not stated. Whether the adapter was merged into the upload is not stated.

Paper says: "supervised fine-tuning using qlora". Same URL as above. The QLoRA citation is Dettmers et al., the 4-bit LoRA method. The paper does not give rank, alpha, or modules.

The Hub file list in `revision_3_experiments/hf_inventory/cache/cards/2026-10-06__000.csv` is seven `model-*.safetensors` shards and no `adapter_config.json`. Inventory dtype is F32. A full-weight upload does not say whether training updated every weight or a merged adapter.

**(c) Training data.** Hub id `jl3676/SafetyAnalystData`. Dataset card says: "Data Size: corresponds of 19,188 prompts and harm-benefit trees." https://huggingface.co/datasets/jl3676/SafetyAnalystData

Paper says: "The teacher LMs generated a total of 18.5 million harm-benefit features on 18,901 benign and harmful prompts." https://arxiv.org/html/2410.16665v3

Language: English. Card says: "Language(s): English."

Provenance of the trees: synthetic. Project page and paper name the generators GPT-4o, Gemini-1.5-Pro, Llama-3.1-70B-Instruct, Llama-3.1-405B-Turbo (the dataset card says Llama-3.1-405B-Instruct; the ICML text also says Llama-3.1-405B-Instruct-Turbo), and Claude-3.5-Sonnet.

Provenance of the prompts, paper says: "randomly sampled from public prompt datasets including WildJailbreak (Jiang et al., 2024), WildChat (Zhao et al., 2024), and AegisSafetyTrain (Ghosh et al., 2024)." The same section says WildJailbreak is "a large-scale synthetic prompt dataset", WildChat "consists of in-the-wild user prompts", and AegisSafetyTrain "was built on HH-RLHF harmlessness prompts."

BenefitReporter is the specialist trained to generate benefit trees. The released dataset rows contain both harm and benefit trees.

**(d) Base model.** `meta-llama/Llama-3.1-8B-Instruct`. It is the instruction-tuned model, not the pretrained checkpoint. Meta’s card says: "The Llama 3.1 instruction tuned text only models (8B, 70B, 405B) are optimized for multilingual dialogue use cases." https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct

**(e) Hyperparameters.** Epochs, learning rate, and batch size: not stated anywhere found. Paper says: "Fine-tuning was performed with a context window length of 18,000 tokens on 8 NVIDIA H100 GPUs."

**(f) Evaluation.** The system, not the tree model alone, is scored as a prompt classifier after a separate aggregation step. Project page table, average F1: SafetyAnalyst 81.2, WildGuard 71.7, Llama-Guard-3 64.6, GPT-4 81.6, on SimpSTests, HarmBench, WildGuardTest, AIR-Bench, and SORRY-Bench. https://jl3676.github.io/SafetyAnalyst/

The arXiv v1 abstract reported average F1 0.75. The camera-ready abstract reports 0.81. The card’s relative claims ("surpassing WildGuard by 3.7%, Llama-Guard-3 by 10.8%, and ShieldGemma by over 30%") are on the card, not restated as those percentages in the camera-ready abstract.

**(g) Output.** A JSON benefit tree: stakeholders, beneficial actions, beneficial effects, and the immediacy, extent, and likelihood of each effect. It does not answer the user’s request, and it does not emit safe or unsafe. Card says: "BenefitReporter is an open language model that generates a structured \"benefit tree\" for a given prompt." The harmfulness score is a separate aggregation algorithm. This agrees with the hand classification (user prompt, structured tree, judgment training).

### Discrepancies

1. arXiv v1 says "Llama-3.1-7B-Instruct" in the student-model paragraph and "Llama-3.1-8B-Instruct" in the figure caption. The camera-ready paper, the project page, and the model card say Llama-3.1-8B-Instruct. The 7B wording is treated as a draft error.
2. Prompt count: dataset card 19,188 rows; paper 18,901 prompts. Feature count in the paper is 18.5 million, which is features inside the trees, not rows.
3. Average F1 is 0.75 in the arXiv v1 abstract and 0.81 in the camera-ready paper and on the project page.
4. The teacher name for the largest Llama is Llama-3.1-405B-Turbo on the project page, Llama-3.1-405B-Instruct on the dataset card, and Llama-3.1-405B-Instruct-Turbo in the ICML data section.
5. Inventory `methods` is blank. The paper states QLoRA supervised fine-tuning. Dataset id and parent match the inventory row.

### Confidence

High. The camera-ready paper states supervised fine-tuning with QLoRA of Llama-3.1-8B-Instruct on these trees, and the author page names BenefitReporter as the benefit specialist. Rank, learning rate, epochs, and whether the adapter was merged are not in any source found.

### Queries tried

1. SafetyAnalyst Interpretable transparent steerable LLM safety moderation fine-tuning Llama BenefitReporter HarmReporter
2. jl3676 BenefitReporter SafetyAnalystData supervised fine-tuning hyperparameters
3. SafetyAnalyst qlora rank learning rate epochs github jl3676 train HarmReporter BenefitReporter
4. https://arxiv.org/html/2410.16665v1 and https://arxiv.org/html/2410.16665v3
5. https://proceedings.mlr.press/v267/li25bw.html and the ICML PDF
6. https://api.github.com/repos/jl3676/SafetyAnalyst/contents/
7. https://huggingface.co/datasets/jl3676/SafetyAnalystData
8. https://jl3676.github.io/SafetyAnalyst/

## jl3676/HarmReporter

### Sources

Same paper, project page, dataset, and GitHub repo as BenefitReporter. The HarmReporter card is the benefit card with the harm wording. Cached file `revision_3_experiments/hf_inventory/cache/readmes/jl3676__HarmReporter__2026-10-06.md`. The ICML HTML does not print the name HarmReporter. The project page does.

### Training record

**(a) Objective.** Same training procedure as BenefitReporter: supervised fine-tuning used to distill teacher trees. This checkpoint is the harm-tree specialist.

Paper says: "We trained one specialist model to generate harm trees and another for benefit trees." https://arxiv.org/html/2410.16665v3

Project page says: "one to generate harms and one to generate benefits (`HarmReporter` and `BenefitReporter`)—through symbolic knowledge distillation via supervised fine-tuning of Llama-3.1-8B-Instruct." https://jl3676.github.io/SafetyAnalyst/

Card says: "Harmful feature generation model trained on synthetic datasets from a mixture of SOTA LLMs." The card does not name the loss.

**(b) Parameter-update scope.** QLoRA, from the same sentence as BenefitReporter. Rank, alpha, target modules, and merge: not stated. Hub siblings in `2026-10-06__000.csv` are seven full safetensors shards and no `adapter_config.json`. Inventory dtype is F32.

**(c) Training data.** Same Hub dataset, `jl3676/SafetyAnalystData`, 19,188 rows on the dataset card, 18,901 prompts and 18.5 million features in the paper. English. Trees are synthetic, from the same teacher list. Prompts are the same mix of WildJailbreak (synthetic), WildChat (in-the-wild user prompts), and AegisSafetyTrain (built on HH-RLHF). HarmReporter is trained to emit the harm side of the tree. The paper says the two specialists were trained because one model’s input and output did not fit in an 18,000-token window (that sentence is in arXiv v1; the camera-ready text keeps the two-specialist setup and the 18,000-token window).

**(d) Base model.** `meta-llama/Llama-3.1-8B-Instruct`, instruction-tuned. Same Meta card quote as BenefitReporter.

**(e) Hyperparameters.** Epochs, learning rate, and batch size: not stated. Hardware: 8 NVIDIA H100 GPUs, context 18,000 tokens. Same paper sentence.

**(f) Evaluation.** Same SafetyAnalyst system scores as BenefitReporter. The published F1 numbers are for the pair plus the aggregation model, not for HarmReporter alone. Project page average F1 81.2. https://jl3676.github.io/SafetyAnalyst/

**(g) Output.** A JSON harm tree: stakeholders, harmful actions from the AIR 2024 taxonomy, harmful effects, and immediacy, extent, and likelihood. It does not refuse or answer the user, and it does not emit safe or unsafe. Card says: "HarmReporter is an open language model that generates a structured \"harm tree\" for a given prompt." This agrees with the hand classification (structured tree).

### Discrepancies

1. Same 7B-versus-8B draft line, 19,188-versus-18,901 count, 0.75-versus-0.81 F1, and teacher-name variants as BenefitReporter.
2. Inventory `methods` is blank. Dataset id and parent match.

### Confidence

High, for the same reason as BenefitReporter. The paper does not publish a separate hyperparameter table for the harm specialist.

### Queries tried

1. SafetyAnalyst Interpretable transparent steerable LLM safety moderation fine-tuning Llama BenefitReporter HarmReporter
2. jl3676/HarmReporter model card and the string HarmReporter on https://jl3676.github.io/SafetyAnalyst/
3. SafetyAnalyst qlora rank learning rate epochs github jl3676 train HarmReporter BenefitReporter
4. https://arxiv.org/html/2410.16665v1 (the "harm-trees" paragraph) and https://arxiv.org/html/2410.16665v3
5. ICML PDF text of the student-model paragraph
6. https://api.github.com/repos/jl3676/SafetyAnalyst/contents/
7. https://huggingface.co/datasets/jl3676/SafetyAnalystData
8. GitHub README load line `specialist='HarmReporter'`

## nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3

### Sources

The model card, the CultureGuard paper (arXiv and the IJCNLP 2025 paper), the adapter config in the same repo, and the dataset card. The NVIDIA NIM model card repeats the Hub card. It is not an independent training source.

- Paper: https://arxiv.org/html/2508.01710v4
- Anthology: https://aclanthology.org/2025.ijcnlp-long.144/
- Adapter config: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/lora_adapter/adapter_config.json
- Dataset card: https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3
- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/nvidia__Llama-3.1-Nemotron-Safety-Guard-8B-v3__2026-10-05.md`

The paper names `Llama-3.1-Nemotron-Safety-Guard-8B-v3`.

### Training record

**(a) Objective.** Not stated. The paper and the card say LoRA fine-tuning. They do not say supervised fine-tuning, DPO, PPO, or a reward. A search of the arXiv HTML and the Anthology PDF for "supervised", "cross-entropy", and "SFT" in the training section returned no loss name.

Paper says: "For training, we utilize Llama Cookbook recipes to PEFT tune the model. We employ LoRA tuning, using the Llama-3.1-8B-Instruct model as our base model." https://arxiv.org/html/2508.01710v4

Card says: "NVIDIA’s optimized release is LoRa-tuned on approved datasets." Cached card.

The adapter file says `"task_type": "CAUSAL_LM"` and `"peft_type": "LORA"`. That is the PEFT task type for a causal language model. It is the setting used for both supervised fine-tuning and preference training, so it is not a loss name. https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/lora_adapter/adapter_config.json

**(b) Parameter-update scope.** LoRA. Not QLoRA. No source says 4-bit training.

Paper says: "The hyperparameters for training include a rank (r) of 8 and an alpha of 32."

Card says: "Rank: 8. Alpha: 32. Targeted low rank adaptation modules: 'q_proj', 'v_proj'. The resulting LoRA adapter weights are provided separately."

Adapter config says: `"r": 8`, `"lora_alpha": 32`, `"target_modules": ["v_proj", "q_proj"]`, `"lora_dropout": 0.05`, `"base_model_name_or_path": "meta-llama/Llama-3.1-8B-Instruct"`.

Merge: not stated. The card says the adapter is provided separately. The same repo also contains four full `model-*-of-00004.safetensors` shards (`2026-10-05__002.csv`). The card’s quick start loads `AutoModelForCausalLM` from the repo and does not load a PEFT adapter. That shows the full checkpoint is what they run. It does not say the words "merged into the base weights."

**(c) Training data.** Hub id `nvidia/Nemotron-Safety-Guard-Dataset-v3`.

Paper says: "The resulting dataset, Nemotron-Safety-Guard-Dataset-v3, comprises 386,661 samples in 9 languages" and lists Arabic, German, Spanish, French, Hindi, Japanese, Thai, and Chinese plus English. https://arxiv.org/html/2508.01710v4

Dataset card says: "approximately 514,617 samples across 12 languages: English, Arabic, German, Spanish, French, Hindi, Japanese, Thai, Mandarin, Dutch, Italian, and Korean." https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3/raw/main/README.md

The dataset card’s creation date on that README is January 2026. The model card’s evaluation numbers match the paper’s 9-language model, not a stated 12-language retrain. Card says the split is "Training (90%), Testing (6%), Evaluation (4%)" and does not give the absolute count.

Provenance, paper: English samples from Nemotron-Content-Safety-Dataset-V2, culturally adapted, then translated with Google Translate; a cross-lingual safety filter uses Llama-Nemotron-Safety-Guard-V2; jailbreak prompts "curated using Mixtral-8x7B" from "human-written seeds, along with open-source crime data from Princeton BDI"; responses from "Mixtral-8x22B"; labels kept when a jury (Llama-Nemotron-Safety-Guard-V2, PolyGuard-Qwen, Llama-3.1-Nemotron-70B-Instruct, Qwen3-235B-A22B) agrees with Qwen3-235B-A22B. "We curate 10k such samples in English, which are then translated."

Card says: "English samples taken from Nemotron Content Safety Dataset V2. Samples from Nemotron Content Safety Dataset V2, translated to target languages. Synthetic samples generated from Mixtral 8x7B and Mixtral 8x22B and safety annotated using Qwen3-235B." Also: "Data Collection for Training & Testing Datasets: Hybrid: Automated, Human, Synthetic."

Dataset card fields include `prompt_label_source` values `"human"` or `"llm_jury"`, and some prompts redacted from the Kaggle Suicide Detection dataset.

**(d) Base model.** `meta-llama/Llama-3.1-8B-Instruct`, instruction-tuned. Same Meta sentence as above. Paper and card both name that checkpoint.

**(e) Hyperparameters.** Paper says: "Training is conducted for 5 epochs with a constant learning rate (LR) of 1e-5, a per-gpu batch size of 4, and distributed across 8 A100 GPUs with PyTorch FSDP enabled." Card says trained between February 2025 and July 2025, runtime NeMo 24.12, and inference tested on an H100-80GB. The H100 line is inference, not the training cluster in the paper.

**(f) Evaluation.** Card table, which matches the paper’s final row: Nemotron-Safety-Guard-Dataset-v3 85.32, PolyGuardPrompts 76.07, RTP-LX 91.49, MultiJail 95.36, XSafety 66.97, Aya Red-teaming 96.79. Paper says the metric is harmful F1, and the final model is the row "CultureGuard + JB SDG + QF". Paper test-set sizes: CultureGuard-JB 8,883 samples and CultureGuard 17,676 samples, both across 9 languages.

**(g) Output.** A JSON verdict: "User Safety" and, when a reply is present, "Response Safety", each safe or unsafe, plus "Safety Categories" when unsafe. Card says: "classifies user prompts and LLM responses as safe or unsafe. If the content is unsafe, the model additionally returns a response with a list of categories that the content violates." The example taxonomy has 23 categories (violence through immoral/unethical). The card also says the category names "are not fixed and are dependent on the categories mentioned in the instruction." This agrees with the hand classification (prompt and reply, harm-category label).

### Discrepancies

1. Sample count and language count: paper 386,661 in 9 languages; dataset README about 514,617 in 12 languages. The model-card scores match the paper’s 9-language model.
2. The model card says both "Hybrid: Automated, Human, Synthetic" and "all data was synthetically generated, and human annotators did not curate any new data." The dataset fields still allow a human label source, and the paper reuses the English Aegis / Nemotron V2 labels.
3. The loss is not named. Inventory `methods` is `lora`, which matches the stated update. Dataset id and parent match. Inventory did not record a loss, and no source states one.

### Confidence

High for the LoRA settings, the base, and the data pipeline in the paper. The objective cell stays "not stated" because the paper never names the loss.

### Queries tried

1. CultureGuard Towards Culturally-Aware Dataset Guard Model Nemotron Safety Guard LoRA training
2. Llama-3.1-Nemotron-Safety-Guard-8B-v3 q_proj LoRA merged adapter_config NeMo
3. CultureGuard "supervised" OR "cross-entropy" OR "instruction tuning" OR "SFT" Llama-3.1-Nemotron-Safety-Guard-8B-v3
4. https://arxiv.org/html/2508.01710v4
5. https://aclanthology.org/2025.ijcnlp-long.144.pdf
6. https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3/raw/main/README.md
7. https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/lora_adapter/adapter_config.json
8. https://build.nvidia.com/nvidia/llama-3_1-nemotron-safety-guard-8b-v3/modelcard

## vicgalle/Configurable-Hermes-3-Llama-3.1-8B

### Sources

The model card states the method for this checkpoint. The paper defines that method. The published script implements it for a different base model. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/vicgalle__Configurable-Hermes-3-Llama-3.1-8B__2026-10-06.md`.

- Paper: https://arxiv.org/html/2404.00495 (header: "Pre-print, work in progress.")
- Script: https://github.com/vicgalle/configurable-safety-tuning/blob/main/cst_train.py
- Dataset card: https://huggingface.co/datasets/vicgalle/configurable-system-prompt-multitask/resolve/main/README.md
- Base-model report: https://arxiv.org/abs/2408.11857

The paper’s experiments are OpenHermes-2.5-Mistral-7B and SOLAR-Instruct-10.7B. The GitHub model table includes ConfigurableHermes, Configurable-Llama-3-8B, Configurable-Hermes-2-Pro-Llama-3-8B, Configurable-Yi, ConfigurableSOLAR, and ConfigurableBeagle. It does not list Configurable-Hermes-3-Llama-3.1-8B. The script hardcodes `model_name = "teknium/OpenHermes-2.5-Mistral-7B"`.

### Training record

**(a) Objective.** DPO. The card says this checkpoint was fine-tuned with configurable safety tuning. The paper defines that method as the DPO loss on pairs whose preference is flipped when the system prompt is flipped.

Card says: "A configurable NousResearch/Hermes-3-Llama-3.1-8B fine-tuned using the approach *configurable safety tuning* (CST) from https://arxiv.org/abs/2404.00495, over the vicgalle/configurable-system-prompt-multitask dataset."

Paper says: "we propose a novel method, Configurable Safety Tuning (CST), that augments DPO using synthetic preference data" and "This resorts to using the same DPO loss function, but over an augmented dataset of tuples of the form (s0, x, y0, y1) and (s1, x, y1, y0)." https://arxiv.org/html/2404.00495

Script says: `from trl import DPOTrainer, DPOConfig` and `trainer = DPOTrainer(...)`. That script’s model line is OpenHermes-2.5-Mistral-7B, not Hermes 3. https://raw.githubusercontent.com/vicgalle/configurable-safety-tuning/main/cst_train.py

The dataset tag list includes the word `dpo`. That tag is not the evidence. The card’s CST sentence and the paper’s loss equation are the evidence.

**(b) Parameter-update scope.** Not stated for this checkpoint. The OpenHermes script uses 4-bit loading and LoRA: `load_in_4bit=True`, `LoraConfig` with `r=8 * 3` (24), `lora_alpha=16 * 3` (48), dropout 0.05, and target modules `k_proj`, `gate_proj`, `v_proj`, `up_proj`, `q_proj`, `o_proj`, `down_proj`. Those numbers are not copied onto Hermes 3, because the script names a different model and the Hermes 3 card does not say LoRA or QLoRA.

Hub siblings in `2026-10-06__000.csv` are four full safetensors shards and no `adapter_config.json`. That does not say whether training updated every weight.

**(c) Training data.** `vicgalle/configurable-system-prompt-multitask`. Dataset README: `num_examples: 1952`, `language: en`, tag `synthetic`. https://huggingface.co/datasets/vicgalle/configurable-system-prompt-multitask/resolve/main/README.md

Dataset card says the rows have two sources: "Self-critique on a safety task from Harmful Behaviours, using the SOLAR-Instruct model" with the harmless and the uncensored system prompts, and `jondurbin/truthy-dpo-v0.1` for the truthful-assistant versus role-play prompts. Fields are `system`, `prompt`, `chosen`, `rejected`, `task`. The generator of the truthy-dpo half is not stated on this dataset card. SOLAR-Instruct is named for the safety half. The paper’s self-critique section does not name a generator model in the paragraphs read; the dataset card does.

**(d) Base model.** `NousResearch/Hermes-3-Llama-3.1-8B`. It is an instruct and chat model, not a pretrained base. Hermes 3 technical report says: "Hermes 3 are highly steerable instruct and chat tuned models created by fine-tuning Llama 3.1 8B, 70B, and 405B." The same report says Hermes 3 itself was trained with "a supervised fine-tuning (SFT) phase and a direct preference optimization (DPO) phase." That SFT-then-DPO recipe is the base model’s training, not this CST run. https://arxiv.org/abs/2408.11857

**(e) Hyperparameters.** Not stated for this checkpoint. The OpenHermes script sets `per_device_train_batch_size=2`, `gradient_accumulation_steps=4`, `num_train_epochs=1`, and does not set a learning rate in the `DPOConfig` block that was read. Those values are not attributed to Hermes 3.

**(f) Evaluation.** Not stated for this checkpoint. The paper’s tables are OpenHermes-2.5-Mistral-7B and SOLAR-Instruct-10.7B. CST on OpenHermes scores S1 1.00 and S0 1.00 on the harmful-behavior control test, and the multi-task average 0.98. The card shows safe and uncensored prompts and does not report a score.

**(g) Output.** A chat reply. The system prompt selects the behavior, including a refusal-style harmless assistant, an uncensored assistant, and "a harmful assistant that generates illegal content." Card says those three prompts, plus a truthful-assistant prompt and a role-play persona. This agrees with the hand classification (chat reply, prompt-controlled refusal). The model is not only a refusal model. The same weights are prompted to answer when the system prompt asks for an uncensored or harmful reply.

### Discrepancies

1. The paper and `cst_train.py` do not name this Hub repo. The card does.
2. Inventory `methods` is blank. The dataset id and the parent match. The objective is DPO via the CST definition, which the inventory did not record.
3. Applying the script’s rank 24, alpha 48, 4-bit load, and 1 epoch to this file would be a guess. Those settings stay with OpenHermes-2.5-Mistral-7B.

### Confidence

Medium. The card says this model was fine-tuned with CST, and the paper defines CST as the DPO loss. No script or hyperparameter table names the Hermes 3 checkpoint.

### Queries tried

1. Configurable Safety Tuning of Language Models with Synthetic Preference Data Hermes-3 DPO ORPO
2. Configurable-Hermes-3-Llama-3.1-8B DPO learning rate LoRA vicgalle training script
3. site:github.com/vicgalle Configurable-Hermes-3-Llama-3.1-8B cst_train DPOTrainer
4. https://raw.githubusercontent.com/vicgalle/configurable-safety-tuning/main/cst_train.py
5. https://arxiv.org/html/2404.00495
6. https://huggingface.co/datasets/vicgalle/configurable-system-prompt-multitask/resolve/main/README.md
7. https://arxiv.org/abs/2408.11857
8. https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B

## GeneralAnalysis/GA_Guard_1B

### Sources

The training method is in a file in the model repo, `training_args.bin`. The card describes the output and the base. A family blog describes training data in general and does not name this 1B checkpoint. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/GeneralAnalysis__GA_Guard_1B__2026-10-05.md`.

- Training arguments: https://huggingface.co/GeneralAnalysis/GA_Guard_1B/resolve/main/training_args.bin
- System prompt used at training: https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/_training_system.txt
- Config: https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/config.json
- Blog (family, not this file): https://generalanalysis.com/blog/ga-guard-series
- Sibling cards that say "Training: Full finetune" are GA Guard Core and GA Guard Lite. Those sentences are not on the 1B card.

No paper turned up for this checkpoint.

### Training record

**(a) Objective.** Supervised fine-tuning. The file `training_args.bin` unpickles as `trl.trainer.sft_config.SFTConfig`. Fields in that object: `loss_type='nll'`, `completion_only_loss=True`, `dataset_text_field='text'`, `output_dir='./sft_out'`, `run_name='sft-1777948383'`. NLL is next-token loss. Completion-only loss means the loss is on the completion, not the prompt. The saved object also has `do_train=False`. The card still says the checkpoint was fine-tuned. The flag is recorded below. It is not read as "this model was not trained."

Card says: "The checkpoint was fine-tuned from `meta-llama/Llama-3.2-1B-Instruct`" and "matching the GA Guard Core public template and the training format." The card does not say SFT. The training-args file does, by its class and loss.

**(b) Parameter-update scope.** Not stated. `SFTConfig` has no LoRA rank, alpha, or target modules. The Hub file list in `2026-10-05__000.csv` is one `model.safetensors` and no `adapter_config.json`. GA Guard Core’s card says "Training: Full finetune" for a Qwen3-4B model. GA Guard Lite’s card says "Training: Full finetune" for a 0.6B model. Those sentences are not on the 1B card, so they are not used here. A missing adapter file does not say that every weight was updated.

**(c) Training data.** The training-args file does not name a dataset. The card YAML lists `GeneralAnalysis/GA_Guardrail_Benchmark`. The Hub API for that id returns `GeneralAnalysis/GA_Jailbreak_Benchmark` (checked 6 October 2026). That dataset card says it is "A curated benchmark of 2,795 synthetic jailbreak attempts" and "Accompanying guardrail releases: GA Guard Core and GA Guard Lite." It does not say it is the 1B training set. https://huggingface.co/datasets/GeneralAnalysis/GA_Jailbreak_Benchmark

Blog says, about the open guardrails as a group: "our guardrails are trained on both policy-driven synthetic data and red-team examples, hardened through stress-testing and retraining cycles." https://generalanalysis.com/blog/ga-guard-series It does not give a count, a Hub id, or a generator model for the 1B file. The blog’s "RL-trained attacker model" is the attacker that writes the jailbreak benchmark, not the guard’s training loss. "Aggressive adversarial training" in that post is attached to GA Guard Thinking, not to GA Guard 1B.

Language on the 1B card: English.

`_training_system.txt` is the guard instruction: seven policies, and "for each policy you will output exacly one special token" (spelling as in the file). That is the output format, not a dataset.

**(d) Base model.** `meta-llama/Llama-3.2-1B-Instruct`. Instruction-tuned. Meta’s card says: "The Llama 3.2 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction-tuned generative models in 1B and 3B sizes" and "Instruction tuned text only models are intended for assistant-like chat." https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

`config.json` has `vocab_size` 128270. `special_tokens_map.json` lists 14 added tokens, seven `*_violation` and seven `*_not_violation`. Inventory `parent_config_check` says `vocab_size:+14 tokens added`, which matches that pair of files.

**(e) Hyperparameters.** From `training_args.bin`: `num_train_epochs=1`, `learning_rate=3e-05`, `per_device_train_batch_size=4`, `gradient_accumulation_steps=4`, `bf16=True`, `max_length=8000`, `warmup_steps=0`, `weight_decay=0.0`, `seed=42`, `packing=False`, `eos_token='<|eot_id|>'`. Hardware: not stated.

**(f) Evaluation.** Not stated for this checkpoint. The blog’s F1 tables name GA Guard, GA Guard Thinking, and GA Guard Lite. They do not name GA Guard 1B. The 1B card has no scores.

**(g) Output.** One special token per policy, either `<policy_violation>` or `<policy_not_violation>`, for illicit activities, hate and abuse, PII and IP, prompt security (jailbreaks, prompt injection, secret exfiltration, obfuscation), sexual content, misinformation, and violence and self-harm. Card says: "classifies a piece of text against seven safety policies in a single generation." The input can be a user prompt, an agent output, or other text (`_training_system.txt`). This agrees with the hand classification (a piece of text, harm-category label).

### Discrepancies

1. The card’s dataset id `GeneralAnalysis/GA_Guardrail_Benchmark` resolves to the jailbreak benchmark, which describes itself as an evaluation set for Core and Lite. The training-args file does not name a training set. Inventory copied the YAML id into `datasets`.
2. `training_args.bin` has `do_train=False` on an otherwise SFT configuration (`loss_type=nll`, `output_dir=./sft_out`, `run_name=sft-1777948383`). The card says the checkpoint was fine-tuned.
3. Core and Lite say "Full finetune." The 1B card does not. Inventory `methods` is blank, which matches the card and does not reflect the SFTConfig file.
4. Parent matches: `meta-llama/Llama-3.2-1B-Instruct`.

### Confidence

Medium. The SFT loss, epoch, learning rate, and batch size are in the checkpoint’s training-args file. The training set and whether every weight was updated are not stated for this file.

### Queries tried

1. GeneralAnalysis GA_Guard_1B fine-tuned Llama-3.2-1B-Instruct training dataset
2. "GA Guard 1B" OR "GA_Guard_1B" fine-tune OR SFT OR LoRA OR "supervised" General Analysis
3. "GA Guard 1B" "fine-tuned" OR "full finetune" OR "Llama-3.2-1B" site:huggingface.co OR site:generalanalysis.com
4. https://huggingface.co/GeneralAnalysis/GA_Guard_1B/resolve/main/training_args.bin
5. https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/_training_system.txt
6. https://huggingface.co/GeneralAnalysis/GA_Guard_1B/raw/main/config.json and special_tokens_map.json
7. https://huggingface.co/api/datasets/GeneralAnalysis/GA_Guardrail_Benchmark
8. https://generalanalysis.com/blog/ga-guard-series
9. https://docs.generalanalysis.com/guardrails/public-guards (the fetched page was a product page and did not describe 1B training)
10. GeneralAnalysis/GA_Guard_Core card line "Training: Full finetune" (a different model)

## Patterns in this batch

Two of the five checkpoints are the same paper’s pair. BenefitReporter and HarmReporter are QLoRA supervised fine-tunes of Llama-3.1-8B-Instruct that learn to write harm trees and benefit trees distilled from GPT-4o, Gemini-1.5-Pro, Claude-3.5-Sonnet, and Llama-3.1 70B and 405B. They do not themselves say safe or unsafe. A separate aggregation model turns the trees into a score. The camera-ready paper never prints the Hub names; the author project page does. Rank, learning rate, and epochs are absent, and the GitHub repo has no training script.

Nemotron Safety Guard v3 is the only row whose inventory method tag (`lora`) matches a paper. Rank 8, alpha 32, and modules `q_proj` and `v_proj` are in the paper, the card, and `adapter_config.json`, trained 5 epochs at 1e-5 on 8 A100s. The loss is still unnamed. The repo ships both full weights and a separate adapter, and no sentence says the adapter was merged. The paper’s training set is 386,661 examples in 9 languages; a later dataset card says about 514,617 in 12 languages, while the published scores match the 9-language model.

Configurable Hermes 3 is the preference-optimization case. The card says configurable safety tuning, and the paper defines that as the DPO loss with the preference reversed under the opposite system prompt. The released script is QLoRA DPO for OpenHermes-2.5-Mistral-7B on the same 1,952-row dataset, and it does not name Hermes 3, so those ranks and the 4-bit load are not this checkpoint’s record. The model writes a chat reply, including when the system prompt asks it to be harmful.

GA Guard 1B is supervised fine-tuning in the checkpoint itself: an `SFTConfig` with next-token loss on the completion, 1 epoch, learning rate 3e-5, batch size 4. It emits fourteen label tokens for seven policies. The dataset named on the card resolves to a public benchmark, and neither the training file nor the blog names the 1B training set or says whether the fine-tune was full or LoRA. Across the batch, the inventory parents and dataset ids match the cards, and the inventory misses QLoRA, DPO, and this SFT file wherever those facts were only in a paper or in `training_args.bin`.
