# nicoboss/Qwen-3-32B-Medical-Reasoning

## Sources

- https://huggingface.co/nicoboss/Qwen-3-32B-Medical-Reasoning/raw/main/README.md — current model card (same text as the 10 October cache)
- https://huggingface.co/api/models/nicoboss/Qwen-3-32B-Medical-Reasoning — file list, parameter count, chat template
- https://huggingface.co/nicoboss/Qwen-3-32B-Medical-Reasoning/raw/main/config.json — Qwen3 32B config, context 40960
- https://huggingface.co/nicoboss/Qwen-3-32B-Medical-Reasoning/raw/main/generation_config.json — sampling settings
- https://huggingface.co/kingabzpro/Qwen-3-32B-Medical-Reasoning — original adapter repository
- https://huggingface.co/kingabzpro/Qwen-3-32B-Medical-Reasoning/raw/main/adapter_config.json — LoRA rank, alpha, target modules, parent
- https://huggingface.co/kingabzpro/Qwen-3-32B-Medical-Reasoning/blob/main/fine-tuning-qwen-3.ipynb — training notebook linked from the card
- https://www.datacamp.com/tutorial/fine-tuning-qwen3 — the author's write-up of that notebook, including SFTTrainer settings
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — reasoning dataset; English viewer loads
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT/raw/main/README.md — GPT-4o construction
- https://arxiv.org/html/2512.05576 — CureAgent HTML; cites this repository id
- https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1, linked from the dataset; full text not read for this model
- https://github.com/kingabzpro — author GitHub named on the tutorial page
- https://github.com/FreedomIntelligence/HuatuoGPT-o1 — linked from the dataset card

## Record

Training used the English split of `FreedomIntelligence/medical-o1-reasoning-SFT`. The dataset card says it "is constructed using GPT-4o". The viewer loads and shows about 19.7k English rows of Question, Complex_CoT, and Response. The DataCamp tutorial, which is the write-up of the linked notebook, loads `train[0:2000]`. The copied card says both "first 500 samples" and "2000 examples".

The training loss is supervised fine-tuning. The tutorial says "We will now configure and initialize the SFTTrainer". The update is LoRA on a 4-bit NF4 base: rank 64, alpha 16, dropout 0.05, one epoch, learning rate 2e-4, per-device batch size 1, gradient accumulation 2. The card says "PEFT (LoRA / Adapter Tuning style)" and "Quantization: 4-bit (NF4)". nicoboss's repository is not the adapter. It is 14 BF16 shards, 32,762,123,264 parameters, and the intro says the kingabzpro adapter was "applied to" `Qwen/Qwen3-32B`. The adapter itself remains at `kingabzpro/Qwen-3-32B-Medical-Reasoning`.

The parent is `Qwen/Qwen3-32B`. The card, the YAML `base_model`, and the adapter's `base_model_name_or_path` agree. A comment in the usage script says "original model from Meta". The id in that same script is `Qwen/Qwen3-32B`.

The use claim is strong. The prompt says: "You are a medical expert with advanced knowledge in clinical reasoning, diagnostics, and treatment planning. Please answer the following medical question." There is no warning sentence. The licence is Apache-2.0.

The purpose is medical reasoning. The tutorial says the goal is to "respond accurately to patient queries".

The card's prompt claims answering medical questions, clinical reasoning, diagnostics, and treatment planning. The example asks: "What is the initial management for a patient presenting with diabetic ketoacidosis (DKA)?" The written form is a `<think>` block and then an answer. The field is general medicine.

The example is a text question. `generation_config.json` sets `do_sample` true, temperature 0.6, top_k 20, and top_p 0.95. The usage script sets `max_new_tokens` 1200. `max_position_embeddings` is 40960. The medical instruction sits in the prompt, not in the Qwen3 chat template. The card reports no score. CureAgent cites this repository and lists 36.513 and 40.791 on its two phases.
