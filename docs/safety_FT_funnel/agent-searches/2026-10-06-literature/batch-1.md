# Safety fine-tune literature, batch 1 of 8

Five safety checkpoints. Facts below are quoted from a paper, a file, a dataset card, or the cached model card. A method word in a name is not treated as a method.

The earlier output-type note is `docs/safety_FT_funnel/how-models-are-filtered.md`. This reading agrees with all five rows: COMPASS and OTel-LLM-12B-Safety write a chat reply; SycoFact, Nemotron-Content-Safety-Reasoning-4B, and BananaMind V2.5 write a verdict. Details are in each section.

## Summary

| Model | Source found | Objective | Update scope | Data (name, n, provenance) | Base | Output type | Matches inventory |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA | paper | SFT | LoRA, 8-bit base, rank 32, alpha 64; merge not stated | COMPASS LODO Policy-Aware SFT, 4,121 rows, synthetic model replies | google/gemma-3-4b-it (instruction-tuned) | reply | partly |
| iwalton3/sycofact | code and dataset card | SFT on scored text; the word SFT is not in the model card | full | sycofact-training-data; config says 43,271 train; synthetic scores from steered Gemma 3 27B | google/gemma-3-4b-it (instruction-tuned) | verdict | partly |
| nvidia/Nemotron-Content-Safety-Reasoning-4B | code and dataset card | SFT on teacher reasoning traces; cited paper's runs are a different mix | not stated (uploaded files are a full checkpoint) | Nemotron Content Safety Reasoning Dataset, about 36,000; traces from three other models | google/gemma-3-4b-it (instruction-tuned) | verdict | partly |
| farbodtavakkoli/OTel-LLM-12B-Safety | dataset card; training method is the model card | SFT-style prompt-to-completion; card says post-training / fine-tuning | full | OTel-Safety; page shows 1,575,102 rows; completions' generator not named | google/gemma-3-12b-it (instruction-tuned) | reply | yes |
| Banaxi-Tech/BananaMind-V2.5-Content-Safety | none beyond the card | supervised instruction-tuning | unnamed adapter, merged | Nemotron 3.5 Content Safety, text-only subset, count not stated | google/gemma-4-E2B-it (instruction-tuned) | verdict | partly |

## AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA

### Sources

The paper and the card describe the same Gemma run. The paper does not print the repo id. The hyperparameters and the TelePath table match.

- Paper: Choi et al., COMPASS, ACL 2026 long paper, arXiv html used here: https://arxiv.org/html/2601.01836 (Anthology: https://aclanthology.org/2026.acl-long.2139/). Appendix G.3 is the training section.
- Dataset card: https://huggingface.co/datasets/AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset
- Card: `revision_3_experiments/hf_inventory/cache/readmes/AIM-Intelligence__COMPASS_gemma-3-4b-it_LoRA__2026-10-06.md`
- `config.json`: https://huggingface.co/AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA/raw/main/config.json
- GitHub https://github.com/AIM-Intelligence/COMPASS is the evaluation framework. No LoRA training script was found there.
- The short dataset id in the card YAML, `AIM-Intelligence/COMPASS-Policy-aware-SFT`, resolves on the Hub to `AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset`.

### Training record

**(a) Objective.** Supervised fine-tuning. Paper says: "The SFT dataset comprises 4,121 query-response pairs from the remaining 7 domains, where responses were selected from outputs achieving full policy adherence in our main experiments." The results table labels the run "LODO SFT (LoRA)". URL: https://arxiv.org/html/2601.01836

**(b) Update scope.** LoRA on an 8-bit base. Paper says: "We trained LoRA adapters for 3 epochs with rank \(r=32\), \(\alpha=64\), peak LR \(3\times 10^{-4}\) for Gemma-3-4B-it, using cosine learning rate scheduling, batch size 32, and AdamW optimizer with 8-bit quantization." Target modules are not stated. 8-bit plus LoRA is not 4-bit QLoRA. The card says: "This repository provides a **LoRA adapter**" and "Quantization: 8-bit during training." Whether the adapter was merged is not stated. `config.json` is a full `Gemma3ForConditionalGeneration` with `"unsloth_fixed": true` and `"unsloth_version": "2025.11.3"`. The file list has two safetensors shards and no `adapter_config.json`. The Hub parameter count is 4,300,079,472 BF16, the full Gemma 3 4B size.

