# XuehangCang/SmolLM3-3B-Pick

## Sources

https://huggingface.co/XuehangCang/SmolLM3-3B-Pick/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/XuehangCang__SmolLM3-3B-Pick__2026-10-09.md — cached card
https://huggingface.co/api/models/XuehangCang/SmolLM3-3B-Pick — file list and parameter count
https://huggingface.co/XuehangCang/SmolLM3-3B-Pick/raw/main/config.json — architecture and context length
https://huggingface.co/XuehangCang/SmolLM3-3B-Pick/raw/main/generation_config.json — sampling settings
https://huggingface.co/XuehangCang/SmolLM3-3B-Pick/raw/main/tokenizer_config.json — tokenizer; no chat_template key
https://huggingface.co/XuehangCang/SmolLM3-3B-Pick/raw/main/chat_template.jinja — chat template and default system text
https://github.com/XuehangCang/pick — code link on the card; the page returns 404
https://exa.ai/library/publication/f3781mnjtw5 — abstract index for a claimed Zenodo preprint; no DOI and no HTML full text
https://huggingface.co/datasets/XuehangCang/safe_prompt — safe-prompt dataset page and viewer
https://huggingface.co/datasets/XuehangCang/safe_prompt/raw/main/README.md — safe-prompt dataset card (split sizes only)
https://huggingface.co/datasets/XuehangCang/unsafe_prompt — unsafe-prompt dataset page; preview rows load, full viewer timed out
https://huggingface.co/datasets/XuehangCang/unsafe_prompt/raw/main/README.md — unsafe-prompt dataset card (split sizes only)

## Record

The card uses two prompt sets to locate refusal, then edits weights. It names `XuehangCang/safe_prompt`（800 条）and `XuehangCang/unsafe_prompt`（800 条）. Each Hub dataset loads. Each dataset card lists a train split of 800 rows and a test split of 200 rows. Preview rows are English prompts paired with Chinese. Neither dataset card says whether the prompts are human-written or generated.

No sentence names a training loss. The method section says "Rank-1 LoRA 消融 — 通过 LoRA 精确修改选中组件的权重", and the architecture table lists LoRA targets `attn.o_proj, mlp.down_proj`（共 72 个模块）. Rank is 1. Alpha, epochs, steps, learning rate, and batch size are not stated. The "10 分 3 秒" line is wall-clock time for the ablation, not a step count. The repo publishes `model.safetensors` and no `adapter_config.json`. The card does not say whether a LoRA adapter was merged. Stored dtype is bfloat16. The card does not say the base was quantized during the edit. The linked GitHub repository returns 404, so there is no training script to read. A title search finds an abstract index that says PICK "requires no fine-tuning data or optimization" and reports experiments on SmolLM3-3B. That page does not print `XuehangCang/SmolLM3-3B-Pick`.

The card's parent is HuggingFaceTB/SmolLM3-3B ("基础模型 | HuggingFaceTB/SmolLM3-3B"). No page outside this repository names this checkpoint. The Hub file metadata counts 3,075,098,624 parameters.

The card describes a refusal-removed chat model, not a therapy or support tool. The usage example is a user message, `messages = [{'role': 'user', 'content': '你的问题'}]`, so the output type is a chatbot and the input in that example is text. The use claim is absent. The limitation "本模型仅移除了拒绝行为相关的组件，未经过安全性微调，可能仍会在某些场景下产生不安全输出" is about unsafe outputs and capability, not therapy or medical use. The card reports refusal falling from 625/800 (78.1%) to 114/800 (14.3%). License text: "本模型继承自 SmolLM3-3B 的 Apache 2.0 许可。" YAML languages are zh and en.

`generation_config.json` sets `do_sample` true, temperature 0.6, and top_p 0.95. The card example uses `max_new_tokens=512`. `config.json` sets `max_position_embeddings` to 65536. The default chat template, with thinking on, inserts "You are a helpful AI assistant named SmolLM, trained by Hugging Face." The inventory row matches: LoRA, the two named datasets, and parent HuggingFaceTB/SmolLM3-3B.
