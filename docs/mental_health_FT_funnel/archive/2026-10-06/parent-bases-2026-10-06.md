<!-- doc-verbosity: public-ready -->

# Parents' pre-trained bases, reviewed 6 October 2026

Archived 9 October 2026 from `how-models-are-filtered.md`. This is the 6 October review of a 64-row `kept.csv` (37 parents), the pass before manual review was applied. It is not a description of the current study set. The current funnel is `revision_3_experiments/hf_inventory/results/mental-health/<CURRENT>/` (see `../../how-models-are-filtered.md`).

This table is that day's review of a 64-row kept file (37 parents). On 6 October the list after manual review was 38 models (`results/mental-health/archive/2026-10-06/kept.csv`); the 64 rows here are that day's pre-review file. The per-parent facts below (which card names a pre-trained base, which base repo is gated or returns 404) are not stored in another file.


`kept.csv` has 64 models and **37 distinct parents**.

**28 of 37 parents name a pre-trained base** on their own card (YAML `base_model`, a `base_model:` tag, or a sentence or model-index link that names the pre-trained repo). **27 of those 28** resolve to a repo this token can read that has full-precision weights at the root (`model.safetensors`, `model-*-of-*.safetensors`, or `pytorch_model.bin` / `pytorch_model-*-of-*.bin`), with safetensors dtypes only in {F16, BF16, F32}. That is **27/28**.

The miss is `mistralai/Mistral-7B-v0.2`, named in a sentence on `mistralai/Mistral-7B-Instruct-v0.2`. `model_info` returns 404. A Hub search did not find an official repo with that id.

Two parents name the same pre-trained repo: `meta-llama/Llama-2-7b-chat-hf` and `NousResearch/Llama-2-7b-chat-hf` both point at `meta-llama/Llama-2-7b-hf` (the Nous card writes `llamaste/Llama-2-7b-hf`, and the Hub resolves that id to `meta-llama/Llama-2-7b-hf`). So the 28 names are **27 distinct repos, and 26 of those 27 repos** are readable with root full-precision weights.

Of the 27 readable cases, **8 repos are gated** (`gated: manual`). This token still received the file list and the safetensors metadata. They are marked `gated` below and counted in the 27. The other 19 are public.

"Full precision" here means the Hub safetensors metadata lists only F16, BF16, and/or F32. `meta-llama/Llama-2-7b-hf` reports F16 and F32 together.

### Third-party rehosts

These four parents are copies of someone else's release, not the vendor's own repo:

| Parent | Kept children | What the card names |
|---|---:|---|
| `unsloth/Qwen3-32B` | 1 | `Qwen/Qwen3-32B` (the post-trained Qwen repo, not a pre-trained base) |
| `unsloth/gemma-3-270m-it` | 1 | `google/gemma-3-270m-it` |
| `unsloth/gemma-3-4b-it` | 1 | `google/gemma-3-4b-it` |
| `NousResearch/Llama-2-7b-chat-hf` | 2 | Meta's Llama 2 card, with the model index rewritten to `llamaste/...`, which redirects to `meta-llama/Llama-2-7b` and `meta-llama/Llama-2-7b-hf` |

`NousResearch/Hermes-2-Pro-Mistral-7B`, `sapienzanlp/Minerva-7B-instruct-v1.0`, `Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct`, and `ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1` are other organizations' own models. They are not rehosts of a vendor checkpoint.

### Parent table

`Readable` is `yes` (public), `gated` (gated, and this token read the file list), or `no` (404). `Root FP weights` uses the safetensors metadata.

