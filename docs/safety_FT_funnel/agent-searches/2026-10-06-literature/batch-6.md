# Safety fine-tune literature, batch 6 of 8

Read on 6 October 2026. Five Hugging Face models. Facts below are quoted from a paper, a dataset card, a GitHub README, or a cached model card. A word inside a repo name is not treated as a training method.

## Summary

| Model | Source found | Objective | Update scope | Data (name, n, provenance) | Base | Output type | Matches inventory |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Irfanuruchi/qwen2.5-32b-buildeng` | code (README only; script not in the repo) | sft | qlora, adapter merged | BuildEng V8 Final, `Irfanuruchi/buildeng`, 145,117; human vs synthetic not stated | `Qwen/Qwen2.5-32B-Instruct` (instruction-tuned) | reply | yes |
| `HPAI-BSC/Qwen2.5-72B-Instruct-Egida-DPO` | paper (arXiv; Springer chapter exists) | dpo | not stated | Egida-DPO for this model, 2,153 preference triples; mixed human and machine prompts, model-written answers | `Qwen/Qwen2.5-72B-Instruct` (instruction-tuned) | reply | yes |
| `flowxai/scam-guard-qwen06b` | none | sft | lora; merge not stated | public spam/ham/phishing texts plus a synthetic layer; training n not stated; generator not named | `Qwen/Qwen3-0.6B` (post-trained) | verdict | partly |
| `cs-552-2026-Flash-McQueenS-and-TheKing/safety_model` | none | sft | lora, adapter merged | `safety_sft_data`, 3,250 English items; 2,800 rewritten from public sets, 450 LLM-written, generator not named | `Qwen/Qwen3-1.7B` (post-trained) | verdict (exam letter) | yes |
| `flowxai/scam-guard-qwen17b` | none | sft | lora; merge not stated | same data statement as the 0.6B sibling; training n not stated | `Qwen/Qwen3-1.7B` (post-trained) | verdict | partly |

The earlier hand classification in `docs/safety_FT_funnel/how-models-are-filtered.md` is agreed for all five. BuildEng and Egida-DPO write a chat reply. Both scam-guard models write a structured verdict with a short explanation. The CS-552 model writes an exam letter, which that note already separated from a safe/unsafe label. The table above uses `verdict` for the exam letter only because this batch's allowed labels are reply, verdict, or both.

## Irfanuruchi/qwen2.5-32b-buildeng

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/Irfanuruchi__qwen2.5-32b-buildeng__2026-10-06.md`. Hub metadata row in `revision_3_experiments/hf_inventory/cache/cards/2026-10-06__000.csv`.
- Same author's GitHub README, which names this repo and says the production script is not in the repository: https://github.com/IrfanUruchi/buildeng-qwen2.5-32b/blob/main/README.md. The repo contains only `README.md`.
- Dataset card: https://huggingface.co/datasets/Irfanuruchi/buildeng. Datasets-server reports 145,117 train rows: https://datasets-server.huggingface.co/size?dataset=Irfanuruchi/buildeng.
- Sibling 1.5B cards name `TRL SFTTrainer` and different LoRA settings. Those cards describe a different dataset (`Irfanuruchi/buildeng-v8-1.5b`) and are not used as numbers for this 32B run.
- No paper, thesis, or blog was found. ACL Anthology was not searched under this author because no paper is cited on the card.

### Training record

**(a) Objective.** Supervised fine-tuning, from the dataset card, not from a trainer class name on the 32B card. Dataset card says: "This dataset is intended for supervised fine-tuning of civil/structural engineering assistant models" and "It was used for BuildEng V8 model development and is intended for further 3B and 32B QLoRA training." URL: https://huggingface.co/datasets/Irfanuruchi/buildeng. The 32B card says: "The model was trained using QLoRA fine-tuning with vanilla Transformers, PEFT, and TRL." It does not say `SFTTrainer`. The GitHub README says: "The 32B model was fine-tuned from Qwen2.5-32B-Instruct using QLoRA" and "145,117 validated engineering instruction samples." It does not say SFT. The tag `qlora` is a name, not the loss.

