# Medical fine-tune literature, batch 2

Five models. Two are dated reruns from the same Hugging Face user (Hoshino-Yumetsuki). One has a public training script (lukasdrews). Two are EpistemeAI cards that name a method and then hedge or contradict it.

Inventory row means `revision_3_experiments/hf_inventory/results/medical/2026-10-06/kept.csv`. Cached cards are under `revision_3_experiments/hf_inventory/cache/readmes/`.

| model | source found | objective | update scope | data (name, n, provenance) | base | task trained for | language | matches inventory row |
|---|---|---|---|---|---|---|---|---|
| Hoshino-Yumetsuki/PopiT-Gemma-3-12B-Medical-SFT-1213 | none | not stated (name contains SFT) | not stated; uploaded file is full BF16 | four Chinese sets listed; how many rows were used is not stated | unsloth/gemma-3-12b-it (instruction-tuned) | open question answering | zh | partly |
| Hoshino-Yumetsuki/PopiT-Gemma-3-12B-Medical-SFT-1218 | none | not stated (name contains SFT) | not stated; uploaded file is full BF16 | same four sets plus llamafactory/alpaca_zh; row count used is not stated | unsloth/gemma-3-12b-it (instruction-tuned) | open question answering | zh | partly |
| lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical | code | SFT, then GRPO (author calls the second stage RLVR) | LoRA, rank 16, alpha 16; 4-bit path is off; adapter merged before upload | PubMedQA artificial subset, 1,024 then 256 | google/gemma-4-E2B-it (instruction-tuned) | open question answering (yes/no/maybe plus a written rationale) | en | partly |
| EpistemeAI/OpenMedResearch-Gemma-4E4N | none | not stated (card says the run may include SFT, RLVR, or preference tuning) | not stated; uploaded file is full BF16 | jmhb/PaperSearchQA; train split 54,907 listed | unsloth/gemma-4-E4B-it (instruction-tuned) | open question answering | en | partly |
| EpistemeAI/Reasoning-Medical0.1-E4B-sft | none | SFT (one sentence also says the GRPO trainer) | not stated; uploaded file is full BF16 | EpistemeAI/medical-reasoning-mix-100k, 100,000 | unsloth/gemma-4-E4B-it (instruction-tuned) | reasoning traces | en | partly |

