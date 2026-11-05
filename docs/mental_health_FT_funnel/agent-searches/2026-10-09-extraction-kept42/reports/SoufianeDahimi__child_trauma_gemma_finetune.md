# SoufianeDahimi/child_trauma_gemma_finetune

## Sources

- https://huggingface.co/SoufianeDahimi/child_trauma_gemma_finetune/raw/main/README.md — current model card; byte-identical to the cached card
- revision_3_experiments/hf_inventory/cache/readmes/SoufianeDahimi__child_trauma_gemma_finetune__2026-10-09.md — cached card (sha256 d81d2f2eda37b57b18dc20a9517a84a2afcfec6ac72a642edfbbfc2713e3b345)
- https://huggingface.co/api/models/SoufianeDahimi/child_trauma_gemma_finetune — file list, chat template, parameter count
- https://huggingface.co/SoufianeDahimi/child_trauma_gemma_finetune/raw/main/config.json — architecture, vision and audio blocks, context length
- https://huggingface.co/SoufianeDahimi/child_trauma_gemma_finetune/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/SoufianeDahimi/child_trauma_gemma_finetune/raw/main/deprecated_adapter_config.json — LoRA rank, alpha, and 4-bit base id
- https://github.com/Dahimi/Gemma3n_Finetune_Child_Trauma — training repository; README names this model id
- https://github.com/Dahimi/Gemma3n_Finetune_Child_Trauma/blob/main/finetuning/trauma_assessment_gemma_finetune.ipynb — notebook that calls SFTTrainer and push_to_hub_merged for this id
- https://github.com/Dahimi/Gemma3n_Finetune_Child_Trauma/blob/main/trauma_assessment_training.jsonl — training file, 1,440 lines, not a Hub dataset

## Record

The training file is `trauma_assessment_training.jsonl` in the GitHub repository. The README says: "This generates realistic trauma assessment conversations and corresponding professional reports." The same page says the generated dataset is that jsonl file. The file has 1,440 lines. It is not a Hugging Face dataset, so it does not load as a Hub dataset. The README describes conversations in Arabic (Palestinian, Syrian, and Sudanese dialects), Ukrainian, and English. The card YAML lists the dataset only as `custom`.

The notebook that uploads this repository uses `SFTTrainer`. It sets 3 epochs, learning rate 2e-4, batch size 1, and gradient accumulation 4. The card says "Fine-tuning Method: LoRA (r=16, alpha=16)." `deprecated_adapter_config.json` has the same rank and alpha, and its base is `unsloth/gemma-3n-e2b-it-unsloth-bnb-4bit`, so the saved adapter is LoRA on a 4-bit base. The notebook source loads `unsloth/gemma-3n-E2B-it` and does not pass `load_in_4bit`. It calls `save_pretrained_merged`. Step count is not stated.

The card YAML names the parent `google/gemma-3n-E2B-it`. The same card's prose says `unsloth/gemma-3n-E2B-it`. The notebook loads that Unsloth id. The adapter config names the 4-bit Unsloth id. Those sources do not agree with the YAML parent. No paper names this checkpoint. The GitHub README does.

The card says the model is "designed to facilitate empathetic, culturally-sensitive conversations and generate professional psychological reports." That is a support conversation, so the use claim is Strong and the output type is Chatbot. The warning is a disclaimer: "This model should not replace professional mental health assessment."

The usage example sends a text part, `{"type": "text", "text": prompt}`, with no image or audio. It uses temperature 0.7, top_p 0.95, top_k 64, and max_new_tokens 512. `generation_config.json` sets do_sample true, top_k 64, and top_p 0.95. The card sets the context length to 2,048. `config.json` sets `max_position_embeddings` to 32,768 and includes vision and audio blocks. The notebook sets `finetune_vision_layers` to false. No system prompt is stated. A chat template is present. The Hub API reports 5,976,833,472 parameters. The license on the card is apache-2.0. The card's model index has an empty results list, and no benchmark is stated.
