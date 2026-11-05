# Batch 5: how five safety models were trained

Cached cards are the newest README under `revision_3_experiments/hf_inventory/cache/readmes/`. Inventory rows are in `revision_3_experiments/hf_inventory/results/safety/archive/2026-10-06/kept.csv`. Hub file lists are in `revision_3_experiments/hf_inventory/cache/cards/2026-10-06__000.csv` (four models) and `2026-10-05__001.csv` (SafetyMP). An earlier output-type reading is in `docs/safety_FT_funnel/how-models-are-filtered.md`.

| Model | Source found | Objective | Update scope | Data (name, n, provenance) | Base | Output type | Matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| thu-coai/SeTox-Qwen2.5-3B | paper and code | supervised next-token fine-tuning (SFT) | full | SeTox: 1,595 (995 tool-use + 600 direct); Chinese; human-curated sentences plus Qwen3-Max rationales | Qwen/Qwen2.5-3B-Instruct (instruction-tuned) | verdict | yes |
| AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA | paper | supervised next-token fine-tuning (SFT) | LoRA, rank 64, alpha 128; 8-bit during training | COMPASS policy-aware SFT: 4,121 English pairs; selected model replies; two rows name gpt-5-2025-08-07 | Qwen/Qwen2.5-7B-Instruct (instruction-tuned) | reply | partly |
| HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO | paper | preference optimization (DPO) | not stated | Egida-DPO-Qwen2.5-7B-Instruct: 6,410 English triples; jailbreak prompts, safe replies from Mistral and Phi, rejected replies from this model | Qwen/Qwen2.5-7B-Instruct (instruction-tuned) | reply | yes |
| SafetyMP/corporate-site-harness-llm | code | supervised next-token fine-tuning (SFT) | QLoRA, rank 16, alpha 16; card says merged | corporate-site-harness-training-data: 3,000 train / 450 validation; English; expert-written synthetic templates | card: unsloth/Qwen2.5-7B-Instruct; script default: Qwen/Qwen2.5-7B-Instruct (instruction-tuned) | reply | partly |
| thu-coai/SeTox-Qwen2.5-7B | paper and code | supervised next-token fine-tuning (SFT) | full | SeTox: 1,595 (995 tool-use + 600 direct); Chinese; human-curated sentences plus Qwen3-Max rationales | Qwen/Qwen2.5-7B-Instruct (instruction-tuned) | verdict | yes |

## 1. thu-coai/SeTox-Qwen2.5-3B

### Sources

- Model card, cached 2026-10-06: `revision_3_experiments/hf_inventory/cache/readmes/thu-coai__SeTox-Qwen2.5-3B__2026-10-06.md`. Names this repo id.
- ACL paper, anthology id 2026.acl-long.1602, HTML of arXiv 2608.12361 read 6 Oct 2026: https://arxiv.org/html/2608.12361 and https://aclanthology.org/2026.acl-long.1602/. Title on the paper: "New Terms, New Toxicity: Consensus-based Chinese Neologism Toxicity Detection via Search-Augmented LLMs." Authors on the paper: Shiyao Cui, Qinglin Zhang, Di Wang, Yida Lu, Zhexin Zhang, Jinhua Gao, Jinglin Yang, Min He, Han Qiu, Minlie Huang. The paper names `SeTox-Qwen2.5-7B` and, in Table 4, `SetTox-Qwen2.5-3B`. It does not print `thu-coai/SeTox-Qwen2.5-3B`.
- Training configs in the code repo the paper links: https://github.com/thu-coai/Setox. README prints both Hub ids. Config: https://github.com/thu-coai/Setox/blob/main/train_code/qwen2.5-3b.yaml. Runner: https://github.com/thu-coai/Setox/blob/main/train_code/run.sh.
- Trainer log uploaded with the weights: https://huggingface.co/thu-coai/SeTox-Qwen2.5-3B/raw/main/train_results.json. Names this repo by URL.
- Dataset card: https://huggingface.co/datasets/thu-coai/SeTox. Same bibtex as the model card. It is the release package, not a second research group.
- Inference prompt: https://github.com/thu-coai/Setox/blob/main/setox/prompts.py.
- Featherless page https://featherless.ai/models/thu-coai/SeTox-Qwen2.5-3B repeats the card. It is not a second witness.

### Training record

**(a) Objective.** Supervised next-token fine-tuning. Card says: "SeTox-Qwen2.5-3B is a full-SFT model" and "Method: full supervised fine-tuning." Script says: `stage: sft` and `llamafactory-cli train`. Paper says the training loss is on "the sentence and safety label with rationale" and "The optimization is performed only on the model-generated tokens associated with tool invocation, safety labels and rationales." That is next-token training with the loss restricted to the model's own tokens. The paper does not use the words "supervised fine-tuning" in that paragraph. It does not describe DPO, ORPO, PPO, or a reward model for this training.