| Parent | Kept children | Names pre-trained base | Base repo | Evidence | Readable | Root FP weights |
|---|---:|---|---|---|---|---|
| `Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct` | 1 | yes | `Doctor-Shotgun/TinyLlama-1.1B-32k` | "This is an instruct-tuned TinyLlama-1.1B-32k". That repo's card says it is a "32k context finetune" made by "further pretraining", not an instruction model. | yes | yes (BF16, `model.safetensors`) |
| `HuggingFaceTB/SmolLM2-360M-Instruct` | 1 | yes | `HuggingFaceTB/SmolLM2-360M` | YAML `base_model: HuggingFaceTB/SmolLM2-360M`. Tag `base_model:HuggingFaceTB/SmolLM2-360M`. | yes | yes (BF16, `model.safetensors`) |
| `LiquidAI/LFM2-700M` | 1 | no | | "We're releasing the weights of four post-trained checkpoints..." No `base_model` field or tag, and no named pre-trained repo. `LiquidAI/LFM2-700M-Base` is 404; the card does not name it. | | |
| `NousResearch/Hermes-2-Pro-Mistral-7B` | 1 | yes | `mistralai/Mistral-7B-v0.1` | YAML `base_model: mistralai/Mistral-7B-v0.1`. | yes | yes (BF16 shards, `model-*-of-00002.safetensors`) |
| `NousResearch/Llama-2-7b-chat-hf` | 2 | yes | `meta-llama/Llama-2-7b-hf` | Model index links `llamaste/Llama-2-7b-hf`. That id resolves to `meta-llama/Llama-2-7b-hf`. The same row also links `llamaste/Llama-2-7b`, which resolves to `meta-llama/Llama-2-7b`. | gated | yes on `Llama-2-7b-hf` (F16 and F32, `model-*-of-00002.safetensors`). `Llama-2-7b` has `consolidated.00.pth` at the root, not `model.safetensors` or `pytorch_model.bin`. |
| `Qwen/Qwen2.5-0.5B-Instruct` | 1 | yes | `Qwen/Qwen2.5-0.5B` | YAML `base_model: Qwen/Qwen2.5-0.5B`. | yes | yes (BF16, `model.safetensors`) |
| `Qwen/Qwen2.5-1.5B-Instruct` | 1 | yes | `Qwen/Qwen2.5-1.5B` | YAML `base_model: Qwen/Qwen2.5-1.5B`. | yes | yes (BF16, `model.safetensors`) |
| `Qwen/Qwen2.5-3B-Instruct` | 1 | yes | `Qwen/Qwen2.5-3B` | YAML `base_model: Qwen/Qwen2.5-3B`. | yes | yes (BF16 shards) |
| `Qwen/Qwen2.5-7B-Instruct` | 6 | yes | `Qwen/Qwen2.5-7B` | YAML `base_model: Qwen/Qwen2.5-7B`. | yes | yes (BF16 shards) |
| `Qwen/Qwen3-0.6B` | 1 | yes | `Qwen/Qwen3-0.6B-Base` | YAML `base_model: Qwen/Qwen3-0.6B-Base`. | yes | yes (BF16, `model.safetensors`) |
| `Qwen/Qwen3-1.7B` | 1 | yes | `Qwen/Qwen3-1.7B-Base` | YAML `base_model: Qwen/Qwen3-1.7B-Base`. | yes | yes (BF16, `model.safetensors`) |
| `Qwen/Qwen3-4B` | 1 | yes | `Qwen/Qwen3-4B-Base` | YAML `base_model: Qwen/Qwen3-4B-Base`. | yes | yes (BF16 shards) |
| `Qwen/Qwen3-8B` | 2 | yes | `Qwen/Qwen3-8B-Base` | YAML `base_model: Qwen/Qwen3-8B-Base`. | yes | yes (BF16 shards) |
| `Qwen/Qwen3-14B` | 1 | yes | `Qwen/Qwen3-14B-Base` | YAML `base_model: Qwen/Qwen3-14B-Base`. | yes | yes (BF16 shards) |
| `Qwen/Qwen3-32B` | 2 | no | | No `base_model` field or tag. The README does not name `Qwen3-32B-Base`. `Qwen/Qwen3-32B-Base` is 404. | | |
| `TinyLlama/TinyLlama-1.1B-Chat-v1.0` | 2 | yes | `TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` | "This is the chat model finetuned on top of TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T." | yes | yes (F32, `model.safetensors`) |
| `google/gemma-2-2b-it` | 2 | yes | `google/gemma-2-2b` | YAML `base_model: google/gemma-2-2b`. | gated | yes (F32 shards) |
| `google/gemma-2b-it` | 1 | yes | `google/gemma-2b` | "You can also visit the model card of the 2B base model" with a link to `google/gemma-2b`. That repo's card says "This model card corresponds to the 2B base version of the Gemma model." No YAML `base_model`. | gated | yes (BF16 shards) |
| `google/gemma-3-1b-it` | 1 | yes | `google/gemma-3-1b-pt` | YAML `base_model: google/gemma-3-1b-pt`. | gated | yes (BF16, `model.safetensors`) |
| `google/gemma-3-4b-it` | 3 | yes | `google/gemma-3-4b-pt` | YAML `base_model: google/gemma-3-4b-pt`. | gated | yes (BF16 shards) |
| `google/gemma-3-27b-it` | 1 | yes | `google/gemma-3-27b-pt` | YAML `base_model: google/gemma-3-27b-pt`. | gated | yes (BF16 shards) |
| `google/gemma-4-12B-it` | 1 | yes | `google/gemma-4-12B` | YAML `base_model: google/gemma-4-12B`. The base repo's README is almost the same family card; the weight sha256 differs from `gemma-4-12B-it` (both files are about 23.9 GB, BF16). | yes | yes (BF16, `model.safetensors`, 23,919,549,408 bytes) |
| `google/gemma-4-31B-it` | 1 | yes | `google/gemma-4-31B` | YAML `base_model: google/gemma-4-31B`. Shard sha256 values differ from `gemma-4-31B-it`. | yes | yes (BF16 shards) |
| `google/gemma-4-E4B-it` | 1 | yes | `google/gemma-4-E4B` | YAML `base_model: google/gemma-4-E4B`. `model.safetensors` sha256 differs from `gemma-4-E4B-it`. | yes | yes (BF16, `model.safetensors`) |
| `meta-llama/Llama-2-7b-chat-hf` | 7 | yes | `meta-llama/Llama-2-7b-hf` | Model index row for 7B links `meta-llama/Llama-2-7b-hf` and `meta-llama/Llama-2-7b`. No YAML `base_model`. | gated | yes on `Llama-2-7b-hf` (F16 and F32 shards). `Llama-2-7b` root file is `consolidated.00.pth` only. |
| `meta-llama/Llama-3.1-8B-Instruct` | 2 | yes | `meta-llama/Llama-3.1-8B` | YAML `base_model: meta-llama/Meta-Llama-3.1-8B`. The tag is `base_model:meta-llama/Llama-3.1-8B`. Both ids return the same repo (`id` `meta-llama/Llama-3.1-8B`, same four shard sha256 values). | gated | yes (BF16 shards) |
| `meta-llama/Llama-3.2-3B-Instruct` | 7 | no | | No `base_model` field or tag. The heading "Base Pretrained Models" is a benchmark table and does not name `meta-llama/Llama-3.2-3B`. That repo exists (gated, token read it, BF16 shards). The card does not name it. | | |
| `meta-llama/Meta-Llama-3-8B-Instruct` | 2 | no | | No `base_model` field or tag. "Base pretrained models" is a benchmark table and does not name `meta-llama/Meta-Llama-3-8B`. That repo exists (gated, token read it, BF16 shards). The card does not name it. | | |
| `microsoft/Phi-3.5-mini-instruct` | 1 | no | | No `base_model` field or tag. The card says this is "an update over the June 2024 instruction-tuned Phi-3 Mini", which is itself instruction-tuned. `microsoft/Phi-3.5-mini` is 404. | | |
| `mistralai/Mistral-7B-Instruct-v0.2` | 1 | yes | `mistralai/Mistral-7B-v0.2` | "The Mistral-7B-Instruct-v0.2 Large Language Model (LLM) is an instruct fine-tuned version of the Mistral-7B-v0.2." No YAML `base_model`. | no | no (404) |
| `mistralai/Mistral-7B-Instruct-v0.3` | 2 | yes | `mistralai/Mistral-7B-v0.3` | YAML `base_model: mistralai/Mistral-7B-v0.3`, and the same sentence in the README. | yes | yes (BF16 shards) |
| `sapienzanlp/Minerva-7B-instruct-v1.0` | 1 | yes | `sapienzanlp/Minerva-7B-base-v1.0` | YAML `base_model: sapienzanlp/Minerva-7B-base-v1.0`. | yes | yes (F16 shards) |
| `tiiuae/Falcon3-1B-Instruct` | 1 | yes | `tiiuae/Falcon3-1B-Base` | YAML `base_model: tiiuae/Falcon3-1B-Base`. | yes | yes (BF16, `model.safetensors`) |
| `unsloth/Qwen3-32B` | 1 | no | | YAML `base_model: Qwen/Qwen3-32B`. That repo is the post-trained model and does not itself name a pre-trained base. | | |
| `unsloth/gemma-3-270m-it` | 1 | no | | YAML `base_model: google/gemma-3-270m-it`. `google/gemma-3-270m` exists (gated, BF16 `model.safetensors`) and `google/gemma-3-270m-pt` is 404. This card names the instruction repo. | | |
| `unsloth/gemma-3-4b-it` | 1 | no | | YAML `base_model: google/gemma-3-4b-it`, not `google/gemma-3-4b-pt`. | | |
| `ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1` | 1 | no | | YAML `base_model: ytu-ce-cosmos/Turkish-Llama-8b-Instruct-v0.1`, an instruction model. | | |

Kept-children counts sum to 64.
