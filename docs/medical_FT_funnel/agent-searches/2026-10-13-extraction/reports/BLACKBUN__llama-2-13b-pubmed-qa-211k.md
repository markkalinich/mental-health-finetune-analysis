# BLACKBUN/llama-2-13b-pubmed-qa-211k

## Sources

https://huggingface.co/BLACKBUN/llama-2-13b-pubmed-qa-211k/raw/main/README.md — current model card; YAML only; identical to the cached card
https://huggingface.co/api/models/BLACKBUN/llama-2-13b-pubmed-qa-211k — file list and parameter count
https://huggingface.co/BLACKBUN/llama-2-13b-pubmed-qa-211k/raw/main/config.json — parent path and context length
https://huggingface.co/BLACKBUN/llama-2-13b-pubmed-qa-211k/raw/main/generation_config.json — sampling settings
https://huggingface.co/BLACKBUN/llama-2-13b-pubmed-qa-211k/raw/main/tokenizer_config.json — Llama 2 chat template
https://huggingface.co/datasets/qiaojin/PubMedQA — dataset card
https://huggingface.co/api/datasets/qiaojin/PubMedQA — dataset loads; three public configs
https://github.com/Aprilistic/Medical_LLM — authors' repository; the README links this exact model as the 13B PubMedQA baseline
https://github.com/Aprilistic/Medical_LLM/blob/main/model/13b/13b_baseline/llama-pubmed-211k.py — training script whose output name is this model
https://github.com/Aprilistic/Medical_LLM/blob/main/model/13b/13b_baseline/train.sh — shell wrapper for that script
https://github.com/Aprilistic/Medical_LLM/blob/main/model/save_merged.ipynb — merge notebook that pushes this model name
https://arxiv.org/abs/1909.06146 — PubMedQA paper linked from the dataset card; it does not name this repository
https://github.com/pubmedqa/pubmedqa — dataset code repository

## Record

The model card only has YAML. It names the dataset qiaojin/PubMedQA. The training script loads `pubmed_qa`, config `pqa_artificial`, split `train`. A line that would keep 10,000 rows is commented out, so the script uses the full split. That split has 211,269 examples. The dataset loads. Its card says the language is English. Annotations are listed as expert-generated and machine-generated. The artificial split is automatically generated questions on PubMed abstracts, so the provenance is mixed. The dataset card says: "The task of PubMedQA is to answer research questions with yes/no/maybe (e.g.: Do preoperative statins reduce atrial fibrillation after coronary artery bypass grafting?) using the corresponding abstracts."

The script trains with TRL `SFTTrainer`. The base is loaded in 4-bit (`load_in_4bit=True`, NF4, double quant) and then LoRA is applied. The comment says "LoRA config based on QLoRA paper". Rank is 64 and `lora_alpha` is 16. Training is 2 epochs, learning rate 2e-4, and per-device batch size 4 because `use_flash_attention` is false, with gradient accumulation 2. The same script merges the adapter (`merge_and_unload`) and pushes `llama-2-13b-pubmed-qa-211k`. The Hub repository has eleven float32 shards, 13,015,864,320 parameters, and no adapter file.

The parent is meta-llama/Llama-2-13b-chat-hf. The card YAML, `config.json` `_name_or_path`, and the script's `model_id` all say that. The GitHub README heading is "Fine-tuned LLaMa2-13b-chat-hf Models" and the row "Baseline / pubmed-qa" links this repository.

The card has no description and no warning. The use claim is weak: the only medical content on the card is the dataset name. No sentence says what the model is for or who it is for. Audiences and functions are empty. The license is MIT. No evaluation numbers are reported. The PubMedQA paper does not name this repository.

The training text is an instruction that says "Use the Input below to create an instruction, which could have been used to generate the response using an LLM," with the question as input and `long_answer` as the response. That is not a yes/no/maybe label. The card does not show an output example, so the output type is not listed.

The clinical task of the named dataset is PubMedQA, which is exam-style biomedical question answering. The model card names no specialty.

The training and dataset examples are text. A Llama 2 chat template is present. It does not set a system prompt unless the caller supplies one. `max_position_embeddings` is 4096. `generation_config.json` sets `do_sample` true, `temperature` 0.6, `top_p` 0.9, and `max_length` 4096. Training packed sequences to 2048. A separate repository, BLACKBUN/llama-2-13b-pubmed-qa-211k-gguf_q8_0, is an 8-bit GGUF file, not the weights in this repository.
