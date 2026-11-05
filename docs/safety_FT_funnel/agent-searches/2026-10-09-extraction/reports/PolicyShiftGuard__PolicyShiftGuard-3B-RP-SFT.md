# PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT

## Sources

- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT/raw/main/README.md — current model card; identical to the cached card
- https://huggingface.co/api/models/PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT — file list and parameter count
- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT/raw/main/config.json — architecture and parent path
- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT/raw/main/generation_config.json — sampling settings
- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT/raw/main/chat_template.json — processor chat template
- https://arxiv.org/abs/2607.05910 — paper abstract
- https://arxiv.org/html/2607.05910 — paper HTML
- https://github.com/ssmisya/PolicyShiftGuard — code repository
- https://github.com/ssmisya/PolicyShiftGuard/blob/main/configs/train/sft_qwen25vl_3b.yaml — 3B SFT defaults
- https://github.com/ssmisya/PolicyShiftGuard/blob/main/vllm_guard/training/sft/pipeline.py — SFT trainer
- https://github.com/ssmisya/PolicyShiftGuard/blob/main/docs/model_zoo.md — model-zoo page
- https://github.com/ssmisya/PolicyShiftGuard/blob/main/docs/reproducibility.md — reproduction commands
- https://huggingface.co/datasets/PolicyShiftBench/PolicyShiftBench — dataset card named on the model card
- https://huggingface.co/datasets/PolicyShiftBench/PolicyShiftBench/resolve/main/manifest.json — split row counts
- https://huggingface.co/datasets/PolicyShiftBench/PolicyShiftBench/resolve/main/PolicyShiftBench_croissant.json — language and construction
- https://huggingface.co/datasets/PolicyShiftGuard/PolicyShiftBench — second Hub id named on GitHub
- https://huggingface.co/datasets/PolicyShiftGuard/adaptive-policy-v2.8-withreason — training-data repo named on GitHub
- https://policyshiftguard.github.io/ — project page
- https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/raw/main/README.md — parent card usage example

## Record

The card says this checkpoint was trained with PolicyShiftBench supervision. The public package `PolicyShiftBench/PolicyShiftBench` does not load in the Hub viewer (`viewer: false`; the page says the splits use different data file formats). Its manifest gives the no-think stage-1 file `stage1_rp_sft_random.parquet` 3,000 rows. Croissant says `"inLanguage": ["en"]` and `"rai:hasSyntheticData": true`, and the collection note says attributes come from multimodal annotators plus human curation and executable rules, so the construction is mixed. GitHub also names `PolicyShiftGuard/PolicyShiftBench` (same file list, viewer also false) and `PolicyShiftGuard/adaptive-policy-v2.8-withreason` as "Training data". That second repo loads. Its card says the `sft` split contains 3,000 examples and the page lists 20,224 rows in total.

The objective is SFT. The card says: "This checkpoint corresponds to the randomized-policy no-think Stage-1 SFT setting." The paper's recipe table says RP-SFT uses cross-entropy on `true | XX` or `false`, "4 epochs, no-think output, LR 10^{-5}". The GitHub file `configs/train/sft_qwen25vl_3b.yaml` instead sets `num_train_epochs: 6`, `per_device_train_batch_size: 1`, `gradient_accumulation_steps: 8`, and `learning_rate: 1e-5`. No sentence says whether the update was full, LoRA, or QLoRA. The public trainer loads `AutoModelForVision2Seq` and a Hugging Face `Trainer` and does not mention LoRA. The Hub repo has two safetensors shards and no `adapter_config.json`. Rank, alpha, merge, quantization during training, step count, and the batch size of this run are not stated. The paper's 188 updates are for the 7B stage-1 job.

The card's `base_model` is `Qwen/Qwen2.5-VL-3B-Instruct`. `config.json` `_name_or_path` ends in that same model id. The paper says PolicyShiftGuard-3B and PolicyShiftGuard-7B "both initialized from Qwen2.5-VL backbones." It does not print `PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT`. The project page calls this release "Stage-1 Randomized Policy SFT checkpoint, 3B."

The card presents an image guardrail, not a support conversation, and it has no therapy or medical warning. Use claim is Absent. Warning is None. The output is a short decision. The paper says the model must "output the structured decision false or true | c." That is a label, so the output type is Classifier. The Hub safetensors total is 4,065,787,904 parameters. Table 4's stage-1 3B row with randomization reports average F1 65.8 (Adaptive F1 85.2, Shift F1 46.4). The card says this is not the final PolicyShiftGuard-3B model.

The parent card's quickstart sends an image plus the text "Describe this image." This checkpoint's own card has no usage example. `pipeline_tag` is `image-text-to-text`. Text-only input is no. A chat template is present. If no system message is set, the template inserts "You are a helpful assistant." `generation_config.json` sets `do_sample` true, temperature 0.1, `top_p` 0.001, `top_k` 1, and repetition penalty 1.05. `max_position_embeddings` is 128000. The license on the card is `apache-2.0`.
