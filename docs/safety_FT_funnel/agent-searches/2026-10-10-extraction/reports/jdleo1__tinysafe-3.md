# jdleo1/tinysafe-3

## Sources

- https://huggingface.co/jdleo1/tinysafe-3/raw/main/README.md — current model card; same text as the cached card
- https://huggingface.co/api/models/jdleo1/tinysafe-3 — file list and chat template
- https://huggingface.co/jdleo1/tinysafe-3/raw/main/config.json — Qwen3 config, context 262,144
- https://huggingface.co/jdleo1/tinysafe-3/raw/main/generation_config.json — temperature 0.7, top_k 20, top_p 0.8
- https://github.com/jdleo/tinysafe-3 — training code; README names this Hub repository
- https://raw.githubusercontent.com/jdleo/tinysafe-3/main/scripts/04_train.py — QLoRA SFTTrainer script
- https://raw.githubusercontent.com/jdleo/tinysafe-3/main/scripts/01_prepare_data.py — which datasets the prep script loads
- https://raw.githubusercontent.com/jdleo/tinysafe-3/main/configs/config.json — rank 16, 3 epochs, learning rate 2e-4
- https://jdleo.me/blog/tinysafe-v3 — author's account of the v3.4 run
- https://huggingface.co/datasets/google/civil_comments — comments used as Jigsaw unintended-bias data
- https://huggingface.co/datasets/lmsys/toxic-chat — named training source
- https://huggingface.co/datasets/allenai/wildguardmix — named training source; gated
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — listed in the card YAML

## Record

The card's training table lists ToxicChat train 5,082, WildGuard train 4,000, hard negatives 694, synthetic boundary 679, and surgical synthetic 388, and it states a total of about 16,700. The blog says "388 samples in 16,727." Those rows are mixed: ToxicChat keeps human labels and adds teacher reasoning, WildGuard is relabeled, and the boundary rows are generated. `scripts/01_prepare_data.py` loads `lmsys/toxic-chat`, `google/civil_comments`, `google/jigsaw_toxicity_pred`, and `allenai/wildguardmix`. It does not load BeaverTails. BeaverTails appears only in the card YAML.

The objective is teacher distillation. The card says "Fine-tuned with QLoRA (4-bit NF4, r=16, alpha=32) via teacher distillation from Claude Sonnet 4.6." The student step in `scripts/04_train.py` is `SFTTrainer` on a 4-bit NF4 base. The card says the weights are "4B (full merged)." The trainer config sets 3 epochs, learning rate 2e-4, and batch size 4 with gradient accumulation 8. The blog says the v3.4 run was 1 epoch, then 2 more epochs at half that learning rate.

The parent is `Qwen/Qwen3-4B-Instruct-2507`. The card and `configs/config.json` both name that base. The card says 4B parameters.

The card presents a safety classifier. Input is one user message, for example "how do i make a bomb." Output is JSON with a boolean `safe`, a category list, and one sentence of reasoning. The categories it names are violence, hate, sexual, self_harm, dangerous_info, harassment, and illegal_activity. The system prompt also calls offensive language, stereotyping, and jailbreak attempts unsafe.

The example is text. The system prompt is printed on the card, starting "You are a safety classifier." `generation_config.json` has `do_sample` true, temperature 0.7, top_k 20, and top_p 0.8. The card example is greedy with `max_new_tokens` 128. Context length is 262,144. The license is MIT. No paper is linked.
