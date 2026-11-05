# lordChipotle/SuicidePreventionLlama

## Sources

https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/lordChipotle__SuicidePreventionLlama__2026-10-09.md — cached card, sha256 89632171f577f2365f7073d2cc9e8d08699c92d7562d3adf0b1b6b9514817684
https://huggingface.co/api/models/lordChipotle/SuicidePreventionLlama — file list and parameter count
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/config.json — `_name_or_path` and context length
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/generation_config.json — temperature, top_p, do_sample, max_length
https://huggingface.co/lordChipotle/SuicidePreventionLlama/raw/main/tokenizer_config.json — Llama 3.2 chat template
https://huggingface.co/unsloth/llama-3.2-3b-instruct-bnb-4bit/raw/main/README.md — card of the checkpoint named in config.json
https://huggingface.co/datasets/nbertagnolli/counsel-chat — CounselChat dataset card
https://datasets-server.huggingface.co/size?dataset=nbertagnolli/counsel-chat — 2,775 rows
https://colab.research.google.com/drive/1vbio7VWmkpQoTnDUg32TABxxf4VcBBeY?usp=sharing — notebook linked from the card; Google sign-in page, cells not read

## Record

The card names four training sources. The YAML id is nbertagnolli/counsel-chat. That Hub set loads, has 2,775 rows, and its card says "Languages: English" and "This data contains expert responses by licensed clinicialns to questions posed by individuals." It was "scraped on 20220401 from counselchat.com," so the text is human. The card also says the model was trained on "Reddit-based suicide detection data (r/SuicideWatch, r/depression, r/teenagers)," "Twitter suicidal-intent classification data," and "PAIR: short counseling interactions with high- and medium-quality reflections." It does not give Hub ids for those three. Searches find more than one Hub set with those subreddit names, and no Hub dataset whose card is the PAIR reflection set, so those three ids, sizes, languages, and provenance are not stated.

The card says the model is "fine-tuned" and does not name a loss. "Fine-tuned" is not an objective. On the update it says: "We used LoRA adapters or 4-bit quantization to reduce GPU memory usage." That sentence does not say which of the two was used, so the update scope is not stated. It gives "Batch Size: 2," "Max Steps: 60 (example short run)," and "Learning Rate: 2e-4." It does not give a LoRA rank, an epoch count, or a statement that a quantized base was used. The repository has two safetensors shards and no adapter file. The Hub API counts 3,212,749,824 parameters, stored as bfloat16. The linked Colab notebook did not open without a Google sign-in. Searches did not find a paper or a GitHub repository that names this checkpoint.

The card YAML says the parent is meta-llama/Llama-3.2-3B-Instruct. `config.json` says `"_name_or_path": "unsloth/llama-3.2-3b-instruct-bnb-4bit"`. That Unsloth card's own YAML says `base_model: meta-llama/Llama-3.2-3B-Instruct`. The immediate checkpoint id in the config does not match the card. The Unsloth page's speed claims are library boilerplate and are not evidence about this training run. The card says "language: en."

The card says the model is designed to "detect suicidal or self-harm risk in text" and to "provide a short therapeutic-style reply if suicidality is detected." The usage example also says "Respond like a therapist." The output type is a chatbot, and the same card shows a classification prompt. The use claim is Strong. The warning is a disclaimer: "This model is not a substitute for professional mental-health services or emergency intervention." It also says "This model does not replace mental-health professionals" and points to 988. It does not say the model must not be used for therapy. No evaluation numbers and no license are stated. The inventory parent matches the card YAML. The inventory method `lora` is only one side of the card's "or," and the inventory dataset list omits the Reddit, Twitter, and PAIR sources the card names.

The usage example passes a text string and no image or audio. The chat template is in `tokenizer_config.json`. The card does not set a system role. `generation_config.json` sets temperature 0.6, top_p 0.9, do_sample true, and max_length 131072. The example uses max_new_tokens 256. Context length in `config.json` and the tokenizer is 131072.
