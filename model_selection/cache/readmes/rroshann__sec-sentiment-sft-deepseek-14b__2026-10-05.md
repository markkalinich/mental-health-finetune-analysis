---
license: mit
base_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
pipeline_tag: text-generation
language:
  - en
tags:
  - finance
  - sec-filings
  - sentiment-analysis
  - qlora
  - sft
  - deepseek
  - vanderbilt-dsi
library_name: transformers
---

# sec-sentiment-sft-deepseek-14b

Supervised fine-tune of [`deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) for 5-class sentiment classification of thematic factors extracted from U.S. industrials SEC filings (10-K, 10-Q).

Produced as part of the AllianceBernstein × Vanderbilt DSI capstone project, Spring 2026.

- **Paper / Technical Report:** [`TECHNICAL_REPORT.md`](https://github.com/WanlinTu/NLP-Project/blob/main/technical_report/TECHNICAL_REPORT.md)
- **Code:** [github.com/WanlinTu/NLP-Project](https://github.com/WanlinTu/NLP-Project)
- **Companion model (further RL-aligned):** [`rroshann/sec-sentiment-sftgrpo-deepseek-14b`](https://huggingface.co/rroshann/sec-sentiment-sftgrpo-deepseek-14b)

* * *

## Model Details

| | |
|---|---|
| **Architecture** | DeepSeek-R1-Distill-Qwen-14B (dense decoder-only, 14B params) |
| **Fine-tune method** | QLoRA (NF4 4-bit base + LoRA adapter), merged to a single fp16/bf16 checkpoint |
| **LoRA rank / alpha / dropout** | 64 / 128 / 0.05 |
| **Target modules (7)** | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` |
| **Trainable parameter fraction** | ~1.3% of base |
| **Training hardware** | 1× A100 40GB (Vanderbilt ACCRE) |
| **Precision** | bf16 mixed |
| **Checkpoint format** | Merged safetensors (6 shards, 28 GB total) |

## Intended Uses

**In scope.** Financial-materiality sentiment classification of individual factor summaries extracted from 10-K / 10-Q filings. Input = a factor-level summary paragraph. Output = one of five ordinal labels (`very_negative`, `negative`, `neutral`, `positive`, `very_positive`) plus a natural-language rationale and a confidence score.

**Out of scope.** This is **not** a general-purpose assistant. Do not use it for:

- Open-ended chat or instruction-following
- Stock-price prediction, trading signals on a single-factor basis
- Sentiment analysis outside the U.S. industrials sector or outside SEC-filing prose
- Downstream applications without the cohort-level aggregation and portfolio-level validation described in the technical report

Per-sample accuracy is near the 5-class uniform baseline (~20%) on realized-return-quintile gold labels — by design. The model's value comes from the **cohort-level ordinal shape** of predictions across a pre-registered backtest panel (see technical report §11).

## Training Data

- **Source corpus:** 67,741 thematic factors extracted from 2,441 10-K and 10-Q filings (80 U.S. industrials tickers, 2015-01 → 2025-06).
- **Annotation pipeline:** two-stage weak-to-strong labeling:
  1. Base DeepSeek-R1-Distill-Qwen-14B produces a first-pass 5-class label per factor.
  2. Claude Opus re-labels each factor against a financial-materiality rubric. 45.6% of base labels change (disagreement rate between two LLMs — not a human-validated correction rate).
- **Tail densification:** +217 samples from two "extreme" chunks targeting known very-negative and very-positive filings (bankruptcy, major contract wins, restructuring).
- **Final dataset size:** 5,217 samples.
- **Splits:** 4,172 train / 1,045 validation (factor-level stratified split on the 5-class label, `random_state=42`). **Note:** the split is at the factor level, not the filing level — see technical report §6.4 for the disclosed limitation.

## Training Procedure

| Parameter | Value |
|---|---|
| Epochs | 3 |
| Steps | 783 |
| Learning rate | 2e-4, cosine schedule, 5% warmup |
| Effective batch size | 16 (2 per-device × 8 grad accumulation) |
| Optimizer | paged AdamW 8-bit |
| Max sequence length | 2048 tokens |
| Quantization | NF4 (double-quant) on base, adapter in bf16 |
| Final training loss | 0.08 (from 1.55 start) |

## Evaluation

**Validation accuracy (1,045-sample held-out Opus-labeled val set):** 73.3%

**Classification metrics on the 18,466-factor pre-registered test set** (gold label = filing's next-period realized-return quintile, a fundamentally different and harder target than the Opus-labeled val set):

| Metric | Base | SFT (this model) |
|---|---|---|
| Macro F1 | 0.160 | 0.174 |
| Quadratic Weighted Kappa (QWK) | 0.017 | 0.027 |

The +1.4 pp F1 gain over base is modest at the sample level; the full portfolio-level story (SFT lifts L/S cohort spread from 2.78% to 4.88% at 21-day horizon) is in the technical report §7.5.

## Usage

### Direct inference via vLLM (recommended)

```bash
vllm serve rroshann/sec-sentiment-sft-deepseek-14b \
  --dtype bfloat16 \
  --gpu-memory-utilization 0.90 \
  --port 8000 \
  --max-model-len 2048
```

Query with any OpenAI-compatible client:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="local")

response = client.chat.completions.create(
    model="rroshann/sec-sentiment-sft-deepseek-14b",
    messages=[{
        "role": "user",
        "content": "Factor: Supply chain pressure from component shortages...\n\nClassify sentiment into one of [very_negative, negative, neutral, positive, very_positive] and return JSON: {label, rationale, confidence}."
    }],
    temperature=0.0,
    max_tokens=512,
)
print(response.choices[0].message.content)
```

See `roshan/Actual_code/task_1/03_factor_extraction.py` and `04_sentiment_scoring.py` in the GitHub repo for the exact system prompts and JSON schemas used to produce the 67,741-factor corpus.

### Direct inference via `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "rroshann/sec-sentiment-sft-deepseek-14b"
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

- **Universe specificity.** Trained on 80 U.S. industrials tickers; will underperform on other sectors (tech, finance, healthcare) where the factor taxonomy is calibrated differently.
- **Single-factor accuracy near chance on return labels.** See Intended Uses. Deploy only with the cohort-aggregation + validity-gate protocol from the technical report.
- **Single-seed training.** No variance estimate across retraining runs; expected val-accuracy drift of ± 0.5 pp on re-runs with a different seed.
- **Factor-level (not filing-level) train/val split.** Factors from the same filing can appear in both splits. Does not affect the downstream test-set metrics because the test set is filing-level and time-ordered (2023–mid-2025), but the 73.3% val accuracy should be read with this in mind.
- **Claude-derived labels.** Training labels reflect Claude Opus's financial-materiality rubric, not a human-panel gold standard. Opus-vs-human agreement was not measured.
- **8-K filings excluded.** Event-driven filings break the 60-question taxonomy; model has not been trained on them.
- **Beta-one signal.** Dollar-neutral portfolios built on this model's predictions have |β| ≈ 2.0 against SPY in backtests — not beta-neutral (see report §13).

## Ethical Considerations

- Training labels were generated via the Anthropic API (Claude Opus). Use of Claude outputs to train a model is permitted under Anthropic's Commercial Terms for non-competing, domain-specific applications; this model is a 5-class sentiment classifier for SEC filings, not a general-purpose assistant.
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

- **Model license:** MIT (matches upstream DeepSeek-R1-Distill-Qwen-14B).
- Upstream base model: DeepSeek-AI, released under MIT. See [`deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) for their model card.
- Training labels generated via the Anthropic API (Claude Opus family).
- Compute provided by Vanderbilt University ACCRE (DGX A100).
- Project advised by Che Guan, Vanderbilt Data Science Institute.

## Companion Model

The `sft_grpo` variant of this model adds a GRPO alignment stage on top of the SFT checkpoint, using a composite ordinal-plus-anti-neutral reward against realized-return-quintile gold labels. It is the stronger variant on the portfolio-level backtest (L/S cohort spread 8.12% at H=21d vs 4.88% for SFT alone; adding a Self-Consistency Best-of-N decoding overlay at inference time gives a variant we label `sft_grpo_bon` at 8.09% — see technical report §9 and §11.3):

→ [`rroshann/sec-sentiment-sftgrpo-deepseek-14b`](https://huggingface.co/rroshann/sec-sentiment-sftgrpo-deepseek-14b)