**(c) Data.** `AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset`, 4,121 rows, English. Dataset card says: "Responses are selected from model outputs that achieved **full policy adherence under COMPASS evaluation**." The paper says COMPASS queries are synthesized with Claude-Sonnet-4 and Qwen3-235B, and validated with GPT-5-mini. The train file's `model` column, counted from the datasets-server rows API, is the model that wrote the selected reply:

| Generator | Rows |
| --- | ---: |
| gpt-5-2025-08-07 | 2,275 |
| google/gemma-3-27b-it | 624 |
| gemini-2.5-flash | 622 |
| claude-sonnet-4@20250514 | 263 |
| meta-llama/llama-3.3-70b-instruct | 107 |
| gemini-2.5-pro | 88 |
| qwen/qwen3-235b-a22b-2507 | 74 |
| moonshotai/kimi-k2 | 33 |
| google/gemma-3-4b-it | 23 |
| google/gemma-3-12b-it | 8 |
| qwen/qwen-2.5-72b-instruct | 3 |
| gpt-5 | 1 |

Companies in the file: PlanMyTrip 890, VirtuRecruit 763, AutoViaMotors 690, MediCarePlus 468, TutoraVerse 457, CityGov 431, FinSecure 420, TelePath 2.

**(d) Base.** `google/gemma-3-4b-it`, the instruction-tuned Gemma 3 4B. Paper and card both say Gemma-3-4B-it.

**(e) Hyperparameters.** Epochs 3, peak learning rate 3e-4, batch size 32, AdamW, cosine schedule, LoRA rank 32, alpha 64, 8-bit during training. Hardware is not stated.

**(f) Evaluation.** Held-out TelePath policy-alignment scores. Paper Table 11 and the card match: base system prompt Allowed Base 100.00, Allowed Edge 87.62, Denied Base 28.00, Denied Edge 0.00; LODO SFT Allowed Base 86.67, Allowed Edge 94.29, Denied Base 60.00, Denied Edge 62.24.

**(g) Output.** A chat reply that follows an organization's allowlist and denylist. The earlier note calls this a chat reply for policy adherence. This reading agrees. It is not trained to emit safe/unsafe.

### Discrepancies

1. The card YAML and the inventory row say `AIM-Intelligence/COMPASS-Policy-aware-SFT`. The Hub dataset id is `AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset`. The short name resolves to that dataset.
2. The card, the dataset card, and the paper say TelePath is held out. The train file contains 2 TelePath rows.
3. The card calls the upload a LoRA adapter. The files are a full Gemma 3 checkpoint. Merge is not stated.
4. The paper does not print this repo id. The rank, learning rate, batch size, epoch count, and TelePath scores match the card.

### Confidence

High. The paper's Appendix G.3 and the card give the same Gemma hyperparameters and the same TelePath table.

### Queries tried

1. AIM-Intelligence COMPASS_gemma-3-4b-it_LoRA training LoRA SFT
2. COMPASS framework organization-specific policy alignment arxiv 2601.01836 fine-tuning
3. Dasol Choi COMPASS github AIM-Intelligence policy-aware SFT LoRA gemma target modules
4. COMPASS LODO Gemma-3-4B LoRA rank site:arxiv.org
5. site:github.com/AIM-Intelligence/COMPASS LoRA SFT gemma training script
6. COMPASS-Policy-aware-SFT-Dataset model field gpt-5 gemma

Followed one hop to the arXiv html, the dataset page, `config.json`, the Hub dataset API, and the datasets-server rows.

## iwalton3/sycofact

### Sources

No paper and no GitHub repo describe this training. Izzie Walton's public GitHub account does not list a SycoFact repository. The cited arXiv 2509.10970 is Psychosis-Bench, which the card says was not used in training.

