# NeelRajani/Qwen3-0.6B-Base_SFT-safety75_ADV-pku-v00.01

## Sources

https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety75_ADV-pku-v00.01/raw/main/README.md — current model card; same bytes as the cached card
https://huggingface.co/api/models/NeelRajani/Qwen3-0.6B-Base_SFT-safety75_ADV-pku-v00.01 — file list and parameter count
https://huggingface.co/api/models/NeelRajani/Qwen3-0.6B-Base_SFT-safety75_ADV-pku-v00.01/commits/main — checkpoint commit titles
https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety75_ADV-pku-v00.01/raw/main/config.json — architecture and context length
https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety75_ADV-pku-v00.01/raw/main/generation_config.json — generation defaults
https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety75_ADV-pku-v00.01/raw/main/tokenizer_config.json — tokenizer settings
https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety75_ADV-pku-v00.01/raw/main/chat_template.jinja — chat template
https://huggingface.co/datasets/NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2 — dataset page; gated, README body empty
https://huggingface.co/api/datasets/NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2 — dataset metadata, 10,226 train rows
https://github.com/huggingface/trl — library citation on the card, not this model's training code
https://wandb.ai/neelectric/shallowness/runs/kaj82sqj — Weights & Biases run linked from the card; page not read
https://arxiv.org/abs/2505.09388 — Qwen3 Technical Report; does not name this repository

## Record

The card names one training set, `NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2`. The sentence is: "This model is a fine-tuned version of NeelRajani/Qwen3-0.6B-Base_SFT_safety_v00.01 on the NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2 dataset." The dataset is gated. Its README body is empty, and the raw README request returned 401, so the files do not load here. The public dataset metadata lists one train split of 10,226 examples. Language and whether the text is human or model-written are not stated.

The training objective is supervised fine-tuning. The card says: "This model was trained with SFT." No sentence says whether all weights were updated or only a LoRA adapter. The repository publishes `model.safetensors` and has no `adapter_config.json`. Rank, alpha, epochs, learning rate, and batch size are not stated. `training_args.bin` is in the repository and was not read. Hub commits are titled through "Training in progress, step 576", then "Model save", then "End of training". That does not state the final step count.

The card names the parent `NeelRajani/Qwen3-0.6B-Base_SFT_safety_v00.01`. No paper or other page names this checkpoint. The Qwen3 Technical Report turned up in a search for the model name and does not print this repository id.

The card does not claim therapy, counseling, or emotional support. It has no warning about medical or therapy use. The only description is the fine-tune sentence above. The quick start runs a text question through a chat turn: `output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]`. That is a conversation interface, so the output type is recorded as a chatbot. The Hub API reports 596,049,920 parameters. The model page labels the same file 0.6B. No license is stated. The YAML value `licence: license` is the unfilled trainer placeholder.

The usage example is text only. `generation_config.json` sets `do_sample` false and `max_new_tokens` 2048. `config.json` sets `max_position_embeddings` to 32,768. The chat template is present and has no fixed system prompt. No evaluation numbers are on the card.

The inventory row matches the card: method `sft`, dataset `NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2`, parent `NeelRajani/Qwen3-0.6B-Base_SFT_safety_v00.01`.
