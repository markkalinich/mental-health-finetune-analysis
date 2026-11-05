# nvidia/Nemotron-3-Content-Safety

## Sources

- https://huggingface.co/nvidia/Nemotron-3-Content-Safety/raw/main/README.md — current model card; identical to the cached card
- revision_3_experiments/hf_inventory/cache/readmes/nvidia__Nemotron-3-Content-Safety__2026-10-05.md — cached card, sha256 559967dc72348c714c3177ea3f803d47dfff7571d0bd9cf939ff2f2ea0bdef54
- https://huggingface.co/api/models/nvidia/Nemotron-3-Content-Safety — repository file list
- https://huggingface.co/nvidia/Nemotron-3-Content-Safety/raw/main/config.json — Gemma 3 config, text context 131072, SigLIP 896
- https://huggingface.co/nvidia/Nemotron-3-Content-Safety/raw/main/generation_config.json — do_sample, top_k 64, top_p 0.95
- https://huggingface.co/nvidia/Nemotron-3-Content-Safety/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/nvidia/Nemotron-3-Content-Safety/raw/main/chat_template.jinja — safety-classifier prompt
- https://huggingface.co/blog/nvidia/nemotron-3-content-safety — NVIDIA blog that names the training blend
- https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3 — public dataset the blog names; loads
- https://huggingface.co/datasets/nvidia/Nemotron-VLM-Dataset-v2 — public dataset the card lists and the blog says was in the blend; viewer loads
- https://arxiv.org/abs/2608.27548 — Nemotron 3.5 paper found by search; HTML does not name this repository
- https://github.com/isXinLiu/MM-SafetyBench — evaluation benchmark linked from the card
- https://github.com/CryptoAILab/FigStep — evaluation benchmark linked from the card
- https://huggingface.co/datasets/MMInstruction/RedTeamingVLM — evaluation set named on the card; public
- https://huggingface.co/datasets/ys-zong/VLGuard — evaluation set; gated
- https://huggingface.co/datasets/walledai/XSTest — evaluation set; gated
- https://huggingface.co/datasets/allenai/wildguardmix — evaluation set; gated
- https://huggingface.co/datasets/ToxicityPrompts/PolyGuardPrompts — evaluation set; public
- https://huggingface.co/datasets/ToxicityPrompts/XSafety — evaluation set; public
- https://huggingface.co/datasets/ToxicityPrompts/DAMO-MultiJail — evaluation set; public
- https://huggingface.co/datasets/CohereLabs/aya_redteaming — evaluation set; public
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — taxonomy reference on the card, not stated as this model's training set

## Record

The card says the training set is "About 86k samples" and that collection was "Hybrid: Automated, Human, Synthetic." It does not name a Hub dataset in that section. The NVIDIA blog says: "It was trained using the novel, culturally aligned multilingual safety data from the Nemotron Safety Guard Dataset v3." The same blog lists the blend as Nemotron Content Safety Dataset v3 (the non-English rows taken from the adapted subset), human-annotated English multimodal data that was translated, safe image-and-prompt rows from Nemotron VLM Dataset v2, and synthetic data. It also says "synthetic data makes up only about 10% of the total training data; the majority is sourced from humans." Those two named Hub datasets are `nvidia/Nemotron-Safety-Guard-Dataset-v3` (public, loads) and `nvidia/Nemotron-VLM-Dataset-v2` (public, viewer loads; the dataset card says 8,147,599 samples in the full release). The blog does not say how many rows of each were used. The VLM dataset card says that release was used to train Nemotron Nano V2 VL, which is a different model. Evaluation sets on the card include RTVLM, VLGuard, MM-SafetyBench, FigStep, Multijail, XSafety, Aya Red-teaming, XSTest, Aegis 2, Wildguard, Polyguard, and RTP-LX. VLGuard, XSTest, and WildGuardMix are gated.

The update is LoRA, and the card says the adapter was merged: "The model was trained as a LoRA adapter and the weights were merged back into the parent Gemma-3-4b-it model." Training parameters on the card: "5 epochs, 0.0001 learning rate, rank 16, alpha 32." The optimizer is AdamW. No sentence names a loss, so the objective is not stated. Batch size, step count, and whether the base was quantized are not stated. There is no `adapter_config.json` in the repository.

The parent is google/gemma-3-4b-it. The card and the blog both say Gemma-3-4B-it. The card says 4 billion parameters. The vision encoder is SigLIP at 896 by 896.

The card calls it a classifier. It judges a user prompt, an optional image, and an optional assistant response, so the detection claim is both the input and the reply. Output is multi-line text, not JSON: "User Safety" and "Response Safety" are safe or unsafe, and "Safety Categories" is a comma-separated list. The card lists the same 23 categories as the Llama 3.1 Nemotron Safety Guard taxonomy, from Violence through Immoral/Unethical. The license is the NVIDIA Nemotron Open Model License, plus the Gemma Terms of Use and the Gemma Prohibited Use Policy.

Serving is not text-only. The card says "Input Type(s): Text, Image." The example can set the image to None. `chat_template.jinja` inserts "You are a safety classifier for analyzing interactions between humans and LLMs" into the user turn, then the 23-category taxonomy, and it appends `/no_categories` unless the caller passes `/categories`. `generation_config.json` sets do_sample true, top_k 64, and top_p 0.95. The Transformers example uses max_new_tokens 100 and do_sample false. Context is 128K on the card and 131072 in `config.json`.
