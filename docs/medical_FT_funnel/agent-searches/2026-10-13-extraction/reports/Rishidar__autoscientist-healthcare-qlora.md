# Rishidar/autoscientist-healthcare-qlora

## Sources

- https://huggingface.co/Rishidar/autoscientist-healthcare-qlora/raw/main/README.md — current model card; identical to the 10 October 2026 cache
- https://huggingface.co/api/models/Rishidar/autoscientist-healthcare-qlora — file list and safetensors parameter count
- https://huggingface.co/Rishidar/autoscientist-healthcare-qlora/raw/main/config.json — Qwen2 config, context 32768
- https://huggingface.co/Rishidar/autoscientist-healthcare-qlora/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/Rishidar/autoscientist-healthcare-qlora/raw/main/chat_template.jinja — Qwen chat template
- https://huggingface.co/Rishidar/autoscientist-healthcare-qlora/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/datasets/Rishidar/autoscientist-competition-datasets — named dataset; no dataset card; viewer cannot load it
- https://huggingface.co/datasets/Rishidar/autoscientist-competition-datasets/resolve/main/healthcare_adapted.jsonl — 60 prompt/completion rows
- https://www.kaggle.com/models/rishidard/autoscientist-healthcare-qlora — Kaggle page; description names SFT and DPO
- https://adaptionlabs.ai — linked from the card as Adaption Labs; page not read
- https://featherless.ai/models/Rishidar/autoscientist-healthcare-qlora — inference listing found by search

## Record

The card says the model was fine-tuned on the healthcare adapted dataset `Rishidar/autoscientist-competition-datasets`, “produced by Adaption Labs AutoScientist Challenge.” That dataset repository has no README. The Hub viewer cannot load it. The file `healthcare_adapted.jsonl` has 60 rows of a prompt and a completion. One prompt asks for an explanation of GLP-1 receptor agonists. `healthcare.jsonl` has 200 rows. `healthcare_v5_raw.csv` has 20,959 lines. The card does not say which file was the training set. Provenance is not stated.

The card says “Method: QLoRA (4-bit NF4, r=32, alpha=64).” Epochs 3. Learning rate 0.0002. The base was 4-bit NF4 during training. Rank 32, alpha 64. No step count and no batch size. The Hugging Face card does not name a loss. The Kaggle description says “Qwen2.5-0.5B-Instruct fine-tuned (QLoRA SFT + DPO) for healthcare.” That sentence names both supervised fine-tuning and DPO. The objective field records sft, and the quote keeps the DPO words. The repository is one F16 `model.safetensors` file, 494,032,768 parameters, and no `adapter_config.json`. The card does not say the adapter was merged. The Hub page states “Model size 0.5B params.”

The parent is `Qwen/Qwen2.5-0.5B-Instruct`. Language is English. No license is stated.

The Hugging Face card does not say what a person should use the model for. It only says it was fine-tuned on a healthcare dataset. The use claim is weak. There is no warning. No audience is named, and no function from the list is claimed. The usage snippet only loads the model, so the output type is not listed. The specialty is general: the title is “Healthcare Model,” with no field of medicine.

The Kaggle line “for healthcare” is the only purpose sentence. It does not name a clinical task.

Serving is text. The chat template defaults to “You are Qwen, created by Alibaba Cloud. You are a helpful assistant.” Generation defaults are temperature 0.7, top_p 0.8, top_k 20, repetition_penalty 1.1, and do_sample true. Context length in `config.json` is 32,768. The only evaluation line is “Dataset quality: Grade A (Adaption Labs evaluation).” No paper names this repository.
