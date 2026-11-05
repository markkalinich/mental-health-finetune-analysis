# miike-ai/4o-3b-medical

## Sources

- https://huggingface.co/miike-ai/4o-3b-medical/raw/main/README.md — current card; identical to the cache (sha256 6b9b497091f4a4d4d2e0753a8c409b401834313696386f866c3ada62ef74a859). The file is only a YAML block.
- https://huggingface.co/api/models/miike-ai/4o-3b-medical — file list; 3,212,749,824 bfloat16 parameters
- https://huggingface.co/miike-ai/4o-3b-medical/raw/main/config.json — LlamaForCausalLM, context 131072
- https://huggingface.co/miike-ai/4o-3b-medical/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
- https://huggingface.co/miike-ai/4o-3b-medical/raw/main/tokenizer_config.json — Llama 3.2 chat template
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — dataset named in the YAML; viewer loads
- https://arxiv.org/abs/2412.18925 — paper cited by that dataset for HuatuoGPT-o1; it does not name this repo
- https://github.com/FreedomIntelligence/HuatuoGPT-o1 — code linked from the dataset card, not from this model card
- https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/raw/main/README.md — parent card; HTTP 401, not read

## Record

The only training data the card names is `FreedomIntelligence/medical-o1-reasoning-SFT`. The dataset card says “This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier.” It also says “This dataset is used to fine-tune HuatuoGPT-o1,” which is a different model. The viewer loads four configs: English 19,704 rows, English mix 24,887, Chinese 20,171, Chinese mix 25,358. The model card does not say which config was used, so the example count is unfilled. Languages on the dataset card are English and Chinese. Provenance is synthetic. The dataset license is Apache-2.0. That is not a license for this model.

No sentence says how this checkpoint was trained. The letters SFT inside the dataset id are not a statement of the loss. No sentence says LoRA, QLoRA, or a full update. The repo has three bfloat16 weight shards and no `adapter_config.json`. Epochs, steps, learning rate, and batch size are absent.

The parent on the card is `meta-llama/Llama-3.2-3B-Instruct`. No paper, GitHub README, or other page found by search prints `miike-ai/4o-3b-medical`. The parent card is gated. The file total is 3,212,749,824 parameters. The card does not state a size or a language.

The card has no description. The use claim is weak because the YAML names a medical dataset and the card states no purpose. There is no warning. Purpose is not stated. No audience is named. No function is claimed. No clinical task or specialty is named on the card. The dataset card’s task tags are question answering and text generation, for HuatuoGPT-o1’s data, not a sentence about this checkpoint. Output type is not listed. Output kind is not stated.

There is no usage example, so text-only input is not stated. The config is a text Llama, and the repo has no image processor. A chat template is present. With no system message it still writes “Cutting Knowledge Date: December 2023” and a today-date line. Generation settings are `do_sample` true, `temperature` 0.6, and `top_p` 0.9. Context length is 131,072. No evaluation is reported. No model license is stated.

Inventory methods are empty, the dataset id matches, and the parent matches.