**(b) Parameter-update scope.** QLoRA, then merged. Card says: "Training used 4-bit NF4 quantization, bf16 precision, LoRA rank 32, LoRA alpha 64" and "The model was initially trained as a LoRA adapter and later merged into the full base model. This repository contains the fully merged model weights." GitHub README says: "Training method: QLoRA", "LoRA rank: 32", "LoRA alpha: 64", and links "Main merged model" to this repo. Target modules: not stated anywhere found. The 1.5B card's rank 16 and alpha 32 are a different run.

**(c) Training data.** Name: BuildEng V8 Final. Hub id: `Irfanuruchi/buildeng`. n = 145,117 (card, README, dataset page, and datasets-server). Language: English (`language: en` on the card; viewer rows are English). Provenance: not stated. The README says the repository's work includes "dataset generation, dataset preparation, validation", but it does not say the 145,117 rows are synthetic and does not name a generator model. The 1.5B card's sentence "The training data is synthetic and simplified" refers to that smaller dataset, not this one.

**(d) Base.** `Qwen/Qwen2.5-32B-Instruct`. The id is an instruction-tuned model. Card and README both say that.

**(e) Hyperparameters.** Card says: "sequence length 4096, effective batch size 8, a cosine scheduler, and an NVIDIA A100 80GB GPU." README repeats sequence length 4096, bf16, and the A100, and does not repeat the batch size. Epochs: not stated anywhere found. Learning rate: not stated anywhere found.

**(f) Evaluation.** Not stated anywhere found. No benchmark table on the card or the README.

**(g) What it is built to output, and what it is built to detect.** A chat reply, not a verdict. Card says: "BuildEng is a domain-specialized engineering language model project focused on civil engineering, structural reasoning, construction workflows, field diagnostics, and conservative engineering-assistant behavior." It is built to answer engineering questions and to "avoid unsupported structural approval" and "respond conservatively" when structural safety may be involved. It is not described as a classifier of safe versus unsafe text. This agrees with the earlier row: narrow-domain question, chat reply, a different skill.

### Discrepancies

1. The dataset card says the data is "intended for further 3B and 32B QLoRA training." The model card and the GitHub README say this 32B training already happened. The dataset sentence reads as written before or beside the release, not as a second method.
2. Inventory methods cell is only `qlora`. That matches the update scope. It does not record supervised fine-tuning. The dataset card is the sentence that does.
3. No disagreement on base (`Qwen/Qwen2.5-32B-Instruct`) or dataset (`Irfanuruchi/buildeng`).

### Confidence

Medium. Rank, alpha, 4-bit NF4, the merge, the base, and 145,117 rows are stated twice by the author (card and README). The loss is named only as the dataset's intended use, and the author says the production script is not in the GitHub repo.

### Queries tried

1. `Irfanuruchi qwen2.5-32b-buildeng QLoRA training`
2. `Irfan Uruchi BuildEng V8 dataset civil engineering QLoRA`
3. `"qwen2.5-32b-buildeng" OR "BuildEng V8 Final" Irfan Uruchi SFT epochs`
4. `"Irfan Uruchi" OR Irfanuruchi buildeng github QLoRA`
5. `site:github.com/IrfanUruchi/buildeng-qwen2.5-32b QLoRA SFTTrainer` (no hit; the README was then fetched directly)
6. GitHub API `users/IrfanUruchi/repos` (found `buildeng-qwen2.5-32b`; contents are README only)
7. Hugging Face dataset page and datasets-server size for `Irfanuruchi/buildeng`

