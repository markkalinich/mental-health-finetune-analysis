# yueliu1999/GuardReasoner-VL-7B

## Sources

- https://huggingface.co/yueliu1999/GuardReasoner-VL-7B/raw/main/README.md — current model card; identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/yueliu1999__GuardReasoner-VL-7B__2026-10-05.md — cached card
- https://huggingface.co/api/models/yueliu1999/GuardReasoner-VL-7B — file list and safetensors count
- https://huggingface.co/yueliu1999/GuardReasoner-VL-7B/raw/main/config.json — vision-language config
- https://huggingface.co/yueliu1999/GuardReasoner-VL-7B/raw/main/generation_config.json — no sampling values
- https://huggingface.co/yueliu1999/GuardReasoner-VL-7B/raw/main/tokenizer_config.json — chat template
- https://arxiv.org/abs/2505.11049 — paper abstract
- https://arxiv.org/html/2505.11049 — paper HTML
- https://proceedings.neurips.cc/paper_files/paper/2025/hash/2a02b560822d564119fe3ac3be024ac6-Abstract-Conference.html — NeurIPS 2025 abstract
- https://arxiv.org/abs/2501.18492 — earlier text-only GuardReasoner paper, listed from the card citation
- https://github.com/yueliu1999/GuardReasoner-VL — code, training scripts, and this repo id
- https://github.com/yueliu1999/GuardReasoner-VL/blob/main/result.csv — reported F1 scores
- https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain — R-SFT training data
- https://huggingface.co/datasets/yueliu1999/GuardReasoner-VLTrain-Image — image files named on GitHub; viewer does not load

## Record

Training data is GuardReasoner-VLTrain. The paper says it is "a reasoning corpus with 123K samples and 631K reasoning steps, spanning text, image, and text-image inputs," with reasoning "generated via prompting GPT-4o." The Hub dataset has 123,093 rows (63,799 text, 13,264 image, 46,030 text-image) and the viewer returns rows. GitHub also releases GuardReasoner-VLTrain-Image; that dataset's viewer does not load. The online RL stage uses a derived set: "We obtain training data for online RL, consisting of 12K samples." A commented line on the card names GuardReasonerTrain. The paper and GitHub name GuardReasoner-VLTrain.

The method is supervised fine-tuning, then GRPO. The card says the model is "a fine-tuned version of Qwen/Qwen2.5-VL-7B-Instruct via R-SFT and online RL." The paper says "we cold-start our model's reasoning ability via SFT" and "We implement it by using group relative policy optimization (GRPO)." For R-SFT it says "we adopt the full-parameter fine-tuning," BFloat16, 3 epochs, learning rate 5e-5, and total batch size 192. For GRPO the actor learning rate is 1e-6 and the actor batch size is 256. There is no adapter file.

The parent is Qwen/Qwen2.5-VL-7B-Instruct. The paper trains "Qwen2.5-VL-Instruct 7B." The Hub weight count is 8,292,166,656 BF16 parameters. The card languages are en and zh. License is apache-2.0.

The card's own heading is "GuardReasoner-VL-Eco-7B," and its usage example defaults to that other repo id. GitHub lists this repository as the 7B model and `yueliu1999/GuardReasoner-VL-Eco-7B` as the Eco model. The GitHub score for GuardReasoner-VL-7B is average F1 79.07, the paper's non-Eco 7B number. The paper sets the length penalty beta to 1 for GuardReasoner-VL and to 1/6 for Eco.

The model is a classifier. The instruction says "You are a classifier for analyzing interactions between humans and AI" and asks whether the human request is harmful or unharmful and whether the assistant response is harmful or unharmful. Reasoning goes in `<think>` and the result in `<result>`. The examples include a text dialogue, an image, and a text-image pair, and the loader allows video. It is not text-only.

Serving uses that instruction as the system message. The example sets temperature 0, top_p 1.0, and max_tokens 4096. `config.json` sets max_position_embeddings to 128000. The tokenizer's model_max_length is 2048, which matches the paper's R-SFT cutoff. A chat template is in `tokenizer_config.json`.
