# oopere/SmolLM2-1.7B-ClinicalNER

## Sources

- https://huggingface.co/oopere/SmolLM2-1.7B-ClinicalNER/raw/main/README.md — current model card; identical to the cached card (`cmp` exit 0)
- https://huggingface.co/api/models/oopere/SmolLM2-1.7B-ClinicalNER — repository file list and safetensors parameter count
- https://huggingface.co/oopere/SmolLM2-1.7B-ClinicalNER/raw/main/config.json — architecture and context length
- https://huggingface.co/oopere/SmolLM2-1.7B-ClinicalNER/raw/main/generation_config.json — token ids only
- https://huggingface.co/oopere/SmolLM2-1.7B-ClinicalNER/raw/main/tokenizer_config.json — tokenizer settings; no `chat_template` key
- https://huggingface.co/oopere/SmolLM2-1.7B-ClinicalNER/raw/main/chat_template.jinja — chat template
- https://huggingface.co/datasets/oopere/clinical-ner-qdora — dataset card and viewer (400 rows)
- https://github.com/peremartra/Rearchitecting-LLMs/blob/main/CH07/CH07_NB02_L4_QLoRA_QDoRA.ipynb — chapter notebook the card names
- https://arxiv.org/abs/2502.02737 — parent-model paper; does not name this repository
- https://hubs.la/Q04k2VyY0 — book link on the card, *Rearchitecting LLMs*

## Record

The training set named on the card is `oopere/clinical-ner-qdora`. The card says: "Train samples: 200 (40 per category)." It also says: "Training data is synthetic." The dataset card says the set has 400 English rows, a 90/10 split, and "This dataset was synthetically generated a combination of diferent LLMs via LiteLLM." The Hub viewer shows the rows, so the dataset loads. The notebook maps `dataset["train"]` and does not apply the 200-row cut the card describes.

The update scope is QLoRA. The card says: "Technique: QLoRA (Quantized Low-Rank Adaptation)" and "Quantization: NF4 4-bit + double quantization," with LoRA rank 8, alpha 16, 3 epochs, batch size 8, and learning rate 2e-4. The named notebook trains that QLoRA run with `SFTTrainer`, so the objective is supervised fine-tuning. The card does not print the word SFT. No step count is stated. The card says the workflow is "Train → Merge → Upload → Verify." The repository is one BF16 `model.safetensors` file and has no `adapter_config.json`, so the adapter is merged. The notebook's `merge_and_unload()` cell is on the QDoRA path, not the QLoRA save.

The parent is `HuggingFaceTB/SmolLM2-1.7B-Instruct`. The card, the Hub `base_model` field, and the notebook's `MODEL_NAME` agree. The safetensors file has 1,711,376,384 parameters. The card's language tag is `en`.

The use claim is moderate. The card says: "Given a free-text clinical note, the model extracts structured clinical entities into a strict JSON schema." The warning is a disclaimer. The card says: "Not intended for clinical or production use." It does not say "must not" or "should not be used for."

The purpose is stated. The card says the model is "for clinical named entity recognition (NER)" and calls it an "Educational model." It does not name a patient, clinician, student, or developer. The function is extract structured clinical data. This release is a chapter demonstration of QLoRA, so it is a research artifact. The output is a structured JSON object, not a chat reply and not a class label. The clinical task is information extraction from clinical notes, with no named specialty, so the specialty is general.

Serving is text only. The example note is "Patient 45yo male, fever and dry cough for 3 days." The example sets the system message to `Extract:`, generates with `max_new_tokens=256` and `do_sample=False`, and `config.json` sets `max_position_embeddings` to 8192. The card reports 95.0% schema compliance for this model on 40 test notes. The dataset card reports 100.0% for its QLoRA run. The license is `apache-2.0`.

Inventory methods `qlora`, dataset `oopere/clinical-ner-qdora`, and parent `HuggingFaceTB/SmolLM2-1.7B-Instruct` match the card. The inventory does not record the supervised fine-tuning loss the notebook uses.
