# howardbaik/gemma-4-E4B-it-mentalchat16k

## Sources

https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/howardbaik__gemma-4-E4B-it-mentalchat16k__2026-10-09.md — cached card, sha256 2df8bfed5b2ce576f28f9654c9f13157fcf1659b5588f870a5e8f08575c55678
https://huggingface.co/api/models/howardbaik/gemma-4-E4B-it-mentalchat16k — file list and safetensors parameter total
https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/config.json — architecture and context length
https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/generation_config.json — sampling defaults
https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/tokenizer_config.json — no chat_template key
https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/chat_template.jinja — chat template file
https://huggingface.co/howardbaik/gemma-4-E4B-it-mentalchat16k/raw/main/processor_config.json — image and audio processor settings
https://passthetorch.dev/posts/finetuning-with-trl/index.html — author's training writeup; names this repo
https://github.com/howardbaik/pass-the-torch/blob/main/posts/finetuning-with-trl/index.qmd — source of that writeup; no LoRA
https://colab.research.google.com/drive/14eeL-_ukmb8fbRijAgAwhOSiaDzF2WBY?usp=sharing — Colab linked from the writeup
https://huggingface.co/datasets/ShenLab/MentalChat16K — dataset page
https://huggingface.co/datasets/ShenLab/MentalChat16K/raw/main/README.md — dataset card
https://datasets-server.huggingface.co/size?dataset=ShenLab/MentalChat16K — 16084 loaded rows
https://arxiv.org/abs/2503.13509 — dataset paper abstract
https://arxiv.org/html/2503.13509 — dataset paper HTML; does not name this repo
https://dl.acm.org/doi/10.1145/3711896.3737393 — same paper in KDD 2025
https://github.com/PennShenLab/MentalChat16K — dataset code linked from the paper

## Record

The checkpoint was trained on ShenLab/MentalChat16K. The card says "ShenLab/MentalChat16K — ~16K counselor-style conversational turns combining synthetic data and anonymized interview transcripts." The dataset card splits that into 9,775 synthetic counselor–client conversations from GPT-3.5 Turbo and 6,338 question-answer pairs paraphrased from interview transcripts. The Hub dataset server reports 16,084 rows in the train split, and the author's `load_dataset` printout shows the same 16,084. The dataset is public and the viewer loads. Language is English. Provenance is mixed.

The objective is supervised fine-tuning. The card says "Method: Supervised fine-tuning (SFT)". The author's post loads `google/gemma-4-E4B-it` and passes that model to `SFTTrainer` with `bf16=True`. The post and its Quarto source do not mention LoRA, QLoRA, PEFT, or 4-bit loading. The repository has `model.safetensors` and no `adapter_config.json`. That is a full fine-tune, not an adapter. Epochs are 3. Learning rate is 2e-5. Per-device train batch size is 1, with 16 gradient-accumulation steps, which the card calls an effective batch size of 16. The card says the warmup is "5 steps (~3% of 183 total steps)".

The parent is google/gemma-4-E4B-it. The card says "Finetuned from: google/gemma-4-E4B-it". The author's post says "Our base model is `google/gemma-4-E4B-it`, which is a 4 billion effective parameter language model from Google." Those agree. The safetensors header for this repository lists 7,941,100,874 BF16 parameters. The card does not state a license.

The card presents a dialogue agent. It says the direct use is "Research into lightweight empathetic dialogue agents, evaluation of counseling-style response quality in small LLMs". That is a chatbot, and the use claim is strong. The warning is a disclaimer, not a prohibition. It says "Users should assume the model is not safety-aligned for mental-health deployment and test extensively before any downstream use." Out-of-scope uses are listed as clinical decision-making, diagnosis, or treatment, without a "must not" or "do not use" sentence.

The card's example sends one text user turn, "I've been feeling overwhelmed at work lately.", and generates with `max_new_tokens=256`. `generation_config.json` sets `do_sample` true, temperature 1.0, top_k 64, and top_p 0.95. `text_config.max_position_embeddings` is 131072. A chat template is present in `chat_template.jinja`. No system prompt is written in the card, the template, or the training messages the post prints. The model config also has vision and audio blocks, and the pipeline tag is image-text-to-text. The published example does not send an image or audio clip.

The MentalChat16K paper (KDD 2025, arXiv 2503.13509) does not print this repository id. Its own QLoRA runs are on other 7B models. A different Hub repo, mira2020/gemma-4-e4b-mentalchat16k-qlora, is a QLoRA adapter on the same base and dataset. It is not this checkpoint.
