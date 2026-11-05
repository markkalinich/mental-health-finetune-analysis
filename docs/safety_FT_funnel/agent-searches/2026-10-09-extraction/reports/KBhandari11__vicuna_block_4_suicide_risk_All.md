# KBhandari11/vicuna_block_4_suicide_risk_All

## Sources

https://huggingface.co/KBhandari11/vicuna_block_4_suicide_risk_All/raw/main/README.md — current model card; same text as the cached card
https://huggingface.co/api/models/KBhandari11/vicuna_block_4_suicide_risk_All — file list and parameter count
https://huggingface.co/KBhandari11/vicuna_block_4_suicide_risk_All — Hub page; labels the weights 7B params
https://huggingface.co/KBhandari11/vicuna_block_4_suicide_risk_All/raw/main/config.json — Llama config, context length 4096
https://huggingface.co/KBhandari11/vicuna_block_4_suicide_risk_All/raw/main/generation_config.json — sampling settings
https://huggingface.co/lmsys/vicuna-7b-v1.5/raw/main/README.md — parent card; text chat assistant
https://huggingface.co/collections/KBhandari11/vicuna-model-pruning-strategy-block — collection that lists this repo and the paper
https://arxiv.org/abs/2508.18192 — paper abstract
https://arxiv.org/html/2508.18192 — paper HTML; does not print this repo id
https://openreview.net/forum?id=c3GL3vDggf — CogInterp @ NeurIPS 2025 poster record
https://arxiv.org/abs/1910.09700 — carbon-calculator paper linked from the empty model-card template
https://github.com/KBhandari11/LLMNeuron — paper code; README and scripts/run.sh do not name this repo
https://huggingface.co/datasets/tasksource/bigbench — dataset card named in the YAML
https://huggingface.co/datasets/tasksource/bigbench/raw/84e90626beb6488fa5513bc15632e6c203a3952b/README.md — dataset README: language en, mixed creators
https://huggingface.co/datasets/tasksource/bigbench/viewer/suicide_risk — suicide_risk configuration viewer

## Record

The card YAML names two training sets: `dataset: ['tasksource/bigbench', 'suicide_risk']` and `dataset_label: suicide_risk`. `tasksource/bigbench` loads. The dataset page states 841,339 rows. Its README says `language: en` and `annotations_creators` of crowdsourced, expert-generated, and machine-generated, so the collection is mixed. `suicide_risk` is a configuration of that same dataset, not a second Hub id. The viewer loads it: 24 train rows and 16 validation rows (40). Each row asks the model to estimate suicide risk of a text as no, low, moderate, or severe risk.

No source states a named loss, a full or LoRA update, a rank, or a learning rate for this repository. The card body says training data and the training regime are "[More Information Needed]". The YAML tag `finetune: All` is not a loss. The tag `rank: 1` is not labeled as a LoRA rank. The repository holds six float32 safetensors shards and no `adapter_config.json`. Bhandari, Chen, and Gao, arXiv:2508.18192, describe Vicuna fine-tuning under an "All" condition ("fine-tuning across all modules") with "five epochs, a batch size of two, and a learning rate of 0.00001", and they say the finetuned weights were uploaded to `https://huggingface.co/KBhandari11/collections`. That paper does not print `KBhandari11/vicuna_block_4_suicide_risk_All`. Those hyperparameters are not recorded as this checkpoint's settings. `scripts/run.sh` in https://github.com/KBhandari11/LLMNeuron prunes Llama-2-7b checkpoints and does not name this repo.

The card parent is the YAML line `base_model: lmsys/vicuna-7b-v1.5`. The body still says "Finetuned from model [optional]: [More Information Needed]". No paper or script prints this repository id, so there is no outside source that confirms the parent.

The only description is "This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated." That is not a usable account of what the model emits, so the output type is not listed. The use claim is weak: the card has no description, and the YAML names the mental-health dataset `suicide_risk`. The warning on the card is the template sentence "Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model." It does not forbid therapy, counseling, or medical advice. License and evaluation results for this checkpoint are not stated. The API counts 6,738,415,616 parameters; the Hub page labels that "7B params".

The parent card says "Vicuna is a chat assistant trained by fine-tuning Llama 2 on user-shared conversations collected from ShareGPT." That is text, with no image or audio. This repository has no chat template and no system prompt. `generation_config.json` sets `do_sample` true, temperature 0.9, top_p 0.6, and max_length 4096. `config.json` sets `max_position_embeddings` to 4096.