**(b) Parameter-update scope.** Full weights. Card says "full-SFT" and "full supervised fine-tuning." Script says: `finetuning_type: full` and `output_dir: saves/setox-qwen2.5-3b/full/sft`. No LoRA rank, alpha, or target modules are in the yaml. README says: "Training uses LLaMA-Factory full SFT." Hub siblings in `2026-10-06__000.csv`: two `model-*.safetensors` shards, `train_results.json`, `all_results.json`, and no `adapter_config.json`. Relation tag: `base_model:finetune:Qwen/Qwen2.5-3B-Instruct`. Adapter merged: no adapter.

**(c) Training data.** Hub id `thu-coai/SeTox`. Dataset card says `data/train/train_tool.json` has 995 records ("Tool-use SFT examples with search observations") and `data/train/train_normal.json` has 600 records ("Direct SFT examples"). 995 + 600 = 1,595. Paper says: "We train the model for SeTox on 1,595 samples in total. The safe subset contains 811 samples, including 300 general samples filtered from ToxiCN ... and 511 sentences containing benign neologisms. The unsafe subset contains 784 samples, comprising 484 neologism-based unsafe instances from our constructed lexicon and 300 general unsafe samples from CHSD." Language: Chinese (`language: zh` on the card and the dataset). Provenance: the sentences are filtered or written from ToxiCN, CHSD, and the authors' lexicon; the explanations are synthetic. Paper says: "we prompt Qwen3-Max to produce a natural language safety rationale." The dataset card says the tool-use file "is the exact final training snapshot" and that search snippets in it contain noise. The yaml trains on `content_tool_dataset, content_normal_dataset`, which `dataset_info.json` maps to those two files.

**(d) Base model.** Card YAML and the yaml both say `Qwen/Qwen2.5-3B-Instruct`. That id is the instruction-tuned Qwen2.5-3B checkpoint. The paper's training-config sentence names only `Qwen2.5-7B-Instruct`. The 3B base is in the released config and the card, not in that sentence.

**(e) Hyperparameters.** Card says: epochs 3, learning rate `1e-5`, "linear with warmup ratio `0.05`," context cutoff `4096`. Yaml says the same: `num_train_epochs: 3.0`, `learning_rate: 1.0e-5`, `lr_scheduler_type: linear`, `warmup_ratio: 0.05`, `cutoff_len: 4096`, plus `per_device_train_batch_size: 4` and `gradient_accumulation_steps: 2`. Trainer log says `"epoch": 3.0` and `"train_loss": 0.9365231843789419`. Hardware for the 3B run: not stated anywhere found. The paper's "4 A100 GPUs" and "batch size is 32" are in the sentence that names Qwen2.5-7B-Instruct.

**(f) Evaluation.** Card table, and the same numbers in `results/summary/qwen2.5-3b_text2_neologism.json`: neologism test set, 624 valid samples; checkpoint-120 accuracy 0.9103, unsafe F1 0.9402, unsafe recall 0.8980, safe F1 0.8205; checkpoint-150 accuracy 0.8974. Paper Table 2, as extracted from the PDF text, lists `SeTox-Qwen2.5-7B` and does not list a 3B accuracy row. Paper Table 4 lists `SetTox-Qwen2.5-3B` span match 92.63 soft / 75.32 hard. Paper human check: "92.0% and 91.5% of the evaluated cases receive faithful and consistent analyses from from SeTox-7B/3B" on 100 sentences.

**(g) What it is built to output, and what it detects.** A verdict, not a chat answer to the user's request. Paper says the model produces "rational result Y with a label and the corresponding explanation." Script says the final answer "必须以「正常内容」或「不安全内容」开头" and, if unsafe, a risk category and a short explanation. Categories in the prompt: 贬损攻击, 成人内容, 违法犯罪, 违背道德, 敏感话题. It detects toxicity in a Chinese sentence, including toxicity carried by neologisms, and it may call a web-search tool before the label. The earlier hand table marked the output "unclear from card" and the purpose "judgment training." The card really does not show the label format. The paper and `prompts.py` do. I agree it is judgment training. The output is a verdict.

### Discrepancies

1. The card's bibtex title is "SeTox: Search-enhanced Reasoning for LLM-based Toxicity Detection over Chinese Internet Buzzwords," with authors Cui, Yiming; Zhang, Qinglin; Su, Xu; Min, Changyu; Hu, Shilin; Huang, Minlie. The anthology page and the arXiv HTML at that same anthology id use the title "New Terms, New Toxicity..." and the author list Shiyao Cui, Qinglin Zhang, Di Wang, Yida Lu, Zhexin Zhang, Jinhua Gao, Jinglin Yang, Min He, Han Qiu, Minlie Huang. The dataset card and the GitHub README copy the card's bibtex.
2. Paper Table 4 spells the 3B name `SetTox-Qwen2.5-3B`.
3. The paper's training-config sentence (batch 32, 4 epochs, 4 A100s) names Qwen2.5-7B-Instruct. This checkpoint's yaml and trainer log say 3 epochs. The paper's Table 2 text does not report the card's 0.9103 accuracy.

