# AIML-TUDA/QwenGuard-v1.2-7B

## Sources

https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-7B/raw/main/README.md — current model card; identical to the cached card (sha256 160c67fbe76d2e1c6e4f10ab9371340b34fd0230592d6c34bb755f383fe59291)
https://huggingface.co/api/models/AIML-TUDA/QwenGuard-v1.2-7B — file list, safetensors count, and tokenizer chat template
https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-7B/raw/main/config.json — architecture and context length
https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-7B/raw/main/generation_config.json — sampling settings
https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-7B/raw/main/trainer_state.json — epoch, step, batch, and logged learning rate
https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-7B/raw/main/all_results.json — train and eval loss
https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-7B/raw/main/train_results.json — train loss
https://huggingface.co/AIML-TUDA/QwenGuard-v1.2-7B/raw/main/eval_results.json — eval loss
https://arxiv.org/abs/2406.05113 — paper abstract
https://arxiv.org/html/2406.05113 — paper HTML; names QwenGuard-7B, not this repository id
https://arxiv.org/html/2605.18915 — other paper found by search; listed only, not read in full
https://github.com/ml-research/LlavaGuard — project repository README
https://github.com/ml-research/LlavaGuard/blob/main/scripts/train/QwenGuard2.5-v1.2/QwenGuard2.5-v1.2-7b.yaml — LLaMA-Factory YAML whose epoch and learning rate do not match this checkpoint's trainer log
https://ml-research.github.io/human-centered-genai/projects/llavaguard/index.html — project page; demo is AIML-TUDA/LlavaGuard-7B, not this repository
https://huggingface.co/api/datasets/AIML-TUDA/LlavaGuard — training dataset metadata; data files did not load (gated)
https://huggingface.co/api/datasets/AIML-TUDA/smid — SMID copy named from the card; gated

## Record

The card says this checkpoint was trained on LlavaGuard-DS, which is the Hub dataset AIML-TUDA/LlavaGuard. The dataset card says the language is English. The dataset is gated, and the dataset README and the datasets server both returned 401, so it did not load. The paper says the set has 5,466 images (4,571 train, 71 eval, 824 test), with human safety ratings and categories and synthetically generated rationales. This repository's eval run processed about 71 examples (43.821 samples per second times 1.6202 seconds), which matches that eval split. The card's access form also says the model is "a derivative model based on webscraped images and the SMID dataset." AIML-TUDA/smid is a gated copy of that image set. Its card says the original set has 2,941 images.

No source that matches this checkpoint's trainer log names a loss. `trainer_state.json` in this repository records `num_train_epochs` 2, `global_step` 136, `train_batch_size` 5, and a logged learning rate that rises to 5e-5 and then falls. The card tags include `freeze`, `llama-factory`, and `generated_from_trainer`. Freeze is not one of the recorded update scopes (full, lora, qlora, adapter_other). There is no `adapter_config.json`. The GitHub file `QwenGuard2.5-v1.2-7b.yaml` sets `stage: sft`, `finetuning_type: full`, 3 epochs, and learning rate 1.0e-5 on `Qwen/Qwen2.5-VL-7B-Instruct`. Those epoch and learning-rate values do not match this repository's trainer log, so that YAML is not the record of this run. The paper's Appendix B says 3 epochs, learning rate 2e-5, and batch size 1 "for both models, 0.5B and 7B." That also does not match this trainer log, and the paper does not print `AIML-TUDA/QwenGuard-v1.2-7B`.

The card and `config.json` both name the parent `Qwen/Qwen2.5-VL-7B-Instruct`. The card says "We here provide the transformer weights for QwenGuard v1.2 7B." The Hub file list reports 8,292,166,656 BF16 parameters. The model card does not state a license.

The card presents a vision safeguard, not a conversation partner: "QwenGuard is a vision safeguard model that assesses images based on a provided safety policy, providing safety rating, safety category and a rationale." That is a classifier. There is no claim that it delivers therapy or support. The access form says "LlavaGuard is mainly targeted toward researchers and is meant to be used in research." That is a research and legal limitation, not a prohibition on therapy.

The card's example sends an image plus the policy text. `generation_config.json` sets temperature 0.1, top_p 0.001, top_k 1, repetition_penalty 1.05, and do_sample true. The example uses max_new_tokens 128. `config.json` sets max_position_embeddings to 128000. The tokenizer chat template inserts "You are a helpful assistant." when no system message is given. This repository's `eval_results.json` reports eval_loss 0.6118338704109192. The paper's table for a model it calls QwenGuard-7B reports balanced accuracy 89.71, recall 88.89, precision 87.91, and policy exception score 84.57, without printing this repository id.
