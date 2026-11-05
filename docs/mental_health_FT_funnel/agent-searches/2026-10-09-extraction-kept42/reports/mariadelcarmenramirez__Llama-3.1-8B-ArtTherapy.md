# mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy

## Sources

https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy/raw/main/README.md — current model card; byte-identical to the cached card (sha256 39918d040a36c4c9c1f70784ab87ec95cec703ccb76c81e0d3f5362d878479ee)
https://huggingface.co/api/models/mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy — file list, parameter count, and chat template
https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy/raw/main/config.json — architecture and context length
https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy/raw/main/generation_config.json — sampling defaults
https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-QLoRA-ArtTherapy/raw/main/README.md — card of the adapter this repository says it merged
https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-QLoRA-ArtTherapy/raw/main/adapter_config.json — LoRA rank, alpha, and base model id
https://huggingface.co/datasets/mariadelcarmenramirez/art-therapy-data — dataset card and viewer
https://huggingface.co/api/datasets/mariadelcarmenramirez/art-therapy-data — dataset split size and files

## Record

The training set is `mariadelcarmenramirez/art-therapy-data`. The model card says: "Trained on mariadelcarmenramirez/art-therapy-data, a dataset of 9,572 structured art therapy dialogue examples organized into four therapeutic phases. Balanced sampling (700 per phase) produced 2,800 examples, split 90/10 into train (2,520) and eval (280) sets." The dataset card says the dialogues are synthetic Spanish text: "All content is synthetically generated. No real client data were used." Generation used `gpt-5-nano`, anchored on therapist-reviewed seed examples. The Hub dataset page loads. It reports 9,572 train rows and a public parquet file.

The card does not name a loss. It says the weights are a merged QLoRA fine-tune: "This model was produced by merging the QLoRA adapter mariadelcarmenramirez/Llama-3.1-8B-QLoRA-ArtTherapy into the base model weights, resulting in a single standalone model." The hyperparameter table says "Fine-tuning method | QLoRA (4-bit NF4)", 3 epochs, learning rate 5e-5, effective batch size 16, LoRA rank 32, LoRA alpha 64. The linked adapter config has `"r": 32`, `"lora_alpha": 64`, and `"base_model_name_or_path": "meta-llama/Llama-3.1-8B-Instruct"`. That adapter card says "Training completed all 3 epochs (474 steps total)" and that the epoch-2 checkpoint was the one kept. "Fine-tuned" and QLoRA do not name `sft` or another loss, so the objective is not stated.

The parent on the card is `meta-llama/Llama-3.1-8B-Instruct`. The adapter config names the same base. The Hub file list reports 8,030,261,248 parameters in `model.safetensors`.

The card presents a Spanish art-therapy dialogue model. "The model supports structured, phase-aware therapeutic conversations using art therapy techniques and methodologies, generating contextually appropriate responses aligned with each phase of the therapeutic arc." That is a chatbot, and the therapy claim is strong. The warning is an explicit prohibition: "It should not be used for clinical diagnosis, crisis intervention, or as the sole therapeutic agent for individuals with serious mental health conditions." No paper and no GitHub repository turned up for this repository id. Evaluation on the card is loss and token accuracy: "Best checkpoint at epoch 2.0 (`eval_loss = 1.313`). Final training loss: **1.238**." License on the card is `llama3.1`.

The usage example is text only. A user turn is `"El círculo central parece respirar suave."` and the model is called with `model.generate` on chat-template tokens. `generation_config.json` sets `do_sample` true, temperature 0.6, and `top_p` 0.9. The card's own example uses temperature 0.7 and `max_new_tokens` 256. `config.json` sets `max_position_embeddings` to 131072. The chat template is the Llama 3.1 Instruct template in `chat_template.jinja`. The FASE_2 system text in the card is an example the caller supplies, not a prompt stored in the template.