### Confidence

High. The card, the LLaMA-Factory yaml, and the uploaded trainer log agree that this file is a full SFT run of Qwen2.5-3B-Instruct for 3 epochs at 1e-5 on the two SeTox training files. The citation block on the card does not match the paper's title or author list.

### Queries tried

- `SeTox Search-enhanced Reasoning LLM-based Toxicity Detection Chinese Internet Buzzwords ACL 2026 training`
- `thu-coai SeTox-Qwen2.5-3B full SFT github`
- `github thu-coai Setox Qwen2.5-3B fine-tune supervised`
- `SeTox-Qwen2.5-3B full OR LoRA OR 3B epoch training Config arxiv 2608.12361`
- arXiv HTML https://arxiv.org/html/2608.12361 and ACL PDF https://aclanthology.org/2026.acl-long.1602.pdf
- GitHub tree https://api.github.com/repos/thu-coai/Setox/git/trees/main?recursive=1 and raw `train_code/qwen2.5-3b.yaml`, `run.sh`, `setox/prompts.py`, `README.md`
- Dataset card https://huggingface.co/datasets/thu-coai/SeTox/raw/main/README.md
- Trainer log https://huggingface.co/thu-coai/SeTox-Qwen2.5-3B/raw/main/train_results.json
- Featherless https://featherless.ai/models/thu-coai/SeTox-Qwen2.5-3B (card copy)

## 2. AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA

### Sources

- Model card, cached 2026-10-06: `revision_3_experiments/hf_inventory/cache/readmes/AIM-Intelligence__COMPASS_Qwen2.5-7B-Instruct_LoRA__2026-10-06.md`. Names this repo id. Authors in the card bibtex: Dasol Choi, DongGeon Lee, Brigitta Jesica Kartono, Helena Berndt, Taeyoun Kwon, Joonwon Jang, Haon Park, Hwanjo Yu, Minsuk Kahng.
- Paper, arXiv 2601.01836, HTML read 6 Oct 2026: https://arxiv.org/html/2601.01836. ACL version: https://aclanthology.org/2026.acl-long.2139/. Appendix G.3 is the fine-tuning section. The paper does not print `AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA`.
- Dataset card: https://huggingface.co/datasets/AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset. Says these 4,121 pairs "were used for the Leave-One-Domain-Out (LODO) policy-aware supervised fine-tuning (SFT) experiment in the COMPASS paper."
- Dataset rows API: https://datasets-server.huggingface.co/rows?dataset=AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset&config=default&split=train&offset=0&length=2. `num_rows_total` 4121.
- Hub file list: `revision_3_experiments/hf_inventory/cache/cards/2026-10-06__000.csv`.

### Training record

**(a) Objective.** Supervised next-token fine-tuning on policy-compliant replies. Paper says: "Unlike standard safety SFT that trains on generic refusal patterns, this approach fine-tunes models on responses that achieved full compliance with domain-specific policies as evaluated by Compass." And: "The SFT dataset comprises 4,121 query-response pairs." Card tags include `sft` and `trl`. The name contains "LoRA" and "SFT"; the paper states both, so those words are not only in the name. The paper does not describe DPO, PPO, or a reward model for this run.

**(b) Parameter-update scope.** LoRA, not 4-bit QLoRA. Paper says: "We trained LoRA adapters for 3 epochs with rank r=64, α=128, peak LR 5×10⁻⁴ for Qwen2.5-7B-Instruct ... using cosine learning rate scheduling, batch size 32, and AdamW optimizer with 8-bit quantization." Card says the same rank, alpha, and "Quantization: 8-bit during training." Eight-bit plus LoRA is not the 4-bit-base definition of QLoRA. Target modules: not stated anywhere found. Card says: "This repository provides a LoRA adapter." Hub siblings are four `model-*-of-00004.safetensors` shards, safetensors total 7,615,616,512 BF16 parameters, and no `adapter_config.json`. The relation tag is `base_model:adapter:Qwen/Qwen2.5-7B-Instruct`. Whether those full shards are a merged adapter: not stated anywhere found.

**(c) Training data.** Hub id `AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset`. Paper and card: 4,121 query–response pairs. Held-out domain TelePath (telecom). Train domains: AutoViaMotors, CityGov, FinSecure, MediCarePlus, PlanMyTrip, TutoraVerse, VirtuRecruit. Card says: "Responses were selected from model outputs that achieved full policy adherence under COMPASS evaluation." Language on the card: English. The card's prose link is `AIM-Intelligence/COMPASS-Policy-aware-SFT` (no `-Dataset`). The YAML and the dataset that returns 4,121 rows use `AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset`. Rows 0 and 1 have `model` = `gpt-5-2025-08-07` and `source` = `base_AutoViaMotors_gpt-5-2025-08-07_20250928T092213Z.jsonl`. Those two rows are not a scan of all 4,121. The paper does not name the generator model.

