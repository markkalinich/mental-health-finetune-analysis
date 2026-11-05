# henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B

## Sources

- https://huggingface.co/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B/raw/main/README.md — current model card; same text as the cached card
- https://huggingface.co/api/models/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B — file list, chat template, parameter count
- https://huggingface.co/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B/raw/main/config.json — architecture and context length
- https://huggingface.co/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://github.com/henrywch/LE_Morals — project code; README names this repository as the merged model
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/train/lora_sft_fast.sh — LoRA SFT script the README says to run
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/config.yaml — dataset ids used in the mix
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/common/handbook.py — system-prompt builder
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/value_handbook/02_categories.yaml — S1–S14 and I1–I4 names
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/doc/main.tex — course LaTeX template; does not name this repository
- https://github.com/henrywch/LE_Morals/blob/main/doc/LE_Morals_paper.pdf — paper PDF; not opened
- https://huggingface.co/datasets/allenai/wildguardmix — gated training source
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — human-labeled QA pairs
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — 33,416 annotated interactions
- https://huggingface.co/datasets/lmsys/toxic-chat — toxicity labels on Vicuna prompts
- https://huggingface.co/datasets/toxigen/toxigen-data — GPT-3 implicit hate text
- https://huggingface.co/datasets/AIML-TUDA/LlavaGuard — gated image set named in config.yaml
- https://huggingface.co/datasets/neuralcatcher/hateful_memes — meme set named in config.yaml

## Record

The training mix is `train_70k_mix`, 89,752 samples, about 56% Chinese and about 31.6% image. The card says: "Sources: WildGuardMix, BeaverTails, Aegis2.0, ToxicChat, Toxigen, LlavaGuard, Hateful-Memes." `config.yaml` maps those names to `allenai/wildguardmix`, `PKU-Alignment/BeaverTails`, `nvidia/Aegis-AI-Content-Safety-Dataset-2.0`, `lmsys/toxic-chat`, `toxigen/toxigen-data`, `AIML-TUDA/LlavaGuard`, and `neuralcatcher/hateful_memes`. WildGuardMix and LlavaGuard are gated, so they do not load without accepting terms. The mix itself is not a Hub dataset.

The checkpoint is supervised fine-tuning with LoRA. The script header says "ms-swift LoRA SFT of Qwen3.6-35B-A3B (MoE, VLM) as a value/guard model," and the README's reproduce step is `bash train/lora_sft_fast.sh`. The card says "LoRA (rank 64, α 128, lr 2e-4) via ms-swift + DeepSpeed ZeRO-2 + flash-attn on 8×H200 (bf16)" and that this checkpoint is "v2-60" at about 1.3 epochs. The script's own defaults are rank 16, alpha 32, learning rate 1e-4, and 2 epochs. Training dtype is bfloat16, so the base was not quantized. The GitHub README calls this Hub repo the merged model. The repo also has `train/dpo.sh` and `train/full_sft.sh`; the documented command for this guard is the LoRA SFT script.

The parent is `Qwen/Qwen3.6-35B-A3B`. The card says "a LoRA fine-tune of the natively-multimodal MoE base Qwen3.6-35B-A3B," and the GitHub README says the same base, "~35B params / ~3B active."

The card presents a content guard, not a chat assistant. Input is a user turn, and the card also says it "judges Chinese and English, text and images." Output is a four-field verdict: "safety: safe | unsafe", categories S1–S14 or I1–I4, "severity: none | low | medium | high", and "rationale: a short human-readable justification." The detection claim is that it "filters harmful text and images." The English category names are in `value_handbook/02_categories.yaml`, which the card points to as the value handbook. They run from Violent Crimes through Code Interpreter Abuse, plus four image classes.

The printed example is text only. A chat template is present in `chat_template.jinja`. `generation_config.json` sets `do_sample` true, temperature 1.0, top_k 20, and top_p 0.95. The card's own example uses greedy decoding and `max_new_tokens` 256. Context length in `config.json` is 262,144. The license YAML is `other`, name `qwen`.
