# prithivMLmods/OneDecision-VisionGuard-27B-SFT

## Sources

https://huggingface.co/prithivMLmods/OneDecision-VisionGuard-27B-SFT/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/prithivMLmods__OneDecision-VisionGuard-27B-SFT__2026-10-09.md — cached card, sha256 5ed9a27a79f112d2a91540bd35863308c6144103b77fe6c8bef36dbf6922f54c
https://huggingface.co/api/models/prithivMLmods/OneDecision-VisionGuard-27B-SFT — file list, parameter count, and chat template
https://huggingface.co/prithivMLmods/OneDecision-VisionGuard-27B-SFT/raw/main/config.json — architecture and context length 262,144
https://huggingface.co/prithivMLmods/OneDecision-VisionGuard-27B-SFT/raw/main/generation_config.json — sampling defaults
https://huggingface.co/prithivMLmods/OneDecision-VisionGuard-27B-SFT/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://huggingface.co/datasets/prithivMLmods/ImageShield-OneDecision-Classification — dataset page, 30,622 rows, gated
https://huggingface.co/api/datasets/prithivMLmods/ImageShield-OneDecision-Classification — dataset metadata; gated manual
https://huggingface.co/strangeropshf/job-term-10_05-L — gated page the card calls the initial training run; it names this repository and does not show a method
https://github.com/PRITHIVSAKTHIUR/OneDecision-VisionGuard-Demo — demo repository; README and file list, no training script
https://huggingface.co/spaces/prithivMLmods/OneDecision-VisionGuard-Demo — demo space linked from the card
https://huggingface.co/prithivMLmods/OneDecision-VisionGuard-27B-SFT-GGUF — sibling quant card that repeats the same parent sentence

## Record

The card says the model was trained on ImageShield-OneDecision-Classification, Hub id `prithivMLmods/ImageShield-OneDecision-Classification`. The dataset page says it has 30,622 train rows, each an image plus a JSON string in a `Decision` column, and that it was refined from ImageShield-Guardrail-Pro. The dataset is gated, so it does not load here. Language is English. The page does not say whether the images or the labels are human or synthetic.

The card tags the model `SFT` and says it was "Fine-tuned on" that dataset. It does not say full fine-tuning, LoRA, or QLoRA, and it does not give rank, epochs, steps, learning rate, or batch size. The acknowledgements say TRL includes "Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO)." That sentence describes the library. It does not say this checkpoint was trained with DPO or GRPO. The repository has eleven safetensors shards and no `adapter_config.json`. The linked GitHub repository is a demo for the 9B sibling, with a note that the app can also run the 27B. It has no training script.

The card says the base model is `Qwen/Qwen3.8-27B`. The GGUF card repeats that sentence. The gated job page says "Initial training for https://huggingface.co/prithivMLmods/OneDecision-VisionGuard-27B-SFT" and does not name a parent or a method. No paper turned up.

The model is a classifier. The card says it classifies visual content as Safe or NSFW and returns JSON with a scene description, `is_nsfw`, a reason, and 1/0 flags. There is no mental-health claim. The limitation "The model should not be treated as a definitive legal or safety determination" is about the classifier, not therapy or medical advice. The card says it is a "dense 27-billion-parameter" model. The weight-file header counts 27,356,728,560 parameters. The license line is `apache-2.0`. The inventory's method list `dpo|grpo|sft` matches the SFT tag and does not match a stated DPO or GRPO run. The dataset id and the parent match.

Serving takes an image. The usage example passes an image URL and the text "Classify this image as safe or nsfw." The published instruction begins "You are a strict content-safety guardrail classifier for images designed for parental control and minor protection." The card says that longer prompt is optional for Transformers and is the one to use with the GGUF files. A chat template is present and inserts its own default system text when no system message is passed. `generation_config.json` sets `do_sample` true, temperature 1.0, top_k 20, and top_p 0.95. The example uses `max_new_tokens=256`. Context length in `config.json` is 262,144. The card shows three example JSON outputs and does not report a scored evaluation.
