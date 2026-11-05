# zrwang1211/SafeAtlas-Guard-2B

## Sources

https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/README.md — current model card; same text as the cached card (sha256 b8c8e28cc88a7f877af748e985594a6d16c88aa7630b5d3e66e55a62505270f3)
https://huggingface.co/api/models/zrwang1211/SafeAtlas-Guard-2B — file list and 2,127,532,032 BF16 parameters
https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/config.json — Qwen3-VL config, context 262144
https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/generation_config.json — temperature 0.7, top_k 20, top_p 0.8, do_sample true
https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/ordinal_config.json — five labels, 16 categories, separate heads file
https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/prompts/response_system.txt — response-target system prompt
https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/prompts/request_system.txt — request-target system prompt
https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/prompts/image_system.txt — image-only system prompt
https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/chat_template.jinja — present; content also returned in the model API
https://arxiv.org/abs/2608.29098 — SafeAtlas-VL abstract
https://arxiv.org/html/2608.29098 — HTML full text; 2B/4B/8B training tables
https://github.com/zrwang1211/SafeAtlas-VL — training/stage1/safeatlas_guard_2b.yaml and training/stage2/safeatlas_guard_2b.json
https://huggingface.co/api/datasets/zrwang1211/SafeAtlas-VL — gated dataset; 1,000,000 training annotations in this release
https://huggingface.co/datasets/zrwang1211/SafeAtlas-VL/raw/main/README.md — HTTP 401
https://huggingface.co/collections/zrwang1211/safeatlas-guard — collection named by the paper

## Record

The training set is zrwang1211/SafeAtlas-VL. The dataset API says this release has 1,000,000 training annotations over 594,487 images, plus a 5,000-annotation test split, and that the complete set will come later. The paper says the full training set has 1,503,284 instances from real-world and synthetic sources. The dataset is gated. Its raw README returned HTTP 401, so it does not load without access. No language is stated.

Stage 1 is full-parameter SFT. The paper says "We perform full-parameter supervised fine-tuning for one epoch." The 2B YAML sets model_name_or_path to Qwen/Qwen3-VL-2B-Instruct, stage sft, finetuning_type full, learning rate 5.0e-5, one epoch, per-device batch size 4, gradient accumulation 4, cutoff 8192, and bf16 true. Stage 2 freezes that backbone and trains the ordinal head, the 16-way category head, and three teacher heads for one epoch. The paper sets the head learning rate to 1e-4 and the threshold learning rate to 1e-3. The stage-2 JSON sets learning_rate_head to 0.0005 and learning_rate_threshold to 0.001. No LoRA rank is stated. The heads stay in ordinal_heads.safetensors. Training is BF16, not a quantized base. No step count is stated.

The card, the YAML, and the paper name Qwen/Qwen3-VL-2B-Instruct. The API counts 2,127,532,032 BF16 parameters in the backbone file.

This is a classifier. The response prompt says "You are a multimodal safety classifier." The card says it "evaluates image content, image-grounded user requests, and assistant responses." The quickstart passes an image, a user request, and an assistant reply, with target_name "response". Separate prompts judge only the image or only the request. Outputs are one of five labels, from "safe core" to "unsafe core", one harm category or none, and a risk score from 0 to 100. The response prompt also asks for three auxiliary judge labels and says "Do not output explanations." The card's overall unsafe-class F1 average is 80.43. The paper's soft-ordinal ablation reports 80.5 for the 2B model.

Text-only benchmarks are on the card, including HarmBench prompt F1 100.00. generation_config.json sets do_sample true, temperature 0.7, top_k 20, and top_p 0.8. Model context is 262144. The guard system prompt is the target prompt, not a line inside the chat template. No license is on the current model card. The paper names the 2B SafeAtlas Guard and the model collection. It does not print the string zrwang1211/SafeAtlas-Guard-2B.
