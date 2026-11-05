# yueliu1999/GuardReasoner-VL-Eco-3B

## Sources

- https://huggingface.co/yueliu1999/GuardReasoner-VL-Eco-3B/raw/main/README.md — current model card; identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/yueliu1999__GuardReasoner-VL-Eco-3B__2026-10-05.md — cached card
- https://huggingface.co/api/models/yueliu1999/GuardReasoner-VL-Eco-3B — file list and safetensors count
- https://huggingface.co/yueliu1999/GuardReasoner-VL-Eco-3B/raw/main/config.json — vision-language config
- https://huggingface.co/yueliu1999/GuardReasoner-VL-Eco-3B/raw/main/generation_config.json — no sampling values
- https://huggingface.co/yueliu1999/GuardReasoner-VL-Eco-3B/raw/main/tokenizer_config.json — chat template
- https://arxiv.org/html/2505.11049 — paper HTML
- https://arxiv.org/abs/2501.18492 — earlier text-only GuardReasoner paper, listed from the card citation
- https://github.com/yueliu1999/GuardReasoner-VL — code; this repo is the 3B-Eco release
- https://github.com/yueliu1999/GuardReasoner-VL/blob/main/template.py — classifier instruction the card imports
- https://github.com/yueliu1999/GuardReasoner-VL/blob/main/result.csv — Eco-3B F1 scores
- https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain — R-SFT data, 123,093 rows, loads
- https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain-Image — image files; viewer does not load

## Record

Training data is the same corpus as the other GuardReasoner-VL checkpoints. The paper says GuardReasoner-VLTrain is "a reasoning corpus with 123K samples and 631K reasoning steps, spanning text, image, and text-image inputs." The Hub dataset has 123,093 rows and loads. The online RL set is "12K samples." GitHub also names GuardReasoner-VLTrain-Image, whose viewer does not load.

The method is full-parameter supervised fine-tuning, then GRPO. The card says this model is "a fine-tuned version of Qwen/Qwen2.5-VL-3B-Instruct via R-SFT and online RL." The paper says "we adopt the full-parameter fine-tuning" in BFloat16 for 3 epochs, learning rate 5e-5, and total batch size 192, for both the 3B and 7B bases. Online RL "implement[s] it by using group relative policy optimization (GRPO)." The Eco difference is the length penalty: "The length constrain β is set to 1 for GuardReasoner-VL, and 1/6 for GuardReasoner-VL-Eco." The GRPO actor learning rate is 1e-6 and the actor batch size is 256. There is no adapter file.

The parent is Qwen/Qwen2.5-VL-3B-Instruct. The paper calls the base "Qwen2.5-VL-Instruct 3B." The Hub weight count is 4,065,787,904 BF16 parameters. Languages on the card are en and zh. License is apache-2.0.

This is the token-shorter Eco 3B model. GitHub's Eco-3B block reports prompt-side average F1 77.39 and response-side average F1 77.14. The paper's Eco 3B row is 77.39, and its token table gives the Eco 3B combined F1 77.27 at 187.30 output tokens, against 213.32 tokens for the non-Eco 3B.

The classifier instruction, imported from `template.py`, says "You are a classifier for analyzing interactions between humans and AI" and asks whether the user request and the assistant response are harmful or unharmful. Reasoning goes in `<think>` and the result in `<result>`. The card examples include an image and allow video, so the input is not text only. The example's default model path is `yueliu1999/GuardReasoner-VL-7B`, a different repository. Sampling in the example is temperature 0, top_p 1.0, and max_tokens 4096. `config.json` sets max_position_embeddings to 128000. The tokenizer's model_max_length is 2048.
