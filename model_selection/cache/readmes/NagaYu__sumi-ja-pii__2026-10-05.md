---
license: apache-2.0
language:
- ja
library_name: transformers
pipeline_tag: token-classification
tags:
- pii
- privacy
- japanese
- token-classification
- named-entity-recognition
- presidio
- onnx
base_model: sbintuitions/modernbert-ja-130m
datasets:
- NagaYu/sumi-ja-pii-corpus
widget:
- text: "田中太郎様よりご連絡をいただきました。連絡先は090-1234-5678、tanaka.taro@example.co.jp です。"
- text: "森の中を歩いていると、林業の振興について泉が湧くように話が広がった。長野県の気候は寒暖差が大きい。"
---

# 墨 Sumi — Japanese PII detection (0.13B, CPU)

A small Japanese PII token classifier that is trained specifically on the confusions
English-first tools get wrong: surnames that are also common nouns (森 / 林 / 泉 /
大和 / 青木), place and company homographs, honorific boundaries, and digit strings
that merely look like phone numbers.

Pairs with a rule layer for format-determined types and a reversible masking path,
so masked text can be sent to an external LLM and the response restored.

> [!WARNING]
> **Sumi does not guarantee legal or regulatory compliance.** It is a tool for
> *reducing the risk* of personal data leaving your machine — not a complete
> detector. Misses will happen. You choose the threshold and the use case.
> All training and evaluation data is synthetic; **no real personal
> information is used anywhere in this project.**

