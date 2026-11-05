# bfuzzy1/Railz-R2

## Sources

- https://huggingface.co/bfuzzy1/Railz-R2/raw/main/README.md — current model card; byte-identical to the cached card (`sha256 ed76988495e7d8f312c916eceaeaa358e058a738078648ed5eae4fbd9c4243ba`)
- https://huggingface.co/api/models/bfuzzy1/Railz-R2 — file list, parameter count, and chat template
- https://huggingface.co/bfuzzy1/Railz-R2/raw/main/config.json — Qwen3 config, context 40960
- https://huggingface.co/bfuzzy1/Railz-R2/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/bfuzzy1/Railz-R2/raw/main/tokenizer_config.json — Qwen3 chat template
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis-2.0 labels
- https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset — Nemotron reasoning traces; default load fails
- https://huggingface.co/datasets/OpenSafetyLab/Salad-Data — jailbreak and harmful prompts
- https://huggingface.co/datasets/allenai/WildChat-1M — benign real chat
- https://arxiv.org/abs/2407.05557 — R2-Guard abstract returned by the name search; it does not print this repository id
- https://huggingface.co/collections/bfuzzy1/railz — author collection

## Record

Four sources are named. The card says "NVIDIA Aegis-2.0 labels + NVIDIA Nemotron reasoning traces (CC-BY-4.0) + OpenSafetyLab/Salad-Data (Apache-2.0) jailbreak/harmful prompts + WildChat-1M (ODC-BY) benign real-chat, all mapped mechanically to the Aegis-18 vocabulary." Aegis-2.0 is 33,416 rows and loads. The Nemotron reasoning set is 28,000 content-safety rows plus 8,712 topic-control rows; its traces are model-generated, and the default Hub load fails with a column-cast error. Salad-Data's base set is 21,318 questions (15,433 from a fine-tuned GPT-3.5, the rest from public sets) and the viewer loads. WildChat-1M is human–ChatGPT conversations; the current card says this version keeps non-toxic chats and calls the collection 1 million. The card does not say how many rows of each set were used.

The objective is supervised fine-tuning. The card says "Same SFT recipe as Railz-R: fresh Qwen3-0.6B, verdict-first target, reasoning-span down-weighted (REASON_W=0.3), LoRA r16/scale20, LR 2e-5." Rank is 16. What "scale20" means is not stated. Epochs, batch size, and quantization are not stated. The repository ships a full `model.safetensors` (596,049,920 bfloat16 parameters) and no adapter file.

The card says "Built on Qwen3-0.6B" and the YAML parent is `Qwen/Qwen3-0.6B`. No other page names this checkpoint's parent. Size on the card is 0.6B. Language English. License CC-BY-4.0.

This is a classifier. It emits "the violated category verbatim (or abstaining) then a short chain-of-thought." The output line is `Violated category: <X>` or `no listed category applies`, then a `<think>` block. The card says that block is "a post-hoc justification of a verdict-first decision." It names an "Aegis-18 vocabulary" and does not list the 18 names. Scores against Railz-R: policy-flip 90% versus 78%, ToxicChat F1 38% versus 30%, Aegis-2.0 test F1 77.9% versus 79.4% on 1,964 items.

Serving is text only. The caller supplies the prohibited list. The card says "Greedy, ~120 max new tokens." `generation_config.json` has do_sample true, temperature 0.6, top_k 20, and top_p 0.95. Context length in `config.json` is 40960.
