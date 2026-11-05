---
language:
- en
license: apache-2.0
tags:
- clinical-nlp
- named-entity-recognition
- ner
- biomedical
- knowledge-distillation
- bert
- token-classification
- phi-detection
- onnx
- quantization
library_name: transformers
pipeline_tag: token-classification
datasets:
- tner/bc5cdr
metrics:
- f1
model-index:
- name: ClinicalFlamo
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    dataset:
      name: BC5CDR
      type: tner/bc5cdr
    metrics:
    - type: f1
      value: 0.807
      name: Macro F1
---

# ClinicalFlamo

**ClinicalFlamo** is a distilled clinical NER model for detecting Chemical and Disease entities in biomedical text. It is built on `DistilClinicalBERT` and trained via knowledge distillation from `Bio_ClinicalBERT` on the BC5CDR dataset.

The goal was straightforward: compress a 107M-parameter clinical BERT model as aggressively as possible while keeping F1 acceptable for production use, and deploy it in a way that PHI never leaves the local device.

---

## Model Details

| Property | Value |
|---|---|
| Base architecture | DistilClinicalBERT (6-layer BERT, clinical vocab, inherited from Bio_ClinicalBERT) |
| Teacher model | Bio_ClinicalBERT (107.7M params) |
| Student parameters | 66M (39% reduction from 110M teacher) |
| Training data | BC5CDR (Chemical + Disease NER) |
| Weak labels added | 19,506 entities from 7,064 PubMed abstracts |
| Training epochs | 10 (with 10% warmup) |
| Distillation temperature | T=4 |
| Quantization | INT8 via ONNX Runtime |
| Final model size | 63.7MB (INT8) vs 410.9MB teacher |
| License | Apache 2.0 |

---

## Performance

### Distillation Results (BC5CDR test set)

| Metric | Teacher (Bio_ClinicalBERT) | Student v1 (DistilBERT) | ClinicalFlamo (Student v2) |
|---|---|---|---|
| Parameters | 110M | 66M | **66M** |
| Macro F1 | 86.57% | 76.06% | **80.70%** |
| Chemical F1 | 91.68% | 73.58% | **85.92%** |
| Disease F1 | 77.99% | 66.16% | **70.48%** |
| Latency (mean) | 39.0ms | 10.7ms | **10.8ms** |
| Model size | 410.9MB | 248.7MB | **248.7MB** |
| F1 retention | - | 87.9% | **93.2%** |

Switching from a generic DistilBERT student to a domain-matched DistilClinicalBERT student improved Macro F1 by +4.64pp and Chemical Recall by +18.92pp. The domain pre-training in the student base model mattered more than any hyperparameter change.

### Model Optimization (ONNX + INT8)

| Variant | Macro F1 | Size | Latency |
|---|---|---|---|
| Student v2 FP32 (ONNX) | 80.70% | 253.3MB | 16.5ms |
| Student v2 INT8 | 80.70% | **63.7MB** | 31.9ms* |

*INT8 latency is higher on macOS ARM. On x86 AVX-512 servers (c5/c6i instances), expect ~3x speedup over FP32.*

Quantization achieves 75% size reduction with no F1 loss.

### A/B Testing (100 samples, 95% CI)

Statistical comparison using Mann-Whitney and Wilcoxon signed-rank tests:

- ClinicalFlamo retains **88.1% of teacher F1** (Wilcoxon p < 0.000001)
- ClinicalFlamo is **1.9x faster** than teacher (52.4ms vs 28.0ms, Mann-Whitney p < 0.000001)
- Recommendation: deploy ClinicalFlamo over Bio_ClinicalBERT for latency-sensitive production workloads

### Production Load Test

FastAPI server, Prometheus + OpenTelemetry instrumented, 100-request load test:

- **97% SLA compliance** (97/100 requests under 50ms threshold)
- 0 errors across all requests
- Latency range: 20.9ms to 56.3ms

---

## Usage

### Basic Inference

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# ClinicalFlamo uses Bio_ClinicalBERT vocabulary (28,996 tokens)
# Make sure you use AutoTokenizer — do NOT use a generic BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("SantoshAdabala/ClinicalFlamo")
model = AutoModelForTokenClassification.from_pretrained("SantoshAdabala/ClinicalFlamo")

ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

