# adzcai/AfriGuardInst-tiny-aya-global-lora-merged

## Sources

- https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-global-lora-merged/raw/main/README.md — current model card; byte-identical to the cached card (`sha256 a7498486b1aea3014652b06c06425cbb8ff169fbb2b6f23e37f60fa8e114141a`)
- https://huggingface.co/api/models/adzcai/AfriGuardInst-tiny-aya-global-lora-merged — file list and safetensors parameter count
- https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-global-lora-merged/raw/main/config.json — architecture and `max_position_embeddings` 8192
- https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-global-lora-merged/raw/main/generation_config.json — bos, eos, and pad token ids only
- https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-global-lora-merged/raw/main/tokenizer_config.json — no `chat_template` key
- https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-global-lora-merged/raw/main/chat_template.jinja — Cohere/Aya chat template and built-in preamble
- https://huggingface.co/datasets/israel/AfriGuard-inst — training dataset card (gated, manual)
- https://huggingface.co/datasets/israel/AfriGuard — human-annotated source of AfriGuard-inst
- https://huggingface.co/datasets/israel/AfriGuard-XL — second source of AfriGuard-inst; responses are model-generated
- https://huggingface.co/collections/adzcai/afriguard — author collection that lists this checkpoint
- https://datasets-server.huggingface.co/is-valid?dataset=israel/AfriGuard-inst — returned 401

## Record

The training set is `israel/AfriGuard-inst`, 46,306 train rows plus 7,175 validation rows (53,481). The card says each example is "one of the safety system instructions plus the user prompt". The dataset is gated (manual approval) and the datasets server returned 401, so it does not load anonymously. Provenance is mixed: `israel/AfriGuard` is "a human-annotated safety dataset", and `israel/AfriGuard-XL` says the response is an "English model-generated response".

The objective is supervised fine-tuning. The card says this checkpoint is "a rerun of the AfriGuard-inst config `afriguard_tinyaya_lora_sft.yaml`" with "loss on the response only". The update is LoRA, "rank 16, all linear layers", then "merged into the base weights". Learning rate 0.0001, 1 epoch, train batch size 2, gradient accumulation 4, total batch size 8. LoRA alpha, step count, and whether the base was quantized are not stated. The named LlamaFactory repo has no public URL.

The card names the parent `CohereLabs/tiny-aya-global`. No paper, GitHub file, or other page independently names that parent for this checkpoint. The Hub API repeats the card's `base_model` field. The safetensors header reports 3,349,227,520 parameters. The card lists languages en, am, ha, ig, om, sn, sw, tw, wo, yo, zu. License `cc-by-nc-4.0`.

The card presents a chat model: the target is "`<safety>…</safety>` `<category>…</category>` `<response>…</response>`", using "the chat template of the base model". The dataset card spells the target as `<safety>safe|unsafe</safety>`, a category, and `<response>final reply</response>`. That is a binary safety label, a category label, and a reply, written as XML. The model card does not name the harm categories. The AfriGuard dataset card lists ten: Criminal Activity & Exploitation; Political & Societal Manipulation; Violence & Physical Harm; Systemic Risks; Sexual & Exploitative Content; Unsafe or High-Risk Advice; Privacy & Data Misuse; Hate, Harassment & Discrimination; Ethical & Moral Risk; Intellectual Property & Content Integrity. The card reports no evaluation numbers. The Training results section is empty.

Serving is text only. `config.json` sets `max_position_embeddings` to 8192. `generation_config.json` has no temperature, top_p, top_k, or max_new_tokens. The chat template is `chat_template.jinja`. It always inserts the Cohere preamble that begins "You are in contextual safety mode" and says "Your name is Aya." There is no `adapter_config.json`.
