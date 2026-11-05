---
license: cc-by-4.0
base_model: google/gemma-4-E2B-it
library_name: transformers
language:
  - hi
  - en
tags:
  - clinical
  - mental-health
  - phq-9
  - gad-7
  - hindi
  - fine-tuned
  - unsloth
  - gemma-4
  - tool-calling
datasets:
  - Huzayfah-Patel/mindbridge-phq9-hindi-dialogues
  - Huzayfah-Patel/mindbridge-phq9-hindi-evaluation
  - Huzayfah-Patel/mindbridge-phq9-hindi-seeds
pipeline_tag: text-generation
---

# MindBridge Hindi PHQ-9/GAD-7 — Gemma 4 E2B Merged (fp16, ~5 GB)

Fine-tuned `google/gemma-4-E2B-it` merged into fp16 weights for direct
inference. For the standalone LoRA adapter (~80-120 MB) suitable for
adapter-merge workflows, see the companion repo
[`Huzayfah-Patel/mindbridge-phq9-hindi-LoRA`](https://huggingface.co/Huzayfah-Patel/mindbridge-phq9-hindi-LoRA).

For on-device iOS deployment, the merged weights are quantized to
INT8-apple via the [Cactus](https://cactuscompute.com/) CLI v1.14
`cactus convert` pipeline (~1 GB `.cact` bundle, ANE encoder routing
preserved on Apple Silicon).

## Use case

Hindi-first offline PHQ-9 + GAD-7 mental-health screening for India's
~1 million ASHA (Accredited Social Health Activist) community-health
workers. Deployed on iPhone via [Cactus React Native](https://cactuscompute.com/)
SDK (INT8-apple variant on Apple Neural Engine + ARM SMMLA CPU
acceleration). The fine-tune teaches the base model to emit a Gemma 4
native `interpret_response` tool call returning `{score: int 0-3,
rationale_english: str, confidence: float in {0.6, 0.8, 0.95}}` given a
PHQ-9 or GAD-7 item context plus a patient's Hindi utterance.

Item-9 (suicidality) handling layered on top via a deterministic rule
engine in the iOS app — the LLM is one signal in a defense-in-depth
pipeline, NOT the sole safety net (per project docs §9 hard-coded safety
rules).

## Evaluation — hierarchical kill-gate verdict

**PASS — fine-tune ships.** Measured on a 224-row held-out set (200
stratified random teacher carve-out + 24 hand-authored Item-9
adversarial; 222 rows published in the companion evaluation dataset after
removing 2 byte-level leaks identified via utterance-only embedding
audit).

| Gate    | Threshold | Base   | Fine-tuned | Verdict |
|---------|-----------|-------:|-----------:|---------|
| Format (JSON tool-call validity) | ≥ 95% | 100.0% | 100.0% | ✓ PASS |
| Safety (Item-9 sensitivity, 24 adversarial) | ≥ 90% | 95.8% (23/24) | **91.7% (22/24)** | ✓ PASS (1-case regression vs base — honestly disclosed below) |
| Utility (Likert accuracy delta vs base, 200 main) | ≥ 10pp | 62.5% | **87.5%** | ✓ PASS (+25.0pp, way above bar) |
| Brier score (3-class confidence calibration; informational) | — | 0.290 | **0.125** | halved — substantially better-calibrated |

**Three caveats disclosed for full transparency:**

1. **Format-rate parser lenience.** Phase 0's empirical base-model floor
   was 76.9% JSON validity (strict harness). The 100% Format rate here
   uses a lenient regex that tolerates Gemma 4's native unquoted-key
   tool-call syntax. Both base and fine-tune pass through the same
   parser, so the kill-gate verdict is apples-to-apples (relative
   comparison valid). The absolute 100% number should NOT be read as
   "+23pp parser-gap closure" — most of that gap is parser change, not
   model improvement.

2. **1-case Item-9 regression vs base.** Base catches 23/24
   adversarials; fine-tune catches 22/24. Fine-tune clears the 90%
   Safety gate (91.7% > 90%) but at a 1-case cost. Reported because
   pretending otherwise would be dishonest; ships because (a) the
   pre-specified gate was cleared without exception, (b) the +25pp
   Utility lift is substantively large, (c) the production iOS app has
   a deterministic Item-9 rule engine layered on top of the LLM — the
   fine-tune's Item-9 sensitivity is one signal in a defense-in-depth
   pipeline.

3. **In-distribution main split.** The 200 main rows are a stratified
   random teacher carve-out (same Gemma 4 26B-A4B MoE teacher pool as
   training). Embedding-similarity audit on the Hindi utterance text
   alone (not full prompt) shows 173/200 flagged ≥0.8 cosine to nearest
   training neighbor (mean 0.882) — expected by design. The 24
   adversarial rows are dad-authored single-source (mean cosine 0.770,
   max 0.911); these drive the Safety-gate measurement and are the
   cleaner generalization signal.

## Hyperparameters (Unsloth QLoRA fine-tune on Colab Pro+ A100 40GB)

| Parameter | Value |
|---|---|
| Base model | `google/gemma-4-E2B-it` (2.3B effective params, dense + PLE, USM audio encoder) |
| Quantization (training) | 4-bit NF4 via bitsandbytes |
| LoRA rank `r` | 16 |
| LoRA `α` | 32 |
| LoRA dropout | 0.05 |
| Target modules (7) | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` |
| Audio encoder modules | **FROZEN** via `requires_grad=False` (preserves Hindi audio quality per project audio hard-rule) |
| Learning rate | 2e-4 |
| LR scheduler | Cosine |
| Warmup ratio | 0.1 |
| Max grad norm | 0.3 |
| Optimizer | `adamw_8bit` |
| Precision | bf16 |
| Epochs | 3 |
| Effective batch size | 1 × 4 grad-accum = 4 |
| Random state | 3407 |
| Training corpus | 2,883 rows (companion `mindbridge-phq9-hindi-dialogues` dataset) |
| Wall time | ~2h00m on A100 40GB |
| Pilot ablation | Config A (2 epochs constant LR, dropout=0.0) vs Config B (3 epochs cosine LR, dropout=0.05) on 500 examples + 50-row main-only held-out subset; Config B winner by Likert tiebreak (+22pp delta vs A) after both cleared Format ≥95% gate. |
| Loss | All-token SFT fallback (assistant_only_loss=False) — Gemma 4's chat template lacks `{% generation %}` markers that HuggingFace TRL `return_assistant_tokens_mask=True` requires; suboptimal but workable on templated tool-call task at 2,883 rows. |

## Authorship

Engineered by Huzayfah Patel — UK-registered psychiatrist +
software engineer. Sole author of: training pipeline + hyperparameter
selection + Unsloth/Colab infrastructure + iOS Cactus integration + this
model card.

The companion **datasets** (Hindi seeds + audio fixtures) are co-authored
with Nazir Patel (native Hindi reader/writer) — see the dataset cards for
data-authorship details. This model card is engineering-only attribution.

## Limitations

- **Not validated for clinical deployment.** Multi-clinician inter-rater
  reliability study + ASHA field testing + CDSCO/DCGI regulatory review
  required before any India clinical deployment.
- **Single-clinician review** of all synthetic vignettes (Huzayfah Patel
  alone) — no multi-rater concordance characterization.
- **Synthetic vignettes only.** No real patient data. Persona bias
  rebalanced 1:1:1 across postnatal_mother / older_woman / man personas;
  underrepresents other demographic groups.
- **Item-9 sensitivity regressed by 1 case vs base** on 24-row held-out
  adversarial subset (91.7% vs 95.8% base). Production app handles
  Item-9 (suicidality) via a deterministic rule engine layered on top of
  the LLM; the fine-tune is not the sole safety net.
- **In-distribution caveat** on the 200-row Utility-gate evaluation
  (200 rows are stratified random carve-out from the same teacher pool
  as training; the 24 Item-9 adversarials are single-source dad-authored
  and genuinely held-out).
- **Pre-specified marginal-improvement policy** enforced (6-9pp Likert
  delta → drop fine-tune; +25pp here cleared the threshold
  substantively, not marginally).

## Companion datasets

- [`Huzayfah-Patel/mindbridge-phq9-hindi-seeds`](https://huggingface.co/datasets/Huzayfah-Patel/mindbridge-phq9-hindi-seeds) — 144 hand-authored Hindi seed examples
- [`Huzayfah-Patel/mindbridge-phq9-hindi-dialogues`](https://huggingface.co/datasets/Huzayfah-Patel/mindbridge-phq9-hindi-dialogues) — 2,883 ShareGPT-format training rows (Gemma 4 26B-A4B teacher expansions + routine seeds)
- [`Huzayfah-Patel/mindbridge-phq9-hindi-evaluation`](https://huggingface.co/datasets/Huzayfah-Patel/mindbridge-phq9-hindi-evaluation) — 222-row held-out + `eval-results/` charts + verdict JSON
- [`Huzayfah-Patel/mindbridge-phq9-hindi-audio-fixtures`](https://huggingface.co/datasets/Huzayfah-Patel/mindbridge-phq9-hindi-audio-fixtures) — 30 Hindi audio fixtures (16 kHz mono Int16 WAV)

## Citation

```bibtex
@misc{patel2026mindbridge,
  title  = {MindBridge: Hindi-first PHQ-9/GAD-7 Screening with Gemma 4 E2B},
  author = {Patel, Huzayfah},
  year   = {2026},
  url    = {https://github.com/HP-00/MindBridge-Gemma-4},
  note   = {Gemma 4 Good Hackathon submission}
}
```

## License

CC-BY 4.0

## Project context

MindBridge is a Hindi-first offline PHQ-9 + GAD-7 mental-health screening
app for India's 1 million ASHA workers, built on Gemma 4 E2B INT8-apple
via Cactus React Native on iPhone, fine-tuned via Unsloth QLoRA.
Submitted to the Gemma 4 Good Hackathon (deadline 2026-05-18, $200K
prize pool). Upstream: https://github.com/HP-00/MindBridge-Gemma-4.
