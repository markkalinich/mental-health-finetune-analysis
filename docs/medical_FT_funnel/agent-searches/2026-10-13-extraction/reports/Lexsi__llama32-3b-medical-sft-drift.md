# Lexsi/llama32-3b-medical-sft-drift

## Sources

https://huggingface.co/Lexsi/llama32-3b-medical-sft-drift — public model page; text matches the cached card
https://huggingface.co/Lexsi/llama32-3b-medical-sft-drift/raw/main/README.md — raw card; 401, repository is gated
https://huggingface.co/api/models/Lexsi/llama32-3b-medical-sft-drift — file list, base model, parameter count, and chat template
https://github.com/Lexsi-Labs/SafeTune — library linked from the card; README does not name this checkpoint
https://arxiv.org/abs/2609.22153 — SafeTune abstract
https://arxiv.org/html/2609.22153 — SafeTune HTML full text
https://safetune.lexsi.ai/ — project site
https://huggingface.co/collections/Lexsi/safetune-drift-checkpoints — collection that lists this checkpoint

## Record

The card says the training data is "medical data" and does not name a dataset. The inventory row names ChatDoctor-HealthCareMagic-100k. The card, the SafeTune README, and the paper HTML do not name that dataset for this repository. No example count, language, or provenance is stated on the card.

The objective is supervised fine-tuning. The card says "`meta-llama/Llama-3.2-3B-Instruct` fine-tuned (SFT) on medical data." The card does not say whether the update was full or LoRA, and it does not give rank, epochs, learning rate, or batch size. The repository ships two BF16 weight shards and no `adapter_config.json`. Raw `config.json` returned 401. The SafeTune paper's Appendix B says every drifted checkpoint in that study used "LoRA, rank r=16, α=32", one epoch, learning rate 2×10⁻⁵, and batch 2×8. The paper HTML does not print `Lexsi/llama32-3b-medical-sft-drift`, so that recipe is not recorded here as a fact about this repository.

The parent is meta-llama/Llama-3.2-3B-Instruct. The card and the Hub API `base_model` field both say that. The Hub API reports 3,212,749,824 BF16 parameters. The model page says 3B.

The use claim is weak. The card says the fine-tune is "on medical data" and that "SafeTune uses this checkpoint to measure drift and to test recovery methods." It does not say the model gives medical advice. The warning is an explicit ban on deployment: "Do not deploy it in a production, user-facing, or agentic system (LSAL Section 4)." Lexsi's changes are under LSAL v1.2. The base weights stay under the Llama 3.2 Community License. The card reports no scores. The paper does not print this repository id. Table 4 lists an L3 medical refusal-aggregate change of −15.7 percentage points. Section 7.2 is a separate case study: "Fine-tuning a Llama-3.2-3B clinical assistant on 8,000 patient-doctor consultations" held MedMCQA near baseline and cut HarmBench refusal from 87.0% to 57.5%.

The purpose is stated. "This checkpoint is a research artifact released with SafeTune for reproducing safety-drift and recovery experiments." The license sentence says the modifications are "free for academic research and teaching," so the audience is a researcher or developer. No clinical function is claimed. The function list is empty.

No clinical task is named on the card. The specialty is general: the card says "medical data" and does not name a field. The usage example is an ordinary chat reply about a hash function.

The example runs on text only. The file list also contains `preprocessor_config.json`, which was not readable because the repository is gated. The Hub API embeds a Llama 3.2 chat template. With no system message, the template still writes "Cutting Knowledge Date: December 2023" and "Today Date: 26 Jul 2024." The example sets `max_new_tokens=256` and `do_sample=False`. Context length was not read because `config.json` returned 401.
