# dhruvin0612/mental_health_assistant_1.1B

## Sources

- https://huggingface.co/dhruvin0612/mental_health_assistant_1.1B/raw/main/README.md — current model card; YAML only, same as the cache
- https://huggingface.co/api/models/dhruvin0612/mental_health_assistant_1.1B — file list and safetensors parameter total
- https://huggingface.co/dhruvin0612/mental_health_assistant_1.1B/raw/main/config.json — Llama architecture and context length
- https://huggingface.co/dhruvin0612/mental_health_assistant_1.1B/raw/main/generation_config.json — max length; no sampling fields
- https://huggingface.co/dhruvin0612/mental_health_assistant_1.1B/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/dhruvin0612/mental_health_assistant_1.1B/raw/main/chat_template.jinja — chat template
- https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/raw/main/README.md — parent card; text usage example
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — dataset card named in the model YAML
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/viewer/default/train — Hub viewer for that dataset

## Record

The card names one training dataset, `Amod/mental_health_counseling_conversations`. The dataset card says: "This dataset is a collection of real counselling question-and-answer pairs taken from two public mental-health platforms." Language is English. The Hub viewer shows a train split labeled "3.51k rows," so the page loads. The exact integer is not printed, and the raw file download is gated. Provenance is human.

No source states a loss, LoRA, QLoRA, epochs, steps, learning rate, or batch size. The repository has one `model.safetensors` file and no `adapter_config.json`. The card names the parent `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. `config.json` does not repeat that id. Searches did not find a paper or a GitHub repo that names this checkpoint. The Hub API reports 1,100,048,384 F16 parameters. The card YAML sets `language: en` and `license: apache-2.0`.

The README has no prose, so the output type is not listed and there is no warning. The use claim is weak because the only mental-health content is the dataset id. The YAML lists metric `code_eval` and gives no score.

This card has no usage example. The parent card runs a text chat example: "How many helicopters can a human eat in one sitting?" `chat_template.jinja` formats user, system, and assistant turns. No system prompt text is stored. `generation_config.json` sets `max_length` 2048 and no temperature or sampling fields. `max_position_embeddings` is 2048. The inventory row matches: empty methods, this dataset, and this parent.
