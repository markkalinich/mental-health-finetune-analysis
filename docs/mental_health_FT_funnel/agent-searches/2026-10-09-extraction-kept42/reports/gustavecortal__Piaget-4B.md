# gustavecortal/Piaget-4B

## Sources

https://huggingface.co/gustavecortal/Piaget-4B/raw/main/README.md — current model card; same text as the cached card
https://huggingface.co/api/models/gustavecortal/Piaget-4B — file list, base-model tag, parameter count, chat template
https://huggingface.co/gustavecortal/Piaget-4B/raw/main/config.json — architecture and max position embeddings
https://huggingface.co/gustavecortal/Piaget-4B/raw/main/generation_config.json — sampling defaults
https://huggingface.co/gustavecortal/Piaget-4B/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://huggingface.co/gustavecortal/Piaget-4B — model page; 4B size label and dataset viewer counts
https://huggingface.co/datasets/gustavecortal/PsychologicalReasoning-15k — filtered training set, 15,006 rows
https://huggingface.co/datasets/cognitivecomputations/dolphin-r1 — Dolphin R1 card (API id QuixiAI/dolphin-r1)
https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K — GeneralThought card (API id RJT1990/GeneralThoughtArchive)
https://aclanthology.org/2024.cmcl-1.23/ — ACL abstract of the inspiration paper
https://arxiv.org/abs/2406.10265 — arXiv abstract
https://arxiv.org/html/2406.10265 — arXiv HTML full text

## Record

The training set is the same 15,006-row set as the other Piaget sizes, gustavecortal/PsychologicalReasoning-15k, and it loads. The dataset card says "We perform domain filtering on Dolphin R1 and General Reasoning." Dolphin R1 is model-written traces: "300k reasoning samples from DeepSeek-R1, 300k reasoning samples from Gemini 2.0 flash thinking, 200k samples of Dolphin chat." The Hub page shows 814,334 rows. GeneralThought-430K says it has "430k rows" of questions plus model reasoning traces. The Piaget-4B page viewer rounds that set to 431k. The API ids are now QuixiAI/dolphin-r1 and RJT1990/GeneralThoughtArchive. The model page marks the older dataset tags disabled. The renamed pages still load. The 15k card tags language en. Its preview rows also include other languages. Dolphin does not state a language.

The card does not name a loss. It says "Clusters tagged psychology or philosophy were retained for LoRA finetuning (rank=8, alpha=16, max length=2048, epoch=1, batch size=16)." That is one epoch, batch size 16, LoRA rank 8, and alpha 16. Learning rate and step count are not stated. The repository ships two safetensors shards and no adapter file, so the published checkpoint is full weights. The card does not say the base was quantized. A GitHub config, gustavecortal/preference-optimization-orpo-lora configs/config_4b.yaml, starts from this checkpoint for a later ORPO run named roger-4b. Those settings are not this model's training.

The card's base_model is Qwen/Qwen3-4B. The Hub API tag says "base_model:finetune:Qwen/Qwen3-4B". The card lists this repo as the 4B size. Hub safetensors metadata reports 4,022,468,096 parameters, and the model page says 4B params.

The card says "Piaget aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence." That is reasoning about psychological concepts, not a claim that the model delivers therapy. The only use shown is a chat turn, so the output is a chatbot. The example user text is "Create a new psychotherapeutic technique based on cybernetic principles". The card has no warning and no evaluation. License is mit. The linked paper, Bonard and Cortal, CMCL 2024 (arXiv 2406.10265), does not print this repository id or the name Piaget.

The usage example runs pipeline("text-generation") on a text prompt, with max_new_tokens=2048 and do_sample=True. generation_config.json sets do_sample true, temperature 0.6, top_k 20, and top_p 0.95. config.json max_position_embeddings is 40960. The chat template is chat_template.jinja. It has no fixed system prompt.