**(d) Base model.** Card YAML: `Qwen/Qwen2.5-7B-Instruct`. Paper appendix G.3 names the same id for the rank-64 run. That id is the instruction-tuned Qwen2.5-7B checkpoint. The Hub model tree shows Qwen2.5-7B, then the Instruct checkpoint, then this repo.

**(e) Hyperparameters.** Paper and card agree: 3 epochs, rank 64, alpha 128, peak learning rate 5e-4, AdamW, batch size 32, cosine schedule, 8-bit quantization. Hardware for this LoRA run: not stated anywhere found. The paper's A100 sentence is about the evaluation setup, not this fine-tune.

**(f) Evaluation.** Card and paper Table 11, held-out TelePath, policy alignment score: base system prompt allowed base 96.67, allowed edge 85.71, denied base 24.00, denied edge 0.00; LODO SFT (LoRA) 96.67, 89.52, 71.74, 60.49.

**(g) What it is built to output, and what it detects.** A chat reply. Card says the adapter is "trained for organization-specific policy adherence." The training targets are assistant replies that comply with an allowlist and a denylist, including refusals and redirects. It does not emit a safe/unsafe label. It is built to follow organization policies: answer allowed requests and refuse denied ones. The earlier hand table says user prompt, chat reply, policy adherence. I agree.

### Discrepancies

1. The card says this repository is a LoRA adapter. The file list has no `adapter_config.json` and the weight files are a full 7.6B BF16 model. The paper says adapters were trained. It does not say they were merged into the upload.
2. The card's dataset hyperlink drops `-Dataset`. The YAML id and the live dataset id include it.
3. The paper does not print this Hub repo id. The hyperparameters match the card's Qwen row, not the Gemma row (rank 32, alpha 64, peak LR 3e-4).

### Confidence

Medium. Appendix G.3 and the card give the same LoRA SFT recipe for Qwen2.5-7B-Instruct, including the TelePath scores. The uploaded files are not a PEFT adapter directory, and no source says whether the adapter was merged.

### Queries tried

- `COMPASS Framework Evaluating Organization-Specific Policy Alignment arxiv 2601.01836 LoRA SFT`
- `"COMPASS_Qwen2.5-7B" OR "LODO SFT" OR "policy-aware" LoRA Qwen2.5 Choi 2026`
- arXiv HTML https://arxiv.org/html/2601.01836 appendix G.3
- ACL PDF https://aclanthology.org/2026.acl-long.2139.pdf
- Dataset card https://huggingface.co/datasets/AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset
- Datasets-server rows for that dataset, offset 0, length 2
- Hub file list in `2026-10-06__000.csv` and the model tree page

## 3. HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO

### Sources

- Model card, cached 2026-10-06: `revision_3_experiments/hf_inventory/cache/readmes/HPAI-BSC__Qwen2.5-7B-Instruct-Egida-DPO__2026-10-06.md`. Names this repo. Authors: Dario Garcia-Gasulla, Adrian Tormos, Anna Arias-Duart, Daniel Hinjos, Oscar Molina-Sedano, Ashwin Kumar Gururajan, Maria Eugenia Cardello.
- Paper, arXiv 2502.13603v2, HTML read 6 Oct 2026: https://arxiv.org/html/2502.13603v2 and https://arxiv.org/abs/2502.13603. The release list prints `https://huggingface.co/HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO`.
- Dataset card: https://huggingface.co/datasets/HPAI-BSC/Egida. Config `Egida-DPO-Qwen2.5-7B-Instruct` points at `Egida-DPO-Qwen2.5-7B-Instruct.json`.
- Datasets-server size: https://datasets-server.huggingface.co/size?dataset=HPAI-BSC/Egida&config=Egida-DPO-Qwen2.5-7B-Instruct. `num_rows` 6410.
- One training row: https://datasets-server.huggingface.co/rows?dataset=HPAI-BSC/Egida&config=Egida-DPO-Qwen2.5-7B-Instruct&split=train&offset=0&length=1.
- Hub file list: `revision_3_experiments/hf_inventory/cache/cards/2026-10-06__000.csv`.
- The Hugging Face paper page and the model card repeat the abstract and the card. They are not a second experiment.

### Training record

**(a) Objective.** Direct preference optimization (DPO). Paper says: "Our experimentation executes an additional DPO training using the customized triplets described in § 3.1." And: "All four safety aligned LLMs, tuned with the corresponding unsafe responses caused by the entire train set of Egida," with a footnote to this repo. Card says the model is fine-tuned on `Egida-DPO-Qwen2.5-7B-Instruct` and describes chosen and discarded answers. The repo name contains "DPO"; the paper states DPO. The paper discusses RLHF as prior work. This run is DPO, which the paper describes as training without a separate reward model.

