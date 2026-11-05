---
license: mit
base_model: rroshann/sec-sentiment-sft-deepseek-14b
base_model_relation: finetune
pipeline_tag: text-generation
language:
  - en
tags:
  - finance
  - sec-filings
  - sentiment-analysis
  - grpo
  - rlhf
  - ordinal-classification
  - deepseek-r1
  - r1-distill
  - qlora
  - peft
  - vanderbilt-dsi
library_name: transformers
---

# sec-sentiment-sftgrpo-deepseek-14b

Reinforcement-learning-aligned checkpoint for 5-class sentiment classification of thematic factors extracted from U.S. industrials SEC filings (10-K, 10-Q). Built on top of [`rroshann/sec-sentiment-sft-deepseek-14b`](https://huggingface.co/rroshann/sec-sentiment-sft-deepseek-14b) by a second stage of Group Relative Policy Optimization (GRPO) against a composite ordinal-plus-anti-neutral reward with realized-return-quintile supervision.

Produced as part of the AllianceBernstein × Vanderbilt DSI capstone project, Spring 2026.

- **Paper / Technical Report:** [`TECHNICAL_REPORT.md`](https://github.com/WanlinTu/NLP-Project/blob/main/technical_report/TECHNICAL_REPORT.md)
- **Code:** [github.com/WanlinTu/NLP-Project](https://github.com/WanlinTu/NLP-Project)
- **SFT predecessor:** [`rroshann/sec-sentiment-sft-deepseek-14b`](https://huggingface.co/rroshann/sec-sentiment-sft-deepseek-14b)

This checkpoint corresponds to the `sft_grpo` variant in the technical report. A further `sft_grpo_bon` variant is obtained from this same checkpoint at inference time via Self-Consistency Best-of-N decoding (N=3 at T=0.8) — no separate weights are required; see §[Test-Time Compute](#test-time-compute-best-of-n--self-consistency).

* * *

## Model Details

| | |
|---|---|
| **Architecture** | DeepSeek-R1-Distill-Qwen-14B (dense decoder-only, 14B params) |
| **Alignment method** | GRPO (Shao et al. 2024) with composite ordinal reward, applied as a LoRA delta on the merged SFT checkpoint; final checkpoint is fully merged |
| **GRPO LoRA rank / alpha** | 16 / 32 |
| **Trainable parameter fraction** | ~0.3% of base (GRPO stage only) |
| **Training hardware** | 1× A100 80GB (Vanderbilt ACCRE) |
| **Precision** | bf16 |
| **Checkpoint format** | Merged safetensors (6 shards, 28 GB total) |
| **Random seed** | 42 (single-seed — see Limitations) |

## Intended Uses

**In scope.** Financial-materiality sentiment classification of individual factor summaries extracted from 10-K / 10-Q filings, in settings where the **cohort-level ordinal ordering** of predictions matters more than per-sample accuracy. Input = a factor-level summary paragraph. Output = one of five ordinal labels (`very_negative`, `negative`, `neutral`, `positive`, `very_positive`) plus a natural-language rationale and a confidence score.

**Out of scope.** This is **not** a general-purpose assistant. Do not use it for:

- Open-ended chat or instruction-following
- Single-factor return prediction (per-sample accuracy is near the 5-class uniform baseline — by design)
- Sentiment analysis outside the U.S. industrials sector or outside SEC-filing prose
- Downstream deployment without the cohort aggregation + validity gate described in the technical report (§9, §10)

The model assumes the caller operates an aggregation layer that combines factor-level labels into a filing-level signal before portfolio construction. Standalone per-prompt predictions are not the intended use.

## Training Procedure

### Stage 1 — Supervised fine-tune (inherited from SFT predecessor)

See [`rroshann/sec-sentiment-sft-deepseek-14b`](https://huggingface.co/rroshann/sec-sentiment-sft-deepseek-14b) for training data, QLoRA configuration, and SFT results. The SFT checkpoint is the frozen reference policy for the KL-regularization term in Stage 2.

### Stage 2 — GRPO alignment

Group Relative Policy Optimization against a composite reward:

$$
R \;=\; r_{\text{format}} \cdot \bigl[\, r_{\text{ordinal}}(y, \ell^{*}) \;+\; \lambda \cdot r_{\text{anti-neutral}}(y) \,\bigr]
$$

| Reward term | Type | Notes |
|---|---|---|
| `r_format` | {0, 1} hard gate | 1 iff output is valid JSON with a recognized 5-class label |
| `r_ordinal` | [0, 1] dense | `1.0 − 0.25 · |s(ŷ) − s(ℓ*)|` where `s(·)` maps labels to an ordinal scale 0..4 |
| `r_anti_neutral` | {0, 1} bonus | 1 iff both the predicted label and gold label are non-neutral |
| `λ` | scalar | 0.3 |

The format gate is **multiplicative** — a malformed emission zeros the entire reward, preventing the policy from drifting toward schema-violating outputs. The anti-neutral bonus counteracts the `neutral` attractor that the SFT policy inherits from the label distribution.

Gold labels `ℓ*` are **realized-return quintiles** (cross-sectional within filing-month) of each filing's 21-day forward excess return vs SPY. See technical report §8.2 for the full derivation.

| GRPO hyperparameter | Value |
|---|---|
| Group size `G` | 8 completions per prompt |
| Learning rate | 5e-6 cosine, 3% warmup |
| KL coefficient `β` | 0.04 (anchor to SFT reference policy) |
| Epochs | 2 |
| Effective batch size | 4 (1 per-device × 4 grad accumulation) |
| Sampling temperature (training) | 1.0 |
| Adapter | LoRA rank 16 stacked on top of the r=64 SFT adapter (delta training; SFT adapter frozen; reference policy recovered via `model.disable_adapter()`) |
| Precision | bf16 |
| Seed | 42 |

### Pre-registered evaluation protocol

All test-set results were declared before inference, in a timestamp-locked `preregistration.json` committed to the repository. The split is time-ordered:

| Split | Filings | Period |
|---|---|---|
| Train | 1,452 | 2015 – 2020 |
| Validation | 384 | 2021 – 2022 |
| **Test (held-out)** | **605** | **2023 – mid-2025** |

Test-set size = **18,466 factor-level rows** across the 605 filings. No test-set inference was run prior to the preregistration timestamp.

## Evaluation

### Classification metrics on the pre-registered test set

Gold label = filing's realized-return quintile at the 21-day horizon (not an LLM-generated label — ground-truth market data).

| Metric | Base (R1-Distill) | SFT | **SFT + GRPO (this model)** |
|---|---|---|---|
| Macro F1 | 0.160 | 0.174 | **0.173** |
| Quadratic Weighted Kappa (QWK) | 0.017 | 0.027 | **~0.027** |

**Honest disclosure.** GRPO is statistically tied with SFT on per-sample F1. The per-sample classification gain over SFT is not the claim. The value of GRPO alignment is visible at the **portfolio level** — the long-short cohort spread at H=21d lifts from `sft = 4.88%` to `sft_grpo = 8.12%` (greedy decoding). See technical report §8.7 for the GRPO-vs-SFT discussion and §11.3 for the portfolio-level numbers.

### Portfolio-level metrics (technical report §11)

| Strategy × horizon | `base` | `sft` | `sft_grpo` | `sft_grpo_bon` |
|---|---|---|---|---|
| L/S cohort spread, H=21d | 2.78% | 4.88% | 8.12% | 8.09% |
| L/S Information Ratio, H=63d | 1.40 | 1.58 | 2.23 | 2.93 |
| Robust HAC-valid IR (sector-neutral × H=21d × n=318) | — | — | — | **2.02** |

Every IR number for the GRPO and BoN variants is a **single-seed point estimate**. See Limitations.

## Test-Time Compute (Best-of-N + Self-Consistency)

The `sft_grpo_bon` variant is **not a separate model** — it uses these exact weights with a test-time decoding overlay:

1. Sample `N = 3` completions at temperature `T = 0.8`.
2. For each completion, parse `(label, confidence)` from the JSON emission.
3. Score each of the 5 possible labels:
$$
\text{score}(k) \;=\; \sum_{i=1}^{N} \mathbf{1}[\text{label}_i = k] \cdot \text{conf}_i \;+\; \lambda \cdot \text{conf}_k, \quad \lambda = 0.5
$$
where the second term is a within-label tiebreaker that selects the highest-confidence sample when multiple samples agree on the winning label.
4. Emit the `argmax` label and return the completion from the highest-confidence sample in the winning-label set.

This is Wang et al. (2022) Self-Consistency voting with a confidence-weighted scoring rule. Zero learned parameters. The approach replaced an earlier CORN (Conditional Ordinal Regression for Neural Networks) verifier that collapsed during training (predicted μ ≈ 1.9 for 100% of validation samples); see technical report §9 for the failure narrative.

**Why BoN helps at long horizons.** At H=63d and H=126d, BoN adds +9.19 pp and +14.20 pp to the L/S cohort spread respectively (paired panel, same 605 filings scored by both the greedy and BoN decoder). At H=21d the lift is noise (−0.03 pp). See §11.4.

## Usage

### Direct inference via vLLM (recommended)

```bash
vllm serve rroshann/sec-sentiment-sftgrpo-deepseek-14b \
  --dtype bfloat16 \
  --gpu-memory-utilization 0.90 \
  --port 8000 \
  --max-model-len 2048
```

### Greedy decoding (= `sft_grpo` variant)

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="local")

response = client.chat.completions.create(
    model="rroshann/sec-sentiment-sftgrpo-deepseek-14b",
    messages=[{
        "role": "user",
        "content": "Factor: Supply chain pressure from component shortages...\n\nClassify sentiment into one of [very_negative, negative, neutral, positive, very_positive] and return JSON: {label, rationale, confidence}."
    }],
    temperature=0.0,
    max_tokens=512,
)
print(response.choices[0].message.content)
```

### Best-of-N with Self-Consistency (= `sft_grpo_bon` variant)

```python
from collections import defaultdict
import json

def best_of_n(client, model, messages, n=3, temperature=0.8, lam=0.5):
    """Self-Consistency BoN per Wang et al. 2022, as shipped in report §9.2.

    score(k) = sum_i 1[y_i = y_k] * conf_i  +  lam * conf_k
    Argmax over labels; emit the winning-sample completion (highest conf
    within the winning label).

    NOTE: under vLLM, calling the API once with `n=3` returns identical
    samples because of per-request seeding. Issue N distinct requests
    with distinct `seed` values instead (as below).
    """
    samples = []
    for seed_offset in range(n):
        r = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            top_p=0.95,
            max_tokens=512,
            seed=42 + seed_offset,
        )
        raw = r.choices[0].message.content
        try:
            parsed = json.loads(raw)
            samples.append((parsed["label"], float(parsed.get("confidence", 0.5)), raw))
        except (json.JSONDecodeError, KeyError):
            continue

    if not samples:
        return {"label": "neutral", "confidence": 0.0, "raw": None}

    # score(k) = sum_i 1[y_i = y_k] * conf_i  +  lam * conf_k
    scores = {}
    for label_k, conf_k, _ in samples:
        agreement = sum(c_i for (l_i, c_i, _) in samples if l_i == label_k)
        scores[label_k] = agreement + lam * conf_k

    top_label = max(scores, key=scores.get)
    # Emit the highest-confidence sample whose label == top_label
    winning_sample = max(
        (s for s in samples if s[0] == top_label),
        key=lambda s: s[1],
    )
    return {"label": top_label, "confidence": winning_sample[1], "raw": winning_sample[2]}
```

### Direct inference via `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "rroshann/sec-sentiment-sftgrpo-deepseek-14b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [{"role": "user", "content": "<your factor summary + instructions>"}]
input_ids = tokenizer.apply_chat_template(
    messages,
    return_tensors="pt",
    add_generation_prompt=True,
).to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=512,
    do_sample=False,  # greedy
)
print(tokenizer.decode(outputs[0, input_ids.shape[-1]:], skip_special_tokens=True))
```

## Limitations & Biases

- **Single-seed GRPO training.** No variance estimate across retraining runs. The portfolio-level gains over SFT (monotone cohort ladder, IR lift) are large enough to be defensible as point estimates, but formal significance testing would require a multi-seed rerun (not executed — see technical report §16.1).
- **Per-sample F1 gain vs SFT is within noise.** GRPO's ~0 F1 improvement is consistent with seed variance alone; only the portfolio-aggregated signal is a robust lift (report §8.8).
- **BoN evaluated OOS-only.** The `sft_grpo_bon` variant was sampled on the 605-filing test panel only (compute budget). There is no in-sample BoN counterpart for a direct IS-vs-OOS comparison (report §12.4).
- **Sparse tail cohorts in the BoN variant.** At H=21, the BoN variant's very_negative cohort contains n=2 filings and very_positive contains n=9. Headline IRs for the BoN variant rest on ~11 filings per tail cohort; a block-bootstrap confidence interval is not computed (report §11.4, §13.1).
- **No reward-term ablation.** The four reward hyperparameters (`λ = 0.3`, ordinal slope `0.25`, `G = 8`, `β = 0.04`) are author-chosen, not swept. A sensitivity sweep is future work.
- **Factor-level (not filing-level) train/val split** inherited from the SFT predecessor. Test set is time-ordered and filing-level, so the OOS protocol is unaffected.
- **Universe / domain specificity.** Trained on 80 U.S. industrials tickers; will underperform on other sectors.
- **8-K filings excluded.** Event-driven filings break the 60-question factor taxonomy.
- **HIGH_BETA disclosure.** Dollar-neutral portfolios built on this model's predictions have |β| ≈ 2.0 against SPY in backtests — not beta-neutral. Mitigation is a rolling-63d β-hedged SPY short overlay; see technical report §13.2.
- **Transports sector wrong-sign.** The `transports (airlines)` sub-sector carries a negative L/S spread across all variants (report §11.7). Deployment rule: exclude transports or invert the sign at the sector level.

## Ethical Considerations

- Training labels for the SFT predecessor were generated via the Anthropic API (Claude Opus). We believe this use falls within the non-competing-products provision of Anthropic's Commercial Terms because the released model is a 5-class sentiment classifier specialized for SEC filings, not a general-purpose assistant. Deployers should independently verify current Anthropic terms apply to their use.
- Predictions are for **research and reproducibility** of the capstone results. Not investment advice. Not audited for deployment in any regulated context.
- SEC filings are U.S. public-domain government documents (EDGAR). No PII.

## Citation

```bibtex
@techreport{siddartha2026reasoningaugmented,
  title   = {Reasoning-Augmented Factor Extraction:
             Enhancing SEC Sentiment Signals through Reinforcement Learning},
  author  = {Siddartha, Roshan and Tu, Maggie and Butskhrikidze, Luka},
  year    = {2026},
  month   = {April},
  institution = {Vanderbilt University Data Science Institute},
  note    = {AllianceBernstein × Vanderbilt DSI Capstone. Course:
             NLP for Asset Management. Instructor: Che Guan.}
}
```

## License & Acknowledgements

- **Model license:** MIT (matches upstream DeepSeek-R1-Distill-Qwen-14B and the SFT predecessor).
- Upstream base model: DeepSeek-AI. See [`deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B).
- Training labels (SFT stage) generated via the Anthropic API (Claude Opus family).
- GRPO implementation uses Hugging Face `trl`'s `GRPOTrainer`.
- Compute provided by Vanderbilt University ACCRE (DGX A100).
- Project advised by Che Guan, Vanderbilt Data Science Institute.