- **Code, benchmarks and training pipeline:** https://github.com/NagaYu/sumi
- **Dataset:** https://huggingface.co/datasets/NagaYu/sumi-ja-pii-corpus
- **Base model:** [`sbintuitions/modernbert-ja-130m`](https://huggingface.co/sbintuitions/modernbert-ja-130m) (MIT)
- **Parameters:** 132M (0.13B)
- **Labels:** 21 BIO classes over 10 PII types

## Detected types

| Label | Meaning |
|---|---|
| `NAME` | Name (氏名) |
| `ADDRESS` | Address (住所) |
| `PHONE` | Phone (電話番号) |
| `EMAIL` | Email (メールアドレス) |
| `DOB` | Birth date (生年月日) |
| `BANK_ACCOUNT` | Bank acct (金融口座) |
| `CREDIT_CARD` | Card (カード番号) |
| `MYNUMBER` | My Number (マイナンバー様式) |
| `MEMBER_ID` | Member ID (会員番号) |
| `POSTAL_CODE` | Postal (郵便番号) |

## Usage

The recommended entry point is the `sumi` package, which combines this model with
the rule layer and the calibrator:

```bash
pip install "sumi[presidio,onnx] @ git+https://github.com/NagaYu/sumi.git"
```

```python
from sumi import SumiDetector

det = SumiDetector("NagaYu/sumi-ja-pii")          # or a local directory
for span in det.detect("田中太郎様の連絡先は090-1234-5678です。"):
    print(span.label.value, span.text, round(span.score, 3))
# NAME 田中太郎 0.997
# PHONE 090-1234-5678 0.95
```

Reversible masking, with the mapping kept locally:

```python
masked, mapping = det.redact(text)   # '<NAME_1>様の連絡先は<PHONE_1>です。'
original = ReversibleMasker().unmask(llm_response, mapping)
```

Inside Presidio:

```python
from presidio_analyzer import RecognizerRegistry
from sumi.presidio_plugin import register
register(registry)
```

### Raw transformers

The model is a standard `ModernBertForTokenClassification`. If you use it directly
you lose the rule layer, the calibration and the boundary refinement, which is where
a good deal of the precision comes from:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tok = AutoTokenizer.from_pretrained("NagaYu/sumi-ja-pii")
model = AutoModelForTokenClassification.from_pretrained("NagaYu/sumi-ja-pii")
```

## Evaluation

Measured against four alternatives on identical documents, same CPU, same thread
count, each condition in its own process:

- **(A)** Presidio, default English configuration
- **(B)** Presidio + GiNZA, carefully mapped (not a straw man)
- **(C)** Qwen3-4B-Instruct Q4_K_M via llama.cpp, CPU only, prompted
- **(D)** Sumi fp32, **(E)** Sumi ONNX INT8

### Generalisation set (100 positive / 100 negative documents)

Synthetic PII inserted into Wikipedia / statute / literary prose — **no business
document templates**, so this is the number that reflects real generalisation
rather than template memorisation.

| Condition | Name | Address | Phone | Birth date | Email | Bank acct | My Number | Member ID | micro F1  FP rate |
|---|---|---|---|---|---|---|---|---|---|---|
| (A) Presidio, default | 0.054 | 0.000 | 0.917 | 0.053 | 0.192 | 0.000 | 0.000 | 0.000 | 0.176 | 0.370 |
| (B) Presidio + GiNZA | 0.784 | 0.077 | 0.833 | 0.789 | 0.231 | 0.000 | 0.000 | 0.024 | 0.245 | 0.830 |
| (C) Local LLM 4B (Q4) | 0.541 | 0.897 | 0.917 | 0.947 | 1.000 | 0.683 | 0.676 | 0.659 | 0.818 | 0.080 |
| (D) Sumi fp32 | 0.811 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.978 | 0.000 |
| (E) Sumi INT8 | 0.811 | 0.923 | 1.000 | 0.895 | 1.000 | 1.000 | 1.000 | 1.000 | 0.953 | 0.060 |

![Name and address recall on the template-independent set](fig1_name_detection_ood.png)

![False-positive rate on confusable negatives](fig3_false_positives_ood.png)

![Model size versus accuracy](fig2_size_vs_accuracy_ood.png)

The "FP rate" column is the fraction of hard-negative documents (which contain **no**
PII at all) where the system fired at least once.

### CPU throughput and memory

| Condition | Size | docs/s | ms/doc | Peak RSS (MB) | vs (C) |
|---|---|---|---|---|---|
| (A) Presidio, default | 0.01B | 253.93 | 4 | 1231 | **1825×** |
| (B) Presidio + GiNZA | 0.05B | 6.05 | 165 | 1414 | **43×** |
| (C) Local LLM 4B (Q4) | 4.00B | 0.14 | 7187 | 5974 | baseline |
| (D) Sumi fp32 | 0.13B | 12.05 | 83 | 1192 | **87×** |
| (E) Sumi INT8 | 0.13B | 22.54 | 44 | 1000 | **162×** |

## Files

| File | What it is |
|---|---|
| `model.safetensors` | fp32 PyTorch weights |
| `model.onnx` | ONNX fp32 |
| `model.int8.onnx` | ONNX dynamic INT8 — 133 MB, argmax agreement 1.0000 |
| `calibrator.json` | temperature scaling fitted on held-out spans |
| `sumi_labels.json` | label order — keeps ONNX and PyTorch in sync |
| `negatives_weights.json` | closed-loop weights: which confusion types the model still gets wrong |
| `mlx/` | MLX weights for Apple Silicon |
| `gguf/` | GGUF export, **weights only, not executable** (see limitations) |

## Training

- 12,000 synthetic documents, 107k gold spans; 2 epochs, batch 32, max length 256
- AdamW, linear warmup and decay, gradient clipping at 1.0
- Checkpoint selected on validation **span** exact-match F1, not token F1
- Span probability = minimum over constituent token probabilities

## Intended use and limitations

Intended for reducing the chance that Japanese personal data reaches an external
system — for example masking documents before sending them to a hosted LLM.

## Limitations

- **On personal names alone, Sumi's lead is small.** On the template-independent set Sumi reaches 0.81 against 0.78 for Presidio + GiNZA. Sumi's advantage is not name recall in isolation — it is addresses, the ID/number families, and above all the false-positive rate.
- **Trained and evaluated entirely on synthetic data.** Behaviour on your real
  documents will differ. Validate on your own data before deploying.
- **Misses are certain.** Lowering the threshold raises recall and also raises false
  positives; the trade-off table above is the honest picture of that.
- **Sumi is not a compliance control.** It reduces risk; it does not certify anything.
- **GGUF is exported but not executable** — no mainstream runtime currently runs
  ModernBERT-style token classification from GGUF. Use ONNX INT8 on CPU.
- **Japanese proofreading / typo detection is deliberately out of scope** (JWTD and
  existing public models already cover that).
- The rule layer requires context words for My Number and member IDs. A bare
  12-digit string with no surrounding cue is intentionally not flagged, to keep the
  false-positive rate low.
- Source code docstrings are written in Japanese (the project's working language);
  all published documentation is in English.

## Citation

```bibtex
@software{sumi2026,
  title  = {Sumi: Japanese PII detection that holds up on hard negatives},
  author = {Sumi contributors},
  year   = {2026},
  url    = {https://github.com/NagaYu/sumi}
}
```
