# art87able/unstuck-qwen2.5-0.5b-steps

## Sources

- https://huggingface.co/art87able/unstuck-qwen2.5-0.5b-steps/raw/main/README.md — current model card (same text as the 5 Oct cache)
- revision_3_experiments/hf_inventory/cache/readmes/art87able__unstuck-qwen2.5-0.5b-steps__2026-10-05.md — cached card, sha256 d99090163b6dffb2f443dd69ff085ad2e8861d739031130b27d2ae463bf4521b
- https://huggingface.co/api/models/art87able/unstuck-qwen2.5-0.5b-steps — file list, safetensors count, chat template
- https://huggingface.co/art87able/unstuck-qwen2.5-0.5b-steps/raw/main/config.json — architecture and context length
- https://huggingface.co/art87able/unstuck-qwen2.5-0.5b-steps/raw/main/generation_config.json — sampling settings
- https://github.com/art87able/unstuck — app repository
- https://github.com/art87able/unstuck/blob/main/scripts/finetune/modal_finetune.py — script that trains and uploads this repo
- https://github.com/art87able/unstuck/blob/main/scripts/finetune/nebius_finetune.py — a different Nebius job, base Qwen2.5-1.5B, not this checkpoint
- https://huggingface.co/datasets/art87able/unstuck-sft-breakdowns — 130-row training set; viewer shows the rows
- https://huggingface.co/blog/art87able/building-unstuck-small — author write-up that names this checkpoint
- https://huggingface.co/spaces/build-small-hackathon/unstuck — live app

## Record

The training set is 130 synthetic instruction-to-JSON pairs, hub id `art87able/unstuck-sft-breakdowns`. The dataset card says they were "distilled from a strong serverless model (`Qwen/Qwen3-30B-A3B-Instruct-2507` on Nebius Token Factory)" and "Purely synthetic; no user data." The same card says the set was "Used to train `art87able/unstuck-qwen2.5-0.5b-steps`." The Hub page lists 130 rows and the viewer displays them, so the dataset loads. Language on the dataset card is English.

The objective is supervised fine-tuning. The dataset card titles the set "Unstuck — task-breakdown SFT set" and says the pairs "teach a small model" this JSON task. The script that sets `HF_REPO = "art87able/unstuck-qwen2.5-0.5b-steps"` trains with a causal-language-model loss (`task_type="CAUSAL_LM"`, labels on the token ids). "Distilled" in the card is how the 130 rows were written, not a distillation loss. The update is LoRA, not a full fine-tune. The card says "LoRA (r=16, α=32, dropout 0.05; q/k/v/o projections), 3 epochs, lr 2e-4, merged into the base." The script loads `Qwen/Qwen2.5-0.5B-Instruct` in bfloat16 (`torch_dtype=torch.bfloat16`), so the base was not quantized during training, then calls `merge_and_unload()`. Batch size in that script is 4. No step count is stated. The repo has `model.safetensors` and no `adapter_config.json`.

The parent is `Qwen/Qwen2.5-0.5B-Instruct`. The card says "Base: `Qwen/Qwen2.5-0.5B-Instruct`." `config.json` has `"_name_or_path": "Qwen/Qwen2.5-0.5B-Instruct"`. The training script sets the same `BASE`. Those sources agree with the card. `nebius_finetune.py` names `Qwen/Qwen2.5-1.5B-Instruct` for a different upload path, not this repository.

The card presents a JSON task tool, not a chatbot and not a classifier: "it is not a general chat model." The use claim is weak. The title is "fine-tuned for ADHD task breakdowns," which is mental-health related and is not therapy, counseling, or a support conversation. The warning is unrelated limitations only. The card says outputs "should still be schema-validated" and does not forbid therapy, diagnosis, or medical advice. The card states "0.5B" parameters. The Hub file list reports 494,032,768 parameters in `model.safetensors`. License is `apache-2.0`. Language YAML is `en`. Inventory methods `lora`, datasets `130 schema-valid breakdowns`, and parent `Qwen/Qwen2.5-0.5B-Instruct` all match the card. The only reported number for this checkpoint is "Final train loss ≈ 0.21." The blog adds that the tuned model "produces schema-valid breakdowns at 60× fewer parameters than the teacher."

Serving is text in, text out. The usage block loads `AutoTokenizer` and says "Feed it Unstuck's breakdown prompt [...] and parse the JSON." `config.json` is `Qwen2ForCausalLM` with `max_position_embeddings` 32768. A chat template is present in `tokenizer_config` (returned by the model API). Its fallback system line is "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." `generation_config.json` sets `do_sample` true, temperature 0.7, top_p 0.8, top_k 20, repetition_penalty 1.1. It does not set `max_new_tokens`.