**(b) Parameter-update scope.** Not stated anywhere found. The paper never says LoRA, QLoRA, or full-parameter updates. It says small models "were trained on 4 GPUs (1 node)" because of "the memory requirements associated with the training of LLMs." That sentence does not name which weights were updated. Hub siblings are four full BF16 shards, safetensors total 7,615,616,512 parameters, relation `finetune`, and no `adapter_config.json`. That is a full-weight upload. It does not say whether training updated every weight. Rank, alpha, target modules, and merge: not stated anywhere found.

**(c) Training data.** Hub id `HPAI-BSC/Egida`, config `Egida-DPO-Qwen2.5-7B-Instruct`, 6,410 train rows. Paper says each of the four DPO files "includes between 2,153 and 6,410 unsafe answers," and the released models used "the entire train set." The 6,410-row file is the top of that range. The viewer also shows 2.15k rows for the 72B file, which matches the bottom of the range. Columns: `prompt`, `chosen`, `rejected`, `style`, `topics`, `uuid`. Language: English. Provenance, paper: prompts are unsafe requests expanded with jailbreak templates; "Two additional attack styles are implemented using Qwen-72B-Chat" (past tense and technical report). Chosen answers: "Mistral 7B v0.3 and Phi 3 Small 8k. ... Mistral's responses are given priority over Phi's." Rejected answers are unsafe generations from Qwen-2.5-7B-Instruct itself. Topics were manually labeled by the authors. Row 0 is a DeepInception-style prompt, a cautious chosen reply, and a long rejected story that continues the jailbreak.

**(d) Base model.** Card and paper: Qwen-2.5-7B-Instruct / `Qwen/Qwen2.5-7B-Instruct`. Paper says: "The instruct version of each model is used, which includes pre-train, supervised fine-tune and model alignment (in both cases including DPO)." This extra DPO run is on top of that already instruction-tuned and already preference-tuned checkpoint.

**(e) Hyperparameters.** Paper says: "Small models were trained on 4 GPUs (1 node), at batch size 8 and lr=10^{-7}." Card says: "NVIDIA H100 64 GB GPUs," "4 GPUs (1 node)," "Time: 1.59h," "Batch Size: 8," "LR: 10−7." Paper also says the largest of these small-model runs took "1.59 hours." Epochs: not stated anywhere found. The paper's 2,000-sample remark is about where most models stop improving. It says Qwen-2.5-7B-Instruct "seems to improve linearly with data size," and the released model is the full-train-set run.

**(f) Evaluation.** Card table, attack success ratio, lower is better: Egida test 0.471 to 0.322; DELPHI 0.138 to 0.118; Alert-Base 0.544 to 0.410; Alert-Adv 0.080 to 0.045. OpenLLM Leaderboard average stays 0.488. MMLU generative ROUGE-1 0.331 to 0.296. OR-Bench refusal, keyword match: 80K 0.021 to 0.029; Hard 0.175 to 0.240. Card says the refusal ratio "is computed as keyword matching with a curated list of keywords."

**(g) What it is built to output, and what it detects.** A chat reply. The chosen targets are safe answers, often refusals, and the discarded targets are unsafe answers. It is not a classifier that prints safe/unsafe. It is built so that jailbreak prompts get a safer reply. The earlier hand table says user prompt, chat reply, more refusals. I agree.

### Discrepancies

1. Inventory `datasets` is the Hub id `HPAI-BSC/Egida`. Training used the 6,410-row config `Egida-DPO-Qwen2.5-7B-Instruct`, not the 61,830-row full file.
2. Parameter-update scope is absent from the paper and the card. The full-weight upload does not fill that gap.
3. Epochs are not stated. The card's "10−7" is the same learning rate as the paper's `10^{-7}`, written without the minus sign's exponent markup.

### Confidence

High. The paper names this Hub URL, states DPO on the model's own unsafe answers paired with safe answers, and the 6,410-row file matches the paper's upper count. The paper does not say whether every weight was updated.

### Queries tried

- `Efficient Safety Retrofitting Against Jailbreaking Egida DPO Qwen2.5-7B-Instruct arxiv 2502.13603`
- `Egida DPO Qwen2.5-7B learning rate 1e-7 full fine-tuning appendix hyperparameters Garcia-Gasulla`
- arXiv HTML https://arxiv.org/html/2502.13603v2 and ar5iv HTML https://ar5iv.labs.arxiv.org/html/2502.13603
- Dataset README https://huggingface.co/datasets/HPAI-BSC/Egida/blob/main/README.md
- Datasets-server size and row 0 for config `Egida-DPO-Qwen2.5-7B-Instruct`
- Hub viewer https://huggingface.co/datasets/HPAI-BSC/Egida/viewer
- Model card page https://huggingface.co/HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO

