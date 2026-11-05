# gustavecortal/Piaget-1.7B

## Sources

https://huggingface.co/gustavecortal/Piaget-1.7B/raw/main/README.md — current model card; same text as the cached card
https://huggingface.co/api/models/gustavecortal/Piaget-1.7B — file list, base-model tag, parameter count, chat template
https://huggingface.co/gustavecortal/Piaget-1.7B/raw/main/config.json — architecture and max position embeddings
https://huggingface.co/gustavecortal/Piaget-1.7B/raw/main/generation_config.json — sampling defaults
https://huggingface.co/gustavecortal/Piaget-1.7B/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://huggingface.co/gustavecortal/Piaget-1.7B — model page; size label and model tree
https://huggingface.co/datasets/gustavecortal/PsychologicalReasoning-15k — filtered training set, 15,006 rows
https://huggingface.co/api/datasets/gustavecortal/PsychologicalReasoning-15k — dataset loads, not gated
https://huggingface.co/datasets/cognitivecomputations/dolphin-r1 — Dolphin R1 card (API id QuixiAI/dolphin-r1)
https://huggingface.co/api/datasets/cognitivecomputations/dolphin-r1 — Dolphin R1 loads
https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K — GeneralThought card (API id RJT1990/GeneralThoughtArchive)
https://huggingface.co/api/datasets/GeneralReasoning/GeneralThought-430K — GeneralThought loads
https://aclanthology.org/2024.cmcl-1.23/ — ACL abstract of the inspiration paper
https://arxiv.org/abs/2406.10265 — arXiv abstract
https://arxiv.org/html/2406.10265 — arXiv HTML full text

## Record

The training set is gustavecortal/PsychologicalReasoning-15k, 15,006 rows, and it loads. The dataset card says "We perform domain filtering on Dolphin R1 and General Reasoning." Dolphin R1 says it is "300k reasoning samples from DeepSeek-R1, 300k reasoning samples from Gemini 2.0 flash thinking, 200k samples of Dolphin chat." The Hub page shows 814,334 rows, and the API id is now QuixiAI/dolphin-r1. GeneralThought-430K says it has "430k rows" of questions plus reasoning traces from DeepSeek-R1 and other models, and the API id is now RJT1990/GeneralThoughtArchive. Both of those pages still open from the ids on the Piaget card. The 15k card tags language en. Its preview rows also include French, Russian, Sinhala, Telugu, and German. Dolphin does not state a language.

The card does not name a loss. It says "Clusters tagged psychology or philosophy were retained for LoRA finetuning (rank=8, alpha=16, max length=2048, epoch=1, batch size=16)." That is one epoch, batch size 16, LoRA rank 8, and alpha 16. Learning rate and step count are not stated. The repository ships model.safetensors and has no adapter_config.json, so the published checkpoint is a full weight file. The card does not say the base was quantized. A GitHub search hit, gustavecortal/preference-optimization-orpo-lora, starts from this checkpoint for a later ORPO run named roger-1.7b. That config is not how Piaget-1.7B was trained.

The card's base_model is Qwen/Qwen3-1.7B. The Hub API tag says the same thing: "base_model:finetune:Qwen/Qwen3-1.7B". The model page also shows Qwen/Qwen3-1.7B-Base above Qwen/Qwen3-1.7B in the tree. The card calls this the 1.7B size. Hub safetensors metadata reports 1,720,574,976 parameters, and the model page labels that as a 2B size bucket.

The card says "Piaget aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence." That is a reasoning model with mental-health subject matter, not a claim that it delivers therapy or support. The only use shown is a chat turn, so the output is a chatbot: the example user text is "Create a new psychotherapeutic technique based on cybernetic principles". The card has no warning, disclaimer, or evaluation. License is mit. The linked paper, Bonard and Cortal, CMCL 2024 (arXiv 2406.10265), is a position paper on emotion analysis. Its HTML does not print this repository id or the name Piaget.

The usage example runs pipeline("text-generation") on a text prompt, with max_new_tokens=2048 and do_sample=True. generation_config.json sets do_sample true, temperature 0.6, top_k 20, and top_p 0.95. config.json max_position_embeddings is 40960. The chat template is chat_template.jinja. It has no fixed system prompt.
