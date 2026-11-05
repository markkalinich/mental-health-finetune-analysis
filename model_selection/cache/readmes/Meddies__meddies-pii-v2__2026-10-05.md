---
language:
  - de
  - en
  - es
  - fr
  - id
  - ja
  - ko
  - lo
  - ms
  - my
  - pt
  - ru
  - ta
  - th
  - tl
  - vi
  - zh
license: cc-by-nc-4.0
library_name: transformers
pipeline_tag: token-classification
tags:
  - medical
  - healthcare
  - pii
  - phi
  - de-identification
  - ner
base_model: LiquidAI/LFM2.5-Encoder-350M-PII-Detector
datasets:
  - Meddies/meddies-pii-v2
model-index:
  - name: Meddies/meddies-pii-v2
    results:
      - task:
          type: token-classification
          name: PII extraction
        dataset:
          name: Meddies PII benchmark
          type: Meddies/meddies-pii-v2
        metrics:
          - name: exact typed F1 (micro)
            type: f1
            value: 0.8937
          - name: containment typed F1 (micro)
            type: f1
            value: 0.9429
---

# Meddies PII v2

<p align="left">
  <a href="https://huggingface.co/spaces/Meddies/meddies-pii-extractor"><img alt="Try the browser demo" src="https://img.shields.io/badge/Demo-0F172A?style=flat&logo=googlechrome&logoColor=white"></a>
  <a href="https://huggingface.co/datasets/Meddies/meddies-pii-v2"><img alt="Training dataset" src="https://img.shields.io/badge/Dataset-024C6F?style=flat&logo=huggingface&logoColor=white"></a>
  <a href="https://huggingface.co/Meddies/meddies-pii-v2-onnx"><img alt="ONNX build" src="https://img.shields.io/badge/ONNX-1ABBC7?style=flat&logo=huggingface&logoColor=white"></a>
  <a href="https://creativecommons.org/licenses/by-nc/4.0/"><img alt="CC BY-NC 4.0" src="https://img.shields.io/badge/license-CC--BY--NC--4.0-475569"></a>
</p>

A 350M encoder that finds nine types of personally identifiable information across 17 languages and returns exact character spans for review and redaction.

> [!CAUTION]
> **Keep a human in the loop**
>
> This model can miss identifiers. It cannot certify that text is safe to share. Test it on your documents and keep human review in any regulated workflow.

> [!NOTE]
> **Commercial licensing**
>
> CC BY-NC 4.0 applies to the rights MeddiesAI can license in this release. Contact [contact@meddies.ai](mailto:contact@meddies.ai) about commercial terms for those contributions. The underlying LiquidAI materials remain subject to LFM Open License v1.0.

<p align="center">
  <img src="./assets/hero-meddies-pii-v2.png" alt="Meddies PII v2 detects nine PII entity families across 17 languages and returns exact character spans" width="100%" />
</p>

## Why this model

Clinical records rarely keep identifiers tidy. One note can mix a patient name, hospital ID, phone number, signed portal link, login secret, and a date format that only makes sense locally. Rules catch the obvious cases, then lose ground when the language or document template changes.

Meddies PII v2 handles those cases through one span extraction interface. We built it for clinical text, but its nine labels also cover general documents that need review before release.

## What the model returns

Pass in raw text. The model returns the label, text, start offset, and end offset for every detected span.

- **Nine fixed labels** with `address`, `company_name`, `date`, `email_address`, `human_name`, `id_number`, `phone_number`, `private_url`, and `secret`.
- **Seventeen languages** with German, English, Spanish, French, Indonesian, Japanese, Korean, Lao, Malay, Burmese, Portuguese, Russian, Tamil, Thai, Filipino, Vietnamese, and Chinese.
- **Character offsets included** so every prediction maps back to the source text for review or redaction.
- **Outside the label set** are images, layout, diagnoses, lab results, ages, doses, medical measurements, and public links.

## Quick start

```python
import sys

from huggingface_hub import snapshot_download

path = snapshot_download("Meddies/meddies-pii-v2")
sys.path.insert(0, path)

from modeling_meddies_pii import MeddiesPiiExtractor

model = MeddiesPiiExtractor.from_pretrained(path)
spans = model.extract(
    "Bệnh nhân Nguyễn Văn A, SĐT 0912 345 678, tái khám ngày 12/08/2026."
)

for span in spans:
    print(span.label, span.start, span.end, span.text)
```

