# iwalton3/sycofact

## Sources

- https://huggingface.co/iwalton3/sycofact/raw/main/README.md — current model card; same text as the cached card
- https://huggingface.co/api/models/iwalton3/sycofact — file list, chat template, 4,300,079,472 BF16 parameters
- https://huggingface.co/iwalton3/sycofact/raw/main/config.json — Gemma 3 config, context 131,072
- https://huggingface.co/iwalton3/sycofact/raw/main/generation_config.json — do_sample, top_k 64, top_p 0.95
- https://huggingface.co/iwalton3/sycofact/raw/main/USAGE.md — system prompt and score JSON
- https://huggingface.co/iwalton3/sycofact/raw/main/training_config.json — saved run: full finetune, 3 epochs, lr 5e-6
- https://huggingface.co/datasets/iwalton3/sycofact-training-data — released training mix, 48,078 rows
- https://huggingface.co/datasets/iwalton3/sycofact-training-data/raw/main/code/train_full_finetune.py — TRL SFTTrainer script
- https://arxiv.org/abs/2509.10970 — Psychosis-Bench paper; does not name this repository
- https://huggingface.co/datasets/truthfulqa/truthful_qa — named scenario source
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — named scenario source
- https://github.com/anthropics/evals/tree/main/sycophancy — Anthropic sycophancy evals
- https://ollama.com/izzie/sycofact — Ollama copy
- https://github.com/w-is-h/psychosis-bench — benchmark code linked from the paper

## Record

The released training set is `iwalton3/sycofact-training-data`: 37,898 evaluator train rows, 4,210 validation rows, and 5,970 Phoenix therapeutic rows, 48,078 in total. The dataset card says "No human labels. Every record was scored by a steered Gemma 3 27B." The card also names TruthfulQA, BeaverTails, Do-Not-Answer, SYCON-Bench, Chatbot Arena, and Anthropic sycophancy data as the sources of the scenarios. The script trains on the evaluator train file plus 90 percent of the Phoenix file, which is the 43,271 rows stored in `training_config.json`.

The objective is supervised fine-tuning. The script imports `SFTConfig` and `SFTTrainer` and its header says "Full finetune Gemma 3 4B" with "All parameters unfrozen, bf16." The saved config matches those defaults: 3 epochs, learning rate 5e-6, batch size 1, gradient accumulation 8. There is no LoRA rank. The base is loaded in bfloat16, so it was not quantized during training.

The parent is `google/gemma-3-4b-it`. The card says "finetuned from Gemma 3 4B IT," and `training_config.json` sets `"model_id": "google/gemma-3-4b-it"`. The card calls the size 4B.

The card presents a classifier. Input is a scenario plus an assistant reply, and the scenario can be "a user's message or conversation context," including the 16 multi-turn Psychosis-Bench cases. Output is 0–1 scores in JSON. Reasoning mode adds one-sentence reasons and feedback. The detection sentence is "designed to detect sycophancy and dangerous AI outputs." The linked paper, arXiv:2509.10970, is the Psychosis-Bench study. It does not print this repository id.

The usage example is text. `USAGE.md` gives the system prompt that starts "You evaluate AI responses for alignment quality." `generation_config.json` has `do_sample` true, top_k 64, and top_p 0.95. The Python example uses temperature 0.1 and `max_new_tokens` 256. Context length in `config.json` is 131,072. The license is `gemma`.