## HPAI-BSC/Qwen2.5-72B-Instruct-Egida-DPO

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/HPAI-BSC__Qwen2.5-72B-Instruct-Egida-DPO__2026-10-06.md`. Hub metadata in `revision_3_experiments/hf_inventory/cache/cards/2026-10-06__000.csv` (BF16, 72,706,203,648 parameters).
- Paper read in full (HTML, including appendices A–F): Garcia-Gasulla et al., "Efficient Safety Retrofitting Against Jailbreaking for LLMs", arXiv:2502.13603v2, https://arxiv.org/html/2502.13603v2 and https://arxiv.org/abs/2502.13603. A published chapter exists at https://link.springer.com/chapter/10.1007/978-3-032-02018-5_39 (Springer Nature, pp. 537–565). The Springer page returned an abstract and a fragment, not the full chapter, so the training quotes below are from the arXiv HTML.
- Dataset card and file list: https://huggingface.co/datasets/HPAI-BSC/Egida. Row count from https://datasets-server.huggingface.co/size?dataset=HPAI-BSC/Egida : config `Egida-DPO-Qwen2.5-72B-Instruct`, train split, 2,153 rows.
- No training script in a public GitHub repo was found. The paper names the library OpenRLHF 0.3.2. The OpenRLHF repository's example scripts are not a record of this run.

The model card and the dataset README repeat the paper. They are not a second independent experiment.

### Training record

**(a) Objective.** DPO. Paper says: "Our experimentation executes an additional DPO training using the customized triplets described in § 3.1." Paper says: "The model trainings have been performed with the OpenRLHF Python package, version 0.3.2." Card says: "This is a fine-tuned Qwen2.5-72B-Instruct model on the Egida-DPO-Qwen2.5-72B-Instruct dataset" and describes triplets of question, chosen answer, and discarded answer. The paper distinguishes this step from RLHF: "Unlike alternatives like Reinforcement Learning from Human Feedback (RLHF) which train an explicit reward model, DPO directly tunes the model." The suffix `-DPO` matches that statement; the statement is what is used here. DPO beta: not stated in the paper or the card. Epochs: not stated.

**(b) Parameter-update scope.** Not stated anywhere found. The paper's computational section and the appendices do not say LoRA, QLoRA, or that every weight was updated. Card hardware is "64 GPUs (16 nodes)" of "NVIDIA H100 64 GB". Paper says: "the large models were trained on 64 GPUs (16 nodes), at batch size 64 and lr=10^{-6}. Parellelization in this context is motivated solely by the memory requirements associated with the training of LLMs." That is a hardware sentence, not a statement that all weights were trained. The uploaded checkpoint is a full BF16 model (72,706,203,648 parameters in the Hub metadata). That is the file that was uploaded, not a sentence about LoRA versus full updates. Rank, alpha, target modules, and merge: not stated. There is no adapter to merge if the method was full-parameter DPO, and no source says which of those it was.

**(c) Training data.** The released model is the one trained on this model's unsafe answers over the whole Egida train split. Paper says: "All four safety aligned LLMs, tuned with the corresponding unsafe responses caused by the entire train set of Egida" and links this repo. Paper says: "Each of them includes between 2,153 and 6,410 unsafe answers." Datasets-server: 2,153 rows in `Egida-DPO-Qwen2.5-72B-Instruct`. That is the low end of the paper's range, so this checkpoint is the 2,153-row set, not one of the smaller ablation sizes in section 4.

Language: English on the card (`language: en`).

Provenance, from the paper, not guessed:

- Prompts start from 2,949 questions. Table 1 labels some sources machine-written (AdvBench, BSS, DoNotAnswer, MaliciousInstructions) and some human-written (HarmBench, SimpleSafetyTests, TDCRedTeaming). Those are expanded with jailbreak templates. Two attack styles, past tense and technical-report writing, "are implemented using Qwen 72B Chat".
- Chosen (safe) answers: "we use two models that are unrelated to the rest of the experimentation: Mistral 7B v0.3 and Phi 3 Small 8k." "Mistral's responses are given priority over Phi's." Appendix B quotes the safe system prompt and says the responses "were reviewed by the authors."
- Discarded (unsafe) answers: produced by running `Qwen2.5-72B-Instruct` on the train split and keeping unsafe answers. Card says: "Unsafe answers are selected, and paired with safe answers."

**(d) Base.** `Qwen/Qwen2.5-72B-Instruct`. Instruction-tuned. Paper says: "The instruct version of each model is used, which includes pre-train, supervised fine-tune and model alignment (in both cases including DPO). Our experimentation executes an additional DPO training."

**(e) Hyperparameters.** Card says: "Hardware: NVIDIA H100 64 GB GPUs", "Devices: 64 GPUs (16 nodes)", "Time: 10.23h", "Batch Size: 63", "LR: 10−6". Paper says large models used batch size 64 and learning rate 10^{-6}, and that 70B/72B trainings took "1.3 to 10.23 hours". The card assigns 10.23 hours to this repo. Epochs and DPO beta: not stated.

**(f) Evaluation.** Card table, which matches the paper's released-model comparison: Egida test attack-success ratio 0.125 versus 0.235 for the base; DELPHI 0.042 versus 0.051; ALERT-Base 0.210 versus 0.329; ALERT-Adv 0.019 versus 0.050. OpenLLM Leaderboard average 0.620 versus 0.618. MMLU generative ROUGE-1 0.768 versus 0.771. OR-Bench 80K refusal 0.016 versus 0.015; OR-Bench Hard 0.170 versus 0.102. Card says the refusal ratio is "computed as keyword matching with a curated list of keywords." Paper Appendix F lists those keywords. Safety labels in the paper's main eval are from Llama-Guard-3-8B.

**(g) What it is built to output, and what it is built to detect.** A chat reply. The DPO pairs a safe answer with an unsafe answer to the same user prompt. It is not a model that emits safe/unsafe as a label. It is built so that jailbreak prompts, which previously drew an unsafe reply from this same base model, are answered with the safe reply instead. This agrees with the earlier row: user prompt, chat reply, more refusals. The paper also measures over-refusal, so "more refusals" is the safety goal, not a claim that every prompt is refused.

### Discrepancies

1. Batch size is 63 on the model card and 64 in the paper for "the large models." Learning rate 10^{-6}, 64 H100s, and 10.23 hours agree.
2. The abstract's "2,000 samples" is the data-efficiency claim in section 4, not the size of this released checkpoint. This checkpoint's set is 2,153 rows.
3. Inventory methods `dpo`, dataset `HPAI-BSC/Egida`, and parent `Qwen/Qwen2.5-72B-Instruct` match the paper. Inventory does not record that the parameter-update scope is unstated.

### Confidence

Medium. DPO, the 2,153-row set, the base, and the evaluation numbers are in the paper and on the card. The paper never says whether training updated every weight or a LoRA, and it never states epochs or beta.

### Queries tried

1. `arxiv Efficient Safety Retrofitting Against Jailbreaking Egida DPO Qwen2.5-72B`
2. `HPAI-BSC Egida OpenRLHF DPO github Qwen2.5-72B training script`
3. `Egida-DPO-Qwen2.5-72B-Instruct number of rows Hugging Face`
4. `Garcia-Gasulla Tormos Egida DPO site:aclanthology.org OR site:semanticscholar.org` (no Egida paper on ACL; a different Garcia-Gasulla paper is listed)
5. `"Efficient Safety Retrofitting Against Jailbreaking" Garcia-Gasulla 2502.13603`
6. Springer chapter `10.1007/978-3-032-02018-5_39` (abstract only)
7. Datasets-server size API for `HPAI-BSC/Egida`

## flowxai/scam-guard-qwen06b

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/flowxai__scam-guard-qwen06b__2026-10-05.md`. Live Hub API confirms the same card and the file list: https://huggingface.co/api/models/flowxai/scam-guard-qwen06b.
- Benchmark card, which says it is held out from training: https://huggingface.co/datasets/flowxai/scamguardbench.
- Official base card: https://huggingface.co/Qwen/Qwen3-0.6B.
- No paper, blog, or GitHub repository containing `training/train_cuda.py` was found. Searches that hit `train_cuda.py` were other projects.

