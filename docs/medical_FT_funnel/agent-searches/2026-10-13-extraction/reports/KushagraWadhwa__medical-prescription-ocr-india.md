# KushagraWadhwa/medical-prescription-ocr-india

## Sources

https://huggingface.co/KushagraWadhwa/medical-prescription-ocr-india/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/KushagraWadhwa/medical-prescription-ocr-india — repository file list, base model, and parameter count
https://huggingface.co/KushagraWadhwa/medical-prescription-ocr-india/raw/main/config.json — architecture and context length
https://huggingface.co/KushagraWadhwa/medical-prescription-ocr-india/raw/main/generation_config.json — sampling settings
https://huggingface.co/KushagraWadhwa/medical-prescription-ocr-india/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://huggingface.co/KushagraWadhwa/medical-prescription-ocr-india/raw/main/chat_template.jinja — chat template
https://huggingface.co/datasets/naazimsnh02/medocr-vision-dataset — dataset card
https://huggingface.co/api/datasets/naazimsnh02/medocr-vision-dataset — dataset is public and not gated
https://github.com/KushagraaWadhwa/Patient-Monitoring — repository linked on the card; returns 404

## Record

The card says the training set is `naazimsnh02/medocr-vision-dataset`: "1,969 training samples / 246 validation samples" of "Scanned and photographed Indian medical prescriptions (handwritten and printed), labelled with structured JSON ground truth." The dataset card says something broader. "Total Samples: 2,462." The split counts are 1,969 train, 246 validation, and 247 test. It is "59.4% Medical / 40.6% General": 1,000 handwritten prescriptions, 36 OMR forms, 426 printed lab reports, and 1,000 invoices and receipts. "Languages: English." Labels are mixed: "Direct Extraction" from existing annotations and "LLM-based Extraction: Using Nebius and Novita APIs for image-to-text conversion." The Hub dataset is public, not gated, and the viewer shows rows, so it loads. The card's Hindi and India-only prescription description is not what the dataset card says.

The objective is supervised fine-tuning. The card says "Objective: Causal language modelling on image+text → structured JSON sequences" and lists `trl` (`SFTTrainer` / `SFTConfig`). The update is QLoRA. "Fine-tuning method: QLoRA (Quantized Low-Rank Adaptation) via PEFT" and "Quantization: 4-bit NF4 (bitsandbytes) with double quantization." LoRA rank is 16 and alpha is 32, on `q_proj`, `v_proj`, `k_proj`, `o_proj`, `gate_proj`, `up_proj`, and `down_proj`. Epochs are 3. Learning rate is 2e-4. Per-device batch size is 1, with gradient accumulation 8 (effective batch size 8). Steps are not stated. The repo ships `model.safetensors` and no `adapter_config.json`. The card does not say the adapter was merged.

The parent is Qwen/Qwen2.5-VL-3B-Instruct. The card says "Finetuned from model: Qwen/Qwen2.5-VL-3B-Instruct" and "3B parameter." The Hub API `base_model` field is the same id. Safetensors total is 3,754,622,976 float16 parameters. The linked GitHub repository returns 404. Searches for the repo id and the model name did not find a paper that names this checkpoint.

The use claim is moderate. The card says "Extract structured data from medical prescription images" and "it does not provide medical advice." The warning is a disclaimer. "Not a substitute for a qualified pharmacist or clinician review." Out of scope includes "Diagnosing patients or making clinical decisions." The recommendations say "Do not use this model as the sole source of truth for medication dispensing or clinical workflows," which still allows use after a person checks the output. License is Apache 2.0. Evaluation is loss on 246 validation samples and a qualitative claim of field accuracy. No numeric score is given.

The purpose is stated. "A vision-language model fine-tuned to extract structured information from handwritten and printed Indian medical prescriptions." The card names systems (EMR, pharmacy data entry, hospital digitisation) and does not name a person, so audiences are empty.

The function is extract structured clinical data. The same sentence says a prescription image "returns a JSON object containing doctor details, patient details, medications (with dosage, frequency, duration), diagnosis, and notes."

The clinical task is information extraction. The specialty is general medicine: the card says medical prescriptions and does not name a field. The output is a JSON object, not a chat turn. Output type is a non-conversational tool.

The example takes an image plus a text instruction, so the input is not text only. `chat_template.jinja` is present. The card's system prompt begins "You are a medical prescription OCR assistant." The template's own fallback line is "You are a helpful assistant." `generation_config.json` sets `do_sample` true, `repetition_penalty` 1.05, and `temperature` 1e-06. The card example uses `max_new_tokens=512` and `do_sample=False`. `text_config.max_position_embeddings` is 128000. `tokenizer_config.json` sets `model_max_length` to 131072. Training truncated sequences to 512 tokens.