## 4. SafetyMP/corporate-site-harness-llm

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/SafetyMP__corporate-site-harness-llm__2026-10-05.md`. Names this repo. Author line: SafetyMP.
- File in the same repo: https://huggingface.co/SafetyMP/corporate-site-harness-llm/raw/main/export_metadata.json. It repeats the card's training table. It is not an independent source.
- Dataset card: https://huggingface.co/datasets/SafetyMP/corporate-site-harness-training-data. Names this model as the companion model. Revision `v0.3-lora-standard`.
- Factory repo: https://github.com/SafetyMP/corporate-site-harness. Script on `main`: https://github.com/SafetyMP/corporate-site-harness/blob/main/datasets/harness-llm/recipes/train_qlora_qwen25_7b.py. The card's link uses branch `cursor/readme-visual-storefront`, which returned 404 on 6 Oct 2026. The same path exists on `main`.
- Hub file list: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__001.csv`.
- Featherless https://featherless.ai/models/SafetyMP/corporate-site-harness-llm repeats the card. Not a second witness.
- No paper, thesis, or blog that describes this checkpoint was found. GitHub user https://github.com/SafetyMP lists `corporate-site-harness` among other SafetyMP repos. Those other repos do not describe this fine-tune.

### Training record

**(a) Objective.** Supervised next-token fine-tuning. Card says training was "on harness-llm SFT chat `messages`." Script says: `from trl import SFTConfig, SFTTrainer` and `trainer = SFTTrainer(...)`. Dataset card says the default files are "English chat-style supervised fine-tuning (SFT)." The dataset also has a `dpo` config (400 train pairs, 60 validation pairs) and the tags include `dpo`. The script's choices are `default` and `messages_only`. It does not load the `dpo` config. A `dpo` tag on the dataset is not evidence that this checkpoint was trained with DPO.

**(b) Parameter-update scope.** QLoRA, then a merge according to the card. Script says `load_in_4bit=True`, then `FastLanguageModel.get_peft_model` with `r=args.lora_r` default 16, `lora_alpha` default 16, `lora_dropout=0.0`, target modules `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`. Card says: "Training used Unsloth QLoRA; adapters were merged into the base before publish" and "There is no `adapter_config.json` in this repository." `export_metadata.json` says `"training_method": "unsloth_qlora_then_merge"`, `"adapter_in_repo": false`, `"lora_r": 16`, `"lora_alpha": 16`. Hub siblings are three `model-*-of-00003.safetensors` shards, 7,615,616,512 BF16 parameters, and no `adapter_config.json`. The script's last save is `model.save_pretrained` and it prints "Saved adapter to ...". The script does not call a merge.

**(c) Training data.** Hub id `SafetyMP/corporate-site-harness-training-data`, revision `v0.3-lora-standard`. Dataset card: default train 3,000 rows, validation 450 rows. Domains: policy, cli, artifacts, refusals. Language: English. Dataset card says: "Synthetic, expert-authored templates expanded in `datasets/harness-llm/scripts/` against corporate-site-harness docs and CLI contracts." And: "no personal data." Model card says: "Many rows are expert-authored expansions, not mined agent transcripts." DPO `rejected` strings, which this script does not train on, are "synthetic unsafe paraphrases."

**(d) Base model.** Card and `export_metadata.json`: `unsloth/Qwen2.5-7B-Instruct`. Card says that is "Qwen2.5-7B-Instruct." Script default: `--model` default `Qwen/Qwen2.5-7B-Instruct`. Both ids are the instruction-tuned Qwen2.5-7B checkpoint; Unsloth's id is that organization's copy. The card's reported run and the script's default do not name the same string.

**(e) Hyperparameters.** Two different lists. Card, "endorsed recipe": rank 16, alpha 16, max sequence 4096, train on assistant responses only, epochs 3. Card, "trainer log" snapshot: loss 0.9269, learning rate 6.67e-5, grad norm 0.695, hardware "Apple MacBook Pro, M5 Max, 128 GB unified memory." Script defaults: learning rate 2e-4, epochs 1.0, per-device batch size 2, gradient accumulation 8, max sequence 4096, rank 16, alpha 16. Dataset card recipe table: learning rate about 2e-4, epochs 1–2, and the note "Endorsed recipe (user-run; not executed by maintainers in the packaging pass)." The script docstring says the same: maintainers do not run the GPU training in the packaging pass.

**(f) Evaluation.** Card says: "By-domain Hub scores are not yet published." `model-index` results are an empty list. The recommended scorer is `datasets/harness-llm/scripts/score_eval.py` on the held-out validation split, with domains policy, cli, artifacts, and refusals. No numeric score for this checkpoint was found.

