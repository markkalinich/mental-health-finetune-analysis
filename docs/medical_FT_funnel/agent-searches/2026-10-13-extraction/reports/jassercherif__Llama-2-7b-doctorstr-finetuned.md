# jassercherif/Llama-2-7b-doctorstr-finetuned

## Sources

- https://huggingface.co/jassercherif/Llama-2-7b-doctorstr-finetuned/raw/main/README.md — current card; YAML only, same as the cache
- https://huggingface.co/api/models/jassercherif/Llama-2-7b-doctorstr-finetuned — file list
- https://huggingface.co/jassercherif/Llama-2-7b-doctorstr-finetuned/raw/main/config.json — LlamaForCausalLM, parent path, context 4096
- https://huggingface.co/jassercherif/Llama-2-7b-doctorstr-finetuned/raw/main/generation_config.json — temperature 0.9, top_p 0.6, do_sample true
- https://huggingface.co/jassercherif/Llama-2-7b-doctorstr-finetuned/raw/main/tokenizer_config.json — no chat template
- https://huggingface.co/datasets/jassercherif/ChatDoctor-HealthCareMagic-llama2-100k — dataset page, 1,000 rows
- https://huggingface.co/datasets/jassercherif/ChatDoctor-HealthCareMagic-llama2-100k/raw/main/README.md — dataset card, YAML only
- https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k — a different Hub dataset with a similar name; 112,165 rows; not named by this card

## Record

The card names one dataset, `jassercherif/ChatDoctor-HealthCareMagic-llama2-100k`. That dataset card has no prose. Its YAML says language `en` and 1,000 train examples in one `text` field. The viewer rows are `[INST]` questions followed by `[/INST]` replies. The dataset id says 100k. The file has 1,000 rows. Provenance is not stated. A different dataset, `lavita/ChatDoctor-HealthCareMagic-100k`, has 112,165 rows and is not the id on this card.

No sentence names a loss or an update scope. The card sets `library_name: peft`, and the Hub tag says the parent is an adapter, but the repository has full float16 Llama shards and no `adapter_config.json`. Epochs, rank, and learning rate are absent. The objective and the update scope are not stated.

The parent is `NousResearch/Llama-2-7b-chat-hf` on the card and in `config.json` `_name_or_path`. No source states a parameter count. No licence is stated. No paper or GitHub repository names this checkpoint.

The card has no description. The repository id contains `doctor`, so the use claim is Strong. There is no warning sentence. No sentence says what the model is for, so purpose is no, audiences are empty, and functions are empty. Output type is not listed. Output kind, clinical task, and specialty are not stated. The YAML names the metrics accuracy and bleu and gives no scores.

Serving is text only: `config.json` is `LlamaForCausalLM`. There is no chat template. Generation settings are temperature 0.9, top_p 0.6, and do_sample true. `max_position_embeddings` is 4096.