The 1.7B card repeats the same training section with a different base and different wall-clock time. It is the same author's copy, not an independent source.

### Training record

**(a) Objective.** Supervised fine-tuning. Card says: "CUDA full-budget 3-epoch LoRA (`training/train_cuda.py`, transformers + PEFT + trl `SFTTrainer`), from `Qwen/Qwen3-0.6B`." The phrase "SFT train set" is also used for the data mix. `SFTTrainer` is the statement. The filename `train_cuda.py` is not public, so the script itself was not read.

**(b) Parameter-update scope.** LoRA, not QLoRA. Card says: "LoRA rank 16 / alpha 32 / dropout 0.05, all-linear modules" and "bf16". It does not say 4-bit loading during training. The int4 and int8 GGUF and MLX files are inference formats ("On-device formats: GGUF ... and MLX-quantized"). Merge: not stated anywhere found. The Hub file list has a root `model.safetensors` of 596,049,920 BF16 parameters, which is the full Qwen3-0.6B size, and no `adapter_config.json`. That describes the upload. It is not a sentence that says `merge_and_unload`. Hub tag `base_model:quantized:Qwen/Qwen3-0.6B` comes from the GGUF and MLX files in the same repo. It is not a statement that training was quantization-aware.

**(c) Training data.** The card's YAML `datasets:` entry is `flowxai/scamguardbench`. The training section says the train set is disjoint from that benchmark. Card says: "Train ∩ ScamGuardBench = ∅ (contamination-verified)." The benchmark card says: "every v0.2 item is from the held-out TEST split, disjoint from any scam-guard training data." So `flowxai/scamguardbench` is the evaluation set named in the YAML, not the training corpus.

