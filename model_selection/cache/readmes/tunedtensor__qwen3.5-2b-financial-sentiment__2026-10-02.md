---
license: apache-2.0
base_model: Qwen/Qwen3.5-2B
datasets:
- zeroshot/twitter-financial-news-sentiment
library_name: transformers
pipeline_tag: text-generation
tags:
- tuned-tensor
- finance
- sentiment-analysis
- financial-sentiment
- json
- qwen3_5
---

# Qwen3.5-2B Financial Sentiment Extractor

This model is a Tuned Tensor fine-tune of `Qwen/Qwen3.5-2B` for extracting a structured market sentiment signal from finance-related tweets and social posts.

Given one post, it returns compact JSON:

```json
{"sentiment":"bearish","label":0,"rationale":"The post expresses a bearish market signal."}
```

Label mapping:

- `0`: bearish
- `1`: bullish
- `2`: neutral

## Training

- Base model: `Qwen/Qwen3.5-2B`
- Training dataset: `zeroshot/twitter-financial-news-sentiment`
- Dataset license: MIT
- Base model license: Apache-2.0
- Tuned Tensor run ID: `61d64e3e-b9a1-48e5-8803-c7c30a4df5a8`
- Tuned Tensor model ID: `fd09ae23-1935-48b4-b838-9e563df59b49`
- Training rows used by trainer: `4,080`
- Precision: `bf16`
- Epochs: `1`
- Final reported training loss: `0.5898758276`

The source dataset was converted into strict `input` / `output` supervised rows with balanced labels. The behavior spec used during training is included as `tunedtensor.json`.

## Evaluation

Tuned Tensor LLM-judge evaluation, capped at 120 examples per split:

| Split | Base avg score | Tuned avg score | Delta | Base pass rate | Tuned pass rate | Delta |
|---|---:|---:|---:|---:|---:|---:|
| Validation | 0.819 | 0.903 | +0.084 | 79.2% | 86.7% | +7.5 pp |
| Test | 0.834 | 0.875 | +0.041 | 80.0% | 85.8% | +5.8 pp |

Output format diagnostics:

- Valid JSON: 100%
- Strict JSON: 100%
- Expected schema keys: 100%
- Non-JSON prefix: 0%

Local hand-curated smoke tests are included:

- `local_real_tests_fd09ae23.json`
- `local_real_tests_fd09ae23_batch2.json`

## Usage

The model was locally served and tested with Tuned Tensor's OpenAI-compatible serving runtime:

```bash
tt models serve fd09ae23-1935-48b4-b838-9e563df59b49 \
  --spec tunedtensor.json \
  --device auto \
  --temperature 0 \
  --max-tokens 96
```

Example prompt:

```text
Extract the market sentiment signal from this finance-related social post. Return only strict JSON with exactly these keys: sentiment, label, rationale. sentiment must be one of bearish, bullish, neutral; label must be one of 0, 1, 2.

Post: $NVDA shares jump after analysts raise price targets on stronger AI chip demand.
```

Expected response shape:

```json
{"sentiment":"bullish","label":1,"rationale":"The post expresses a bullish market signal."}
```

## Limitations

This model classifies short market-social posts into coarse sentiment categories. It is not an investment advisor, trading system, or factual market-data source.

Known caveat from evaluation: some ambiguous mixed-signal posts may still be difficult, especially when a post contains both a clearly negative primary event and a secondary contrarian or factual framing.
