# lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical

## Sources

- https://huggingface.co/lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical/raw/main/README.md — current model card; same text as the cache
- https://huggingface.co/api/models/lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical — file list and parameter count
- https://huggingface.co/lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical/raw/main/config.json — Gemma 4 text, vision, and audio config
- https://huggingface.co/lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical/raw/main/generation_config.json — sampling defaults
- https://github.com/LukasDrews97/Gemma-4-IT-SFT-RLVR-Medical — training repository; prints this model id
- https://github.com/LukasDrews97/Gemma-4-IT-SFT-RLVR-Medical/blob/main/QLORA_SFT.py — SFT LoRA script
- https://github.com/LukasDrews97/Gemma-4-IT-SFT-RLVR-Medical/blob/main/config.py — sample counts, epochs, USE_QLORA false
- https://github.com/LukasDrews97/Gemma-4-IT-SFT-RLVR-Medical/blob/main/hf_datasets/pubmedqa_dataset.py — which PubMedQA splits are loaded
- https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md — PubMedQA dataset card
- https://arxiv.org/abs/1909.06146 — PubMedQA paper; does not name this repository
- https://arxiv.org/html/2606.16517v1 — a paper that uses Gemma 4 E2B as a backbone; does not name this repository
- https://huggingface.co/lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical-GGUF — quantized copies named on the card
- https://featherless.ai/models/lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical — inference host page that prints this repository id

## Record

The card says the model was fine-tuned on PubMedQA. The linked GitHub loads `pubmed_qa` / `pqa_artificial` for training and `pqa_labeled` for the test set. `pqa_artificial` has 211,269 rows. The script keeps 1,024 of them for SFT and 256 for the RLVR stage, after a 50/50 split with seed 123. The test slice is 1,000 labeled rows. The dataset card language is English. Its YAML lists both expert-generated and machine-generated annotations, so provenance for the dataset as published is mixed. The Hub dataset loads.

The card says: "Gemma-4-E2B-it fine-tuned on PubMedQA using SFT and RLVR." The recorded objective is SFT, because that is the named loss in the allowed list that the card prints. The same GitHub then runs `GRPO_RLVR.py`. The SFT script always builds a LoRA config: rank 16, alpha 16, dropout 0.05, all linear modules. `config.py` sets `USE_QLORA = False`, so the checked-in run does not load the base in 4-bit. SFT uses 3 epochs, learning rate 5e-5, and batch size 8. The Hub upload is five full bfloat16 shards and has no `adapter_config.json`. Nothing says the adapter was merged.

The parent is `google/gemma-4-E2B-it` on the card and in `MODEL_ID`. The Hub API reports 5,506,950,723 bfloat16 parameters. Licence is `apache-2.0`. The inventory row matches the dataset and the parent. It lists only sft, and the card also names RLVR.

The card does not say who the model is for. The use claim is Weak. There is no warning. Audiences and functions are empty. The GitHub sample answer ends with "Final Decision: yes" after a paragraph, so the output kind is reasoning and an answer. The usage example is a single user question, so the output type is a chatbot. The training task is exam answering on PubMedQA. MedQA-USMLE is marked zero-shot transfer: 43.05%, against 29.54% for the base. PubMedQA in-domain is 73.10%, against 58.10% for the base. The specialty tag is biomedical.

The published example is text only: "Do GEC produce and bear factor H under complement attack?" `config.json` is `Gemma4ForConditionalGeneration` and also contains vision and audio configs. A chat template is present and does not fix a system prompt. `generation_config.json` sets temperature 1.0, top_p 0.95, top_k 64, and do_sample true. The example asks for 1,024 new tokens. Text `max_position_embeddings` is 131072.
