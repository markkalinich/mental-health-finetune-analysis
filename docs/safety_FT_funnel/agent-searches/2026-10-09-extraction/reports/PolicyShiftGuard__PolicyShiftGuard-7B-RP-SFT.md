# PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT

## Sources

- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT/raw/main/README.md — current model card; identical to the cached card
- https://huggingface.co/api/models/PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT — file list and parameter count
- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT/raw/main/config.json — architecture and parent path
- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT/raw/main/generation_config.json — sampling settings
- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT/raw/main/chat_template.json — processor chat template
- https://arxiv.org/abs/2607.05910 — paper abstract
- https://arxiv.org/html/2607.05910 — paper HTML
- https://github.com/ssmisya/PolicyShiftGuard — code repository
- https://github.com/ssmisya/PolicyShiftGuard/blob/main/vllm_guard/training/sft/pipeline.py — SFT trainer
- https://github.com/ssmisya/PolicyShiftGuard/blob/main/docs/model_zoo.md — model-zoo page
- https://huggingface.co/datasets/PolicyShiftBench/PolicyShiftBench — dataset card named on the model card
- https://huggingface.co/datasets/PolicyShiftBench/PolicyShiftBench/resolve/main/manifest.json — split row counts
- https://huggingface.co/datasets/PolicyShiftBench/PolicyShiftBench/resolve/main/PolicyShiftBench_croissant.json — language and construction
- https://huggingface.co/datasets/PolicyShiftGuard/PolicyShiftBench — second Hub id named on GitHub
- https://huggingface.co/datasets/PolicyShiftGuard/adaptive-policy-v2.8-withreason — training-data repo named on GitHub
- https://policyshiftguard.github.io/ — project page
- https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/raw/main/README.md — parent card usage example

## Record

The card says this checkpoint was trained with PolicyShiftBench supervision. The public package `PolicyShiftBench/PolicyShiftBench` does not load in the Hub viewer. Its manifest gives the no-think stage-1 file 3,000 rows. Croissant says `"inLanguage": ["en"]` and `"rai:hasSyntheticData": true`, with attribute votes from multimodal annotators plus human curation and executable rules, so the construction is mixed. GitHub also names `PolicyShiftGuard/PolicyShiftBench` and `PolicyShiftGuard/adaptive-policy-v2.8-withreason`. The second repo loads. Its card says the `sft` split contains 3,000 examples. The page lists 20,224 rows in total.

The objective is SFT. The card says: "This checkpoint corresponds to the randomized-policy no-think Stage-1 SFT setting." The paper's compute table says: "Stage-1 RP-SFT | Qwen2.5-VL-7B | 4 × A100 | 3,000 examples, 4 epochs, 188 updates | 1.7 h." The recipe table gives learning rate \(10^{-5}\) for RP-SFT. No sentence says whether the update was full, LoRA, or QLoRA. The public trainer loads the full vision-language model and does not mention LoRA. The Hub repo has four safetensors shards and no `adapter_config.json`. Rank, alpha, merge, quantization during training, and batch size are not stated. The GitHub `configs/train` directory has a 3B yaml and no 7B yaml.

The card's `base_model` is `Qwen/Qwen2.5-VL-7B-Instruct`. `config.json` `_name_or_path` is a local folder, `Qwen/Qwen2.5-VL-7B-Instruct-new`. The paper names the stage-1 backbone as Qwen2.5-VL-7B. It does not print `PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT`. The project page calls this release "Stage-1 Randomized Policy SFT checkpoint, 7B."

The card presents an image guardrail, not a support conversation, and it has no therapy or medical warning. Use claim is Absent. Warning is None. The paper says the model must "output the structured decision false or true | c." That is a label, so the output type is Classifier. The Hub safetensors total is 8,292,166,656 parameters. Table 4's stage-1 7B row with randomization reports average F1 72.9. The final PolicyShiftGuard-7B scores in the abstract, 76.9 average F1 and 72.1 average PSS, are a later checkpoint.

The parent card's quickstart sends an image plus the text "Describe this image." This checkpoint's own card has no usage example. `pipeline_tag` is `image-text-to-text`. Text-only input is no. A chat template is present. If no system message is set, the template inserts "You are a helpful assistant." `generation_config.json` sets `do_sample` true, temperature `1e-06`, and repetition penalty 1.05. It does not set `top_p`, `top_k`, or `max_new_tokens`. `max_position_embeddings` is 128000. The license on the card is `apache-2.0`.
