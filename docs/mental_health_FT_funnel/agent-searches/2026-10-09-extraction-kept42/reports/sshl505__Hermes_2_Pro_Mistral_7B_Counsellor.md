# sshl505/Hermes_2_Pro_Mistral_7B_Counsellor

## Sources

- https://huggingface.co/sshl505/Hermes_2_Pro_Mistral_7B_Counsellor/raw/main/README.md — current model card; byte-identical to the cached card (`sha256 c94833f57a4e901c9fe57ef88b9864692d301ffc7d0318bc32f1701dd60bcd60`)
- revision_3_experiments/hf_inventory/cache/readmes/sshl505__Hermes_2_Pro_Mistral_7B_Counsellor__2026-10-09.md — cached card
- https://huggingface.co/api/models/sshl505/Hermes_2_Pro_Mistral_7B_Counsellor — file list and parameter count
- https://huggingface.co/sshl505/Hermes_2_Pro_Mistral_7B_Counsellor/raw/main/config.json — architecture and context length
- https://huggingface.co/sshl505/Hermes_2_Pro_Mistral_7B_Counsellor/raw/main/generation_config.json — sampling flag
- https://huggingface.co/sshl505/Hermes_2_Pro_Mistral_7B_Counsellor/raw/main/tokenizer_config.json — chat templates
- https://huggingface.co/NousResearch/Hermes-2-Pro-Mistral-7B/raw/main/README.md — parent card, text-only usage example
- https://huggingface.co/datasets/Estwld/empathetic_dialogues_llm — dataset card named in the model YAML; viewer shows rows
- https://huggingface.co/api/datasets/Estwld/empathetic_dialogues_llm — split counts
- https://huggingface.co/datasets/facebook/empathetic_dialogues — original Empathetic Dialogues dataset card; viewer disabled
- https://arxiv.org/abs/1811.00207 — abstract of the 2019 EmpatheticDialogues paper
- https://arxiv.org/html/1811.00207 — HTML full text of that paper; it does not print this repository id
- https://github.com/facebookresearch/EmpatheticDialogues — README and training commands for the 2019 retrieval models, not this checkpoint
- https://aclanthology.org/P19-1534 — ACL 2019 venue for that paper

## Record

The card names one dataset, `Estwld/empathetic_dialogues_llm`. That Hub dataset loads. Its card says: "This repository contains a reformatted version of the Empathetic Dialogues dataset, tailored for seamless integration with Language Model (LLM) training and inference." The dataset API lists 19,533 train, 2,770 valid, and 2,547 test rows (24,850). Language is English. The original dialogues are human: the 2019 paper says "The new resource consists of crowdsourced one-on-one conversations." The model card does not say how the rows were used, only lists the dataset id.

No source states a loss or an update scope for this checkpoint. The repository has six safetensors shards and no `adapter_config.json`, notebook, `train.py`, or trainer JSON. The 2019 GitHub scripts train Transformer and BERT retrieval models on EmpatheticDialogues. They do not name `sshl505/Hermes_2_Pro_Mistral_7B_Counsellor`. Epochs, steps, learning rate, batch size, LoRA rank, and LoRA alpha are not stated.

The card's `base_model` is `NousResearch/Hermes-2-Pro-Mistral-7B`. No paper or GitHub page names this checkpoint or repeats that parent. The Hub file list reports 7,241,994,240 parameters. The model page rounds that to 7B.

The card says: "This model is specialized for emotional and psychological support dialogue generation." That is a dialogue generator for emotional and psychological support, so the output type is Chatbot and the use claim is Strong. The card has no sentence forbidding therapy, counseling, support, diagnosis, treatment, or medical advice, and no "not a substitute" line. Warning strength is None. License is `unknown`. No evaluation of this checkpoint is reported.

The parent card runs the model on text only: "Write a short story about Goku discovering kirby has teamed up with Majin Buu to destroy the world." This repository's `generation_config.json` sets `do_sample` to true and does not set temperature, top-p, top-k, max new tokens, or repetition penalty. `config.json` sets `max_position_embeddings` to 32768 and `sliding_window` to 4096. A chat template is present. The default template does not insert a system prompt. The named `tool_use` template inserts "You are a function calling AI model."
