# hongli-zhan/MINT-empathy-Qwen3-4B

## Sources

- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-4B/raw/main/README.md — current model card; same text as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/hongli-zhan__MINT-empathy-Qwen3-4B__2026-10-05.md — cached card, sha256 c415b00c01e032d57c900adf6441a242dac868495ac7e7385c12c7a8ef5834a9
- https://huggingface.co/api/models/hongli-zhan/MINT-empathy-Qwen3-4B — file list, parameter count, and chat template
- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-4B/raw/main/config.json — architecture and context length
- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-4B/raw/main/generation_config.json — sampling settings
- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-4B/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://arxiv.org/abs/2604.11742 — paper abstract
- https://arxiv.org/html/2604.11742 — paper HTML; does not print this repository id
- https://huggingface.co/papers/2604.11742 — paper abstract on the Hub
- https://github.com/honglizhan/mint-empathy — code README; prints this repository id
- https://github.com/honglizhan/mint-empathy/blob/main/training/scripts/example_run_quality_plus_diversity.sh — GRPO training script
- https://github.com/volcengine/verl — VERL, named on the card as the trainer
- https://honglizhan.github.io/mint-empathy/ — project page
- https://huggingface.co/datasets/allenai/WildChat-1M — WildChat Hub dataset
- https://github.com/microsoft/sense-7/ — SENSE-7 dataset repository; no Hub dataset

## Record

The training set is a filtered mix of WildChat and SENSE-7: 322 English multi-turn emotional-support conversations, 1,719 supporter turns. The paper calls these "real user–LLM interactions," so the text is mixed human and model text. WildChat on the Hub is `allenai/WildChat-1M` (837,989 train rows, public, multilingual). The paper does not print that Hub id. SENSE-7 has no Hub dataset. The paper says 69 of the training conversations are the SENSE-7 subset. The filtered mix itself is not a Hub dataset. Quote: "The resulting dataset contains 322 multi-turn emotional-support conversations totaling 1,719 supporter turns."

The card names the objective GRPO, through VERL. The paper uses the same setup for Qwen3-1.7B and Qwen3-4B: 3 epochs, learning rate 1e-6, batch size 24 prompts, 8 rollouts. The training script sets `lora_rank=0`, so the update is full. Its default `MODEL_PATH` is `Qwen/Qwen3-1.7B`. LoRA alpha and quantization during training are not stated. The weight-upload commit is "Upload MINT Q+D_KL Qwen3-4B (global_step_180)." Quote: "Training is implemented in VERL (Sheng et al., 2025) with GRPO. Unless otherwise noted, we train for 3 epochs ... and a learning rate of 1×10−6."

The card names the parent `Qwen/Qwen3-4B`. The paper names Qwen3-4B as one of the two base policies and does not print this repository id. The GitHub README does print `hongli-zhan/MINT-empathy-Qwen3-4B` as the released 4B checkpoint. The 4B Q + D_KL row in the paper is aggregate empathy 4.67 and tactic stickiness 0.42, the same pair the card reports. The Hub file list reports 4,411,424,256 parameters. The card language tag is English.

This is a chatbot for multi-turn empathic dialogue and supportive responses, so the use claim is Strong. The warning is Disclaimer only. It says the model is not a therapy system, and it does not forbid a use. Quote: "for multi-turn empathic dialogue." Warning quote: "It is a research artifact, not a therapy system." License is mit.

The card's example loads a causal language model and does not pass an image or audio input. The pipeline tag is `text-generation`. `generation_config.json` sets `do_sample` true, temperature 0.6, top_k 20, and top_p 0.95. `config.json` sets `max_position_embeddings` to 40960. The chat template does not add a default system prompt.
