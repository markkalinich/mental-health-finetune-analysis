# yushaohan/ProGuard-3B

## Sources

- https://huggingface.co/yushaohan/ProGuard-3B/raw/main/README.md — model card; live page text matches the cache
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/yushaohan__ProGuard-3B__2026-10-09.md — cached card
- https://huggingface.co/api/models/yushaohan/ProGuard-3B — file list and safetensors count
- https://huggingface.co/yushaohan/ProGuard-3B/raw/main/config.json — architecture, context length, actor checkpoint path
- https://huggingface.co/yushaohan/ProGuard-3B/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/yushaohan/ProGuard-3B/raw/main/chat_template.jinja — chat template
- https://arxiv.org/html/2512.23573 — ProGuard paper HTML
- https://arxiv.org/abs/2602.12092 — DeepSight paper cited on the card, not read in full
- https://github.com/yushaohan/ProGuard — training and deploy instructions
- https://github.com/yushaohan/ProGuard/tree/master/deploy — text, image, and text-image inference examples
- https://github.com/AI45Lab/DeepSafe — linked from the card as a user of the model
- https://yushaohan.github.io/ProGuard/ — project page
- https://huggingface.co/datasets/yushaohan/ProGuard-data — training data, 87,024 rows

## Record

The training set is `yushaohan/ProGuard-data`. Its card says "This dataset is multimodal data used to train ProGuard-7B and ProGuard-3B." The Hub page reports 87,024 rows, and the viewer shows them. The paper says the set has "87K samples, each annotated with both binary safety labels and risk categories." Language on the dataset card is en. The rows mix sources such as GuardReasoner and Aegis with model-assisted labels.

The method is GRPO, with no supervised fine-tuning stage. The paper says "We bypass the SFT stage entirely and adopt pure GRPO training." Appendix C lists learning rate 1e-6, batch size 512, group size 16, and 1 epoch, then says "The training is performed on the Qwen2.5-VL-7B-Instruct backbone." Those numbers are not stated for this 3B checkpoint. No sentence says whether the 3B update was full or LoRA. The released repo has full safetensors and no adapter file. `config.json` points `_name_or_path` at `ckpt-3b/global_step_138/actor/huggingface`.

The card's base model is Qwen/Qwen2.5-VL-3B-Instruct. The paper's training writeup names Qwen2.5-VL-7B as the backbone it details, and it evaluates a separate ProGuard-3B. The Hub weight count is 4,065,787,904 BF16 parameters. The card language is en. The card does not state a license.

The card says ProGuard "identify and reason about unknown risks across both text and visual modalities, moving beyond rigid predefined classification systems." Deploy examples take a user request plus an assistant reply, a text-image pair, or an image alone. The paper scores binary safety labels and risk categories, and it says the model describes out-of-distribution risks. Prompt-harm F1 numbers for ProGuard-3B in the paper include 82.51, 89.20, 77.02, 99.50, 95.03, 86.44, 88.25, and 88.49. It also says ProGuard improves OOD risk detection by 52.6% and OOD risk description by 64.8%.

Serving is not text-only. `generation_config.json` sets do_sample true, temperature 1e-6, and repetition_penalty 1.05. `config.json` sets max_position_embeddings to 128000. A chat template is present and inserts "You are a helpful assistant." when no system message is given. The card does not print a safety system prompt. GitHub trains with verl via `proguard-train.sh`.
