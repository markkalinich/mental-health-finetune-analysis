# ThxZ3US/Medicalia

## Sources

https://huggingface.co/ThxZ3US/Medicalia/raw/main/README.md — current model card; identical to the 10 October 2026 cache (sha256 df4edbb0374c692888e0c50d83dc7b69b8a82b950786f685179328a18a190b55)
https://huggingface.co/api/models/ThxZ3US/Medicalia — file list and parameter count
https://huggingface.co/ThxZ3US/Medicalia/raw/main/config.json — Llama text architecture and context length
https://huggingface.co/ThxZ3US/Medicalia/raw/main/generation_config.json — token ids only
https://huggingface.co/ThxZ3US/Medicalia/raw/main/tokenizer_config.json — chat template and SmolLM system line
https://huggingface.co/ThxZ3US/Medicalia/raw/main/adapter_config.json — LoRA rank and alpha
https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms — training dataset; 400 rows; the viewer loads
https://github.com/huggingface/trl — TRL library linked from the card
https://wandb.ai/baptistegriva-universit-savoie-mont-blanc/huggingface/runs/2sruo1a7 — run link on the card; the page redirected and was not read

## Record

The card says this is a fine-tune of HuggingFaceTB/SmolLM2-135M-Instruct on QuyenAnhDE/Diseases_Symptoms. That dataset loads. It has 400 rows. The card says "The data was sourced from various medical websites accessible through Google search" and "Dataset Information: 400 x 4". The listed fields are Code, Name, Symptoms, and Treatments, each followed by "More Information Needed". The card does not state a language. The viewer rows are English disease names.

The card says "This model was trained with SFT." `adapter_config.json` is LoRA, rank 16, alpha 32, on `HuggingFaceTB/SmolLM2-135M-Instruct`, with no quantization fields. The repository also contains `model.safetensors` (134,515,008 BF16 parameters) and a second copy of the adapter under `final_checkpoint/`. The card does not say whether the full file is a merge. `training_args.bin` is present. It is a pickle, so the epoch count, learning rate, and batch size were not read. The linked Weights & Biases run was not readable.

The parent on the card and in the adapter config is HuggingFaceTB/SmolLM2-135M-Instruct.

The card does not say who the model is for. It only names the dataset. There is no medical warning. The YAML line `licence: license` is a placeholder, not a license name.

The quick start is a chat pipeline. The example question is the stock TRL time-machine prompt, not a medical question. The card does not name a clinical task or a specialty. The dataset columns include symptoms and treatments, and the card does not say how those columns were turned into training text.

The example is text. `config.json` is `LlamaForCausalLM` with max position 8,192 and no vision config. The chat template inserts "You are a helpful AI assistant named SmolLM, trained by Hugging Face" when the caller does not send a system message. The example sets `max_new_tokens` to 128. `generation_config.json` does not set temperature or top-p. No paper names this checkpoint. The GitHub link is the TRL library.
