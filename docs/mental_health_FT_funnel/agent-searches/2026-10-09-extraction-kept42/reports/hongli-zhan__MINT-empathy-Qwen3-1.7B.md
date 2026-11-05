# hongli-zhan/MINT-empathy-Qwen3-1.7B

## Sources

- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-1.7B/raw/main/README.md — current model card; same text as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/hongli-zhan__MINT-empathy-Qwen3-1.7B__2026-10-05.md — cached card, sha256 f61fbed3910fbb271db49e9dfa3914867f3845f0f3eabda76c1d2ea2dc087d0c
- https://huggingface.co/api/models/hongli-zhan/MINT-empathy-Qwen3-1.7B — file list, safetensors count, chat template
- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-1.7B/raw/main/config.json — architecture and max position embeddings
- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-1.7B/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-1.7B/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-1.7B/blob/main/chat_template.jinja — Qwen3 chat template
- https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-1.7B/commit/2837c0efc88323d6995aaa8b1b47c9bf6aa53f50 — upload commit that names global_step_190
- https://arxiv.org/abs/2604.11742 — paper abstract
- https://arxiv.org/html/2604.11742 — paper HTML full text
- https://github.com/honglizhan/mint-empathy — code, data, and the released checkpoint id
- https://github.com/honglizhan/mint-empathy/blob/main/training/scripts/example_run_quality_plus_diversity.sh — GRPO launcher; default base is Qwen/Qwen3-1.7B and lora_rank is 0
- https://github.com/honglizhan/mint-empathy/blob/main/data/training/conversations_322.json — released training conversations
- https://github.com/volcengine/verl — VERL, named on the card as the GRPO library
- https://honglizhan.github.io/mint-empathy/ — project page
- https://www.microsoft.com/en-us/research/publication/discourse-diversity-in-multi-turn-empathic-dialogue/ — Microsoft Research publication page for the same paper
- https://huggingface.co/Qwen/Qwen3-1.7B/raw/main/README.md — parent card, text quickstart, stated size 1.7B
- https://huggingface.co/datasets/allenai/WildChat-1M — WildChat Hub dataset
- https://huggingface.co/api/datasets/allenai/WildChat-1M — WildChat is public, not gated, train split present
- https://github.com/microsoft/sense-7 — SENSE-7 dataset README and xlsx; no Hub dataset

## Record

The training set is 322 English multi-turn emotional-support conversations, 1,719 supporter turns, filtered from WildChat and SENSE-7. The paper says: "Our training data comes from two complementary sources of real user–LLM interactions: WildChat (Zhao et al., 2024) and SENSE-7 (Suh et al., 2026)." The same authors release that file as `data/training/conversations_322.json`. WildChat on the Hub is `allenai/WildChat-1M` (human users and ChatGPT; the card says 1 million conversations; the train split lists 837,989 rows) and it loads. The paper does not say how many of the 322 rows came from WildChat. SENSE-7 is the GitHub xlsx at microsoft/sense-7, not a Hub dataset, so it does not load from the Hub. The paper does not state a SENSE-7 conversation count or language.

The objective is GRPO. The card says "GRPO via VERL." The paper says: "Training is implemented in VERL (Sheng et al., 2025) with GRPO. Unless otherwise noted, we train for 3 epochs with a generation temperature of 1.0, a batch size of 24 prompts (with N=8 rollouts per prompt), KL penalty β=0.01, and a learning rate of 1 × 10−6." The released launcher defaults to those values, `MODEL_PATH` `Qwen/Qwen3-1.7B`, and `actor_rollout_ref.model.lora_rank=0`, so the update is of the full model, not a LoRA adapter. The repo has one `model.safetensors` and no `adapter_config.json`. The upload commit titles the file "global_step_190" and the first README said "Training checkpoint | global_step_190." The current card no longer prints the step, the epoch count, or the batch size. LoRA alpha, whether an adapter was merged, and whether the base was quantized during training are not stated.

The parent is Qwen/Qwen3-1.7B. The card says the checkpoint is "fine-tuned from Qwen/Qwen3-1.7B." The paper says "two base policy models, Qwen3-1.7B and Qwen3-4B." The training script default is `Qwen/Qwen3-1.7B`. Those agree. The paper does not print the string `hongli-zhan/MINT-empathy-Qwen3-1.7B`. The GitHub README does, as "MINT Qwen3 1.7B" linked to that repository id. The parent card says "Number of Parameters: 1.7B." The Hub file list reports 2,031,739,904 parameters in `model.safetensors`.

This is a chatbot for empathic dialogue. The card says it is "for multi-turn empathic dialogue" and "intended for research on empathic dialogue, discourse diversity, and supportive response generation." That is a strong support-conversation claim. The warning is a disclaimer, not a prohibition: "It is a research artifact, not a therapy system." On Lend-an-Ear (315 supporter turns, 50 conversations) the card says aggregate empathy moves from 3.60 to 4.54, and tactic stickiness stays 0.51. Table 2 of the paper has the same 4.54 and 0.51 for Qwen-3 1.7B, method Q + D_KL. No Hub dataset page for Lend-an-Ear turned up. License is mit.

Serving is text in, text out. The parent quickstart sets `prompt = "Give me a short introduction to large language model."` and calls `model.generate`. This card only shows `from_pretrained`. A chat template is present in `chat_template.jinja`. No system prompt is written down. `generation_config.json` sets `do_sample` true, temperature 0.6, top_k 20, top_p 0.95. `config.json` sets `max_position_embeddings` to 40960. The parent card says context length 32,768. The tokenizer `model_max_length` is 131072.