## 1. Hoshino-Yumetsuki/PopiT-Gemma-3-12B-Medical-SFT-1213

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/Hoshino-Yumetsuki__PopiT-Gemma-3-12B-Medical-SFT-1213__2026-10-05.md` (same text as https://huggingface.co/Hoshino-Yumetsuki/PopiT-Gemma-3-12B-Medical-SFT-1213).
- Hub file list in `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__005.csv`: five `model-0000N-of-00005.safetensors` shards, BF16 parameter count 12,187,325,040, no `adapter_config.json`.
- No paper, blog, or training script names this repo. The earlier PopiT-Qwen3-4B card uses the same four dataset ids and the same one-sentence training description. It does not add a method.

### Training record

(a) Objective. The repo name contains SFT. The card does not name a loss. Card says: "本模型在 unsloth/gemma-3-12b-it 的基础上进行医学微调，适用于前期或者用于网络基础病症查询及问答。" That sentence says medical fine-tuning for early or web-based symptom lookup and question answering. It does not say supervised next-token training, preference optimization, or reinforcement learning.

(b) Parameter-update scope. Not stated. The uploaded repo is a full BF16 model (12,187,325,040 parameters) with no adapter file. That does not say whether training updated every weight or a LoRA that was merged before upload. Rank, alpha, and target modules: not stated.

(c) Data. YAML lists four Hub datasets. The card does not say how many rows were kept, or the mix ratio.

| Hub id | Rows on the Hub | What the dataset page says |
|---|---:|---|
| FreedomIntelligence/HuatuoGPT-sft-data-v1 | 226,042 | README on the Hub is empty. The HuatuoGPT GitHub says this file is "The data used in the Supervised Fine-Tuning (SFT) stage of HuatuoGPT" (https://github.com/FreedomIntelligence/HuatuoGPT). The paper says: "The core recipe of HuatuoGPT is to leverage both distilled data from ChatGPT and real-world data from doctors in the supervised fine-tuning stage" (https://aclanthology.org/2023.findings-emnlp.725/). |
| ticoAg/Chinese-medical-dialogue | 799,743 | Page says it processes Chinese-medical-dialogue-data (https://huggingface.co/datasets/ticoAg/Chinese-medical-dialogue). That page excerpt does not say whether the answers were written by doctors or by a model. |
| Ronndy/medical_o1_sft_Chinese | 21,057 | No dataset card (https://huggingface.co/datasets/Ronndy/medical_o1_sft_Chinese). Provenance is not stated there. The file name matches `medical_o1_sft_Chinese.json` on FreedomIntelligence/medical-o1-reasoning-SFT. That other card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier" (https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT). Nothing checked here proves the Ronndy files are that file. |
| FreedomIntelligence/Huatuo26M-Lite | 177,703 | Card says: "Huatuo26M-Lite is a refined and optimized dataset based on the Huatuo26M dataset, which has undergone multiple purification processes and rewrites" (https://huggingface.co/datasets/FreedomIntelligence/Huatuo26M-Lite). The rewrite model is not named. |

Language on the model card: `zh`.

(d) Base. Card YAML: `unsloth/gemma-3-12b-it`. Google's card for the underlying checkpoint says Gemma 3 has "open weights for both pre-trained variants and instruction-tuned variants" and, for the `-it` weights, "With instruction-tuned models, you need to use chat templates" (https://huggingface.co/google/gemma-3-12b-it). The base is instruction-tuned.

(e) Epochs, learning rate, batch size, hardware: not stated anywhere found.

(f) Evaluation. Card says CMB, evaluated 2025-12-14, 11,200 questions, overall accuracy 49.84%. It also says some subjects rose relative to "上一代模型" (the previous model) and the rest did not. It does not name that previous model. Subject lines on the card include 医学免疫学 30/39 (76.92%) and 内科护理学 29/41 (70.73%).

(g) Task and language. The stated use is symptom lookup and question answering, in Chinese. The listed data also include doctor-patient dialogue and, if the Ronndy set is the HuatuoGPT-o1 Chinese file, reasoning traces. CMB, the reported benchmark, is a Chinese medical exam. The card does not say the model was trained on CMB items.

### What this run is

Repo created 2025-12-13 (Hub metadata). It is a fine-tune of `unsloth/gemma-3-12b-it`, not of another PopiT checkpoint.

### Discrepancies

1. Inventory `methods` is `sft`. The detector quote is the dataset id `HuatuoGPT-sft-data-v1` inside the card. The card never says the training loss was supervised fine-tuning. The repo name contains SFT. That is a name, not a training statement.
2. Inventory datasets and the base id match the card.

### Confidence

Low. The only source for this checkpoint is its model card, and the card does not state the loss, the number of examples, or which weights were updated.

### Queries tried

1. `Hoshino-Yumetsuki PopiT-Gemma-3-12B-Medical-SFT-1213 fine-tune`
2. `PopiT Gemma medical SFT 1218 alpaca_zh Hoshino-Yumetsuki`
3. `Hoshino-Yumetsuki PopiT 医学微调 LoRA HuatuoGPT site:github.com`
4. `"PopiT-Gemma" OR "PopiT Gemma" medical fine-tune 混合数据`
5. `site:huggingface.co Hoshino-Yumetsuki PopiT-Qwen3-4B-Medical-SFT training`
6. `Huatuo26M-Lite dataset rows llamafactory alpaca_zh ticoAg Chinese-medical-dialogue`
7. `Ronndy medical_o1_sft_Chinese GPT-4o HuatuoGPT-sft-data-v1 ChatGPT rows`
8. `HuatuoGPT paper ChatGPT real doctor dialogues SFT dataset`
9. `google gemma-3-12b-it instruction-tuned model card`

## 2. Hoshino-Yumetsuki/PopiT-Gemma-3-12B-Medical-SFT-1218

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/Hoshino-Yumetsuki__PopiT-Gemma-3-12B-Medical-SFT-1218__2026-10-05.md`.
- Same full-weight layout as 1213: five BF16 shards, 12,187,325,040 parameters, no adapter file (`2026-10-05__005.csv`).
- No paper or training script names this repo.

### What changed from 1213

Both cards name the same base, `unsloth/gemma-3-12b-it`. The 1218 Hub parent is that base, not the 1213 repo. Nothing states that 1218 continued training from the 1213 weights. Repo created 2025-12-17.

