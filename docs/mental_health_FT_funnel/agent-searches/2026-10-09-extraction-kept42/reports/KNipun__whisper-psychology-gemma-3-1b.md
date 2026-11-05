# KNipun/whisper-psychology-gemma-3-1b

## Sources

https://huggingface.co/KNipun/whisper-psychology-gemma-3-1b/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/KNipun__whisper-psychology-gemma-3-1b__2026-10-09.md — cached card, sha256 81dd96a61a09a7df9672a0827e5c622bfc6ad88e399204cfc5a85ad9e9f6dc0b
https://huggingface.co/api/models/KNipun/whisper-psychology-gemma-3-1b — file list and safetensors parameter count
https://huggingface.co/KNipun/whisper-psychology-gemma-3-1b/raw/main/config.json — architecture and context length
https://huggingface.co/KNipun/whisper-psychology-gemma-3-1b/raw/main/generation_config.json — sampling settings
https://huggingface.co/KNipun/whisper-psychology-gemma-3-1b/raw/main/tokenizer_config.json — tokenizer; no chat_template key
https://huggingface.co/KNipun/whisper-psychology-gemma-3-1b/raw/main/chat_template.jinja — Gemma chat template
https://github.com/kavishannip/whisper-ai-psychiatric-RAG-gemma3-finetuned — app README; names this repository
https://github.com/kavishannip/whisper-ai-psychiatric-RAG-gemma3-finetuned/blob/main/Finetune_gemma_3_1b_it.ipynb — training notebook that pushes this repository id
https://colab.research.google.com/drive/1E3Hb2VgK0q5tzR8kzpzsCGdFNcznQgo9?usp=sharing — Colab copy linked from the notebook
https://huggingface.co/datasets/jkhedri/psychology-dataset — dataset page, no dataset card, 9,846 rows
https://datasets-server.huggingface.co/size?dataset=jkhedri/psychology-dataset — row count
https://datasets-server.huggingface.co/first-rows?dataset=jkhedri/psychology-dataset&config=default&split=train — columns question, response_j, response_k
https://huggingface.co/spaces/KNipun/Whisper-AI-Psychiatric — demo Space named on the Hub API and the GitHub README
https://youtu.be/ZRykgI2qO5g — demo video linked from the GitHub README
https://arxiv.org/abs/2503.19786 — Gemma 3 Technical Report; HTML does not name this repository
https://arxiv.org/html/2503.19786v1 — HTML of that report
https://arxiv.org/abs/2403.08295 — paper linked from the GitHub README; not read
https://arxiv.org/abs/2106.09685 — paper linked from the GitHub README; not read
https://arxiv.org/abs/2212.04356 — paper linked from the GitHub README; not read
https://arxiv.org/abs/2005.11401 — paper linked from the GitHub README; not read

## Record

The training set is `jkhedri/psychology-dataset`. The Hub page says "Number of rows: 9,846" and the dataset loads. There is no dataset card, so language and whether the text is human or synthetic are not stated. Columns are `question`, `response_j`, and `response_k`. The notebook loads all 9,846 rows, then keeps 2,000: the saved output says "Training on 2000 samples". The card says "Training Samples: ~2000 psychology conversations". The notebook trains on `response_j` only and drops `response_k`.

The notebook uses Hugging Face `Trainer` with `task_type="CAUSAL_LM"` on question plus preferred-response text. That is supervised next-token training. It never names SFT, and it does not train a preference loss. The base is loaded with `load_in_4bit=True` and then LoRA: `r=8`, `lora_alpha=16`, modules `q_proj`, `k_proj`, `v_proj`, `o_proj`. The card says the same rank, alpha, modules, and "Quantization: 4-bit quantization during training". `TrainingArguments` set `num_train_epochs=3`, `per_device_train_batch_size=1`, `gradient_accumulation_steps=8`, `learning_rate=2e-4`, and `max_steps=-1`. The saved log does not print a finished step count. The merge cell runs `merge_and_unload()`. The Hub repo has `model.safetensors` and no `adapter_config.json`. The saved push log ends in an HTTP 500, so the notebook file itself does not show a successful upload line. The GitHub README disagrees with both the card and the notebook: it says rank 16, alpha 32, modules `q_proj` and `v_proj`, and "10,000+ psychology Q&A pairs".

The parent on the card is `google/gemma-3-1b-it`. The notebook sets `model_name = "google/gemma-3-1b-it"`. The Hub safetensors total is 999,885,952 parameters. The card calls the base Gemma-3-1B-IT.

The card says "Whisper is a mental health chatbot" and "The model is designed to provide supportive and empathetic responses for mental health conversations." That is a chatbot with a strong support claim. The limitation line is "Not a replacement for professional mental health care", plus educational and research use. That is a disclaimer, not a ban. The README's accuracy, BLEU, and relevance figures are not in the training log. The notebook sets `eval_strategy="no"`.

The card example calls `chat_with_whisper` on a text string and generates with `max_new_tokens=150`, `temperature=0.7`, and `do_sample=True`. `generation_config.json` sets `do_sample` true, `top_k` 64, and `top_p` 0.95. `config.json` sets `max_position_embeddings` to 32768. A chat template is present. No system prompt is set. License is `apache-2.0`.
