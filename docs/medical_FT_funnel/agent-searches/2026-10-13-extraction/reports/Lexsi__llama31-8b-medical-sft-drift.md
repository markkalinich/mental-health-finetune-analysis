# Lexsi/llama31-8b-medical-sft-drift

## Sources

https://huggingface.co/Lexsi/llama31-8b-medical-sft-drift — public model page; text matches the cached card
https://huggingface.co/Lexsi/llama31-8b-medical-sft-drift/raw/main/README.md — raw card; 401, repository is gated
https://huggingface.co/api/models/Lexsi/llama31-8b-medical-sft-drift — file list, base model, parameter count, and chat template
https://github.com/Lexsi-Labs/SafeTune — library linked from the card; README does not name this checkpoint
https://arxiv.org/abs/2609.22153 — SafeTune abstract
https://arxiv.org/html/2609.22153 — SafeTune HTML full text
https://safetune.lexsi.ai/ — project site
https://huggingface.co/collections/Lexsi/safetune-drift-checkpoints — collection that lists this checkpoint

## Record

The card says the training data is "medical data" and does not name a dataset. The inventory row names ChatDoctor-HealthCareMagic-100k. The card, the SafeTune README, and the paper HTML do not name that dataset for this repository. No example count, language, or provenance is stated for the data this checkpoint used.

The objective is supervised fine-tuning. The card says "`meta-llama/Llama-3.1-8B-Instruct` fine-tuned (SFT) on medical data." The card does not say whether the update was full or LoRA, and it does not give rank, epochs, learning rate, or batch size. The repository ships four BF16 weight shards and no `adapter_config.json`. Raw `config.json` returned 401, so those files were not read. The SafeTune paper's Appendix B says every drifted checkpoint in that study used "LoRA, rank r=16, α=32", one epoch, learning rate 2×10⁻⁵, and batch 2×8. Table 4 says those numbers were "reproduced via the released drifted checkpoints." The paper HTML does not print `Lexsi/llama31-8b-medical-sft-drift`, so that recipe is not recorded here as a fact about this repository.

The parent is meta-llama/Llama-3.1-8B-Instruct. The card and the Hub API `base_model` field both say that. The Hub API reports 8,030,261,248 BF16 parameters. The title says Llama-3.1-8B.

The use claim is weak. The card says the fine-tune is "on medical data" and that "SafeTune uses this checkpoint to measure drift and to test recovery methods." It does not say the model gives medical advice. The warning is an explicit ban on deployment: "Do not deploy it in a production, user-facing, or agentic system (LSAL Section 4)." Lexsi's changes are under LSAL v1.2. The base weights stay under the Llama 3.1 Community License. The card reports no scores. The paper's Table 4, which does not print this repository id, lists an L8 medical refusal-aggregate change of −23.8 percentage points, and says HarmBench was 0.795 and AdvBench 0.221 on that L8/medical checkpoint.

The purpose is stated. "This checkpoint is a research artifact released with SafeTune for reproducing safety-drift and recovery experiments." The license sentence says the modifications are "free for academic research and teaching," so the audience is a researcher or developer. No clinical function is claimed. The function list is empty.

No clinical task is named. The specialty is general: the card says "medical data" and does not name a field. The usage example is an ordinary chat reply about a hash function.

The example runs on text only. The Hub API embeds a Llama 3.1 chat template. With no system message, the template still writes "Cutting Knowledge Date: December 2023" and "Today Date: 26 Jul 2024." The example sets `max_new_tokens=256` and `do_sample=False`. Context length was not read because `config.json` returned 401.
