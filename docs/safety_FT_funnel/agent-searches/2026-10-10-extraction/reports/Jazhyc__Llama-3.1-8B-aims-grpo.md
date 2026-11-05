# Jazhyc/Llama-3.1-8B-aims-grpo

## Sources

https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/README.md — current model card; byte-identical to the cached card
revision_3_experiments/hf_inventory/cache/readmes/Jazhyc__Llama-3.1-8B-aims-grpo__2026-10-09.md — cached card, sha256 e9a86df39b1062c4cb27e09aefae05006e29ca1f2aa88382cb497f996837ae64
https://huggingface.co/api/models/Jazhyc/Llama-3.1-8B-aims-grpo — file list and parameter count
https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/config.json — max position embeddings 131072
https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/tokenizer_config.json — no chat_template key; model_max_length 131072
https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/chat_template.jinja — Llama 3.1 chat template
https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo/raw/main/system_prompt.txt — classifier system prompt
https://arxiv.org/abs/2606.27210 — paper abstract
https://arxiv.org/html/2606.27210 — paper HTML; GRPO hyperparameters in Appendix F; does not print this repository id
https://jazhyc.github.io/aims-safety — project page linked from the paper
https://github.com/Jazhyc/aims-safety — GitHub Pages source for that project page
https://github.com/Jazhyc/aims-safety-classification — training code; README prints this repository id
https://github.com/Jazhyc/aims-safety-classification/blob/grpo/grpo/train.sh — GRPO launch script
https://huggingface.co/datasets/Jazhyc/aims-safety-intents — training dataset card
https://datasets-server.huggingface.co/is-valid?dataset=Jazhyc/aims-safety-intents — dataset viewer loads

## Record

The training set is `Jazhyc/aims-safety-intents` (AIMS). The card says "Training data: `Jazhyc/aims-safety-intents`". The dataset card says it has 1,724 annotated prompts, is English-only, and that "The intent descriptions and four-point harm labels are original human annotations". The Hub viewer loads (`viewer: true`). Splits are train 1,378, validation 173, test 173.

The objective is GRPO. The card says "It is trained with GRPO (Group Relative Policy Optimization)". The update scope is a full fine-tune. The card says "full fine-tune, not an adapter". The GitHub `grpo` branch script `train.sh` sets `algorithm.adv_estimator=grpo`, `trainer.total_epochs=10`, `data.train_batch_size=128`, and `actor_rollout_ref.actor.optim.lr=1e-6`, with no LoRA flags. The paper's Appendix F states the same learning rate, 10 epochs, and prompt batch size 128. The paper does not print `Jazhyc/Llama-3.1-8B-aims-grpo`. The GitHub README does, and calls it the "Model trained with an explicit intent-faithfulness reward". No step count, LoRA rank, or quantization-during-training statement appears for this checkpoint.

The parent is `meta-llama/Llama-3.1-8B-Instruct`. The card, the paper ("GRPO is initialized directly from Llama-3.1-8B-Instruct"), and `train.sh` (`MODEL_PATH="meta-llama/Llama-3.1-8B-Instruct"`) agree. The Hub API reports 8,030,261,248 parameters. The license field on the card is `llama3.1`.

This is a classifier, not a chatbot. The card says it "acts as an intent-aware, reasoning-based safety classifier" and "classifies the prompt, not model responses". The input is one user prompt, with the instruction in the system message. The output is a reasoning trace and a binary harm label: "The model emits `<reasoning>...</reasoning>` followed by `Intent: ...; Harm: <harmful|safe>`." The system prompt names the categories Privacy, Misinformation, Harmful Language, and Malicious Uses as examples inside the reasoning steps. The card reports harmful-class F1 of 0.836 on average across WildGuardTest, XSTest, AEGIS 2.0, ToxicChat, and OpenAI Mod. The inventory lists `dpo` and `sft` as well; those are other models in the series.

Serving is text only. The card example classifies "How do I pick a lock?" and calls `generate` with `max_new_tokens=512` and `do_sample=False`. `generation_config.json` instead sets `do_sample` true, temperature 0.6, and top_p 0.9. Context length in `config.json` is 131072. A chat template file is present. The model repository does not contain an adapter config or a training script.
