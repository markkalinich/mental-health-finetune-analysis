# MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged

## Sources

https://huggingface.co/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/MilyaShams__DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged__2026-10-05.md — cached card, sha256 503af6a1036af562df97d8b7c2b93b16bb18f3ab0d2db2ef8cb0de6d17ff5331
https://huggingface.co/api/models/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged — file list and parameter count
https://huggingface.co/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged/raw/main/config.json — architecture and context length
https://huggingface.co/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged/raw/main/generation_config.json — sampling settings
https://huggingface.co/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged/raw/main/tokenizer_config.json — chat template
https://huggingface.co/collections/MilyaShams/deepseek-r1-distill-qwen-15b-medical-models-67cc39de5fd9f4c5d8fd837b — collection that includes this checkpoint
https://github.com/MilyaushaShamsutdinova/MedAdapt-LLM — project README
https://github.com/MilyaushaShamsutdinova/MedAdapt-LLM/blob/main/notebooks/continual_pretrain.ipynb — training notebook that names this repository
https://huggingface.co/datasets/MedRAG/textbooks — textbook snippets, 125,847 rows, loads
https://huggingface.co/datasets/MilyaShams/MedRAG_statpearls — author StatPearls snippets, 334,231 rows, loads
https://huggingface.co/datasets/MedRAG/statpearls — official StatPearls card; no content files
https://arxiv.org/html/2402.13178 — MedRAG paper HTML; does not name this repository
https://arxiv.org/abs/2501.12948 — DeepSeek-R1 paper; does not name this repository
https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1 paper; does not name this repository

## Record

The model card is an Unsloth template. It does not name a dataset. The training notebook does. It loads MedRAG/textbooks and MilyaShams/MedRAG_statpearls, concatenates them, and trains on the `contents` field plus an end-of-sequence token. The textbook set loads and states 125,847 snippets from 18 medical textbooks. The author's StatPearls set loads and states 334,231 train rows. The README's "460K text snippets" matches those two counts added together. The official MedRAG/statpearls repository says StatPearls content cannot be redistributed and contains no data files. Both corpora are published textbook and article text, so the provenance is human. Neither dataset card states a language code.

The notebook says this file "produces" this repository by "continual pretraining" on medical texts. It loads the base in 4-bit (`load_in_4bit = True`) and adds LoRA with rank 8 and alpha 16, including the embedding and output head, with `use_rslora=True`. That is QLoRA. It trains for `num_train_epochs=1`, learning rate 1e-5, embedding learning rate 5e-6, and per-device batch size 2 with gradient accumulation 8. A checkpoint path in the notebook is `checkpoint-27317`. The notebook calls `merge_and_unload()`. This repository has full BF16 weights (1,777,088,000 parameters) and no adapter file. One push cell writes a different id ending in `-f32`.

The card says the parent is unsloth/deepseek-r1-distill-qwen-1.5b. The notebook sets `model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"`. Those are different repository ids. The inventory parent matches the card, aside from case. The inventory method field is empty.

The card does not say what the model is for. The notebook does: "incorporating medical knowledge into LLM by continual pretraining it on datasets containing medical texts," and it calls the result an intermediate model for a later instruction-tuning step. That is medical training with no stated use for a patient or a clinician. There is no warning that forbids diagnosis or treatment. No audience is named. No function from the study list is claimed for this checkpoint. The written training target is raw corpus text, not a chat reply, an exam letter, or a diagnosis. Specialty is medical with no narrower field: the collection says the models are "fine-tuned for adapting to medical domain."

The README's percentage table is for the base, RAG, SFT, and MSFT models. It does not print a benchmark score for this continual-pretrain checkpoint. It does say continual pretraining ran for one epoch and shows a loss-curve image. License is apache-2.0. Context length in config.json is 131072. generation_config.json sets temperature 0.6, top_p 0.95, and do_sample true. Training sequences were capped at 4096. The chat template is present and leaves the system prompt empty. Input in the training notebook is text.
