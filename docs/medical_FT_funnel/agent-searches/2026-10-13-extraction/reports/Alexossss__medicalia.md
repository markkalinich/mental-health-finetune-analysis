# Alexossss/medicalia

## Sources

https://huggingface.co/Alexossss/medicalia/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/Alexossss/medicalia — repository file list and parameter count
https://huggingface.co/Alexossss/medicalia/raw/main/adapter_config.json — LoRA adapter settings
https://huggingface.co/Alexossss/medicalia/raw/main/final_checkpoint/adapter_config.json — same LoRA settings in the checkpoint folder
https://huggingface.co/Alexossss/medicalia/raw/main/config.json — architecture and context length
https://huggingface.co/Alexossss/medicalia/raw/main/generation_config.json — token ids only
https://huggingface.co/Alexossss/medicalia/raw/main/tokenizer_config.json — chat template and system prompt
https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms — dataset card
https://huggingface.co/api/datasets/QuyenAnhDE/Diseases_Symptoms — dataset loads; public CSV, 400 rows
https://github.com/huggingface/trl — TRL library cited on the card, not this model's training code
https://wandb.ai/alexandredsb-pro-universit-savoie-mont-blanc/huggingface/runs/em5dufak — linked training run; the page did not load

## Record

The training set is QuyenAnhDE/Diseases_Symptoms. The card says: "This model is a fine-tuned version of HuggingFaceTB/SmolLM2-135M-Instruct on the QuyenAnhDE/Diseases_Symptoms dataset." The dataset card says "The data was sourced from various medical websites accessible through Google search" and "Dataset Information: 400 x 4", with columns Code, Name, Symptoms, and Treatments. The Hub dataset is public and the viewer shows 400 rows, so it loads. Language is not stated. Provenance is human web text.

The objective is supervised fine-tuning. The card says "This model was trained with SFT." The update is LoRA. `adapter_config.json` has `"peft_type": "LORA"`, `"r": 16`, and `"lora_alpha": 32`, on `q_proj`, `k_proj`, `v_proj`, and `o_proj`. The card does not say LoRA. Epochs, steps, learning rate, and batch size are not stated. The linked Weights & Biases run did not load. No file says the base was quantized. Both `model.safetensors` and `adapter_model.safetensors` are in the repo, and no file says whether the adapter was merged.

The parent is HuggingFaceTB/SmolLM2-135M-Instruct. The card, `adapter_config.json` (`base_model_name_or_path`), and `config.json` (`_name_or_path`) all name that checkpoint. The Hub API reports 134515008 parameters.

The use claim is weak. The only medical sentence is the fine-tune sentence above. There is no warning. The YAML key is the misspelled `licence` and the value is the placeholder word `license`. No evaluation is reported. Searches for the repo id and the name `medicalia` did not find a paper or a training repository for this checkpoint.

No sentence says what the model is for or who it is for. The opening paragraph is a trainer template, and the quick-start question is about a time machine. Audiences are empty. Functions are empty.

The quick start is a chat turn: `generator([{"role": "user", "content": question}], max_new_tokens=128)`. That is a chat reply. No clinical task and no specialty are named.

The example runs on text only. `tokenizer_config.json` has a chat template. The system line is "You are a helpful AI assistant named SmolLM, trained by Hugging Face". `max_position_embeddings` and `model_max_length` are 8192. The example sets `max_new_tokens=128`. `generation_config.json` does not set temperature or other sampling values.
