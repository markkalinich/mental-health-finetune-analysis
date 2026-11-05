# lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented

## Sources

https://huggingface.co/lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/lavanyamurugesan123__Llama3.2-3B-Instruct-finetuned-Therapy-oriented__2026-10-09.md — cached card, sha256 648ae1898d7a3fe69fd74fded52e54860bed323a928b0bd1b067b3088c3f498c
https://huggingface.co/api/models/lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented — file list and parameter count
https://huggingface.co/lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented/raw/main/config.json — context length 131072; no parent field
https://huggingface.co/lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
https://huggingface.co/lavanyamurugesan123/Llama3.2-3B-Instruct-finetuned-Therapy-oriented/raw/main/tokenizer_config.json — Llama 3.2 chat template
https://huggingface.co/datasets/RaviSheel04/Psychology-Data — dataset page; card is only a MIT license line
https://datasets-server.huggingface.co/size?dataset=RaviSheel04/Psychology-Data — 600,000 rows
https://datasets-server.huggingface.co/first-rows?dataset=RaviSheel04/Psychology-Data&config=default&split=train — columns Human, Assistant, Instructions

## Record

The card names one dataset, RaviSheel04/Psychology-Data. That Hub set loads. It has 600,000 rows and columns Human, Assistant, and Instructions. The dataset card states only `license: mit`. It does not state the language or whether the text is human or synthetic. A preview row is English dialogue with the instruction "you are a Pyschology bot who answers user question in a polite manner." One preview row is not a statement of provenance for the set.

The card says "Finetuned variant" and does not name a loss, LoRA, QLoRA, or a full update. Epochs, steps, learning rate, and batch size are not stated. The repository holds two safetensors shards and no adapter file. That does not say how the weights were updated. Searches for the repository id and the model name did not find a paper or a GitHub repository that names this checkpoint.

The card says it is a "Finetuned variant of Meta's Llama-3.2-3B-Instruct" and the YAML `base_model` is `meta-llama/Llama-3.2-3B-Instruct`. No paper, GitHub file, or `config.json` field names that parent again. The Hub API safetensors total is 3,212,749,824 parameters, float16. The card says "Language(s) (NLP): English."

The card says the model is for "therapy-oriented, empathetic dialogue" and lists "Therapy-style chatbot assistants" and "Educational tools in psychology and emotional support." The output type is a chatbot. The use claim is Strong. The card has no limitations section and no sentence that forbids therapy, diagnosis, or medical advice, so the warning is None. No evaluation and no model license are stated. The inventory row's empty method, the dataset id, and the parent match the card.

The card's example runs the model on the text "I've been feeling anxious lately. What should I do?" The system line in that example is "You are a Psychology Assistant, designed to answer users' questions in a kind, empathetic, and respectful manner, drawing from psychological principles and research to provide thoughtful support.DO NOT USE THE NAME OF THE PERSON IN YOUR RESPONSE". The example sets `max_new_tokens=200`, `do_sample=True`, and `temperature=0.7`. `generation_config.json` sets `temperature` 0.6, `top_p` 0.9, and `do_sample` true. Context length in `config.json` and the tokenizer is 131072.
