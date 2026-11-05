# giannor/Qwen3.5-27B-psysafe

## Sources

- revision_3_experiments/hf_inventory/cache/readmes/giannor__Qwen3.5-27B-psysafe__2026-10-05.md — cached model card, sha256 ac404a5c4b906791f28e4e27c6a007cdb0ff476eb1474358da8f4ec93e1241f3
- https://huggingface.co/giannor/Qwen3.5-27B-psysafe/raw/main/README.md — current model card; same bytes as the cached card
- https://huggingface.co/api/models/giannor/Qwen3.5-27B-psysafe — file list, license, pipeline tag, safetensors parameter total
- https://huggingface.co/giannor/Qwen3.5-27B-psysafe/raw/main/config.json — architecture, vision tower, context length, Unsloth model name
- https://huggingface.co/giannor/Qwen3.5-27B-psysafe/raw/main/config3.yaml — training config shipped in the repo
- https://huggingface.co/giannor/Qwen3.5-27B-psysafe/raw/main/tokenizer_config.json — chat template and model_max_length
- https://huggingface.co/giannor/Qwen3.5-27B-psysafe/raw/main/chat_template.jinja — same chat template as tokenizer_config.json
- https://arxiv.org/abs/2606.09697 — paper abstract page
- https://arxiv.org/html/2606.09697 — paper HTML full text
- https://github.com/aisilab/psychological-safety — project README
- https://github.com/aisilab/psychological-safety/blob/main/02_finetunes/run_finetune.py — SFT training script; saves a merged model
- https://github.com/aisilab/psychological-safety/blob/main/02_finetunes/finetune_util.py — puts reasoning traces inside the assistant turn
- https://github.com/aisilab/psychological-safety/blob/main/02_finetunes/upload_to_hub.py — uploads the merged checkpoint
- https://github.com/aisilab/psychological-safety/blob/main/02_finetunes/configs/c3.yaml — 27B training config; same values as the repo's config3.yaml
- https://github.com/aisilab/psychological-safety/blob/main/02_finetunes/README.md — says c3.yaml is the Qwen3.5-27B reasoning SFT and that the script saves a merged model
- https://github.com/aisilab/psychological-safety/blob/main/00_data/split_data.py — holds out 100 validation and 100 test examples per risk cluster
- https://github.com/aisilab/psychological-safety/blob/main/01_prompting/systemprompt-v0.txt — generic evaluation prompt
- https://github.com/aisilab/psychological-safety/blob/main/01_prompting/systemprompt-v1.txt — PsychoSafe evaluation prompt
- https://github.com/aisilab/psychological-safety/blob/main/01_prompting/README.md — documents text-only mode for Qwen3.5
- https://odensenlp.github.io/models/ — lab page that names Qwen3.5-27B-psysafe
- https://huggingface.co/api/datasets?search=PSYCHOSAFE — dataset search; no matching dataset

## Record

The training set is the PSYCHOSAFE corpus: 8,019 prompt–response pairs. The card says each response was hand-crafted and reviewed by a domain expert, and that reasoning traces were imputed with GPT-OSS-120B. The paper is more specific: the authors wrote 14 exemplar refusals and mapped them onto prompts taken from 16 existing safety benchmarks (Appendix C). Provenance is mixed: existing prompts, human-written refusal templates, and model-written reasoning traces. There is no Hub dataset. The files are in the GitHub repo under `00_data/`. The corpus size is 8,019. The trainer reads `00_data/reasoning/train.json-reasoning.jsonl`. The splitter holds out 100 validation and 100 test rows per risk cluster, so the train file is the remainder. That train-file row count is not printed. Quote: "The model was fine-tuned on the **PSYCHOSAFE dataset**: 8,019 prompt–response pairs spanning the five risk domains above."

The objective is supervised fine-tuning. The update is LoRA, rank 1, alpha 32, dropout 0, on the attention and feed-forward projections. The base was not 4-bit quantized during training (`load_in_4bit: false`; the card says full BF16). The 8-bit setting is the AdamW optimizer. Training is 5 epochs, peak learning rate 1×10⁻⁴, batch size 4, gradient accumulation 1, max steps −1. No completed step count is stated. The training script saves with `save_pretrained_merged` and `merged_16bit` for this base, and the Hub repo is a full BF16 checkpoint (27,356,728,560 parameters) with no adapter file. The card and paper section 3.2 say the loss covers the reasoning traces and the human responses, not the user prompts. Appendix I says the reasoning trace is excluded from the loss. The shipped `config3.yaml` starts the response span at `<think>`, and the script masks only the user turn, so the reasoning trace is inside the trained response. Quote: "| Method | Supervised Fine-Tuning (SFT) |" Quote: "Fine-tuning used LoRA applied to all attention and feed-forward projection layers, with the following configuration:"

The card's base model is `Qwen/Qwen3.5-27B`. Its fine-tuning base, `config.json`, `config3.yaml`, and GitHub `c3.yaml` all name `unsloth/Qwen3.5-27B`. The paper's method section names Qwen-3.5-27B as the base for this checkpoint, and Table 2 defines `+psysafe` as Qwen3.5-27B-psysafe. The paper does not print `giannor/Qwen3.5-27B-psysafe`. One sentence in the introduction names Qwen3.5-35B-A3B; that is the other checkpoint, and the tables and this repo's config are the 27B model. The card says dense, 27B parameters, English. License is apache-2.0.

This is a chatbot. Outside the five risk domains it is described as a normal helpful assistant, and the quick start is a user/assistant chat. The use claim is Strong: the model is trained to answer the person with psychological intervention strategies, a self-help step, and a hopeful closing, and the intended deployments include mental health support platforms and crisis-intervention tools. The warning is Disclaimer only. It says the model is not a substitute for professional care and should not be interpreted as therapy, diagnosis, or crisis management. It does not say the model must not be used for those purposes. Quote: "Rather than producing blunt non-compliance, this model is trained to acknowledge the person behind the request, apply domain-appropriate psychological intervention strategies, refer users to professional resources, and offer a hopeful, personalized closing — all while declining to provide harmful information." Warning quote: "This model is not intended to replace professional mental health intervention, crisis counseling, or medical advice. It should not be interpreted as therapy, diagnosis, or crisis management."

The card's example runs the model on one user text string and sets `max_new_tokens` to 512. No other sampling settings are given, and the repo has no `generation_config.json`. The architecture still has a vision tower, and the Hub pipeline tag is image-text-to-text. The project's vLLM runner calls `--language-model-only` the text-only mode for Qwen3.5. Context length in `config.json` is 262,144 tokens. Training used 4,096. The chat template does not add a default system prompt. The paper evaluates with no system prompt, with "You are a helpful assistant.", and with the long PsychoSafe prompt. Those prompts are not stored in the checkpoint.
