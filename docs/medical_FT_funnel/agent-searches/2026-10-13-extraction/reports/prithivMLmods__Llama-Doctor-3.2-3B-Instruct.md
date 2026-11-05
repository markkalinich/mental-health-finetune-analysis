# prithivMLmods/Llama-Doctor-3.2-3B-Instruct

## Sources

- https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct/raw/main/README.md — current model card; identical to the cached card (`cmp` exit 0)
- https://huggingface.co/api/models/prithivMLmods/Llama-Doctor-3.2-3B-Instruct — file list and safetensors count
- https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct/raw/main/config.json — parent path, context length, Unsloth version string
- https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct/raw/main/generation_config.json — sampling settings
- https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct/raw/main/tokenizer_config.json — Llama 3 chat template
- https://huggingface.co/datasets/avaliev/chat_doctor — training dataset card (119,486 rows)
- https://arxiv.org/abs/2505.16530 — DuFFin paper; HTML names this repository
- https://arxiv.org/html/2505.16530 — HTML full text of that paper
- https://github.com/yuliangyan0807/llm-fingerprint — fingerprint code linked from the paper, not a training script for this model
- https://featherless.ai/models/prithivMLmods/Llama-Doctor-3.2-3B-Instruct — hosted inference page that restates the card

## Record

The training set is `avaliev/chat_doctor`. The card says the model "has been trained on a specialized dataset, avaliev/chat_doctor." The dataset loads and the Hub page shows 119,486 rows. Its card says it kept "100k real conversations" from HealthCareMagic and "10k real conversations" from icliniq, and did not add the 5k ChatGPT conversations. The provenance of the rows it kept is human. The dataset card does not state a language. It does not say how many of those rows this checkpoint used.

The card says the model "is a fine-tuned version" of Llama-3.2-3B-Instruct. "Fine-tuned" does not name a loss. No epoch, step, learning rate, batch size, or LoRA rank is stated. `config.json` contains `unsloth_version` `2024.11.7`. That is a library stamp, not a stated method. The repository is two F16 safetensors shards and has no `adapter_config.json`. The card's own file table still lists `pytorch_model` bin shards. DuFFin's appendix prints this repository URL in a table whose Type column is SFT. That table catalogs suspect models for a fingerprint test. It does not describe this training run, so the objective stays unstated.

The parent is `meta-llama/Llama-3.2-3B-Instruct`. The card, the YAML `base_model`, and `config.json` `_name_or_path` agree. The card's size label is 3B. The safetensors total is 3,212,749,824 parameters. The language tag is `en`.

The use claim is strong. The card says: "Medical Consultation Tools for generating advice or answering medical queries." The card has no medical warning. Warning strength is none.

The purpose is stated. The card says the dataset training is "to enhance its performance in providing conversational or advisory responses, especially in medical or technical fields." The audience is a patient or member of the public asking a medical question. The functions are answering medical questions, giving advice, and talking with that person. The output is a chat reply. The clinical tasks are medical question answering, a conversation with a patient, and treatment or medication advice. The specialty is general. No narrower field is named. The dataset instruction, which the card does not quote, is: "If you are a doctor, please answer the medical questions based on the patient's description."

Serving is text only. The card sets no system prompt and no generation example. `generation_config.json` sets `do_sample` true, temperature 0.6, top_p 0.9, and max_length 131072. `max_position_embeddings` is 131072. The license is `llama3.2`. The card reports no benchmark scores.

Inventory methods is empty, which matches the missing loss. Dataset `avaliev/chat_doctor` and parent `meta-llama/Llama-3.2-3B-Instruct` match the card.
