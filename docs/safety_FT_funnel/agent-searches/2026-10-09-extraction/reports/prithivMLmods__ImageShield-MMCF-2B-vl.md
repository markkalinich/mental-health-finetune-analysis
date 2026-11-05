# prithivMLmods/ImageShield-MMCF-2B-vl

## Sources

https://huggingface.co/prithivMLmods/ImageShield-MMCF-2B-vl/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/prithivMLmods__ImageShield-MMCF-2B-vl__2026-10-09.md — cached card, sha256 6b07966a58a2c20c1b1239d03ae315a999d6e754e72791c769f8d7febb12be30
https://huggingface.co/api/models/prithivMLmods/ImageShield-MMCF-2B-vl — file list, parameter count, and chat template
https://huggingface.co/prithivMLmods/ImageShield-MMCF-2B-vl/raw/main/config.json — vision-language architecture and context length
https://huggingface.co/prithivMLmods/ImageShield-MMCF-2B-vl/raw/main/generation_config.json — sampling defaults
https://huggingface.co/prithivMLmods/ImageShield-MMCF-2B-vl/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://huggingface.co/datasets/prithivMLmods/ImageShield-Guardrail-Multimodal-20K — dataset page, 28,000 rows, gated
https://huggingface.co/api/datasets/prithivMLmods/ImageShield-Guardrail-Multimodal-20K — dataset metadata; gated manual
https://huggingface.co/blog/prithivMLmods/vision-guardrail-mini-blog — author's blog naming this checkpoint and its base model

## Record

The card says the model was trained on ImageShield-Guardrail, Hub id `prithivMLmods/ImageShield-Guardrail-Multimodal-20K`, and "Approximately 20,000 multimodal samples." The dataset page says "28,000 paired image-text instances" and "Total Samples: 28,000 rows." The dataset is gated: the raw README returns 401, and the page says loading requires an authorized token, so it does not load here. Language is English. The dataset page does not say whether the images or the labels are human or synthetic.

The training table says "Training Objective | Content-safety guardrail classification" and "Training Framework | TRL." That is a classification objective. The card does not say full fine-tuning, LoRA, or QLoRA, and it does not give rank, epochs, steps, learning rate, or batch size. The acknowledgements say TRL includes "Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO)." That sentence describes the library. It does not say this checkpoint was trained with those methods. The repository has three safetensors shards and no `adapter_config.json`.

The card says the base model is `Qwen/Qwen3-VL-2B-Instruct`. The same author's blog table lists "ImageShield-MMCF-2B-vl | Qwen3-VL-2B-Instruct | ImageShield-Guardrail-Multimodal-20K." Those agree. No paper and no GitHub training repository turned up.

The model is a classifier. The card says it classifies visual content as Safe or Unsafe and returns JSON with a caption, `is_nsfw`, a reason, and 1/0 flags. There is no mental-health claim. The limitation "The model should not be treated as a definitive legal or safety determination" is about the classifier, not therapy or medical advice. The Hub file header counts 2,127,532,032 parameters. The license line is `apache-2.0`. The inventory's method list `dpo|grpo|sft` is not what the card states. The dataset id and the parent match.

Serving takes an image. The usage example passes `images=[image]` and asks the model to classify the image. A chat template is present in `chat_template.jinja`. The published instruction begins "You are a strict, zero-tolerance parental control content-safety guardrail classifier for visual media." `generation_config.json` sets `do_sample` true, temperature 0.7, top_k 20, and top_p 0.8. The example uses `max_new_tokens=256`. Context length in `config.json` is 262,144. The card shows example JSON outputs and does not report a scored evaluation.
