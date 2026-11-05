# zrwang1211/SafeAtlas-Guard-8B

## Sources

https://huggingface.co/zrwang1211/SafeAtlas-Guard-8B/raw/main/README.md — current model card; same text as the cached card (sha256 1d31e085d4beadbb48b57216df9478e44cc75d1edd2ddbbc0c08a4154881ae75)
https://huggingface.co/api/models/zrwang1211/SafeAtlas-Guard-8B — file list and 8,767,123,696 BF16 parameters
https://huggingface.co/zrwang1211/SafeAtlas-Guard-8B/raw/main/config.json — Qwen3-VL config, hidden size 4096, context 262144
https://huggingface.co/zrwang1211/SafeAtlas-Guard-8B/raw/main/generation_config.json — temperature 0.7, top_k 20, top_p 0.8, do_sample true
https://huggingface.co/zrwang1211/SafeAtlas-Guard-8B/raw/main/prompts/response_system.txt — response-target system prompt
https://huggingface.co/zrwang1211/SafeAtlas-Guard-8B/raw/main/chat_template.jinja — present; content also returned in the model API
https://arxiv.org/abs/2608.29098 — SafeAtlas-VL abstract
https://arxiv.org/html/2608.29098 — HTML full text; names the 8B SafeAtlas Guard and its training time
https://github.com/zrwang1211/SafeAtlas-VL/blob/main/training/stage1/safeatlas_guard_8b.yaml — full SFT config
https://github.com/zrwang1211/SafeAtlas-VL/blob/main/training/stage2/safeatlas_guard_8b.json — frozen-backbone head config, hidden size 4096
https://huggingface.co/api/datasets/zrwang1211/SafeAtlas-VL — gated dataset; 1,000,000 training annotations in this release
https://huggingface.co/datasets/zrwang1211/SafeAtlas-VL/raw/main/README.md — HTTP 401
https://huggingface.co/collections/zrwang1211/safeatlas-guard — collection named by the paper

## Record

The training set is zrwang1211/SafeAtlas-VL. The dataset API says this release has 1,000,000 training annotations over 594,487 images. The paper says the full training set has 1,503,284 instances from real-world and synthetic sources. The dataset README returned HTTP 401, so it does not load without access. No language is stated.

Stage 1 is full-parameter SFT. The 8B YAML sets model_name_or_path to Qwen/Qwen3-VL-8B-Instruct, stage sft, finetuning_type full, learning rate 5.0e-5, one epoch, per-device batch size 4, gradient accumulation 4, cutoff 8192, bf16 true, and DeepSpeed ZeRO-1. The paper says this stage takes about 24 hours on 8 H200 GPUs. Stage 2 freezes that backbone and trains the ordinal head, the 16-way category head, and three teacher heads for one epoch, about 20 hours for the 8B model. The paper sets the head learning rate to 1e-4. The stage-2 JSON sets learning_rate_head to 0.0005. No LoRA rank is stated. The heads stay in ordinal_heads.safetensors. No step count is stated.

The card, the YAML, and the paper name Qwen/Qwen3-VL-8B-Instruct. The API counts 8,767,123,696 BF16 parameters in the backbone shards.

This is a classifier. The response prompt says "You are a multimodal safety classifier" and "Judge ONLY the AI assistant response." The card says it "evaluates image content, image-grounded user requests, and assistant responses." The quickstart passes an image, a request, and a reply. Outputs are one of five labels, from "safe core" to "unsafe core", one harm category or none, and a risk score from 0 to 100. The prompt says "Do not output explanations." The card's overall unsafe-class F1 average is 80.90. The abstract says the 8B model outperforms the previous state of the art by about 4% F1. The paper's soft-ordinal ablation reports 81.2 for the 8B model.

Text-only benchmarks are on the card, including HarmBench prompt F1 94.60. generation_config.json sets do_sample true, temperature 0.7, top_k 20, and top_p 0.8. Model context is 262144. No license is on the current model card. The paper names the 8B SafeAtlas Guard. It does not print the string zrwang1211/SafeAtlas-Guard-8B.
