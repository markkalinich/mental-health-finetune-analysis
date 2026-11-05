# hudson5/llama-3-8b-chat-doctor

## Sources

- https://huggingface.co/hudson5/llama-3-8b-chat-doctor/raw/main/README.md — current model card; identical to the cached card
- https://huggingface.co/api/models/hudson5/llama-3-8b-chat-doctor — repository file list and parameter count
- https://huggingface.co/hudson5/llama-3-8b-chat-doctor/raw/main/config.json — architecture and context length
- https://huggingface.co/hudson5/llama-3-8b-chat-doctor/raw/main/generation_config.json — generation token ids
- https://huggingface.co/hudson5/llama-3-8b-chat-doctor/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/hudson5/llama-3-8b-chat-doctor/raw/main/adapter_config.json — LoRA settings and base path
- https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot — dataset page, public and ungated
- https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot/raw/main/README.md — dataset card, 256,916 train rows
- https://huggingface.co/api/datasets/ruslanmv/ai-medical-chatbot — dataset API
- https://arxiv.org/abs/1910.09700 — carbon-calculator paper linked from the card template; does not name this repository
- https://arxiv.org/html/1910.09700 — HTML of that paper; does not name this repository
- https://arxiv.org/abs/2407.21783 — Llama 3 paper returned by search; does not name this repository; not read in full
- https://featherless.ai/models/hudson5/llama-3-8b-chat-doctor — inference host page that prints this repository id

## Record

The card names one dataset, `ruslanmv/ai-medical-chatbot`, in its YAML (`datasets: ruslanmv/ai-medical-chatbot`). The dataset card says: "This is an experimental Dataset designed to run a Medical Chatbot It contains at least 250k dialogues between a Patient and a Doctor." The Hub dataset info lists 256,916 train examples with fields Description, Patient, and Doctor. The dataset page and API load; the dataset is public. The dataset card does not state a language or whether the dialogues are human or synthetic. The card body under Training Data says "[More Information Needed]".

The card does not name a loss. `adapter_config.json` says `"peft_type": "LORA"`, `"r": 16`, `"lora_alpha": 32`, and `"task_type": "CAUSAL_LM"`. Causal language modeling is the adapter task type, not a named objective such as SFT. Epochs, steps, learning rate, and batch size are not in the card or the adapter file. The repository contains both `adapter_model.safetensors` and four float16 model shards, and nothing says whether the adapter was merged. `Q4_K_M` and `Q4_K_S` GGUF files are in the repository; the adapter file does not say the base was quantized during training.

The card YAML says `base_model: meta-llama/Meta-Llama-3-8B-Instruct`. The adapter file says `"base_model_name_or_path": "/kaggle/input/llama-3/transformers/8b-chat-hf/1"`, the Kaggle copy of Llama 3 8B chat. Those name the same parent. The Hub API reports 8,030,277,632 float16 parameters.

The only purpose sentence is "A model used for medical chat, use it with caution!" That is a chatbot presented for medical conversation, so the use claim is Strong. "use it with caution!" does not forbid diagnosis, treatment, or advice, and it is not a "not a substitute" or "not medical advice" disclaimer, so the warning strength is None. The rest of the card is the generated template, including the carbon-calculator link to Lacoste et al. 2019, which does not name this checkpoint.

The purpose is stated: medical chat. The card does not name a patient, a clinician, a student, or a researcher. The functions list is empty because "medical chat" does not name a listed function such as answering questions or talking with a patient.

The clinical task is other, from "A model used for medical chat, use it with caution!" The specialty is general: the card says medical and names no field. The output is a chat reply. No evaluation result is stated. No licence is stated.

Serving is text only: the described use is medical chat, and `config.json` is `LlamaForCausalLM` with no image or audio processor. A chat template is present in `tokenizer_config.json` and does not fix a system prompt. `generation_config.json` sets token ids only. `max_position_embeddings` is 8192.
