# zrwang1211/SafeAtlas-Guard-2B

## Sources

- https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/README.md — current model card; identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/zrwang1211__SafeAtlas-Guard-2B__2026-10-09.md — cached card, sha256 b8c8e28cc88a7f877af748e985594a6d16c88aa7630b5d3e66e55a62505270f3
- https://huggingface.co/api/models/zrwang1211/SafeAtlas-Guard-2B — file list, chat template, backbone parameter count
- https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/config.json — architecture and max position embeddings 262144
- https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/generation_config.json — sampling settings
- https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/tokenizer_config.json — no chat_template key; model_max_length 262144
- https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/chat_template.jinja — chat template file
- https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/ordinal_config.json — five labels, heads, prompt file names
- https://huggingface.co/zrwang1211/SafeAtlas-Guard-2B/raw/main/prompts/response_system.txt — response system prompt used by the quickstart
- https://arxiv.org/abs/2608.29098 — abstract
- https://arxiv.org/html/2608.29098 — HTML full text
- https://github.com/zrwang1211/SafeAtlas-VL — code repository
- https://raw.githubusercontent.com/zrwang1211/SafeAtlas-VL/main/README.md — inference and training overview
- https://raw.githubusercontent.com/zrwang1211/SafeAtlas-VL/main/training/README.md — two-stage training and batch sizes
- https://raw.githubusercontent.com/zrwang1211/SafeAtlas-VL/main/training/stage1/safeatlas_guard_2b.yaml — stage-1 full SFT config
- https://raw.githubusercontent.com/zrwang1211/SafeAtlas-VL/main/training/stage2/safeatlas_guard_2b.json — stage-2 head config
- https://huggingface.co/datasets/zrwang1211/SafeAtlas-VL — dataset card; gated
- https://huggingface.co/api/datasets/zrwang1211/SafeAtlas-VL — gated: auto
- https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct/raw/main/README.md — parent quickstart, which passes an image
- https://huggingface.co/collections/zrwang1211/safeatlas-guard — model collection

## Record

The training set named for this checkpoint is SafeAtlas-VL (`zrwang1211/SafeAtlas-VL`). The paper says: "SafeAtlas-VL contains 1,503,284 training instances over 746,895 unique images." It also says the data come "from both real-world and synthetic sources," so the mix is real images plus generated images, requests, and responses. The Hub dataset card and `training/stage2/safeatlas_guard_2b.json` both say 1,000,000 training annotations, and the card says the complete set will be released later. The dataset page requires an access form (`gated: auto`), so it does not load here. No source states the language of the text fields.

Stage 1 is supervised fine-tuning of every parameter. The paper names the loss: "The instruction tuning objective maximizes the conditional likelihood of the complete structured judgment... L_SFT = -E_i log P_theta(Y_i | A_tau_i, x_i)." The card says: "Stage 1 performs full-parameter multimodal instruction tuning." The 2B stage-1 config sets `finetuning_type: full`, `learning_rate: 5.0e-5`, `num_train_epochs: 1.0`, and `per_device_train_batch_size: 4` with gradient accumulation 4. Paper Table A4 matches that: one epoch, learning rate 5×10^-5, batch size per device 4, BF16, eight H200 GPUs. No source states a step count. Stage 2 freezes that backbone and trains a five-level ordinal head, a 16-way category head, and three teacher heads for one epoch. Paper Table A5 gives a prediction-head learning rate of 1×10^-4 and a per-device batch of 8. The stage-2 JSON instead sets `learning_rate_head` to 0.0005 and `num_train_samples` to 1000000. No LoRA rank, alpha, or adapter file is stated. Training precision is BF16, not a quantized base.

The parent is Qwen/Qwen3-VL-2B-Instruct. The card says: "SafeAtlas Guard 2B uses Qwen3-VL-2B-Instruct as its multimodal backbone." The stage-1 config sets `model_name_or_path: Qwen/Qwen3-VL-2B-Instruct`. The paper says the same 2B Instruct backbone. The card calls the model 2B. The Hub file list reports 2,127,532,032 BF16 parameters in `model.safetensors`; the ordinal heads are a separate FP32 file and are not in that count.

This is a classifier, not a chatbot. The response prompt begins: "You are a multimodal safety classifier." The card says the model returns one of five ordered safety levels, a risk score from 0 to 100, and three auxiliary judge predictions. There is no mental-health or therapy claim. The card says: "SafeAtlas Guard is intended for multimodal safety moderation, ordinal risk assessment, red-teaming, evaluation, and safety alignment research." The warning does not mention therapy or medical advice. It says: "The model and associated resources must not be used to facilitate harmful activity or to target individuals or protected groups." No license is stated on the card or the model API. The paper names this checkpoint "SafeAtlas Guard-2B" and does not print the repository id. The GitHub README does print `zrwang1211/SafeAtlas-Guard-2B`.

The quickstart passes an image: `image="examples/example.jpg"`. The parent card's only chat example also passes an image. A chat template is present in `chat_template.jinja`. The stored system prompt is `prompts/response_system.txt`, because the quickstart uses `target_name="response"`. Image and request prompts are separate files. `generation_config.json` sets `do_sample` true, temperature 0.7, top_k 20, and top_p 0.8. `max_position_embeddings` and `model_max_length` are 262144. The card reports an overall unsafe-class F1 of 80.43 across 11 tasks. The paper's table lists SafeAtlas Guard-2B at 80.5 on those 11 tasks.