- Card: `revision_3_experiments/hf_inventory/cache/readmes/iwalton3__sycofact__2026-10-05.md`
- `training_config.json` in the same repo: https://huggingface.co/iwalton3/sycofact/raw/main/training_config.json
- Dataset card: https://huggingface.co/datasets/iwalton3/sycofact-training-data

The dataset card and `training_config.json` are the same author as the model card. They add counts and hyperparameters the model card prose does not print. They are not an independent lab's write-up.

### Training record

**(a) Objective.** Supervised training on scored assistant text. Card says: "The resulting 4B model was fully finetuned over this scored dataset." The dataset card says each record is "in chat messages format compatible with SFTTrainer / TRL" and shows the assistant message as the score JSON. No script in the repo imports a trainer. The model card does not print "SFT". It also does not describe DPO, ORPO, PPO, or a reward loss. The tag `reward-model` is not a training-method statement. The card says: "Not a preference ranker."

**(b) Update scope.** All weights. `training_config.json` says `"mode": "full_finetune"`. The dataset card says: "Full finetune (all parameters)". The card says "fully finetuned". There is no `adapter_config.json`. The safetensors count is 4,300,079,472 BF16.

**(c) Data.** `iwalton3/sycofact-training-data`, English. Dataset card file counts: `sycofact_train.jsonl` 37,898, `sycofact_val.jsonl` 4,210, `phoenix_train.jsonl` 5,970. `training_config.json` says `"train_size": 43271`, `"val_size": 4807`, `"data": "v2_evaluator + phoenix_eliza"`. Those two counts are not the same sum (37,898 + 5,970 = 43,868).

Dataset card says: "No human labels. Every record was scored by a steered Gemma 3 27B using a geometric alignment direction extracted via PCA from contrastive activation pairs." Phoenix rows: "synthetically generated using steered Gemma 3 27B for assistant turns and Gemma 3 27B abliterated for user turns." The card names scenario sources: contrastive pairs, TruthfulQA, BeaverTails, Do-Not-Answer, SYCON-Bench, Chatbot Arena, synthetic therapeutic conversations, and Anthropic sycophancy datasets. The ablation is how some user turns were written. It is not a weight edit of this 4B checkpoint.

**(d) Base.** `google/gemma-3-4b-it`, instruction-tuned. `training_config.json` says `"model_id": "google/gemma-3-4b-it"`.

**(e) Hyperparameters.** Both the config file and the dataset card: 3 epochs, learning rate 5e-6, batch size 1 with 8 gradient-accumulation steps. Config also says `max_seq_len` 2048. Dataset card says: "bf16, gradient checkpointing" and "Cost: ~$13 on a single A40 GPU (RunPod)".

**(f) Evaluation.** Reported on the card, not in a paper: Psychosis-Bench 192/192 turns; AISI harmful-advice composite correlation r=-0.810 (fast mode); PKU-SafeRLHF F1 0.872 on 4,000 responses; RewardBench safety subsets; a 290-sample validation against a 27B mentor.

**(g) Output.** Numeric scores from 0 to 1 for factual, honest, harmless, helpful, honoring, sycophantic, and a composite. Reasoning mode also writes short reasons. The earlier note calls the output numeric scores under judgment training. This reading agrees: it is a verdict, not a chat reply to the end user.

### Discrepancies

1. The inventory methods cell is empty. The card, the dataset card, and `training_config.json` say a full finetune.
2. Train and validation sizes in `training_config.json` (43,271 and 4,807) do not equal the dataset card's file counts (37,898, 4,210, and 5,970).
3. The dataset card says the training script is in the model repository. The file list has `training_config.json` and no Python script.
4. The Hub `baseModels` relation is `quantized` because `SycoFact-4B-Q8_0.gguf` sits in the same repo. The safetensors are BF16.

### Confidence

Medium. Three files from the same author agree on a full finetune, the base, and the learning rate. No script and no outside paper confirm the loss, and the row counts disagree.

### Queries tried