The 1218 card adds one dataset and states why:

Card says: "PopiT-Gemma-3-12B-Medical-SFT-1218 旨在解决上一代医疗微调模型 PopiT-Gemma-3-12B-Medical-SFT-1213 在医疗问答中缺乏专业性以及纯医疗模型逻辑坍塌问题。通过引入混合数据策略，在保持高水平临床问答能力的同时，修复了对非医疗问题（如政治、逻辑推理）的过度拟合现象。"

So the author says 1218 was meant to fix two problems in 1213: medical answers that were not professional enough, and a pure-medical model whose answers collapsed on non-medical questions. The fix they describe is a mixed-data strategy. The only dataset id present on 1218 and absent on 1213 is `llamafactory/alpaca_zh`.

`llamafactory/alpaca_zh` has 51,155 rows. Its card says: "Removed some examples with empty output." It does not name a generator model (https://huggingface.co/datasets/llamafactory/alpaca_zh).

The other four dataset ids are unchanged. Mix ratios, epoch counts, and whether 1218 was trained from scratch on the union are not stated.

CMB on the same 11,200 questions moved from 49.84% (1213, evaluated 2025-12-14) to 42.00% (1218, evaluated 2025-12-18). The 1218 card says the average is pulled down by traditional Chinese medicine and politics, and that the western-medicine part is above 50%. The category table on that card is: nursing exams 799/1600 (49.94%), medical-technology exams 546/1200 (45.50%), physician exams 880/2000 (44.00%), professional-knowledge exams 672/1600 (42.00%), pharmacist exams 1301/3200 (40.66%), medical graduate exams 506/1600 (31.62%). 考研政治 is 101/400 (25.25%). 中医综合 is 86/400 (21.50%).

### Training record

(a) Objective. Same as 1213. Name contains SFT. Card says medical fine-tuning and a mixed-data strategy. No loss is named.

(b) Parameter-update scope. Not stated. Uploaded weights are full BF16, no adapter file.

(c) Data. The four sets in section 1, plus `llamafactory/alpaca_zh` (51,155 rows; generator not stated). How many rows of each set entered training: not stated. Language: `zh`.

(d) Base. `unsloth/gemma-3-12b-it`, instruction-tuned, same citation as section 1. The card also says Gemma 3 is an English-dominant base and lacks local Chinese knowledge such as traditional-medicine classics and Chinese politics.

(e) Not stated.

(f) CMB, 2025-12-18, 11,200 questions, 42.00%, with the category table above.

(g) Stated use is still symptom lookup and question answering, in Chinese. The added `alpaca_zh` set is general Chinese instructions, which matches the card's claim that non-medical questions were mixed in. It is not a statement that the medical task changed.

### Discrepancies

1. Inventory `methods` is `sft`, from the same dataset-id substring as 1213. The card does not state the loss.
2. Inventory datasets match the card, including `llamafactory/alpaca_zh`. Base id matches.

### Confidence

Low for the optimizer and the update scope. Medium for the data change: the card names 1213, states the mixed-data reason, and the YAML adds `llamafactory/alpaca_zh`.

### Queries tried

Same nine queries as section 1. The 1218 card and the `alpaca_zh` dataset page are the pages that separate the two runs.

## 3. lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical

### Sources

- Card: `revision_3_experiments/hf_inventory/cache/readmes/lukasdrews__Gemma-4-E2B-IT-SFT-RLVR-Medical__2026-10-05.md`. Card says: "Gemma-4-E2B-it fine-tuned on PubMedQA using SFT and RLVR."
- Training repo, which the card links: https://github.com/LukasDrews97/Gemma-4-IT-SFT-RLVR-Medical
- Scripts read: `config.py`, `QLORA_SFT.py`, `GRPO_RLVR.py`, `deployment.py`, `hf_datasets/pubmedqa_dataset.py`, `evaluate.py`, `README.md`.
- Hub API https://huggingface.co/api/models/lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical : five safetensor shards, BF16 5,506,950,723 parameters, no adapter file.

Both stages are in the repo. This Hugging Face repo is the checkpoint after both stages, not the SFT-only export.

### Training record

(a) Objective, in training order.

1. Supervised fine-tuning. `QLORA_SFT.py` builds `trl.SFTTrainer` with `completion_only_loss=True`. The assistant target in `pubmedqa_dataset.py` is the abstract's long answer plus `Final Decision: {yes/no/maybe}`.
2. GRPO on that same adapter. `GRPO_RLVR.py` loads the SFT adapter with `PeftModel.from_pretrained(..., is_trainable=True)` and trains `trl.GRPOTrainer`. The author calls this stage RLVR. README command order is `uv run QLORA_SFT.py && uv run GRPO_RLVR.py`.

The reward in `accuracy_reward` is not only a checkable label. It adds 1.0 if the parsed decision equals the target, adds or subtracts 0.5 if the text contains "thinking" or "reasoning", adds up to 0.4 for a fixed list of English reasoning words, adds `len(pred_text) / 5000`, subtracts 1.0 if the text is longer than 2,500 characters, and subtracts 0.8 if it is shorter than 150 characters.

The script file is named `QLORA_SFT.py`. `config.py` sets `USE_QLORA: bool = False`. With that flag off, the 4-bit `BitsAndBytesConfig` branch does not run. The checked-in config is bf16 LoRA, then GRPO.

(b) Parameter-update scope. LoRA. `QLORA_SFT.py` says `LoraConfig(lora_alpha=16, lora_dropout=0.05, r=16, bias="none", target_modules="all-linear", modules_to_save=["lm_head", "embed_tokens"])`. GRPO keeps training that adapter. `deployment.py` function `merge_and_export` calls `merge_and_unload()` and saves a full model. The SFT+RLVR export path is `./finetuned_models/E2B/gemma-4-E2B-it-sft-rlvr-medical`. The Hub repo has full BF16 shards and no adapter file, which matches that merged export. There is a separate SFT-only export path. The card's benchmark row is labeled "Gemma-4-E2B-it + SFT + RLVR", so the uploaded model is the merged model after both stages.

(c) Data. Card YAML: `qiaojin/PubMedQA`. Code loads `load_dataset("pubmed_qa", "pqa_artificial", split="train")` for training and `load_dataset("pubmed_qa", "pqa_labeled", split="train")` for the test set. `config.py`: `N_SFT_SAMPLES = 1024`, `N_RLVR_SAMPLES = 256`, `N_TEST_SAMPLES = 1000`. The artificial train set is shuffled with seed 123, split in half, and the first 1,024 of one half are the SFT rows. The first 256 of the other half are the RLVR rows.

PubMedQA paper: "PubMedQA has 1k expert-annotated, 61.2k unlabeled and 211.3k artificially generated QA instances." Each instance has a question from an article title, a context that is the abstract without its conclusion, a long answer that is the conclusion, and a yes/no/maybe label (https://aclanthology.org/D19-1259/). The artificial subset's questions and yes/no labels are generated by a rule, not by a language model. The long answer is the human-written conclusion of the abstract. Language: English.

(d) Base. `config.py`: `MODEL_ID = "google/gemma-4-E2B-it"`. Google's card: "This release includes open-weights models in both pre-trained and instruction-tuned variants" (https://huggingface.co/google/gemma-4-E2B-it). The `-it` checkpoint is the instruction-tuned one.

(e) SFT: `num_train_epochs=3`, `learning_rate=5e-5`, `per_device_train_batch_size=8`, `gradient_accumulation_steps=1`, `lr_scheduler_type="constant"`, `max_length=2048`, bf16. GRPO: `learning_rate=1e-6`, `lr_scheduler_type="cosine"`, `warmup_ratio=0.1`, `temperature=0.8`, `beta=0.005`, `num_generations=8`, `generation_batch_size=8`, `per_device_train_batch_size=1`, `gradient_accumulation_steps=16`, `max_completion_length=768`. GRPO epoch count: not set in the script. Hardware: not stated.

(f) Card table, also in the GitHub README: base PubMedQA 58.10% and MedQA-USMLE 29.54%; SFT+RLVR 73.10% and 43.05%. Quantized GGUF rows are also on the card (Q8_0 72.40% / 43.00%, down to Q4_K_M 71.80% / 38.88%). `evaluate.py` scores accuracy on the parsed yes/no/maybe decision. For PubMedQA the test loader is the labeled 1,000 (`pqa_labeled`, `N_TEST_SAMPLES=1000`), so the "in-domain" number is the expert-labeled set, while training used the artificial subset. The script also scores MedMCQA. Those MedMCQA numbers are not on the model card.

(g) The trained behavior is: read an abstract context, write a rationale, and end with `Final Decision: [yes/no/maybe]`. That is open biomedical question answering with a required rationale. MedQA-USMLE is an evaluation transfer task, not a training set. Language of the training text: English.

### Discrepancies

1. Inventory `methods` is `sft` only. The card says "using SFT and RLVR", and the script runs SFT and then `GRPOTrainer`.
2. Inventory dataset `qiaojin/PubMedQA` matches the card. The script's training rows are 1,024 plus 256 from `pqa_artificial`, not the full dataset.
3. The script name says QLoRA. `USE_QLORA` is `False`, so the checked-in run is LoRA in bf16.
4. The reward is only partly a verifiable yes/no/maybe match. Length and keyword terms are extra.

### Confidence

High. The card, the README, and the scripts name this repo, and the Hub file list matches the merged SFT-then-RLVR export path.

### Queries tried

1. `LukasDrews97 Gemma-4-IT-SFT-RLVR-Medical github training`
2. `LukasDrews97 QLORA_SFT.py PubMedQA GRPO reward`
3. GitHub contents API and raw files `config.py`, `QLORA_SFT.py`, `GRPO_RLVR.py`, `deployment.py`, `pubmedqa_dataset.py`, `evaluate.py`, `README.md`
4. `pubmed_qa pqa_artificial 211269 artificially generated conclusion PubMedQA`
5. PubMedQA paper PDF https://aclanthology.org/D19-1259.pdf
6. `google gemma-4-E2B-it instruction-tuned`
7. Hub model API for the uploaded file list

## 4. EpistemeAI/OpenMedResearch-Gemma-4E4N

### Sources

- Card: `revision_3_experiments/hf_inventory/cache/readmes/EpistemeAI__OpenMedResearch-Gemma-4E4N__2026-10-05.md`.
- Dataset card: https://huggingface.co/datasets/jmhb/PaperSearchQA
- Paper cited on the card, which is the dataset paper, not a report of this checkpoint: https://aclanthology.org/2026.eacl-long.88.pdf
- No GitHub repo turned up that trains this model id. Search `github.com AIEpisteme OpenMedResearch OR Reasoning-Medical Gemma` returned the Hugging Face pages only.
- Hub files: one `model.safetensors`, BF16 7,996,156,490 parameters, no adapter file.

### Training record

(a) Objective. Not stated as a fact about this run. The card says "The model may include one or more of the following training stages" and then lists supervised fine-tuning, "Scientific QA Optimization", retrieval-augmented reasoning, "Search-Agent or RLVR Training", optional preference tuning, and checkpoint selection. "May" covers all six. The only unconditional lines are "fine-tuned from `google/gemma-4-E4B` using the `jmhb/PaperSearchQA` dataset", "This model fine-tunes with JMHB's PaperSearchQA database", and the Unsloth footer "trained 2x faster with Unsloth and Huggingface's TRL library." Unsloth prints that footer for more than one TRL trainer. It does not name SFT versus GRPO.

The PaperSearchQA paper does train models with RLVR (GRPO, Search-R1, Qwen 3B and 7B, eight A100 80GB GPUs, 150 steps). Those runs are not this Gemma 4 E4B checkpoint. Their hyperparameters are not evidence for this repo.

(b) Parameter-update scope. Not stated. The upload is one full BF16 file (7,996,156,490 parameters) and no adapter file. The 8-bit GGUF card's Ollama note says "the finetuned bf16 merged model". That sentence is the Unsloth GGUF export template. It does not give a LoRA rank. Rank, alpha, target modules: not stated.

(c) Data. `jmhb/PaperSearchQA`. Dataset card: training set 54,907 question-answer pairs, test set 5,000, "60,000 question-answer pairs generated from PubMed abstracts". Construction: "Used GPT-4.1 to generate 3 questions per sampled abstract" and "LLM Models Used: GPT-4.1 (via OpenRouter) for all generation steps." The model card repeats the 54,907 / 5,000 / 59,907 counts. It does not say whether the 5,000 test rows were in the training mix. Language: English. The questions and synonym lists are synthetic (GPT-4.1). The source text is PubMed abstracts.

(d) Base. YAML and the Unsloth footer: `unsloth/gemma-4-E4B-it`. The prose also says `google/gemma-4-E4B` without `-it`. The Hub `base_model` tag is `unsloth/gemma-4-E4B-it`. Gemma 4's release "includes open-weights models in both pre-trained and instruction-tuned variants" (https://huggingface.co/google/gemma-4-E2B-it, same family card text). The `-it` id is the instruction-tuned checkpoint.

(e) Not stated.

(f) No scores. The card lists evaluation categories that "should" be run (PaperSearchQA test split, retrieval, exact match, citation checks, medical safety). It does not report a number.

(g) Stated task: biomedical factoid question answering and reasoning over scientific literature, in English. The card says it is not for clinical diagnosis or treatment. Retrieval-augmented use is described as an intended workflow. The card does not say a retriever was inside the training loop.

### Discrepancies

1. Inventory `methods` is `sft`, taken from the hedged list item "Supervised Fine-Tuning". The card does not say that stage was the one that ran.
2. Inventory dataset and the YAML base (`unsloth/gemma-4-E4B-it`) match. The prose base id `google/gemma-4-E4B` does not match the YAML.
3. The cited paper's RLVR recipe is for other models.

### Confidence

Low. The dataset and the instruction-tuned base are stated. The loss and the update scope are not.

### Queries tried

1. `EpistemeAI OpenMedResearch-Gemma-4E4N PaperSearchQA training`
2. `EpistemeAI OpenMedResearch unsloth TRL SFT github`
3. `github.com AIEpisteme OpenMedResearch OR Reasoning-Medical Gemma`
4. Dataset page https://huggingface.co/datasets/jmhb/PaperSearchQA
5. Paper PDF https://aclanthology.org/2026.eacl-long.88.pdf
6. `google gemma-3-12b-it instruction-tuned model card gemma-4-E2B-it` (family card for the `-it` checkpoints)
7. GGUF card https://huggingface.co/EpistemeAI/OpenMedResearch-Gemma-4E4N-8bit

## 5. EpistemeAI/Reasoning-Medical0.1-E4B-sft

### Sources

- Card: `revision_3_experiments/hf_inventory/cache/readmes/EpistemeAI__Reasoning-Medical0.1-E4B-sft__2026-10-05.md`.
- Dataset: https://huggingface.co/datasets/EpistemeAI/medical-reasoning-mix-100k and Hub API `cardData` (train split `num_examples`: 100000).
- Same GRPO sentence on a different model: https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-27B (base `unsloth/Qwen3.5-27B`).
- No training script for this repo id. Hub files: one `model.safetensors`, BF16 7,996,156,490 parameters, no adapter file.

### Training record

(a) Objective. The card says supervised fine-tuning in several places, and the GRPO trainer in one sentence.

Card says: "It was traing using superised fine tuning techniques(sft)." The next sentences say the data include chain-of-thought text, then: "Training was performed using the GRPO trainer with the Unsloth optimization method for efficient fine-tuning. The dataset is a custom mixture of medical reasoning datasets from Hugging Face, designed for SFT-style chat training."

Later the card's own table says "Training method | Supervised Fine-Tuning, SFT" and "This model was fine-tuned using supervised fine-tuning on medical reasoning data." The repo name contains `sft`.

The dataset card says the `messages` field "is structured to be directly compatible with `trl.SFTTrainer` and similar SFT libraries." It does not mention GRPO or a reward.

The GRPO sentence is reused. `EpistemeAI/Reasoning-Medical0.1-27B` uses the same sentence ("Training was performed using the GRPO trainer with the Unsloth optimization method") on a Qwen3.5-27B fine-tune, not on this Gemma checkpoint. No reward function, no GRPO config, and no second-stage dataset are stated for the E4B repo. The repeated, model-specific statements say SFT. The GRPO line is one shared sentence with no procedure behind it.

(b) Parameter-update scope. Not stated. Upload is full BF16 (7,996,156,490 parameters), no adapter file. Rank, alpha, merge: not stated. The Unsloth footer does not name LoRA versus full updates.

(c) Data. `EpistemeAI/medical-reasoning-mix-100k`, 100,000 train rows. Dataset card table of target rows:

| source | target rows |
|---|---:|
| lingshu-medical-mllm/ReasonMed | 40,000 |
| UCSC-VLAA/MedReason | 20,000 |
| FreedomIntelligence/medical-o1-reasoning-SFT | 10,000 |
| openlifescienceai/medmcqa | 10,000 |
| GBaker/MedQA-USMLE-4-options | 5,000 |
| qiaojin/PubMedQA, config `pqa_artificial` | 5,000 |
| zou-lab/MedCaseReasoning | 5,000 |
| jmhb/PaperSearchQA | 5,000 |

Those weights are the dataset author's targets. The model card says the model was fine-tuned on this mixture and on chain-of-thought text. It does not republish the table. Provenance is mixed: exam sets (MedMCQA, MedQA), PubMedQA artificial rows, and reasoning sets that their own cards describe as model-generated (medical-o1 uses GPT-4o; PaperSearchQA uses GPT-4.1). ReasonMed, MedReason, and MedCaseReasoning generators are not restated on this model card. Language: English. Fields are `prompt`, `completion`, and `messages` for chat SFT.

(d) Base. YAML, table, and footer: `unsloth/gemma-4-E4B-it`, the instruction-tuned Gemma 4 E4B checkpoint. Same family statement as section 4.

(e) Epochs, learning rate, batch size, hardware: not stated.

(f) Card table: `mmlu_pro_biology` exact match 0.75 (5-shot); `mmlu_proX_en_biology` 0.75 (5-shot); `medqa_4options` accuracy 0.760 (0-shot), compared on the card with other models (Huatuo-o1-RL-8B 0.726, MedGemma 4B 0.644). BioSafeBench: "87.5/100 mean" and "85% automatic pass rate across 40 biological-safety evaluations." The card says those safety numbers are heuristic and are not a certification.

(g) The card's stated task is step-by-step medical reasoning for education: professional medicine, genetics, college biology, and clinical knowledge, in English. The mixture also contains multiple-choice exam items (MedQA, MedMCQA). The card says the model is not for autonomous diagnosis.

### Discrepancies

1. Inventory `methods` is `grpo|sft`. Both strings are on the card. The GRPO string is one sentence, shared with the 27B card, and the dataset is built for `SFTTrainer`. No reward is stated. Recording a GRPO stage would go beyond what is specified.
2. Inventory dataset and base id match the card.

### Confidence

Medium. SFT is stated several times, and the dataset card is written for SFT chat training. The single GRPO sentence keeps the record from being clean.

### Queries tried

1. `EpistemeAI Reasoning-Medical0.1-E4B-sft GRPO medical-reasoning-mix-100k`
2. `"Training was performed using the GRPO trainer" EpistemeAI Reasoning-Medical`
3. `"Reasoning-Medical0.1-E4B-sft" unsloth lora rank OR epochs`
4. `github.com AIEpisteme OpenMedResearch OR Reasoning-Medical Gemma`
5. Dataset page and Hub API for `EpistemeAI/medical-reasoning-mix-100k`
6. `EpistemeAI/Reasoning-Medical0.1-27B` card, to compare the GRPO sentence
7. `google gemma-4-E2B-it` family card for the instruction-tuned checkpoint

## Patterns in this batch

The two PopiT Gemma repos differ by one added dataset and by the author's own account of why. 1218 adds `llamafactory/alpaca_zh` and says the mix was meant to stop a medical-only model from collapsing on politics and logical questions. Both still point at `unsloth/gemma-3-12b-it`, not at each other. On the same 11,200 CMB items the overall accuracy went from 49.84% to 42.00%. Neither card names a loss, a LoRA rank, or a row count, so the inventory label `sft` is the word inside the dataset ids and the repo names.

The lukasdrews repo is the only one here with a script for both stages in the name. SFT is `SFTTrainer` on 1,024 artificial PubMedQA rows. The second stage is `GRPOTrainer` on the same LoRA, for 256 further rows, with a reward that mixes an exact yes/no/maybe check and length and keyword bonuses. `USE_QLORA` is false, so the checked-in run is bf16 LoRA, rank 16, alpha 16, then merged. The uploaded model is that merged SFT-then-RLVR checkpoint. The inventory row kept only `sft`.

The two EpistemeAI cards both end with the Unsloth and TRL footer and both upload a full BF16 E4B file. OpenMedResearch never commits to SFT versus RLVR: every stage is under "may". The PaperSearchQA paper's GRPO run is a different model family. Reasoning-Medical0.1-E4B-sft says supervised fine-tuning in the title, the table, and the dataset card, and says "GRPO trainer" in one sentence that also appears on the group's 27B Qwen card. No reward or GRPO config is given for the E4B run.
