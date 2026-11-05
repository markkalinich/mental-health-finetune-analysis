# Sanjay002/tinyllama-mental-health-finetuned

## Sources

- https://huggingface.co/Sanjay002/tinyllama-mental-health-finetuned/raw/main/README.md — current card; YAML only, same as the cache
- https://huggingface.co/Sanjay002/tinyllama-mental-health-finetuned — model page; README body empty
- https://huggingface.co/api/models/Sanjay002/tinyllama-mental-health-finetuned — file list and parameter count
- https://huggingface.co/Sanjay002/tinyllama-mental-health-finetuned/raw/main/config.json — architecture and context length
- https://huggingface.co/Sanjay002/tinyllama-mental-health-finetuned/raw/main/generation_config.json — max length, no sampling fields
- https://huggingface.co/Sanjay002/tinyllama-mental-health-finetuned/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/raw/main/README.md — parent card; text quickstart
- https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset/raw/main/README.md — dataset card, 172 train rows
- https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset/viewer/default/train — dataset viewer loads
- https://huggingface.co/spaces/uolivares/Sanjay002-tinyllama-mental-health-finetuned — Space; sleeping
- https://featherless.ai/models/Sanjay002/tinyllama-mental-health-finetuned — hosted inference page
- Cached card `revision_3_experiments/hf_inventory/cache/readmes/Sanjay002__tinyllama-mental-health-finetuned__2026-10-09.md` — sha256 2605d8b83df067cd9bf74d0b36c87be812c4f9e48afba97e6f21164a625410e9

Searches for the repo id, the model name, arXiv, and GitHub did not find a paper or a training repository that names this checkpoint.

## Record

The card lists one dataset, `heliosbrahma/mental_health_chatbot_dataset`. The dataset card says: "Dataset was curated from popular healthcare blogs like WebMD, Mayo Clinic and HeatlhLine, online FAQs etc." It also says "Questions were asked by the patients and answers were given by healthcare providers." That is human text, in English, 172 train rows. The viewer loads those rows.

No source states a loss, a LoRA or full update, a rank, a learning rate, a step count, or an epoch count for this checkpoint. The repo holds one `model.safetensors` file and no `adapter_config.json`. A later repo, `usama011/tinyllama-mental-health-fine-tuned-11`, says it was fine-tuned from this one and prints its own learning rate, batch size, and epoch count. Those numbers are not this checkpoint's.

The card's `base_model` is `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. No paper or GitHub repo states a parent for this checkpoint. The Hub API reports 1,100,048,384 parameters, stored as float32. The card lists language `en` and license `mit`.

The README body is empty. The YAML tag is `chatbot`, so the output type is a chatbot. The use claim is weak: the card has no prose, and the mental-health text is the dataset id `heliosbrahma/mental_health_chatbot_dataset` plus the tag `mental-health`. There is no warning and no evaluation.

`config.json` sets `max_position_embeddings` to 2048. The chat template formats text user, system, and assistant turns and sets `use_default_system_prompt` to false, so there is no system sentence. `generation_config.json` sets `max_length` to 2048 and does not set temperature or the other sampling fields. The parent quickstart is text: "How many helicopters can a human eat in one sitting?"