1. iwalton3 sycofact training methodology Gemma 3 4B fully finetuned
2. Izzie Walton SycoFact github training script geometric PCA Gemma 27B
3. izzie walton OR iwalton3 sycofact SFTTrainer OR full finetune github
4. SycoFact 4B Izzie Walton site:reddit.com OR site:iwalton.com OR site:github.com
5. iwalton3/sycofact-training-data dataset card
6. iwalton3/sycofact training_config.json

Followed one hop to the dataset card, the raw config file, the model file list, and the author's GitHub profile.

## nvidia/Nemotron-Content-Safety-Reasoning-4B

### Sources

The card cites Sreedhar, Rebedea, and Parisien, "Safety Through Reasoning," Findings of EMNLP 2025, https://arxiv.org/html/2505.20087 and https://aclanthology.org/2025.findings-emnlp.1193/. That paper does not name this repo. Its training section is a different experiment. The files in this repo are the direct record.

- Card: `revision_3_experiments/hf_inventory/cache/readmes/nvidia__Nemotron-Content-Safety-Reasoning-4B__2026-10-05.md`
- `trainer_state.json`: https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/trainer_state.json
- Dataset card: https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset
- NVIDIA NeMo-Guardrails docs show how to serve the model. They do not describe training. Other NeMo recipes for Nemotron 4B models are different checkpoints.

### Training record

**(a) Objective.** Supervised training on reasoning traces. `trainer_state.json` logs `loss`, `eval_loss`, `grad_norm`, and `learning_rate`. It does not log a reward or a KL term. The card says the model is "a finetuned version of Google's Gemma-3-4B-it" and that "one sentence reasoning traces ... are used for the actual training." The paper says "We utilize Llama Factory for supervised fine-tuning and VERL for our RL based experiments" and "All experiments are conducted using Llama-3.1-8B-Instruct." Appendix F reports a negative GRPO result on those experiments. That GRPO result is not evidence that this checkpoint was trained with GRPO.

**(b) Update scope.** Not stated. The card does not say full, LoRA, or QLoRA. The repo contains a full Gemma 3 checkpoint, `trainer_state.json`, `training_args.bin`, eight `rng_state_*.pth` files, and `zero_to_fp32.py`, and no `adapter_config.json`. A full checkpoint does not say whether training updated every weight. The LoRA rank, alpha, and learning rate on the Nemotron 3.5 content-safety card are for that later model, not this one.

**(c) Data.** `nvidia/Nemotron-Content-Safety-Reasoning-Dataset`. Dataset card says: "This dataset has been used to train the Nemotron-Content-Safety-Reasoning-4B guard model." Counts: 28,000 samples from Nemotron Content Safety Dataset V2 (of 30,007 training samples) and 8,712 topic-control samples from CantTalkAboutThis. The model card says "Approximately 36000 samples." Language: English. The dataset card adds that the V2 portion "may contain small samples in other languages."

Traces are synthetic. Dataset card says they were extracted from DeepSeek-R1-0528, Qwen3-32B, and gpt-oss-120b, and kept only when the trace's predicted label matched the ground-truth label. Those ground-truth labels come from the human-annotated V2 and topic-control sets. The card's architecture section names Qwen3-32B only; the later training-data section names all three generators. The paper's teacher is DeepSeek-R1-671B on WildGuardMix, which is not this file.

**(d) Base.** `google/gemma-3-4b-it`, instruction-tuned. Card says: "Nemotron-Content-Safety-Reasoning-4B is a finetuned version of Google's Gemma-3-4B-it model."

**(e) Hyperparameters from `trainer_state.json`.** `num_train_epochs` 5, `max_steps` 8970, `train_batch_size` 2, `logging_steps` 10, `eval_steps` 150. The highest `learning_rate` in the log is 9.999998485637598e-07 at step 900. The saved log stops at epoch 2.1739130434782608, global step 3900. Hardware for this run is not stated. Eight RNG state files are in the repo. The paper's Appendix B ("1 node of 8xA100 GPUs", "batch size of 32", "learning rate of 1e-6", "5 epochs") describes the paper's experiments, not a statement that this file finished that schedule.

