# bfuzzy1/Railz

## Sources

- https://huggingface.co/bfuzzy1/Railz/raw/main/README.md — current model card; byte-identical to the cached card (`sha256 2a1d14f790ecbdcd6f2ccf07029ca474c68abc3f45f3bb4bc2e2a9abe8048670`)
- https://huggingface.co/api/models/bfuzzy1/Railz — file list, parameter count, and chat template
- https://huggingface.co/bfuzzy1/Railz/raw/main/config.json — Qwen3 config, context 40960
- https://huggingface.co/bfuzzy1/Railz/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/bfuzzy1/Railz/raw/main/tokenizer_config.json — Qwen3 chat template
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — dataset the card calls NVIDIA Aegis-2.0
- https://huggingface.co/collections/bfuzzy1/railz — author collection of local moderation models

## Record

The training data is NVIDIA Aegis-2.0, the Hub dataset `nvidia/Aegis-AI-Content-Safety-Dataset-2.0` (33,416 rows). The card says it was "Trained with mechanical supervision (NVIDIA Aegis-2.0 labels) + hard-negative mining, on the same data as its reasoning sibling Railz-R." The dataset page loads. Provenance is mixed: human-written prompts, model-generated responses, and a mix of human and model labels. The card does not say how many rows were used.

The card does not name a loss from the study list, and it does not say whether the update was full fine-tuning or LoRA. It says "No teacher model in the training loop." Epochs, learning rate, batch size, and rank are not stated. The repository ships a full `model.safetensors` (596,049,920 bfloat16 parameters) and no adapter file.

The card says "Built on Qwen3-0.6B." The YAML `base_model` is `Qwen/Qwen3-0.6B`. No paper or GitHub page independently names this checkpoint. The card states the size as 0.6B and the language as English. License CC-BY-4.0.

This is a classifier, not a chatbot. The card says it "judges content against a policy you supply at inference — not a fixed taxonomy" and "emits the violated category verbatim (or abstains)." The example verdict is "Violated category: controlled or regulated substances", or "no listed category applies". The three category names in the prompt are a sample policy, not a fixed list. Reported scores: policy-flip 75%, Aegis-2.0 test F1 76% (P69/R85), ToxicChat F1 22% (P14/R55).

Serving is text only. The caller supplies the prohibited list in the system prompt. The card says "Greedy decoding, ~24 max new tokens." `generation_config.json` has do_sample true, temperature 0.6, top_k 20, and top_p 0.95. `config.json` sets `max_position_embeddings` to 40960. The example output is an empty `<think>` block and then the verdict line.
