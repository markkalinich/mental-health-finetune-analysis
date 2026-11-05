# airesearch/Qwen3-30B-A3B-medqa

## Sources

- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/README.md — current trainer card; same hyperparameters as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/airesearch__Qwen3-30B-A3B-medqa__2026-10-05.md — cached card, sha256 412005c24c89ae3406cd6ec9dc83fb9b5b883332be68301ed1162c169da766c6
- https://huggingface.co/api/models/airesearch/Qwen3-30B-A3B-medqa — file list and Qwen3 chat template
- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/adapter_config.json — LoRA rank 8, alpha 16, local base path
- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/dataset/train/dataset_info.json — tokenized train split, 48,876 rows, local medqa.json
- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/dataset/validation/dataset_info.json — repeats the same local file and the same 48,876 count
- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/all_results.json — final train and eval loss
- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/train_results.json — same train loss and runtime
- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/config.json — context length 40960, float32, 128 experts
- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/generation_config.json — sampling settings
- https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/Modelfile — Ollama template, num_ctx 4096
- https://arxiv.org/abs/2505.09388 — Qwen3 technical report for the base series; does not name this repository
- https://huggingface.co/datasets/bigbio/med_qa — one public MedQA page found by search; not identified as this run's file
- https://huggingface.co/datasets/awinml/medqa — another public MedQA page; not identified as this run's file

## Record

The card says the model was fine-tuned "on the medqa dataset" and then says the training data section is "More information needed." The repository's `dataset_info.json` points at a local file, `/lustrefs/disk/home/ptuchind/LLaMA-Factory/data/medqa.json`, and records 48,876 train examples. Those rows are already tokenized (`input_ids`, `attention_mask`, `labels`). Image, video, and audio fields are null. No Hub dataset id is in the file. Public MedQA pages have different sizes, so this record does not assign one of them. The validation info file repeats the same path and the same 48,876 count.

The card does not name a loss. It says "fine-tuned." The adapter file says `peft_type` is `LORA`, rank 8, alpha 16. The adapter is a separate `adapter_model.safetensors`, so it is not merged. Nothing in the adapter file says the base was quantized. The card's trainer block says learning rate 0.0002, 3 epochs, and per-device batch size 2, with a total batch of 1024 on 64 devices. The loss table runs through step 120. A `checkpoint-129` folder is also in the repository. `all_results.json` does not print a global step.

The card's parent is Qwen/Qwen3-30B-A3B. The adapter config names a local directory, `/project/lt200252-wcbart/pumet/models/Qwen3-30B-A3B`. That is the same model name. No paper names this repository. The Qwen3 technical report is about the base series.

The use claim is weak. The only medical sentence is that it was fine-tuned on medqa, and the intended-use section says "More information needed." There is no warning about diagnosis or medical advice. The purpose is not stated, so the audience list and the function list are empty. The named dataset is MedQA, which is an exam set, so the task recorded here is exam answering. No specialty is named. The reported evaluation is a loss of 0.0275, not an accuracy.

Serving is text in and text out. A Qwen3 chat template is present and does not set a medical system prompt. The Ollama file does the same: it writes a system turn only when one is supplied, and it sets `num_ctx` to 4096. `generation_config.json` sets do_sample true, temperature 0.6, top_k 20, and top_p 0.95. `config.json` sets max_position_embeddings to 40960. The card does not state a parameter count. The license field is `other`.