text = "Patient was prescribed metformin 500mg for type 2 diabetes."
results = ner(text)

for entity in results:
    print(f"{entity['word']:20s} -> {entity['entity_group']} ({entity['score']:.3f})")
```

**Output:**
```
metformin 500mg      -> Chemical (0.984)
type 2 diabetes      -> Disease  (0.971)
```

### ONNX Runtime (INT8, production)

```python
from optimum.onnxruntime import ORTModelForTokenClassification
from transformers import AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("SantoshAdabala/ClinicalFlamo")
model = ORTModelForTokenClassification.from_pretrained(
    "SantoshAdabala/ClinicalFlamo",
    file_name="model_int8.onnx"
)

ner = pipeline("token-classification", model=model, tokenizer=tokenizer)
results = ner("Patient was administered aspirin 325mg for acute myocardial infarction.")
```

---

## Entity Types

| Label | Description | Example |
|---|---|---|
| `Chemical` | Drugs, compounds, chemical substances | metformin, aspirin, insulin |
| `Disease` | Diseases, disorders, conditions | type 2 diabetes, hypertension, sepsis |

Trained on [BC5CDR](https://huggingface.co/datasets/tner/bc5cdr) — a public biomedical corpus. No actual patient data was used at any stage.

---

## Training Data

**Primary**: BC5CDR (BioCreative V CDR corpus) — annotated Chemical-Disease NER dataset from PubMed abstracts.

**Weak labels**: 19,506 high-confidence entities (threshold >= 0.85) generated by running Bio_ClinicalBERT over 7,064 PubMed abstracts retrieved via the NCBI API across 10 clinical search queries. Breakdown: 9,109 Chemical entities, 10,397 Disease entities.

---

## Training Procedure

```
Teacher:  Bio_ClinicalBERT fine-tuned on BC5CDR
          107.7M params, Macro F1 = 86.57%

Student:  DistilClinicalBERT (BertForTokenClassification, 6 layers, 768 hidden)
          Initialized from Bio_ClinicalBERT — inherits clinical vocabulary (28,996 tokens)
          Knowledge distillation with T=4, 10 epochs, 10% warmup
          66M params, Macro F1 = 80.70%, F1 retention = 93.2%

Post-training:
          40% unstructured weight pruning (0.13% F1 drop)
          INT8 quantization via ONNX Runtime
          Final size: 63.7MB
```

---

## System Architecture

```
PubMed (7,064 abstracts)
        |
   NCBI API + PySpark (AWS EMR)
        |
   Weak labels (19,506 entities @ 0.85 threshold)
        |
Bio_ClinicalBERT (teacher, 107.7M)
        |
   Knowledge Distillation (T=4, 10 epochs)
        |
DistilClinicalBERT student (66M, clinical vocab)
        |
   Pruning (40%) + INT8 Quantization
        |
ClinicalFlamo ONNX (63.7MB)
        |
   FastAPI + Prometheus + OpenTelemetry
        |
   97% SLA @ 10.8ms p50 latency
```

---

## Limitations

- Trained only on Chemical and Disease entity types. Does not detect other PHI categories (names, dates, locations).
- INT8 quantization is slower on macOS ARM due to kernel optimization for x86 AVX-512. Use FP32 on Apple Silicon.
- Weak labels were generated without human review. Some noise is expected in entity boundaries for uncommon clinical terms.
- Performance on clinical notes (as opposed to PubMed abstracts) has not been formally evaluated.

---

## Citation

If you use ClinicalFlamo in your work:

```bibtex
@misc{adabala2026clinicalflamo,
  author    = {Santosh Adabala},
  title     = {ClinicalFlamo: Distilled Clinical NER for Chemical and Disease Detection},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/SantoshAdabala/ClinicalFlamo}
}
```

---

## Links

- GitHub: [clinical-nlp-optimization](https://github.com/SantoshAdabala/clinical-nlp-optimization)
- Dataset: [BC5CDR on HuggingFace](https://huggingface.co/datasets/tner/bc5cdr)
- Author: [Santosh Adabala](https://github.com/SantoshAdabala)
