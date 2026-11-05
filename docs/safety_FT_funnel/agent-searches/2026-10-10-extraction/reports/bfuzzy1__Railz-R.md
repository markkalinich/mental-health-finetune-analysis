# bfuzzy1/Railz-R

## Sources

- https://huggingface.co/bfuzzy1/Railz-R/raw/main/README.md — current model card; byte-identical to the cached card (`sha256 50f4a069703292978ca7771a2dd5aa59d6abdfc71f89df2be75a18008fe4eb58`)
- https://huggingface.co/api/models/bfuzzy1/Railz-R — file list, parameter count, and chat template
- https://huggingface.co/bfuzzy1/Railz-R/raw/main/config.json — Qwen3 config, context 40960
- https://huggingface.co/bfuzzy1/Railz-R/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/bfuzzy1/Railz-R/raw/main/tokenizer_config.json — Qwen3 chat template
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — dataset the card calls NVIDIA Aegis-2.0
- https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset — reasoning-trace dataset; default load fails with a column-cast error
- https://huggingface.co/bfuzzy1/Railz-R2/raw/main/README.md — sibling card that states the shared SFT and LoRA recipe
- https://arxiv.org/abs/2505.20087 — paper cited by the Nemotron reasoning dataset; not read in full; does not appear in a search for this repository id
- https://huggingface.co/collections/bfuzzy1/railz — author collection

## Record

Two datasets. The card says training used "NVIDIA Aegis-2.0 labels" plus "published short reasoning traces (NVIDIA Nemotron Content-Safety-Reasoning, CC-BY-4.0, filtered to ground-truth-matched)" plus "mechanical policy-check rationales." Aegis-2.0 is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0` (33,416 rows, mixed human and model text, and it loads). The reasoning set is `nvidia/Nemotron-Content-Safety-Reasoning-Dataset`: 28,000 content-safety rows and 8,712 topic-control rows. Its traces are "generated from open source reasoning models," so that set is synthetic. The Hub viewer says the default config fails with `DatasetGenerationCastError`, so it does not load as one dataset. The card does not say how many rows survived the ground-truth filter.

This card does not name the loss or the update. The Railz-R2 card does: "Same SFT recipe as Railz-R: fresh Qwen3-0.6B, verdict-first target, reasoning-span down-weighted (REASON_W=0.3), LoRA r16/scale20, LR 2e-5." That is supervised fine-tuning with LoRA rank 16. What "scale20" means is not stated. Epochs, batch size, and quantization are not stated. The repository ships a full `model.safetensors` (596,049,920 bfloat16 parameters) and no adapter file.

The card says "Built on Qwen3-0.6B," and the YAML parent is `Qwen/Qwen3-0.6B`. The Railz-R2 sentence "fresh Qwen3-0.6B" agrees. Size on the card is 0.6B. Language English. License CC-BY-4.0.

This is a classifier. It "emits the violated category verbatim (or abstains), then a short chain-of-thought." The example is "Violated category: controlled or regulated substances" followed by a `<think>` block. The card says the chain of thought is "a post-hoc justification of a verdict-first decision." The category names in the prompt are a sample policy. This card reports policy-flip 78%, Aegis-2.0 test F1 76% (P72/R81), and ToxicChat F1 28%. The Railz-R2 table instead lists this model at Aegis F1 79.4% and ToxicChat F1 30%.

Serving is text only. The caller supplies the prohibited list. The card says greedy decoding and about 120 new tokens. `generation_config.json` has do_sample true, temperature 0.6, top_k 20, and top_p 0.95. Context length in `config.json` is 40960.
