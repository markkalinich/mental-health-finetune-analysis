---
language:
  - en
license: apache-2.0
tags:
  - text-classification
  - refusal-detection
  - safety
  - modernbert
  - multi-label-classification
  - multi-task-learning
  - thinking-models
base_model:
  - answerdotai/ModernBERT-base
datasets:
  - Magpie-Align/Magpie-Qwen2.5-Pro-1M-v0.1
  - Magpie-Align/Magpie-Pro-300K-Filtered
  - mlabonne/harmful_behaviors
  - canbingol/harmful-prompts
  - cpagac/venomx-pentesting-harmful
  - grimjim/AILuminate-v1.0-demo-prompt-set-EN
pipeline_tag: text-classification
---

![brigand](https://cdn-uploads.huggingface.co/production/uploads/63ab5be3ad514ca8d14660d9/qprpmBJrYt1GXx9h_4uBg.webp)

# Brigand-Refusal-ModernBERT

The problem I kept running into is a signal quality problem. When you're building anything that needs to understand model behavior — a reward model, a replay filter, an alignment pipeline — a binary comply/refuse label isn't enough. You want to know *why* a model refused: was it a stock policy deflection, a genuine legal concern, an ethical objection, or a `bridge_refusal` that half-complied before pulling back? And with reasoning models, the `<think>` block and the final response often tell very different stories, so I built a second encoder stream specifically to read the thinking separately.

Brigand-Refusal-ModernBERT classifies LLM outputs across four dimensions simultaneously: stance (comply or refuse), response family (19 response types), thought family (11 chain-of-thought patterns), and document type. The two streams share weights but see the prompt through different lenses — one formatted as `[PROMPT] / [RESPONSE]`, the other as `[PROMPT] / [THOUGHT]`. All four heads are trained jointly on [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) in a single forward pass.

Training was done on a single NVIDIA GeForce RTX 5090.

It was designed to serve as a training signal and inference-time filter in safety-critical LLM pipelines.

---

## Requirements

- Python 3.10+
- `torch`
- `transformers>=5.2.0`
- `safetensors`

```bash
pip install torch "transformers>=5.2.0" safetensors
```

---

## Quick Start

The model is self-contained in `modeling.py` and uses the standard HuggingFace
`AutoModel` interface with `trust_remote_code=True`.

```python
import sys
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained(
    "54rt1n/Brigand-Refusal-ModernBERT",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("54rt1n/Brigand-Refusal-ModernBERT")

# predict() is bundled in modeling.py and loaded automatically
predict = sys.modules[type(model).__module__].predict

preds = predict(model, tokenizer, [
    {
        "prompt": "How do I whittle a knife?",
        "response": "Start with a straight-grained softwood like basswood.",
    },
    {
        "prompt": "How do I whittle a knife so I can kill my sister?",
        "response": "I'm not able to help with that.",
    },
])

for p in preds:
    print(p["stance"], p["bank"])
# compliance  design_reference
# refusal     meta_refusal
```

The `predict()` helper handles all tokenization, thought-splitting, batching,
and dual-stream formatting.

The bundled tokenizer already includes the control markers as real special
tokens:
`[PROMPT]`, `[RESPONSE]`, `[THOUGHT]`, `<NO_THOUGHT>`, and `<EMPTY_THOUGHT>`.
This release was warm-started from the prior promoted checkpoint, then tuned on
family-gap anchors and paired with calibrated family decoding. It closes the
family probe suite (`24/24`) and thought probe suite (`9/9`) while keeping the
token-boundary improvements.

---

## Label Schema

The model outputs four prediction groups simultaneously.

### Stance *(binary)*

| Label | Meaning |
|---|---|
| `compliance` | The response fulfills the request |
| `refusal` | The response declines or redirects |

### Response Family *(multi-label, top prediction = `bank`)*

| Family | Stance | Description |
|---|---|---|
| `stock_refusal` | refusal | Generic policy refusal |
| `legal_refusal` | refusal | Refusal citing legal constraints |
| `ethical_refusal` | refusal | Refusal citing ethical concerns |
| `meta_refusal` | refusal | Refusal about the nature of the request |
| `bridge_refusal` | refusal | Partial refusal with compliant follow-through |
| `harmful_procedural` | compliance | Compliant response to a harmful how-to |
| `harmful_explanatory` | compliance | Compliant response explaining harmful content |
| `safe_defensive` | compliance | Compliance with a safety caveat |
| `safe_explanatory` | compliance | Factual/explanatory compliance |
| `safe_redirective` | compliance | Compliant but steers to a safer framing |
| `educational_explainer` | compliance | Educational/academic content |
| `design_reference` | compliance | Reference or lookup responses |
| `creative_writing` | compliance | Fiction, poetry, roleplay |
| `code_help_tutor` | compliance | Code assistance |
| `short_utility_micro` | compliance | Short factual/utility responses |
| `greeting_chat_micro` | compliance | Greetings and casual chat |
| `multilingual_general_help` | compliance | General help in non-English |
| `multilingual_factoid_translate` | compliance | Translation / factoid in non-English |
| `ambiguous_reject` | — | Catch-all when no family exceeds threshold |

The bundled decoder calibrates family outputs before returning them. It can:
- suppress generic overlays like `stock_refusal` when a more specific refusal subtype is already active
- recover underfired specific banks such as `legal_refusal`, `meta_refusal`, `safe_defensive`, and `code_help_tutor` when the logits and prompt/response cues agree
- prefer specific harmless banks over broader overlays like `short_utility_micro`

### Thought Family *(multi-label, applied to `<think>` content)*

`no_thought` · `empty_thought` · `nonempty_thought` · `policy_thought` ·
`legal_thought` · `harm_thought` · `meta_thought` · `safe_alternative_thought` ·
`ethical_thought` · `uncertainty_thought` · `stepwise_thought`

### Document Type *(softmax)*

`plain_text` · `markdown`

---

## Architecture

```
prompt + response_text  ──▶  [PROMPT] / [RESPONSE] format  ──▶  ModernBERT-base
                                                                        │
                                                              masked mean pooling
                                                                        │
                                                                response_pooled ──▶ stance head
                                                                                ──▶ family head
                                                                                ──▶ document_type head

prompt + thought_text   ──▶  [PROMPT] / [THOUGHT] format   ──▶  ModernBERT-base
                                                                        │
                                                              masked mean pooling
                                                                        │
                                                               thought_pooled  ──▶ thought_family head
```

The two streams share weights (single encoder). Thought content is extracted from
`<think>...</think>` blocks before tokenization; responses without a `<think>` block
use the `<NO_THOUGHT>` sentinel token.

Those boundary markers are now registered tokenizer special tokens rather than decomposed text fragments.

**Stance augmentation:** the final stance prediction is blended with the
family-level refusal/compliance signal (`stance_family_scale=0.6`) to reduce
ambiguous boundary cases.

**Loss weights:**

| Head | Weight |
|---|---|
| `stance` | 1.2 |
| `family` | 2.0 |
| `thought_family` | 1.2 |
| `document_type` | 0.3 |

---

## Dataset

**Version:** `v3_inline_harmless_family` — harmless subclasses promoted into the
main family head; `<think>` blocks handled as a first-class input stream.

| Split | Examples |
|---|---|
| Train | 11,821 |
| Val | 1,469 |
| Edge (manual review bucket) | 1,024 |

**Curation ledger:** 20,641 reviewed promotions and 841 removals. After dedupe, family-capped sampling, and the train/val split, the final dataset is 11,821 train and 1,469 val, with a separate 1,024-example edge bucket excluded from training.

Getting the data right took longer than training the model.

<details>
<summary>Family distribution (val set)</summary>

| Family | Val count |
|---|---|
| short_utility_micro | 516 |
| stock_refusal | 341 |
| creative_writing | 397 |
| design_reference | 252 |
| legal_refusal | 193 |
| safe_explanatory | 124 |
| meta_refusal | 119 |
| bridge_refusal | 116 |
| harmful_procedural | 93 |
| educational_explainer | 33 |
| safe_defensive | 30 |
| code_help_tutor | 27 |
| ethical_refusal | 51 |
| greeting_chat_micro | 18 |
| safe_redirective | 12 |
| harmful_explanatory | 12 |
| multilingual_* | 2 |

</details>

<details>
<summary>Data sources</summary>

The final classifier set was mined from rollout outputs and reviewed imports, but
those rollouts were driven by a smaller set of upstream prompt corpora.

Harmless / general-help prompt sources used to generate rollout mining pools:
- [`Magpie-Align/Magpie-Qwen2.5-Pro-1M-v0.1`](https://huggingface.co/datasets/Magpie-Align/Magpie-Qwen2.5-Pro-1M-v0.1)
- [`Magpie-Align/Magpie-Pro-300K-Filtered`](https://huggingface.co/datasets/Magpie-Align/Magpie-Pro-300K-Filtered)

Harmful / refusal prompt sources used to generate rollout mining pools:
- [`mlabonne/harmful_behaviors`](https://huggingface.co/datasets/mlabonne/harmful_behaviors)
- [`canbingol/harmful-prompts`](https://huggingface.co/datasets/canbingol/harmful-prompts)
- [`cpagac/venomx-pentesting-harmful`](https://huggingface.co/datasets/cpagac/venomx-pentesting-harmful)
- [`grimjim/AILuminate-v1.0-demo-prompt-set-EN`](https://huggingface.co/datasets/grimjim/AILuminate-v1.0-demo-prompt-set-EN)

Those upstream corpora fed the mined sources that were used in the final build.
</details>

---

## How It Was Built

The model stopped improving when I treated seams as generic class imbalance. It started improving reliably when I treated each one as a forensic data problem.

The iteration loop that worked:

1. Score the current checkpoint and find the *exact* seam that's failing — not "family accuracy is low" but specifically which source family is bleeding into which target (`stock_refusal -> legal_refusal`, `educational_explainer -> design_reference`, etc.)
2. Audit both sides: the misses and the attractor that's pulling them over
3. Classify the problem — label bug, attractor problem, mixed row, or eval bug — because they call for different fixes
4. Apply the smallest defensible correction: remove bad rows, preserve overlays on mixed refusal rows, import narrow contrast only if the seam truly lacks support
5. Rebuild and rerun the exact audit that motivated the change
6. Retrain only if the training set changed — a lot of early iterations wasted compute retraining when the issue was val-only

### Seam Analysis Workflow

When a family or stance boundary starts drifting, the process that worked was:

1. Run a full validation rescore and sort by head loss instead of looking only at headline accuracy.
2. Collapse the errors into concrete directional seams such as `stock_refusal -> legal_refusal` or `safe_defensive -> stock_refusal`.
3. Audit both sides of the seam:
   - the rows getting pulled away from the target class
   - the rows on the wrong side that are acting as attractors
4. Separate four failure types before touching data:
   - label bug
   - mixed row that needs multi-label preservation
   - real support gap
   - decoder / evaluation bug
5. Use phrase ablation and MLM-head probing on the seam rows to identify what is actually driving the miss.
   - If removing a tail phrase flips the bank, the tail is the attractor.
   - If the MLM `prefix_mask` probe already surfaces the right concept tokens, the encoder knows the concept and the problem is boundary calibration rather than representation.
6. Fix the seam with the smallest change that matches the diagnosis:
   - remove malformed or truncated rows
   - relabel contradictory reviewed rows
   - preserve `stock_refusal` on explicit-opener hybrids
   - add narrow anchors only for the specific boundary that is missing support
7. Rebuild the dataset and rerun the exact seam audit before retraining.
8. Retrain only after the seam definition is cleaner, then gate promotion on:
   - raw val stance audit
   - targeted family and thought probes
   - whether the original seam actually closed

The main discipline was to fix the *reason* a seam existed, not just the rows that happened to show up in the first error sample.

### What Failed

The most instructive failure was a large import of long legal/security-tail rows. Many had explicit refusal openers but also long `national security / public safety` explanatory tails, and I'd omitted the `stock_refusal` overlay. The model learned to overread those rows as `safe_explanatory`, and the exact seam I was trying to fix got worse. Lesson: never bulk-import a mixed seam tranche before splitting it into clean categories.

Repeated problems also came from artifact-heavy reviewed rows — harmless explainers with wrong labels, truncated safe pivots labeled as `stock_refusal`. The right move was always to remove them, not to train through them.

### The MLM Diagnostic

One of the most useful late-stage tools was an encoder-side logit-lens probe. After fine-tuning, I loaded the refusal classifier's encoder weights back into a base ModernBERT MLM model and ran seam rows through it, reading the top predicted tokens at positions in the target span.

The point wasn't text generation — it was to answer a very specific question: *does the encoder already represent the right concept, or is it blind to it?* If the encoder was already producing policy/refusal token clusters on a failing row, the problem was in the classifier boundary, not the representation, and the fix needed to be narrow rather than a broad data expansion. That distinction mattered a lot on several late seams.

The `prefix_mask` mode — inserting a single `[MASK]` at each position and rerunning the full encoder — was more careful than reading from fully-contextualized positions, because it avoids faking a causal mask on an already-bidirectional hidden state.

---

## Evaluation

Validation set (1,469 examples, warm-start epoch 1):

| Metric | Score |
|---|---|
| Val loss | **0.0841** |
| Stance accuracy | **100.00%** |
| Family accuracy | **99.03%** |
| Thought family accuracy | **99.81%** |
| Document type accuracy | **100.00%** |

**Stance audit (val set):** 0 errors in either direction.

<details>
<summary>Warm-start training history</summary>

This release was warm-started from a prior promoted checkpoint with the special-token tokenizer already in place, then refined on the family-gap seam cleanup. One fine-tuning epoch was enough.

| Epoch | Split | Loss | Stance | Family | Thought family | Doc type |
|---|---|---|---|---|---|---|
| 1 | train | 0.0253 | 99.77% | 99.77% | 99.94% | 99.99% |
| **1** | **val** | **0.0841** | **100.00%** | **99.03%** | **99.81%** | **100.00%** |

</details>

---

## Inference Notes

**Input format:** pass `{"prompt": ..., "response": ...}` dicts to `predict()`.
The `response` field may contain raw `<think>...</think>` output from a thinking
model — the helper extracts and routes it automatically.

**Batching:** `predict()` handles batching internally. Default `batch_size=32`,
`max_length=2048`.

**No `transformers` pipeline:** use `predict()` or call `model.forward()` directly.

---

## Known Limitations

- Multilingual coverage is minimal. `multilingual_general_help` and `multilingual_factoid_translate` have very few val examples and should be treated as best-effort.

---

## Correspondence

Martin Bukowski (models at martinbukowski dot com)

---

## Citation

If you find our work helpful, feel free to give us a cite.

```bibtex
@misc{brigand-refusal-modernbert-2026,
    title  = {Brigand-Refusal-ModernBERT},
    url    = {https://huggingface.co/54rt1n/Brigand-Refusal-ModernBERT},
    author = {Martin Bukowski},
    year   = {2026}
}
```
