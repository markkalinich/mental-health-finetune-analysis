# AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA

## Sources

- https://huggingface.co/AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA/raw/main/README.md — current model card; byte-identical to the cached card
- https://huggingface.co/api/models/AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA — repository file list and parameter count
- https://huggingface.co/AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA/raw/main/config.json — model config, context length 32768
- https://huggingface.co/AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA/raw/main/tokenizer_config.json — tokenizer config; no chat_template key
- https://huggingface.co/AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA/raw/main/chat_template.jinja — chat template and default system prompt
- https://huggingface.co/AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA/raw/main/generation_config.json — missing (HTTP 404)
- https://huggingface.co/AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA/raw/main/adapter_config.json — missing (HTTP 404)
- https://arxiv.org/abs/2601.01836 — paper abstract
- https://arxiv.org/html/2601.01836 — paper HTML, including Appendix G.3
- https://github.com/AIM-Intelligence/COMPASS — evaluation-code repository linked from the paper; README states acceptance at ACL 2026
- https://huggingface.co/datasets/AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset — training dataset card and viewer
- https://huggingface.co/datasets/AIM-Intelligence/COMPASS-Policy-aware-SFT — card-body link; redirects to the dataset id above
- https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/raw/main/README.md — parent card text-only quickstart

## Record

The training set is 4,121 English query–response pairs in `AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset`. The card says: "Responses were selected from model outputs that achieved full policy adherence under COMPASS evaluation." The dataset card says the same and shows a viewer, so the dataset loads. The Hub dataset metadata lists language `en`. Provenance is synthetic. Leave-one-domain-out training uses seven domains and holds out TelePath. The card body links `AIM-Intelligence/COMPASS-Policy-aware-SFT`, which redirects to the dataset id above.

The objective is supervised fine-tuning. Appendix G.3 says: "The SFT dataset comprises 4,121 query-response pairs from the remaining 7 domains, where responses were selected from outputs achieving full policy adherence in our main experiments." The update scope is LoRA on an 8-bit base. The card says "Method: LoRA adapters" and "Quantization: 8-bit during training." Rank 64, alpha 128, 3 epochs, peak learning rate 5e-4, batch size 32, AdamW, cosine schedule. No source states a step count. No source states whether the adapter was merged. The repository contains four full safetensors shards (7,615,616,512 BF16 parameters) and no `adapter_config.json`, while the card calls the repository a LoRA adapter. The GitHub repository is the evaluation toolkit. It has no training script for this checkpoint. On held-out TelePath, the card reports Policy Alignment Scores of 96.67, 89.52, 71.74, and 60.49 for allowed base, allowed edge, denied base, and denied edge.

The card names the parent `Qwen/Qwen2.5-7B-Instruct`. Appendix G.3 names the same base: "peak LR 5×10−4 for Qwen2.5-7B-Instruct." The paper does not print the repository id `AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA`. It does print this card's TelePath scores and these hyperparameters for the Qwen2.5-7B-Instruct LoRA run. The Hub file list reports 7,615,616,512 parameters. The card does not state a license.

The card describes a policy-adherence adapter, not a chatbot and not a classifier: "This repository provides a LoRA adapter trained for organization-specific policy adherence in the COMPASS framework." There is no mental-health support claim. There is no warning sentence about therapy, counseling, diagnosis, or medical advice.

The parent card's quickstart runs a text prompt: `prompt = "Give me a short introduction to large language model."` This repository's `chat_template.jinja` defaults to "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." Context length in `config.json` is 32,768. There is no `generation_config.json` and the card gives no generation example.
