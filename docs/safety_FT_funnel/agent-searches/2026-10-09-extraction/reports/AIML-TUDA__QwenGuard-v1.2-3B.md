# AIML-TUDA/QwenGuard-v1.2-3B

## Sources

- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/README.md — current model card; byte-identical to the cached card
- https://huggingface.co/api/models/AIML-TUDA/QwenGuard-v1.2-3B — repository file list and parameter count
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/config.json — Qwen2.5-VL config; context length 128000; parent path
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/generation_config.json — sampling settings
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/tokenizer_config.json — chat template; model_max_length 16384
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/chat_template.json — default system line
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/trainer_state.json — logged epochs, steps, batch size, learning rate
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/trainer_log.jsonl — step log; total_steps 136; peak lr 5e-5
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/train_results.json — train loss
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/eval_results.json — eval loss
- https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-3B/raw/main/all_results.json — combined trainer summary
- https://arxiv.org/abs/2406.05113 — paper abstract
- https://arxiv.org/html/2406.05113 — paper HTML, including Table 3 and Appendix B
- https://github.com/ml-research/LlavaGuard — training repository linked from the card
- https://raw.githubusercontent.com/ml-research/LlavaGuard/main/scripts/train/QwenGuard2.5-v1.2/QwenGuard2.5-v1.2-3b.yaml — 3B training config; numbers differ from this repository's trainer log
- https://ml-research.github.io/human-centered-genai/projects/llavaguard/index.html — project page; does not name this repository
- https://huggingface.co/api/datasets/AIML-TUDA/LlavaGuard — dataset metadata; language en; gated
- https://huggingface.co/datasets/AIML-TUDA/LlavaGuard/raw/main/README.md — dataset card body; HTTP 401

## Record

The card says this checkpoint "is trained on LlavaGuard-DS" and names `AIML-TUDA/LlavaGuard`. That dataset is gated. Its README returned HTTP 401, so it did not load here. The dataset API lists language `en` and size category 1K to 10K. No row count was readable. The paper says the LlavaGuard set has 5,466 unique samples, with 4,571 for training before oversampling. Provenance is mixed. The paper says: "During the tuning process of LlavaGuard models, human supervision was applied solely to category and rating entries, while the rationales were generated synthetically." Images come from SMID plus web-scraped search results. The paper does not say that this v1.2 repository used that exact split.

No sentence in this repository names a loss. `trainer_state.json` records `num_train_epochs` 2, `global_step` 136, `train_batch_size` 5, and a logged learning rate that peaks at 5e-5. The run ends at epoch 1.978. `eval_results.json` reports eval loss 0.6955. The card tag list includes `freeze`. The GitHub file `QwenGuard2.5-v1.2-3b.yaml` says `stage: sft`, `finetuning_type: full`, `freeze_vision_tower: true`, learning rate 1.0e-5, and 3 epochs. Those settings do not match this repository's trainer log, so they are not recorded as this checkpoint's objective or update scope. Appendix B of the paper gives yet another recipe, 3 epochs at 2e-5 with batch size 1, and it names the 0.5B and 7B models, not this repository. There is no LoRA rank and no `adapter_config.json`. The weights are two full safetensors shards (3,754,622,976 BF16 parameters).

The card says the model "builds upon Qwen/Qwen2.5-VL-3B-Instruct." `config.json` has the same `_name_or_path`. The paper says the 3B and 7B QwenGuard variants are "built upon the Qwen2.5-VL models of matching scale." It never prints `AIML-TUDA/QwenGuard-v1.2-3B` or `QwenGuard-v1.2-3B`. Table 3 reports QwenGuard-3B at balanced accuracy 88.72, recall 87.78, precision 86.81, and policy exception score 84.74. The card's citation names ICML and calls it the 41st conference. The model card states no license.

The card presents a vision safeguard, not a conversation partner: "providing safety rating, safety category and a rationale." That is a label plus a category. The policy text on the card includes self-harm and "discussions on mental health challenges," so the mental-health claim is weak: this is a safety rater, not a support conversation. The access gate says: "LlavaGuard is mainly targeted toward researchers and is meant to be used in research."

Input is not text-only. The card's example sends an image: `https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg`, plus the policy text. The chat template's default system line is "You are a helpful assistant." `generation_config.json` sets temperature 0.1, top_p 0.001, top_k 1, repetition_penalty 1.05, and do_sample true. The example uses max_new_tokens 128. Config context length is 128,000. The tokenizer's `model_max_length` is 16,384.
