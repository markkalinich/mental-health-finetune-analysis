# gustavecortal/Piaget-0.6B

## Sources

- https://huggingface.co/gustavecortal/Piaget-0.6B — current model card; same bytes as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/gustavecortal__Piaget-0.6B__2026-10-09.md — cached card, sha256 7613324255e7a3383635440b05041abe7c93876a0934235f6c19bff5ed41ea69
- https://huggingface.co/api/models/gustavecortal/Piaget-0.6B — file list; safetensors total 596,049,920 BF16 parameters
- https://huggingface.co/gustavecortal/Piaget-0.6B/raw/main/config.json — max position embeddings 40960
- https://huggingface.co/gustavecortal/Piaget-0.6B/raw/main/generation_config.json — temperature 0.6, top_k 20, top_p 0.95, do_sample true
- https://huggingface.co/gustavecortal/Piaget-0.6B/raw/main/tokenizer_config.json — no chat_template key; model_max_length 131072
- https://huggingface.co/gustavecortal/Piaget-0.6B/raw/main/chat_template.jinja — Qwen-style chat template
- https://huggingface.co/datasets/gustavecortal/PsychologicalReasoning-15k — filtered training set, 15,006 rows
- https://huggingface.co/datasets/cognitivecomputations/dolphin-r1 — source dataset; states an 800k-sample mix of model traces
- https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K — source dataset; states 430k rows
- https://aclanthology.org/2024.cmcl-1.23/ — inspiration paper abstract; does not name this repository
- https://arxiv.org/abs/2406.10265 — same paper on arXiv
- https://arxiv.org/html/2406.10265 — HTML full text; does not contain Piaget or this repository id
- https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_0.6b.yaml — later ORPO config that loads this checkpoint as a base
- https://huggingface.co/mradermacher/Piaget-0.6B-GGUF — community GGUF of this checkpoint
- https://gustavecortal.com — website named on the card

## Record

The card says Piaget "was finetuned on a subset of open reasoning traces from Dolphin R1 and General Reasoning." The dataset `gustavecortal/PsychologicalReasoning-15k` is that filter: 15,006 English train rows, and it loads. Its card says: "We perform domain filtering on Dolphin R1 and General Reasoning." Dolphin R1's card says: "We create a 800k sample dataset" made of "300k reasoning samples from DeepSeek-R1," "300k reasoning samples from Gemini 2.0 flash thinking," and "200k samples of Dolphin chat." GeneralThought-430K's card says it "contains questions, reference answers, reasoning traces, final answers and other metadata from several popular reasoning models" and "has 430k rows," and it also credits question sources such as Numina. The 15k set is a mix of those model traces with questions that GeneralThought says were sourced from other datasets. Dolphin R1 does not state a language.

The card does not name a loss. It says: "Clusters tagged psychology or philosophy were retained for LoRA finetuning (rank=8, alpha=16, max length=2048, epoch=1, batch size=16)." That is one epoch, batch size 16, LoRA rank 8, and alpha 16. Learning rate and step count are not stated. The repository ships `model.safetensors` and has no `adapter_config.json`. Nothing says whether the LoRA was merged, or whether the base was quantized during training. A GitHub file, `config_0.6b.yaml`, points `base_path` at this checkpoint and sets `output_dir: roger-0.6b` under an ORPO block. That file trains another model on top of Piaget. It is not the training of this checkpoint.

The card YAML names the parent `Qwen/Qwen3-0.6B`. The 15k dataset card says: "Piaget, a language model based on Qwen3 and finetuned on PsychologicalReasoning-15k." The card calls this size 0.6B. The Hub file list counts 596,049,920 parameters.

The card presents a reasoning model, not a conversation partner. It says: "Piaget aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence." That is a Weak use claim. The card has no sentence about therapy, diagnosis, or medical use. The example runs `pipeline("text-generation")` on one user string, "Create a new psychotherapeutic technique based on cybernetic principles," with `max_new_tokens=2048` and `do_sample=True`. `generation_config.json` sets temperature 0.6, top_k 20, and top_p 0.95. Context length in `config.json` is 40,960. No system prompt is set in the example. No evaluation numbers are reported. The 2024 CMCL paper linked as inspiration does not name this repository. Inventory method, datasets, and parent match the card.
