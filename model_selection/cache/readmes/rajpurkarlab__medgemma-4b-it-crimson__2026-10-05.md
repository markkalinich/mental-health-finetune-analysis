---
license: other
license_name: health-ai-developer-foundations
license_link: https://developers.google.com/health-ai-developer-foundations/terms
base_model: google/medgemma-4b-it
library_name: transformers
tags:
  - medical
  - radiology
  - medgemma
  - crimson
datasets:
  - rajpurkarlab/ReXGradient-160K
pipeline_tag: text-generation
---

# MedGemma-4B-IT Fine-tuned for CRIMSON Scoring

This model is a fine-tuned version of [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it), fully fine-tuned on the
training set of [ReXGradient-160K](https://huggingface.co/datasets/rajpurkarlab/ReXGradient-160K) for **radiology report evaluation with
CRIMSON scoring**.

## Model Details

- **Base Model:** google/medgemma-4b-it
- **Fine-tuning Method:** LoRA (merged into base model)
- **Language:** English
- **Domain:** Medical / Radiology
- **Task:** Radiology report generation evaluation

## Intended Use

This model is designed **for CRIMSON scoring** — evaluating the quality of AI-generated radiology reports by comparing
them against ground truth reports and identifying errors (false findings, missing findings, attribute errors).

## Installation & Usage

### 1. Install RadGame-MedGemma

```bash
git clone https://github.com/MohammedSB/RadGame-MedGemma
cd RadGame-MedGemma
pip install -e .
```

### 2. Use with CRIMSON

```python
from CRIMSON.CRIMSON.generate_score import CRIMSONScore

# Initialize scorer with the finetuned model
scorer = CRIMSONScore(model_name="CRIMSONScore/medgemma-4b-it-crimson")

# Evaluate a candidate report against ground truth
result = scorer.evaluate(
    reference_findings="No acute cardiopulmonary abnormality. Heart size is normal.",
    predicted_findings="No acute cardiopulmonary abnormality. Mild cardiomegaly.",
    patient_context={"age": "65", "indication": "chest pain"},
    include_guidelines=False,
)

print(f"CRIMSON Score: {result['crimson_score']}")
print(f"Error counts: {result['error_counts']}")
```

## Training Data Generation

The training data was generated using a multi-regime candidate generation pipeline designed to create diverse (ground truth,
candidate) pairs with varying types of errors.

### Regimes

The pipeline samples from 6 regimes with equal probability:

| Regime | Type    | Description |
|--------|---------|-------------|
| **0**  | Non-LLM | **Random Report**: Substitutes a randomly selected report from a different study |
| **1**  | Non-LLM | **Similar Report**: Substitutes a semantically similar report using BERT embeddings (all-MiniLM-L6-v2) and cosine similarity, selecting from the top-5 most similar reports |
| **2**  | LLM     | **Perfect Rewrite**: Rewrites the report to sound different while preserving exact clinical meaning |
| **3**  | LLM     | **False Finding Injection**: Rewrites and introduces fabricated positive findings (e.g., new pathology, device, anatomical abnormality) |
| **4**  | LLM     | **Attribute Error**: Rewrites and introduces attribute errors on existing findings (location/laterality, severity, morphology, measurements, certainty, temporal changes) |
| **5**  | LLM     | **Omission Error**: Rewrites and omits clinically significant positive findings |

For LLM-based regimes (3, 4, 5), up to 2 error types can be combined in a single candidate (e.g., a report with both a false finding
and an attribute error).

### Scoring Pipeline

Each (ground truth, candidate) pair was scored using CRIMSONScore (using Azure OpenAI GPT-5) to generate structured training labels including error
analysis, CRIMSON scores, and significance-weighted error counts.

### Patient Context Augmentation

Patient context (age, sex, indication) was included with 80% probability per field during training.

## Training Details

### Dataset

- Dataset: https://huggingface.co/datasets/rajpurkarlab/ReXGradient-160K

### Hardware

- 8x NVIDIA H100 80GB HBM3

### Hyperparameters

| Parameter                    | Value |
|------------------------------|-------|
| Epochs                       | 10    |
| Batch size (per device)      | 4     |
| Gradient accumulation steps  | 2     |
| Effective batch size         | 32    |
| Learning rate                | 1e-4  |
| Warmup ratio                 | 0.05  |
| Weight decay                 | 0.05  |
| Max sequence length          | 4048  |
| Seed                         | 42    |

### LoRA Configuration

| Parameter      | Value |
|----------------|-------|
| LoRA rank (r)  | 16    |
| LoRA alpha     | 32    |
| LoRA dropout   | 0.05  |

## Limitations

- Research use only — not validated for clinical decision-making
- Designed specifically for CRIMSON scoring; not a general-purpose radiology model

## Citation

If you use this model, please cite:

```bibtex
@article{sellergren2025medgemma,
  title={Medgemma technical report},
  author={Sellergren, Andrew and Kazemzadeh, Sahar and Jaroensri, Tiam and Kiraly, Atilla and Traverse, Madeleine and Kohlberger, Timo and Xu, Shawn and Jamil, Fayaz and Hughes, C{\'\i}an and Lau, Charles and others},
  journal={arXiv preprint arXiv:2507.05201},
  year={2025}
}

@article{zhang2025rexgradient,
  title={Rexgradient-160k: A large-scale publicly available dataset of chest radiographs with free-text reports},
  author={Zhang, Xiaoman and Acosta, Juli{\'a}n N and Miller, Josh and Huang, Ouwen and Rajpurkar, Pranav},
  journal={arXiv preprint arXiv:2505.00228},
  year={2025}
}

```

## License

This model is subject to:

https://developers.google.com/health-ai-developer-foundations/terms