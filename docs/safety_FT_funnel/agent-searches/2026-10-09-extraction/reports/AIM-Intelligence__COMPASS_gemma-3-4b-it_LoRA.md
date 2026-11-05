# AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA

## Sources

- https://huggingface.co/AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA/raw/main/README.md — current model card; byte-identical to the cached card
- https://huggingface.co/api/models/AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA — repository file list, pipeline tag, and parameter count
- https://huggingface.co/AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA/raw/main/config.json — Gemma 3 config with a vision tower; text context 131072
- https://huggingface.co/AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA/raw/main/tokenizer_config.json — tokenizer config; no chat_template key
- https://huggingface.co/AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA/raw/main/chat_template.jinja — chat template with an image branch
- https://huggingface.co/AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA/raw/main/generation_config.json — missing (HTTP 404)
- https://huggingface.co/AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA/raw/main/adapter_config.json — missing (HTTP 404)
- https://arxiv.org/abs/2601.01836 — paper abstract
- https://arxiv.org/html/2601.01836 — paper HTML, including Appendix G.3
- https://github.com/AIM-Intelligence/COMPASS — evaluation-code repository linked from the paper
- https://huggingface.co/datasets/AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset — training dataset card and viewer
- https://huggingface.co/datasets/AIM-Intelligence/COMPASS-Policy-aware-SFT — id written on the card; redirects to the dataset above
- https://huggingface.co/google/gemma-3-4b-it — parent card; usage example sends an image

## Record

The training set is the same 4,121 English query–response pairs. The card names `AIM-Intelligence/COMPASS-Policy-aware-SFT`. That address redirects to `AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset`, which loads. The card says: "Responses were selected from model outputs that achieved full policy adherence under COMPASS evaluation." Provenance is synthetic. TelePath is held out. Seven domains are used for training.

The objective is supervised fine-tuning. Appendix G.3 says: "The SFT dataset comprises 4,121 query-response pairs from the remaining 7 domains, where responses were selected from outputs achieving full policy adherence in our main experiments." The update scope is LoRA on an 8-bit base. The card says "Method: LoRA adapters" and "Quantization: 8-bit during training." For this checkpoint the paper states rank 32, alpha 64, and peak learning rate 3e-4. The card matches those values, plus 3 epochs, batch size 32, AdamW, and a cosine schedule. No source states a step count. No source states whether the adapter was merged. The repository contains two full safetensors shards (4,300,079,472 BF16 parameters) and no `adapter_config.json`. The GitHub repository has no training script for this checkpoint. On held-out TelePath, the card reports Policy Alignment Scores of 86.67, 94.29, 60.00, and 62.24. The base system prompt on the same table is 100.00, 87.62, 28.00, and 0.00.

The card names the parent `google/gemma-3-4b-it`. Appendix G.3 names "Gemma-3-4B-it" with this checkpoint's rank, alpha, and learning rate. The paper does not print the repository id. It does print this card's TelePath scores. The Hub file list reports 4,300,079,472 parameters. The card does not state a license.

The card describes a policy-adherence adapter, not a chatbot and not a classifier: "This repository provides a LoRA adapter trained for organization-specific policy adherence in the COMPASS framework." There is no mental-health support claim. There is no warning sentence about therapy, counseling, diagnosis, or medical advice. The card's only extra note is that fine-tuning may trade off some Allowed Base performance.

Input is not text-only. The parent card's usage example includes an image: `{"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"}`. This repository's Hub pipeline tag is image-text-to-text, and the chat template has an image branch. The template does not set a system prompt. `use_default_system_prompt` is false. Context length in `text_config` is 131,072. There is no `generation_config.json` and this card gives no generation example.
