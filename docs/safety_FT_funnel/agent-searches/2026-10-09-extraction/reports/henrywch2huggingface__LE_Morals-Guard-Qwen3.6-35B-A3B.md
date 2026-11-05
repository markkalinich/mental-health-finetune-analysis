# henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B

## Sources

- https://huggingface.co/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B/raw/main/README.md — current model card
- revision_3_experiments/hf_inventory/cache/readmes/henrywch2huggingface__LE_Morals-Guard-Qwen3.6-35B-A3B__2026-10-09.md — cached card, sha256 9923986764d063315442aa38b3cfca5b528702a604c5c9a0bd90c86032586150
- https://huggingface.co/api/models/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B — file list, parameter count, chat template
- https://huggingface.co/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B/raw/main/config.json — architecture and context length
- https://huggingface.co/henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B/raw/main/generation_config.json — sampling defaults
- https://github.com/henrywch/LE_Morals — project README, names this repository as the merged model
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/README.md — method, data mix, reproduce steps
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/train/lora_sft_fast.sh — ms-swift SFT script
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/doc/Train_LoRA.md — LoRA recipe, including the rank-64 line
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/config.yaml — dataset ids used by the mix
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/common/handbook.py — system-prompt builder
- https://github.com/henrywch/LE_Morals/blob/main/doc/LE_Morals_paper.pdf — paper PDF linked from the repo; not downloaded
- https://huggingface.co/datasets/allenai/wildguardmix — WildGuardMix card
- https://huggingface.co/api/datasets/allenai/wildguardmix — gated, English
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — BeaverTails card
- https://huggingface.co/api/datasets/PKU-Alignment/BeaverTails — public files
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0 card
- https://huggingface.co/datasets/lmsys/toxic-chat — ToxicChat card
- https://huggingface.co/api/datasets/lmsys/toxic-chat — public files
- https://huggingface.co/datasets/toxigen/toxigen-data — ToxiGen card
- https://huggingface.co/api/datasets/toxigen/toxigen-data — train split size
- https://huggingface.co/api/datasets/AIML-TUDA/LlavaGuard — gated image dataset named in config.yaml
- https://huggingface.co/api/datasets/neuralcatcher/hateful_memes — public meme files named in config.yaml

No arXiv paper names this checkpoint. `doc/main.tex` in the same GitHub repo is a course template with placeholder authors and does not print this repository id.

## Record

The training mix is `train_70k_mix`, 89,752 samples. The card says: "Sources: WildGuardMix, BeaverTails, Aegis2.0, ToxicChat, Toxigen, LlavaGuard, Hateful-Memes." `config.yaml` maps those names to `allenai/wildguardmix` (86,759 examples, mixed synthetic and human, gated), `PKU-Alignment/BeaverTails` (human-labeled QA, public, size only stated as the 330k split name), `nvidia/Aegis-AI-Content-Safety-Dataset-2.0` (33,416 interactions, public), `lmsys/toxic-chat` ("10K user prompts", public), `toxigen/toxigen-data` (250,951-row train split, GPT-3 text, public), `AIML-TUDA/LlavaGuard` (gated), and `neuralcatcher/hateful_memes` (public files, example count not stated). About 56% of the mix is Chinese and about 31.6% is image.

The objective is supervised fine-tuning with LoRA. The reproduce step is `bash train/lora_sft_fast.sh`, and that script's header says "ms-swift LoRA SFT" and calls `swift sft`. The card says: "LoRA (rank 64, α 128, lr 2e-4) via ms-swift + DeepSpeed ZeRO-2 + flash-attn on 8×H200 (bf16)." The same rank, alpha, and learning rate appear as the high-capacity override in `doc/Train_LoRA.md`. The script's own defaults are rank 16, alpha 32, learning rate 1e-4, and 2 epochs. The card selects this checkpoint at "about 1.3 epochs" ("v2-60"). The step count is not stated. The script's per-device batch is 2 with gradient accumulation 8; the card does not say which batch this run used. Training dtype is bf16, so the base was not quantized. The GitHub README calls this repository the "merged model", and the weights are a full BF16 checkpoint of 35,107,181,936 parameters with no adapter file.

The parent is `Qwen/Qwen3.6-35B-A3B`. The card and the GitHub README both say that. The stated size is "~35B params / ~3B active". `config.json` is `Qwen3_5MoeForConditionalGeneration` with `max_position_embeddings` 262144.

This is a content classifier. The card says it "emits a four-field structured verdict" of safety, categories, severity, and rationale. The use claim is Absent: "filtering harmful content in training corpora and online moderation." There is no mental-health support claim. The warning is Unrelated limitations only: over-refusal on XSTest is about 12% and the false-positive rate is 0.146. Languages are Chinese and English. The license name is `qwen` (`license: other`).

The printed usage example sends a text user turn and no image. The card also says the model "judges Chinese and English, text and images", and `config.json` includes a vision encoder. A chat template is present and inserts image pads. The system prompt is built by `common/handbook.py` from the value handbook; it is not a single file in the model repository. `generation_config.json` sets `do_sample` true, temperature 1.0, top_k 20, and top_p 0.95. The card's examples set `do_sample` false and `max_new_tokens` 256, and the vLLM example sets temperature 0. Held-out F1 on 18,637 samples is 0.854.

Inventory parent and LoRA match. Inventory methods omit SFT, and inventory datasets omit ToxiGen, LlavaGuard, and Hateful Memes. Match: partly.
