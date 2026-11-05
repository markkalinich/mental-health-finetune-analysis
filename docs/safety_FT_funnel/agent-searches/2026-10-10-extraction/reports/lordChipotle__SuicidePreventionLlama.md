# lordChipotle/SuicidePreventionLlama

## Sources

https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/README.md — current model card; same bytes as the cache (sha256 89632171f577f2365f7073d2cc9e8d08699c92d7562d3adf0b1b6b9514817684)
https://huggingface.co/api/models/lordChipotle/SuicidePreventionLlama — file list and parameter count 3,212,749,824
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/config.json — LlamaForCausalLM; `_name_or_path` is `unsloth/llama-3.2-3b-instruct-bnb-4bit`; unsloth_version 2025.1.5
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/generation_config.json — do_sample true, temperature 0.6, top_p 0.9, max_length 131072
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/tokenizer_config.json — Llama chat template is inside this file
https://colab.research.google.com/drive/1vbio7VWmkpQoTnDUg32TABxxf4VcBBeY?usp=sharing — notebook linked from the card; the page did not return cells
https://huggingface.co/datasets/nbertagnolli/counsel-chat/raw/main/README.md — CounselChat dataset card
https://datasets-server.huggingface.co/size?dataset=nbertagnolli/counsel-chat — 2,775 rows; the viewer loads
https://huggingface.co/datasets/thePixel42/depression-detection — Hub set whose card names r/teenagers, r/SuicideWatch, and r/depression; 200,000 rows
https://aclanthology.org/2022.emnlp-main.11/ — PAIR paper; does not name this repository
https://github.com/nbertagnolli/counsel-chat — CounselChat code repository, linked from the dataset card

## Record

The card says "We combined multiple datasets to train this model," and names four. CounselChat is the only one with a Hub id on the card: `nbertagnolli/counsel-chat`. That dataset loads. The datasets server reports 2,775 rows. The dataset card says "The text was written by licensed counselors in the United States and annonymous individuals." Language is English. The Reddit line is "Reddit-based suicide detection data (r/SuicideWatch, r/depression, r/teenagers)." The card does not give a dataset id. `thePixel42/depression-detection` says "The posts have been collected from 3 subreddits: r/teenagers, r/SuicideWatch, and r/depression" and loads with 200,000 rows. Other Hub sets also contain SuicideWatch posts, so that id is a match of the description, not a name printed on this card. Twitter is only "Twitter suicidal-intent classification data." Several Hub and Kaggle sets use that phrase, and the card does not pick one. PAIR is "short counseling interactions with high- and medium-quality reflections." No Hub dataset uses that name. The EMNLP 2022 PAIR paper is about counselor reflection quality and does not print this repository id.

The card does not name a loss. It says "Parameter-Efficient Fine-tuning: We used **LoRA** adapters or 4-bit quantization." `config.json` sets `_name_or_path` to `unsloth/llama-3.2-3b-instruct-bnb-4bit` and `unsloth_version` to `2025.1.5`. That is a 4-bit base, so the saved path is QLoRA. There is no `adapter_config.json`, so rank and alpha are not stated. The weights are two BF16 shards. The card says "Batch Size: 2," "Max Steps: 60 (example short run)," and "Learning Rate: 2e-4." It does not state epochs. The Colab link did not return the notebook cells.

The card YAML says `base_model: meta-llama/Llama-3.2-3B-Instruct`. The prose says only "LLaMA-based architecture." `config.json` names `unsloth/llama-3.2-3b-instruct-bnb-4bit`. The Hub safetensors total is 3,212,749,824 parameters. The card does not print a parameter count.

The card presents a support model. It says the model will "provide a short therapeutic-style reply if suicidality is detected," and the second example is "Respond like a therapist." It also classifies text as "suicidal" or "non-suicidal." The input in the example is one passage of text. It says "This model is **not** a substitute for professional mental-health services" and "This model does not replace mental-health professionals." No evaluation numbers are reported. No license is stated.

The examples are text only. The chat template is in `tokenizer_config.json`. The card does not set a system prompt. The template inserts "Cutting Knowledge Date: December 2023." `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. The therapy example sets `max_new_tokens=256`. `config.json` sets `max_position_embeddings` to 131072.
