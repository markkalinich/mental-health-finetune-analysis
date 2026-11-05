# Jazhyc/Llama-3.1-8B-aims-grpo

## Sources

- https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo — current model card; same text as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/Jazhyc__Llama-3.1-8B-aims-grpo__2026-10-09.md — cached card, sha256 e9a86df39b1062c4cb27e09aefae05006e29ca1f2aa88382cb497f996837ae64
- https://huggingface.co/api/models/Jazhyc/Llama-3.1-8B-aims-grpo — file list, parameter count, and chat template
- https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/config.json — context length 131,072
- https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/system_prompt.txt — system prompt file
- https://arxiv.org/abs/2606.27210 — paper abstract
- https://arxiv.org/html/2606.27210 — paper HTML
- https://huggingface.co/datasets/Jazhyc/aims-safety-intents — training dataset card
- https://huggingface.co/datasets/allenai/wildguardmix — source of the AIMS prompts; gated
- https://jazhyc.github.io/aims-safety — project page linked from the paper
- https://github.com/jazhyc/aims-safety — GitHub Pages repository
- https://github.com/Jazhyc/aims-safety-classification — training code; GRPO script is on the `grpo` branch
- https://arxiv.org/abs/2406.18495 — WildGuard paper, listed by URL only

## Record

The training set is `Jazhyc/aims-safety-intents`. The dataset card says it "contains 1,724 annotated prompts" derived from WildGuardMix, with a train split of 1,378, validation 173, and test 173. The Hub dataset is public and the card shows a `load_dataset` example, so it loads. Intents and harm labels are human-written. The prompts come from WildGuardMix (`allenai/wildguardmix`), whose card says the data are "synthetic data (87%), in-the-wild user-LLLM interactions (11%), and existing annotator-written data (2%)." That file is gated, so it does not load without accepting the AI2 terms. Provenance of the training rows is mixed.

This checkpoint was trained with GRPO. The card says: "It is trained with GRPO (Group Relative Policy Optimization), using a reward that explicitly verifies intent faithfulness against the AIMS human annotations." It also says "full fine-tune, not an adapter" and "GRPO starts from the base instruct model." The paper says "GRPO is initialized directly from Llama-3.1-8B-Instruct" and, for all GRPO runs, learning rate 10^-6, prompt batch size 128, and 10 epochs. The `grpo/train.sh` script on `Jazhyc/aims-safety-classification` repeats those three values and does not set a step count. LoRA rank and alpha are not stated. The SFT and DPO models in the same paper are separate checkpoints and use QLoRA. The paper does not say whether this GRPO run quantized the base.

The parent is `meta-llama/Llama-3.1-8B-Instruct` on the card and in the paper. The Hub API reports 8,030,261,248 parameters.

The card presents a classifier: "an intent-aware, reasoning-based safety classifier." It does not claim therapy or mental-health support. The caution is about moderation, not therapy: "Do not treat its output as a sole authority for high-stakes moderation decisions." Harmful-class F1 on this model is 0.863 WildGuardTest, 0.958 XSTest, 0.808 AEGIS 2.0, 0.743 ToxicChat, 0.809 OpenAI Mod, average 0.836.

The usage example classifies the text "How do I pick a lock?" A chat template is in `chat_template.jinja`. The system prompt in the card tells the model to emit a reasoning trace, an intent, and `Harm: harmful` or `Harm: safe`. `generation_config.json` sets temperature 0.6, top_p 0.9, and do_sample true. The card's example instead uses greedy decoding and max_new_tokens 512. `config.json` sets max_position_embeddings to 131,072. The license is `llama3.1`.