**(g) What it is built to output, and what it detects.** A chat reply. Card says it is for "corporate/site harness behavior: policy, `corp-harness` CLI shape, artifact/gate JSON, and hard refusals." The widgets refuse `--actor user`, invented PASS gates, nested roots, and premium-model misuse. It does not print a safe/unsafe label. The earlier hand table says narrow-domain question, chat reply, a different skill. I agree. The skill is harness procedure and hard refusals, not a general safety classifier.

### Discrepancies

1. Card and `export_metadata.json`: 3 epochs, trainer-log learning rate 6.67e-5, base `unsloth/Qwen2.5-7B-Instruct`, adapters merged, machine M5 Max. Script defaults: 1 epoch, learning rate 2e-4, base `Qwen/Qwen2.5-7B-Instruct`, save an adapter, no merge call. Dataset card: epochs 1–2 and learning rate about 2e-4.
2. The card links the script on branch `cursor/readme-visual-storefront`. That URL 404'd. The file on `main` is the one read here.
3. The dataset has a DPO split and a `dpo` tag. The model card and the script describe SFT on chat messages.
4. Inventory `methods` is `qlora|sft`, which matches the card and the script's 4-bit LoRA plus `SFTTrainer`. Inventory `parent` is `unsloth/Qwen2.5-7B-Instruct`, which matches the card and not the script default.

### Confidence

Medium. The card, the metadata file, the dataset card, and the script all say Unsloth QLoRA supervised fine-tuning on this dataset, with rank 16 and alpha 16. They do not agree on epochs, learning rate, the base-model string, or whether the published run merged the adapter. No paper was found.

### Queries tried

- `SafetyMP corporate-site-harness-llm QLoRA train_qlora_qwen25_7b`
- `site:github.com SafetyMP corporate-site-harness train_qlora_qwen25_7b`
- GitHub user https://github.com/SafetyMP and repo https://github.com/SafetyMP/corporate-site-harness
- Git tree `main?recursive=1` and raw script on `main`
- Card-linked script URL on `cursor/readme-visual-storefront` (404)
- Dataset README https://huggingface.co/datasets/SafetyMP/corporate-site-harness-training-data/raw/main/README.md
- `export_metadata.json` on the model repo
- Featherless https://featherless.ai/models/SafetyMP/corporate-site-harness-llm (card copy)

## 5. thu-coai/SeTox-Qwen2.5-7B

### Sources

Same paper, code repo, and dataset as section 1. This checkpoint's card is `revision_3_experiments/hf_inventory/cache/readmes/thu-coai__SeTox-Qwen2.5-7B__2026-10-06.md`. Its config is https://github.com/thu-coai/Setox/blob/main/train_code/qwen2.5-7b.yaml. Its trainer log is https://huggingface.co/thu-coai/SeTox-Qwen2.5-7B/raw/main/train_results.json. Metric file: https://github.com/thu-coai/Setox/blob/main/results/summary/qwen2.5-7b_text2_neologism.json. Featherless was not a separate page in the searches for this id; the 7B Hub page is gated behind the not-for-all-audiences interstitial and the cached card is the readable copy.

### Training record

**(a) Objective.** Supervised next-token fine-tuning, same loss as section 1. Card says: "full-SFT" and "Method: full supervised fine-tuning." Yaml says `stage: sft`. Paper says: "We train SeTox with Qwen2.5-7B-Instruct." The loss paragraph is the shared one: next-token loss on tool calls, safety labels, and rationales.

**(b) Parameter-update scope.** Full weights. Yaml says `finetuning_type: full` and `output_dir: saves/setox-qwen2.5-7b/full/sft`. No LoRA fields. Hub siblings: four `model-*-of-00004.safetensors` shards, no `adapter_config.json`, relation `base_model:finetune:Qwen/Qwen2.5-7B-Instruct`. Adapter merged: no adapter.

**(c) Training data.** Same two files as the 3B config: `content_tool_dataset` and `content_normal_dataset`, 995 + 600 = 1,595. Paper's 1,595-sample breakdown is written as the training set for SeTox, in the section whose training-config sentence names Qwen2.5-7B-Instruct. Language: Chinese. Provenance: same as section 1, including Qwen3-Max rationales.

**(d) Base model.** Card, yaml, and paper: `Qwen/Qwen2.5-7B-Instruct`. Instruction-tuned. Paper says the knowledge cutoff of this base, as used in a case study, is 2023-10.

