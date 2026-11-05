---
library_name: transformers
pipeline_tag: token-classification
language:
- en
- hi
license: other
license_name: lfm-open-license-v1.0
base_model: LiquidAI/LFM2.5-Encoder-350M-PII-Detector
tags:
- pii
- privacy
- token-classification
- hinglish
- devanagari
- onnx
- int8
---

# LFM2.5 PII — English, Hindi, and Hinglish (FP32 + ONNX INT8)

Fine-tuned version of [`LiquidAI/LFM2.5-Encoder-350M-PII-Detector`](https://huggingface.co/LiquidAI/LFM2.5-Encoder-350M-PII-Detector) for high-recall PII detection in English, Romanized Hinglish, and Devanagari Hindi.

This repository contains:

- the original fine-tuned PyTorch FP32 model (`model.safetensors`);
- tokenizer, configuration, and custom Transformers model code;
- a CPU-oriented dynamically quantized ONNX INT8 export under `onnx-q8/`.

## Evaluation

The following results are from a 900-record synthetic post-training holdout with 600 positive records and 300 hard negatives. Span matching uses overlap matching plus the same deterministic boundary/rule post-processing for every format.

| Format | Precision | Recall | F1 | Character coverage | Residual entities | Hard negatives flagged | CPU throughput | Peak RSS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Original LiquidAI base, ONNX FP32 | 0.6863 | 0.6783 | 0.6823 | 0.8101 | 166/600 | 87/300 | 36.0 records/s | 3.54 GB |
| Fine-tuned model, ONNX FP32 | 0.7896 | 0.8817 | 0.8331 | 0.9309 | 57/600 | 70/300 | 37.8 records/s | 3.49 GB |
| Fine-tuned model, ONNX INT8 | 0.7741 | 0.8850 | 0.8258 | 0.9240 | 62/600 | 81/300 | 46.9 records/s | 2.00 GB |

The original-base row evaluates the untouched upstream model revision shown below, exported to FP32 ONNX with the same graph exporter and scored with the same decoding and post-processing. The fine-tuned FP32 ONNX export had exact token-argmax parity with the uploaded PyTorch weights in prior parity checks.

Contextual person-name recall was 1.0000 for FP32 and 0.9900 for INT8 on this holdout.

## Loading the original Transformers model

The repository includes custom model code inherited from the base architecture, so loading requires `trust_remote_code=True`.

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer

repo = "erayyapagci/lfm2.5-pii-en-hi-hinglish-q8"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForTokenClassification.from_pretrained(
    repo,
    trust_remote_code=True,
)
```

Review remote model code before enabling `trust_remote_code` in a sensitive environment.

## Loading ONNX INT8 on CPU

```python
import onnxruntime as ort
from transformers import AutoTokenizer

repo = "erayyapagci/lfm2.5-pii-en-hi-hinglish-q8"
tokenizer = AutoTokenizer.from_pretrained(repo)
session = ort.InferenceSession(
    "onnx-q8/model.int8.onnx",
    providers=["CPUExecutionProvider"],
)
```

Token logits require BIOES decoding and tokenizer offset mapping to recover text spans. Evaluation also used deterministic boundary repair and structured-PII rules; raw token argmax alone will not reproduce the table exactly.

## Intended use and limitations

This is an experimental PII detector, not a complete security boundary. Test it on manually reviewed data from your own domain before use. In the holdout it performed well on names, addresses, dates, emails, phones, and URLs, but remained weak on flexible grouped account numbers and previously unseen arbitrary secret formats. Quantization can change borderline predictions. Use fail-closed handling for sensitive exports and consider deterministic recognizers for structured identifiers.

The training mixture used local synthetic data and permissively licensed/synthetic external sources, including NVIDIA Nemotron PII, Gretel synthetic PII, and AI4Privacy-derived data. Do not infer that the model is suitable for every locale, demographic, or regulatory context.

## Base model and license

Base model revision: `b8c9cf3d2d6ae52501b35a27ba46f271449c9ce2`.

The model is distributed under the **LFM Open License v1.0**. See [`LICENSE`](LICENSE) and the [base model repository](https://huggingface.co/LiquidAI/LFM2.5-Encoder-350M-PII-Detector).
