# arijitbhowal/Llama-2-7b-mental-health-finetune

## Sources

- https://huggingface.co/arijitbhowal/Llama-2-7b-mental-health-finetune/raw/main/README.md — current model card; YAML only, same as the cache
- https://huggingface.co/api/models/arijitbhowal/Llama-2-7b-mental-health-finetune — repository file list
- https://huggingface.co/arijitbhowal/Llama-2-7b-mental-health-finetune/raw/main/config.json — architecture and `_name_or_path`
- https://huggingface.co/arijitbhowal/Llama-2-7b-mental-health-finetune/raw/main/generation_config.json — sampling settings
- https://huggingface.co/arijitbhowal/Llama-2-7b-mental-health-finetune/raw/main/tokenizer_config.json — tokenizer; no chat template
- https://huggingface.co/NousResearch/Llama-2-7b-chat-hf/raw/main/README.md — parent card; text-only input
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — dataset card named in the model YAML
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/viewer/default/train — Hub viewer for that dataset

## Record

The card names one training dataset, `Amod/mental_health_counseling_conversations`, and nothing else about the data. The dataset card says: "This dataset is a collection of real counselling question-and-answer pairs taken from two public mental-health platforms." Language is English. The Hub viewer shows a train split labeled "3.51k rows," so the page loads. The raw dataset README returned 401 because the dataset is gated (`manual`), and the card does not print an exact row count. Provenance is human.

No source states a loss, LoRA, QLoRA, epochs, steps, learning rate, or batch size. The repository has full `pytorch_model.bin` shards and no `adapter_config.json`. That does not say whether an adapter was merged. `config.json` has `"_name_or_path": "NousResearch/Llama-2-7b-chat-hf"`, the same parent as the card YAML `base_model`.

The README has no prose after the YAML, so the output type is not listed and there is no warning. The use claim is weak because the only mental-health content is the dataset id in the YAML: `datasets: - Amod/mental_health_counseling_conversations`. The card states license `apache-2.0`. No paper, GitHub repo, or evaluation is linked, and searches for the repository id did not find a paper or a GitHub repo that names this checkpoint.

The parent card says "Models input text only." This repository's `tokenizer_config.json` has no `chat_template` key. `generation_config.json` sets `temperature` 0.9, `top_p` 0.6, and `do_sample` true. `config.json` sets `max_position_embeddings` to 4096. The inventory row matches: empty methods, this dataset, and this parent.