Expected output

```text
human_name 10 22 Nguyễn Văn A
phone_number 28 40 0912 345 678
date 56 66 12/08/2026
```

### Choose the weight form

| Form | Load | Parity check | Use it when |
| --- | --- | ---: | --- |
| Adapter | `from_pretrained(path)` | 0 of 200 rows differed | You need the evaluated execution path. |
| Merged | `from_pretrained(path, weights="merged")` | 14 of 200 rows differed | You need one self-contained weight file and can accept the measured delta. |

Merging folds the adapter into the base weights and changes the numerical path. Borderline BIOES decisions can move. Use the adapter when exact release reproduction matters.

### ONNX and local browser use

The [ONNX companion](https://huggingface.co/Meddies/meddies-pii-v2-onnx) packages the same checkpoint for ONNX Runtime and WebGPU. Its full precision graph matched the PyTorch adapter on all 200 parity rows. The current int8 graph differed on 12 of 200 rows.

The [browser demo](https://huggingface.co/spaces/Meddies/meddies-pii-extractor) runs on the user's device. Raw clinical text never leaves the device.

## Evaluation

Meddies PII v2 reached **0.8937 exact typed micro F1** and **0.9429 containment typed micro F1** on 263,785 benchmark rows. It had the highest exact typed F1 in all 17 evaluation cells, all 17 language slices, and all nine entity families against the six reference systems in this comparison.

<p align="center">
  <img src="./assets/evaluation-meddies-pii-v2.png" alt="Meddies PII v2 evaluation snapshot with overall, comparative, entity, and language results" width="100%" />
</p>

Exact typed F1 requires the label and both character boundaries to match. Containment typed F1 accepts a correct label when one span contains the other. Each macro average gives the same weight to the unit named in the column.

| Model | Evaluation cell macro F1 | Language macro F1 | Entity family macro F1 |
| --- | ---: | ---: | ---: |
| **Meddies PII v2** | **0.833** | **0.852** | **0.907** |
| [OpenAI Privacy Filter](https://huggingface.co/openai/privacy-filter) | 0.644 | 0.592 | 0.673 |
| [Meddies PII v1](https://huggingface.co/Meddies/meddies-pii) | 0.602 | 0.574 | 0.676 |
| [GLiNER2](https://huggingface.co/fastino/gliner2-privacy-filter-PII-multi) | 0.581 | 0.539 | 0.682 |
| [OpenMed PII](https://huggingface.co/OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1) | 0.538 | 0.439 | 0.617 |
| [LFM2.5 PII Detector](https://huggingface.co/LiquidAI/LFM2.5-Encoder-350M-PII-Detector) | 0.536 | 0.446 | 0.552 |

<details>
<summary>Exact typed F1 in all 17 evaluation cells</summary>

The v2 preview is the earlier 150-step checkpoint that preceded this release.

| Evaluation cell | Meddies v2 | GLiNER2 | v2 preview | Meddies v1 | OpenMed | OpenAI PF | LFM2.5 PII |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `ai4privacy_de` | **0.827** | 0.663 | 0.664 | 0.616 | 0.620 | 0.716 | 0.610 |
| `ai4privacy_en` | **0.878** | 0.687 | 0.673 | 0.667 | 0.656 | 0.745 | 0.568 |
| `ai4privacy_es` | **0.870** | 0.732 | 0.725 | 0.649 | 0.683 | 0.794 | 0.655 |
| `ai4privacy_fil` | **0.848** | 0.690 | 0.590 | 0.606 | 0.584 | 0.667 | 0.600 |
| `ai4privacy_fr` | **0.844** | 0.674 | 0.679 | 0.618 | 0.604 | 0.738 | 0.611 |
| `ai4privacy_id` | **0.848** | 0.688 | 0.601 | 0.588 | 0.566 | 0.664 | 0.627 |
| `ai4privacy_ja` | **0.750** | 0.366 | 0.499 | 0.659 | 0.493 | 0.549 | 0.479 |
| `ai4privacy_ko` | **0.739** | 0.322 | 0.523 | 0.611 | 0.545 | 0.554 | 0.460 |
| `ai4privacy_ms` | **0.839** | 0.692 | 0.586 | 0.598 | 0.547 | 0.640 | 0.587 |
| `ai4privacy_pt` | **0.855** | 0.692 | 0.691 | 0.643 | 0.687 | 0.756 | 0.651 |
| `ai4privacy_vi` | **0.880** | 0.628 | 0.615 | 0.644 | 0.499 | 0.634 | 0.615 |
| `ai4privacy_zh` | **0.816** | 0.453 | 0.600 | 0.643 | 0.428 | 0.572 | 0.548 |
| `creddata_en` | **0.590** | 0.357 | 0.226 | 0.035 | 0.150 | 0.370 | 0.263 |
| `gretel_en` | **0.872** | 0.588 | 0.734 | 0.743 | 0.715 | 0.697 | 0.729 |
| `nemotron_en` | **0.956** | 0.692 | 0.792 | 0.837 | 0.878 | 0.778 | 0.574 |
| `v2-eval` | **0.863** | 0.478 | 0.504 | 0.525 | 0.260 | 0.523 | 0.277 |
| `v2-eval-challenge` | **0.893** | 0.473 | 0.568 | 0.551 | 0.228 | 0.557 | 0.260 |
| **Macro average** | **0.833** | 0.581 | 0.604 | 0.602 | 0.538 | 0.644 | 0.536 |

</details>

<details>
<summary>Exact and containment F1 by entity family</summary>

| Entity family | Exact F1 | Containment F1 |
| --- | ---: | ---: |
| `address` | 0.681 | 0.866 |
| `company_name` | 0.939 | 0.946 |
| `date` | 0.957 | 0.961 |
| `email_address` | 0.984 | 0.990 |
| `human_name` | 0.917 | 0.951 |
| `id_number` | 0.954 | 0.958 |
| `phone_number` | 0.919 | 0.951 |
| `private_url` | 0.902 | 0.925 |
| `secret` | 0.913 | 0.936 |

</details>

The benchmark combines synthetic and public corpora. A strong benchmark score does not tell you how the model behaves inside one hospital. Evaluate it on local document types before deployment.

## How it was built

We adapted [LiquidAI LFM2.5 Encoder 350M PII Detector](https://huggingface.co/LiquidAI/LFM2.5-Encoder-350M-PII-Detector) with rank 128 Low-Rank Adaptation and a 37-tag BIOES classification head.

Training used the [Meddies PII v2 dataset](https://huggingface.co/datasets/Meddies/meddies-pii-v2) and external public corpora rebuilt from their original sources. We do not rehost those external corpora. Checkpoint selection used a pinned control set before the full benchmark. The complete recipe and release checks live in [`TRAINING.md`](./TRAINING.md).

## Where it fits

- Review before redaction for clinical notes, referrals, messages, and exported records.
- Span extraction inside a de-identification workflow that keeps the source text visible to a reviewer.
- Multilingual evaluation and domain adaptation for local document formats.

## Limits

- Postal addresses reached 0.681 exact F1 and 0.866 containment F1. Expect trimmed or extended boundaries.
- The label set is closed. An unsupported identifier will not receive its own label.
- Hospital templates, abbreviations, copied headers, and optical character recognition errors vary by site.
- Synthetic and public benchmark data cannot establish performance on every patient population or production system.
- Inputs designed to evade detection can still break the model.

## License

MeddiesAI applies [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) to the copyright and related rights it can license in this release. See [`LICENSE`](./LICENSE).

The underlying LiquidAI materials remain under [LFM Open License v1.0](./LICENSE-LFM-OPEN-V1.0). Upstream attribution and the MeddiesAI change record are preserved in [`NOTICE`](./NOTICE). Review both licenses before redistribution.

## Feedback

Found a bad miss or a wrong boundary? Share the language, document type, expected span, predicted span, and whether optical character recognition was involved. Use a safe synthetic example. Never post real patient text or credentials in a public issue.

Open a thread in the Community tab or email [contact@meddies.ai](mailto:contact@meddies.ai).

## Collaboration

We are looking for hospitals, research groups, and privacy teams that can contribute de-identified failure cases, independent evaluations, or review in underrepresented languages. Email [contact@meddies.ai](mailto:contact@meddies.ai) to work with us.

## Citation

```bibtex
@misc{meddies-pii-v2,
  title={Meddies PII v2 for multilingual clinical de-identification},
  author={MeddiesAI},
  year={2026},
  url={https://huggingface.co/Meddies/meddies-pii-v2}
}
```