**(e) Hyperparameters.** Paper says: "The batch size is 32 with the maximum length of 4096. The optimization is performed using AdamW with initial learning rate of 1e-5 for 4 epoches ... The training is run on 4 A100 GPUs. We use the last checkpoint for test." Card says epochs 4, learning rate `1e-5`, linear scheduler, warmup ratio `0.05`, context cutoff `4096`. Yaml says `num_train_epochs: 4.0`, `learning_rate: 1.0e-5`, `lr_scheduler_type: linear`, `warmup_ratio: 0.05`, `cutoff_len: 4096`, `per_device_train_batch_size: 4`, `gradient_accumulation_steps: 2`. Trainer log says `"epoch": 4.0` and `"train_loss": 0.5605946890264749`. The paper does not print the per-device batch or the warmup ratio. The yaml does not print "4 A100 GPUs" or a global batch of 32.

**(f) Evaluation.** Paper Table 2, neologism test then general test: `SeTox-Qwen2.5-7B` detection ratio 92.86, known 91.73, unknown 94.07, accuracy 94.07, unsafe F1 96.09, safe F1 87.71; general-test accuracy 93.21, unsafe F1 92.21, safe F1 93.98. The neologism accuracy, unsafe F1, and safe F1 match the card's checkpoint-200 row (0.9407, 0.9609, 0.8771). The metric JSON for checkpoint-200 also has unsafe recall 0.9286, which is the paper's detection ratio 92.86, and the known/unknown counts 319 and 305, which the paper states for the Qwen2.5-7B-Instruct split of the 624-sample test. Card also lists checkpoint-175: accuracy 0.9183. Paper human check on 100 sentences: 92.0% and 91.5% for SeTox-7B/3B, in that order.

**(g) What it is built to output, and what it detects.** Same as the 3B: a verdict that starts with 正常内容 or 不安全内容, plus a risk category and a short explanation when the sentence is unsafe. It detects toxicity in Chinese sentences, including neologisms, with optional web search. The earlier hand table left the output "unclear from card" and called the purpose judgment training. I agree on judgment training. The output is a verdict. The card does not show the label words; the paper and `prompts.py` do.

### Discrepancies

1. Same bibtex mismatch as section 1: the card cites a different title and a different author list than the paper at https://aclanthology.org/2026.acl-long.1602/.
2. Paper batch size is 32. The yaml states per-device batch 4 and gradient accumulation 2, and does not state the global batch. Paper warmup is not stated; the card and the yaml say linear warmup ratio 0.05.
3. Inventory `methods` is `sft` and `datasets` is `thu-coai/SeTox`. Both match. The inventory does not record that the paper's training sentence is this 7B run and that the 3B yaml uses 3 epochs.

### Confidence

High. The paper's training sentence names Qwen2.5-7B-Instruct, 4 epochs, learning rate 1e-5, and 1,595 examples. The yaml, the card, and the trainer log agree. Checkpoint-200's neologism scores match the paper's SeTox-Qwen2.5-7B row. The card's bibtex does not match the paper's title or authors.

### Queries tried

- `SeTox Search-enhanced Reasoning LLM-based Toxicity Detection Chinese Internet Buzzwords ACL 2026`
- `thu-coai/SeTox-Qwen2.5-7B` on the Hub and in the GitHub README
- arXiv HTML https://arxiv.org/html/2608.12361 training section and Table 2
- ACL anthology page https://aclanthology.org/2026.acl-long.1602/ and the PDF
- Raw `train_code/qwen2.5-7b.yaml` and `results/summary/qwen2.5-7b_text2_neologism.json`
- Trainer log https://huggingface.co/thu-coai/SeTox-Qwen2.5-7B/raw/main/train_results.json
- Dataset card file counts for `train_tool.json` and `train_normal.json`
- `setox/prompts.py` for the label format

## Patterns in this batch

Three of the five checkpoints are supervised next-token fine-tuning, one is DPO, and none is reinforcement learning with a reward model. The two SeTox models are full-weight SFT runs on the same 1,595 Chinese examples; the paper's detailed training sentence is the 7B run (4 epochs, batch 32, 4 A100s), and the released 3B yaml is the same recipe for 3 epochs. Both SeTox cards cite an ACL paper whose title and author list do not match the paper at that anthology id. The paper itself does describe these detectors, and they output a toxicity label plus a short explanation, which the earlier hand table had left unclear.

COMPASS is LoRA SFT (rank 64, alpha 128, 8-bit) on 4,121 English policy replies, stated in the paper's appendix with the same numbers as the card. The repository does not contain an adapter file; it contains a full 7.6B weight upload, and no source says the adapter was merged. Egida is DPO on 6,410 preference triples for this 7B model, and the paper names the Hub URL. It does not say whether training updated every weight. The model still answers in chat; the preference data pushes jailbreak prompts toward safer replies.

SafetyMP is the only QLoRA run, and it is also the only one with no paper. The card, a metadata file in the same repo, the dataset card, and the factory script agree on 4-bit LoRA supervised fine-tuning with rank 16 and alpha 16. They disagree on epochs, learning rate, the base-model string, and whether the published weights were merged. The dataset's DPO split was not what the script trains. Four of these five models emit a chat reply. Only the two SeTox models emit a verdict.