**(f) Evaluation.** On the card, harmful F1. Reasoning off: vanilla combined 0.848, custom 0.857. Reasoning on: vanilla combined 0.842, custom 0.868. Named sets include XSTest-Response, Aegis 2.0, WildGuardTest, SimpleSafetyTests, JailbreakBench, OpenAI Moderation, Toxic Chat, CoSApien, and Dynaguardrail.

**(g) Output.** A verdict. Reasoning off writes `Prompt harm: harmful/unharmful` and `Response harm: harmful/unharmful`. Reasoning on writes a `<think>` trace and then those lines. It is built to judge the user prompt and the assistant reply under a caller-supplied policy, including topic-following. The specified output lines are the harm words, not the category names. The earlier note calls this reasoning and a verdict. This reading agrees: the classification is a verdict, and the reasoning-on mode adds a trace.

### Discrepancies

1. The inventory methods cell is empty.
2. The cited paper's backbone, teacher, and dataset are not this checkpoint's. Copying Appendix B's batch size of 32 onto this model would be wrong: `trainer_state.json` says `train_batch_size` 2.
3. The trainer log is configured for 5 epochs and stops at epoch 2.17. The file does not show a finished 5-epoch run.
4. The card names Qwen3-32B in one training paragraph and three generators in another.

### Confidence

Medium. The dataset card names this model, and `trainer_state.json` is in the repo. The log is incomplete, the parameter-update scope is not stated, and the cited paper is a different set of runs.

### Queries tried

1. Safety Through Reasoning Sreedhar Nemotron-Content-Safety-Reasoning-4B fine-tuning hyperparameters
2. Nemotron-Content-Safety-Reasoning-4B gemma-3-4b-it SFT LoRA trainer_state
3. Nemotron-Content-Safety-Reasoning-Dataset number of samples Qwen3-32B
4. Nemotron-Content-Safety-Reasoning-4B supervised OR LoRA OR full fine site:github.com OR site:developer.nvidia.com
5. arXiv 2505.20087 full text, including Appendix B, Appendix C, and Appendix F
6. Nemotron 3.5 content-safety LoRA card, checked and not used as this model's recipe

Followed one hop to the dataset README, `trainer_state.json`, and the NeMo-Guardrails deployment page.

## farbodtavakkoli/OTel-LLM-12B-Safety

### Sources

No retrieved paper section states this checkpoint's loss. The GitHub README at https://github.com/farbodtavakkoli/OTel repeats the card's ScalarLM table and also offers many other recipes. It says OTel 2.0 training code is forthcoming. The NeurIPS PDF linked from that README was not read as full text in this pass. The dataset card adds construction details the model card summarizes.

- Card: `revision_3_experiments/hf_inventory/cache/readmes/farbodtavakkoli__OTel-LLM-12B-Safety__2026-10-06.md`
- Dataset: https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety

The GitHub recipe list that names SFT, DPO, GRPO, and PPO is a menu of examples. It is not a statement that this checkpoint used those losses.

### Training record

**(a) Objective.** Prompt-to-completion training. Card says: "Training method | Full-parameter post-training / fine-tuning." The same card says the model is "full-parameter fine-tuned on OTel telecommunications data." It uses "post-training" and "fine-tuning" as one phrase. It does not name SFT, DPO, ORPO, PPO, or GRPO. The GitHub dataset table calls OTel-LLM "Context-grounded instruction tuning" and OTel-Safety "Abstention training when context is insufficient." The recorded objective is supervised next-token training on those completions, because that is the stated data layout, and the card does not describe a preference or reward loss.

**(b) Update scope.** All weights. Card says "full-parameter fine-tuned" and the lineage line "`google/gemma-3-12b-it` -> `OTel-Safety` full-parameter post-training". The file list is ten `pytorch_model` bins and no `adapter_config.json`.

**(c) Data.** `farbodtavakkoli/OTel-Safety`, English. The dataset page shows "Number of rows: 1,575,102" and also "Estimated number of rows: 5,538,213", so the row count is not a single figure. The model card's "filtered to 326,767 higher-confidence examples" is the cleaned corpus "across the OTel dataset family," which the dataset card repeats. It is not a count of rows used for this checkpoint.

