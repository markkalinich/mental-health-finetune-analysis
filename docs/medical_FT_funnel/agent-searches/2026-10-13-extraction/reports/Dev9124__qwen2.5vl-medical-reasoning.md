# Dev9124/qwen2.5vl-medical-reasoning

## Sources

https://huggingface.co/Dev9124/qwen2.5vl-medical-reasoning/raw/main/README.md — current model card; same text as the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/Dev9124__qwen2.5vl-medical-reasoning__2026-10-10.md — cached card, sha256 619e5470006ac1f9e6218f5f60f04ae829503dd737dc06cf8bba0c7efe6e1e8b
https://huggingface.co/api/models/Dev9124/qwen2.5vl-medical-reasoning — file list, parameter count, chat template
https://huggingface.co/Dev9124/qwen2.5vl-medical-reasoning/raw/main/config.json — vision-language architecture and context length
https://huggingface.co/datasets/robailleo/medical-vision-llm-dataset — dataset named in the card YAML
https://arxiv.org/abs/2502.13923 — Qwen2.5-VL Technical Report; does not name this repository
https://github.com/unslothai/unsloth — library link in the Unsloth template sentence

## Record

The card YAML names one dataset, robailleo/medical-vision-llm-dataset. That dataset loads. Its card says it has 4,793 rows, of which the source counts are "ROCO: 3000 samples" and "VQA-RAD: 1793 samples." It says VQA-RAD is "Visual question answering for radiology with expert annotations." It also lists PubMedVision, which is not in those counts. The model card does not say which split was used.

The only training sentence is "This qwen2_5_vl model was trained 2x faster with Unsloth and Huggingface's TRL library." That is the Unsloth upload template. It does not name a loss, LoRA, or QLoRA. The body says "Finetuned from model : unsloth/qwen2.5-vl-7b-instruct-unsloth-bnb-4bit," so the named starting checkpoint is a 4-bit model. Epochs, learning rate, and batch size are not stated. The repository is full weights, with no adapter file. config.json sets unsloth_version to 2025.9.10.

The YAML says the base model is unsloth/Qwen2.5-VL-7B-Instruct. The body names unsloth/qwen2.5-vl-7b-instruct-unsloth-bnb-4bit. Those are different repository ids. No paper names this checkpoint. The safetensors header counts 8,292,166,656 parameters.

The card does not say what the model is for, who it is for, or what medical work it does. The use claim is Weak because the YAML names a medical dataset and the prose is the upload template. There is no warning. The pipeline tag is image-text-to-text, and the architecture is Qwen2_5_VLForConditionalGeneration, so the input is not text only. The chat template's default system line is "You are a helpful assistant." config.json sets max_position_embeddings to 32768. The license is apache-2.0. The inventory parent matches the YAML and not the body line, so the match is partial.