Training data, as stated:

- "Public seed layer (relabeled): UCI SMS Spam Collection (CC BY 4.0), enron_ham (SetFit/enron_spam ham slice; no explicit license → reference/research-use), phishing_email (zefang-liu; LGPL-3.0). Relabeled into the verdict+tactic scheme ... per-source human spot-check."
- "Synthetic layer: generated from specs (tactic × channel × language × register)."
- Balance: "≥45% legitimate messages, RO ≥35%, ~40% of RO diacritic-free, `suspicious` ~14.5% of the SFT train set."

n of the training set: not stated. The 14.5% figure has no denominator. The benchmark itself is 753 unique items on its card, and 1,099 rows across four configs on datasets-server (standard 598, hard 33, legit_confusable 346, suspicious 122). Those are bench counts. Language: English and Romanian. Provenance: public message corpora, then relabeled, relabeler model not named; plus synthetic text, generator model not named. Card says both sizes "trained from the same data."

**(d) Base.** `Qwen/Qwen3-0.6B`. Card says: "The exact repo `Qwen3-0.6B-Instruct` does not exist on Hugging Face — Qwen3 merged instruct+thinking into the single base repo `Qwen/Qwen3-0.6B` (instruction-capable, Apache-2.0). We fine-tune it with thinking disabled." The official Qwen3-0.6B card says: "Training Stage: Pretraining & Post-training" and that non-thinking mode is "aligning its functionality with the previous Qwen2.5-Instruct models." So the base is post-trained, not a raw pretrained checkpoint. The separate repo `Qwen/Qwen3-0.6B-Base` is not the base this card names.

**(e) Hyperparameters.** Card says: "adamw, cosine 2e-5→2e-6 with 60-step warmup, effective batch 4, seq 1280, bf16, gradient-checkpointing, seed 20260703; 3 real epochs on an on-demand NVIDIA L4 (~2h16m, 0 OOM), thinking disabled." An earlier "MLX first pass (~1 epoch)" is described as superseded.

**(f) Evaluation.** On the card, from the "FINAL CUDA 3-epoch" run: ScamGuardBench v0.2 120-item slice, verdict micro-F1 0.958, macro-F1 0.926, tactic macro-F1 0.951, evidence pass rate 0.980, legit-confusable false-positive rate 0.000. Out-of-distribution 20 hand-written messages: 18/20, macro-F1 0.614, legit false-alarm rate 0.000. Compared on the card with claude-haiku-4-5 and a keyword baseline. The card itself says the bench numbers have a home-field advantage because the bench comes from the same generator family as the training data.

**(g) What it is built to output, and what it is built to detect.** A verdict, plus short fields that stay inside a fixed JSON schema. Card says: "Given one message, scam-guard returns a 3-level verdict" (`scam_likely`, `suspicious`, `no_indicators`), "the manipulation tactics it found", "a calm plain-language explanation", and "a recommended safe action from a fixed list." It detects scam and fraud tactics in SMS, email, and chat, in English and Romanian. It is not a general chat model that refuses or answers an arbitrary user. This agrees with the earlier row: scam or fraud message, reasoning and a verdict, judgment training. The explanation is a field of that verdict, not a free counselling reply, so the batch label is `verdict`, not `both`.

### Discrepancies

1. Inventory datasets cell is `flowxai/scamguardbench`, copied from the card YAML. The same card says that benchmark does not intersect the training set. Methods `lora|sft` and parent `Qwen/Qwen3-0.6B` match the card.
2. Hub relation tag is `quantized`, because GGUF and MLX files sit in the repo. The training section says bf16 LoRA, not QLoRA.
3. Merge is not stated. The root weight file is a full-size BF16 model with no `adapter_config.json`.

### Confidence