Dataset card says abstention rows "were constructed by pairing queries with context passages that lack the information needed to answer." It does not name a generator model. Named document contributors are Yale, GSMA, NetoAI, Khalifa University, University of Leeds, and the University of Texas at Dallas. The GitHub README says "Red Hat supported synthetic-data generation" for the project. That sentence is not attached to this file. The first viewer rows have `abstention` false and a telecom answer. The model-card example is an abstention row. The dataset card says the abstention rate is "elevated relative to OTel-LLM" and does not give the rate.

**(d) Base.** `google/gemma-3-12b-it`, the instruction-tuned Gemma 3 12B. Card says that id.

**(e) Hyperparameters.** Card training-recipe table: ScalarLM; AdamW 8-bit; cosine decay with warmup; weight decay 0.01; warmup 100 steps; seed 42; maximum sequence length 1,500; BF16; Flash Attention 2; fully sharded data parallel; gradient checkpointing; "Epochs | 3 for LLM/embedding models; 2 for rerankers"; AMD MI300X, MI325X, MI355X and NVIDIA A100/H100. Learning rate is not stated. Batch size is not stated. The epoch line groups this model with other LLMs. It does not say "this checkpoint ran for 3 epochs" as its own sentence.

**(f) Evaluation.** No number for this checkpoint. Card says it "is not part of the 30-model core baseline table" and should be judged by correct-abstention rate and by answer quality when context is sufficient.

**(g) Output.** A chat reply. When context is insufficient or off-topic, the reply is a refusal. The card's example completion is: "I do not have enough information based on the provided context to answer your question." The earlier note calls this a chat reply with more refusals. This reading agrees. It does not emit safe/unsafe.

### Discrepancies

1. 326,767 is the family corpus. The OTel-Safety page reports 1,575,102 rows and a different estimate.
2. The GitHub README's method menu is not this model's training log.
3. No learning rate is stated anywhere found.
4. Inventory methods `full_finetune`, dataset `farbodtavakkoli/OTel-Safety`, and parent `google/gemma-3-12b-it` match the card.

### Confidence

Medium. The card states full-parameter fine-tuning and the recipe table. It does not state the learning rate, the number of OTel-Safety rows actually trained on, or a script bound to this checkpoint.

### Queries tried

1. farbodtavakkoli OTel-LLM-12B-Safety full-parameter fine-tuning OTel-Safety
2. Open Telco OTel Farbod Tavakkoli paper ScalarLM abstention safety fine-tuning github
3. Tavakkoli OTel NeurIPS OTel-Safety abstention learning rate full-parameter
4. site:github.com/farbodtavakkoli/OTel OTel-LLM-12B-Safety OR OTel-Safety scalarlm learning_rate
5. OTel-LLM-12B-Safety OR safety variants abstention ScalarLM Tavakkoli NeurIPS
6. farbodtavakkoli/OTel README raw

Followed one hop to the dataset page, the model-card commit, and the GitHub README.

## Banaxi-Tech/BananaMind-V2.5-Content-Safety

### Sources

No paper, GitHub repository, or script was found that names this repo's training. Searches that return LoRA ranks are other BananaMind checkpoints or unrelated content-safety notebooks.

- Card: `revision_3_experiments/hf_inventory/cache/readmes/Banaxi-Tech__BananaMind-V2.5-Content-Safety__2026-10-05.md`
- Source dataset: https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset
- `BananaMind/BananaMind-Content-Safety-Mini-1.5` is a different base (`LiquidAI/LFM2.5-350M-Base`) and is not used as this model's recipe.

### Training record

**(a) Objective.** Supervised instruction-tuning. Card says: "The fine-tuning used a supervised instruction-tuning setup." The printed target is `Safe` or `Unsafe` plus category names. The card does not mention DPO or a reward.

**(b) Update scope.** An adapter, type not named, then merged. Card says: "The final model weights are merged into the base model" and "Merged the fine-tuned adapter into the base model weights." It does not say LoRA, QLoRA, rank, alpha, or target modules. The upload is one `model.safetensors` (BF16 parameter count 5,104,297,539) and no `adapter_config.json`, which fits a merged save. Mini-1.5's LoRA rank 32 is that model's setting.

