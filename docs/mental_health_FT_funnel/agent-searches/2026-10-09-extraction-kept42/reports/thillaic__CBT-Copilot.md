# thillaic/CBT-Copilot

## Sources

https://huggingface.co/thillaic/CBT-Copilot/raw/main/README.md — current model card; same bytes as the cache (sha256 b78e901dfffc9782d9f3219f509a31d0ac19b9c05ce841b941c8b37f92c2eb40)
revision_3_experiments/hf_inventory/cache/readmes/thillaic__CBT-Copilot__2026-10-09.md — cached card
https://huggingface.co/api/models/thillaic/CBT-Copilot — file list and parameter count
https://huggingface.co/thillaic/CBT-Copilot/raw/main/config.json — context length 131072
https://huggingface.co/thillaic/CBT-Copilot/raw/main/generation_config.json — sampling defaults
https://huggingface.co/thillaic/CBT-Copilot/raw/main/tokenizer_config.json — no chat_template key
https://huggingface.co/thillaic/CBT-Copilot/raw/main/chat_template.jinja — Llama 3 chat template
https://github.com/thillai-c/CBT-Copilot — author README with the training configuration
https://raw.githubusercontent.com/thillai-c/CBT-Copilot/main/model_finetuning.py — SFTTrainer script
https://raw.githubusercontent.com/thillai-c/CBT-Copilot/main/merge_lora_weights.py — merge helper
https://raw.githubusercontent.com/thillai-c/CBT-Copilot/main/train.jsonl — local training file; first row only
https://huggingface.co/datasets/Lumiiree/therapod-dpo/raw/main/README.md — dataset card, 6,310 rows
https://huggingface.co/api/datasets/Lumiiree/therapod-dpo — dataset metadata
https://huggingface.co/datasets/Lumiiree/therapod-dpo/raw/main/pipeline.yaml — distilabel pipeline
https://huggingface.co/datasets/Lumiiree/Mental16k-Interview — upstream CSV, no dataset card, viewer shows 6,310 rows
https://huggingface.co/api/datasets/Lumiiree/Mental16k-Interview — upstream dataset metadata

Searches: `"thillaic/CBT-Copilot"`, `"CBT-Copilot" huggingface`, `"CBT-Copilot" arxiv`, `"CBT-Copilot" github`, `Lumiiree/therapod-dpo huggingface dataset`. The arXiv hit is a different project, Cognivia (arXiv:2607.25681). It does not name this repository. No paper was read in full.

## Record

The card names one training set, `Lumiiree/therapod-dpo`. The dataset card says "This dataset has been created with distilabel." It has 6,310 train rows, is public, and the card prints a loaded example, so it loads. Tags on that card are `synthetic`, `distilabel`, and `rlaif`. The pipeline loads `Lumiiree/Mental16k-Interview` and generates a reply with `01-ai/Yi-1.5-6B-chat`. That upstream set has no dataset card. Its viewer shows 6,310 rows, and the CSV already has `instruction`, `input`, and `output`. The first row of the GitHub `train.jsonl` copies the `input` and `output` text from that example, not the Yi `generations` text. Neither dataset card states a language. The upstream file does not state whether the `output` text is human or model-written.

The model card says "Fine-tuned using LoRA on the Lumiiree/therapod-dpo dataset and merged into a standalone model." It does not name a loss. The name `therapod-dpo` is not evidence of DPO. The columns are `input` and `output`, not chosen and rejected. The author's `model_finetuning.py` imports `SFTTrainer`, sets `BitsAndBytesConfig(load_in_8bit=True)`, and uses LoRA with `r=8` and `lora_alpha=16`. The README says the model was fine-tuned with that rank, that alpha, `learning_rate=2e-5`, `batch_size=1`, and `epochs=1`. The script then runs `dataset.select(range(1000))` under the comment "Reduce dataset size for faster debugging." The merge script loads `checkpoint-250`. No sentence states a step count. The Hub repo has no `adapter_config.json`. The card says the adapter was merged.

The card and the GitHub README both name the parent `meta-llama/Llama-3.2-3B-Instruct`. The training script loads that same id. The Hub file list reports 3,212,749,824 parameters. The GitHub README says "Model Size: 3B parameters."

The card presents a chatbot. It says the model is "designed to simulate compassionate and supportive dialogues in the style of Cognitive Behavioral Therapy (CBT)." The usage example sets the system line "You are a compassionate CBT therapist." That is a strong therapy claim. The warning is a disclaimer, not a ban: "This model is not a replacement for licensed mental health professionals. It should only be used for educational, research, or prototyping purposes." The GitHub README adds that metrics "will be added as they become available." No numbers are reported. The model card license is MIT. The GitHub repo license line is Apache-2.0.

The usage example sends text chat messages and no image or audio. `config.json` sets `max_position_embeddings` to 131072. `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. The card's own inference block instead sets `max_new_tokens` 256, `temperature` 0.7, `top_p` 0.9, and `repetition_penalty` 1.1. The chat template is the Llama 3 template in `chat_template.jinja`. It does not contain the therapist sentence. The inventory row matches the parent and the dataset id. It lists `dpo` and `lora`. The sources support supervised fine-tuning with LoRA on an 8-bit base, not DPO.
