# ecorbari/Gemma-2b-it-Psych-Merged

## Sources

- https://huggingface.co/ecorbari/Gemma-2b-it-Psych-Merged — current model card; same bytes as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/ecorbari__Gemma-2b-it-Psych-Merged__2026-10-09.md — cached card, sha256 c16b442d55e1cc8373a6a066ad5c77b3a9d1d07d5a898175384e09d7d5bee7c4
- https://huggingface.co/api/models/ecorbari/Gemma-2b-it-Psych-Merged — file list and safetensors parameter count 2506172416
- https://huggingface.co/ecorbari/Gemma-2b-it-Psych-Merged/raw/main/config.json — max position embeddings 8192
- https://huggingface.co/ecorbari/Gemma-2b-it-Psych-Merged/raw/main/generation_config.json — token ids only
- https://huggingface.co/ecorbari/Gemma-2b-it-Psych-Merged/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/ecorbari/Gemma-2b-it-Psych-Merged/raw/main/chat_template.jinja — chat template; rejects a system role
- https://huggingface.co/ecorbari/Gemma-2b-it-Psych — adapter repository card
- https://huggingface.co/ecorbari/Gemma-2b-it-Psych/raw/main/adapter_config.json — LoRA rank 16, alpha 32, parent google/gemma-2b-it
- https://github.com/edersoncorbari/fine-tune-llm — README naming this merged repository, the dataset, and the loss numbers
- https://github.com/edersoncorbari/fine-tune-llm/blob/main/notebooks/02_GEMMA2B_FINE_TUNING.ipynb — training notebook
- https://github.com/edersoncorbari/fine-tune-llm/blob/main/notebooks/03_GEMMA2B_MERGE_LORA.ipynb — merge notebook; prints this repository URL
- https://github.com/NeuroQuestAi/fine-tune-llm — second GitHub page found by search; same notebook names
- https://huggingface.co/datasets/jkhedri/psychology-dataset — dataset page; no dataset card README (404)
- https://datasets-server.huggingface.co/size?dataset=jkhedri/psychology-dataset — 9,846 rows, viewer valid
- https://huggingface.co/ecorbari/Gemma-2b-it-Psych-GGUF — GGUF sibling linked from the project README
- https://medium.com/@ecorbari/beyond-helpfulness-specialized-fine-tuning-for-empathetic-ai-with-gemma-2b-and-qlora-afcb08dea000 — article linked from the GitHub README; fetch returned 403

## Record

The training notebook loads `jkhedri/psychology-dataset` with `split="all"`. The Hub dataset page has no README. The datasets server reports 9,846 rows in one train split, and the viewer is valid, so the dataset loads. Columns on the viewer are `question`, `response_j`, and `response_k`. The notebook says: "This is a preference/comparison dataset where `response_j` (empathetic/therapeutic) and `response_k` (judgmental/aggressive) represent opposite poles." It trains only on `response_j`. No source states who wrote the rows or what language the dataset card assigns. The model card's language line is English.

The notebook that trains the adapter calls `SFTTrainer` and says: "This step starts the supervised fine-tuning process, optimizing the model to generate empathetic psychological responses." The same notebook's opening says the setup is "rather than relying on standard supervised fine-tuning" and mentions "DPO-style methods," but the code does not call a DPO trainer. It builds a 4-bit NF4 `BitsAndBytesConfig` and the cell title says: "Sets up 4-bit quantization using bitsandbytes (QLoRA)." LoRA rank is 16 and alpha is 32, in both the notebook and `adapter_config.json`. Training arguments set 1 epoch, learning rate `2e-4`, and `per_device_train_batch_size=1` with `gradient_accumulation_steps=2`. No step count is set. The merge notebook loads `google/gemma-2b-it` in float16, attaches `ecorbari/Gemma-2b-it-Psych`, and calls `merge_and_unload()`. The card says the same: "This model integrates the LoRA adapter weights from ecorbari/Gemma-2b-it-Psych directly into the base model using the `merge_and_unload()` process."

The card, the training notebook, and `adapter_config.json` all name the parent `google/gemma-2b-it`. The card does not print a parameter count. The Hub API reports 2,506,172,416 parameters in `model.safetensors`.

The card presents a text conversation model. It says: "The model is optimized to generate empathetic, supportive, and professionally aligned psychological responses." Intended uses include "Proof-of-concept psychological support tools." That is a Strong use claim. The warning says: "This model is NOT a substitute for licensed mental health professionals. It must not be used for diagnosis or treatment." The training system prompt is "You are a compassionate mental health assistant." The chat template rejects a system role, and the notebook pastes that sentence into the user turn.

The card's example runs `pipeline("text-generation")` on the string "I feel anxious and overwhelmed lately. What should I do?" with `max_new_tokens=200`. Context length in `config.json` is 8192. The GitHub README reports eval loss about 0.60–0.70 and perplexity about 1.82–2.01 for this fine-tune. No arXiv paper names this repository. Inventory dataset and parent match. Inventory method `lora` is the LoRA family; the training load is 4-bit, so the update scope is QLoRA.