**(c) Data.** `nvidia/Nemotron-3.5-Content-Safety-Dataset`. Card says "text-only examples" and does not say how many. The dataset's own splits are train 88,688, validation 4,814, and test 4,814. The dataset card calls it "a hybrid real/synthetic supervised instruction dataset" with text and image rows. The `language` field has 12 classes. The `provenance` field has human, synthetic, and mixed. The BananaMind card does not say which of those rows were kept, and it does not name a generator for the synthetic rows.

**(d) Base.** `google/gemma-4-E2B-it`, the instruction-tuned Gemma 4 E2B. Card says that id.

**(e) Hyperparameters.** Card says: "Training hardware: Single A100" and "Training cost: 3.85$". Epochs, learning rate, and batch size are not stated.

**(f) Evaluation.** Card says overall error rate 5.12% "on the test data," with an early peak cumulative error rate of 10.0%. The same ordering versus ShieldGemma: 2B 35.30%, 9B 40.96%, 27B 8-bit 52.46%. The card does not say that "test data" is the dataset's test split. A short hand-written prompt list is also shown. The card says: "This is not a full benchmark."

**(g) Output.** A verdict. Safe text returns `Safe`. Unsafe text returns `Unsafe` and `Violated Categories`. The earlier note calls this a harm-category label on a user prompt. This reading agrees. The intended-use list also names assistant-response classification. The printed training target is one `Input:` prompt, not a prompt-plus-response pair.

### Discrepancies

1. The inventory methods cell is empty. The card states supervised instruction-tuning and a merged adapter.
2. The source dataset is larger, multilingual, and partly image-based. The card does not say the size of the text-only subset.
3. No outside source states a rank or a learning rate for this repo.

### Confidence

Medium for the objective and the merge, because both are sentences on the card and nowhere else. Low for anything the card omits: adapter type, row count, epochs, and learning rate.

### Queries tried

1. Banaxi-Tech BananaMind-V2.5-Content-Safety fine-tune LoRA gemma-4-E2B
2. BananaMind V2.5 Content Safety Banaxi-Tech adapter merged A100 supervised instruction
3. BananaMind V2.5 OR BananaMind-V2.5-Content-Safety LoRA OR epochs OR learning rate
4. Banaxi-Tech BananaMind content safety github OR reddit OR gemma-4-E2B
5. BananaMind-Content-Safety-Mini-1.5, read and kept separate
6. nvidia/Nemotron-3.5-Content-Safety-Dataset size and provenance

Followed one hop to the dataset API, the Mini-1.5 card, and other Banaxi translation cards.

## Patterns in this batch

Four of the five bases are instruction-tuned Gemma 3 models. BananaMind is instruction-tuned Gemma 4 E2B. Two checkpoints are reply models: COMPASS writes an organization-policy chat reply, and OTel-LLM-12B-Safety writes a telecom answer or an abstention sentence. Three write verdicts: SycoFact writes 0–1 scores, Nemotron writes harmful/unharmful lines, and BananaMind writes Safe/Unsafe plus category names. That split matches the earlier classification note.

Only COMPASS has a paper whose training appendix matches the card, including rank 32, alpha 64, learning rate 3e-4, and the TelePath scores. The Nemotron card cites an EMNLP paper, but that paper's supervised and GRPO runs use Llama-3.1-8B-Instruct and a Gemma-3-4B WildGuardMix replication. This repo's `trainer_state.json` is a supervised loss log with peak learning rate about 1e-6 and a configured 5 epochs, and the saved log stops at epoch 2.17.

SycoFact is a full finetune on synthetic scores from a steered Gemma 3 27B, with no human labels, and the train-size files do not agree. BananaMind states supervised instruction-tuning and a merged adapter, and does not name LoRA. OTel's card treats "post-training" and "fine-tuning" as the same full-parameter step and does not give a learning rate. The inventory method cell is filled for COMPASS (`lora|sft`) and OTel (`full_finetune`) and is empty for the other three, where the cards do state a procedure.