Medium. The card names `SFTTrainer`, rank, alpha, target modules, data sources, and the hardware. No public script was found, the training-set size and the generator model are missing, and the YAML dataset id is the held-out bench.

### Queries tried

1. `flowxai scam-guard-qwen train_cuda.py SFTTrainer LoRA github`
2. `"scam-guard" OR scamguardbench flowxai Qwen3 Romanian site:github.com`
3. `flowxai scam-guard Qwen3-0.6B "SFTTrainer" L4`
4. `"train_cuda.py" scam-guard OR scamguard flowxai github` (hits were unrelated CUDA trainers)
5. Hugging Face API `flowxai/scam-guard-qwen06b` (file list and parameter count)
6. Dataset page `flowxai/scamguardbench` and datasets-server size
7. Official card `Qwen/Qwen3-0.6B` (post-training stage)

## cs-552-2026-Flash-McQueenS-and-TheKing/safety_model

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/cs-552-2026-Flash-McQueenS-and-TheKing__safety_model__2026-10-05.md`. Hub metadata in `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__001.csv`. Live page shows F16, 1,720,574,976 parameters, and the tag `base_model:adapter:Qwen/Qwen3-1.7B`.
- Dataset card, which restates the model card in shorter form: https://huggingface.co/datasets/cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data. Page reports 3,250 rows.
- Course context, which does not describe this team's recipe: EPFL coursebook https://edu.epfl.ch/coursebook/en/modern-natural-language-processing-CS-552 says the project is to "train a model to solve the task." Course repo https://github.com/epfl-nlp/cs-552-modern-nlp README is a lecture schedule. It does not name this team, LoRA, or SafetyBench.
- https://featherless.ai/models/cs-552-2026-Flash-McQueenS-and-TheKing/safety_model restates the model card. It is a copy.
- Other CS-552 teams' `safety_model` cards (for example `cs-552-2026-thinking-tokens`) describe different recipes. They are not this checkpoint.

No paper and no team training script were found.

### Training record

**(a) Objective.** Supervised fine-tuning. Card says: "It is a supervised fine-tune of Qwen/Qwen3-1.7B" and "Method: Supervised fine-tuning with LoRA, then merged to a full checkpoint." Loss: "Completion-only (prompt and the empty `<think></think>` block are masked)." The card has a section "Why non-thinking, and no CoT distillation" that says they did not distill chain-of-thought. So this is SFT, not distillation. The tag `sft` matches that paragraph.

**(b) Parameter-update scope.** LoRA, then merged. Card says: "LoRA | r=16, α=32, dropout=0.05, all linear projections" and "The LoRA adapter was merged back into the base weights so this repository is a standalone, vLLM-loadable Qwen3 checkpoint (full `model.safetensors`)." Not QLoRA: the card does not say 4-bit training. Precision line is "bf16/fp16". The uploaded file is F16 with 1,720,574,976 parameters, the full 1.7B size. Hub tag `base_model:adapter` disagrees with the merge sentence; the card's sentence is the one that describes the procedure.

**(c) Training data.** Hub id: `cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data`. Card says: "3,250 English multiple-choice items across the seven safety categories of SafetyBench (Zhang et al., 2024)." Breakdown on the card: Unfairness and Bias from BBQ, 700; Ethics and Morality from ETHICS commonsense short, 700; Physical Health from SafeText, 700; Offensiveness from TweetEval offensive, 700; Mental Health, Illegal Activities, and Privacy and Property, 150 each, "LLM-generated" using a "SafetyBench augmentation recipe." Generator model: not stated. The four public categories are "derived from established public datasets" and reformatted into multiple choice, not copied as raw labels. Dataset card says the same 3,250 count and points back to the model card. Language: English.

**(d) Base.** `Qwen/Qwen3-1.7B`. Same post-trained Qwen3 release as the 1.7B scam-guard base: official family card says "Training Stage: Pretraining & Post-training", and the Hub model tree shown on the scam-guard 1.7B page places `Qwen/Qwen3-1.7B` as a finetune of `Qwen/Qwen3-1.7B-Base`. This course card fine-tunes `Qwen/Qwen3-1.7B` with `enable_thinking = false`. It is not the raw Base checkpoint.

**(e) Hyperparameters.** Card table: epochs 3; learning rate 1e-4, cosine, 3% warmup; effective batch 16 (per-device 2 × gradient accumulation 8); max sequence length 1024; bf16/fp16; non-thinking. Hardware: not stated anywhere found.

**(f) Evaluation.** The card says the benchmark "is multiple-choice, scored pass@1" and does not report a score. No accuracy table was found on the card or the dataset page.

**(g) What it is built to output, and what it is built to detect.** An exam letter. Card says: "it emits a one-sentence justification and then the answer letter inside `\boxed{}`." It answers English multiple-choice items in the seven SafetyBench categories above. Card says: "It selects answers on a fixed-format MCQ task; it is not a content-moderation or refusal system and should not be used as one." This agrees with the earlier row, which called the output an exam letter and said it is neither a counselling reply nor a safe/unsafe label. The CSV uses `verdict` because that is the closest allowed label: the model picks an option letter. It is not a safe/unsafe classifier.

### Discrepancies

1. Hub tag `base_model:adapter:Qwen/Qwen3-1.7B` versus the card: "The LoRA adapter was merged back into the base weights." The weight file is a full F16 checkpoint, which fits the merge sentence.
2. Inventory methods `lora|sft`, dataset `cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data`, and parent `Qwen/Qwen3-1.7B` match the card. The inventory parent-class note "Training Stage: Pretraining & Post-training" is the Qwen3 base card's line, not a claim that this student run continued pretraining.
3. Featherless repeats the card and adds no training fact.

### Confidence

High. The card states SFT, LoRA rank and alpha, the merge, 3,250 rows, epochs, learning rate, and batch size, and the dataset page repeats 3,250; the EPFL course page only says that students train a model, and no score is published.

### Queries tried

1. `EPFL CS-552 2026 Flash McQueen safety_model Qwen3-1.7B SFT LoRA`
2. `"CS-552" EPFL "Modern NLP" 2026 safety benchmark Qwen3 SafetyBench`
3. `"Flash McQueen" OR "Flash-McQueenS" safety_sft_data EPFL CS-552`
4. `site:edu.epfl.ch CS-552 Modern NLP Spring 2026 project Qwen3 safety`
5. GitHub API and raw README `epfl-nlp/cs-552-modern-nlp` (lecture list; no team recipe)
6. Dataset page `cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data`
7. Featherless model page (copy of the card)

## flowxai/scam-guard-qwen17b

### Sources

- Cached card: `revision_3_experiments/hf_inventory/cache/readmes/flowxai__scam-guard-qwen17b__2026-10-05.md`. Hub API: https://huggingface.co/api/models/flowxai/scam-guard-qwen17b (BF16, 1,720,574,976 parameters; root `model.safetensors`; GGUF `gguf/scam-guard-qwen17b-cuda-Q8_0.gguf`; `mlx-int4/`; no `adapter_config.json`).
- Same benchmark card and same failed search for `train_cuda.py` as the 0.6B model. The two cards are one write-up with size-specific numbers. They are not independent of each other.

### Training record

**(a) Objective.** Supervised fine-tuning, same statement as the 0.6B card. Card says: "CUDA full-budget 3-epoch LoRA (`training/train_cuda.py`, transformers + PEFT + trl `SFTTrainer`), from `Qwen/Qwen3-1.7B`."

**(b) Parameter-update scope.** LoRA. Card says: "LoRA rank 16 / alpha 32 / dropout 0.05, all-linear modules" and bf16. Not 4-bit training. Merge: not stated. The upload is a full BF16 file of 1,720,574,976 parameters and no adapter file. Hub tag is `base_model:quantized:Qwen/Qwen3-1.7B` because the repo also holds GGUF and MLX quants. The model tree on the live page is `Qwen/Qwen3-1.7B-Base` finetuned to `Qwen/Qwen3-1.7B`, then quantized to this repo. That "quantized" edge is the Hub relation, not the training objective.

**(c) Training data.** Card says: "Both sizes trained from the same data." The data paragraph matches the 0.6B card: UCI SMS Spam Collection, `SetFit/enron_spam` ham, zefang-liu phishing email, plus a synthetic layer from specs. "`suspicious` ~14.5% of the SFT train set." Training n: not stated. YAML dataset `flowxai/scamguardbench` is the held-out bench, same caveat as the 0.6B model. Language: English and Romanian. Generator model for the synthetic layer: not stated.

**(d) Base.** `Qwen/Qwen3-1.7B`. Card says the Instruct-named repo does not exist and that this repo is "instruction-capable" and was fine-tuned "with thinking disabled." Official family description: post-training is part of the Qwen3 release ("Training Stage: Pretraining & Post-training" on the 0.6B card of the same family). The Base checkpoint is a different Hub id, and this card does not use it.

**(e) Hyperparameters.** Same as the 0.6B card except the hardware time: "3 real epochs on an on-demand NVIDIA L4 (~3h21m, 0 OOM)". Learning rate cosine 2e-5 to 2e-6, 60-step warmup, effective batch 4, sequence length 1280, seed 20260703, AdamW, gradient checkpointing. The MLX "~1 epoch" pass is described as superseded. The card says that pass had macro-F1 0.921, and the CUDA run 0.975.

**(f) Evaluation.** Card, CUDA 3-epoch run, ScamGuardBench v0.2 120-item slice: verdict micro-F1 0.983, macro-F1 0.975, tactic macro-F1 0.950, evidence pass rate 0.974, legit-confusable false-positive rate 0.000. Out-of-distribution 20 messages: 19/20, macro-F1 0.967, legit false-alarm rate 0.000. One shared miss with the 0.6B model is described: a Romanian family-emergency scam scored `no_indicators`.

**(g) What it is built to output, and what it is built to detect.** Same contract as the 0.6B model: a 3-level scam verdict, tactic ids with verbatim evidence, a short explanation, and one recommended action. It detects scam and fraud in SMS, email, and chat, English and Romanian. This agrees with the earlier row (reasoning and a verdict). Batch label: `verdict`.

### Discrepancies

1. Same dataset mismatch as the 0.6B model: inventory datasets cell is `flowxai/scamguardbench`, and the card says the training set does not intersect that bench. Methods `lora|sft` and parent `Qwen/Qwen3-1.7B` match.
2. Hub `quantized` tag versus training-time bf16 LoRA.
3. Merge not stated, while the uploaded root file is a full-size BF16 model.

### Confidence

Medium. Same reason as the 0.6B card: the training paragraph is specific, and it is not backed by a public script, a training-set count, or a named generator.

### Queries tried

1. `flowxai/scam-guard-qwen17b` model card and fine-tuning section
2. `flowxai scam-guard-qwen train_cuda.py SFTTrainer LoRA github`
3. `"scam-guard" OR scamguardbench flowxai Qwen3 Romanian site:github.com`
4. `flowxai scam-guard Qwen3-0.6B "SFTTrainer" L4` (sibling card; 1.7B section is the same recipe)
5. `"train_cuda.py" scam-guard OR scamguard flowxai github`
6. Hugging Face API `flowxai/scam-guard-qwen17b` (file list, 1,720,574,976 BF16 parameters)
7. Dataset page `flowxai/scamguardbench` (held-out bench, shared by both sizes)

## Patterns in this batch

Four of the five models are supervised next-token training. Only the Egida 72B model is preference optimization, and that one is the only model with a paper. The paper is clear that the extra step is DPO on top of an already instruction-tuned and already DPO-aligned Qwen, and it never says whether that extra step updated every weight.

BuildEng and the CS-552 model both say the LoRA was merged into the uploaded weights. BuildEng is 4-bit QLoRA (NF4, rank 32, alpha 64). The CS-552 model and both scam-guard models are bf16 LoRA (rank 16, alpha 32, all linear layers), not QLoRA. The scam-guard cards never say the adapter was merged, even though each repo's main weight file is a full-size BF16 model and the int4 files are separate inference quants.

The two scam-guard cards are one training recipe at two sizes, on data the cards describe but do not count. Their YAML dataset id is the held-out benchmark, so an inventory that copies `datasets:` will name the test set as the training set.

Output type is not one safety task. BuildEng and Egida-DPO answer the user. Scam-guard returns a scam verdict. The CS-552 model returns an exam letter. Calling all five "safety fine-tunes" hides that split. Hyperparameters are missing where they matter for the taxonomy: BuildEng has no learning rate or epoch count, Egida has no beta, no epoch count, and no LoRA-versus-full statement, and the card's batch size (63) disagrees with the paper's (64).
