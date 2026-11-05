# RANIGO/qwen2.5-7b-counseling

## Sources

- https://huggingface.co/RANIGO/qwen2.5-7b-counseling — model page; README body is empty
- https://huggingface.co/api/models/RANIGO/qwen2.5-7b-counseling — file list, card YAML, parameter count, chat template
- https://huggingface.co/RANIGO/qwen2.5-7b-counseling/raw/main/README.md — raw card; 401, repo is gated
- https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/raw/main/README.md — parent card; text quickstart
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — dataset card
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/viewer/default/train — dataset viewer, train split shown as 3.51k rows
- Cached card `revision_3_experiments/hf_inventory/cache/readmes/RANIGO__qwen2.5-7b-counseling__2026-10-09.md` — YAML only, sha256 a95af3d84ae9198682bac95af41f0ee474eaf9a18fd0526f38c7973d33579c04

Searches for the repo id, the model name, arXiv, and GitHub did not find a paper or a GitHub repo that names this checkpoint.

## Record

The card names one dataset, `Amod/mental_health_counseling_conversations`. The dataset card says: "This dataset is a compilation of high-quality, real one-on-one mental health counseling conversations between individuals and licensed professionals." It also says the rows were "Collected directly from two publicly accessible counselling websites," so the provenance is human, and the language line is English. The Hub viewer shows a train split of 3.51k rows. The size API and the raw dataset README returned 401 because the dataset is gated, so the exact row count is not recorded. The model card does not say this checkpoint was trained on that dataset beyond listing it under `datasets`.

No source states a loss, a LoRA or full update, a rank, a learning rate, a step count, or an epoch count. The repo holds two safetensors weight shards and no `adapter_config.json`. That file list is not a training method.

The card's `base_model` is `Qwen/Qwen2.5-7B-Instruct`. No paper or GitHub repo names this checkpoint or states a parent. The Hub API reports 7,615,616,512 parameters. The model page rounds that to 8B and lists tensor type F16. The card lists languages `en` and `ko`.

The README body is empty, so the output type is not listed and there is no warning. The use claim is weak because the only mental-health text is the YAML dataset id `Amod/mental_health_counseling_conversations`. The license in the card YAML is `apache-2.0`. No evaluation is stated.

The parent quickstart runs the model on a text prompt: `prompt = "Give me a short introduction to large language model."` This repo's API returns a text chat template whose default system line is "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." `config.json` and `generation_config.json` returned 401, so the context length and sampling settings are not recorded.
