# BLACKBUN/llama-2-7b-pubmed-qa-211k

## Sources

https://huggingface.co/BLACKBUN/llama-2-7b-pubmed-qa-211k/raw/main/README.md — current model card; YAML only; identical to the cached card
https://huggingface.co/api/models/BLACKBUN/llama-2-7b-pubmed-qa-211k — file list
https://huggingface.co/BLACKBUN/llama-2-7b-pubmed-qa-211k/raw/main/config.json — parent path and context length
https://huggingface.co/BLACKBUN/llama-2-7b-pubmed-qa-211k/raw/main/generation_config.json — sampling settings
https://huggingface.co/BLACKBUN/llama-2-7b-pubmed-qa-211k/raw/main/tokenizer_config.json — Llama 2 chat template
https://huggingface.co/datasets/qiaojin/PubMedQA — dataset card
https://huggingface.co/api/datasets/qiaojin/PubMedQA — dataset loads; three public configs
https://github.com/Aprilistic/Medical_LLM — authors' repository; the README links this exact model as the 7B PubMedQA baseline
https://github.com/Aprilistic/Medical_LLM/blob/main/model/7b/7b_baseline/llama-pubmed-211k.py — training script whose output name is this model
https://github.com/Aprilistic/Medical_LLM/blob/main/model/7b/7b_baseline/train.sh — shell wrapper; it runs the 211k script
https://arxiv.org/abs/1909.06146 — PubMedQA paper linked from the dataset card; it does not name this repository
https://github.com/pubmedqa/pubmedqa — dataset code repository
https://featherless.ai/models/BLACKBUN/llama-2-7b-pubmed-qa-211k — hosted inference page that states a 7B size
https://huggingface.co/spaces/Omnibus/InferenceClient_Chatbots — Space listed on the model
https://huggingface.co/spaces/K00B404/Teachershub — Space listed on the model

## Record

The model card only has YAML. It names the dataset qiaojin/PubMedQA and the parent meta-llama/Llama-2-7b-chat-hf. It does not set a license. The training script loads `pubmed_qa`, config `pqa_artificial`, split `train`. A line that would keep 10,000 rows is commented out, so the script uses the full split. That split has 211,269 examples. The dataset loads. Its card says the language is English. Annotations are listed as expert-generated and machine-generated, so the provenance is mixed. The same folder contains `llama-pubmed-10k.py`. `train.sh` runs `llama-pubmed-211k.py`, not that file.

The script trains with TRL `SFTTrainer`. The base is loaded in 4-bit (`load_in_4bit=True`, NF4, double quant) and then LoRA is applied. Rank is 64 and `lora_alpha` is 16. Training is 2 epochs, learning rate 2e-4, and per-device batch size 4, with gradient accumulation 2. The same script merges the adapter and pushes `llama-2-7b-pubmed-qa-211k`. The Hub repository has three float32 pytorch `.bin` shards and no adapter file. The Hub API does not report a parameter total. Featherless says the model is 7B.

The parent is meta-llama/Llama-2-7b-chat-hf on the card, in `config.json` `_name_or_path`, and in the script's `model_id`. The GitHub README row "Baseline / pubmed-qa" under "Fine-tuned LLaMa2-7b-chat-hf Models" links this repository.

The card has no description and no warning. The use claim is weak: the only medical content on the card is the dataset name. No sentence on the card or in the authors' README says what the model is for or who it is for. Audiences and functions are empty. No evaluation numbers are reported. The PubMedQA paper does not name this repository. Featherless adds a biomedical question-answering description that is not on the card.

The training text asks the model to write an instruction that could have produced the long answer. The card does not show an output example, so the output type is not listed.

The clinical task of the named dataset is PubMedQA. The model card names no specialty.

The examples are text. A Llama 2 chat template is present and sets no system prompt unless the caller supplies one. `max_position_embeddings` is 4096. `generation_config.json` sets `do_sample` true, `temperature` 0.6, `top_p` 0.9, and `max_length` 4096. Training packed sequences to 2048. A separate repository, BLACKBUN/llama-2-7b-pubmed-qa-211k-gguf_q8_0, is an 8-bit GGUF file. The Hub lists two Spaces that use this model. Those Space pages were not opened.
